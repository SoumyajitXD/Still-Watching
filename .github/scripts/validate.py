#!/usr/bin/env python3
"""Repository CI guard for Still Watching.

This intentionally checks repository invariants without depending on files that may
not exist in lightweight documentation-only releases. It fails loudly, with useful
messages, and leaves generation/editing to maintainers.
"""
from __future__ import annotations

import argparse
import html.parser
import json
import re
import sys
import zipfile
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[2]
DOC_FILES = [
    "README.md",
    "CONTRIBUTING.md",
    "installation-guide.md",
    "latest-modlist.md",
    "curseforge-description.html",
]
REQUIRED_PATHS = DOC_FILES + ["LICENSE", ".github/workflows/ci.yml", ".github/workflows/link-check.yml"]
CURSEFORGE_HOST = "www.curseforge.com"
CURSEFORGE_KINDS = {"mc-mods", "modpacks", "shaders", "texture-packs"}
SPONSOR_URL = "https://url-shortener.curseforge.com/AZDOs"
BASELINE_FACTS = {
    "project name": re.compile(r"\bStill\s+Watching\b", re.I),
    "minecraft version": re.compile(r"\b1\.20\.1\b"),
    "loader": re.compile(r"\bForge\b", re.I),
    "curseforge project id": re.compile(r"\b1420406\b"),
}

try:
    import yaml  # type: ignore
except Exception:  # pragma: no cover - CI installs PyYAML.
    yaml = None


class HtmlSmokeParser(html.parser.HTMLParser):
    pass


def fail(errors: list[str]) -> None:
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    raise SystemExit(1)


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig", errors="replace")


def existing_doc_paths() -> list[Path]:
    return [ROOT / path for path in DOC_FILES if (ROOT / path).is_file()]


def check_layout() -> None:
    errors = [f"missing required path: {path}" for path in REQUIRED_PATHS if not (ROOT / path).exists()]
    for directory in [".github", ".github/workflows", ".github/scripts"]:
        if not (ROOT / directory).is_dir():
            errors.append(f"missing required directory: {directory}")
    if errors:
        fail(errors)
    print("layout: ok")


def check_yaml() -> None:
    if yaml is None:
        fail(["PyYAML is not installed; run `python -m pip install PyYAML`"])
    errors: list[str] = []
    for path in sorted((ROOT / ".github").glob("**/*.yml")) + sorted((ROOT / ".github").glob("**/*.yaml")):
        try:
            data = yaml.safe_load(read(path))
            if data is None:
                errors.append(f"{rel(path)} is empty")
            if ".github/workflows" in path.as_posix():
                validate_workflow_shape(path, data, errors)
        except Exception as exc:
            errors.append(f"{rel(path)}: invalid YAML: {exc}")
    if errors:
        fail(errors)
    print("yaml: ok")


def validate_workflow_shape(path: Path, data: object, errors: list[str]) -> None:
    if not isinstance(data, dict):
        errors.append(f"{rel(path)} must be a mapping")
        return
    if not data.get("name"):
        errors.append(f"{rel(path)} missing workflow name")
    if not data.get(True) and not data.get("on"):
        # YAML 1.1 parsers can load the key `on` as boolean True. Yes, cursed.
        errors.append(f"{rel(path)} missing trigger block")
    jobs = data.get("jobs")
    if not isinstance(jobs, dict) or not jobs:
        errors.append(f"{rel(path)} missing jobs")
    if data.get("permissions") != {"contents": "read"}:
        errors.append(f"{rel(path)} should use least-privilege permissions: contents: read")


def check_text_hygiene() -> None:
    errors: list[str] = []
    for path in existing_doc_paths() + sorted((ROOT / ".github").glob("**/*")):
        if path.is_file() and path.suffix.lower() in {".md", ".html", ".yml", ".yaml", ".py"}:
            text = read(path)
            if not text.strip():
                errors.append(f"{rel(path)} is empty")
            if "\r\n" in text:
                errors.append(f"{rel(path)} uses CRLF line endings")
            if not text.endswith("\n"):
                errors.append(f"{rel(path)} must end with a newline")
            for number, line in enumerate(text.splitlines(), 1):
                if line.rstrip() != line:
                    errors.append(f"{rel(path)}:{number} has trailing whitespace")
                    break
    if errors:
        fail(errors)
    print("text hygiene: ok")


def check_html() -> None:
    errors: list[str] = []
    for path in sorted(ROOT.glob("*.html")):
        try:
            parser = HtmlSmokeParser()
            parser.feed(read(path))
            parser.close()
        except Exception as exc:
            errors.append(f"{rel(path)}: HTML parse failed: {exc}")
    if errors:
        fail(errors)
    print("html smoke: ok")


def markdown_links(text: str) -> list[tuple[str, int]]:
    pattern = re.compile(r"(?<!!)(?:\[[^\]\n]+\]|<[^>\n]+>)\(([^)\n]+)\)")
    return [(match.group(1).strip(), text.count("\n", 0, match.start(1)) + 1) for match in pattern.finditer(text)]


def html_links(text: str) -> list[tuple[str, int]]:
    pattern = re.compile(r'''\b(?:href|src)=["']([^"']+)["']''', re.I)
    return [(match.group(1).strip(), text.count("\n", 0, match.start(1)) + 1) for match in pattern.finditer(text)]


def check_local_links() -> None:
    errors: list[str] = []
    for path in existing_doc_paths():
        text = read(path)
        links = markdown_links(text)
        if path.suffix.lower() == ".html":
            links += html_links(text)
        for href, line_number in links:
            if not href or href.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = href.split("#", 1)[0].split("?", 1)[0]
            if not target:
                continue
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f"{rel(path)}:{line_number} link escapes repository: {href}")
                continue
            if not resolved.exists():
                errors.append(f"{rel(path)}:{line_number} broken local link: {href}")
    if errors:
        fail(errors)
    print("local links: ok")


def check_curseforge_links() -> None:
    errors: list[str] = []
    for path in existing_doc_paths():
        text = read(path)
        links = markdown_links(text) + html_links(text)
        for href, line_number in links:
            parsed = urlparse(href)
            if parsed.netloc != CURSEFORGE_HOST:
                continue
            parts = [part for part in parsed.path.split("/") if part]
            if len(parts) < 3 or parts[0] != "minecraft" or parts[1] not in CURSEFORGE_KINDS:
                errors.append(f"{rel(path)}:{line_number} suspicious CurseForge URL: {href}")
    modlist = ROOT / "latest-modlist.md"
    if modlist.exists():
        mod_links = [href for href, _line in markdown_links(read(modlist)) if urlparse(href).netloc == CURSEFORGE_HOST]
        if len(mod_links) < 40:
            errors.append(f"latest-modlist.md should contain at least 40 CurseForge entries, found {len(mod_links)}")
        for href, count in Counter(mod_links).items():
            if count > 1:
                errors.append(f"latest-modlist.md duplicate CurseForge link: {href}")
    if errors:
        fail(errors)
    print("curseforge links: ok")


def check_release_facts() -> None:
    errors: list[str] = []
    fact_paths = [ROOT / name for name in ["README.md", "installation-guide.md", "latest-modlist.md", "curseforge-description.html"] if (ROOT / name).exists()]
    for path in fact_paths:
        text = read(path)
        for label, regex in BASELINE_FACTS.items():
            if not regex.search(text):
                errors.append(f"{rel(path)} missing baseline fact: {label}")
    versions: dict[str, list[str]] = {}
    version_regex = re.compile(r"\bStill\s+Watching\s+V(\d+\.\d+\.\d+)\b", re.I)
    for path in existing_doc_paths():
        for version in version_regex.findall(read(path)):
            versions.setdefault(version, []).append(rel(path))
    if len(versions) > 1:
        errors.append("conflicting documented release versions: " + json.dumps(versions, sort_keys=True))
    if errors:
        fail(errors)
    print("release facts: ok")


def check_sponsor() -> None:
    errors: list[str] = []
    readme = ROOT / "README.md"
    description = ROOT / "curseforge-description.html"
    if readme.exists() and SPONSOR_URL not in read(readme):
        errors.append("README.md missing BisectHosting sponsor URL")
    if description.exists() and SPONSOR_URL not in read(description):
        errors.append("curseforge-description.html missing BisectHosting sponsor URL")
    if errors:
        fail(errors)
    print("sponsor guard: ok")


def check_release_archives() -> None:
    errors: list[str] = []
    release_dir = ROOT / "Releases"
    if not release_dir.exists():
        print("release archives: skipped (no Releases directory)")
        return
    for archive in sorted(release_dir.glob("*.zip")):
        try:
            with zipfile.ZipFile(archive) as zf:
                bad = zf.testzip()
                if bad:
                    errors.append(f"{rel(archive)} corrupt entry: {bad}")
                if not zf.infolist():
                    errors.append(f"{rel(archive)} is empty")
        except zipfile.BadZipFile as exc:
            errors.append(f"{rel(archive)} is not a valid zip: {exc}")
    if errors:
        fail(errors)
    print("release archives: ok")


def run_all() -> None:
    for check in [
        check_layout,
        check_yaml,
        check_text_hygiene,
        check_html,
        check_local_links,
        check_curseforge_links,
        check_release_facts,
        check_sponsor,
        check_release_archives,
    ]:
        check()


def main() -> None:
    checks = {
        "all": run_all,
        "layout": check_layout,
        "yaml": check_yaml,
        "text": check_text_hygiene,
        "html": check_html,
        "links": check_local_links,
        "curseforge": check_curseforge_links,
        "facts": check_release_facts,
        "sponsor": check_sponsor,
        "archives": check_release_archives,
    }
    parser = argparse.ArgumentParser(description="Validate Still Watching repository health.")
    parser.add_argument("check", nargs="?", default="all", choices=checks)
    args = parser.parse_args()
    checks[args.check]()


if __name__ == "__main__":
    main()
