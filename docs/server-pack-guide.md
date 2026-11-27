<!-- markdownlint-disable MD013 -->

# Server Pack Guide

This guide covers **Still Watching V2.0.x**, including V2.0.2, dedicated servers on Minecraft `1.20.1` with Forge and Java `17` where required.

Use CurseForge as the source of playable files. The GitHub ZIP is not the recommended playable installer and is not a server pack.

---

## Baseline

| Item | Value |
| --- | --- |
| Project | Still Watching |
| Minecraft | `1.20.1` |
| Loader | Forge |
| Java | Java `17` where required |
| CurseForge Project ID | `1420406` |
| Current documented release | Still Watching V2.0.2 |
| RAM | `5 GB` minimum; `6–8 GB` preferred for small groups |
| Repository license | Apache-2.0 for original repository files only |

> [!WARNING]
> V2.0.0 changes Overworld, Nether, End, and structure generation. Back up existing server worlds and test migrations in a disposable copy. A new world is strongly recommended.

Start with the simplest supported installation method. Only assemble a server manually if you can verify the required mods and configs.

---

## V2.0.2 Compatibility Note

V2.0.2 updates selected mod versions. A matching dedicated-server pack and runtime compatibility have not been verified here.

- Use the exact selected release and matching Forge build on server and clients.
- Keep shader packs out of the dedicated server's mod directory. Check each mod's distribution-side requirements.
- Verify the exact Forge 1.20.1 artifacts, including FTB entries whose project titles mention NeoForge.
- Back up the server and test startup, joining, world generation, dimension travel, and voice chat before replacing the live instance.

Do not assume a client release automatically provides an official server pack.

---

## Best Setup Path

| Rank | Path | Use when |
| --- | --- | --- |
| 1 | Hosting-provider CurseForge installer | Your host supports CurseForge modpack installation. |
| 2 | Official server pack from CurseForge | The selected CurseForge file provides a server pack. |
| 3 | Manual Forge server | You can verify sides, dependencies, worldgen files, configs, and logs yourself. |

Use the manual path only if you can verify each required dependency and configuration file.

---

## Non-Negotiable Rules

1. Start from the official CurseForge release or official server-pack instructions.
2. Keep the server, every client, configs, datapacks, and modpack version matched.
3. Match Minecraft `1.20.1` and the required Forge build.
4. Back up worlds before updates, migrations, config edits, or mod removals.
5. Do not copy the entire V1.1.2 configuration set into the new installation.
6. Do not upload client-only visual, shader, UI, map, menu, audio-only, or rendering files unless the author explicitly supports them server-side.
7. Test startup, world generation, joining, voice chat, structures, Nether travel, End travel, respawn, and map-independent gameplay before inviting players.
8. Keep logs. A crash without logs is not actionable.

---

## V2.0.0 World-Generation Warning

The V2.0.0 server world depends on a changed generation stack, including Terralith, Tectonic, Incendium, Nullscape, Lithostitched, Dungeons and Taverns, Explorify, and Towns and Towers.

Migrating a V1.1.2 world can cause:

- hard borders between old and new terrain;
- different biome layouts in unexplored chunks;
- changed Nether and End generation;
- removed-mod blocks or structures remaining in generated chunks;
- new structures appearing only in newly generated areas;
- increased CPU pressure while several players generate new terrain.

A new V2.0.0 world is recommended. If you need to keep an old world, test a disposable copy first and expect some terrain borders to remain.

---

## Path A: Hosting-Provider Installer

1. Open the hosting control panel.
2. Find the **CurseForge**, **Modpacks**, or **Modpack Installer** area.
3. Search for **Still Watching**.
4. Select **V2.0.2** or the exact release used by every client.
5. Install the pack.
6. Start the server once.
7. Check the console for missing dependencies, wrong Java, memory errors, or worldgen failures.
8. Create a disposable test world.
9. Join with one clean matching client before inviting the group.

If the provider installer works, there is no need to assemble the server manually.

---

## Path B: Official Server Pack

Use this only if the selected CurseForge release provides a server pack.

1. Open the [Still Watching Files page](https://www.curseforge.com/minecraft/modpacks/still-watching/files).
2. Choose the exact client version.
3. Download the matching server pack when available.
4. Extract it into a clean folder.
5. Read included server notes.
6. Run the included start script or Forge server jar.
7. Accept the Minecraft EULA when prompted.
8. Restart the server.
9. Inspect logs and console output.
10. Test a new world and one matching client.

Use the same Still Watching release on the server and every client.

---

## Path C: Manual Forge Server

Manual setup is advanced and unsupported unless verified for the exact release.

1. Install a clean Forge `1.20.1` server.
2. Use the Forge build required by the selected CurseForge release.
3. Copy only server-compatible mods and required libraries.
4. Copy required configs, default configs, datapacks, and worldgen data.
5. Remove client-only files.
6. Allocate server RAM.
7. Start the server and read the first failure in the log.
8. Fix errors before inviting players.
9. Generate a disposable test world.
10. Test Overworld, Nether, End, structures, respawn, voice chat, and joining with one clean client.

Check which side each mod supports before placing it on a dedicated server.

---

## Client-Only Categories to Treat Carefully

These categories commonly cause dedicated-server problems unless the author says otherwise:

- shader loaders and shader packs;
- visual-only or rendering mods;
- HUD, menu, title-screen, minimap, and world-map mods;
- audio-only client mods;
- resource packs;
- screenshot, camera, or client-presentation tools;
- background FPS reducers and other client lifecycle tools.

Some mods have both client and server behavior. Some libraries are required on both sides. Check each mod's documented side support and dependencies rather than relying on its filename.

---

## Files and Folders to Preserve

| Path | Why it matters |
| --- | --- |
| World folder | Terrain, player data, dimensions, structures, and world state |
| `config/` | Global mod configuration |
| `defaultconfigs/` | Templates applied to new worlds |
| `serverconfig/` | Per-world server configuration |
| Datapack and worldgen files | Required generation behavior for the selected release |
| `ops.json` | Operator list |
| `whitelist.json` | Whitelist |
| Ban files | Ban data |
| `server.properties` | Core server settings |
| `logs/` | Evidence when things break |

Stop the server cleanly before copying these files. Keep at least one backup outside the server directory and verify that it restores into a separate test instance.

---

## Minimum Smoke Test

- [ ] Server starts with no fatal errors.
- [ ] One clean matching client can join.
- [ ] A new world generates on the selected release.
- [ ] Existing-world backup restores correctly, if migration is being tested.
- [ ] Common structures generate without immediate crashes.
- [ ] Nether portal travel works.
- [ ] End portal travel works.
- [ ] Voice chat is configured and tested when used.
- [ ] Respawn works.
- [ ] Logs are accessible.
- [ ] Backups exist outside the live server folder.

These checks cover basic startup and gameplay, not long-session stability or load testing.

---

## Common Failures

| Problem | Likely cause | First fix |
| --- | --- | --- |
| Server crashes before world load | Wrong Forge, wrong Java, missing dependency, or client-only file | Read the first fatal error and rebuild from a supported path. |
| New world fails to generate | Missing or mismatched worldgen dependency, config, or datapack | Reinstall the exact selected server set and compare logs. |
| Client cannot join | Pack version, Forge build, configs, or files differ | Match the exact CurseForge release on server and clients. |
| Severe lag during exploration | Multiple players generating terrain, high view distance, weak CPU, or heavy entities | Reduce load and test world generation with fewer players. |
| Broken old-world terrain | Major generator migration | Restore backup or accept seams; prefer a new world. |
| Voice chat fails | Port, firewall, host panel, or mod config issue | Check networking and Simple Voice Chat configuration. |
| Players see different behavior | Config or mod mismatch | Recopy required files from the exact release. |

---

## RAM and Hosting Notes

The pack baseline is `5 GB` minimum and `6–8 GB` preferred. Server needs depend on player count, view distance, world generation, structures, exploration speed, and host CPU quality.

Start conservative:

- small private group: `6–8 GB` server RAM when the host allows it;
- lower view and simulation distance if TPS suffers;
- avoid sending several players in different directions during initial terrain generation;
- test all dimensions before a real session;
- avoid extra mods unless you can debug the consequences.

More RAM cannot fix an incompatible mod, incorrect config or CPU bottleneck.

---

## Updating a Server

1. Announce downtime.
2. Stop the server cleanly.
3. Back up the world, configs, whitelist, operators, and server settings.
4. Preserve the original backup outside the live server folder.
5. Install the new CurseForge server release path.
6. Match every client to the same pack version.
7. Test a new disposable world first.
8. Test a copy of the old world only if migration is required.
9. Inspect logs, terrain generation, structures, Nether, End, and joining.
10. Open the real world only after the update passes basic checks.

Do not test an update for the first time on the only live world.

---

## License and Redistribution

Original repository files are licensed under [Apache License 2.0](../LICENSE). That license does **not** grant permission to redistribute Minecraft, Forge, CurseForge assets, third-party mod JARs, shaders, resource packs, sounds, textures, logos, or external project content outside their own licenses and terms.

Do not publish unofficial Still Watching server packs unless every included file permits it. When in doubt, link users to CurseForge instead of rehosting files.
