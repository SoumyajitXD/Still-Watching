<!-- markdownlint-disable MD013 -->

# CI and Branch Protection Guide

This repository uses CI to protect the maintenance surface of **Still Watching**: documentation, metadata, release-facing HTML, links, workflow hygiene, and repository safety checks.

It does **not** build Minecraft, Forge, Java, Gradle, Maven, npm packages, or prove that a playable modpack works. Playable Still Watching releases belong on CurseForge.

---

## Project Baseline

| Item | Value |
| --- | --- |
| Project | Still Watching |
| Minecraft | `1.20.1` |
| Loader | Forge |
| Java | Java `17` where required |
| CurseForge Project ID | `1420406` |
| Current documented release | Still Watching V2.0.0 |
| RAM | `5 GB` minimum; `6–8 GB` preferred |
| Repository license | Apache-2.0 for original repository files only |

The CI should enforce consistency around this baseline, not pretend to validate every third-party mod or runtime behavior.

---

## Release-Facing Files

A version, modlist, or release-direction change should be checked across at least:

- `.github/ci/project-metadata.json`;
- `README.md`;
- `CHANGELOG.md`;
- `latest-modlist.md`;
- `installation-guide.md`;
- `docs/server-pack-guide.md`;
- `curseforge-description.html`;
- `SUPPORT.md`;
- `SECURITY.md`;
- `CONTRIBUTING.md`.

Updating one file while leaving nine stale is not release maintenance. It is documentation whack-a-mole.

---

## What CI Checks

The maintained validation script is:

```bash
python3 .github/ci/validate_repository.py all
```

It checks:

- required files and directories;
- project metadata drift;
- CurseForge-description HTML sanity;
- mod-list structure;
- internal links;
- workflow security policy;
- whitespace errors;
- suspicious committed secrets;
- merge-conflict markers;
- forbidden junk files;
- oversized files outside expected asset and release paths;
- dead references to deleted helper scripts.

Markdown linting should also run:

```bash
npx --yes markdownlint-cli2@0.18.1 "**/*.md" "!Releases/**"
```

For link-heavy edits:

```bash
python3 .github/ci/validate_repository.py links --external-links
```

CurseForge, shields, and CDN hosts can rate-limit or block CI user agents. Validation should distinguish a hostile robot gate from an actually broken project link.

---

## V2.0.0 Consistency Checks

Release validation should catch stale references to V1.1.2 when V2.0.0 is the current baseline, while allowing intentional historical references in migration notes and changelog history.

Human review should confirm:

- the modlist has 80 documented entries;
- V2.0.0 additions and removals are reflected in the changelog;
- README and CurseForge source describe Terralith, Tectonic, Incendium, Nullscape, Xaero's maps, and the optimization stack;
- migration docs warn about new worlds and JourneyMap data;
- server docs mention worldgen and dimension smoke tests;
- no removed mod is still advertised as current content.

---

## What CI Should Not Require

CI should **not** require:

- building or launching Minecraft;
- downloading every third-party dependency;
- proving that a GitHub ZIP is playable;
- bundling third-party mod JARs;
- generating release files from untrusted pull requests;
- runtime compatibility claims without an actual test environment.

Repository CI validates repository claims. It is not a séance that can infer whether eighty third-party components behave perfectly in-game.

---

## Recommended Branch Protection for Main

Recommended settings:

- Require a pull request before merging to `main`.
- Require CI checks before merging.
- Require branches to be up to date when practical.
- Block force pushes and deletion of `main`.
- Require conversation resolution.
- Require linear history when the maintainer prefers it.
- Optionally require signed commits when stricter provenance is worth the friction.

The goal is simple: make accidental breakage harder than doing the right thing.

---

## Workflow Security Rules

Keep the workflow boring and locked down:

- Use `pull_request`, not `pull_request_target`, for untrusted pull requests.
- Keep top-level permissions at `contents: read`.
- Pin marketplace actions to approved immutable SHAs.
- Use concurrency cancellation and job timeouts.
- Use `set -euo pipefail` in Bash steps.
- Do not grant write permissions without a clear reviewed reason.

CI should guard the door. It should not become the monster in the house.

---

## License Notes for Automation

Original repository files are Apache-2.0 licensed through [`../LICENSE`](../LICENSE). CI may validate those repository files.

That does not relicense Minecraft, Forge, CurseForge, third-party mods, screenshots, shaders, resource packs, sounds, textures, or external assets. CI should not encourage bundling or redistribution outside allowed channels.
