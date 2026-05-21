# Still Watching Repository Quality Audit

Audit date: 2026-05-21
Repository: `SoumyajitXD/Still-Watching`
Scope requested: `README.md`, `installation-guide.md`, `latest-modlist.md`, `curseforge-description.html`, `.github/workflows/ci.yml`, `.github/scripts/validate.py`, `.github/ISSUE_TEMPLATE/`, `Releases/`, and `Screenshots/`.

## Ground rules used for this audit

- **Verified facts** are based on files inspected in the repository during this audit.
- **Guesses / needs confirmation** are explicitly marked. No fake claims are made about CurseForge release ZIP contents.
- CurseForge remains the official playable install source. GitHub remains documentation, issue tracking, screenshots, release-side files, validation, and licensing clarity.
- Do **not** remove or weaken required sponsor content. Sponsor blocks should only be touched when validation requires it.
- Preserve the horror tone. The docs currently have teeth; do not replace them with corporate oatmeal.

---

## Critical fixes

### 1. Hard-coded `V1.0.9` in `curseforge-description.html` is a stale-release trap

**Verified fact:** `curseforge-description.html` hard-codes `Still Watching V1.0.9` in multiple places:

- `Current release: Still Watching V1.0.9`
- quick facts table: `Latest Version: V1.0.9`
- install step: `Install or update to Still Watching V1.0.9`
- issue-reporting bullet: `Modpack version, for example Still Watching V1.0.9`

**Risk:** The moment CurseForge gets a newer file, the CurseForge description source becomes stale unless manually updated. This is exactly how docs rot: one release walks in, version strings start lying, and players get sent into the fog with bad coordinates.

**Files affected:**

- `curseforge-description.html`
- `.github/scripts/validate.py`
- `.github/workflows/ci.yml`

**Exact suggested changes:**

Replace hard-coded latest-version wording with source-of-truth wording unless the release process guarantees automatic updates.

Recommended replacements:

```html
<strong style="color: #fa1d04;">Current release:</strong> Use the latest file on CurseForge. Update through CurseForge, back up your worlds, and keep multiplayer clients and servers on matching versions.
```

```html
<td style="border: 1px solid rgba(255,255,255,0.07);">Use the latest CurseForge file unless your server/world requires a specific version.</td>
```

```html
<li>Install or update to the latest <strong style="color: #fff;">Still Watching</strong> file on CurseForge.</li>
```

```html
<li>Modpack version, for example the exact Still Watching CurseForge file/version shown by your launcher</li>
```

Then add a validator check that fails if `curseforge-description.html` contains a hard-coded latest release pattern like:

```python
r"\b(Current release|Latest Version)\b[\s\S]{0,120}\bV\d+\.\d+\.\d+\b"
```

Do **not** make the validator fail on example placeholders like `V1.0.x` in issue templates. Those are examples, not claims.

---

### 2. `latest-modlist.md` is named “latest” but has no release metadata

**Verified fact:** `latest-modlist.md` contains 64 numbered CurseForge links and categories, but no header stating which CurseForge file/version/date it was verified against.

**Risk:** The file can be structurally valid while still being semantically stale. CI can prove the links look like CurseForge links. It cannot prove the list matches the actual latest CurseForge release unless metadata or manifest validation exists.

**Files affected:**

- `latest-modlist.md`
- `.github/scripts/validate.py`
- `.github/workflows/ci.yml`

**Exact suggested changes:**

Add a metadata block immediately under the title:

```md
# Latest Modlist

> Verified against: **manual check required**
> CurseForge release/file: **fill with exact CurseForge file name or file ID**
> Last verified: **YYYY-MM-DD**
>
> This repository list is documentation. CurseForge is the source of truth for playable release files.
```

Then add a validation rule requiring these labels to exist:

- `Verified against:`
- `CurseForge release/file:`
- `Last verified:`
- `CurseForge is the source of truth`

This does **not** claim anything about release ZIP contents. It forces the maintainer to admit what was checked, instead of letting “latest” cosplay as evidence.

---

### 3. External links are not actually checked

**Verified fact:** `validate.py` validates modlist URLs by pattern only. It checks scheme/domain/path shape, duplicate links, and continuous numbering. It does not perform HTTP status checks or verify that linked CurseForge pages exist.

**Risk:** A typo can pass CI if it merely looks like a CurseForge URL. That is link-shaped garbage wearing a badge.

**Files affected:**

- `.github/scripts/validate.py`
- `.github/workflows/ci.yml`
- `README.md`
- `installation-guide.md`
- `latest-modlist.md`
- `curseforge-description.html`

**Exact suggested changes:**

Add an optional `links` check that verifies HTTP status for external links, with timeout and retry limits:

```bash
python .github/scripts/validate.py links
```

Rules:

- Check Markdown links in `.md` files.
- Check `href` and `src` URLs in `curseforge-description.html`.
- Allow sponsor shortlink `https://url-shortener.curseforge.com/AZDOs` without expanding or rewriting it.
- Treat `429`, temporary network failures, and Cloudflare-ish failures as warnings, not hard failures.
- Treat obvious `404`/`410` as failures.

Also add internal relative-link validation for:

- `./README.md`
- `./installation-guide.md`
- `./latest-modlist.md`
- `./Screenshots`
- `./Releases`
- `../../issues`
- headings such as `#multiplayer--server-setup`

---

### 4. Release ZIP audit is too shallow for modpack-specific safety

**Verified fact:** `release_zips()` currently checks only that ZIP archives are readable, non-empty, and that `overrides/` does not exist without `manifest.json`.

**Risk:** A release-side ZIP can pass while still being useless or misleading. It might have a malformed manifest, wrong Minecraft version, wrong mod loader, junk top-level nesting, or missing basic CurseForge-export structure.

**Files affected:**

- `.github/scripts/validate.py`
- `.github/workflows/ci.yml`
- `Releases/`

**Exact suggested changes:**

Extend `release_zips()` only for repository release-side archives, without pretending to know CurseForge’s current playable files.

Suggested validations when `manifest.json` exists:

- JSON parses successfully.
- `minecraft.version == "1.20.1"`.
- `manifestType` is present.
- `manifestVersion` is present.
- `name` contains `Still Watching`.
- `files` exists and is a list when this is a CurseForge-style manifest.
- `overrides/` path does not contain obvious secrets or garbage: `.git/`, `.env`, `token`, `cache`, `logs/`, `crash-reports/`, `saves/`, `journeymap/`.

Suggested validations when `manifest.json` does **not** exist:

- Do not fail automatically unless the repository policy says every ZIP must be a CurseForge export.
- Print a warning: `ZIP has no manifest.json; treating as release-side auxiliary archive, not a playable CurseForge modpack export.`

This keeps the audit honest. No fake assumptions about CurseForge release files. No “I divine server pack truth from vibes” nonsense.

---

## High-value improvements

### 5. Project-fact validation checks presence, not consistency

**Verified fact:** `project_facts()` checks that README, installation guide, and CurseForge description mention `Still Watching`, `1.20.1`, `Forge`, `Java 17`, `CurseForge`, and project ID `1420406`.

**Gap:** It does not ensure the RAM recommendation is consistent, that all docs point to the same install source, or that no file says GitHub ZIP is playable.

**Files affected:**

- `.github/scripts/validate.py`
- `README.md`
- `installation-guide.md`
- `curseforge-description.html`

**Exact suggested changes:**

Add consistency checks for these canonical strings:

```python
CANONICAL = {
    "minecraft": "1.20.1",
    "loader": "Forge",
    "java": "Java 17",
    "ram_min": "5 GB",
    "ram_preferred": "6–8 GB",
    "curseforge_project_id": "1420406",
}
```

Also fail if any public doc contains unsafe install wording such as:

```text
install from GitHub
GitHub ZIP playable
GitHub ZIP installer
```

Allow only negated warnings like `GitHub ZIP is not a playable modpack installer`.

---

### 6. CurseForge HTML validation is only smoke-level parsing

**Verified fact:** `html()` feeds HTML files to Python’s `HTMLParser`, which catches very little. `HTMLParser` is forgiving and will not guarantee CurseForge-safe output.

**Risk:** Broken tags, missing image `alt`, invalid sponsor image dimensions, missing required links, and style regressions can slip through.

**Files affected:**

- `curseforge-description.html`
- `.github/scripts/validate.py`

**Exact suggested changes:**

Add a dedicated `curseforge_html()` validation check:

- Required links:
  - CurseForge project page
  - GitHub issues
  - installation guide
- Required phrases:
  - `Still Watching`
  - `Forge`
  - `1.20.1`
  - `CurseForge`
  - `GitHub ZIP is not` or an equivalent warning if added later
- Required sponsor URL/image if sponsor content is required in the CurseForge description too.
- Count `<img` tags and warn if `alt=""` is used on meaningful screenshots.
- Fail on hard-coded stale latest-version claims unless intentionally allowed.

Do **not** rewrite the whole HTML into sterile product-copy sludge. The current page has a clear horror identity. Guard it; do not embalm it.

---

### 7. Sponsor guard protects README only

**Verified fact:** `sponsor_guard()` checks the BisectHosting sponsor markers, required shortlink, and required banner image in `README.md`.

**Gap:** `curseforge-description.html` also contains the sponsor banner/link, but the current sponsor guard does not protect it.

**Files affected:**

- `.github/scripts/validate.py`
- `curseforge-description.html`
- `README.md`

**Exact suggested changes:**

Add a second sponsor check for `curseforge-description.html` if that sponsor placement is contractually required:

```python
def sponsor_guard_curseforge_description() -> None:
    text = read(ROOT / "curseforge-description.html")
    for label, needle in {
        "BisectHosting sponsor link": BISECT_SPONSOR_LINK,
        "BisectHosting sponsor banner": BISECT_SPONSOR_BANNER,
    }.items():
        if needle not in text:
            fail(f"curseforge-description.html missing required sponsor content: {label}")
```

If the CurseForge sponsor block is **not** required, document that clearly in this audit or a future `CONTRIBUTING.md` so nobody treats it as sacred by accident.

---

### 8. Issue templates are strong, but routing has one sharp edge

**Verified fact:** The issue forms already require useful fields: pack version, launcher/source, Minecraft version, Forge version, Java version, OS, mode, steps, logs where relevant, clean-install checks, and extra-content disclosure.

**Verified edge case:** `server_issue.yml` includes options for `Server crash` and `Client crash when joining`, while `crash_report.yml` says crashes should use the crash report template.

**Risk:** Crash reports can be split between two forms. That creates triage soup.

**Files affected:**

- `.github/ISSUE_TEMPLATE/server_issue.yml`
- `.github/ISSUE_TEMPLATE/crash_report.yml`

**Exact suggested changes:**

Option A, strict routing:

```yml
# In server_issue.yml, remove these issue-type options:
- Server crash
- Client crash when joining
```

Then add markdown:

```md
If the client or server terminates and creates a crash report, use the Crash report template. Server issue is for setup, mismatch, connection, LAN, hosted-server, and multiplayer-only behavior that does not produce a crash report.
```

Option B, flexible routing:

Keep the options, but make `client-logs` required when `issue-type` is `Client crash when joining`. GitHub issue forms do not support conditional required fields, so this is weaker.

Recommended: **Option A.** Cleaner. Less mud.

---

### 9. Discussions link may be fragile unless Discussions are enabled

**Verified fact:** `.github/ISSUE_TEMPLATE/config.yml` includes a contact link to `https://github.com/SoumyajitXD/Still-Watching/discussions`.

**Needs confirmation:** This audit did not verify whether GitHub Discussions are enabled for the repository.

**Risk:** If Discussions are disabled, the issue chooser sends users to a dead room with the lights off.

**Files affected:**

- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/scripts/validate.py`

**Exact suggested changes:**

Either:

- Confirm Discussions are enabled and keep the link.
- Or replace the contact link with a safer destination, such as the installation guide or issues page.

Add link validation that checks this URL does not return a hard failure.

---

### 10. `Screenshots/` needs lightweight documentation

**Verified fact:** README points users to `Screenshots/`, and CI watches `Screenshots/**`.

**Gap:** No inspected file documented screenshot naming, preferred dimensions, allowed formats, or whether screenshots are source assets for CurseForge.

**Files affected:**

- `Screenshots/README.md` new file
- `README.md`
- `.github/scripts/validate.py`

**Exact suggested changes:**

Add `Screenshots/README.md`:

```md
# Screenshots

Screenshots used for GitHub and CurseForge presentation.

Guidelines:

- Prefer `.png` or high-quality `.jpg`.
- Use clear filenames: `still-watching-fog-forest-01.png`.
- Do not include private server IPs, usernames you do not want public, coordinates for private worlds, or chat leaks.
- Keep the horror tone visible: fog, caves, structures, audio/visual pressure, threats, and survival setups.
- Do not upload giant uncompressed junk. The fog is heavy enough.
```

Optional validation:

- Warn on files over a chosen size threshold.
- Warn on unsupported extensions.
- Require at least one screenshot if the directory is expected to be non-empty.

---

### 11. `Releases/` needs a policy file so release-side files are not misunderstood

**Verified fact:** README says `Releases/` contains release-side files. The installation guide repeatedly warns that GitHub is not the playable installer.

**Gap:** No inspected file inside `Releases/` explained what belongs there, what must not be there, or how it relates to CurseForge.

**Files affected:**

- `Releases/README.md` new file
- `.github/scripts/validate.py`
- `README.md`

**Exact suggested changes:**

Add `Releases/README.md`:

```md
# Releases

This folder is for release-side repository files only.

CurseForge is the official playable install source. Files here must not be described as the canonical playable installer unless they are explicitly mirrored from a verified CurseForge release and documented as such.

Do not commit:

- private logs
- crash reports
- saves/world folders
- server IPs or secrets
- launcher caches
- local test junk

If a ZIP is a CurseForge-style export, it should include `manifest.json`. If it is an auxiliary archive, document what it is. Mystery ZIPs are not atmospheric. They are maintenance debt in a body bag.
```

Update `release_zips()` to warn when ZIPs lack `manifest.json`, but do not falsely claim they are invalid unless repository policy requires every ZIP to be a CurseForge export.

---

## Nice-to-have polish

### 12. Add `CONTRIBUTING.md`

**Why:** README has contribution notes, but a dedicated contributor guide would keep the issue tone, sponsor rules, release-file rules, and validation commands in one place.

**Files affected:**

- `CONTRIBUTING.md` new file
- `README.md`

**Exact suggested sections:**

- What this repo is / is not
- How to report useful bugs
- How to update docs without breaking tone
- Sponsor block rules
- Release file rules
- Local validation command:

```bash
python .github/scripts/validate.py all
```

### 13. Add a short changelog or release-notes pointer

**Why:** The repo points to CurseForge files for specific versions, but there is no local release notes index.

**Files affected:**

- `CHANGELOG.md` new file, or `Releases/README.md`

**Exact suggested wording:**

```md
# Changelog

CurseForge file pages are the source of truth for playable releases. This file only summarizes repository-side documentation and validation changes.
```

This avoids pretending GitHub owns the playable distribution.

### 14. Add markdown linting that respects the project voice

**Why:** Docs are readable now, but future edits can introduce broken heading order, repeated headings, malformed tables, or dead anchors.

**Files affected:**

- `.github/workflows/ci.yml`
- `.github/scripts/validate.py` or a separate markdown lint config

**Exact suggested checks:**

- Duplicate heading detection.
- Broken relative anchors.
- Tables have consistent separator rows.
- No trailing placeholder text like `TODO`, `FIXME`, `vX.X.X` outside examples.

Do **not** enforce bland style rules like “avoid strong language.” The pack’s voice is part of the product. Removing it would be vandalism with a spellchecker.

---

## Files affected summary

| File/path | Priority | Action |
| --- | --- | --- |
| `curseforge-description.html` | Critical | Remove or validate hard-coded latest release version claims. |
| `latest-modlist.md` | Critical | Add verification metadata: release/file, date, source-of-truth warning. |
| `.github/scripts/validate.py` | Critical | Add stale-version, link, stronger release ZIP, stronger HTML, and cross-doc consistency checks. |
| `.github/workflows/ci.yml` | High | Add new validation commands and include any new docs in path filters. |
| `.github/ISSUE_TEMPLATE/server_issue.yml` | High | Route crashes cleanly to crash report template. |
| `.github/ISSUE_TEMPLATE/config.yml` | High | Verify Discussions link or replace it. |
| `Releases/` | High | Add `Releases/README.md`; define what belongs here. |
| `Screenshots/` | High | Add `Screenshots/README.md`; define image rules and privacy warnings. |
| `README.md` | Nice-to-have | Link to new contributor/release/screenshot docs once added. |
| `installation-guide.md` | Nice-to-have | Keep as-is unless anchor/link validation finds drift. Current warnings are direct and useful. |

---

## Risks / things not to change

- Do **not** remove sponsor content or sponsor markers unless validation/sponsor requirements explicitly change.
- Do **not** say GitHub is the playable installer. It is not.
- Do **not** invent exact server-side mod lists from the client modlist. The installation guide is correct to warn against unverified server-pack guessing.
- Do **not** hard-code “latest version” unless there is an automated release process updating every place the version appears.
- Do **not** replace the horror voice with generic customer-support paste. The current tone is clear, useful, and memorable. Keep the knives; just sharpen the checks.
- Do **not** make CI depend on live external link checks as a hard blocker without fallback behavior. CurseForge/GitHub/CDNs can rate-limit or hiccup. Network ghosts are real; do not let them brick every PR.

---

## Verified vs. unverified notes

### Verified during audit

- README states CurseForge is the install source and GitHub ZIP is not playable.
- Installation guide repeats the same source-of-truth warning and includes install, update, backup, server, logs, and troubleshooting sections.
- `latest-modlist.md` contains 64 numbered CurseForge mod links.
- `curseforge-description.html` hard-codes `V1.0.9`.
- CI runs layout, YAML, HTML smoke parsing, project facts, issue templates, modlist, sponsor guard, and release ZIP audit.
- Validator protects the README BisectHosting sponsor block.
- Issue templates are structured YAML forms and collect useful debugging fields.
- The latest visible commit already fixed modlist numbering drift and corrected the README workflow reference.

### Not verified / needs manual confirmation

- Whether CurseForge’s actual latest file is `V1.0.9` or newer.
- Whether files in `Releases/` match any CurseForge release.
- Whether `Releases/` currently contains ZIPs, auxiliary files, or nothing.
- Whether `Screenshots/` currently contains all images referenced by CurseForge/GitHub presentation.
- Whether GitHub Discussions are enabled for the repository.

Those are not assumptions. They are inspection targets for the next pass once directory listings or release artifacts are explicitly reviewed.
