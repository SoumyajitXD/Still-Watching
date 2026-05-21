# Release Checklist

## Pre-release checks
- Confirm `data/project.yml` reflects reality.
- Run `python .github/scripts/generate_docs.py`.
- Run `python .github/scripts/validate.py all`.

## CurseForge file checks
- Upload only tested build files.
- Verify project ID `1420406`, Minecraft `1.20.1`, Forge, Java 17 guidance.
- Confirm file changelog matches GitHub `CHANGELOG.md`.

## Version bump checklist
- Update `current_release` in `data/project.yml`.
- Update README/installation/CurseForge description references.
- Add changelog entry.

## Modlist update checklist
- Update `data/mods.yml` from release source files.
- Regenerate `latest-modlist.md`.
- Keep unknown side labels where proof is missing.

## Server pack verification checklist
- Check hosted installer path first.
- If official server pack exists, test it clean.
- Verify client-only trims and unknown-side mods before production.

## Screenshot/gallery checklist
- Ensure screenshots reflect current release tone and content.
- Remove misleading outdated UI/version captures.

## Sponsor-content checklist
- Keep sponsor marker block unchanged.
- Keep required sponsor link/banner intact.

## Post-release checks
- Verify CurseForge file page is live.
- Verify README quick links.
- Open one smoke-test issue template.

## If GitHub docs and CurseForge disagree
- CurseForge is source of truth for playable release.
- Fix GitHub docs immediately and note mismatch in changelog/issue.
