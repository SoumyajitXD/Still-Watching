# Still Watching Installation Guide

This guide explains how to install, launch, update, troubleshoot, and report issues for **Still Watching**, a Minecraft Java Edition horror-survival modpack for **Minecraft 1.20.1** on **Forge**.

> [!IMPORTANT]
> **Install from CurseForge. Do not use the GitHub ZIP as a modpack installer.**
>
> The GitHub repository is for documentation, issue tracking, source-side files, project maintenance, and licensing clarity. The playable modpack release lives on CurseForge.

## Official Links

| Resource | Link |
| --- | --- |
| CurseForge project page | [Still Watching on CurseForge](https://www.curseforge.com/minecraft/modpacks/still-watching) |
| CurseForge files page | [Still Watching Files](https://www.curseforge.com/minecraft/modpacks/still-watching/files) |
| GitHub issues | [Report an issue](../../issues) |
| README | [README.md](./README.md) |

CurseForge is the source of truth for released files. If GitHub and CurseForge disagree, trust CurseForge and report the mismatch.

---

## Quick Install

Use this path if you just want to play.

1. Install the [CurseForge App](https://www.curseforge.com/download/app).
2. Open the **Minecraft** section.
3. Search for **Still Watching**.
4. Confirm:
   - Project name: **Still Watching**
   - Creator: **Soumyajit**
   - Minecraft: **1.20.1**
   - Loader: **Forge**
5. Click **Install**.
6. Allocate RAM if needed.
7. Launch once with **no extra mods, shaders, or resource packs**.
8. Create a new test world.
9. Confirm the game loads, audio works, and FPS is playable.

That is the clean path. Do not turn the first launch into a science experiment.

---

## Requirements

| Requirement | Details |
| --- | --- |
| Minecraft edition | Minecraft: Java Edition |
| Minecraft version | 1.20.1 |
| Loader | Forge |
| Java | Java 17 if required by the launcher |
| RAM | 5 GB minimum, 6–8 GB recommended |
| Disk space | 5–10 GB recommended |
| Internet connection | Required for download |
| Headphones | Recommended, not required |
| Official source | CurseForge |
| CurseForge Project ID | `1420406` |

> [!TIP]
> CurseForge is the source of truth for released files. If GitHub and CurseForge disagree, trust CurseForge and report the mismatch.

---

## What Not To Do

> [!WARNING]
> These are the classic ways to break the pack before it even gets to scare you.

- Do **not** install from the GitHub source ZIP.
- Do **not** use random mirrors.
- Do **not** add extra mods before first launch.
- Do **not** allocate all system RAM.
- Do **not** report modified-profile bugs until tested on a clean profile.

---

## CurseForge App Install

This is the recommended install method.

1. Download and install the [CurseForge App](https://www.curseforge.com/download/app).
2. Open CurseForge.
3. Select **Minecraft**.
4. Open **Browse** or **Discover**.
5. Search for **Still Watching**.
6. Verify the project details:
   - Name: **Still Watching**
   - Creator: **Soumyajit**
   - Minecraft: **1.20.1**
   - Loader: **Forge**
7. Click **Install**.
8. Wait for CurseForge to create the profile and download dependencies.
9. Open **My Modpacks**.
10. Select **Still Watching**.
11. Open **Profile Options**.
12. Configure RAM if needed.
13. Launch the pack.

### Verification Checklist

Before you start serious play, confirm:

- The profile is installed from CurseForge.
- The Minecraft version is **1.20.1**.
- The loader is **Forge**.
- RAM is set between **5 GB and 8 GB**.
- No extra mods, shaders, or resource packs were added before the first launch.
- A new test world loads successfully.

---

## CurseForge Website Install

Use this if you found the pack through your browser.

1. Open the official page: [Still Watching on CurseForge](https://www.curseforge.com/minecraft/modpacks/still-watching).
2. Click **Install**, **Install via App**, or the current CurseForge equivalent.
3. Allow your browser to open the CurseForge App.
4. Let CurseForge create the profile.
5. Open the profile from **My Modpacks**.
6. Configure RAM if needed.
7. Launch clean once before changing anything.

For specific versions, use the [CurseForge Files page](https://www.curseforge.com/minecraft/modpacks/still-watching/files).

Use the latest release unless a server or existing world requires a specific older version.

---

## Other Launchers

Other launchers may work only if they properly support CurseForge manifests and dependency downloads.

Use the official CurseForge export/import flow where supported.

General flow:

1. Choose **Import Modpack**, **Install from CurseForge**, or the launcher’s equivalent.
2. Search for **Still Watching**, or import the official CurseForge archive.
3. Confirm Minecraft **1.20.1**.
4. Confirm the loader is **Forge**.
5. Allocate RAM.
6. Launch with no extra modifications.
7. Test a new world.

> [!CAUTION]
> Manual assembly is unsupported unless you know exactly what you are doing. Bugs from third-party launcher installs should be reproduced on CurseForge before reporting.

---

## RAM Allocation

| System RAM | Suggested Minecraft RAM |
| --- | --- |
| 8 GB | 5 GB, close background apps |
| 12 GB | 5–6 GB |
| 16 GB | 6–8 GB |
| 32 GB+ | 8 GB |

Useful values:

| RAM | MB value |
| --- | ---: |
| 5 GB | `5120 MB` |
| 6 GB | `6144 MB` |
| 8 GB | `8192 MB` |

> [!WARNING]
> More RAM is not always better. Do not allocate all system RAM. If the whole PC freezes, stutters badly, or starts swapping heavily, allocation may be too high.

### CurseForge RAM Steps

1. Open **CurseForge**.
2. Go to **My Modpacks**.
3. Select **Still Watching**.
4. Open **Profile Options**.
5. Disable **Use System Memory Settings**.
6. Set the MB value:
   - `5120 MB` = 5 GB
   - `6144 MB` = 6 GB
   - `8192 MB` = 8 GB
7. Save.
8. Relaunch the pack.

---

## First Launch Checklist

Launch clean before changing anything:

- No extra mods.
- No shaders.
- No extra resource packs.
- Create a new test world.
- Check loading.
- Check audio.
- Check FPS.
- Exit normally.
- Add optional changes one at a time.

If the clean pack works and the modified profile breaks, the modification is the suspect. Drag it into the light and test it.

---

## Recommended Game Settings

| Setting | Starting Point | Why |
| --- | --- | --- |
| Render Distance | 8–10 chunks | Keeps performance stable without crushing atmosphere |
| Simulation Distance | 5–6 chunks | Reduces CPU load |
| Brightness | 30–60%, adjust for accessibility | Preserves darkness without making the game uncomfortable |
| Shaders | Off first | Confirms the base pack works before adding GPU load |
| Resource packs | Off first | Prevents conflicts during first launch |
| Hostile/Ambient audio | 70–100% | Sound matters in a horror pack |
| Subtitles | Optional/accessibility | Useful if audio cues are hard to track |
| Headphones | Recommended | Better directional audio and atmosphere |

### Accessibility Notes

- Subtitles are fine.
- Higher brightness is fine if needed.
- Lower visual intensity if fog, darkness, or shaders cause discomfort.
- Take breaks.

Accessibility is not “playing wrong.” The goal is fear, not eye strain.

---

## Updating Safely

Do not raw-dog updates on your main world. Back up first.

1. Back up worlds.
2. Check the [CurseForge Files page](https://www.curseforge.com/minecraft/modpacks/still-watching/files).
3. Update through the launcher.
4. Launch clean.
5. Test a disposable or new world.
6. Only then open your main world.

> [!IMPORTANT]
> All clients and the server must use the same pack version, Minecraft version, Forge version, and required configs.

---

## Backups

Back up before:

- Updates.
- Server moves.
- Config edits.
- World migration.
- Adding major extra mods.

Back up these when relevant:

| Folder/File | Why |
| --- | --- |
| `saves/` | Singleplayer worlds |
| `config/` | Main mod configuration |
| `defaultconfigs/` | Default world/server config templates |
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

> [!TIP]
> Test that the archive actually contains the files. A backup you never checked is just a bedtime story.

---

## Multiplayer & Server Setup

Still Watching supports multiplayer when the client, server, Minecraft version, Forge version, pack version, and configs match.

> [!WARNING]
> Do not mix pack versions between players and server. Version mismatch errors are not mysterious. They are Minecraft screaming the answer at you.

### Recommended Server Path

Use this if your hosting provider supports CurseForge modpacks.

1. Open your hosting panel.
2. Find **Modpacks**, **CurseForge Modpacks**, or the host’s equivalent.
3. Search for **Still Watching**.
4. Install the exact same Still Watching version as all clients.
5. Start the server.
6. Check the console for errors.
7. Join with a clean matching client.

This is the cleanest route. Let the host installer do the boring work.

### Official Server Pack

Use this if CurseForge provides a server pack for your chosen release.

1. Open the [CurseForge Files page](https://www.curseforge.com/minecraft/modpacks/still-watching/files).
2. Select the exact same version used by clients.
3. Download the server pack, if available.
4. Extract it into a clean server folder.
5. Run the included start script or Forge server jar.
6. Accept the Minecraft EULA when prompted.
7. Restart the server.
8. Check the console.
9. Join with a matching client.

> [!CAUTION]
> Do not invent your own server pack unless you understand mod sides, configs, and Forge logs. The server will not politely ignore client-only nonsense.

### Manual Forge Server

Manual setup is advanced and not the recommended support path.

1. Install a clean Forge **1.20.1** server.
2. Use the required Forge build for the selected release.
3. Copy server-compatible mods only.
4. Copy required configs.
5. Remove client-only mods.
6. Allocate server RAM.
7. Start the server.
8. Read logs.
9. Fix errors.
10. Test before inviting players.

Client-only categories often include:

- Shader loaders.
- Minimap/map rendering mods.
- HUD-only mods.
- Rendering/performance mods.
- Visual-only mods.
- Audio-only mods.

Do **not** provide or rely on an exact server mod list unless it has been verified from the actual pack files for that release.

---

## Troubleshooting

Before reporting, try this clean baseline:

1. Restart the launcher.
2. Confirm Minecraft **1.20.1**.
3. Confirm **Forge** loader.
4. Allocate **5–8 GB** RAM.
5. Remove extra mods.
6. Disable shaders and resource packs.
7. Repair or reinstall the profile.
8. Test a new world.
9. Check `latest.log` or the crash report.

### Diagnosis Table

| Problem | First Check | Next Action |
| --- | --- | --- |
| Won’t launch | Correct launcher profile, Forge, Java, RAM | Repair/reinstall the CurseForge profile and launch clean |
| Crash during loading | Extra mods, shaders, corrupted files, memory errors | Remove extras, allocate 5–8 GB, check crash report |
| Crash after joining world | Whether it happens in a new world | Restore backup if only one world crashes |
| Server crashes on boot | Client-only mods, missing mods, Forge mismatch | Read server `latest.log` and remove wrong-side mods |
| Server rejects client | Pack version, Minecraft version, Forge version, configs | Make client and server match exactly |
| Bad FPS | Render distance, simulation distance, shaders | Lower settings, close background apps, launch without extras |
| Missing mods/config mismatch | Client/server files and configs | Reinstall matching versions on both sides |
| Audio feels wrong | Output device, Minecraft audio sliders, headphones | Check hostile/ambient volume and system output |
| Weird behavior after update | Update path and old configs | Test clean profile and disposable world |
| Issue appears only after extra mods | The added mods | Reproduce on clean Still Watching before reporting |

### Clean Reinstall

1. Back up worlds first.
2. Open CurseForge.
3. Go to **My Modpacks**.
4. Delete the broken **Still Watching** profile.
5. Reinstall from the official CurseForge page.
6. Allocate RAM again.
7. Launch once before restoring worlds or adding extras.
8. Restore backed-up worlds only after the clean install works.

### Crash During Loading

Common causes:

- Wrong Minecraft version.
- Wrong loader.
- Wrong Java version.
- Not enough RAM.
- Corrupted profile.
- Broken extra mods.
- Shader or resource pack conflict.
- Client-only/server-only mismatch.
- Outdated graphics drivers.

### Crash After Joining a World

Ask:

1. Does it happen in a new world?
2. Did you add or remove mods after creating the world?
3. Did you update without a backup?
4. Does the crash report name a specific mod, entity, biome, structure, or dimension?
5. Can you reproduce it at the same location or with the same action?

If one world crashes but fresh worlds work, the issue may be world-specific. If every world crashes, the install or config is probably broken.

### Lag or Bad FPS

Try:

1. Lower render distance.
2. Lower simulation distance.
3. Close background apps.
4. Disable shaders.
5. Remove extra resource packs.
6. Keep included performance mods and configs intact.
7. Restart after major video setting changes.

Do not max graphics, pile on shaders, and then act shocked when the frames get buried.

---

## Logs and Crash Reports

Useful files are inside the modpack profile folder.

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

### Find the CurseForge Profile Folder

1. Open **CurseForge**.
2. Go to **My Modpacks**.
3. Right-click **Still Watching**, or click the three dots.
4. Choose **Open Folder**.
5. Check:
   - `logs/`
   - `crash-reports/`
   - `saves/`
   - `config/`

> [!CAUTION]
> Logs may contain usernames, local file paths, server IPs, system details, or tokens. Review before posting publicly.

Useful log search terms:

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

Read the first meaningful error, not only the final line. The last line often just describes the wreckage.

---

## Bug Reports

Open bug reports here: [GitHub Issues](../../issues)

Reports should be based on clean install reproduction where possible.

Include:

- Still Watching version.
- Launcher.
- Minecraft version.
- Forge version, if visible.
- Java version, if relevant.
- Operating system.
- Singleplayer or multiplayer.
- Dedicated server, LAN, or hosted server, if relevant.
- Crash report or `latest.log`.
- Steps to reproduce.
- Screenshots or clips, if useful.
- Extra mods, shaders, resource packs, or config edits.

### Good Report Example

```text
Pack version: Still Watching vX.X.X
Launcher: CurseForge App
Minecraft: 1.20.1
Loader: Forge
Mode: Singleplayer
OS: Windows 11

Issue:
Game crashes when entering a cave structure in a new world.

Steps to reproduce:
1. Install Still Watching from CurseForge.
2. Launch with no extra mods, shaders, or resource packs.
3. Create a new world.
4. Enter the cave structure.
5. Game crashes.

Attached:
- latest.log
- crash report
- screenshot of location before crash
```

### Bad Report Example

```text
it broke fix pls
```

That report gives nothing to debug. Logs and steps, or everyone is just throwing bones at the wall.

---

## FAQ

### Can I install from GitHub?

No. Install from CurseForge.

The GitHub ZIP is not a playable modpack installer. It is repository source content for documentation, issue tracking, maintenance, and licensing clarity.

### Can I add extra mods?

Yes, but added mods are your responsibility.

If something breaks, reproduce the issue on a clean CurseForge install before reporting it.

### Can I use shaders?

Yes, if your system can handle them.

Launch clean first. Add shaders only after the base pack works.

### Can I play without headphones?

Yes.

Headphones are recommended because sound is part of the horror design, but they are not required.

### Which version should I install?

Use the latest version on the [CurseForge Files page](https://www.curseforge.com/minecraft/modpacks/still-watching/files), unless your world or server requires a specific older version.

### Where do I find the Forge version?

Check:

- The selected CurseForge file.
- The launcher profile details.
- The top section of `logs/latest.log`.

### Should I report bugs after modifying the pack?

Only after testing the same issue on a clean profile.

If the issue only happens with extra mods, shaders, edited configs, or third-party launcher changes, the problem is probably in the modification.

### Can I use another launcher?

Maybe.

The launcher must properly support CurseForge manifests and dependency downloads. If a third-party launcher install breaks, reproduce the issue in CurseForge before reporting.

### Why does server setup fail?

Usually one of these:

- Client and server pack versions do not match.
- Forge version does not match.
- Configs do not match.
- Client-only mods were placed on the server.
- Server pack was manually assembled incorrectly.
- Server RAM is too low.
- The wrong Minecraft version was used.

Read the server log. It is usually less mysterious than it looks.

---

## Final Checklist

Before serious play:

- Installed from CurseForge.
- Confirmed Minecraft **1.20.1** and Forge.
- Allocated **5–8 GB** RAM.
- Launched clean.
- Tested a new world.
- Audio works.
- Backed up important worlds.
- Matched client/server versions for multiplayer.
- Saved logs/crash reports for useful bug reports.

Then step into the fog. Do not trust the quiet.
