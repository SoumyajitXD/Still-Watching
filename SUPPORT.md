# Support

Need help with Still Watching? Start with the official install path, check the basics, then bring logs. Guesswork is for horror atmosphere, not troubleshooting.

---

## Official Support Baseline

| Item | Value |
| --- | --- |
| Project | Still Watching |
| Minecraft | `1.20.1` |
| Loader | Forge |
| Java | Java 17 where required |
| Official playable release | CurseForge |
| CurseForge Project ID | `1420406` |
| Current documented release | Still Watching V1.1.0 |
| RAM | `5 GB` minimum; `6–8 GB` preferred |
| Latest release | Primary support |
| Older releases | Best-effort support |

Install playable releases from CurseForge:

- [Still Watching on CurseForge](https://www.curseforge.com/minecraft/modpacks/still-watching)
- [Still Watching files](https://www.curseforge.com/minecraft/modpacks/still-watching/files)
- [Installation guide](./installation-guide.md)

The GitHub ZIP is **not** a playable installer. It is repository source content. If you install from the GitHub ZIP and it breaks, the problem is already identified.

---

## Where to Get Help

Use GitHub Issues for reproducible project problems:

- [Open an issue](https://github.com/SoumyajitXD/Still-Watching/issues)

Use CurseForge for official playable files and release downloads:

- [CurseForge project page](https://www.curseforge.com/minecraft/modpacks/still-watching)

A Discord server is planned, but it is not available yet. Until an official Discord link appears in the repository or project page, do not trust random “support server” links pretending to be official.

---

## What GitHub Issues Are For

Open an issue for:

- reproducible crashes on the official CurseForge release;
- dedicated-server or multiplayer setup failures with logs;
- documentation errors;
- broken links;
- mod metadata mistakes;
- server-pack problems;
- compatibility reports with clear testing details;
- suspicious downloads, fake links, or unsafe public references;
- attribution, credit, or license-reference problems.

A good issue gives maintainers enough evidence to act. A bad issue just screams “it broke” into the cave and waits for Java to confess.

---

## What GitHub Issues Are Not For

Do not open issues for:

- general Minecraft modding lessons;
- cracked-launcher support;
- unofficial reuploads or modified packs;
- installs made from the GitHub ZIP;
- extra mods, shaders, resource packs, or configs unless the issue also happens on a clean CurseForge install;
- low FPS reports without hardware/settings/log details;
- crash screenshots with no log or crash report;
- “add this mod” requests with no design reason or testing;
- vague reports like “fix,” “broken,” “lag,” or “doesn’t work.”

Those are not support requests. Those are fog noises with a keyboard.

---

## Before Asking for Help

Do this first:

1. Install the latest Still Watching release from CurseForge.
2. Launch once with no extra mods, shaders, or resource packs.
3. Confirm Minecraft `1.20.1`.
4. Confirm the correct Forge environment.
5. Use Java 17 if the launcher or server requires it.
6. Allocate `5 GB` minimum RAM; `6–8 GB` preferred.
7. Reproduce the issue.
8. Collect `logs/latest.log` and any crash report.
9. Note whether the issue happens in singleplayer, multiplayer, client, or dedicated server.

Skipping these steps usually creates a support thread that dies face-down in the swamp.

---

## What to Include in a Help Request

Include:

- Still Watching version;
- where you installed it from;
- launcher used;
- operating system;
- singleplayer or multiplayer;
- client or dedicated server;
- Java version, if relevant;
- RAM allocated;
- steps to reproduce;
- what you expected to happen;
- what actually happened;
- `logs/latest.log`;
- crash report, if one exists;
- whether you added extra mods, shaders, resource packs, or config edits;
- whether it happens on a clean CurseForge install.

If you are reporting a server issue, also include:

- server host or local server type, if relevant;
- server RAM;
- whether the server uses the official server-pack instructions;
- server log;
- whether all clients are on the same pack version.

---

## Logs and Privacy

Logs can contain private details. Before posting, check for:

- usernames;
- local file paths;
- IP addresses;
- server hostnames;
- tokens or secret-looking strings;
- private server information.

Attach logs or use a paste service when they are long. Do not paste a wall of log sludge directly into the issue body unless it is short and relevant.

---

## Latest vs Older Versions

The latest CurseForge release gets primary support.

Older versions may receive best-effort help, especially for documentation, migration, or known issues. But if the problem is already fixed in a newer release, update first. Maintaining old ghosts forever is not support; it is necromancy with version numbers.

---

## Security or Suspicious Downloads

For fake downloads, suspicious links, unsafe public references, or possible exposure of private data, read [`SECURITY.md`](./SECURITY.md).

Do not post secrets or sensitive private details publicly.

---

## Contributing Fixes

If you want to fix docs, metadata, validation, or support information, read [`CONTRIBUTING.md`](./CONTRIBUTING.md).
