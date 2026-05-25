# Release Checklist

Use this checklist before publishing or editing release-facing files.

## Before release

- Confirm the playable pack file is published through CurseForge.
- Confirm README, installation guide, CurseForge description, and latest modlist all describe the same documented release.
- Confirm Minecraft version is `1.20.1` and loader is Forge.
- Confirm Java guidance still says Java `17` where relevant.
- Preserve the required BisectHosting sponsor block and links.
- Run local validation:

```bash
python .github/scripts/validate.py all
```

## After release

- Check the CurseForge page and files page.
- Check GitHub links and issue templates.
- Do not upload random generated ZIPs unless they are intentional release-side artifacts.

Boring release hygiene prevents exciting public disasters.
