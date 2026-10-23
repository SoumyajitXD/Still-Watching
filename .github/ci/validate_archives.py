#!/usr/bin/env python3
"""Read-only structural checks for Still Watching's archived ZIP files.

These are repository release archives, not proof of installability or Minecraft
runtime compatibility. Never extract untrusted archive entries to disk.
"""
from __future__ import annotations

import json
import re
import stat
import sys
import zipfile
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[2]
ARCHIVES = ROOT / "Releases"
METADATA = ROOT / ".github/ci/project-metadata.json"
MAX_ENTRIES = 100_000
MAX_EXPANDED_BYTES = 8 * 1024 ** 3
MAX_MANIFEST_BYTES = 1024 * 1024


def unsafe_member_name(name: str) -> bool:
    """Reject absolute, traversal, and Windows-ambiguous entry names."""
    path = PurePosixPath(name)
    return (
        not name
        or name.startswith(("/", "\\"))
        or "\\" in name
        or "\x00" in name
        or ":" in name.split("/")[0]
        or ".." in path.parts
    )


def inspect_archive(path: Path, *, current: bool = False,
                    game_version: str = "1.20.1",
                    loader: str = "Forge") -> list[str]:
    errors: list[str] = []
    try:
        with zipfile.ZipFile(path) as archive:
            members = archive.infolist()
            if not members:
                errors.append("Archive contains no entries")
            if len(members) > MAX_ENTRIES:
                errors.append(f"Too many ZIP entries: {len(members)}")
                return errors

            seen: set[str] = set()
            expanded = 0
            manifests: list[zipfile.ZipInfo] = []
            for member in members:
                name = member.filename
                if unsafe_member_name(name):
                    errors.append(f"Unsafe ZIP member path: {name!r}")
                    continue
                key = name.rstrip("/").casefold()
                if key in seen:
                    errors.append(f"Duplicate/case-colliding ZIP member: {name!r}")
                seen.add(key)
                if member.flag_bits & 1:
                    errors.append(f"Encrypted ZIP member: {name!r}")
                if member.create_system == 3 and stat.S_ISLNK(member.external_attr >> 16):
                    errors.append(f"Symlink entry is not allowed: {name!r}")
                expanded += member.file_size
                if current and not member.is_dir() and (
                    name == "manifest.json" or
                    (name.count("/") == 1 and name.endswith("/manifest.json"))
                ):
                    manifests.append(member)

            if expanded > MAX_EXPANDED_BYTES:
                errors.append(f"Total expanded data exceeds {MAX_EXPANDED_BYTES} bytes")
                return errors

            if current and not errors:
                # A missing manifest is legitimate for source/repository ZIPs.
                # Inspect a manifest only when one exists, without treating it
                # as proof that third-party mods work together.
                if len(manifests) > 1:
                    errors.append("More than one possible root modpack manifest")
                elif manifests:
                    info = manifests[0]
                    if info.file_size > MAX_MANIFEST_BYTES:
                        errors.append("Modpack manifest exceeds maximum safe size")
                    else:
                        try:
                            metadata = json.loads(archive.read(info).decode("utf-8"))
                        except (ValueError, UnicodeError, RuntimeError, zipfile.BadZipFile) as exc:
                            errors.append(f"Invalid modpack manifest: {exc}")
                        else:
                            game = metadata.get("minecraft", {})
                            if isinstance(game, dict) and "version" in game:
                                if str(game["version"]) != game_version:
                                    errors.append(
                                        f"Manifest Minecraft version {game['version']!r} "
                                        f"does not match {game_version!r}"
                                    )
                                modloaders = game.get("modLoaders", [])
                                if isinstance(modloaders, list) and modloaders:
                                    prefixes = [str(x.get("id", "")).lower()
                                                for x in modloaders if isinstance(x, dict)]
                                    if not any(x.startswith(loader.lower() + "-") for x in prefixes):
                                        errors.append(f"Manifest lacks the expected {loader} loader")

                # CRC-check every member in the documented current archive, not
                # only the ZIP central directory. No extraction is performed.
                if not errors:
                    bad_member = archive.testzip()
                    if bad_member is not None:
                        errors.append(f"Bad CRC or unreadable member: {bad_member!r}")
    except (OSError, zipfile.BadZipFile, zipfile.LargeZipFile, RuntimeError) as exc:
        errors.append(f"Unreadable ZIP: {exc}")
    return errors


def main() -> int:
    settings = json.loads(METADATA.read_text(encoding="utf-8"))
    match = re.fullmatch(r"Still Watching V(\d+\.\d+\.\d+)",
                         settings["current_documented_release"])
    if not match:
        print("::error file=.github/ci/project-metadata.json::Malformed current documented release")
        return 1
    current_file = f"Still Watching-{match.group(1)}.zip"
    archives = sorted(ARCHIVES.glob("*.zip"))
    if not archives or current_file not in {x.name for x in archives}:
        print(f"::error file=Releases::{current_file} is missing from release archives")
        return 1

    failures = 0
    for path in archives:
        current = path.name == current_file
        issues = inspect_archive(
            path, current=current,
            game_version=settings["minecraft_version"], loader=settings["loader"]
        )
        print(f"{path.name}: {'FAIL' if issues else 'OK'}"
              f" ({'CRC and metadata' if current else 'structure and metadata'})")
        for issue in issues:
            failures += 1
            print(f"::error file=Releases/{path.name}::{issue}")
    print(f"Checked {len(archives)} ZIPs; {failures} issue(s)."
          " This is not Minecraft runtime validation.")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
