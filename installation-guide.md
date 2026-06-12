<!-- markdownlint-disable MD013 -->

# Still Watching Installation Guide

This guide covers installing, updating, backing up, troubleshooting, and hosting **Still Watching**, a Minecraft Java Edition horror-survival modpack by **Soumyajit** for **Minecraft `1.20.1`** on **Forge**.

Current documented release: **Still Watching V1.1.1**.

> [!IMPORTANT]
> **CurseForge is the supported playable source.**
>
> This GitHub repository is for documentation, release-facing source files, validation, issue tracking, screenshots, and licensing clarity. The GitHub ZIP is **not** a playable modpack installer and is **not** a server pack.

---

## Start Here

| Goal | Go here | First rule |
| --- | --- | --- |
| Install and play | [Quick Install](#quick-install) | Use CurseForge, not the GitHub ZIP. |
| Allocate memory | [RAM Allocation](#ram-allocation) | `5 GB` minimum; `6–8 GB` preferred. |
| Update safely | [Updating Safely](#updating-safely) | Back up before updating. |
| Host multiplayer | [Multiplayer and Server Setup](#multiplayer-and-server-setup) | Match pack, Forge, configs, and files. |
| Fix a crash | [Troubleshooting](#troubleshooting) | Test clean before adding extras. |
| Report a bug | [Bug Reports](#bug-reports) | Logs beat vibes. |

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

Use this route if you just want to play.

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

## Installing from CurseForge

CurseForge is the source of truth for playable files.

### CurseForge App

1. Download and install the [CurseForge App](https://www.curseforge.com/download/app).
2. Open **Minecraft**.
3. Search for **Still Watching**.
4. Verify the name, creator, Minecraft version, and Forge loader.
5. Install the latest release.
6. Open the profile from **My Modpacks**.
7. Adjust RAM if needed.
8. Launch clean once before changing anything.

### CurseForge Website

1. Open [Still Watching on CurseForge](https://www.curseforge.com/minecraft/modpacks/still-watching).
2. Click **Install**, **Install via App**, or CurseForge's current equivalent.
3. Allow the browser to open CurseForge.
4. Let CurseForge create the profile and download dependencies.
5. Launch clean once before adding extras.

### Installing a Specific Version

Use the [CurseForge Files page](https://www.curseforge.com/minecraft/modpacks/still-watching/files) when a server, world, or test case requires a specific pack version.

For normal play, use the latest available CurseForge release. For multiplayer, install the exact version used by the server.

---

## Other Launchers

Other launchers are reasonable only when they properly support CurseForge manifests and dependency resolution.

Baseline rules:

- Import from CurseForge or from a proper CurseForge export when supported.
- Confirm Minecraft `1.20.1` and Forge.
- Use Java `17` if the launcher asks.
- Launch clean before adding extras.
- Reproduce issues in the CurseForge App before reporting them.

Manual assembly is unsupported unless you already know Forge mod sides, dependencies, configs, and logs. Random file dragging is not installation. It is ritual sacrifice with worse documentation.

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

> [!WARNING]
> More RAM is not always better. Too little causes crashes and stutter; too much can make garbage collection uglier. Start with the table, then adjust based on logs and performance.

### CurseForge RAM Steps

1. Open **CurseForge**.
2. Go to **My Modpacks**.
3. Select **Still Watching**.
4. Open **Profile Options**.
5. Disable **Use System Memory Settings** if needed.
6. Set memory to `5120 MB`, `6144 MB`, or `8192 MB`.
7. Save.
8. Relaunch the pack.

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

If the clean pack works and your modified profile breaks, the modification is the suspect. Test it like evidence.

---

## Recommended Game Settings

| Setting | Starting point | Notes |
| --- | --- | --- |
| Render distance | `8–10` chunks | Lower first if FPS drops. |
| Simulation distance | `5–6` chunks | Helps reduce CPU load. |
| Brightness | Comfort first | Darkness helps the mood; eye strain helps nothing. |
| Shaders | Off for first launch | Add later only after the base pack works. |
| Extra resource packs | Off for first launch | Prevents noisy first-run conflicts. |
| Subtitles | Optional | Useful for accessibility and audio tracking. |
| Headphones | Recommended | Directional sound matters in this pack. |

Accessibility is not playing wrong. Use subtitles, brightness, volume controls, and breaks as needed.

---

## Updating Safely

1. Back up your worlds.
2. Check the [CurseForge Files page](https://www.curseforge.com/minecraft/modpacks/still-watching/files).
3. Update through the launcher.
4. Launch clean.
5. Test a disposable or new world.
6. Open your main world only after the update passes basic testing.

> [!IMPORTANT]
> Multiplayer requires all clients and the server to match the pack version, Minecraft version, Forge version, required files, and required configs.

Do not test an update for the first time on your only serious world. That is how save files become ghost stories.

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
Still-Watching-worldname-before-v1.1.1-update.zip
```

Check that the archive actually contains files. An empty backup is just a lie with a `.zip` extension.

---

## Multiplayer and Server Setup

Still Watching multiplayer works only when **every client and the server use matching pack version, Minecraft version, Forge version, required mods, and configs**.

If those do not match, stop and fix that first. The server is not haunted; your versions are fighting in a trench coat.

### Path A Hosting Provider Installer

Best for most users when a host supports CurseForge modpacks.

1. Open your hosting panel.
2. Find the **CurseForge**, **Modpacks**, or **Modpack Installer** section.
3. Search for **Still Watching**.
4. Choose the exact pack version used by all clients.
5. Install it.
6. Start the server.
7. Check the console for errors.
8. Join with a clean matching client.

Use this path when possible. Let the installer handle dependencies instead of hand-crafting a crash log.

### Path B Official Server Pack

Use this only if the selected CurseForge release provides a server pack.

1. Open the [CurseForge Files page](https://www.curseforge.com/minecraft/modpacks/still-watching/files).
2. Pick the exact client version.
3. Download the server pack if one is available for that file.
4. Extract it to a clean folder.
5. Run the included start script or Forge server jar.
6. Accept the Minecraft EULA when prompted.
7. Restart the server.
8. Check logs and console output.
9. Join with a matching client.

Do not use a server pack from one version with clients from another. That is dependency roulette.

### Path C Manual Forge Server

Manual setup is advanced and unsupported unless verified for the exact release.

1. Install a clean Forge `1.20.1` server.
2. Use the Forge build required by the selected CurseForge release.
3. Copy only server-compatible mods.
4. Copy required configs.
5. Remove client-only files.
6. Allocate server RAM.
7. Start the server.
8. Read the logs.
9. Fix errors before inviting players.
10. Test with one clean matching client.

Do **not** provide, trust, or paste an exact server mod list unless it was verified from the actual release files. Client-only categories commonly include shader loaders, minimap or map renderers, HUD-only mods, visual-only mods, menu mods, audio-only mods, and client rendering or performance mods.

For the conservative server-focused version of these rules, read [`docs/server-pack-guide.md`](./docs/server-pack-guide.md).

### Common Server Failure Causes

| Problem | What it usually means | First fix |
| --- | --- | --- |
| Client and server versions differ | Pack versions differ | Install the same CurseForge file on server and clients. |
| Wrong Forge build | Server and client are not using the release's required Forge build | Check the selected profile and match it. |
| Missing dependency | A required library or mod is absent | Reinstall through the host installer or official server pack. |
| Client-only file on server | Dedicated server is loading client-side code | Remove wrong-side files and read the server log. |
| Config mismatch | Server and client configs differ where they must match | Recopy required configs from the selected release. |
| Too little RAM | Server cannot load or TPS collapses | Increase server memory and reduce load. |
| Wrong Java runtime | Server starts with an incompatible Java | Use Java `17` when required. |
| Bad manual assembly | Files were copied by guesswork | Rebuild using Path A or Path B. |

---

## Troubleshooting

Start with a clean baseline before chasing demons.

### Clean Baseline Test

1. Restart the launcher.
2. Confirm Minecraft `1.20.1`.
3. Confirm the loader is Forge.
4. Use Java `17` if required.
5. Allocate `5–8 GB` RAM.
6. Remove extra mods.
7. Disable shaders and extra resource packs.
8. Repair or reinstall the profile.
9. Test a new world.
10. Check `logs/latest.log` or the crash report.

### Symptom Table

| Problem | First check | Next action |
| --- | --- | --- |
| Won't launch | Profile, Minecraft version, loader, RAM | Repair or reinstall the CurseForge profile. |
| Crash during loading | Extras, shaders, memory, corrupted profile | Remove extras, use `5–8 GB` RAM, check crash report. |
| Crash after joining world | New world vs old world | Restore backup if the crash is world-specific. |
| Server crashes on boot | Pack version, Forge, Java, server-only file set | Rebuild from official server path and read logs. |
| Missing dependencies | CurseForge install or manual assembly | Reinstall through CurseForge. |
| Low FPS | Render distance, shaders, RAM, hardware | Lower render distance and disable shaders first. |
| Broken audio | Device, volume, mod audio settings | Test vanilla audio and OS output device. |
| Multiplayer join failure | Client/server version mismatch | Match exact pack version and configs. |

### Logs to Check

| File | Use |
| --- | --- |
| `logs/latest.log` | Main client or server log |
| `crash-reports/` | Crash report folder |
| Server console log | Dedicated server startup and runtime errors |
| Launcher log | Launcher-side download, Java, or profile issues |

Logs are evidence. Screenshots of generic launcher errors are usually not enough.

---

## Bug Reports

Before opening an issue, test on a clean CurseForge install when possible.

Include:

- Still Watching version, for example **Still Watching V1.1.1**.
- Install source.
- Launcher used.
- Minecraft version.
- Forge version, if visible.
- Java version, if relevant.
- Operating system.
- Singleplayer or multiplayer.
- Client or dedicated server.
- Server host and RAM, if relevant.
- Crash report or `latest.log`.
- Steps to reproduce.
- Any extra mods, shaders, resource packs, or config edits.
- Whether the issue happens on a clean CurseForge install.

Bad report:

```text
it broke fix pls
```

Good report:

```text
Pack version: Still Watching V1.1.1
Install source: CurseForge App
Minecraft: 1.20.1
Loader: Forge
Mode: Singleplayer
Issue: Crash when entering a cave structure in a new world
Steps:
1. Install from CurseForge
2. Launch with no extra mods, shaders, resource packs, or config edits
3. Create a new world
4. Enter the structure
5. Game crashes
Attached: latest.log and crash report
```

A good report gives maintainers something to reproduce. A bad report just throws a noise into the woods and expects Java to confess.

---

## License Notes

This repository's original project files are licensed under the [Apache License 2.0](./LICENSE), commonly identified as **Apache-2.0**.

That license covers original repository files maintained for Still Watching. It does **not** relicense Minecraft, Forge, CurseForge, third-party mods, third-party assets, mod names, logos, screenshots containing third-party content, shaders, resource packs, sounds, textures, or external project content. Those remain under their own licenses, permissions, and terms.

Do not redistribute third-party mod files outside their allowed channels. The safe install path is CurseForge.

---

## Security and Suspicious Downloads

For fake downloads, suspicious links, unsafe public references, exposed secrets, or possible private-data leaks, read [`SECURITY.md`](./SECURITY.md).

Do not post secrets, tokens, passwords, private server IPs, or sensitive logs in public issues.
