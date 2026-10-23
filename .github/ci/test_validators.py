"""Regression tests for repository and archive validators (stdlib only)."""
from __future__ import annotations

import contextlib
import io
import json
import os
import stat
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parent))
import validate_archives as archives  # noqa: E402
import validate_repository as repository  # noqa: E402


def make_zip(path: Path, members: dict[str, bytes]) -> None:
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as out:
        for name, payload in members.items():
            out.writestr(name, payload)


class ArchiveValidationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.path = Path(self.temporary.name) / "Still Watching-2.0.0.zip"

    def test_valid_repository_archive_without_manifest(self) -> None:
        make_zip(self.path, {"README.md": b"readme", "config/settings.txt": b"hello"})
        self.assertEqual(archives.inspect_archive(self.path, current=True), [])

    def test_traversal_is_rejected(self) -> None:
        make_zip(self.path, {"../escape.txt": b"bad"})
        self.assertTrue(any("Unsafe" in s for s in archives.inspect_archive(self.path)))

    def test_windows_unsafe_entry_is_rejected(self) -> None:
        make_zip(self.path, {"C:\\escape.txt": b"bad"})
        self.assertTrue(any("Unsafe" in s for s in archives.inspect_archive(self.path)))

    def test_duplicate_paths_ignore_case(self) -> None:
        make_zip(self.path, {"Config/Test.txt": b"one", "config/test.txt": b"two"})
        self.assertTrue(any("Duplicate" in s for s in archives.inspect_archive(self.path)))

    def test_wrong_minecraft_version_fails(self) -> None:
        data = {"minecraft": {"version": "1.21.11", "modLoaders": [{"id": "forge-47.4.0"}]}}
        make_zip(self.path, {"manifest.json": json.dumps(data).encode()})
        self.assertTrue(any("Minecraft version" in s
                            for s in archives.inspect_archive(self.path, current=True)))

    def test_wrong_loader_fails(self) -> None:
        data = {"minecraft": {"version": "1.20.1", "modLoaders": [{"id": "fabric-0.17.0"}]}}
        make_zip(self.path, {"manifest.json": json.dumps(data).encode()})
        self.assertTrue(any("expected Forge" in s
                            for s in archives.inspect_archive(self.path, current=True)))

    def test_broken_zip_fails(self) -> None:
        self.path.write_bytes(b"not a ZIP")
        self.assertTrue(any("Unreadable" in s
                            for s in archives.inspect_archive(self.path, current=True)))

    def test_symlink_fails(self) -> None:
        info = zipfile.ZipInfo("evil")
        info.create_system = 3
        info.external_attr = (stat.S_IFLNK | 0o777) << 16
        with zipfile.ZipFile(self.path, "w") as out:
            out.writestr(info, b"destination")
        self.assertTrue(any("Symlink" in s for s in archives.inspect_archive(self.path)))

    def test_manifest_is_not_claimed_if_missing(self) -> None:
        make_zip(self.path, {"modpack/README.md": b"source archive"})
        self.assertEqual(archives.inspect_archive(self.path, current=True), [])


class RepositoryValidationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)

    def test_modlist_detects_count_drift(self) -> None:
        content = (
            "# Modlist\n\nStill Watching V2.0.0\n"
            "**Documented entries:** 2 mods\n\n"
            "| Name | Curseforge |\n| --- | --- |\n"
            "| Example | [CurseForge](https://www.curseforge.com/minecraft/mc-mods/example) |\n"
        )
        (self.root / "latest-modlist.md").write_text(content, encoding="utf-8")
        with mock.patch.object(repository, "ROOT", self.root), \
             mock.patch.object(repository, "load_metadata", return_value={"current_documented_release": "Still Watching V2.0.0"}):
            results = repository.Reporter()
            with contextlib.redirect_stdout(io.StringIO()):
                repository.check_modlist(results)
        self.assertEqual(results.errors, 1)

    def test_modlist_detects_duplicate_names(self) -> None:
        content = (
            "# Modlist\n\nStill Watching V2.0.0\n"
            "**Documented entries:** 2 mods\n\n"
            "| Name | Curseforge |\n| --- | --- |\n"
            "| Example | [CurseForge](https://www.curseforge.com/minecraft/mc-mods/example) |\n"
            "| example | [CurseForge](https://www.curseforge.com/minecraft/mc-mods/example2) |\n"
        )
        (self.root / "latest-modlist.md").write_text(content, encoding="utf-8")
        with mock.patch.object(repository, "ROOT", self.root), \
             mock.patch.object(repository, "load_metadata", return_value={"current_documented_release": "Still Watching V2.0.0"}):
            results = repository.Reporter()
            with contextlib.redirect_stdout(io.StringIO()):
                repository.check_modlist(results)
        self.assertEqual(results.errors, 1)

    def test_broken_relative_anchor_fails(self) -> None:
        (self.root / "README.md").write_text("[broken](guide.md#missing)\n", encoding="utf-8")
        (self.root / "guide.md").write_text("# Existing\n", encoding="utf-8")
        with mock.patch.object(repository, "ROOT", self.root), \
             mock.patch.object(repository, "LINK_CHECK_TARGETS", [Path("README.md")]):
            results = repository.Reporter()
            with contextlib.redirect_stdout(io.StringIO()):
                repository.check_links(results)
        self.assertEqual(results.errors, 1)

    def test_html_rejects_script(self) -> None:
        data = {
            "project_name": "Still Watching", "minecraft_version": "1.20.1",
            "loader": "Forge", "current_documented_release": "Still Watching V2.0.0",
            "minimum_ram": "5 GB", "preferred_ram": "6–8 GB",
        }
        html = (
            "Still Watching 1.20.1 Forge Still Watching V2.0.0 5 GB 6–8 GB "
            "https://url-shortener.curseforge.com/AZDOs "
            '<img src="https://media.forgecdn.net/test.png">'
            '<a href="https://www.curseforge.com">Link</a><script>alert(1)</script>'
        )
        (self.root / "curseforge-description.html").write_text(html, encoding="utf-8")
        with mock.patch.object(repository, "ROOT", self.root), \
             mock.patch.object(repository, "load_metadata", return_value=data):
            results = repository.Reporter()
            with contextlib.redirect_stdout(io.StringIO()):
                repository.check_html(results)
        self.assertGreaterEqual(results.errors, 1)

    def test_push_whitespace_diff_uses_event_base(self) -> None:
        path = self.root / "event.json"
        path.write_text(json.dumps({"before": "a" * 40}), encoding="utf-8")
        with mock.patch.dict(os.environ, {"GITHUB_EVENT_NAME": "push", "GITHUB_EVENT_PATH": str(path)}):
            self.assertEqual(repository.git_diff_check_arguments(), ["a" * 40, "HEAD"])

    def test_missing_metadata_does_not_throw_keyerror(self) -> None:
        (self.root / "README.md").write_text("Still Watching", encoding="utf-8")
        with mock.patch.object(repository, "ROOT", self.root), \
             mock.patch.object(repository, "METADATA_TARGETS", [Path("README.md")]), \
             mock.patch.object(repository, "load_metadata", return_value={"project_name": "Still Watching"}):
            results = repository.Reporter()
            with contextlib.redirect_stdout(io.StringIO()):
                repository.check_metadata(results)
        self.assertGreater(results.errors, 0)


if __name__ == "__main__":
    unittest.main()
