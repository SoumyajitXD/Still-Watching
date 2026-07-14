<!-- markdownlint-disable MD013 -->

# Changelog

This changelog tracks public-facing releases and repository documentation for **Still Watching**.

Playable files live on CurseForge. If this file and CurseForge disagree about a downloadable release, trust CurseForge first and open an issue with evidence.

---

## Current Documented Release

| Field | Value |
| --- | --- |
| Project | Still Watching |
| Current documented release | Still Watching V2.0.0 |
| Minecraft | `1.20.1` |
| Loader | Forge |
| Java | Java `17` where required |
| CurseForge Project ID | `1420406` |
| RAM | `5 GB` minimum; `6–8 GB` preferred |
| Documented content entries | 80 mods, libraries, shaders, and resource packs |
| Official playable release source | [CurseForge](https://www.curseforge.com/minecraft/modpacks/still-watching/files) |
| Repository license | Apache-2.0 for original repository files only |

---

## Still Watching V2.0.0

Still Watching V2.0.0 is a major content, world-generation, exploration, mapping, and performance overhaul. It replaces several V1.1.2 systems instead of piling more mods onto the same foundation and hoping the loading screen forgives us.

### Highlights

- Rebuilt the Overworld around **Terralith** and **Tectonic**.
- Added **Incendium** for expanded Nether generation.
- Added **Nullscape** for overhauled End generation.
- Added **Lithostitched** for world-generation integration and compatibility.
- Added **Dungeons and Taverns** to expand structure variety.
- Added **The One Who Watches** to the horror roster.
- Replaced JourneyMap with **Xaero's Minimap** and **Xaero's World Map**.
- Added **ImmediatelyFast**, **FerriteCore**, **ModernFix**, and **FPS Reducer**.
- Added **TACZ: Durability** for expanded Timeless and Classics Zero weapon progression.
- Removed outdated, replaced, or no-longer-required content and dependencies.
- Regenerated and retuned configuration files for the new V2.0.0 mod set.

### World-Generation Overhaul

V2.0.0 replaces the previous Biomes O' Plenty-centered setup with a more focused terrain and dimension stack:

- **Terralith** expands Overworld biomes and terrain using vanilla-style blocks.
- **Tectonic** creates larger-scale mountains, valleys, and terrain formations.
- **Incendium** expands Nether terrain and exploration.
- **Nullscape** rebuilds the End around larger and more varied void landscapes.
- **Lithostitched** supports the updated world-generation stack.
- **Dungeons and Taverns**, **Explorify**, and **Towns and Towers** provide the main structure layer.

A new world is strongly recommended. Existing worlds can develop hard terrain borders, inconsistent biome transitions, changed dimension generation, removed-mod remnants, and new structures appearing only in unexplored chunks.

### Expanded Horror

**The One Who Watches** joins the existing horror lineup, which continues to include:

- The Anomaly
- The Man From The Fog
- From The Fog
- Cave Dweller Reimagined
- The Knocker
- The Midnight Lurker
- The Mimicer
- Siren Head: The Arrival
- GoatMan
- Apollyon
- Eyes in the Darkness

The goal is not merely a larger monster count. V2.0.0 combines stalking entities, environmental tension, sound design, visual pressure, world scale, and unpredictable encounters into a more cohesive horror loop.

### Performance and Memory

Added a dedicated optimization layer:

- **ImmediatelyFast** reduces overhead in several rendering and interface paths.
- **FerriteCore** reduces memory usage.
- **ModernFix** provides broad loading, memory, stability, and performance improvements.
- **FPS Reducer** lowers unnecessary resource usage while Minecraft is inactive or running in the background.

These additions complement **Embeddium**, **Chloride**, and **Oculus**. Actual performance still depends heavily on hardware, render distance, simulation distance, shaders, entities, and active world generation. A heavy shader at heroic settings can still turn expensive hardware into a haunted PowerPoint.

### Mapping Changes

- Removed **JourneyMap**.
- Added **Xaero's Minimap**.
- Added **Xaero's World Map**.

JourneyMap waypoints and map data do not automatically transfer to Xaero's mapping system. Back up the old `journeymap/` folder before removing a V1.1.2 instance if that data matters.

### TaCZ Changes

Added **TACZ: Durability** for **Timeless and Classics Zero Guns**, introducing an additional durability and maintenance layer for weapons.

### Added

The following entries are new in V2.0.0:

- Dungeons and Taverns
- FPS Reducer
- FerriteCore
- ImmediatelyFast
- Incendium
- Lithostitched
- ModernFix
- Nullscape
- TACZ: Durability
- Tectonic
- Terralith
- The One Who Watches
- Xaero's Minimap
- Xaero's World Map

### Removed

The following entries from V1.1.2 were removed:

- Biomes O' Plenty
- Carry On
- Dungeons Enhanced
- GlitchCore
- JourneyMap
- Structure Gel API
- The End of Herobrine
- Valhelsia Structures

Some removals were direct replacements. Others were dependencies or content that no longer matched the direction of the rebuilt pack.

### Updating from V1.1.2

For the cleanest upgrade:

1. Back up the old instance and all important worlds.
2. Install V2.0.0 as a fresh CurseForge profile when possible.
3. Do not copy the complete V1.1.2 configuration folder over V2.0.0.
4. Create a new world for the intended world-generation experience.
5. Reconfigure personal keybinds, shaders, voice chat, and graphics settings.
6. Keep JourneyMap data separately if old waypoints or map tiles matter.
7. Test disposable copies before loading irreplaceable worlds or servers.

### Repository Updates

- Updated the GitHub landing page for V2.0.0.
- Replaced the V1.1.2 modlist with the complete V2.0.0 list.
- Updated installation, server, support, security, contribution, and CI documentation.
- Updated CurseForge-description source content.
- Updated machine-readable release metadata.
- Added explicit migration warnings for the world-generation and map-system changes.

---

## V1.1.2

V1.1.2 was the previous documented release and the last release before the V2.0.0 world-generation, mapping, performance, and content overhaul.

Players keeping V1.1.2 worlds should preserve backups before testing V2.0.0. Older releases receive best-effort support; V2.0.0 is the current documentation baseline.

---

## Release History Source of Truth

Use these pages for playable releases and downloads:

- [Still Watching on CurseForge](https://www.curseforge.com/minecraft/modpacks/still-watching)
- [Still Watching files on CurseForge](https://www.curseforge.com/minecraft/modpacks/still-watching/files)

Use this repository for docs, screenshots, validation, issue tracking, support policy, server-pack guidance, release metadata, and licensing clarity.
