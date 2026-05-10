# Still Watching Installation Guide

A complete installation, update, server, and troubleshooting guide for **Still Watching** — a Forge `1.20.1` Minecraft horror-survival modpack where fog is cover, sound is a warning, and the quiet is usually lying.

> **Official download source:** [Still Watching on CurseForge](https://www.curseforge.com/minecraft/modpacks/still-watching)  
> **CurseForge Project ID:** `1420406`  
> **Minecraft:** `1.20.1`  
> **Loader:** `Forge`  
> **Java:** `17` if your launcher asks  
> **Forge version:** check the selected CurseForge file page for the exact required build  
> **Recommended RAM:** `5 GB` minimum, `6–8 GB` preferred  
> **Recommended free disk space:** `5–10 GB`  
> **Recommended install method:** CurseForge App  
> **Server pack:** check the CurseForge **Files** page for the version you want  
> **Best played with:** headphones, low light, and basic survival instincts

Do **not** download Still Watching from random reupload sites. Use CurseForge or a launcher that pulls directly from CurseForge. Malware loves impatient players. Do not hand it a chair.

This repository is for documentation, issue tracking, source-side material, and licensing clarity. Player downloads should come from CurseForge. Do **not** treat this GitHub repository as the player install package.

---

## Table of Contents

- [Official Links](#official-links)
- [Quick Install](#quick-install)
- [First Launch Checklist](#first-launch-checklist)
- [Support Scope](#support-scope)
- [Before You Install](#before-you-install)
- [Recommended Method: CurseForge App](#recommended-method-curseforge-app)
- [Installing from the CurseForge Website](#installing-from-the-curseforge-website)
- [Installing with Another Compatible Launcher](#installing-with-another-compatible-launcher)
- [Manual Import Notes](#manual-import-notes)
- [RAM Allocation](#ram-allocation)
- [Java Notes](#java-notes)
- [Recommended Game Settings](#recommended-game-settings)
- [Accessibility Notes](#accessibility-notes)
- [Multiplayer / Server Notes](#multiplayer--server-notes)
- [Updating the Modpack](#updating-the-modpack)
- [Safe Backup Checklist](#safe-backup-checklist)
- [Troubleshooting](#troubleshooting)
- [Finding Logs and Crash Reports](#finding-logs-and-crash-reports)
- [Bug Reports](#bug-reports)
- [FAQ](#faq)
- [Documentation Roadmap](#documentation-roadmap)
- [Final Warning](#final-warning)

---

## Official Links

- [Still Watching on CurseForge](https://www.curseforge.com/minecraft/modpacks/still-watching)
- [Download the CurseForge App](https://www.curseforge.com/download/app)
- [Minecraft: Java & Bedrock Edition for PC](https://www.minecraft.net/store/minecraft-java-bedrock-edition-pc)
- [GitHub Issues](../../issues)

---

## Quick Install

For most players, this is all you need:

1. Install the **CurseForge App**.
2. Open **Minecraft** inside the app.
3. Search for **Still Watching**.
4. Confirm the project is by **Soumyajit**.
5. Click **Install**.
6. Allocate at least `5 GB` RAM.
7. Launch the pack.
8. Put on headphones.
9. Regret entering the fog.

Do **not** download the modpack from GitHub. This repository is for documentation, source-side material, issue tracking, and licensing clarity. Player downloads should come from CurseForge.

The first launch may take longer than later launches because Forge and the launcher are preparing files. Do not force-close the game unless it is clearly frozen or has crashed.

If something breaks, do not start randomly deleting files like a raccoon with admin permissions. Use the troubleshooting section below.

---

## First Launch Checklist

Before changing anything:

1. Launch the pack once without extra mods.
2. Create or open a test world.
3. Confirm the game loads correctly.
4. Confirm audio works.
5. Confirm FPS is playable.
6. Only then add shaders, resource packs, or optional changes.

If the clean pack works but breaks after your changes, the problem is probably your changes. That is not a curse. That is cause and effect wearing blocky shoes.

---

## Support Scope

Supported:

- Clean CurseForge App installations.
- Official CurseForge downloads.
- Matching client/server pack versions.
- Reproducible bugs with logs or crash reports.
- Server setups using a host installer or official server pack, when available.

Not supported unless reproduced on a clean install:

- Unofficial reuploads.
- Manually assembled mod lists.
- Random extra mods.
- Modified configs.
- Heavy shaders or stacked resource packs.
- Outdated versions, unless needed for a specific server or world.
- Server crashes caused by client-only mods.

This is documentation armor. Wear it before the issue tracker becomes a landfill with Markdown support.

---

## Before You Install

Make sure you have:

- A valid **Minecraft: Java Edition** account.
- The **CurseForge App**, or another launcher that supports CurseForge modpacks.
- Enough system memory to allocate at least `5 GB` to Minecraft.
- At least `5–10 GB` of free disk space for the pack, logs, worlds, screenshots, and backups.
- A stable internet connection for downloading the pack and dependencies.
- Headphones or decent stereo audio.

Still Watching is designed around atmosphere, audio cues, fog, darkness, and stalking entities. Playing muted is legal, but so is eating soup with a fork. Neither is smart.

---

## Recommended Method: CurseForge App

This is the cleanest install path because the CurseForge App handles the profile and dependency download process.

1. Download and install the **CurseForge App**.
2. Open the app.
3. Select **Minecraft**.
4. Open **Browse** or **Discover**.
5. Search for **Still Watching**.
6. Confirm these details:
   - Author: **Soumyajit**
   - Minecraft version: `1.20.1`
   - Loader: `Forge`
7. Click **Install**.
8. Wait for the installation to finish.
9. Go to **My Modpacks**.
10. Select **Still Watching**.
11. Open profile settings and allocate RAM.
12. Click **Play**.

The CurseForge App can install modpacks from Browse/Discover and then exposes installed packs through **My Modpacks**. That is the path you want. Dragging random jars into the folder is how clean installs go to die.

---

## Installing from the CurseForge Website

Use this if you found the modpack page in your browser first.

1. Open the official project page:
   - [https://www.curseforge.com/minecraft/modpacks/still-watching](https://www.curseforge.com/minecraft/modpacks/still-watching)
2. Click **Install** or **Install via App**.
3. Allow your browser to open the CurseForge App.
4. Let the app complete the installation.
5. Launch the pack from **My Modpacks**.

The CurseForge website may show newer files after this guide is written. Treat the project page as the source of truth for the current release. Hardcoding a “latest version” in docs is a classic way to make the docs rot in public.

---

## Installing with Another Compatible Launcher

Some launchers can install or import CurseForge modpacks. Use this only if the launcher supports CurseForge packs properly.

General flow:

1. Open your launcher.
2. Choose the option to install or import a CurseForge modpack.
3. Search for **Still Watching**, or use the CurseForge project page.
4. Install the latest release matching:
   - Minecraft: `1.20.1`
   - Loader: `Forge`
5. Allocate RAM.
6. Launch the pack.

Only mark a third-party launcher as supported after testing it. Guesswork in docs is how users get sacrificed to the modloader gods.

If your launcher asks for a modpack `.zip`, download it only from the official CurseForge project page. If the launcher asks you to manually assemble every mod yourself, that is not an installation guide anymore; that is punishment with buttons.

---

## Manual Import Notes

Only use manual import if your launcher specifically supports CurseForge-exported modpack `.zip` files.

A valid CurseForge modpack archive normally contains metadata such as a manifest and override files. A random folder zipped from someone’s `.minecraft/mods` directory may not import correctly.

If import fails:

1. Confirm the file is a `.zip`.
2. Confirm it came from the official CurseForge project page.
3. Confirm your launcher supports CurseForge modpack imports.
4. Try reinstalling through the CurseForge App instead.
5. Do not unzip the archive unless your launcher explicitly tells you to.

Do not mix manual imports with half-installed profiles. That creates a mutant profile: too broken to play, too cursed to explain.

---

## RAM Allocation

Recommended allocation: `5 GB` minimum.  
Preferred allocation: `6–8 GB` if your PC can spare it.

| System RAM | Suggested Minecraft Allocation | Notes |
| --- | --- | --- |
| `8 GB` | `5 GB` | Close browsers, launchers, overlays, and background junk. |
| `12 GB` | `5–6 GB` | Safer breathing room for the OS. |
| `16 GB` | `6–8 GB` | Good target for smoother play. |
| `32 GB+` | `8 GB` | More is not always better. Stop feeding Java like it is a dragon. |

Do **not** allocate all system RAM to Minecraft. Your operating system still needs memory. Starving Windows/Linux/macOS to feed Minecraft is not optimization; it is a hostage situation.

### How to allocate RAM in the CurseForge App

1. Open the **CurseForge App**.
2. Go to **My Modpacks**.
3. Right-click **Still Watching**, or click the three dots on the profile.
4. Open **Profile Options**.
5. Uncheck **Use System Memory Settings**.
6. Set allocated memory to:
   - `5120 MB` for `5 GB`
   - `6144 MB` for `6 GB`
   - `8192 MB` for `8 GB`
7. Save changes.
8. Launch the pack again.

If the game still runs badly after correct RAM allocation, do not blindly add more memory. Lower render distance, remove shaders, and check logs. Throwing RAM at every problem is not troubleshooting; it is Java worship.

---

## Java Notes

Minecraft `1.20.1` normally uses Java `17`.

Most modern launchers handle Java automatically. If your launcher asks for a Java version, use Java `17` unless the pack release notes say otherwise.

Do not randomly swap Java versions because a forum goblin said it fixed something in 2017. Wrong Java versions can create crashes that look like modpack problems.

---

## Recommended Game Settings

These settings are not mandatory, but they are good starting points for this pack.

| Setting | Recommended Starting Point |
| --- | --- |
| Brightness | `30–60%`; avoid full bright unless accessibility requires it |
| Render Distance | `8–10 chunks` |
| Simulation Distance | `5–6 chunks` |
| Music | Personal choice |
| Hostile Creatures | `70–100%` |
| Ambient/Environment | `70–100%` |
| Shaders | Off for first launch; enable later only if performance is stable |
| Resource Packs | Avoid stacking extras until the clean pack works |
| Fullscreen | Recommended |
| Headphones | Strongly recommended |

Still Watching uses sound and limited visibility as design tools. If you crank brightness, mute ambience, stack a brutal shader, and then complain that performance or horror is worse, congratulations: you mugged the atmosphere and blamed the victim.

---

## Accessibility Notes

Still Watching is designed around darkness, fog, and sound cues. If needed, adjust brightness, subtitles, volume balance, field of view, or visual settings for comfort and accessibility. Atmosphere matters, but playability matters more.

---

## Multiplayer / Server Notes

Still Watching is listed as a multiplayer modpack, but server setup depends on the files available for the current release and how your host handles CurseForge packs.

> **Version rule:**  
> Client, server, Minecraft version, Forge version, modpack version, and configs must match unless the changelog says otherwise.

### Which server method should I use?

| Situation | Use |
| --- | --- |
| Your host supports CurseForge modpacks | Option A |
| CurseForge provides a server pack for your version | Option B |
| No host installer and no server pack | Option C, advanced only |
| You do not know what client-only mods are | Do not use manual setup |

### Option A: Hosted server with CurseForge support

Use this if your hosting panel has a CurseForge or modpack installer.

1. Open your server host panel.
2. Select **Modpacks**, **CurseForge Modpacks**, or your host's equivalent option.
3. Search for **Still Watching**.
4. Install the version matching your client.
5. Start the server.
6. Check the console for missing mod, Forge, or config errors.
7. Join using the same Still Watching version on your client.

If the host offers one-click installation, use it. Manual FTP upload works only if you know what belongs on the server. Throwing the full client profile onto a server is caveman deployment.

### Option B: Official server pack, if available

Use this if the CurseForge file page provides a server pack for the version you want.

1. Open the CurseForge project page.
2. Go to **Files**.
3. Choose the same version your client uses.
4. Download the server pack if one is provided.
5. Extract it into a clean server folder.
6. Run the included start script or Forge server jar.
7. Accept the Minecraft EULA when prompted.
8. Restart the server.
9. Read the console instead of pretending red text is decorative.

Do not redistribute modified server packs unless the included mods and configs allow it under their licenses.

### Option C: Manual server setup

Manual setup is advanced. Use it only if no server pack is available and you know how Forge servers work.

1. Install a clean Forge `1.20.1` server.
2. Use the Forge server version required by the pack release.
3. Copy required server-compatible mods.
4. Copy required configs.
5. Do **not** copy client-only mods.
6. Give the server enough RAM.
7. Start the server.
8. Remove or replace any mod named in the crash log as client-only or incompatible.
9. Test with a clean client profile before adding extra mods or config edits.

Manual setup is where confidence goes to get audited by stack traces. Move slowly.

### Client-only mods warning

Visual, UI, audio, shader, map, and performance-rendering mods are often client-only. Installing client-only mods on a dedicated server can crash the server before it even finishes tying its shoes.

Common client-only categories include:

- Minimap/map rendering mods.
- Shader loaders.
- HUD/UI-only mods.
- Client performance/rendering mods.
- Audio/visual-only mods.

When in doubt:

- Check the mod page.
- Check the crash log.
- Test with a clean server pack.
- Do not guess and then blame Forge.

---

## Updating the Modpack

Recommended update path:

1. Open the CurseForge App.
2. Go to **My Modpacks**.
3. Select **Still Watching**.
4. Check for updates.
5. Back up worlds before launching the updated version.
6. Update through the launcher.
7. Launch and test.

Before updating an important world:

- Back up `saves/`.
- Back up custom configs.
- Remove extra mods you added yourself if troubleshooting.
- Read changelogs or file notes when available.
- Test the update before committing your main world to it.

After updating:

1. Launch the pack before opening your main world.
2. Create or load a test world.
3. Check controls, audio, FPS, shaders, and resource packs.
4. Join your server only after the server is updated too.
5. Open your main world only after the update looks stable.

> **Version rule:**  
> Do not update the client and leave the server behind. Do not update the server and leave clients behind. Mismatched versions are bug factories with a loading screen.

Never test a modpack update on your only copy of a world. That is not bravery. That is speedrunning regret.

---

## Safe Backup Checklist

Before updates, major config changes, server migrations, or suspicious experiments, back up:

- `saves/`
- `config/`
- `defaultconfigs/`, if present
- `serverconfig/` inside world folders, if present
- `journeymap/` or map data, if you care about it
- `screenshots/`, if you want to keep evidence of bad decisions
- Server world folders
- Server `ops.json`, `whitelist.json`, and banned-player files, if relevant

Name backups clearly:

```text
Still-Watching-worldname-before-vX.X.X-update.zip
```

A backup named `new new final real backup 2.zip` is not a system. It is a cry for help.

---

## Troubleshooting

### Start here: common fixes

Try these before opening an issue:

1. Restart the launcher.
2. Confirm the profile is Minecraft `1.20.1` with Forge.
3. Allocate at least `5 GB` RAM.
4. Remove manually added mods.
5. Disable shaders and extra resource packs.
6. Repair or reinstall the profile.
7. Check `latest.log` or the crash report.

### Fast diagnosis

| Problem | Start here |
| --- | --- |
| Won't launch | Check RAM, Java, Forge version, and profile repair |
| Crashes during loading | Remove extra mods and check crash report |
| Crashes in one world | Test a new world and restore from backup |
| Crashes on server | Check client-only mods and version mismatch |
| Bad FPS | Lower render/simulation distance and disable shaders |
| No atmosphere/audio | Check headphones, output device, and sound sliders |

### The pack does not launch

Try this first:

1. Restart the launcher.
2. Make sure the profile is Forge `1.20.1`.
3. Allocate at least `5 GB` RAM.
4. Remove manually added mods.
5. Disable extra shaders/resource packs temporarily.
6. Repair or reinstall the profile.
7. Check `latest.log` or the crash report.

### Clean reinstall

Use this when repair does not fix the profile.

1. Back up your worlds first.
2. Open the CurseForge App.
3. Go to **My Modpacks**.
4. Delete the broken **Still Watching** profile.
5. Reinstall the pack from the official CurseForge page.
6. Allocate RAM again.
7. Launch once before adding worlds, shaders, resource packs, or extra mods.
8. Restore your backed-up world only after the clean install works.

Do not “clean reinstall” by deleting random folders while the launcher is open. That is not a reinstall. That is file system vandalism.

### The game crashes while loading

Common causes:

- Wrong Minecraft version.
- Wrong mod loader.
- Wrong Java version.
- Not enough RAM.
- Corrupted profile install.
- Broken manual mod additions.
- Client-only/server-only mod mismatch.
- Outdated graphics drivers.
- Shader/resource pack conflict.

### The game crashes after joining a world

Check:

1. Did the crash happen in a new world too?
2. Did you add or remove mods after creating the world?
3. Did you update the pack without backing up?
4. Does the crash report mention a specific mod, entity, biome, structure, or dimension?
5. Can you reproduce it at the same location or action?

If a crash happens only in one world, the issue may be world-specific. If it happens in every world, the install or config is probably cooked.

### The game is laggy

Try this:

1. Lower render distance.
2. Lower simulation distance.
3. Close background apps.
4. Avoid heavy shaders.
5. Avoid stacking extra resource packs.
6. Keep the included performance setup intact.
7. Restart the game after changing major video settings.

Do not set every graphics option to “maximum suffering” and then ask why the frames died. You built the crime scene.

### Audio feels wrong or too quiet

Still Watching uses sound as part of the horror design.

Try this:

1. Use headphones.
2. Keep hostile creature sounds audible.
3. Keep ambient/environment sounds audible.
4. Check Minecraft audio sliders.
5. Check system output device.
6. Enable subtitles if audio cues are hard to hear.
7. Disable external audio effects if they damage positional sound.

### Multiplayer connection issues

Check:

1. Client and server use the same pack version.
2. Client and server target Minecraft `1.20.1`.
3. Client and server use the correct Forge version.
4. Client and server use matching configs where required.
5. The server does not contain client-only mods.
6. The server has enough RAM.
7. The server log does not show missing mods or config mismatch errors.

### Advanced diagnosis

Use this when the basic checks do not expose the problem:

- Test a fresh install with no extra files.
- Test a new world.
- Compare client and server modpack versions.
- Read the first real error in the crash report, not only the final line.
- Search the log for `Caused by`, `Mod File`, `Missing`, `Failed`, and `Exception`.
- Attach the full log when reporting the issue.

---

## Finding Logs and Crash Reports

Useful files usually live inside the modpack profile folder.

Look for:

```text
logs/latest.log
crash-reports/crash-YYYY-MM-DD_HH.mm.ss-client.txt
crash-reports/crash-YYYY-MM-DD_HH.mm.ss-server.txt
```

For server issues, also check:

```text
logs/latest.log
logs/debug.log
crash-reports/
```

> **Privacy warning:** Logs can contain usernames, local file paths, server IPs, system details, and sometimes tokens. Review logs before posting them publicly.

When sharing logs:

- Upload the full file if possible.
- Do not paste only the final three lines unless asked.
- Remove private tokens, IPs, or personal info if present.
- Mention what you were doing when it crashed.

A crash report without steps is a corpse with no murder weapon. Interesting, but not enough.

---

## Bug Reports

Open an issue here:

- [GitHub Issues](../../issues)

Before reporting a bug, reproduce it on a clean install.

Reports involving extra mods, custom shaders, edited configs, or manually changed files may be closed unless the issue also happens on an unmodified Still Watching profile.

Do **not** report as a pack bug unless you tested on a clean install:

- Crashes after adding extra mods.
- Crashes after adding shaders.
- Crashes after editing configs.
- Crashes from a manually assembled mod list.
- Server crashes caused by client-only mods.
- Problems from unofficial downloads.

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
- Any extra mods, shaders, resource packs, or config changes you added yourself.

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

### Can I add extra mods?

Yes, but added mods are your responsibility. If the pack breaks after you add something, test again on a clean install before reporting it.

### Can I use shaders?

Yes, if your system can handle them. If performance collapses, lower settings or disable the shader. Beautiful fog at 8 FPS is just a slideshow with trauma.

### Can I play without headphones?

Yes, but headphones are strongly recommended. This pack uses sound for atmosphere and threat awareness.

### Is the GitHub repo the download source?

No. Use CurseForge for player downloads. The repository is for project documentation, source-side material, issue tracking, and licensing clarity.

### Should I manually install every mod?

No. Use the modpack install flow unless you have a specific reason and know what you are doing. Manual assembly is where compatibility goes to get stabbed in an alley.

### Which version should I install?

Install the latest release shown on the official CurseForge project page unless you need an older version for a server or world compatibility reason.

### Should I report bugs after modifying the pack?

Only after testing the same issue on a clean install. If the problem exists only after your extra mods, shaders, edited configs, or manual file changes, the bug is probably yours. Congratulations, you invented a problem.

---

## Documentation Roadmap

Planned improvements:

- Add screenshots for CurseForge search, project confirmation, install button, profile options, RAM allocation, My Modpacks, and server-pack file selection.
- Add release-specific notes when major pack updates change installation or server behavior.
- Add tested third-party launcher notes after actual verification.
- Add a known client-only mod list if server setup problems become common.

Screenshots are not decorative glitter. They reduce support chaos.

---

## Final Warning

Install cleanly. Allocate enough RAM. Use headphones. Back up your worlds. Read your logs. Do not trust random downloads.

Then step into the fog.

**Do not trust the quiet.**
