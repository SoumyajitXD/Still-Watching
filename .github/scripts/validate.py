#!/usr/bin/env python3
"""CI guardrails for the Still Watching repository."""
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
DOCS = ["README.md", "CONTRIBUTING.md", "installation-guide.md", "latest-modlist.md", "curseforge-description.html"]
REQUIRED = DOCS + ["LICENSE", ".github/workflows/ci.yml", ".github/workflows/link-check.yml"]
SPONSOR_URL = "https://url-shortener.curseforge.com/AZDOs"
CURSEFORGE_KINDS = {"mc-mods", "modpacks", "shaders", "texture-packs"}

try:
    import yaml  # type: ignore
except Exception:
    yaml = None


def die(errors: list[str]) -> None:
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    raise SystemExit(1)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig", errors="replace")


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def docs() -> list[Path]:
    return [ROOT / name for name in DOCS if (ROOT / name).is_file()]


def check_layout() -> None:
    errors = [f"missing required path: {path}" for path in REQUIRED if not (ROOT / path).exists()]
    for directory in [".github", ".github/scripts", ".github/workflows"]:
        if not (ROOT / directory).is_dir():
            errors.append(f"missing required directory: {directory}")
    if errors:
        die(errors)
    print("layout: ok")


def check_yaml() -> None:
    if yaml is None:
        die(["PyYAML is required"])
    errors: list[str] = []
    for path in sorted((ROOT / ".github").glob("**/*.yml")) + sorted((ROOT / ".github").glob("**/*.yaml")):
        try:
            data = yaml.safe_load(read(path))
        except Exception as exc:
            errors.append(f"{rel(path)} invalid YAML: {exc}")
            continue
        if data is None:
            errors.append(f"{rel(path)} is empty")
        if ".github/workflows" in path.as_posix():
            if not isinstance(data, dict):
                errors.append(f"{rel(path)} must be a mapping")
                continue
            if not data.get("name"):
                errors.append(f"{rel(path)} missing name")
            if not data.get(True) and not data.get("on"):
                errors.append(f"{rel(path)} missing on trigger")
            if not isinstance(data.get("jobs"), dict):
                errors.append(f"{rel(path)} missing jobs")
            if data.get("permissions") != {"contents": "read"}:
                errors.append(f"{rel(path)} must use permissions: contents: read")
    if errors:
        die(errors)
    print("yaml: ok")


def check_text() -> None:
    errors: list[str] = []
    paths = docs() + [p for p in sorted((ROOT / ".github").glob("**/*")) if p.is_file()]
    for path in paths:
        if path.suffix.lower() not in {".md", ".html", ".yml", ".yaml", ".py"}:
            continue
        text = read(path)
        if not text.strip():
            errors.append(f"{rel(path)} is empty")
        if "\r\n" in text:
            errors.append(f"{rel(path)} uses CRLF line endings")
        if not text.endswith("\n"):
            errors.append(f"{rel(path)} must end with newline")
        for number, line in enumerate(text.splitlines(), 1):
            if line.rstrip() != line:
                errors.append(f"{rel(path)}:{number} has trailing whitespace")
                break
    if errors:
        die(errors)
    print("text: ok")


def md_links(text: str) -> list[tuple[str, int]]:
    pattern = re.compile(r"(?<!!)(?:\[[^\]\n]+\]|<[^>\n]+>)\(([^)\n]+)\)")
    return [(m.group(1).strip(), text.count("\n", 0, m.start(1)) + 1) for m in pattern.finditer(text)]


def html_links(text: str) -> list[tuple[str, int]]:
    pattern = re.compile(r'''\b(?:href|src)=["']([^"']+)["']''', re.I)
    return [(m.group(1).strip(), text.count("\n", 0, m.start(1)) + 1) for m in pattern.finditer(text)]


def check_html() -> None:
    errors: list[str] = []
    for path in ROOT.glob("*.html"):
        try:
            parser = html.parser.HTMLParser()
            parser.feed(read(path))
            parser.close()
        except Exception as exc:
            errors.append(f"{rel(path)} failed HTML smoke parse: {exc}")
    if errors:
        die(errors)
    print("html: ok")


def check_links() -> None:
    errors: list[str] = []
    for path in docs():
        links = md_links(read(path)) + (html_links(read(path)) if path.suffix == ".html" else [])
        for href, line in links:
            if not href or href.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = href.split("#", 1)[0].split("?", 1)[0]
            if not target:
                continue
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f"{rel(path)}:{line} link escapes repository: {href}")
                continue
            if not resolved.exists():
                errors.append(f"{rel(path)}:{line} broken local link: {href}")
    if errors:
        die(errors)
    print("local links: ok")


def check_curseforge() -> None:
    errors: list[str] = []
    modlist = ROOT / "latest-modlist.md"
    mod_links: list[str] = []
    for path in docs():
        for href, line in md_links(read(path)) + html_links(read(path)):
            parsed = urlparse(href)
            if parsed.netloc != "www.curseforge.com":
                continue
            parts = [p for p in parsed.path.split("/") if p]
            if len(parts) < 3 or parts[0] != "minecraft" or parts[1] not in CURSEFORGE_KINDS:
                errors.append(f"{rel(path)}:{line} suspicious CurseForge URL: {href}")
            if path == modlist:
                mod_links.append(href)
    if modlist.exists() and len(mod_links) < 40:
        errors.append(f"latest-modlist.md has only {len(mod_links)} CurseForge links")
    errors += [f"latest-modlist.md duplicate CurseForge link: {href}" for href, count in Counter(mod_links).items() if count > 1]
    if errors:
        die(errors)
    print("curseforge: ok")


def check_facts() -> None:
    errors: list[str] = []
    readme = ROOT / "README.md"
    if readme.exists():
        text = read(readme)
        required = {
            "Still Watching": r"\bStill\s+Watching\b",
            "Minecraft 1.20.1": r"\b1\.20\.1\b",
            "Forge": r"\bForge\b",
            "CurseForge project ID 1420406": r"\b1420406\b",
        }
        for label, pattern in required.items():
            if not re.search(pattern, text, re.I):
                errors.append(f"README.md missing {label}")
    versions: dict[str, list[str]] = {}
    for path in docs():
        for version in re.findall(r"\bStill\s+Watching\s+V(\d+\.\d+\.\d+)\b", read(path), re.I):
            versions.setdefault(version, []).append(rel(path))
    if len(versions) > 1:
        errors.append("conflicting documented release versions: " + json.dumps(versions, sort_keys=True))
    if errors:
        die(errors)
    print("facts: ok")


def check_sponsor() -> None:
    errors = [f"{name} missing sponsor URL" for name in ["README.md", "curseforge-description.html"] if (ROOT / name).exists() and SPONSOR_URL not in read(ROOT / name)]
    if errors:
        die(errors)
    print("sponsor: ok")


def check_archives() -> None:
    errors: list[str] = []
    release_dir = ROOT / "Releases"
    if not release_dir.exists():
        print("archives: skipped")
        return
    for archive in release_dir.glob("*.zip"):
        try:
            with zipfile.ZipFile(archive) as zf:
                bad = zf.testzip()
                if bad:
                    errors.append(f"{rel(archive)} corrupt entry: {bad}")
                if not zf.infolist():
                    errors.append(f"{rel(archive)} is empty")
        except zipfile.BadZipFile as exc:
            errors.append(f"{rel(archive)} invalid zip: {exc}")
    if errors:
        die(errors)
    print("archives: ok")


def all_checks() -> None:
    for check in [check_layout, check_yaml, check_text, check_html, check_links, check_curseforge, check_facts, check_sponsor, check_archives]:
        check()


def main() -> None:
    checks = {
        "all": all_checks,
        "layout": check_layout,
        "yaml": check_yaml,
        "text": check_text,
        "html": check_html,
        "links": check_links,
        "curseforge": check_curseforge,
        "facts": check_facts,
        "sponsor": check_sponsor,
        "archives": check_archives,
    }
    parser = argparse.ArgumentParser(description="Validate Still Watching repository health.")
    parser.add_argument("check", nargs="?", default="all", choices=checks)
    args = parser.parse_args()
    checks[args.check]()


if __name__ == "__main__":
    main()
