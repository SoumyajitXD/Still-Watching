from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path

DOC_EXTENSIONS = {".md", ".mdx", ".rst", ".adoc", ".txt"}
SKIP_DIRS = {".git", "node_modules", "build", "dist", ".venv", "venv", "__pycache__"}

EXPECTED = {
    "project_name": "Still Watching",
    "minecraft_version": "1.20.1",
    "loader": "Forge",
    "curseforge_project_id": "1420406",
    "release_pattern": "Still Watching Vx.y.z",
}


@dataclass(frozen=True)
class Finding:
    path: Path
    line_number: int
    rule: str
    expected: str
    found: str
    line: str


def doc_paths(root: Path) -> list[Path]:
    paths: list[Path] = []
    for path in root.rglob("*"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.is_file() and path.suffix.lower() in DOC_EXTENSIONS:
            paths.append(path)
    return sorted(paths)


def split_lines(path: Path) -> list[str]:
    try:
        return path.read_text(encoding="utf-8").splitlines()
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8", errors="replace").splitlines()


def ignored_line(line: str) -> bool:
    stripped = line.strip()
    return not stripped or stripped.startswith(("<!--", "-->", "# noqa", "//"))


def add(
    findings: list[Finding],
    path: Path,
    line_no: int,
    rule: str,
    expected: str,
    found: str,
    line: str,
) -> None:
    findings.append(Finding(path, line_no, rule, expected, found.strip(), line.strip()))


def is_expected_release_name(value: str) -> bool:
    return re.fullmatch(r"Still Watching V\d+\.\d+\.\d+", value.strip(), flags=re.IGNORECASE) is not None


def scan_file(path: Path) -> list[Finding]:
    findings: list[Finding] = []

    for line_no, line in enumerate(split_lines(path), start=1):
        if ignored_line(line):
            continue

        lower = line.lower()
        normalized = re.sub(r"[`*_\[\](){}]", " ", line)

        if re.search(r"\b(project|modpack|mod)\s+name\b", lower) or re.search(r"\bname\s*[:=-]", lower):
            name_match = re.search(r"(?:project|modpack|mod)?\s*name\s*[:=-]\s*([^|#]+)", normalized, flags=re.IGNORECASE)
            if name_match:
                value = name_match.group(1).strip().strip("\"'")
                if value and "still watching" not in value.lower():
                    add(findings, path, line_no, "Project name", EXPECTED["project_name"], value, line)

        for match in re.finditer(r"\b(?:minecraft|mc)\s*(?:version|versions)?\s*[:=-]?\s*(\d+\.\d+(?:\.\d+)?)", lower):
            value = match.group(1)
            if value != EXPECTED["minecraft_version"]:
                add(findings, path, line_no, "Minecraft version", EXPECTED["minecraft_version"], value, line)

        if "minecraft" in lower or re.search(r"\bmc\b", lower):
            versions = re.findall(r"\b1\.\d+(?:\.\d+)?\b", lower)
            wrong_versions = [v for v in versions if v != EXPECTED["minecraft_version"]]
            if wrong_versions and any(
                token in lower
                for token in ("requires", "required", "for", "version", "versions", "compatible", "supports", "support")
            ):
                add(
                    findings,
                    path,
                    line_no,
                    "Minecraft version",
                    EXPECTED["minecraft_version"],
                    ", ".join(dict.fromkeys(wrong_versions)),
                    line,
                )

        loader_claim = re.search(r"\b(?:mod\s*)?loader\s*[:=-]?\s*(fabric|quilt|neoforge|forge)\b", lower)
        if loader_claim and loader_claim.group(1) != "forge":
            add(findings, path, line_no, "Loader", EXPECTED["loader"], loader_claim.group(1), line)

        if re.search(r"\b(fabric|quilt|neoforge)\b", lower) and re.search(
            r"\b(required|requires|only|loader|install|installation|compatible|supports|support)\b", lower
        ):
            negated = re.search(
                r"\bnot\s+(?:fabric|quilt|neoforge)\b|\b(fabric|quilt|neoforge)\s+(?:is\s+)?not\b",
                lower,
            )
            if not negated:
                add(findings, path, line_no, "Loader", EXPECTED["loader"], "Fabric/Quilt/NeoForge claim", line)

        cf_id_claim = re.search(r"\b(?:curseforge\s*)?(?:project\s*)?id\s*[:=#-]?\s*(\d{5,})\b", lower)
        if cf_id_claim:
            value = cf_id_claim.group(1)
            if value != EXPECTED["curseforge_project_id"]:
                add(findings, path, line_no, "CurseForge Project ID", EXPECTED["curseforge_project_id"], value, line)

        if re.search(r"\b(current\s+release|release\s+pattern|release\s+name|file\s+name|version\s+name)\b", lower):
            quoted_values = re.findall(r"[\"'`]([^\"'`]*\bV?\d+\.\d+\.\d+[^\"'`]*)[\"'`]", line)
            if quoted_values:
                for value in quoted_values:
                    if not is_expected_release_name(value):
                        add(findings, path, line_no, "Current release pattern", EXPECTED["release_pattern"], value, line)
            elif re.search(r"\bv?\d+\.\d+\.\d+\b", line, flags=re.IGNORECASE) and "still watching" not in lower:
                add(findings, path, line_no, "Current release pattern", EXPECTED["release_pattern"], line.strip(), line)

        if "curseforge" in lower and re.search(r"\b(unsupported|not\s+supported|do\s+not\s+use|avoid)\b", lower):
            add(findings, path, line_no, "Supported install source", "CurseForge is supported", line.strip(), line)

        other_source = re.search(r"\b(modrinth|github releases?|github zip|source zip|zip download)\b", lower)
        install_claim = re.search(
            r"\b(supported|recommended|official|primary|playable|installer|install source|install\s+from|download\s+from)\b",
            lower,
        )
        negated = re.search(r"\bnot\b|\bnever\b|\bisn['’]?t\b|\bnot\s+the\s+playable\s+installer\b", lower)
        if other_source and install_claim and "curseforge" not in lower and not negated:
            add(findings, path, line_no, "Supported install source", "CurseForge", line.strip(), line)

        github_zip_claim = re.search(r"\bgithub\b.*\b(zip|source\s+code|archive)\b", lower)
        playable_claim = re.search(r"\b(playable|installer|installable|ready\s+to\s+play|use\s+as\s+the\s+installer)\b", lower)
        if github_zip_claim and playable_claim and not negated:
            add(
                findings,
                path,
                line_no,
                "GitHub ZIP installer",
                "GitHub ZIP is not the playable installer",
                line.strip(),
                line,
            )

    return findings


def main() -> int:
    root = Path.cwd()
    docs = doc_paths(root)
    findings: list[Finding] = []

    for path in docs:
        findings.extend(scan_file(path))

    print("Documentation facts guard")
    print("Source of truth:")
    print(f"- Project name: {EXPECTED['project_name']}")
    print(f"- Minecraft version: {EXPECTED['minecraft_version']}")
    print(f"- Loader: {EXPECTED['loader']}")
    print(f"- CurseForge Project ID: {EXPECTED['curseforge_project_id']}")
    print(f"- Current release pattern: {EXPECTED['release_pattern']}")
    print("- CurseForge is the supported install source")
    print("- GitHub ZIP is not the playable installer")
    print()
    print(f"Scanned {len(docs)} documentation file(s).")

    if not findings:
        print("No factual contradictions found. Omissions are allowed.")
        return 0

    print()
    print(f"Found {len(findings)} factual contradiction(s):")
    for finding in findings:
        display_path = finding.path.as_posix()
        print(
            f"::error file={display_path},line={finding.line_number},title={finding.rule} contradiction::"
            f"Expected {finding.expected}; found {finding.found}"
        )
        print(f"- {display_path}:{finding.line_number}")
        print(f"  Rule: {finding.rule}")
        print(f"  Expected: {finding.expected}")
        print(f"  Found: {finding.found}")
        print(f"  Line: {finding.line}")

    return 1


if __name__ == "__main__":
    sys.exit(main())
