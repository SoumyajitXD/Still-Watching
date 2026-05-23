# Server Pack Guide

Use this when you run multiplayer. If server/client files drift, the fog is not haunted—your deployment is.

## Paths
1. **Hosted CurseForge installer path (recommended):** use host panel modpack installer for *Still Watching*.
2. **Official server pack path:** download matching file from CurseForge files page if provided.
3. **Manual Forge server path:** only if no official server pack; build from exact release artifacts.

## Source of truth

Use this order when resolving mod-side or server-pack questions:

1. Current CurseForge release files / manifest for **Still Watching V1.0.9**.
2. Actual pack files in this repository under `Releases/`, if present and relevant.
3. Official CurseForge pages for each mod.
4. Known dedicated-server testing results.
5. If none of that proves it, treat the side as `unknown` and the server action as `verify`.

Do not use this repository's generated mod list as proof of itself. That is circular logic wearing a fake mustache.

## Server-pack actions

- `keep` means the mod is needed server-side or shared by gameplay/worldgen/content.
- `remove` means it is safely client-only for a dedicated server.
- `verify` means the exact release file or server log still needs to prove the decision.

## Client-only removals

Use `latest-modlist.md` section **Server pack trimming candidates** as the working list, but only remove entries whose reason says they are dedicated-server safe. Anything marked `verify` is not free loot; test it first.

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
