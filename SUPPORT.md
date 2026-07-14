<!-- markdownlint-disable MD013 -->

# Support

Need help with **Still Watching**? Start from the official install path, reproduce on a clean profile, then bring logs. Guesswork belongs in the atmosphere, not in support threads.

---

## Support Baseline

| Item | Value |
| --- | --- |
| Project | Still Watching |
| Type | Minecraft Java Edition horror-survival modpack |
| Minecraft | `1.20.1` |
| Loader | Forge |
| Java | Java `17` where required |
| Official playable release | CurseForge |
| CurseForge Project ID | `1420406` |
| Current documented release | Still Watching V2.0.0 |
| RAM | `5 GB` minimum; `6–8 GB` preferred |
| Latest CurseForge release | Primary support target |
| Older releases | Best-effort support |
| GitHub ZIP | Not the recommended playable install source |

Install playable releases from CurseForge:

- [Still Watching on CurseForge](https://www.curseforge.com/minecraft/modpacks/still-watching)
- [Still Watching files](https://www.curseforge.com/minecraft/modpacks/still-watching/files)
- [Installation guide](./installation-guide.md)

---

## V2.0.0 Migration Support

V2.0.0 changes the Overworld, Nether, End, structure set, map system, and optimization stack.

Before reporting an update problem:

1. Back up the V1.1.2 instance and world.
2. Install V2.0.0 as a fresh CurseForge profile.
3. Test a newly created V2.0.0 world.
4. Do not copy the entire old `config/` folder over the new release.
5. Test migrated worlds only from disposable copies.
6. Remember that JourneyMap data does not automatically transfer to Xaero's maps.

Terrain seams and different generation in unexplored chunks are expected consequences of migrating a world across a major generator overhaul. That is not a bug the support team can erase with motivational speaking.

---

## Where to Get Help

Use GitHub Issues for reproducible project problems:

- [Open an issue](https://github.com/SoumyajitXD/Still-Watching/issues)

Use CurseForge for official playable files and downloads:

- [CurseForge project page](https://www.curseforge.com/minecraft/modpacks/still-watching)

Do not trust random support-server links, mirrors, or modified downloads pretending to be official.

---

## Supported Help

Open an issue for:

- reproducible crashes on the official CurseForge release;
- broken installation or migration instructions;
- world-generation failures on a clean V2.0.0 profile;
- dedicated-server or multiplayer failures with logs;
- server-pack documentation problems;
- broken links or incorrect project metadata;
- wrong mod-list information;
- compatibility reports backed by clear testing details;
- suspicious downloads or unsafe public references;
- attribution, credit, or license-scope problems.

Good support requests provide enough evidence to act. Bad requests just scream into the cave and wait for Java to confess.

---

## Unsupported Help

Do not open support issues for:

- cracked launchers;
- unofficial reuploads, mirrors, or modified packs;
- installs assembled from the GitHub ZIP;
- random extra mods, shaders, resource packs, or config edits unless the issue also happens clean;
- expected terrain borders after migrating a V1.1.2 world;
- requests to convert JourneyMap data into Xaero's map data;
- low-FPS reports without hardware, settings, shader, and log details;
- crash screenshots without logs;
- vague reports such as `fix`, `broken`, `lag`, or `doesn't work`.

Those are not actionable support requests. They are fog noises with a keyboard.

---

## Before Asking for Help

1. Install the latest release from CurseForge.
2. Launch with no extra mods, shaders, resource packs, or copied configs.
3. Confirm Minecraft `1.20.1` and the correct Forge environment.
4. Use Java `17` if required.
5. Allocate `5 GB` minimum RAM; `6–8 GB` preferred.
6. Create a clean test world.
7. Reproduce the issue.
8. Collect `logs/latest.log` and any crash report.
9. Record whether the issue affects a new V2.0.0 world or a migrated world.

Skipping these steps usually creates a support thread that dies face-down in the swamp.

---

## What to Include

Include:

- Still Watching version;
- installation source and launcher;
- operating system;
- Minecraft, Forge, and Java versions;
- RAM allocation;
- singleplayer, multiplayer, client, or dedicated server;
- new world or migrated world;
- exact reproduction steps;
- expected and actual behavior;
- `logs/latest.log` and crash report;
- shader name and graphics settings for performance reports;
- any extra mods, resource packs, or config edits;
- whether the issue reproduces on a clean CurseForge profile.

For server issues, also include server RAM, host or local-server type, setup method, server log, and whether all clients match the exact release.

---

## Logs and Privacy

Before posting logs, check for usernames, local paths, IP addresses, server hostnames, tokens, credentials, and private server information.

Attach long logs or use a paste service. Do not paste a wall of log sludge into the issue body unless the excerpt is short and directly relevant.

---

## Latest Versus Older Versions

The latest CurseForge release gets primary support. Older releases receive best-effort help for documentation, migration, and known issues.

If a problem is already fixed in a newer release, update first. Maintaining old ghosts forever is not support; it is necromancy with version numbers.

---

## Security and Redistribution

For fake downloads, suspicious links, exposed secrets, or private-data leaks, read [`SECURITY.md`](./SECURITY.md).

Original repository files are Apache-2.0 licensed. That does not relicense Minecraft, Forge, third-party mods, shaders, resource packs, sounds, textures, logos, or external assets.
