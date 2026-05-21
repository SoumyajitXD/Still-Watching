#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
import zipfile
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

import yaml

ROOT = Path(__file__).resolve().parents[2]

BISECT_SPONSOR_START = "<!-- sponsor:bisecthosting:start -->"
BISECT_SPONSOR_END = "<!-- sponsor:bisecthosting:end -->"
BISECT_SPONSOR_LINK = "https://url-shortener.curseforge.com/AZDOs"
BISECT_SPONSOR_BANNER = (
    "https://media.forgecdn.net/attachments/description/1420406/"
    "description_0434b1be-41ee-4fa8-a2f5-177b2fe87c95.png"
)


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig", errors="ignore")


def load_yaml(path: Path):
    with path.open(encoding="utf-8-sig") as handle:
        return yaml.safe_load(handle)


def layout() -> None:
    required_files = ["README.md", "installation-guide.md", "latest-modlist.html", "curseforge-description.html", "LICENSE"]
    required_dirs = [".github/ISSUE_TEMPLATE", ".github/workflows", "Releases", "Screenshots"]
    missing = [item for item in required_files if not (ROOT / item).is_file()]
    missing += [item for item in required_dirs if not (ROOT / item).is_dir()]
    if missing:
        fail("Missing required repository paths: " + ", ".join(missing))
    print("Repository layout OK")


def yaml_files() -> None:
    paths = sorted((ROOT / ".github" / "workflows").glob("*.y*ml"))
    paths += sorted((ROOT / ".github" / "ISSUE_TEMPLATE").glob("*.y*ml"))
    if not paths:
        fail("No YAML files found")
    failed = False
    for path in paths:
        try:
            if load_yaml(path) is None:
                raise ValueError("file is empty")
            print(f"OK: {path.relative_to(ROOT)}")
        except Exception as exc:
            failed = True
            print(f"ERROR: {path.relative_to(ROOT)}: {exc}", file=sys.stderr)
    if failed:
        raise SystemExit(1)


class HtmlSmokeParser(HTMLParser):
    pass


def html() -> None:
    failed = False
    for path in sorted(ROOT.glob("*.html")):
        try:
            parser = HtmlSmokeParser()
            parser.feed(read(path))
            parser.close()
            print(f"OK: {path.name}")
        except Exception as exc:
            failed = True
            print(f"ERROR: {path.name}: {exc}", file=sys.stderr)
    if failed:
        raise SystemExit(1)


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links = []
        self.current = None

    def handle_starttag(self, tag, attrs):
        if tag.lower() == "a":
            self.current = {"href": dict(attrs).get("href", "").strip(), "text": []}

    def handle_data(self, data):
        if self.current is not None:
            self.current["text"].append(data)

    def handle_endtag(self, tag):
        if tag.lower() == "a" and self.current is not None:
            self.links.append((self.current["href"], " ".join("".join(self.current["text"]).split())))
            self.current = None


def modlist() -> None:
    path = ROOT / "latest-modlist.html"
    if not path.is_file():
        fail("latest-modlist.html is missing")
    parser = LinkParser()
    parser.feed(read(path))
    parser.close()
    links = parser.links
    errors = []
    if len(links) < 40:
        errors.append(f"expected at least 40 modlist links, found {len(links)}")
    for index, (href, text) in enumerate(links, 1):
        parsed = urlparse(href)
        parts = [part for part in parsed.path.split("/") if part]
        if not text:
            errors.append(f"link #{index} has empty text: {href}")
        if parsed.scheme != "https" or parsed.netloc != "www.curseforge.com":
            errors.append(f"non-CurseForge link: {href}")
        elif len(parts) < 3 or parts[0] != "minecraft" or parts[1] not in {"mc-mods", "texture-packs", "shaders", "modpacks"}:
            errors.append(f"unexpected CurseForge path: {href}")
    for href, count in Counter(href for href, _ in links).items():
        if count > 1:
            errors.append(f"duplicate link: {href}")
    if errors:
        fail("; ".join(errors))
    print(f"Modlist OK: {len(links)} links")


def release_zips() -> None:
    release_dir = ROOT / "Releases"
    if not release_dir.is_dir():
        fail("Releases directory is missing")
    failed = False
    for archive in sorted(release_dir.glob("*.zip")):
        try:
            with zipfile.ZipFile(archive) as zf:
                bad = zf.testzip()
                names = [info.filename.lower() for info in zf.infolist()]
                if bad:
                    raise zipfile.BadZipFile(f"corrupt entry: {bad}")
                if not names:
                    raise zipfile.BadZipFile("empty archive")
                if any(name == "overrides/" or name.startswith("overrides/") for name in names) and "manifest.json" not in names:
                    raise zipfile.BadZipFile("overrides/ exists without manifest.json")
                print(f"OK: {archive.relative_to(ROOT)}")
        except zipfile.BadZipFile as exc:
            failed = True
            print(f"ERROR: {archive.relative_to(ROOT)}: {exc}", file=sys.stderr)
    if failed:
        raise SystemExit(1)


def project_facts() -> None:
    files = [ROOT / "README.md", ROOT / "installation-guide.md", ROOT / "curseforge-description.html"]
    checks = {
        "project name": re.compile(r"\bStill\s+Watching\b", re.I),
        "Minecraft 1.20.1": re.compile(r"\b1\.20\.1\b"),
        "Forge": re.compile(r"\bForge\b", re.I),
        "Java 17": re.compile(r"\bJava\b[\s\S]{0,80}\b17\b|\b17\b[\s\S]{0,80}\bJava\b", re.I),
        "CurseForge": re.compile(r"\bCurseForge\b", re.I),
        "project ID 1420406": re.compile(r"\b1420406\b"),
    }
    errors = []
    for path in files:
        if not path.is_file():
            errors.append(f"missing {path.name}")
            continue
        text = read(path)
        for label, pattern in checks.items():
            if not pattern.search(text):
                errors.append(f"{path.name} missing {label}")
    if errors:
        fail("; ".join(errors))
    print("Project facts OK")


def sponsor_guard() -> None:
    path = ROOT / "README.md"
    if not path.is_file():
        fail("README.md is missing")

    text = read(path)
    required_items = {
        "BisectHosting sponsor start marker": BISECT_SPONSOR_START,
        "BisectHosting sponsor end marker": BISECT_SPONSOR_END,
        "BisectHosting sponsor link": BISECT_SPONSOR_LINK,
        "BisectHosting sponsor banner": BISECT_SPONSOR_BANNER,
    }
    missing = [label for label, needle in required_items.items() if needle not in text]
    if missing:
        fail("README.md missing required sponsor content: " + ", ".join(missing))

    blocks = []
    cursor = 0
    while True:
        left = text.find(BISECT_SPONSOR_START, cursor)
        if left == -1:
            break
        right = text.find(BISECT_SPONSOR_END, left)
        if right == -1:
            fail("BisectHosting sponsor block start marker has no matching end marker")
        blocks.append(text[left : right + len(BISECT_SPONSOR_END)])
        cursor = right + len(BISECT_SPONSOR_END)

    if not blocks:
        fail("README.md must contain at least one complete BisectHosting sponsor block")
    if not any(BISECT_SPONSOR_LINK in block and BISECT_SPONSOR_BANNER in block for block in blocks):
        fail("No BisectHosting sponsor block contains both the required link and banner image")

    print("BisectHosting sponsor guard OK")


def issue_templates() -> None:
    template_dir = ROOT / ".github" / "ISSUE_TEMPLATE"
    if not template_dir.is_dir():
        fail(".github/ISSUE_TEMPLATE is missing")
    errors = []
    config = template_dir / "config.yml"
    if not config.is_file():
        errors.append("missing config.yml")
    elif not isinstance(load_yaml(config), dict) or load_yaml(config).get("blank_issues_enabled") is not False:
        errors.append("config.yml must set blank_issues_enabled: false")
    forms = sorted(path for path in template_dir.glob("*.y*ml") if path.name != "config.yml")
    if not forms:
        errors.append("no issue form files found")
    for path in forms:
        data = load_yaml(path)
        if not isinstance(data, dict):
            errors.append(f"{path.name} must be a mapping")
            continue
        for key in ["name", "description", "title", "labels", "body"]:
            if not data.get(key):
                errors.append(f"{path.name} missing {key}")
        body = data.get("body")
        if not isinstance(body, list) or not body:
            errors.append(f"{path.name} has empty body")
            continue
        ids = set()
        required = False
        for i, item in enumerate(body, 1):
            if not isinstance(item, dict):
                errors.append(f"{path.name} body item {i} must be a mapping")
                continue
            field_type = item.get("type")
            if field_type != "markdown":
                field_id = item.get("id")
                attrs = item.get("attributes") or {}
                if not field_id:
                    errors.append(f"{path.name} field {i} missing id")
                elif field_id in ids:
                    errors.append(f"{path.name} duplicate field id {field_id}")
                ids.add(field_id)
                if not attrs.get("label"):
                    errors.append(f"{path.name} field {i} missing label")
            if field_type in {"input", "textarea", "dropdown", "checkboxes"} and (item.get("validations") or {}).get("required") is True:
                required = True
        if not required:
            errors.append(f"{path.name} needs at least one required user field")
    if errors:
        fail("; ".join(errors))
    print("Issue templates OK")


def all_checks() -> None:
    for check in [layout, yaml_files, html, project_facts, issue_templates, modlist, sponsor_guard, release_zips]:
        check()


def main() -> None:
    checks = {
        "all": all_checks,
        "layout": layout,
        "yaml": yaml_files,
        "html": html,
        "modlist": modlist,
        "release-zips": release_zips,
        "project-facts": project_facts,
        "issue-templates": issue_templates,
        "sponsor": sponsor_guard,
    }
    parser = argparse.ArgumentParser()
    parser.add_argument("check", choices=checks)
    checks[parser.parse_args().check]()


if __name__ == "__main__":
    main()
