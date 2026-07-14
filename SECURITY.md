<!-- markdownlint-disable MD013 -->

# Security Policy

**Still Watching** is a Minecraft Java Edition horror-survival modpack. Most reports are gameplay bugs, mod conflicts, broken installs, bad configs, or cursed launcher behavior. Annoying, yes. Security vulnerabilities, usually no.

Security reports are for risks that could harm players, servers, maintainers, or the project's distribution chain.

---

## Official Release Source

Install playable releases from the official CurseForge project:

- [Still Watching on CurseForge](https://www.curseforge.com/minecraft/modpacks/still-watching)
- [Still Watching files](https://www.curseforge.com/minecraft/modpacks/still-watching/files)

| Item | Value |
| --- | --- |
| Project | Still Watching |
| Minecraft | `1.20.1` |
| Loader | Forge |
| Java | Java `17` where required |
| CurseForge Project ID | `1420406` |
| Current documented release | Still Watching V2.0.0 |
| RAM | `5 GB` minimum; `6–8 GB` preferred |
| Repository license | Apache-2.0 for original repository files only |

The GitHub repository contains documentation, validation, screenshots, release metadata, and issue tracking. The GitHub ZIP is **not** the recommended playable installer and is not an official server pack.

If someone tells players to install Still Watching from a random ZIP, mirror, reupload, shortened link, or mystery launcher, treat that as suspicious until proven otherwise.

---

## Supported Versions

| Source | Security support status |
| --- | --- |
| Latest CurseForge release | Primary support |
| Older CurseForge releases | Best-effort support |
| GitHub ZIP or source download | Not a supported playable install |
| Third-party reuploads, mirrors, or modified packs | Not supported |

V2.0.0 is the current documentation baseline. Older releases may still receive attention when a report is clear and useful.

---

## What Counts as a Security Concern

Open an issue when safe to do so if you find or suspect:

- fake Still Watching downloads, mirrors, installers, or launchers;
- tampered files pretending to be official releases;
- malicious links in issues, comments, documentation, or release notes;
- accidental exposure of secrets, tokens, passwords, private server addresses, credentials, or private files;
- project files that mislead users into unsafe installation behavior;
- unsafe instructions encouraging unsupported redistribution or untrusted downloads;
- supply-chain concerns around release references, attribution, dependency metadata, or license scope;
- a release archive that contains unexpected executables, scripts, or files unrelated to the documented modpack.

Bring evidence: links, filenames, hashes when available, screenshots when useful, and where the suspicious item was found.

---

## What Is Usually Not a Security Concern

These belong in normal support or bug channels:

- crashes or broken installs;
- missing dependencies and mod conflicts;
- low FPS, lag, or memory pressure;
- server startup failures;
- broken configs;
- expected terrain seams after migrating an old world to V2.0.0;
- JourneyMap data not transferring to Xaero's maps;
- horror mobs being unfair, loud, invisible, rude, or emotionally unemployed;
- issues caused by extra mods, shaders, resource packs, cracked launchers, or modified pack files.

If the issue only affects gameplay or stability, file it as a normal bug with logs and reproduction steps.

---

## Reporting Security Issues

For reports safe to discuss publicly, use [GitHub Issues](https://github.com/SoumyajitXD/Still-Watching/issues).

Do **not** publicly post secrets, tokens, passwords, private server IPs, private logs, credentials, or anything that would make the situation worse by being indexed forever.

Redact sensitive details before posting. Publicly leaking the evidence while reporting the leak is a remarkably efficient way to double the problem.

---

## Before Posting Logs

Logs and crash reports can contain:

- usernames;
- local file paths;
- server addresses;
- tokens or session-like strings;
- private modpack or server information;
- IP addresses or hostnames.

Post the smallest useful log section that still proves the issue. Evidence is good. Doxxing yourself by accident is not character development.

---

## Release Archive Safety

The repository may contain release-side exported material under `Releases/`. CurseForge remains the official playable release source.

Before trusting any archive:

1. Confirm the repository owner is `SoumyajitXD`.
2. Confirm the project is Still Watching and CurseForge Project ID is `1420406`.
3. Compare the documented release version and contents.
4. Treat unexpected executables, launchers, credential requests, or unrelated scripts as suspicious.
5. Prefer downloading the playable pack through CurseForge.

---

## License Scope

Original repository files are licensed under **Apache-2.0** through [`LICENSE`](./LICENSE). That does not relicense Minecraft, Forge, CurseForge, third-party mods, screenshots containing third-party content, shaders, resource packs, sounds, textures, logos, or external project content.

Security reports may include license-scope and redistribution risks when they affect user safety, official-source clarity, or project integrity.

---

## Maintainer Response

Valid security concerns may result in documentation fixes, warning notices, issue cleanup, link removal, release-reference corrections, license clarifications, or other repository changes.

Reports without evidence may be closed. Panic is not a reproduction step.
