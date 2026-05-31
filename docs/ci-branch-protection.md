# CI and Branch Protection Recommendations

Repository settings cannot be enforced from this patch, but the maintainer should protect `main` so the new CI actually guards the door.

Recommended GitHub settings:

- Require a pull request before merging to `main`.
- Require the CI workflow checks before merging.
- Require branches to be up to date before merging when practical.
- Block force pushes to `main`.
- Block deletion of `main`.
- Require conversation resolution before merge.
- Optionally require signed commits if the maintainer wants stricter provenance.

The goal is simple: make accidental breakage harder than doing the right thing.
