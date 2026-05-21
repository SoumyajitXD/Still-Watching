# Contributing

## What we accept
- Reproducible bug fixes in docs/validation/release-side files.
- Clear documentation improvements with the pack's horror tone.
- Automation that keeps metadata/modlist consistent.

## What we reject
- "Add random horror mods" requests without reproducible design/testing evidence.
- Claims that GitHub ZIP is a playable installer.

## Tone
Keep it sharp, direct, horror-flavored. No corporate filler.

## Local validation
```bash
python .github/scripts/generate_docs.py
python .github/scripts/validate.py all
```

## Updating mod metadata
1. Edit `data/mods.yml` from real release evidence.
2. Keep unknown side labels when unsure.
3. Regenerate `latest-modlist.md`.

## Bug reports
Use issue templates with logs, reproduction steps, and clean-install status.
