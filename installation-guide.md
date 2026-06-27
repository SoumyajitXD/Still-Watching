<!-- markdownlint-disable MD013 -->

# Still Watching Installation Guide

This guide covers installing, updating, backing up, troubleshooting, and hosting **Still Watching**, a Minecraft Java Edition horror-survival modpack by **Soumyajit** for **Minecraft `1.20.1`** on **Forge**.

Current documented release: **Still Watching V1.1.2**.

---

## Project Baseline

| Item | Value |
| --- | --- |
| Project | Still Watching |
| Minecraft | `1.20.1` |
| Loader | Forge |
| Java | Java `17` if the launcher or server asks |
| CurseForge Project ID | `1420406` |
| Current documented release | Still Watching V1.1.2 |
| RAM | `5 GB` minimum; `6–8 GB` preferred |
| Repository license | Apache-2.0 for original repository files only |

> [!IMPORTANT]
> CurseForge is the supported playable source. The GitHub ZIP is **not** a playable modpack installer and is **not** a server pack.

---

## Official Links

| Resource | Link |
| --- | --- |
| CurseForge project | [Still Watching on CurseForge](https://www.curseforge.com/minecraft/modpacks/still-watching) |
| CurseForge files | [Still Watching Files](https://www.curseforge.com/minecraft/modpacks/still-watching/files) |
| GitHub issues | [Report an issue](https://github.com/SoumyajitXD/Still-Watching/issues) |
| README | [README.md](./README.md) |
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

## Quick Install

1. Install the [CurseForge App](https://www.curseforge.com/download/app).
2. Open **Minecraft** in CurseForge.
3. Search for **Still Watching**.
4. Verify the project details:
   - Name: **Still Watching**.
   - Creator: **Soumyajit**.
   - Minecraft: **`1.20.1`**.
   - Loader: **Forge**.
5. Click **Install**.
6. Allocate RAM if needed.
7. Launch once with **no extra mods, shaders, resource packs, or config edits**.
8. Create a new test world.
9. Confirm loading, audio, controls, and FPS are playable.

That is the clean path. Save experiments for after the pack actually launches.

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
- [ ] No extra mods.
- [ ] No extra shaders.
- [ ] No extra resource packs.
- [ ] No config edits.
- [ ] Minecraft `1.20.1` confirmed.
- [ ] Forge profile confirmed.
- [ ] Java `17` used if required.
- [ ] RAM allocation checked.
- [ ] New test world created.
- [ ] Audio works.
- [ ] FPS is playable.
- [ ] Game exits normally.

If the clean pack works and your modified profile breaks, the modification is the suspect.

---

## Updating Safely

1. Back up your worlds.
2. Check the [CurseForge Files page](https://www.curseforge.com/minecraft/modpacks/still-watching/files).
3. Update through the launcher.
4. Launch clean.
5. Test a disposable or new world.
6. Open your main world only after the update passes basic testing.

Multiplayer requires all clients and the server to match the pack version, Minecraft version, Forge version, required files, and required configs.

---

## Backups

Back up before updates, server moves, config edits, world migrations, mod removals, or major experiments.

| Folder or file | Why it matters |
| --- | --- |
| `saves/` | Singleplayer worlds |
| `config/` | Main mod configuration |
| `defaultconfigs/` | Default config templates for new worlds or servers |
| `serverconfig/` | Per-world server configs |
| `journeymap/` | Map data, if present |
| `screenshots/` | Screenshots you care about |
| Server world folder | Dedicated server world data |
| `ops.json` | Server operator list |
| `whitelist.json` | Server whitelist |
| Ban files | Server ban data |

Example backup name:

```text
Still-Watching-worldname-before-v1.1.2-update.zip
```

Check that the archive actually contains files. An empty backup is just a lie with a `.zip` extension.

---

## Multiplayer and Server Setup

Still Watching multiplayer works only when **every client and the server use matching pack version, Minecraft version, Forge version, required mods, and configs**.

Recommended paths:

1. Use a hosting provider CurseForge installer when available.
2. Use an official CurseForge server pack when the selected file provides one.
3. Use manual Forge server setup only if you can verify sides, dependencies, configs, and logs yourself.

For conservative server-focused rules, read [`docs/server-pack-guide.md`](./docs/server-pack-guide.md).

---

## Troubleshooting

Start with a clean baseline before chasing demons.

| Symptom | First move |
| --- | --- |
| Crash on launch | Reinstall through CurseForge, remove extras, allocate `5 GB+`, use Java `17` if asked, then check logs. |
| Missing mods | Reinstall from CurseForge. The GitHub ZIP is not an installer. |
| Low FPS | Lower render distance, reduce shader or visual settings, and check RAM allocation. |
| Server mismatch | Match pack version, Forge version, configs, and files on server and clients. |
| Bug after adding mods | Reproduce on a clean CurseForge install before reporting. Extra mods are suspects. |

---

## Bug Reports

Before opening an issue, reproduce the problem on a clean CurseForge install when possible.

Include:

- Pack version, for example `Still Watching V1.1.2`.
- Launcher used.
- Minecraft version.
- Forge version, if visible.
- Java version, if relevant.
- Operating system.
- Singleplayer or multiplayer.
- Server host and RAM, if relevant.
- Crash report or `latest.log`.
- Steps to reproduce.
- Any extra mods, shaders, resource packs, or config edits.

Logs beat vibes. Always.