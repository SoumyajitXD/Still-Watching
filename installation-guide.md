<!-- markdownlint-disable MD013 -->

# Still Watching Installation Guide

This guide covers installing, updating, migrating, backing up, troubleshooting, and hosting **Still Watching**, a Minecraft Java Edition horror-survival modpack by **Soumyajit** for **Minecraft `1.20.1`** on **Forge**.

Current documented release: **Still Watching V2.0.2**.

---

## Project Baseline

| Item | Value |
| --- | --- |
| Project | Still Watching |
| Minecraft | `1.20.1` |
| Loader | Forge |
| Java | Java `17` if the launcher or server asks |
| CurseForge Project ID | `1420406` |
| Current documented release | Still Watching V2.0.2 |
| RAM | `5 GB` minimum; `6–8 GB` preferred |
| Repository license | Apache-2.0 for original repository files only |

> [!IMPORTANT]
> CurseForge is the supported playable source. The GitHub ZIP is **not** the recommended playable modpack installer and is **not** a server pack.

<!-- Separate independent alerts for Markdown rendering and MD028 lint. -->

> [!WARNING]
> V2.0.0 changes Overworld, Nether, End, structure, and mapping systems. A new world is strongly recommended. Back up old worlds before testing the update.

---

## Official Links

| Resource | Link |
| --- | --- |
| CurseForge project | [Still Watching on CurseForge](https://www.curseforge.com/minecraft/modpacks/still-watching) |
| CurseForge files | [Still Watching Files](https://www.curseforge.com/minecraft/modpacks/still-watching/files) |
| GitHub issues | [Report an issue](https://github.com/SoumyajitXD/Still-Watching/issues) |
| Changelog | [CHANGELOG.md](./CHANGELOG.md) |
| Latest mod list | [latest-modlist.md](./latest-modlist.md) |
| Server guide | [docs/server-pack-guide.md](./docs/server-pack-guide.md) |
| Support policy | [SUPPORT.md](./SUPPORT.md) |

If GitHub and CurseForge disagree about a playable release, trust CurseForge first and report the mismatch with evidence.

---

## Requirements

| Requirement | Details |
| --- | --- |
| Minecraft edition | Minecraft: Java Edition |
| Minecraft version | `1.20.1` |
| Loader | Forge |
| Recommended installer | CurseForge App |
| Java | Java `17` if the launcher or server asks |
| RAM | `5 GB` minimum; `6–8 GB` preferred |
| Disk space | `5–10 GB` recommended |
| Internet | Required for download and dependency installation |
| Audio | Headphones recommended for direction and atmosphere |
| CurseForge Project ID | `1420406` |

Leave enough memory for Windows or your operating system and any background applications. On an 8 GB system, close unnecessary apps before launching.

---

## Clean Installation

1. Install the [CurseForge App](https://www.curseforge.com/download/app).
2. Open **Minecraft** in CurseForge.
3. Search for **Still Watching**.
4. Verify the project details:
   - Name: **Still Watching**.
   - Creator: **Soumyajit**.
   - Minecraft: **`1.20.1`**.
   - Loader: **Forge**.
5. Install **Still Watching V2.0.2** or the newest compatible release.
6. Allocate RAM if needed.
7. Launch once with **no extra mods, shaders, resource packs, or config edits**.
8. Create a new test world.
9. Confirm world generation, dimensions, audio, controls, menus, maps, and FPS are playable.

Confirm that the unmodified pack works before testing additional mods or settings.

---

## Updating to V2.0.2

V2.0.2 is a minor update to selected bundled mod versions. V2.0.1 previously added Zepholume Shaders and Configured and removed Chloride and TACZ: Durability.

1. Back up the previous profile, worlds, configs, and personal settings.
2. Install the exact V2.0.2 CurseForge release in a separate profile before replacing a working instance.
3. Launch without extra mods or shaders, then test a new world and a disposable copy of the old save.
4. Verify the required Forge build and dependencies from the selected release.
5. Match the exact pack version on all multiplayer clients and the server, if applicable.

Do not assume a minor update guarantees world or configuration compatibility. See the [changelog](./CHANGELOG.md) and [V2.0.1 content inventory](./latest-modlist.md) for context.

---

## Updating from V1.1.2

The safest migration is a fresh profile, not an overwrite.

1. Back up the complete V1.1.2 instance.
2. Back up every important world separately.
3. Preserve the old `journeymap/` folder if its waypoints or map tiles matter.
4. Install the current V2.0.x release as a fresh CurseForge profile.
5. Do **not** copy the entire old `config/` folder into the new profile.
6. Reapply only personal settings you understand, such as keybinds, shader choice, voice-chat preferences, and graphics options.
7. Create a new world for the intended V2.0.0 terrain and structure experience.
8. Test an old world only from a disposable copy.

### Why a New World Is Recommended

V2.0.0 replaces or adds major world-generation systems:

- Terralith and Tectonic reshape the Overworld.
- Incendium changes Nether generation.
- Nullscape changes End generation.
- Dungeons and Taverns changes the structure mix.
- Several V1.1.2 biome and structure mods were removed.

Old worlds can show hard chunk borders, changed biome transitions, new structures only in unexplored chunks, removed-mod remnants, and inconsistent dimension generation.

### JourneyMap to Xaero's Maps

JourneyMap was removed. V2.0.0 uses Xaero's Minimap and Xaero's World Map.

JourneyMap data does not automatically migrate. Keep the old `journeymap/` folder as an archive if you need its waypoints or explored map tiles.

---

## RAM Allocation

| System RAM | Suggested Minecraft RAM |
| --- | --- |
| 8 GB | `5 GB`; close background apps |
| 12 GB | `5–6 GB` |
| 16 GB | `6–8 GB` |
| 32 GB or more | `8 GB` |

| RAM | MB value |
| --- | ---: |
| `5 GB` | `5120 MB` |
| `6 GB` | `6144 MB` |
| `8 GB` | `8192 MB` |

Allocating more RAM than needed does not guarantee better performance. Leave memory for the operating system, background apps and integrated graphics. On an 8 GB PC, start at 5 GB rather than assigning 6–8 GB and forcing the system to page to disk. If the pack still runs out of memory, close background apps and test without optional shaders.

---

## First Launch Checklist

- [ ] Installed through CurseForge.
- [ ] V2.0.2 or the intended release selected.
- [ ] No extra mods.
- [ ] No extra shaders or resource packs.
- [ ] No copied V1.1.2 config folder.
- [ ] Minecraft `1.20.1` confirmed.
- [ ] Forge profile confirmed.
- [ ] Java `17` used if required.
- [ ] RAM allocation checked.
- [ ] New test world created.
- [ ] Overworld generation works.
- [ ] Nether and End portals work in testing.
- [ ] Xaero's Minimap and World Map open correctly.
- [ ] Audio works.
- [ ] FPS is playable.
- [ ] Game exits normally.

If the clean pack works and your modified profile breaks, the modification is the suspect.

---

## Backups

Back up before updates, server moves, config edits, world migrations, mod removals, or major experiments.

| Folder or file | Why it matters |
| --- | --- |
| `saves/` | Singleplayer worlds |
| `config/` | Main mod configuration |
| `defaultconfigs/` | Default templates for new worlds or servers |
| `saves/<world>/serverconfig/` | Per-world server configs, included in a complete world backup |
| `journeymap/` | Legacy V1.1.2 map data, if present |
| Xaero map folders | V2.0.0 minimap and world-map data, if present |
| `screenshots/` | Screenshots you care about |
| Server world folder | Dedicated server world data |
| `ops.json` | Server operator list |
| `whitelist.json` | Server whitelist |
| Ban files | Server ban data |

Example backup name:

```text
Still-Watching-worldname-before-v2.0.0-migration.zip
```

Exit Minecraft or stop the dedicated server before copying world files. Keep a backup outside the live instance and test extraction into a separate folder before relying on it.

---

## Multiplayer and Server Setup

Still Watching multiplayer works only when **every client and the server use matching pack version, Minecraft version, Forge version, required mods, datapacks, and configs**.

Recommended paths:

1. Use a hosting-provider CurseForge installer when available.
2. Use an official CurseForge server pack when the selected file provides one.
3. Use manual Forge server setup only if you can verify sides, dependencies, worldgen files, configs, and logs yourself.

For conservative server-focused rules, read [`docs/server-pack-guide.md`](./docs/server-pack-guide.md).

---

## Troubleshooting

Start with a clean CurseForge profile.

| Symptom | First move |
| --- | --- |
| Crash on launch | Reinstall through CurseForge, remove extras, allocate `5 GB+`, use Java `17` if asked, then inspect logs. |
| Crash while creating a world | Test a new clean profile and inspect the first worldgen-related error in `latest.log`. |
| Broken old-world terrain | Restore the backup or use a new V2.0.0 world; terrain seams are expected after major generator changes. |
| Missing JourneyMap data | Open the old V1.1.2 profile; JourneyMap data does not automatically transfer to Xaero's maps. |
| Low FPS | Lower render distance, reduce shader settings, test without shaders, and include hardware/settings in reports. |
| Server mismatch | Match pack version, Forge version, configs, worldgen files, and required mods on server and clients. |
| Bug after adding mods | Reproduce on a clean CurseForge install before reporting. Extra mods are suspects. |

---

## Bug Reports

Before opening an issue, reproduce the problem on a clean CurseForge install when possible.

Include:

- Pack version, for example `Still Watching V2.0.2`.
- Launcher used.
- Minecraft and Forge versions.
- Java version, if relevant.
- Operating system.
- Singleplayer or multiplayer.
- Whether the world was newly created or migrated from V1.1.2.
- Server host and RAM, if relevant.
- Crash report or `latest.log`.
- Steps to reproduce.
- Any extra mods, shaders, resource packs, or config edits.

Copy the log before launching again, and remove sensitive information before sharing it.
