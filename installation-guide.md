<!-- markdownlint-disable MD013 -->

# Still Watching Installation Guide

This guide covers installing, updating, migrating, backing up, troubleshooting, and hosting **Still Watching**, a Minecraft Java Edition horror-survival modpack by **Soumyajit** for **Minecraft `1.20.1`** on **Forge**.

Current documented release: **Still Watching V2.0.0**.

---

## Project Baseline

| Item | Value |
| --- | --- |
| Project | Still Watching |
| Minecraft | `1.20.1` |
| Loader | Forge |
| Java | Java `17` if the launcher or server asks |
| CurseForge Project ID | `1420406` |
| Current documented release | Still Watching V2.0.0 |
| RAM | `5 GB` minimum; `6–8 GB` preferred |
| Repository license | Apache-2.0 for original repository files only |

> [!IMPORTANT]
> CurseForge is the supported playable source. The GitHub ZIP is **not** the recommended playable modpack installer and is **not** a server pack.

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

Do not allocate every megabyte of system memory to Minecraft. The operating system still needs room to breathe.

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
5. Install **Still Watching V2.0.0** or the newest compatible release.
6. Allocate RAM if needed.
7. Launch once with **no extra mods, shaders, resource packs, or config edits**.
8. Create a new test world.
9. Confirm world generation, dimensions, audio, controls, menus, maps, and FPS are playable.

That is the clean path. Save experiments for after the pack actually launches.

---

## Updating from V1.1.2

The safest migration is a fresh profile, not an overwrite.

1. Back up the complete V1.1.2 instance.
2. Back up every important world separately.
3. Preserve the old `journeymap/` folder if its waypoints or map tiles matter.
4. Install V2.0.0 as a fresh CurseForge profile.
5. Do **not** copy the entire old `config/` folder into V2.0.0.
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

More RAM is not always better. Too little causes crashes and stutter; too much can make garbage collection uglier.

---

## First Launch Checklist

- [ ] Installed through CurseForge.
- [ ] V2.0.0 or the intended release selected.
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
| `serverconfig/` | Per-world server configs |
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

Check that the archive actually contains files. An empty backup is just a lie with a `.zip` extension.

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

Start with a clean baseline before chasing demons.

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

- Pack version, for example `Still Watching V2.0.0`.
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

Logs beat vibes. Always.
