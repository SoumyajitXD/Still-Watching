<!-- markdownlint-disable MD013 -->

# CI and Branch Protection Guide

This repository uses CI to protect the maintenance surface of **Still Watching**: documentation, metadata, release-facing HTML, links, workflow hygiene, and repository safety checks.

It does **not** build Minecraft, Forge, Java, Gradle, Maven, npm packages, or a playable modpack. The playable Still Watching release belongs on CurseForge.

---

## Project Baseline

| Item | Value |
| --- | --- |
| Project | Still Watching |
| Minecraft | `1.20.1` |
| Loader | Forge |
| Java | Java `17` where required |
| CurseForge Project ID | `1420406` |
| Current documented release | Still Watching V1.1.2 |
| RAM | `5 GB` minimum; `6–8 GB` preferred |
| Repository license | Apache-2.0 for original repository files only |

The CI should enforce consistency around this baseline, not pretend to validate every third-party mod or runtime behavior.

---

## What CI Checks

The maintained validation script is:

```bash
python3 .github/ci/validate_repository.py all
```

It checks:

- required files and required directories;
- project metadata drift;
- CurseForge description HTML sanity;
- mod-list structure;
- internal links;
- workflow security policy;
- whitespace errors;
- suspicious committed secrets;
- merge conflict markers;
- forbidden junk files;
- oversized files outside expected asset and release paths;
- dead references to deleted helper scripts.

Markdown linting should also run for normal documentation hygiene:

```bash
npx --yes markdownlint-cli2@0.18.1 "**/*.md" "!Releases/**"
```

For link-heavy edits, maintainers can also run:

```bash
python3 .github/ci/validate_repository.py links --external-links
```

CurseForge, shields, and CDN hosts can rate-limit or block CI user agents. The validation script treats those hosts more carefully so useful checks do not fail because a public host dislikes robots.

---

## What CI Should Not Require

CI should **not** require:

- building Minecraft;
- launching the modpack;
- downloading every third-party dependency;
- proving that a GitHub ZIP is playable;
- bundling third-party mod JARs;
- generating release files from untrusted pull requests;
- a changelog file.

The repository no longer requires `CHANGELOG.md`. Release history should live in the appropriate release pages, CurseForge file notes, commit history, or project documentation chosen by the maintainer.

---

## Recommended Branch Protection for Main

Repository settings cannot be enforced from a Markdown patch, but `main` should be protected.

Recommended settings:

- Require a pull request before merging to `main`.
- Require the CI workflow checks before merging.
- Require branches to be up to date before merging when practical.
- Block force pushes to `main`.
- Block deletion of `main`.
- Require conversation resolution before merge.
- Require linear history if the maintainer prefers a cleaner commit graph.
- Optionally require signed commits if stricter provenance is worth the friction.

The goal is simple: make accidental breakage harder than doing the right thing.

---

## Workflow Security Rules

Keep the workflow boring and locked down:

- Use `pull_request`, not `pull_request_target`, for untrusted pull requests.
- Keep top-level permissions to `contents: read`.
- Pin marketplace actions to approved immutable SHAs.
- Use concurrency cancellation.
- Add job timeouts.
- Use `set -euo pipefail` in Bash steps.
- Do not grant write permissions unless a future workflow has a clear, reviewed reason.

CI should guard the door. It should not become the monster in the house.

---

## License Notes for Automation

Original repository files are Apache-2.0 licensed through [`../LICENSE`](../LICENSE). CI may validate those repository files.

That does not relicense Minecraft, Forge, CurseForge, third-party mods, screenshots containing third-party content, shaders, resource packs, sounds, textures, or external assets. CI should not encourage bundling or redistributing third-party files outside their allowed channels.
