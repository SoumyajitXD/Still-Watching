#!/usr/bin/env python3
"""Repository quality checks for the Still Watching modpack docs repo.

The checks intentionally target this repository's maintenance surface: docs,
metadata, release-facing HTML, links, workflow safety, and hygiene. They do not
try to build Minecraft, Forge, Java, Gradle, Maven, npm, or Python packages.
"""
from __future__ import annotations

import argparse
import html.parser
import json
import re
import stat
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[2]
METADATA_PATH = Path(".github/ci/project-metadata.json")
WORKFLOW_PATH = Path(".github/workflows/ci.yml")

REQUIRED_FILES = [
    Path("README.md"),
    Path("CONTRIBUTING.md"),
    Path("SUPPORT.md"),
    Path("SECURITY.md"),
    Path("installation-guide.md"),
    Path("latest-modlist.md"),
    Path("curseforge-description.html"),
    Path("LICENSE"),
    WORKFLOW_PATH,
]

METADATA_TARGETS = [
    Path("README.md"),
    Path("installation-guide.md"),
    Path("SUPPORT.md"),
    Path("CONTRIBUTING.md"),
    Path("curseforge-description.html"),
    Path("latest-modlist.md"),
]

TEXT_EXTENSIONS = {
    ".css",
    ".editorconfig",
    ".gitattributes",
    ".gitignore",
    ".html",
    ".json",
    ".md",
    ".py",
    ".toml",
    ".txt",
    ".yml",
    ".yaml",
}

LARGE_FILE_LIMIT = 5 * 1024 * 1024
LARGE_FILE_ALLOWLIST_PREFIXES = ("Screenshots/", "Releases/")
LARGE_FILE_ALLOWLIST_NAMES = {"still-watching-logo.jpg", "bisecthosting-banner.png"}

SECRET_PATTERNS = [
    ("AWS access key", re.compile(r"AKIA[0-9A-Z]{16}")),
    ("GitHub token", re.compile(r"gh[pousr]_[A-Za-z0-9_]{36,}")),
    ("Slack token", re.compile(r"xox[baprs]-[A-Za-z0-9-]{10,}")),
    ("Private key", re.compile(r"-----BEGIN (?:RSA |DSA |EC |OPENSSH |)PRIVATE KEY-----")),
]

CONFLICT_MARKERS = ("<<<<<<< ", "=======", ">>>>>>> ")
PLACEHOLDER_RE = re.compile(r"\b(?:TODO|FIXME|TBD|LOREM IPSUM|INSERT|PLACEHOLDER)\b", re.IGNORECASE)
MARKDOWN_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
HTML_ATTR_RE = re.compile(r"\b(?:href|src)=[\"']([^\"']+)[\"']", re.IGNORECASE)
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")
ACTION_USES_RE = re.compile(r"^\s*uses:\s*([^\s#]+)", re.MULTILINE)
JOB_LINE_RE = re.compile(r"^  ([A-Za-z0-9_-]+):\s*$")

EXTERNAL_LINK_SOFT_FAIL_HOSTS = {
    # CurseForge and shields are public, rate-limited, and occasionally block CI user agents.
    "www.curseforge.com",
    "curseforge.com",
    "img.shields.io",
    "url-shortener.curseforge.com",
    "media.forgecdn.net",
}

ALLOWED_MARKETPLACE_ACTIONS = {
    "actions/checkout@de0fac2e4500dabe0009e67214ff5f5447ce83dd",
}


@dataclass
class Reporter:
    errors: int = 0
    warnings: int = 0

    def error(self, path: Path | str, message: str, line: int | None = None) -> None:
        self.errors += 1
        location = f"file={path}"
        if line is not None:
            location += f",line={line}"
        print(f"::error {location}::{message}")

    def warning(self, path: Path | str, message: str, line: int | None = None) -> None:
        self.warnings += 1
        location = f"file={path}"
        if line is not None:
            location += f",line={line}"
        print(f"::warning {location}::{message}")

    def group(self, name: str) -> None:
        print(f"::group::{name}")

    def endgroup(self) -> None:
        print("::endgroup::")


def rel(path: Path) -> Path:
    try:
        return path.relative_to(ROOT)
    except ValueError:
        return path


def read_text(path: Path) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def load_metadata() -> dict[str, str]:
    return json.loads(read_text(METADATA_PATH))


def git_files() -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files", "-z"],
        cwd=ROOT,
        check=True,
        stdout=subprocess.PIPE,
    )
    return [Path(p.decode()) for p in result.stdout.split(b"\0") if p]


def is_text_file(path: Path) -> bool:
    return path.suffix.lower() in TEXT_EXTENSIONS or path.name in {"LICENSE"}


def normalize_for_metadata(text: str) -> str:
    return (
        text.replace("&ndash;", "–")
        .replace("&#8211;", "–")
        .replace("&mdash;", "—")
        .replace("&nbsp;", " ")
        .replace("5GB", "5 GB")
        .replace("6–8GB", "6–8 GB")
        .replace("6-8 GB", "6–8 GB")
    )


def check_baseline(reporter: Reporter) -> None:
    reporter.group("Required files and docs")
    for path in REQUIRED_FILES + [METADATA_PATH]:
        full = ROOT / path
        if not full.is_file():
            reporter.error(path, "Missing required repository file")
        elif full.stat().st_size == 0:
            reporter.error(path, "Required repository file is empty")
    reporter.endgroup()

    reporter.group("Required directories and README targets")
    for path in [Path("Screenshots"), Path("Releases"), Path(".github/ISSUE_TEMPLATE")]:
        if not (ROOT / path).is_dir():
            reporter.error(path, "Missing required directory referenced by README")
    readme = read_text(Path("README.md")) if (ROOT / "README.md").is_file() else ""
    if "./docs/server-pack-guide.md" in readme and not (ROOT / "docs/server-pack-guide.md").is_file():
        reporter.error("docs/server-pack-guide.md", "README links to the server-pack guide, but the file is missing")
    if "./.github/ISSUE_TEMPLATE" in readme and not (ROOT / ".github/ISSUE_TEMPLATE").is_dir():
        reporter.error(".github/ISSUE_TEMPLATE", "README links to issue templates, but the directory is missing")
    if "./CHANGELOG.md" in readme and not (ROOT / "CHANGELOG.md").is_file():
        reporter.error("CHANGELOG.md", "README links to CHANGELOG.md, but the file is missing")
    reporter.endgroup()

    reporter.group("Workflow inventory and legacy helper scripts")
    workflows = sorted(Path(".github/workflows").glob("*")) if (ROOT / ".github/workflows").is_dir() else []
    for path in workflows:
        if path != WORKFLOW_PATH:
            reporter.error(path, "Only .github/workflows/ci.yml is intentionally allowed in this repo")
    legacy_scripts = ROOT / ".github/scripts"
    if legacy_scripts.exists():
        for path in sorted(legacy_scripts.rglob("*")):
            reporter.error(rel(path), "Legacy .github/scripts helpers are blocked; maintained checks live under .github/ci/")
    for path in [Path("README.md"), Path("CONTRIBUTING.md"), Path("SUPPORT.md"), Path("SECURITY.md"), Path("installation-guide.md")]:
        if not (ROOT / path).is_file():
            continue
        text = read_text(path)
        if ".github/scripts/" in text or ".github/scripts/validate" in text or ".github/scripts/generate" in text:
            reporter.error(path, "Dead reference to deleted legacy helper scripts; use .github/ci/ commands")
    reporter.endgroup()


def check_metadata(reporter: Reporter) -> None:
    metadata = load_metadata()
    labels = {
        "project_name": "project name",
        "minecraft_version": "Minecraft version",
        "loader": "loader",
        "java_version": "Java version",
        "curseforge_project_id": "CurseForge project ID",
        "current_documented_release": "current documented release",
        "minimum_ram": "minimum RAM",
        "preferred_ram": "preferred RAM",
    }
    reporter.group("Metadata source of truth")
    missing = [key for key in labels if not metadata.get(key)]
    for key in missing:
        reporter.error(METADATA_PATH, f"Missing metadata key: {key}")
    reporter.endgroup()

    reporter.group("Metadata consistency")
    for path in METADATA_TARGETS:
        if not (ROOT / path).is_file():
            reporter.error(path, "Cannot validate metadata because file is missing")
            continue
        text = normalize_for_metadata(read_text(path))
        for key, label in labels.items():
            value = metadata[key]
            candidate_values = [value]
            if key == "current_documented_release" and value.startswith("Still Watching "):
                candidate_values.append(value.removeprefix("Still Watching "))
            if key == "java_version":
                candidate_values.extend([f"Java {value}", f"Java `{value}`"])
            if key == "minimum_ram":
                candidate_values.append(value.replace(" ", ""))
            if key == "preferred_ram":
                candidate_values.append(value.replace(" ", ""))
            if not any(candidate in text for candidate in candidate_values):
                reporter.error(path, f"Missing metadata value for {label}: {value}")
    reporter.endgroup()


def check_html(reporter: Reporter) -> None:
    path = Path("curseforge-description.html")
    if not (ROOT / path).is_file():
        reporter.error(path, "Missing CurseForge description HTML")
        return
    text = read_text(path)
    norm = normalize_for_metadata(text)
    metadata = load_metadata()
    reporter.group("CurseForge HTML sanity")
    required = [
        (metadata["project_name"], "project name"),
        (metadata["current_documented_release"], "current documented release"),
        (metadata["minecraft_version"], "Minecraft version"),
        (metadata["loader"], "loader"),
        ("url-shortener.curseforge.com", "CurseForge sponsor shortener URL"),
    ]
    for needle, label in required:
        if needle not in norm:
            reporter.error(path, f"Missing required HTML content: {label}")
    for match in PLACEHOLDER_RE.finditer(text):
        reporter.error(path, f"Placeholder text remains: {match.group(0)}")
    for match in re.finditer(r"<img\b[^>]*\bsrc=[\"']([^\"']+)[\"']", text, re.IGNORECASE):
        src = match.group(1)
        if src.startswith("http://"):
            reporter.error(path, f"Inline image URL must use HTTPS: {src}")
    parser = html.parser.HTMLParser(convert_charrefs=True)
    try:
        parser.feed(text)
        parser.close()
    except Exception as exc:  # pragma: no cover - html.parser is forgiving, but keep annotation useful.
        reporter.error(path, f"HTML parser rejected the description: {exc}")
    reporter.endgroup()


def check_modlist(reporter: Reporter) -> None:
    path = Path("latest-modlist.md")
    if not (ROOT / path).is_file():
        reporter.error(path, "Missing latest modlist")
        return
    text = read_text(path)
    lines = text.splitlines()
    metadata = load_metadata()
    reporter.group("Modlist structure")
    if not lines or lines[0].strip() != "# Modlist":
        reporter.error(path, "latest-modlist.md must start with '# Modlist'", 1)
    if metadata["current_documented_release"] not in text:
        reporter.error(path, "Modlist does not include the current documented release")
    try:
        header_index = next(i for i, line in enumerate(lines) if line.strip().lower() == "| name | curseforge |")
    except StopIteration:
        reporter.error(path, "Missing Markdown table header '| Name | Curseforge |'")
        reporter.endgroup()
        return
    separator_index = header_index + 1
    if separator_index >= len(lines) or not re.match(r"^\|\s*:?-{3,}:?\s*\|\s*:?-{3,}:?\s*\|$", lines[separator_index].strip()):
        reporter.error(path, "Modlist table separator is malformed", separator_index + 1)
    names: dict[str, int] = {}
    row_count = 0
    for index, line in enumerate(lines[separator_index + 1 :], start=separator_index + 2):
        if not line.strip():
            break
        if not line.startswith("|"):
            reporter.error(path, "Modlist row is not a Markdown table row", index)
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != 2:
            reporter.error(path, "Every modlist row must have exactly two columns", index)
            continue
        name, link_cell = cells
        if not name:
            reporter.error(path, "Mod row has an empty mod name", index)
        normalized_name = re.sub(r"\s+", " ", name.lower())
        if normalized_name in names:
            reporter.error(path, f"Duplicate mod name also appears on line {names[normalized_name]}", index)
        else:
            names[normalized_name] = index
        url_match = re.search(r"\((https://www\.curseforge\.com/[^)]+)\)", link_cell)
        if not url_match:
            reporter.error(path, "Mod row must contain a CurseForge HTTPS URL", index)
        elif not url_match.group(1).startswith("https://www.curseforge.com/"):
            reporter.error(path, "CurseForge link must start with https://www.curseforge.com/", index)
        lower_name = name.lower()
        url = url_match.group(1).lower() if url_match else ""
        if "fabric" in lower_name and "forge" not in lower_name and "forge" not in url:
            reporter.warning(path, "Mod name mentions Fabric without an obvious Forge-compatible title or URL; verify loader support", index)
        if "neoforge" in lower_name and "forge" not in url:
            reporter.warning(path, "Mod name mentions NeoForge; verify this entry still supports the Forge target", index)
        row_count += 1
    if row_count == 0:
        reporter.error(path, "Modlist table has no mod rows")
    reporter.endgroup()


def slugify_heading(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"[`*_~]", "", text).strip().lower()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    return text.replace(" ", "-").strip("-")


def collect_headings(path: Path) -> set[str]:
    anchors: set[str] = set()
    seen: dict[str, int] = {}
    for line in read_text(path).splitlines():
        match = HEADING_RE.match(line)
        if not match:
            continue
        base = slugify_heading(match.group(2))
        count = seen.get(base, 0)
        seen[base] = count + 1
        anchors.add(base if count == 0 else f"{base}-{count}")
    return anchors


def extract_links(path: Path) -> Iterable[tuple[int, str]]:
    text = read_text(path)
    for lineno, line in enumerate(text.splitlines(), start=1):
        for regex in [MARKDOWN_LINK_RE, HTML_ATTR_RE]:
            for match in regex.finditer(line):
                target = match.group(1).strip()
                if target and not target.startswith("#"):
                    yield lineno, target


def resolve_internal_link(source: Path, target: str) -> tuple[Path, str]:
    target = target.split()[0]
    target = target.strip("<>")
    parsed = urllib.parse.urlparse(target)
    raw_path = urllib.parse.unquote(parsed.path)
    anchor = urllib.parse.unquote(parsed.fragment)
    if raw_path in ("", "."):
        destination = source
    else:
        destination = (ROOT / source).parent / raw_path
    return destination.resolve(), anchor


def is_external(target: str) -> bool:
    scheme = urllib.parse.urlparse(target).scheme.lower()
    return scheme in {"http", "https"}


def should_skip_link(target: str) -> bool:
    return target.startswith(("mailto:", "tel:", "javascript:")) or "img.shields.io" in target


def check_external_link(reporter: Reporter, source: Path, line: int, target: str) -> None:
    parsed = urllib.parse.urlparse(target)
    request = urllib.request.Request(
        target,
        method="HEAD",
        headers={"User-Agent": "Still-Watching-CI/1.0 (+https://github.com/SoumyajitXD/Still-Watching)"},
    )
    try:
        with urllib.request.urlopen(request, timeout=12) as response:
            status_code = response.getcode()
    except urllib.error.HTTPError as exc:
        # Some servers reject HEAD but accept GET.
        if exc.code in {405, 403}:
            try:
                get_request = urllib.request.Request(
                    target,
                    method="GET",
                    headers={"User-Agent": "Still-Watching-CI/1.0 (+https://github.com/SoumyajitXD/Still-Watching)"},
                )
                with urllib.request.urlopen(get_request, timeout=12) as response:
                    status_code = response.getcode()
            except Exception as get_exc:
                if parsed.hostname in EXTERNAL_LINK_SOFT_FAIL_HOSTS:
                    reporter.warning(source, f"External link could not be verified due host blocking/rate limit: {target} ({get_exc})", line)
                    return
                reporter.error(source, f"External link failed: {target} ({get_exc})", line)
                return
        elif parsed.hostname in EXTERNAL_LINK_SOFT_FAIL_HOSTS and exc.code in {401, 403, 429, 500, 502, 503, 504}:
            reporter.warning(source, f"External link returned tolerated flaky status {exc.code}: {target}", line)
            return
        else:
            reporter.error(source, f"External link returned HTTP {exc.code}: {target}", line)
            return
    except Exception as exc:
        reporter.warning(source, f"External link could not be verified due network/host blocking: {target} ({exc})", line)
        return
    if status_code >= 400:
        reporter.error(source, f"External link returned HTTP {status_code}: {target}", line)


def check_links(reporter: Reporter, external: bool = False) -> None:
    files = [Path("README.md"), Path("installation-guide.md"), Path("SUPPORT.md"), Path("SECURITY.md"), Path("CONTRIBUTING.md"), Path("latest-modlist.md"), Path("curseforge-description.html")]
    reporter.group("Internal and external links" if external else "Internal links")
    for source in files:
        if not (ROOT / source).is_file():
            reporter.error(source, "Cannot check links because the file is missing")
            continue
        for line, target in extract_links(source):
            if should_skip_link(target):
                continue
            if is_external(target):
                if external:
                    check_external_link(reporter, source, line, target)
                continue
            destination, anchor = resolve_internal_link(source, target)
            try:
                relative_destination = destination.relative_to(ROOT)
            except ValueError:
                reporter.error(source, f"Internal link escapes repository: {target}", line)
                continue
            if not destination.exists():
                reporter.error(source, f"Broken internal link target: {target}", line)
                continue
            if anchor and destination.is_file() and destination.suffix.lower() == ".md":
                anchors = collect_headings(relative_destination)
                if anchor not in anchors:
                    reporter.error(source, f"Broken Markdown heading anchor '#{anchor}' in {target}", line)
    reporter.endgroup()


def check_hygiene(reporter: Reporter) -> None:
    reporter.group("Git whitespace")
    diff = subprocess.run(["git", "diff", "--check"], cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if diff.returncode != 0:
        for line in diff.stdout.splitlines():
            reporter.error("git diff --check", line)
    reporter.endgroup()

    reporter.group("Repository hygiene")
    for path in git_files():
        full = ROOT / path
        name = path.name
        posix = path.as_posix()
        if name in {".DS_Store", "Thumbs.db"} or name.endswith(("~", ".bak", ".orig", ".rej")):
            reporter.error(path, "Forbidden junk/editor backup file is committed")
        size = full.stat().st_size
        if size > LARGE_FILE_LIMIT and not posix.startswith(LARGE_FILE_ALLOWLIST_PREFIXES) and name not in LARGE_FILE_ALLOWLIST_NAMES:
            reporter.error(path, f"File is larger than {LARGE_FILE_LIMIT // (1024 * 1024)} MiB and is not an allowed asset/release file")
        mode = full.stat().st_mode
        if mode & stat.S_IXUSR and full.suffix.lower() not in {".sh"} and full.name != "validate_repository.py":
            reporter.error(path, "Unexpected executable bit on non-script file")
        if is_text_file(path):
            text = full.read_text(encoding="utf-8", errors="replace")
            for index, line in enumerate(text.splitlines(), start=1):
                if any(line.startswith(marker) for marker in CONFLICT_MARKERS):
                    reporter.error(path, "Unresolved merge conflict marker", index)
            for label, pattern in SECRET_PATTERNS:
                for match in pattern.finditer(text):
                    line = text.count("\n", 0, match.start()) + 1
                    reporter.error(path, f"Possible committed secret: {label}", line)
    reporter.endgroup()


def check_workflow(reporter: Reporter) -> None:
    if not (ROOT / WORKFLOW_PATH).is_file():
        reporter.error(WORKFLOW_PATH, "Missing workflow")
        return
    text = read_text(WORKFLOW_PATH)
    reporter.group("Workflow security policy")
    if not re.search(r"^permissions:\n\s+contents:\s+read\s*$", text, re.MULTILINE):
        reporter.error(WORKFLOW_PATH, "Workflow must declare minimal top-level permissions: contents: read")
    if re.search(r"^\s+pull_request_target:\s*$", text, re.MULTILINE):
        reporter.error(WORKFLOW_PATH, "Use pull_request, not pull_request_target, for this untrusted docs CI")
    if not re.search(r"^concurrency:\s*$", text, re.MULTILINE) or "cancel-in-progress: true" not in text:
        reporter.error(WORKFLOW_PATH, "Workflow must use concurrency cancellation")
    if re.search(r"contents:\s+write|pull-requests:\s+write|actions:\s+write|id-token:\s+write", text):
        reporter.error(WORKFLOW_PATH, "Workflow grants write permissions that this CI does not need")
    for match in ACTION_USES_RE.finditer(text):
        action = match.group(1)
        line = text.count("\n", 0, match.start()) + 1
        if action.startswith("./"):
            continue
        if action not in ALLOWED_MARKETPLACE_ACTIONS:
            reporter.error(WORKFLOW_PATH, f"Marketplace action is not pinned to an approved immutable SHA: {action}", line)
    lines = text.splitlines()
    job_lines = [(i + 1, m.group(1)) for i, line in enumerate(lines) if (m := JOB_LINE_RE.match(line))]
    # Limit to lines after jobs: and ignore maps nested below known job keys by checking two-space indent only.
    job_lines = [(line, name) for line, name in job_lines if line > next((i + 1 for i, l in enumerate(lines) if l == "jobs:"), 0)]
    for idx, (line_no, job_name) in enumerate(job_lines):
        next_line = job_lines[idx + 1][0] if idx + 1 < len(job_lines) else len(lines) + 1
        block = "\n".join(lines[line_no - 1 : next_line - 1])
        if "timeout-minutes:" not in block:
            reporter.error(WORKFLOW_PATH, f"Job '{job_name}' is missing timeout-minutes", line_no)
    if "set -euo pipefail" not in text:
        reporter.error(WORKFLOW_PATH, "Bash steps must use set -euo pipefail")
    reporter.endgroup()


def run_checks(check_names: list[str], external_links: bool) -> Reporter:
    reporter = Reporter()
    checks = {
        "baseline": check_baseline,
        "metadata": check_metadata,
        "html": check_html,
        "modlist": check_modlist,
        "links": lambda r: check_links(r, external=external_links),
        "hygiene": check_hygiene,
        "workflow": check_workflow,
    }
    selected = list(checks) if "all" in check_names else check_names
    for name in selected:
        checks[name](reporter)
    print(f"Validation finished with {reporter.errors} error(s) and {reporter.warnings} warning(s).")
    return reporter


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Still Watching repository quality gates.")
    parser.add_argument("checks", nargs="*", default=["all"], choices=["all", "baseline", "metadata", "html", "modlist", "links", "hygiene", "workflow"])
    parser.add_argument("--external-links", action="store_true", help="Also probe external HTTP(S) links; flaky CurseForge-like hosts warn instead of failing on rate limits.")
    args = parser.parse_args()
    reporter = run_checks(args.checks, args.external_links)
    return 1 if reporter.errors else 0


if __name__ == "__main__":
    sys.exit(main())
