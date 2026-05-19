# Still Watching Installation Guide

A practical install and survival-safe setup guide for **Still Watching**, a Forge `1.20.1` Minecraft horror-survival modpack built around fog, sound, darkness, exploration, and the feeling that the world noticed you before you noticed it.

> [!IMPORTANT]
> **Install Still Watching from CurseForge. Do not install from the GitHub ZIP.**
>
> This repository is for documentation, issue tracking, source files, screenshots, and licensing clarity. The playable modpack release lives on CurseForge. If GitHub and CurseForge ever disagree, trust CurseForge first and report the mismatch.

---

## Project at a Glance

| Item | Details |
| --- | --- |
| Modpack | **Still Watching** |
| Creator | **Soumyajit** |
| Official download | [CurseForge](https://www.curseforge.com/minecraft/modpacks/still-watching) |
| Version files | [CurseForge Files](https://www.curseforge.com/minecraft/modpacks/still-watching/files) |
| CurseForge Project ID | `1420406` |
| Minecraft | `1.20.1` |
| Loader | `Forge` |
| Java | `17` if your launcher asks |
| RAM | `5 GB` minimum, `6–8 GB` recommended |
| Disk space | `5–10 GB` recommended |
| Best experience | Headphones, dim room, stable FPS, and enough awareness to not treat darkness like wallpaper |

Never download the pack from random mirrors. CurseForge is the source of truth. Mirror sites are where malware goes to cosplay as convenience.

---

## Contents

- [Fast Install](#fast-install)
- [Before You Install](#before-you-install)
- [CurseForge App Install](#curseforge-app-install)
- [CurseForge Website Install](#curseforge-website-install)
- [Other Launchers](#other-launchers)
- [RAM Allocation](#ram-allocation)
- [First Launch Checklist](#first-launch-checklist)
- [Recommended Game Settings](#recommended-game-settings)
- [Updating Safely](#updating-safely)
- [Backups](#backups)
- [Multiplayer & Server Notes](#multiplayer--server-notes)
- [Troubleshooting](#troubleshooting)
- [Logs and Crash Reports](#logs-and-crash-reports)
- [Bug Reports](#bug-reports)
- [FAQ](#faq)
- [Final Checklist](#final-checklist)

---

## Fast Install

Use this if you want the pack installed without turning your `.minecraft` folder into a crime scene.

1. Install the [CurseForge App](https://www.curseforge.com/download/app).
2. Open **Minecraft** inside CurseForge.
3. Search for **Still Watching**.
4. Confirm the project is by **Soumyajit**.
5. Click **Install**.
6. Open the profile options and allocate at least `5 GB` RAM.
7. Launch once with **no extra mods, shaders, or resource packs**.
8. Create a new test world.
9. Confirm loading, audio, and FPS are stable.
10. Only then add optional shaders, extra resource packs, or personal changes.

The first launch can be slow because Forge and the launcher are preparing files. Slow is normal. Crash loops are not.

---

## Before You Install

You need:

- A valid **Minecraft: Java Edition** account.
- The **CurseForge App**, or another launcher that can properly install CurseForge modpack manifests.
- Enough memory to allocate at least `5 GB` to Minecraft.
- `5–10 GB` of free disk space for the pack, worlds, logs, screenshots, and backups.
- A stable internet connection.
- Headphones or decent stereo audio.

Still Watching uses sound, fog, darkness, and hostile timing as core pressure. Playing muted is technically allowed, just like walking into traffic blindfolded is technically movement.

### Do not do this

- Do **not** install from the GitHub source ZIP.
- Do **not** drag random `.jar` files into the pack before first launch.
- Do **not** install from unofficial mirrors.
- Do **not** allocate all system RAM to Minecraft.
- Do **not** report bugs from a modified profile until you reproduce them on a clean one.

A clean baseline saves everyone time. Chaos is not debugging. It is arson with a loading bar.

---

## CurseForge App Install

This is the recommended method. It handles the profile, dependencies, launcher setup, and updates cleanly.

1. Download and install the [CurseForge App](https://www.curseforge.com/download/app).
2. Open the app.
3. Select **Minecraft**.
4. Open **Browse** or **Discover**.
5. Search for **Still Watching**.
6. Confirm the listing:
   - Name: **Still Watching**
   - Author: **Soumyajit**
   - Minecraft: `1.20.1`
   - Loader: `Forge`
7. Click **Install**.
8. Wait for the download and setup to finish.
9. Go to **My Modpacks**.
10. Select **Still Watching**.
11. Open **Profile Options**.
12. Allocate RAM.
13. Click **Play**.

### Confirm the correct project

Before installing, check the listing like your save file depends on it:

- It must be **Still Watching**.
- It must be by **Soumyajit**.
- It must target Minecraft `1.20.1`.
- It must use **Forge**.
- It must come from CurseForge, not a reupload wearing a fake moustache.

If any of those details are wrong, stop. Do not negotiate with suspicious downloads.

---

## CurseForge Website Install

Use this if you found the pack in your browser first.

1. Open the official CurseForge page: [Still Watching](https://www.curseforge.com/minecraft/modpacks/still-watching).
2. Click **Install**, **Install via App**, or the current CurseForge equivalent.
3. Allow the browser to open the CurseForge App.
4. Let CurseForge create the profile.
5. Launch from **My Modpacks**.
6. Allocate RAM before serious play.

For specific versions, use the [CurseForge Files page](https://www.curseforge.com/minecraft/modpacks/still-watching/files). Install the latest release unless your world or server requires an older version.

---

## Other Launchers

Some launchers can import CurseForge modpacks. Use them only if they support CurseForge manifests and dependency downloads properly.

General flow:

1. Open your launcher.
2. Choose **Import Modpack**, **Install from CurseForge**, or the launcher’s equivalent.
3. Search for **Still Watching**, or import the official `.zip` from the CurseForge Files page.
4. Confirm Minecraft `1.20.1` and Forge.
5. Allocate RAM.
6. Launch once with no extra modifications.
7. Test a new world before moving your main world or server into it.

If a launcher asks you to manually assemble every mod yourself, that is not an install process. That is punishment with a file picker.

### Manual import rules

Only manually import a `.zip` if:

- It came from the official CurseForge project page.
- Your launcher supports CurseForge modpack archives.
- You are importing the archive directly.
- You are not unzipping it and flinging folders around like a raccoon with admin rights.

A valid CurseForge modpack archive normally includes manifest metadata and overrides. A zipped `mods` folder from a stranger is not a modpack. It is a liability in a trench coat.

---

## RAM Allocation

Recommended allocation:

- Minimum: `5 GB` / `5120 MB`
- Recommended: `6 GB` / `6144 MB`
- High-end comfort: `8 GB` / `8192 MB`

| System RAM | Suggested Minecraft RAM | Notes |
| --- | --- | --- |
| `8 GB` | `5 GB` | Close browsers, overlays, recorders, and background junk. |
| `12 GB` | `5–6 GB` | Leave breathing room for the OS. |
| `16 GB` | `6–8 GB` | Best normal target. |
| `32 GB+` | `8 GB` | More is not automatically better. Java is not a dragon. Stop feeding it. |

Do **not** allocate all system RAM to Minecraft. Starving the operating system so Java can hoard memory is not optimization. It is a hostage situation.

### CurseForge RAM steps

1. Open **CurseForge**.
2. Go to **My Modpacks**.
3. Right-click **Still Watching**, or click the three dots.
4. Open **Profile Options**.
5. Disable **Use System Memory Settings**.
6. Set memory to one of these:
   - `5120 MB` for `5 GB`
   - `6144 MB` for `6 GB`
   - `8192 MB` for `8 GB`
7. Save.
8. Relaunch the pack.

### RAM symptoms

| Symptom | Likely fix |
| --- | --- |
| Crash during loading with memory errors | Increase allocation within safe limits. |
| Stutter after long sessions | Restart the game and close background apps. |
| Whole PC freezes or swaps heavily | Allocation may be too high. Lower it. |
| Low FPS without memory errors | Lower render distance, simulation distance, or shaders. |

RAM is medicine, not seasoning. Use enough. Do not dump the bottle into the soup.

---

## First Launch Checklist

Before adding anything extra:

1. Launch the pack clean.
2. Do not add extra mods.
3. Do not enable shaders.
4. Do not stack resource packs.
5. Create a new test world.
6. Confirm the world loads.
7. Confirm audio works.
8. Confirm FPS is playable.
9. Close the game normally.
10. Then make optional changes one at a time.

A boring baseline is useful. A chaotic baseline is just a crime scene with particles enabled.

### Clean test settings

| Setting | Starting point |
| --- | --- |
| RAM | `5–8 GB` |
| Render Distance | `8–10 chunks` |
| Simulation Distance | `5–6 chunks` |
| Shaders | Off |
| Extra resource packs | Off |
| Audio | Headphones recommended |

If the clean pack works but breaks after your changes, the pack did not betray you. Your changes did.

---

## Recommended Game Settings

These are starting points, not holy scripture.

| Setting | Recommended |
| --- | --- |
| Brightness | `30–60%`, unless accessibility requires higher |
| Render Distance | `8–10 chunks` |
| Simulation Distance | `5–6 chunks` |
| Hostile Creatures | `70–100%` |
| Ambient / Environment | `70–100%` |
| Subtitles | Optional, useful for accessibility and noisy rooms |
| Shaders | Off first; enable later only if stable |
| Resource packs | Avoid extras until the clean pack works |
| Fullscreen | Recommended |
| Headphones | Strongly recommended |

Still Watching uses darkness and sound as mechanics. Full-bright, muted audio, and a brutal shader stack can gut the horror and murder your FPS, then leave you wondering who did it. Spoiler: you did.

### Accessibility

Adjust the pack so it is playable for you:

- Enable subtitles if audio cues are hard to track.
- Raise brightness if darkness causes eye strain.
- Lower visual intensity if fog, darkness, or shaders become uncomfortable.
- Reduce volume spikes through Minecraft or system audio settings.
- Take breaks. Horror is entertainment, not a medical endurance test.

---

## Updating Safely

Use the launcher update flow. Do not manually replace random jars unless you enjoy debugging self-inflicted nonsense.

1. Back up important worlds.
2. Open CurseForge.
3. Go to **My Modpacks**.
4. Select **Still Watching**.
5. Check for updates.
6. Update through CurseForge.
7. Launch the pack.
8. Test a new or disposable world.
9. Open your main world only after the update looks stable.

### Multiplayer update rule

Client and server must match:

- Same Still Watching version.
- Same Minecraft version.
- Same Forge version.
- Same required configs.

Do not update the client and leave the server behind. Do not update the server and leave clients behind. Version mismatch is a bug factory with a loading screen.

---

## Backups

Back up before updates, major config edits, server migrations, and suspicious experiments.

Back up:

- `saves/`
- `config/`
- `defaultconfigs/`, if present
- `serverconfig/` inside world folders, if present
- `journeymap/` or map data, if you care about it
- `screenshots/`, if you want proof of your terrible decisions
- Server world folders
- Server `ops.json`, `whitelist.json`, and ban files, if relevant

Use clear names:

```text
Still-Watching-worldname-before-vX.X.X-update.zip
```

A backup named `new new final real backup 2.zip` is not a system. It is a cry for help.

### Restore check

For important worlds, occasionally verify the archive opens and contains the expected folders. A broken backup is just griefing yourself in advance.

---

## Multiplayer & Server Notes

Still Watching can be played in multiplayer when every client and the server use matching versions.

> [!WARNING]
> Client, server, Minecraft version, Forge version, pack version, and required configs must match unless a release note says otherwise.

### Choose your server path

| Situation | Use |
| --- | --- |
| Your host supports CurseForge packs | Host installer |
| CurseForge provides a server pack for your version | Official server pack |
| No host installer and no server pack | Manual Forge server, advanced only |
| You do not understand client-only mods | Do not use manual setup |

### Server preflight

Before inviting players:

1. Confirm client and server use the same pack version.
2. Confirm both target Minecraft `1.20.1`.
3. Confirm the required Forge build matches.
4. Start the server once and read the console.
5. Join with a clean client profile.
6. Test a new world.
7. Back up before updates or config changes.

Red console text is not decoration. Read it before it reads you.

### Hosted server with CurseForge support

1. Open your hosting panel.
2. Find **Modpacks**, **CurseForge Modpacks**, or the equivalent.
3. Search for **Still Watching**.
4. Install the version matching your client.
5. Start the server.
6. Check the console for missing mods, Forge mismatch, or config errors.
7. Join using the matching client version.

If your host has a one-click installer, use it. Uploading a full client profile by FTP is caveman deployment.

### Official server pack

If CurseForge provides a server pack for your chosen version:

1. Open the [CurseForge Files page](https://www.curseforge.com/minecraft/modpacks/still-watching/files).
2. Select the same version your client uses.
3. Download the server pack, if available.
4. Extract it into a clean server folder.
5. Run the included start script or Forge server jar.
6. Accept the Minecraft EULA when prompted.
7. Restart the server.
8. Read the console.
9. Join with a matching clean client.

Do not redistribute modified server packs unless every included mod and config allows it under its license.

### Manual Forge server

Manual setup is advanced. Use it only when no server pack exists and you understand Forge servers.

1. Install a clean Forge `1.20.1` server.
2. Use the Forge build required by the pack release.
3. Copy only server-compatible mods.
4. Copy required configs.
5. Do **not** copy client-only mods.
6. Allocate enough server RAM.
7. Start the server.
8. Remove or replace anything the crash log identifies as client-only or incompatible.
9. Test with a clean client before adding extra changes.

Manual setup is where confidence gets audited by stack traces. Move slowly.

### Client-only mod warning

Client-only categories often include:

- Shader loaders.
- HUD/UI-only mods.
- Minimap or map rendering mods.
- Client performance/rendering mods.
- Audio/visual-only mods.

If a dedicated server crashes instantly, check for client-only mods before blaming the pack, Forge, the moon, or whatever else is nearby.

---

## Troubleshooting

Start with the obvious fixes. They are obvious because they work.

1. Restart the launcher.
2. Confirm the profile is Minecraft `1.20.1` and Forge.
3. Allocate at least `5 GB` RAM.
4. Remove manually added mods.
5. Disable shaders and extra resource packs.
6. Repair or reinstall the profile.
7. Check `latest.log` or the crash report.

### Fast diagnosis

| Problem | Check first |
| --- | --- |
| Won’t launch | RAM, Java, Forge version, profile repair |
| Crashes during loading | Extra mods, corrupted install, crash report |
| Crashes in one world | Test a new world, restore backup |
| Server crashes | Version mismatch, client-only mods, server logs |
| Bad FPS | Render distance, simulation distance, shaders |
| Missing mods/config mismatch | Client/server pack versions |
| Audio feels wrong | Output device, sound sliders, headphones |
| Weird behavior after update | Clean install and test world |

### Clean reinstall

Use this when repair fails.

1. Back up your worlds first.
2. Open CurseForge.
3. Go to **My Modpacks**.
4. Delete the broken **Still Watching** profile.
5. Reinstall from the official CurseForge page.
6. Allocate RAM again.
7. Launch once before restoring worlds or adding extras.
8. Restore your backed-up world only after the clean install works.

Deleting random folders while the launcher is open is not a clean reinstall. That is file-system vandalism.

### Crash during loading

Common causes:

- Wrong Minecraft version.
- Wrong loader.
- Wrong Java version.
- Not enough RAM.
- Corrupted profile.
- Broken extra mods.
- Shader/resource pack conflict.
- Client-only/server-only mismatch.
- Outdated graphics drivers.

### Crash after joining a world

Ask:

1. Does it happen in a new world?
2. Did you add or remove mods after creating the world?
3. Did you update without a backup?
4. Does the crash report name a specific mod, entity, biome, structure, or dimension?
5. Can you reproduce it at the same location or with the same action?

If one world crashes but fresh worlds work, the issue may be world-specific. If every world crashes, the install or config is probably cooked.

### Lag or bad FPS

Try:

1. Lower render distance.
2. Lower simulation distance.
3. Close background apps.
4. Disable heavy shaders.
5. Remove extra resource packs.
6. Keep included performance mods and configs intact.
7. Restart after major video setting changes.

Do not max out every graphics option and then act shocked when the frames die. You built the crime scene.

### Multiplayer connection issues

Check:

1. Client and server use the same pack version.
2. Both target Minecraft `1.20.1`.
3. Both use the correct Forge version.
4. Required configs match.
5. Server does not contain client-only mods.
6. Server has enough RAM.
7. Server log does not show missing mods or config mismatches.

### Useful log search terms

Search logs for:

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

Read the first meaningful error, not only the final line. The last line often just announces the corpse; the murder weapon is higher up.

---

## Logs and Crash Reports

Useful files are inside the modpack profile folder.

Look for:

```text
logs/latest.log
crash-reports/crash-YYYY-MM-DD_HH.mm.ss-client.txt
crash-reports/crash-YYYY-MM-DD_HH.mm.ss-server.txt
```

For servers, also check:

```text
logs/latest.log
logs/debug.log
crash-reports/
```

### Find the CurseForge profile folder

1. Open CurseForge.
2. Go to **My Modpacks**.
3. Right-click **Still Watching**, or click the three dots.
4. Choose **Open Folder**.
5. Look for `logs/`, `crash-reports/`, `saves/`, and `config/`.

That folder is the crime scene. Do not clean it before collecting evidence.

> [!CAUTION]
> Logs may contain usernames, local file paths, server IPs, system details, and sometimes tokens. Review logs before posting them publicly.

When sharing logs:

- Upload the full file when possible.
- Do not paste only the final three lines unless asked.
- Remove private tokens, IPs, or personal information.
- Say what you were doing when it crashed.
- For server issues, include both client and server logs when possible.

---

## Bug Reports

Open issues here: [GitHub Issues](../../issues)

Before reporting, reproduce the issue on a clean install.

Reports involving extra mods, custom shaders, edited configs, or manually changed files may be closed unless the same issue happens on an unmodified Still Watching profile.

Include:

- Still Watching version.
- Launcher used.
- Minecraft version.
- Forge version, if visible.
- Java version, if relevant.
- Operating system.
- Singleplayer or multiplayer.
- Dedicated server, LAN, or hosted server, if relevant.
- Crash report or `latest.log`.
- Steps to reproduce.
- Screenshots or clips, if useful.
- Any extra mods, shaders, resource packs, or config changes.

Good report:

```text
Pack version: Still Watching V1.0.x
Launcher: CurseForge App
Mode: Singleplayer
Issue: Crash when entering a cave near a structure
Steps:
1. Create a new world
2. Travel to a cave structure
3. Enter the lower chamber
4. Game crashes
Attached: latest.log and crash report
```

Bad report:

```text
it broke fix pls
```

That is not a bug report. That is a haunted postcard.

---

## FAQ

### Can I install from GitHub?

No. Use CurseForge for player installs. The GitHub ZIP is not the modpack installer.

### Can I add extra mods?

Yes, but added mods are your responsibility. If the pack breaks after you add one, test again on a clean install before reporting it.

### Can I use shaders?

Yes, if your system can handle them. Test the clean pack first. Beautiful fog at 8 FPS is just a slideshow with trauma.

### Can I play without headphones?

Yes, but headphones are strongly recommended. Sound is part of the pack’s threat design.

### Which version should I install?

Install the latest release shown on the official CurseForge Files page unless you need an older version for world or server compatibility.

### Where do I find the exact Forge version?

Check the selected CurseForge file, your launcher profile details, or the top of `logs/latest.log`.

### Should I report bugs after modifying the pack?

Only after testing the same issue on a clean install. If it only happens with your extra mods, shaders, edited configs, or manual file changes, the bug is probably yours. Congratulations, you invented a problem.

---

## Final Checklist

Before serious play:

- Installed from CurseForge.
- Confirmed Minecraft `1.20.1` and Forge.
- Allocated `5–8 GB` RAM.
- Launched once clean.
- Tested a new world.
- Confirmed audio works.
- Backed up important worlds.
- Matched client/server versions for multiplayer.

Then step into the fog.

**Do not trust the quiet.**
