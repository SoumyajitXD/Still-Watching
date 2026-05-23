#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
import zipfile
from collections import Counter
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

import yaml

ROOT = Path(__file__).resolve().parents[2]
PROJECT = {
    "project_name": "Still Watching",
    "minecraft_version": "1.20.1",
    "loader": "Forge",
    "java_version": "17",
    "curseforge_project_id": "1420406",
    "current_release": "Still Watching V1.0.9",
}
SPONSOR = {
    "start": "<!-- sponsor:bisecthosting:start -->",
    "end": "<!-- sponsor:bisecthosting:end -->",
    "url": "https://url-shortener.curseforge.com/AZDOs",
    "banner": "https://media.forgecdn.net/attachments/description/1420406/description_0434b1be-41ee-4fa8-a2f5-177b2fe87c95.png",
}
FACT_FILES = [ROOT / p for p in ["README.md", "installation-guide.md", "curseforge-description.html", "latest-modlist.md"]]
REQ_MAP = [
    "README.md", "installation-guide.md", "latest-modlist.md", "curseforge-description.html",
    "Screenshots/", "Releases/", ".github/ISSUE_TEMPLATE/", ".github/workflows/ci.yml",
    ".github/scripts/validate.py", "LICENSE",
]

@dataclass
class LocalLink:
    source: Path
    target: str
    line: int

def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)

def read(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig", errors="ignore")

def load_yaml(path: Path):
    with path.open(encoding="utf-8-sig") as handle:
        return yaml.safe_load(handle)

def line_number(text: str, index: int) -> int:
    return text.count("\n", 0, index) + 1

def plain(text: str) -> str:
    return " ".join(re.sub(r"<[^>]+>", " ", text).split())

def layout() -> None:
    files = [
        "README.md", "installation-guide.md", "latest-modlist.md", "curseforge-description.html",
        "CHANGELOG.md", "LICENSE", "data/project.yml", "data/mods.yml",
        ".github/scripts/generate_docs.py", ".github/scripts/validate.py", ".github/workflows/ci.yml",
        "docs/release-checklist.md", "docs/server-pack-guide.md",
    ]
    dirs = [".github/ISSUE_TEMPLATE", ".github/workflows", "Releases", "Screenshots", "data", "docs"]
    missing = [p for p in files if not (ROOT / p).is_file()] + [p for p in dirs if not (ROOT / p).is_dir()]
    if missing:
        fail("Missing required repository paths: " + ", ".join(missing))
    print("Repository layout OK")

def yaml_files() -> None:
    paths = sorted((ROOT / ".github" / "workflows").glob("*.y*ml"))
    paths += sorted((ROOT / ".github" / "ISSUE_TEMPLATE").glob("*.y*ml"))
    paths += [ROOT / "data/project.yml", ROOT / "data/mods.yml"]
    errors = []
    for path in paths:
        try:
            if load_yaml(path) is None:
                raise ValueError("file is empty")
            print(f"OK: {path.relative_to(ROOT)}")
        except Exception as exc:
            errors.append(f"{path.relative_to(ROOT)}: {exc}")
    if errors:
        fail("; ".join(errors))

def html() -> None:
    class Smoke(HTMLParser):
        pass
    errors = []
    for path in sorted(ROOT.glob("*.html")):
        try:
            parser = Smoke(); parser.feed(read(path)); parser.close()
            print(f"OK: {path.name}")
        except Exception as exc:
            errors.append(f"{path.name}: {exc}")
    if errors:
        fail("; ".join(errors))

def metadata() -> None:
    errors = []
    project = load_yaml(ROOT / "data/project.yml")
    mods_doc = load_yaml(ROOT / "data/mods.yml")
    if not isinstance(project, dict):
        fail("data/project.yml must be a mapping")
    for key, expected in PROJECT.items():
        if str(project.get(key)) != expected:
            errors.append(f"data/project.yml {key}={project.get(key)!r}, expected {expected!r}")
    sponsor = project.get("sponsor") or {}
    sponsor_keys = {
        "bisecthosting_url": SPONSOR["url"],
        "required_banner_url": SPONSOR["banner"],
        "sponsor_marker_start": SPONSOR["start"],
        "sponsor_marker_end": SPONSOR["end"],
    }
    for key, expected in sponsor_keys.items():
        if sponsor.get(key) != expected:
            errors.append(f"data/project.yml sponsor.{key} mismatch")
    mods = mods_doc.get("mods") if isinstance(mods_doc, dict) else None
    if not isinstance(mods, list):
        errors.append("data/mods.yml must contain a mods list")
    else:
        names, urls = [], []
        for index, mod in enumerate(mods, 1):
            if not isinstance(mod, dict):
                errors.append(f"mod #{index} must be a mapping")
                continue
            for key in ["name", "category", "side", "side_confidence", "purpose", "curseforge_url", "notes", "server_pack_action", "reason"]:
                if not mod.get(key):
                    errors.append(f"mod #{index} missing {key}")
            name = str(mod.get("name", "")).strip()
            side = str(mod.get("side", "")).lower()
            confidence = str(mod.get("side_confidence", "")).lower()
            action = str(mod.get("server_pack_action", "")).lower()
            reason = str(mod.get("reason", ""))
            url = str(mod.get("curseforge_url", "")).strip()
            names.append(name); urls.append(url)
            if side not in {"client", "server", "both", "unknown"}:
                errors.append(f"{name} invalid side {side!r}")
            if action not in {"keep", "remove", "verify", "unknown"}:
                errors.append(f"{name} invalid server_pack_action {action!r}")
            if confidence in {"likely", "guess", "guessed"}:
                errors.append(f"{name} uses weak side_confidence {confidence!r}; use official source, manifest, tested, or needs verification")
            if action == "remove" and not re.search(r"\b(tested|official|manifest|dedicated-server safe|server safe)\b", reason, re.I):
                errors.append(f"{name} marked removable without proof")
            parsed = urlparse(url)
            parts = [part for part in parsed.path.split("/") if part]
            if parsed.scheme != "https" or parsed.netloc != "www.curseforge.com" or len(parts) < 3 or parts[0] != "minecraft" or parts[1] not in {"mc-mods", "texture-packs", "shaders", "modpacks"}:
                errors.append(f"{name} unexpected CurseForge URL {url}")
        errors += [f"duplicate mod name: {name}" for name, count in Counter(names).items() if name and count > 1]
        errors += [f"duplicate CurseForge URL: {url}" for url, count in Counter(urls).items() if url and count > 1]
    if errors:
        fail("; ".join(errors))
    print("Metadata YAML OK")

def markdown_links(text: str) -> list[tuple[str, str]]:
    pattern = re.compile(r"(?<!!)\[([^\]\n]+)\]\((https?://[^\s)]+)\)")
    return [(href.strip(), " ".join(label.split())) for label, href in pattern.findall(text)]

def table_rows(text: str) -> list[tuple[int, str, str, str, str]]:
    pattern = re.compile(r"(?m)^\|\s*(\d+)\s*\|\s*([^|\n]+?)\s*\|\s*(client|server|both|unknown)\s*\|\s*([^|\n]+?)\s*\|\s*([^|\n]+?)\s*\|\s*\[[^\]\n]+\]\((https?://[^\s)]+)\)\s*\|", re.I)
    return [(int(n), name.strip(), side.lower(), confidence.strip().lower(), href.strip()) for n, name, side, confidence, _purpose, href in pattern.findall(text)]

def modlist() -> None:
    text = read(ROOT / "latest-modlist.md")
    links = markdown_links(text)
    rows = table_rows(text)
    errors = []
    if "admin reference" not in text.lower() or "not a playable manifest" not in text.lower():
        errors.append("latest-modlist.md must say it is an admin reference, not a playable manifest")
    if "curseforge release" not in text.lower():
        errors.append("latest-modlist.md must defer exact versions to CurseForge release files")
    if len(links) < 40:
        errors.append(f"expected at least 40 CurseForge links, found {len(links)}")
    if len(rows) != len(links):
        errors.append(f"expected every modlist link to be a table row, found {len(rows)} rows for {len(links)} links")
    numbers = [number for number, *_ in rows]
    if numbers != list(range(1, len(rows) + 1)):
        errors.append("modlist numbering must be continuous")
    for index, (href, _label) in enumerate(links, 1):
        parsed = urlparse(href)
        parts = [part for part in parsed.path.split("/") if part]
        if parsed.scheme != "https" or parsed.netloc != "www.curseforge.com" or len(parts) < 3 or parts[0] != "minecraft" or parts[1] not in {"mc-mods", "texture-packs", "shaders", "modpacks"}:
            errors.append(f"unexpected CurseForge link #{index}: {href}")
    errors += [f"duplicate link: {href}" for href, count in Counter(href for href, _ in links).items() if count > 1]
    for number, name, side, confidence, _url in rows:
        if side != "unknown" and confidence not in {"official source", "manifest", "tested", "needs verification"}:
            errors.append(f"row {number} {name} side lacks acceptable confidence")
    if errors:
        fail("; ".join(errors))
    print(f"Modlist OK: {len(rows)} entries, {len(links)} links")

def release_zips() -> None:
    errors = []
    for archive in sorted((ROOT / "Releases").glob("*.zip")):
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
            errors.append(f"{archive.relative_to(ROOT)}: {exc}")
    if errors:
        fail("; ".join(errors))
    print("Release ZIP audit OK")

def release_facts() -> None:
    required = {
        "Still Watching": re.compile(r"\bStill\s+Watching\b", re.I),
        "Minecraft 1.20.1": re.compile(r"\b1\.20\.1\b"),
        "Forge": re.compile(r"\bForge\b", re.I),
        "Java 17": re.compile(r"\bJava\b[\s\S]{0,100}\b17\b|\b17\b[\s\S]{0,100}\bJava\b", re.I),
        "Project ID 1420406": re.compile(r"\b1420406\b"),
    }
    errors, versions = [], {}
    for path in FACT_FILES:
        text = read(path)
        if path.name != "latest-modlist.md":
            for label, pattern in required.items():
                if not pattern.search(text):
                    errors.append(f"{path.name} missing {label}")
        for pattern, expected, label in [
            (r"\bMinecraft(?:\s+version)?\b[^\n<|]{0,80}\b(\d+\.\d+(?:\.\d+)?)\b", "1.20.1", "Minecraft"),
            (r"\bJava\b[^\n<|]{0,80}\b(\d{1,2})\b", "17", "Java"),
            (r"(?:Project\s+ID[^\d]{0,20}|attachments/description/)(\d+)", "1420406", "CurseForge ID"),
        ]:
            for match in re.finditer(pattern, text, re.I):
                if match.group(1) != expected:
                    errors.append(f"{path.name}:{line_number(text, match.start(1))} has {label} {match.group(1)}, expected {expected}")
        for match in re.finditer(r"\b(?:Loader|Mod Loader)\b[^\n<|]{0,80}\b(Fabric|Quilt|NeoForge)\b", text, re.I):
            errors.append(f"{path.name}:{line_number(text, match.start())} mentions non-Forge loader near: {plain(text[max(0, match.start()-70):match.end()+70])}")
        for match in re.finditer(r"\b(?:Still\s+Watching\s+V|Current\s+(?:documented\s+)?release[\s\S]{0,120}\bV|Latest\s+(?:documented\s+)?Version[\s\S]{0,120}\bV?)(\d+\.\d+\.\d+)\b", text, re.I):
            versions.setdefault(match.group(1), []).append(path.name)
    if len(versions) > 1:
        errors.append(f"release/version text is inconsistent: {versions}")
    if errors:
        fail("; ".join(errors))
    print("Release facts OK")

def sponsor_guard() -> None:
    errors = []
    for path in [ROOT / "README.md", ROOT / "curseforge-description.html"]:
        text = read(path)
        for label, value in SPONSOR.items():
            if value not in text:
                errors.append(f"{path.name} missing sponsor {label}")
        blocks = re.findall(re.escape(SPONSOR["start"]) + r"[\s\S]*?" + re.escape(SPONSOR["end"]), text)
        if not blocks:
            errors.append(f"{path.name} has no complete sponsor block")
        elif not any(SPONSOR["url"] in block and SPONSOR["banner"] in block for block in blocks):
            errors.append(f"{path.name} has incomplete sponsor block")
    if errors:
        fail("; ".join(errors))
    print("BisectHosting sponsor guard OK")

def issue_templates() -> None:
    template_dir = ROOT / ".github" / "ISSUE_TEMPLATE"
    errors = []
    config = template_dir / "config.yml"
    if not config.is_file():
        errors.append("missing config.yml")
    elif (load_yaml(config) or {}).get("blank_issues_enabled") is not False:
        errors.append("config.yml must set blank_issues_enabled: false")
    forms = [p for p in sorted(template_dir.glob("*.y*ml")) if p.name != "config.yml"]
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
        ids, required = set(), False
        for index, item in enumerate(data.get("body") or [], 1):
            if not isinstance(item, dict):
                errors.append(f"{path.name} body item {index} must be a mapping")
                continue
            if item.get("type") != "markdown":
                field_id = item.get("id")
                attrs = item.get("attributes") or {}
                if not field_id:
                    errors.append(f"{path.name} field {index} missing id")
                elif field_id in ids:
                    errors.append(f"{path.name} duplicate field id {field_id}")
                ids.add(field_id)
                if not attrs.get("label"):
                    errors.append(f"{path.name} field {index} missing label")
            if item.get("type") in {"input", "textarea", "dropdown", "checkboxes"} and (item.get("validations") or {}).get("required") is True:
                required = True
        if not required:
            errors.append(f"{path.name} needs at least one required user field")
    if errors:
        fail("; ".join(errors))
    print("Issue templates OK")

def local_links() -> None:
    errors = []
    pattern = re.compile(r"(?<!!)(?:\[[^\]\n]+\]|<[^>\n]+>)\(([^)\n]+)\)")
    for path in sorted(ROOT.glob("*.md")) + sorted((ROOT / "docs").glob("*.md")):
        text = read(path)
        for match in pattern.finditer(text):
            href = match.group(1).strip()
            if not href or href.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = href.split("#", 1)[0].split("?", 1)[0].strip()
            if not target:
                continue
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f"{path.relative_to(ROOT)}:{line_number(text, match.start(1))} escapes repo: {href}")
                continue
            if not resolved.exists():
                errors.append(f"{path.relative_to(ROOT)}:{line_number(text, match.start(1))} broken local link {href}")
    if errors:
        fail("; ".join(errors))
    print("Local markdown links OK")

def readme_docs() -> None:
    text = read(ROOT / "README.md")
    errors = []
    for href in ["./installation-guide.md", "./latest-modlist.md", "./curseforge-description.html"]:
        if f"]({href})" not in text and f"`{href}`" not in text:
            errors.append(f"README.md missing required docs link: {href}")
    match = re.search(r"##\s+Repository Map\n\n\| Path \| Purpose \|\n\| --- \| --- \|\n([\s\S]*?)(?:\n---|\Z)", text)
    if not match:
        errors.append("README.md missing Repository Map table")
    else:
        listed = []
        for label, href in re.findall(r"\|\s*\[`]?([^`|]+?)[`]?\s*\]\(([^)]+)\)\s*\|", match.group(1)):
            if not href.startswith("./"):
                errors.append(f"Repository Map uses non-local link for {label.strip()}: {href}")
                continue
            normalized = href[2:]
            listed.append(normalized)
            fs_path = ROOT / normalized.rstrip("/")
            if normalized.endswith("/") and not fs_path.is_dir():
                errors.append(f"Repository Map entry points to missing directory: {normalized}")
            elif not normalized.endswith("/") and not fs_path.is_file():
                errors.append(f"Repository Map entry points to missing file: {normalized}")
        for required in REQ_MAP:
            if required not in listed:
                errors.append(f"Repository Map missing required path: {required}")
    if errors:
        fail("; ".join(errors))
    print("README docs and repository map OK")

def curseforge_id_consistency() -> None:
    errors = []
    pattern = re.compile(r"(?:/curseforge/(?:v|dt)/|attachments/description/|Project\s+ID[^\d]{0,20})(\d+)", re.I)
    for path in FACT_FILES:
        ids = sorted(set(pattern.findall(read(path))))
        if ids and ids != ["1420406"]:
            errors.append(f"{path.name} has CurseForge IDs {ids}, expected [1420406]")
    if errors:
        fail("; ".join(errors))
    print("CurseForge project ID consistency OK (1420406)")

def all_checks() -> None:
    for check in [layout, yaml_files, html, metadata, local_links, readme_docs, curseforge_id_consistency, release_facts, issue_templates, modlist, sponsor_guard, release_zips]:
        check()

def main() -> None:
    checks = {
        "all": all_checks, "layout": layout, "yaml": yaml_files, "html": html, "metadata": metadata,
        "modlist": modlist, "markdown-links": local_links, "readme-docs": readme_docs,
        "curseforge-id": curseforge_id_consistency, "release-zips": release_zips,
        "release-facts": release_facts, "issue-templates": issue_templates, "sponsor": sponsor_guard,
    }
    parser = argparse.ArgumentParser()
    parser.add_argument("check", choices=checks)
    checks[parser.parse_args().check]()

if __name__ == "__main__":
    main()
