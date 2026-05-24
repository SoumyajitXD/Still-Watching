# Server Pack Guide

Use this when you run multiplayer or prepare a dedicated server pack for **Still Watching V1.0.9**.

Target facts for this documented release:

| Item | Value |
| --- | --- |
| Minecraft | `1.20.1` |
| Loader | Forge |
| Java | Java 17 where required |
| Official install source | CurseForge |
| CurseForge Project ID | `1420406` |

If server/client files drift, the fog is not haunted. Your deployment is.

---

## Supported Paths

Use the least clever path that works.

1. **Hosted CurseForge installer path, recommended:** use the host panel modpack installer for **Still Watching**.
2. **Official server pack path:** download the matching server pack from the CurseForge files page if one is provided for the selected file.
3. **Manual Forge server path:** use only when you have verified the exact release files, mod sides, dependencies, and configs.

Do not build a server from the GitHub ZIP. It is not a playable installer and it is not proof that a dedicated server pack is correct.

---

## Source of Truth

Use this order when resolving mod-side or server-pack questions:

1. Current CurseForge release files or manifest for **Still Watching V1.0.9**.
2. Official server pack from the same CurseForge file, if available.
3. Actual release-side files in this repository under `Releases/`, if present and relevant.
4. Official CurseForge pages for each mod.
5. Dedicated-server testing logs for the exact release.
6. If none of that proves it, mark the decision as `verify` and test it.

Do not use this repository's generated mod list as proof of itself. That is circular logic wearing a fake mustache.

---

## Server-Pack Actions

| Action | Meaning |
| --- | --- |
| `keep` | Needed server-side or shared by gameplay, worldgen, content, libraries, commands, teams, quests, voice, or configs. |
| `remove` | Verified client-only for a dedicated server. |
| `verify` | Not proven safe. Test against the exact release and server log. |
| `unknown` | Treat like `verify`; the server does not care about confidence cosplay. |

Use [`latest-modlist.md`](../latest-modlist.md) section **Server pack trimming candidates** as a working list, not holy scripture. Only remove entries whose reason clearly says they are dedicated-server safe.

---

## Client-Only Warning

Dedicated servers should not load client-only code.

Common client-only categories include:

- shader loaders and shader packs;
- rendering, model, animation, or visual-only helpers;
- HUD, overlay, minimap, map renderer, or screenshot-only tools;
- client audio/ambience presentation mods unless the mod explicitly supports server-side behavior;
- performance mods that patch only the Minecraft client renderer.

That list is a warning, not a license to delete blindly. Some mods look client-shaped but still ship shared libraries or optional server hooks. If the exact release files or logs do not prove the side, keep it in `verify` until tested.

---

## Manual Server Build Checklist

Manual setup is advanced. If you are guessing, stop and use the host installer or official server pack.

1. Start with a fresh server folder.
2. Install the Forge server for Minecraft `1.20.1` using the Forge build required by the selected CurseForge release.
3. Use the same Still Watching version as every client.
4. Copy only server-compatible required mods.
5. Copy required `config/`, `defaultconfigs/`, and any release-required server files.
6. Keep `resourcepacks/` and `shaderpacks/` client-side unless a release note explicitly says otherwise.
7. Remove only verified client-only mods.
8. Start the server once, read `logs/latest.log`, then stop cleanly.
9. Fix missing dependency, wrong-side, or config errors before inviting players.
10. Join with one clean matching CurseForge client.

---

## Compare These Folders and Files

| Path | Why it matters |
| --- | --- |
| `mods/` | Required server/shared mods and dependencies. |
| `config/` | Main configuration. Some values must match clients. |
| `defaultconfigs/` | Defaults for new worlds and servers. |
| `serverconfig/` | Per-world server config after world creation. |
| `kubejs/` | Required only if present in the selected release. |
| `scripts/` | Required only if present in the selected release. |
| `resourcepacks/` | Usually client-side. Do not put on server unless required. |
| `shaderpacks/` | Client-side. Do not put on a dedicated server. |

---

## Crash Log Reading Quickstart

Check `logs/latest.log` first. Search for:

```text
Caused by:
Missing or unsupported mandatory dependencies
Attempted to load class
Dist.CLIENT
NoClassDefFoundError
Mod File
requires
mismatch
```

Common meanings:

| Log clue | Likely cause |
| --- | --- |
| `Dist.CLIENT` or client class errors | Client-only mod is on the dedicated server. |
| Missing dependency | Required library/mod was removed or not installed. |
| Mod version mismatch | Server and client or dependency versions differ. |
| Config sync/mismatch | Required configs differ. |
| Java/runtime error | Wrong Java or server launch command. |

Read the first meaningful error. The last line usually only describes the wreckage.

---

## Safe Testing Procedure

1. Fresh server folder.
2. Install the matching Still Watching release from CurseForge or the official matching server pack.
3. Start once and stop cleanly.
4. Join with a clean matching CurseForge client.
5. Generate new chunks.
6. Test basic survival, structures, deaths, voice/chat behavior if used, and reconnects.
7. Run a 15–30 minute multiplayer smoke test.
8. Back up before adding players or moving worlds.

---

## Final Checklist Before Inviting Players

- [ ] Same Still Watching version everywhere: **Still Watching V1.0.9** for this documented release.
- [ ] Minecraft `1.20.1` everywhere.
- [ ] Forge loader everywhere, with the selected release's required Forge build.
- [ ] Java 17 available where required.
- [ ] Installed from CurseForge or the matching official server pack.
- [ ] CurseForge Project ID checked: `1420406`.
- [ ] Required configs copied.
- [ ] Client-only mods removed only after verification.
- [ ] No unresolved `unknown` or `verify` decisions in a production pack.
- [ ] Backups created.

If that sounds boring, good. Servers should be boring. The horror belongs in-game, not in the console.
