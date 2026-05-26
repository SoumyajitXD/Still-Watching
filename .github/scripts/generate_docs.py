#!/usr/bin/env python3
"""Lightweight documentation helper for Still Watching.

If `data/mods.yml` and `data/project.yml` exist, this regenerates
`latest-modlist.md`. If they do not exist, it performs a safe dry validation and
leaves tracked documentation untouched.
"""
from __future__ import annotations

import argparse
from pathlib import Path

try:
    import yaml  # type: ignore
except Exception:  # pragma: no cover - CI installs PyYAML.
    yaml = None

ROOT = Path(__file__).resolve().parents[2]
MOD_FIELDS = ["name", "curseforge_url"]


def fail(message: str) -> None:
    raise SystemExit(f"ERROR: {message}")


def load_yaml(path: Path):
    if yaml is None:
        fail("PyYAML is not installed; run `python -m pip install PyYAML`")
    with path.open(encoding="utf-8-sig") as handle:
        return yaml.safe_load(handle)


def build_from_data() -> str:
    project_path = ROOT / "data/project.yml"
    mods_path = ROOT / "data/mods.yml"
    project = load_yaml(project_path)
    mods_doc = load_yaml(mods_path)
    mods = mods_doc.get("mods") if isinstance(mods_doc, dict) else None
    if not isinstance(project, dict):
        fail("data/project.yml must be a mapping")
    if not isinstance(mods, list) or not mods:
        fail("data/mods.yml must contain a non-empty mods list")

    rows: list[str] = []
    for index, mod in enumerate(mods, 1):
        if not isinstance(mod, dict):
            fail(f"mod #{index} must be a mapping")
        for field in MOD_FIELDS:
            if not mod.get(field):
                fail(f"mod #{index} missing {field}")
        rows.append(f"| {mod['name']} | [Curseforge]({mod['curseforge_url']}) |")

    release = project.get("current_release", "Still Watching")
    out = [
        "# Modlist",
        "",
        f"**Version:** {release} (latest)",
        "",
        "| Name | Curseforge |",
        "|---|---|",
        *rows,
        "",
    ]
    return "\n".join(out)


def main() -> None:
    parser = argparse.ArgumentParser(description="Regenerate latest-modlist.md when source data exists.")
    parser.add_argument("--check", action="store_true", help="Verify generated output matches latest-modlist.md.")
    args = parser.parse_args()

    project_path = ROOT / "data/project.yml"
    mods_path = ROOT / "data/mods.yml"
    target = ROOT / "latest-modlist.md"

    if not project_path.exists() or not mods_path.exists():
        if not target.exists() or not target.read_text(encoding="utf-8-sig", errors="replace").strip():
            fail("latest-modlist.md is missing or empty, and source data files are absent")
        print("No data/*.yml source files found; kept latest-modlist.md unchanged.")
        return

    generated = build_from_data()
    if args.check:
        current = target.read_text(encoding="utf-8-sig", errors="replace") if target.exists() else ""
        if current != generated:
            fail("latest-modlist.md is stale; run python .github/scripts/generate_docs.py")
        print("generated docs: ok")
        return

    target.write_text(generated, encoding="utf-8")
    print("Wrote latest-modlist.md")


if __name__ == "__main__":
    main()
