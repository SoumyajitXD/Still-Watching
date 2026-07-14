<!-- markdownlint-disable MD013 -->

# Contributing

Still Watching accepts useful work: reproducible reports, clean documentation, evidence-backed metadata fixes, validation improvements, and changes that make the modpack easier to install, maintain, support, or troubleshoot.

It does not need random noise wearing a pull request costume.

---

## Project Baseline

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
| Repository license | Apache-2.0 for original repository files only |

Install from CurseForge when testing playable behavior. The GitHub ZIP is repository source content, not the recommended playable installer.

---

## V2.0.0 Context

Contributions must account for the current V2.0.0 direction:

- Terralith and Tectonic drive Overworld generation.
- Incendium and Nullscape overhaul the Nether and End.
- Lithostitched supports the world-generation stack.
- Dungeons and Taverns, Explorify, and Towns and Towers provide structures.
- Xaero's Minimap and World Map replace JourneyMap.
- ImmediatelyFast, FerriteCore, ModernFix, FPS Reducer, Embeddium, and Chloride form the main optimization stack.
- The One Who Watches is part of the current horror roster.

Do not reintroduce removed V1.1.2 systems casually. A mod being popular is not a compatibility plan.

---

## License Scope

This repository is licensed under [Apache License 2.0](./LICENSE) for original project files. That includes project-maintained documentation, metadata, validation helpers, configuration source, and other original repository files unless a file says otherwise.

That does **not** relicense Minecraft, Forge, CurseForge, third-party mods, screenshots containing third-party content, trademarks, logos, mod names, shader packs, resource packs, sounds, textures, or external project content.

Do not submit files you do not have the right to contribute. Do not upload mod JARs, copied assets, private files, or unlicensed material.

---

## Useful Contributions

Good contributions usually include:

- documentation fixes for players, server admins, contributors, or maintainers;
- reproducible bug reports with logs and clean-install testing;
- V2.0.0 migration guidance backed by actual testing;
- world-generation compatibility notes backed by evidence;
- server-pack corrections backed by dedicated-server testing;
- mod metadata corrections backed by source or release evidence;
- broken-link, typo, table, and navigation fixes;
- validation or automation improvements;
- performance observations with hardware, settings, shader, and logs;
- missing credit, attribution, or license-scope corrections;
- presentation improvements that fit the pack's horror identity.

Useful work makes the project clearer. Useless work makes maintainers dig through fog with a spoon.

---

## Changes Usually Rejected

Do not open issues or pull requests for:

- installing from the GitHub ZIP and reporting that it is not a launcher-ready pack;
- unsupported launcher support;
- reuploaded modpack files or unofficial mirrors;
- random mod dumps with no design reason, dependency audit, or testing;
- reintroducing removed mods without a migration and compatibility case;
- server/client-side claims without evidence;
- crash screenshots without logs;
- vague reports such as `broken`, `fix`, or `doesn't work`;
- copyrighted assets, copied branding, bundled mod JARs, or content you cannot license;
- changes that flatten the pack's horror identity into generic modpack sludge;
- changes that remove credits, source-of-truth warnings, license notes, or sponsor content.

The pack has a theme. If a change does not serve that theme or maintenance reality, it is probably clutter.

---

## Before Opening an Issue

1. Install the latest release from CurseForge.
2. Launch with no extra mods, shaders, resource packs, or copied configs.
3. Confirm Minecraft `1.20.1`, Forge, and Java `17` where required.
4. Allocate `5 GB` minimum RAM; `6–8 GB` preferred.
5. Create a clean V2.0.0 test world.
6. Reproduce the issue.
7. Collect `logs/latest.log` and any crash report.
8. State whether the world is new or migrated from V1.1.2.

A bug report without logs is a campfire story with the stack trace missing.

---

## Pull Request Guidelines

Pull requests should be focused: one clear job per PR.

Good pull requests:

- explain what changed and why;
- link related issues when relevant;
- avoid unrelated rewrites;
- preserve the project tone and CurseForge source-of-truth warning;
- preserve Apache-2.0 wording and third-party license scope;
- preserve credits, attribution, mod names, links, and sponsor references;
- update all release-facing surfaces when changing version or mod metadata;
- include validation results.

Bad pull requests remodel the whole haunted house because one window squeaked.

---

## Documentation Style

Keep writing direct, specific, useful, honest about uncertainty, and clear about what is supported.

Avoid corporate filler, fake certainty, giant paragraphs, jokes that hide instructions, and vague claims such as `optimized`, `fixed`, or `compatible` without evidence.

Personality is seasoning. Accuracy is the meal. Do not serve a bowl of paprika.

---

## Mod Metadata and Server Changes

Changes involving mods, sides, dependencies, loaders, world generation, or server behavior need evidence.

1. Edit source metadata only with release evidence.
2. Keep cautious wording when proof is missing.
3. Do not call a mod server-safe because it looks client-only.
4. Preserve third-party names, links, credits, and permission notes.
5. Regenerate derived docs when source data changes.
6. Validate before committing.
7. Test V2.0.0 worldgen changes in new worlds and disposable migrated copies.
8. Test dedicated-server changes on a dedicated server or clearly mark them unverified.

---

## Validation

Run the maintained repository checks:

```bash
python3 .github/ci/validate_repository.py all
```

Run Markdown linting:

```bash
npx --yes markdownlint-cli2@0.18.1 "**/*.md" "!Releases/**"
```

Check whitespace:

```bash
git diff --check
```

If validation cannot be run, say so. Silence makes reviewers assume the fog was part of the test plan.

---

## Support

Read [`SUPPORT.md`](./SUPPORT.md) for installation help, troubleshooting boundaries, and evidence requirements.
