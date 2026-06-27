<!-- markdownlint-disable MD013 -->

# Server Pack Guide

Still Watching servers should stay predictable in the places where predictability saves worlds. This guide is for the current documented release, **Still Watching V1.1.2**, targeting Minecraft `1.20.1` on Forge with Java `17` when required.

Use CurseForge as the source of playable files. The GitHub ZIP is not a playable installer and is not a server pack.

---

## Baseline

| Item | Value |
| --- | --- |
| Project | Still Watching |
| Minecraft | `1.20.1` |
| Loader | Forge |
| Java | Java `17` where required |
| CurseForge Project ID | `1420406` |
| Current documented release | Still Watching V1.1.2 |
| RAM | `5 GB` minimum; `6–8 GB` preferred for small groups |
| Repository license | Apache-2.0 for original repository files only |

This guide is deliberately conservative. A server that starts cleanly and lets players join is better than an impressive manual file experiment that collapses into a crash log.

---

## Best Setup Path

Use these paths in order.

| Rank | Path | Use when |
| --- | --- | --- |
| 1 | Hosting provider CurseForge installer | Your host supports CurseForge modpack installation. |
| 2 | Official server pack from CurseForge | The selected CurseForge file provides a server pack. |
| 3 | Manual Forge server | You can verify sides, dependencies, configs, and logs yourself. |

Manual setup is the failure-prone path. Use it only when you know what each file is doing.

---

## Non-Negotiable Rules

1. Start from the official CurseForge release or official server-pack instructions when available.
2. Keep the server, every client, configs, and modpack version matched.
3. Match Minecraft `1.20.1` and the required Forge build for the selected release.
4. Back up worlds before updates, migrations, config edits, or mod removals.
5. Do not upload client-only visual, shader, UI, map, menu, audio-only, or rendering-only files to a dedicated server unless the mod author explicitly supports that file server-side.
6. Test startup, world generation, joining, voice chat, common travel, structures, and respawn behavior before inviting players.
7. Keep logs. A crash without logs is not actionable.

---

## Path A Hosting Provider Installer

This is the recommended route for most servers.

1. Open your hosting control panel.
2. Find the **CurseForge**, **Modpacks**, or **Modpack Installer** area.
3. Search for **Still Watching**.
4. Select the exact pack version that clients will use.
5. Install the pack.
6. Start the server once.
7. Check the console for missing dependencies, wrong Java, or memory errors.
8. Join with one clean matching client before inviting the full group.

If this works, do not replace it with manual assembly just because manual work feels more technical. The goal is a stable server.

---

## Path B Official Server Pack

Use this only if the selected CurseForge release provides a server pack.

1. Open the [Still Watching Files page](https://www.curseforge.com/minecraft/modpacks/still-watching/files).
2. Choose the exact client version.
3. Download the server pack if one is available for that file.
4. Extract it into a clean folder.
5. Read any included server notes.
6. Run the included start script or Forge server jar.
7. Accept the Minecraft EULA when prompted.
8. Restart the server.
9. Check logs and console output.
10. Join with a matching clean client.

Never mix a server pack from one release with clients from another. That is dependency roulette.

---

## Path C Manual Forge Server

Manual setup is advanced and unsupported unless verified for the exact release.

1. Install a clean Forge `1.20.1` server.
2. Use the Forge build required by the selected CurseForge release.
3. Copy only server-compatible mods.
4. Copy required configs and default configs.
5. Remove client-only files.
6. Allocate server RAM.
7. Start the server.
8. Read the first failure in the log, not the loudest one.
9. Fix errors before inviting players.
10. Test with one clean matching client.

Do not claim a file is server-safe because it looks harmless. Side mistakes are how servers fail.

---

## Client-Only Categories to Treat Carefully

These categories are common dedicated-server problems unless the mod author says otherwise:

- shader loaders;
- shader packs;
- visual-only mods;
- client rendering or performance mods;
- HUD-only mods;
- menu or title-screen mods;
- minimap, world-map, or map-rendering mods;
- audio-only or client-audio mods;
- resource packs;
- screenshot, camera, or client presentation tools.

Some mods have both client and server behavior. Some libraries are required on both sides. Do not infer side support from vibes, file names, or wishful thinking.

---

## Files and Folders to Preserve

When building, updating, or moving a server, preserve the files that actually carry state.

| Path | Why it matters |
| --- | --- |
| World folder | Terrain, player data, dimensions, structures, and world state |
| `config/` | Global mod configuration |
| `defaultconfigs/` | Templates applied to new worlds |
| `serverconfig/` | Per-world server config |
| `ops.json` | Operator list |
| `whitelist.json` | Whitelist |
| Ban files | Ban data |
| `server.properties` | Core server settings |
| `logs/` | Evidence when things break |

Back up before editing any of these. An untested backup is not a backup; it is optimism with a file extension.

---

## Minimum Smoke Test

Before inviting players, run this checklist.

- [ ] Server starts with no fatal errors.
- [ ] One clean matching client can join.
- [ ] A new test world generates.
- [ ] Existing world backup restores correctly, if applicable.
- [ ] Voice chat is configured and tested if used.
- [ ] Common structures generate without immediate crashes.
- [ ] Basic exploration works in overworld, caves, and structures.
- [ ] Respawn works.
- [ ] Logs are accessible.
- [ ] Backups exist outside the live server folder.

This does not prove the server is perfect. It proves the basics are not obviously broken.

---

## Common Failure Table

| Problem | Likely cause | First fix |
| --- | --- | --- |
| Server crashes before world load | Wrong Forge, wrong Java, missing dependency, or client-only file | Read the first fatal error and rebuild from a supported path. |
| Client cannot join | Pack version, Forge build, configs, or files differ | Match the exact selected CurseForge release on server and clients. |
| Missing mod error | Manual assembly missed a dependency | Use host installer or official server pack. |
| Classloading or rendering error | Client-only code on the dedicated server | Remove wrong-side files and test again. |
| Low TPS | RAM, CPU, view distance, entity load, or worldgen pressure | Lower load, check logs, and avoid overallocating. |
| Voice chat fails | Port, firewall, host panel, or mod config issue | Check host networking and Simple Voice Chat config. |
| World breaks after update | No backup or unsafe version jump | Restore backup and test update in a disposable copy. |
| Players have different behavior | Config mismatch | Recopy required configs from the selected release. |

---

## RAM and Hosting Notes

The modpack baseline is `5 GB` minimum and `6–8 GB` preferred. For servers, actual needs depend on player count, view distance, worldgen, structures, exploration speed, and host CPU quality.

Start conservative:

- small private group: `6–8 GB` server RAM if the host allows it;
- lower view distance if TPS suffers;
- pre-test world generation before a real session;
- avoid running heavy extra mods unless you can debug the consequences.

More RAM does not fix every problem. A weak CPU, broken config, or wrong-side mod will still cause failures.

---

## Updating a Server

1. Announce downtime.
2. Stop the server cleanly.
3. Back up the world, configs, whitelist, operator files, and server settings.
4. Install the new CurseForge server release path.
5. Match every client to the same pack version.
6. Start the server and read logs.
7. Test a disposable copy or test world first.
8. Open the real world only after the update passes basic checks.

Do not test an update for the first time on the only live world.

---

## License and Redistribution Notes

Original repository files are licensed under [Apache License 2.0](../LICENSE), commonly identified as **Apache-2.0**.

That license does **not** grant permission to redistribute Minecraft, Forge, CurseForge assets, third-party mod JARs, third-party assets, shaders, resource packs, sounds, textures, screenshots containing third-party content, logos, or external project content outside their own licenses and terms.

Do not publish unofficial Still Watching server packs unless you are certain every included file allows it. When in doubt, link users to CurseForge instead of rehosting files.

---

## When in Doubt

If a file's side is unclear, do not guess. Check the CurseForge page, mod author notes, issue tracker, license information, or test a throwaway dedicated server first.

Guessing at Forge server files is not bravery. It is just feeding the crash log.