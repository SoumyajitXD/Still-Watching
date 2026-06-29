<!-- markdownlint-disable MD013 -->

## Summary

Describe what changed and why.

## Change Type

- [ ] Documentation
- [ ] Metadata
- [ ] Issue templates or support flow
- [ ] CI or validation
- [ ] Server-pack guidance
- [ ] Screenshots or presentation
- [ ] Other

## Scope Check

- [ ] I kept CurseForge as the official playable install source.
- [ ] I did not imply that the GitHub ZIP is a playable modpack installer.
- [ ] I did not claim unsupported loader, Minecraft-version, launcher, or server-pack support.
- [ ] I preserved Apache-2.0 wording for original repository files only.
- [ ] I preserved third-party license and attribution boundaries.
- [ ] I kept this PR focused.

## Validation

Paste the commands you ran:

```text

```

Suggested checks:

```bash
python3 .github/ci/validate_repository.py all
npx --yes markdownlint-cli2@0.18.1 "**/*.md" "!Releases/**"
git diff --check
```

## Evidence

Add screenshots, logs, links, or notes that prove the change is correct.

## Reviewer Notes

Mention risk, uncertainty, or follow-up work.
