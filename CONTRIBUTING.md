# Contributing

Still Watching accepts useful work: fixes, evidence, clean documentation, reproducible bug reports, and changes that make the modpack easier to install, maintain, validate, or troubleshoot.

It does not need random noise wearing a pull request costume.

---

## Project Baseline

| Item | Value |
| --- | --- |
| Project | Still Watching |
| Type | Minecraft Java Edition horror-survival modpack |
| Minecraft | `1.20.1` |
| Loader | Forge |
| Java | Java 17 where required |
| Official playable release | CurseForge |
| CurseForge Project ID | `1420406` |
| Current documented release | Still Watching V1.1.1 |
| RAM | `5 GB` minimum; `6–8 GB` preferred |
| Repository license | Apache-2.0 for original repository files only |

Install from CurseForge when testing playable behavior. The GitHub ZIP is repository source content, not a playable modpack installer.

---

## License Scope

This repository is licensed under the [Apache License 2.0](./LICENSE) for original repository files created for Still Watching, such as documentation, metadata, scripts, configuration source, validation helpers, and other project-maintained files unless a file clearly says otherwise.

That does **not** relicense Minecraft, Forge, CurseForge, third-party mods, third-party assets, screenshots containing third-party content, trademarks, logos, mod names, or external project content. Those stay under their own owners' licenses, terms, and permissions.

Do not submit files you do not have the right to contribute. Do not upload mod JARs, copied assets, ripped textures, stolen logos, private files, or anything that would make licensing a dumpster fire with a README.

---

## Contribution License

By opening a pull request or otherwise contributing original content to this repository, you agree that your contribution may be used, modified, reproduced, and distributed under the repository's Apache-2.0 license unless you clearly mark a different compatible license and the maintainer accepts it.

Contributions must be your own work, public-domain material, or material you are allowed to submit under compatible terms. If attribution is required, include it clearly in the relevant file or PR description.

This is not legal advice. It is the project rule: do not bring licensing grenades into the modpack.

---

## What Contributions Help

Good contributions usually fall into one of these buckets:

- documentation fixes for players, server admins, contributors, or maintainers;
- reproducible bug reports with logs and clean-install testing;
- server-pack corrections backed by actual dedicated-server testing;
- mod metadata corrections backed by source/release evidence;
- broken link fixes;
- typo, formatting, table, and navigation improvements;
- validation or automation improvements;
- compatibility notes for the documented release;
- performance observations with hardware, settings, and logs;
- screenshots or presentation improvements that fit the pack’s identity.

Useful work makes the project clearer. Useless work makes maintainers dig through fog with a spoon.

---

## What Will Usually Be Rejected

Do not open issues or pull requests for:

- installing from the GitHub ZIP and then reporting that it does not work;
- cracked-launcher support;
- reuploaded modpack files or unofficial mirrors;
- random mod dumps with no design reason or testing;
- adding horror mobs just because they exist;
- server/client-side claims without evidence;
- crash screenshots without logs;
- vague reports like “broken,” “fix,” or “doesn’t work”;
- copyrighted assets, copied branding, stolen files, bundled mod JARs, or content you cannot license to this repository;
- changes that strip the pack’s horror identity into bland generic modpack sludge;
- changes that remove required credits, attribution, licensing notes, or sponsor-related content.

The pack has a theme. If a change does not serve that theme or maintenance reality, it is probably clutter.

---

## Before Opening an Issue

Check the basics first:

1. Install the latest release from CurseForge.
2. Launch once with no extra mods, shaders, or resource packs.
3. Confirm Minecraft `1.20.1` and the correct Forge environment.
4. Use Java 17 if the launcher/server asks.
5. Allocate enough RAM: `5 GB` minimum, `6–8 GB` preferred.
6. Reproduce the issue.
7. Collect `logs/latest.log` and any crash report.

A bug report without logs is not a report. It is a campfire story with stack traces missing.

---

## Bug Report Checklist

When reporting a bug, include:

- Still Watching version;
- whether it came from CurseForge;
- singleplayer or multiplayer;
- client or dedicated server;
- operating system;
- Java version, if relevant;
- steps to reproduce;
- expected behavior;
- actual behavior;
- logs and crash reports;
- whether the issue happens on a clean CurseForge install;
- any extra mods, shaders, resource packs, or config edits.

Do not paste giant logs directly into the issue body unless they are short. Use attachments or a paste service when needed, and remove secrets/private details first.

---

## Pull Request Guidelines

Pull requests should be focused. One clear job per PR.

Good PRs:

- explain what changed and why;
- link related issues when relevant;
- avoid unrelated rewrites;
- preserve the existing project tone;
- keep tables and docs readable;
- include validation results when the change touches generated or release-facing files;
- preserve license notices, attribution, credits, and third-party references.

Bad PRs try to remodel the whole haunted house because one window squeaked.

---

## Documentation Style

Keep the writing:

- direct;
- specific;
- useful;
- horror-flavored where it fits;
- honest about uncertainty.

Avoid:

- corporate filler;
- fake certainty;
- giant paragraphs nobody will read;
- jokes that hide important instructions;
- vague claims like “optimized,” “fixed,” or “compatible” without proof.

Personality is seasoning. Accuracy is the meal. Do not serve a bowl of paprika.

---

## Mod Metadata and Server-Pack Changes

Changes involving mods, sides, dependencies, loaders, or server-pack behavior need evidence.

Rules:

1. Edit source metadata only when you have real release evidence.
2. Keep `unknown`, `verify`, or cautious wording when proof is missing.
3. Do not call a mod server-safe because it “looks client-only.” That is how servers become smoke.
4. Preserve third-party mod names, links, credits, and license/permission notes.
5. Regenerate derived docs when source data changes.
6. Validate before committing.

If a change affects dedicated servers, test it on a dedicated server or clearly say it still needs testing.

---

## Validation

Before committing release-facing documentation, metadata, workflow, or link changes, run the same maintained checks CI uses. The old helper scripts are gone on purpose; maintained validation lives under `.github/ci/` so contributors do not chase dead ghosts.

```bash
python3 .github/ci/validate_repository.py all
```

Run Markdown linting before touching tables, headings, fenced blocks, or README navigation:

```bash
npx --yes markdownlint-cli2@0.18.1 "**/*.md" "!Releases/**"
```

If your change touches links, run the link check. It verifies internal links and probes external links with soft warnings for rate-limited CurseForge-style hosts:

```bash
python3 .github/ci/validate_repository.py links --external-links
```

Always check for whitespace errors before committing:

```bash
git diff --check
```

If you cannot run validation, say so in the PR or issue. Silence makes reviewers assume you skipped it and hoped the fog would cover the body.

---

## Security Reports

Do not post secrets, tokens, private server addresses, or sensitive logs publicly.

Use normal GitHub Issues only for non-sensitive security concerns, suspicious public links, fake downloads, or unsafe public references. See [`SECURITY.md`](./SECURITY.md) before reporting security-related issues.

---

## Support

For installation help, troubleshooting, and where to ask questions, read [`SUPPORT.md`](./SUPPORT.md).

A Discord server may be added later. Until it exists and is officially linked, GitHub and CurseForge are the project’s public support path.