<!-- markdownlint-disable MD013 -->

## What changed?

Explain the problem and the fix. Link the related issue, if there is one.

## Checks

- [ ] CurseForge remains the official playable download; no unsupported compatibility claims.
- [ ] Third-party credits and license boundaries are preserved.
- [ ] Release metadata and related docs are updated where needed.

Run the relevant checks and note anything you could not run:

```bash
python3 .github/ci/validate_repository.py all
python3 -m unittest discover -s .github/ci -p 'test_*.py' -v
npx --yes markdownlint-cli2@0.18.1 "**/*.md" "!Releases/**"
git diff --check
```

## Evidence or risks

Include relevant logs, screenshots, sources, or testing limitations.
