<!-- markdownlint-disable MD013 -->

# Security Policy

**Still Watching** is a Minecraft Java Edition horror-survival modpack. Most reports here will be gameplay bugs, mod conflicts, broken installs, bad configs, or cursed launcher behavior. Annoying, yes. Security vulnerabilities, usually no.

Security reports are for risks that could harm players, servers, maintainers, or the project's distribution chain.

---

## Official Release Source

Install playable releases from the official CurseForge project:

- [Still Watching on CurseForge](https://www.curseforge.com/minecraft/modpacks/still-watching)
- [Still Watching files](https://www.curseforge.com/minecraft/modpacks/still-watching/files)

Project baseline:

| Item | Value |
| --- | --- |
| Project | Still Watching |
| Minecraft | `1.20.1` |
| Loader | Forge |
| Java | Java `17` where required |
| CurseForge Project ID | `1420406` |
| Current documented release | Still Watching V1.1.2 |
| RAM | `5 GB` minimum; `6–8 GB` preferred |
| Repository license | Apache-2.0 for original repository files only |

The GitHub repository is for source-side project files, documentation, validation, issue tracking, screenshots, release metadata, and licensing clarity.

The GitHub ZIP is **not** a playable modpack installer. If someone tells players to install Still Watching from a random ZIP, mirror, reupload, shortened link, or mystery launcher, treat that as suspicious until proven otherwise.

---

## Supported Versions

| Source | Security support status |
| --- | --- |
| Latest CurseForge release | Primary support |
| Older CurseForge releases | Best-effort support |
| GitHub ZIP or source download | Not a supported playable install |
| Third-party reuploads, mirrors, or modified packs | Not supported |

Older releases may still get attention when the report is clear and useful, but the latest CurseForge release is the baseline.

---

## What Counts as a Security Concern

Open a GitHub issue if you find or suspect:

- fake Still Watching downloads, mirrors, installers, or launchers;
- tampered files pretending to be official releases;
- malicious links in issues, comments, documentation, release notes, or project pages;
- accidental exposure of secrets, tokens, passwords, private server addresses, credentials, or private files;
- project files that could mislead users into unsafe installation behavior;
- unsafe instructions that encourage unsupported redistribution or manual installation from untrusted sources;
- supply-chain concerns around release references, downloads, attribution, dependency metadata, or license scope.

Bring evidence: links, filenames, screenshots if useful, where you found the problem, and what made it suspicious.

---

## What Is Usually Not a Security Concern

These belong in normal support or bug channels:

- crashes;
- broken installs;
- missing dependencies;
- mod conflicts;
- low FPS, lag, or memory pressure;
- server startup failures;
- broken configs;
- horror mobs being unfair, loud, invisible, rude, or emotionally unemployed;
- issues caused by extra mods, shaders, resource packs, cracked launchers, or modified pack files.

If the issue only affects gameplay or stability, file it as a normal bug with logs and reproduction steps.

---

## Reporting Security Issues

For reports that are safe to discuss publicly, use GitHub Issues:

- [Open an issue](https://github.com/SoumyajitXD/Still-Watching/issues)

Do **not** publicly post secrets, tokens, passwords, private server IPs, private logs, credentials, or anything that would make the situation worse by being indexed forever.

If a report contains sensitive details, redact the sensitive parts before posting. A Discord server may be added later, but it is not an official support or security-reporting route until it is linked by the project.

---

## Before Posting Logs

Logs and crash reports can contain personal or server-specific details. Check before sharing:

- usernames;
- local file paths;
- server addresses;
- tokens or session-like strings;
- private modpack or server information;
- IP addresses or hostnames you do not want public.

Post the smallest useful log section that still proves the issue. Evidence is good. Doxxing yourself by accident is not character development.

---

## License Scope and Security

Original repository files are licensed under **Apache-2.0** through [`LICENSE`](./LICENSE). That does **not** relicense Minecraft, Forge, CurseForge, third-party mods, third-party assets, mod names, logos, screenshots containing third-party content, shaders, resource packs, sounds, textures, or external project content.

Security reports may include license-scope and redistribution risks when they affect user safety, official-source clarity, or project integrity. Examples include fake official downloads, bundled third-party files outside allowed channels, or pages implying that the GitHub ZIP is a supported installer.

---

## Maintainer Response

Reports will be reviewed as time allows. Valid security concerns may result in documentation fixes, warning notices, issue cleanup, link removal, release-reference corrections, license-scope clarifications, or other repository changes.

Reports without evidence may be closed. Panic is not a reproduction step.
