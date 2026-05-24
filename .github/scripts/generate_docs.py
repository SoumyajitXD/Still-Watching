#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
REQUIRED_MOD_FIELDS = [
    "name",
    "category",
    "side",
    "side_confidence",
    "purpose",
    "curseforge_url",
    "notes",
    "server_pack_action",
    "reason",
]
ALLOWED_SIDES = {"client", "server", "both", "unknown"}
ALLOWED_SERVER_PACK_ACTIONS = {"keep", "remove", "verify", "unknown"}


def fail(message: str) -> None:
    raise SystemExit(f"ERROR: {message}")


def load_yaml(path: Path):
    with path.open(encoding="utf-8-sig") as handle:
        return yaml.safe_load(handle)


def parse_project() -> dict:
    data = load_yaml(ROOT / "data/project.yml")
    if not isinstance(data, dict):
        fail("data/project.yml must be a mapping")
    return data


def parse_mods() -> list[dict]:
    data = load_yaml(ROOT / "data/mods.yml")
    mods = data.get("mods") if isinstance(data, dict) else None
    if not isinstance(mods, list) or not mods:
        fail("data/mods.yml must contain a non-empty mods list")

    errors: list[str] = []
    for index, mod in enumerate(mods, 1):
        if not isinstance(mod, dict):
            errors.append(f"mod #{index} must be a mapping")
            continue

        name = str(mod.get("name") or f"#{index}")
        for field in REQUIRED_MOD_FIELDS:
            if field not in mod or mod[field] in (None, ""):
                errors.append(f"mod {name!r} missing {field}")

        side = mod.get("side")
        if side not in ALLOWED_SIDES:
            errors.append(f"mod {name!r} invalid side {side!r}")

        action = mod.get("server_pack_action")
        if action not in ALLOWED_SERVER_PACK_ACTIONS:
            errors.append(f"mod {name!r} invalid server_pack_action {action!r}")

    if errors:
        fail("; ".join(errors))
    return mods


def main() -> None:
    project = parse_project()
    mods = parse_mods()

    total = len(mods)
    both = sum(mod["side"] == "both" for mod in mods)
    client = sum(mod["side"] == "client" for mod in mods)
    unknown = sum(mod["side"] == "unknown" for mod in mods)

    out = [
        "# Latest Modlist",
        "",
        "> [!WARNING]",
        "> This is an admin reference, not a playable manifest. Use CurseForge release files for exact mod versions and truth.",
        "",
        f"Current documented release: **{project['current_release']}**.",
        f"Minecraft: **{project['minecraft_version']}** | Loader: **{project['loader']}** | Java: **{project['java_version']}** | CurseForge Project ID: **{project['curseforge_project_id']}**",
        "",
        "## Summary",
        "",
        "| Metric | Count |",
        "| --- | ---: |",
        f"| Total mods | {total} |",
        f"| Both-side count | {both} |",
        f"| Client candidate count | {client} |",
        f"| Unknown count | {unknown} |",
        "",
    ]

    # Deterministic category order, while preserving the existing source order
    # within each category so the generated modlist does not churn needlessly.
    categories: dict[str, list[dict]] = {}
    for mod in mods:
        categories.setdefault(mod["category"], []).append(mod)

    row_number = 1
    for category in sorted(categories):
        out += [
            f"## {category}",
            "",
            "| # | Mod | Side | Confidence | Purpose | CurseForge |",
            "| ---: | --- | --- | --- | --- | --- |",
        ]
        for mod in categories[category]:
            out.append(
                f"| {row_number} | {mod['name']} | {mod['side']} | {mod['side_confidence']} | {mod['purpose']} | [Link]({mod['curseforge_url']}) |"
            )
            row_number += 1
        out.append("")

    out += ["## Server pack trimming candidates", ""]
    trimming_candidates = [
        mod for mod in mods if mod["side"] == "client" or mod["server_pack_action"] == "remove"
    ]
    for index, mod in enumerate(trimming_candidates, 1):
        out.append(f"{index}. **{mod['name']}** — {mod['reason']}")

    out += ["", "## Needs verification", ""]
    verification_candidates = [
        mod
        for mod in mods
        if mod["side"] == "unknown"
        or mod["side_confidence"] in {"unknown", "needs verification"}
        or mod["server_pack_action"] == "verify"
    ]
    for index, mod in enumerate(verification_candidates, 1):
        out.append(f"{index}. **{mod['name']}** — {mod['reason']}")

    (ROOT / "latest-modlist.md").write_text("\n".join(out) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
