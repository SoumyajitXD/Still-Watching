# Still Watching Installation Guide

This guide covers installing, updating, backing up, troubleshooting, reporting bugs, and setting up multiplayer for **Still Watching**, a Minecraft Java Edition horror-survival modpack by **Soumyajit** for **Minecraft 1.20.1** on **Forge**.

> [!IMPORTANT]
> **CurseForge is the supported install source.** The playable release is distributed through CurseForge.
>
> The GitHub ZIP is **not** a playable modpack installer. It is repository source content for documentation, issue tracking, maintenance, screenshots, release-side files, and licensing clarity.

## Start Here

| Goal | Use this section |
| --- | --- |
| Install and play | [Quick Install](#quick-install) |
| Need a specific version | [Installing a Specific Version](#installing-a-specific-version) |
| Updating safely | [Updating Safely](#updating-safely) |
| Make backups | [Backups](#backups) |
| Fix a crash or broken install | [Troubleshooting](#troubleshooting) |
| Host a server | [Multiplayer & Server Setup](#multiplayer--server-setup) |
| Report a bug | [Bug Reports](#bug-reports) |

## Official Links

| Resource | Link |
| --- | --- |
| CurseForge project page | [Still Watching on CurseForge](https://www.curseforge.com/minecraft/modpacks/still-watching) |
| CurseForge files page | [Still Watching Files](https://www.curseforge.com/minecraft/modpacks/still-watching/files) |
| GitHub issues | [Report an issue](../../issues) |
| README | [README.md](./README.md) |
| Latest mod list | [latest-modlist.md](./latest-modlist.md) |

If GitHub and CurseForge disagree about a released file, trust CurseForge and report the mismatch. Do not turn a source ZIP into a fake installer and then blame the fog.

---

## Requirements

| Requirement | Details |
| --- | --- |
| Minecraft edition | Minecraft: Java Edition |
| Minecraft version | `1.20.1` |
| Loader | Forge |
| Recommended installer | CurseForge App |
| Java | Java 17 if the launcher asks |
| RAM | `5 GB` minimum; `6–8 GB` recommended |
| Disk space | `5–10 GB` recommended |
| Internet | Required for download and dependency installation |
| Headphones | Recommended for audio cues and atmosphere |
| CurseForge Project ID | `1420406` |

---

## Quick Install

Use this path if you just want to play.

1. Install the [CurseForge App](https://www.curseforge.com/download/app).
2. Open **Minecraft** in CurseForge.
3. Search for **Still Watching**.
4. Verify the project details:
   - Name: **Still Watching**
   - Creator: **Soumyajit**
   - Minecraft: **1.20.1**
   - Loader: **Forge**
5. Click **Install**.
6. Allocate RAM if needed.
7. Launch once with **no extra mods, shaders, or resource packs**.
8. Create a new test world.
9. Confirm loading, audio, and FPS are playable.

That is the clean route. Save the experiments for after the pack actually launches.

---

## Installing from CurseForge

CurseForge is the normal install path and the source of truth for released files.

### CurseForge App

1. Download and install the [CurseForge App](https://www.curseforge.com/download/app).
2. Open **Minecraft**.
3. Search for **Still Watching**.
4. Verify the name, creator, Minecraft version, and Forge loader.
5. Click **Install**.
6. Open the profile from **My Modpacks**.
7. Adjust RAM if needed.
8. Launch clean once before changing anything.

### CurseForge Website

1. Open [Still Watching on CurseForge](https://www.curseforge.com/minecraft/modpacks/still-watching).
2. Click **Install**, **Install via App**, or CurseForge’s current equivalent.
3. Allow the browser to open CurseForge.
4. Let CurseForge create the profile and download dependencies.
5. Launch clean once before adding extras.

### Installing a Specific Version

Use the [CurseForge Files page](https://www.curseforge.com/minecraft/modpacks/still-watching/files) when a server, world, or testing case requires a specific version.

For normal play, use the latest available CurseForge release. For multiplayer, install the exact version used by the server.

---

## Other Launchers

Other launchers are only reasonable if they properly handle CurseForge manifests and dependencies.

General rule:

- Import from CurseForge or a proper CurseForge export when supported.
- Confirm Minecraft **1.20.1** and Forge.
- Launch clean before adding extras.
- Reproduce issues on the CurseForge App before reporting them.

Manual assembly is unsupported unless you already know how Forge mod sides, dependencies, configs, and logs work. Random file-dragging is not installation. It is ritual sacrifice with worse documentation.

---

## RAM Allocation

| System RAM | Suggested Minecraft RAM |
| --- | --- |
| 8 GB | 5 GB; close background apps |
| 12 GB | 5–6 GB |
| 16 GB | 6–8 GB |
| 32 GB+ | 8 GB |

| RAM | MB value |
| --- | ---: |
| 5 GB | `5120 MB` |
| 6 GB | `6144 MB` |
| 8 GB | `8192 MB` |

> [!WARNING]
> Do not allocate all system RAM. Minecraft needs memory, but Windows/macOS/Linux and background apps still need to breathe. Starving the OS is not optimization; it is self-sabotage with a slider.

### CurseForge RAM Steps

1. Open **CurseForge**.
2. Go to **My Modpacks**.
3. Select **Still Watching**.
4. Open **Profile Options**.
5. Disable **Use System Memory Settings** if needed.
6. Set the memory value:
   - `5120 MB` = 5 GB
   - `6144 MB` = 6 GB
   - `8192 MB` = 8 GB
7. Save.
8. Relaunch the pack.

---

## First Launch Checklist

- [ ] No extra mods.
- [ ] No shaders.
- [ ] No extra resource packs.
- [ ] New test world created.
- [ ] Game loads successfully.
- [ ] Audio works.
- [ ] FPS is playable.
- [ ] Game exits normally.
- [ ] Optional changes are added one at a time afterward.

If the clean pack works and your modified profile breaks, the modification is the suspect. Drag it into the light and test it properly.

---

## Recommended Game Settings

| Setting | Starting point | Notes |
| --- | --- | --- |
| Render distance | 8–10 chunks | Lower first if FPS drops. |
| Simulation distance | 5–6 chunks | Helps reduce CPU load. |
| Brightness | Adjust for comfort/accessibility | Darkness is part of the mood, but eye strain is useless. |
| Shaders | Off for first launch | Add later only after the base pack works. |
| Extra resource packs | Off for first launch | Prevents first-run conflict noise. |
| Subtitles | Optional | Useful for accessibility and tracking audio cues. |
| Headphones | Recommended | Directional sound matters in a horror pack. |

Accessibility is not “playing wrong.” Use subtitles, brightness, and breaks as needed. The goal is fear, not a migraine.

---

## Updating Safely

1. Back up your worlds.
2. Check the [CurseForge Files page](https://www.curseforge.com/minecraft/modpacks/still-watching/files).
3. Update through the launcher.
4. Launch clean.
5. Test a disposable or new world.
6. Open your main world only after the update passes basic testing.

> [!IMPORTANT]
> Multiplayer requires all clients and the server to match the pack version, Minecraft version, Forge version, and required configs.

Do not test an update for the first time on your only serious world. That is not bravery. That is how save files become ghost stories.

---

## Backups

Back up before updates, server moves, config edits, world migrations, or major experiments.

| Folder/File | Why it matters |
| --- | --- |
| `saves/` | Singleplayer worlds |
| `config/` | Main mod configuration |
| `defaultconfigs/` | Default config templates for new worlds/servers |
| `serverconfig/` | Per-world server configs |
| `journeymap/` | Map data, if present |
| `screenshots/` | Screenshots you care about |
| Server world folder | Dedicated server world data |
| `ops.json` | Server operator list |
| `whitelist.json` | Server whitelist |
| Ban files | Server ban data |

Example backup name:

```text
Still-Watching-worldname-before-vX.X.X-update.zip
```

Check that the archive actually contains files. An empty backup is just a lie with a `.zip` extension.

---

<a id="multiplayer--server-notes"></a>
## Multiplayer & Server Setup

Still Watching multiplayer works only when **every client and the server use matching pack version, Minecraft version, Forge version, required mods, and configs**.

If those do not match, stop. Fix that first. The server is not haunted; your versions are fighting in a trench coat.

### Path A: Hosting Provider CurseForge Installer

Best for most users.

1. Open your hosting panel.
2. Find the **CurseForge**, **Modpacks**, or **Modpack Installer** section.
3. Search for **Still Watching**.
4. Choose the exact same pack version as all clients.
5. Install it.
6. Start the server.
7. Check the console for errors.
8. Join with a clean matching client.

Use this path when your host supports it. Let the installer handle dependencies instead of hand-crafting a crash log.

### Path B: Official Server Pack from CurseForge

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

### Path C: Manual Forge Server

Manual setup is advanced and unsupported unless verified for the exact release.

1. Install a clean Forge **1.20.1** server.
2. Use the Forge build required by the selected CurseForge release.
3. Copy only server-compatible mods.
4. Copy required configs.
5. Remove client-only mods.
6. Allocate server RAM.
7. Start the server.
8. Read the logs.
9. Fix errors before inviting players.
10. Test with one clean matching client.

Do **not** provide, trust, or paste an exact server mod list unless it was verified from the actual release files. Client-only categories commonly include shader loaders, minimap/map renderers, HUD-only mods, visual-only mods, audio-only mods, and client rendering/performance mods.

### Common Server Failure Causes

| Problem | What it usually means | First fix |
| --- | --- | --- |
| Client/server version mismatch | Pack versions differ | Install the same CurseForge file on server and clients. |
| Wrong Forge build | Server and client are not using the release’s required Forge build | Check the selected file/profile and match it. |
| Missing dependencies | A required library or mod is absent | Reinstall through the host installer or official server pack. |
| Client-only mods on server | Dedicated server is loading client-side code | Remove wrong-side mods and read the server log. |
| Config mismatch | Server and client configs differ where they must match | Recopy required configs from the selected release. |
| Too little RAM | Server cannot load or TPS collapses | Increase server memory and reduce load. |
| Wrong Java/runtime | Server starts with an incompatible Java | Use Java 17 when required. |
| Bad manual assembly | Files were copied by guesswork | Rebuild using Path A or Path B. |

---

## Troubleshooting

Start with a clean baseline before chasing demons.

### Clean Baseline Test

1. Restart the launcher.
2. Confirm Minecraft **1.20.1**.
3. Confirm the loader is **Forge**.
4. Allocate **5–8 GB** RAM.
5. Remove extra mods.
6. Disable shaders and extra resource packs.
7. Repair or reinstall the profile.
8. Test a new world.
9. Check `logs/latest.log` or the crash report.

### Symptom Table

| Problem | First check | Next action |
| --- | --- | --- |
| Won’t launch | Profile, Minecraft version, loader, RAM | Repair/reinstall the CurseForge profile. |
| Crash during loading | Extras, shaders, memory, corrupted profile | Remove extras, use 5–8 GB RAM, check crash report. |
| Crash after joining world | New world vs old world | Restore backup if the crash is world-specific. |
| Server crashes on boot | Client-only mods, missing mods, Forge mismatch | Read server log and remove wrong-side mods. |
| Server rejects client | Version/config mismatch | Make server and client match exactly. |
| Bad FPS | Render distance, shaders, background apps | Lower settings and launch without extras. |
| Missing mods/config mismatch | Install source and version | Reinstall matching CurseForge version. |
| Audio feels wrong | Output device, sliders, headphones | Check Minecraft and system audio settings. |
| Weird behavior after update | Old configs/world data | Test a clean profile and disposable world. |
| Only breaks with extra mods | Added mods/config edits | Reproduce clean before reporting. |

### Clean Reinstall

1. Back up worlds first.
2. Open CurseForge.
3. Delete the broken **Still Watching** profile.
4. Reinstall from the official CurseForge page.
5. Allocate RAM again.
6. Launch clean before restoring worlds or adding extras.
7. Restore backed-up worlds only after the clean install works.

### Crash During Loading

Common causes:

- Wrong Minecraft version.
- Wrong loader.
- Wrong Java version.
- Too little RAM.
- Corrupted profile.
- Broken extra mods.
- Shader or resource pack conflicts.
- Client/server-side mod mismatch.
- Outdated graphics drivers.

Attach the crash report and `latest.log` if you report it. A screenshot of the launcher saying “Exit Code 1” is basically a ransom note with no address.

### Crash After Joining a World

Check this order:

1. Does a new world work?
2. Did you update recently?
3. Did you add or remove mods after creating the world?
4. Does the crash happen at the same place or after the same action?
5. Does the crash report name a mod, entity, structure, biome, or dimension?

If only one world crashes, treat it as world-specific and restore a backup. If every world crashes, treat the install/profile/config as broken.

### Lag or Bad FPS

Try:

1. Lower render distance.
2. Lower simulation distance.
3. Disable shaders.
4. Remove extra resource packs.
5. Close background apps.
6. Keep included performance mods and configs intact.
7. Restart after major video setting changes.

Do not max graphics, stack shaders, and then act shocked when the frames get buried.

### Server/Client Mismatch

Check:

- Same Still Watching pack version.
- Same Minecraft version: **1.20.1**.
- Same required Forge version for the selected release.
- Required server mods are present.
- Client-only mods are not on the dedicated server.
- Required configs match.
- Both sides were installed from the same CurseForge release or official server pack.

---

## Logs and Crash Reports

Useful files live inside the modpack profile or server folder.

Client:

```text
logs/latest.log
crash-reports/crash-YYYY-MM-DD_HH.mm.ss-client.txt
```

Server:

```text
logs/latest.log
logs/debug.log
crash-reports/
```

### Open the CurseForge Profile Folder

1. Open **CurseForge**.
2. Go to **My Modpacks**.
3. Right-click **Still Watching** or click the three dots.
4. Choose **Open Folder**.
5. Check `logs/`, `crash-reports/`, `saves/`, and `config/`.

> [!CAUTION]
> Logs may contain usernames, local file paths, server IPs, tokens, or system details. Review files before posting them publicly.

Useful search terms:

```text
Caused by
Exception
OutOfMemoryError
Mod File
Missing
Failed
mismatch
requires
```

Read the first meaningful error, not just the final line. The last line often only describes the wreckage.

---

## Bug Reports

Open reports here: [GitHub Issues](../../issues)

Before reporting, reproduce on a clean CurseForge install when possible. Use the matching issue template: bug, crash, server, performance, installation/update, or another template if present.

### Required Info Checklist

- [ ] Still Watching pack version.
- [ ] Launcher.
- [ ] Minecraft version.
- [ ] Forge version, if visible.
- [ ] Java version, if relevant.
- [ ] Operating system.
- [ ] Singleplayer or multiplayer.
- [ ] Server type, host/provider, and server RAM if relevant.
- [ ] `latest.log` and crash report when relevant.
- [ ] Steps to reproduce.
- [ ] Expected result and actual result.
- [ ] Extra mods, shaders, resource packs, datapacks, plugins, config edits, or launcher changes.

### Good Report Example

```text
Pack version: Still Watching vX.X.X
Launcher: CurseForge App
Minecraft: 1.20.1
Loader: Forge
Java: Java 17
OS: Windows 11
Mode: Singleplayer

Issue:
Game crashes when entering a cave structure in a new world.

Steps to reproduce:
1. Install Still Watching from CurseForge.
2. Launch with no extra mods, shaders, or resource packs.
3. Create a new world.
4. Enter the cave structure.
5. Game crashes.

Attached:
- logs/latest.log
- crash report

Modifications:
None
```

### Bad Report Example

```text
it broke fix pls
```

That report contains nothing to debug. Logs and steps, or everyone is just throwing bones at the wall.

---

## FAQ

### Can I install from GitHub?

No. Install from CurseForge.

The GitHub ZIP is not a playable modpack installer. It is repository source content, not the distributed pack profile.

### Can I add extra mods?

Yes, but added mods are your responsibility. Reproduce issues on a clean CurseForge install before reporting them.

### Can I use shaders?

Yes, if your system can handle them. Launch clean first, then add shaders one at a time.

### Can I play without headphones?

Yes. Headphones are recommended because sound is part of the pack’s horror design, but they are not required.

### Which version should I install?

Use the latest version on the [CurseForge Files page](https://www.curseforge.com/minecraft/modpacks/still-watching/files), unless your server or world requires a specific older version.

### Where do I find the Forge version?

Check the selected CurseForge file, the launcher profile details, or the top section of `logs/latest.log`.

### Should I report bugs after modifying the pack?

Only after testing the same issue on a clean profile. If it only breaks with extra mods, shaders, edited configs, or third-party launcher changes, the modification is probably the culprit.

### Can I use another launcher?

Maybe. It must properly support CurseForge manifests and dependency downloads. If it fails, reproduce the issue in CurseForge before reporting.

### Why does server setup fail?

Usually because the server and clients do not match, the wrong Forge build is used, dependencies are missing, client-only mods are on the server, configs differ, RAM is too low, Java is wrong, or the server pack was manually assembled badly.

Read the server log. Minecraft is noisy, but it usually tells on itself.

---

## Final Checklist

Before serious play:

- [ ] Installed from CurseForge.
- [ ] Minecraft **1.20.1** confirmed.
- [ ] Forge confirmed.
- [ ] `5–8 GB` RAM allocated.
- [ ] Launched clean.
- [ ] New test world works.
- [ ] Audio works.
- [ ] Backups made.
- [ ] Client/server versions match for multiplayer.
- [ ] Logs/crash reports are ready for useful bug reports.

Then step into the fog. Do not trust the quiet.
