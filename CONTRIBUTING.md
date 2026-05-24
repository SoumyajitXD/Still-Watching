# Contributing

Still Watching accepts useful work, not random noise wearing a pull request costume.

Current documented baseline:

| Item | Value |
| --- | --- |
| Release | Still Watching V1.0.9 |
| Minecraft | `1.20.1` |
| Loader | Forge |
| Java | Java 17 where required |
| Official install source | CurseForge |
| CurseForge Project ID | `1420406` |

## What We Accept

- Documentation fixes that help players, server admins, or maintainers.
- Reproducible bug reports with logs and clean-install status.
- Compatibility notes backed by testing on the documented release.
- Corrections to broken links, metadata, credits, attribution, or release facts.
- Validation or automation changes that keep docs and release-side files consistent.

## What We Reject

- Claims that the GitHub ZIP is a playable installer.
- Random mod requests with no design reason, testing, or compatibility evidence.
- Server-pack guesses presented as fact.
- Crash reports with no logs, no reproduction steps, and no clean baseline.
- Edits that flatten the pack into generic modpack paste.
- Changes that remove, weaken, or damage required sponsor content.

## Tone

Keep it sharp, direct, and horror-flavored. No corporate fog machine. No bland wiki sludge. The pack has personality; do not sandblast it into beige.

That said, personality is not a permission slip for fake certainty. If something is unverified, say so.

## Before You Edit Release-Facing Docs

Run the generator only when you are intentionally updating generated files from source data:

```bash
python .github/scripts/generate_docs.py
```

Always run validation before committing release-facing documentation:

```bash
python .github/scripts/validate.py all
```

Also check whitespace before shipping:

```bash
git diff --check
```

## Updating Mod Metadata

1. Edit `data/mods.yml` only from real release evidence.
2. Keep `unknown` or `verify` labels when side/support proof is missing.
3. Do not call a mod server-safe because it "looks client-only".
4. Regenerate `latest-modlist.md` after metadata changes.
5. Validate the repository.

## Bug Reports

Use the issue templates. Include logs, reproduction steps, version details, and whether the issue happens on a clean CurseForge install.

A useful report gives someone a trail to follow. A useless report just screams in the woods and expects the trees to debug Java.
