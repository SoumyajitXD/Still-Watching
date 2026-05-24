# Release Checklist

Use this before publishing or touching release-facing docs. The goal is simple: ship dread, not contradictions.

Current documented baseline:

| Item | Value |
| --- | --- |
| Release | Still Watching V1.0.9 |
| Minecraft | `1.20.1` |
| Loader | Forge |
| Java | Java 17 where required |
| Official install source | CurseForge |
| CurseForge Project ID | `1420406` |

## Pre-Release Checks

- Confirm `data/project.yml` reflects the actual release facts.
- Confirm CurseForge remains the official playable install source.
- Confirm the GitHub ZIP is never described as a playable installer.
- Run docs generation only when source data changed:

```bash
python .github/scripts/generate_docs.py
```

- Run validation:

```bash
python .github/scripts/validate.py all
```

- Run whitespace checks:

```bash
git diff --check
```

## CurseForge File Checks

- Upload only tested build files.
- Verify project ID `1420406`.
- Verify Minecraft `1.20.1`.
- Verify Forge loader.
- Try to inspect the exact CurseForge file manifest or matching release archive for **Still Watching V1.0.9** before changing exact mod membership, versions, file IDs, overrides, or server-pack claims.
- If the exact V1.0.9 manifest/server pack is not accessible, keep exact mod metadata marked as requiring manifest/server-pack verification. Do not invent exact versions or exact membership.
- Keep Java 17 guidance where relevant.
- Confirm the CurseForge file changelog does not conflict with GitHub `CHANGELOG.md`.
- Do not promise a server pack unless the selected CurseForge file actually provides one.

## Version Bump Checklist

- Update `current_release` in `data/project.yml`.
- Update README, installation guide, CurseForge description source, support/security docs, and changelog references.
- Add a changelog entry.
- Regenerate generated docs if source metadata changed.
- Validate before commit.

## Modlist Update Checklist

- Update `data/mods.yml` from release source files, not memory.
- Keep `unknown` or `verify` side labels where proof is missing.
- Regenerate `latest-modlist.md`.
- Do not convert client-only guesses into server-pack facts.

## Server Pack Verification Checklist

- Check hosted CurseForge installer path first.
- If an official server pack exists, test it clean with the matching client version.
- Verify client-only trims against the exact release files or logs.
- Leave uncertain mods as `verify` until tested.
- Back up worlds before production updates.

## Screenshot and Gallery Checklist

- Ensure screenshots reflect the current release tone and content.
- Remove misleading outdated UI/version captures.
- Do not imply features, shaders, or settings that are not part of the documented release.

## Sponsor Content Checklist

- Keep sponsor marker block unchanged.
- Keep required sponsor link and banner intact.
- Do not move sponsor content into a place where it gets lost, hidden, or stripped by tooling.

## Post-Release Checks

- Verify the CurseForge file page is live.
- Verify README quick links.
- Open one issue template smoke test.
- Check that docs still agree on release, Minecraft, Forge, Java, CurseForge source, and Project ID.

## If GitHub Docs and CurseForge Disagree

- CurseForge is the source of truth for playable release files.
- Fix GitHub docs immediately.
- Note the mismatch in changelog or an issue when useful.
- Do not patch the mismatch with fake certainty. That is how documentation becomes fan fiction.
