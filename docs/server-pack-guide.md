# Server Pack Guide

Use this when you run multiplayer. If server/client files drift, the fog is not haunted—your deployment is.

## Paths
1. **Hosted CurseForge installer path (recommended):** use host panel modpack installer for *Still Watching*.
2. **Official server pack path:** download matching file from CurseForge files page if provided.
3. **Manual Forge server path:** only if no official server pack; build from exact release artifacts.

## Client-only candidates
Use `latest-modlist.md` section **Server pack trimming candidates** as likely removals. Verify before deleting.

## Unknown-side warning
Mods marked unknown/verify are not safe assumptions. Test with logs before production.

## Crash log reading quickstart
- Check `logs/latest.log` first.
- Look for `Caused by:` and missing class/mod IDs.
- Compare against client extras and removed mods.

## Compare these folders/files
- `mods/`
- `config/`
- `defaultconfigs/`
- `kubejs/` (if present)
- `scripts/` (if present)
- `resourcepacks/` and `shaderpacks/` should stay client-side unless explicitly required

## Safe testing procedure
1. Fresh server folder.
2. Install matching pack version.
3. Start once, stop cleanly.
4. Join with clean client.
5. Generate new chunks.
6. Run 15–30 minute multiplayer smoke test.

## Final checklist before inviting players
- Same Still Watching version everywhere.
- Minecraft `1.20.1`, Forge match, Java 17 where required.
- Backups created.
- No unresolved unknown-side mod decisions.
