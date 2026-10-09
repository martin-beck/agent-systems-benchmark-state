# AR-1756 plan: Coordinator v0.4.0 development vendor and acceptance lifecycle

## Scope

The upstream Coordinator `origin/main` at
`c2692d08382e0a16e9d0dd4f8c08dba36a29b713` contains the reviewed
`feat: add spec acceptance command` change (`f058a8b0a259ccb3ee8df610e2379af9fc49fd88`)
and reports project version `0.4.0`. The upstream repository has no `v0.4.0`
tag; therefore this AR is explicitly a development-vendor adoption, not a
release upgrade or release-provenance claim.

Use a clean exact upstream checkout and the documented `vendor.py
sync-development --commit c2692d08382e0a16e9d0dd4f8c08dba36a29b713` path.
Review the complete staged vendor diff and generated schema-v2 manifest. Never
edit a vendored Coordinator file in place. Any compatibility or fixture repair
must be confined to ASB-owned files and carry positive and negative coverage.

## Required work

1. Independently verify the upstream commit, tree, cleanliness, ancestry of the
   acceptance implementation, declared version, and absence of a v0.4.0 tag.
2. Sync the exact commit into an isolated ASB-state worktree with the supported
   development vendor tool; verify every recorded digest and source-to-vendor
   byte comparison.
3. Run the complete state quality, generated-view, privacy, schema, strict
   Ruff/mypy, unit/coverage, formal, and doctor gates. Repair only downstream
   regressions, preserving AR-1729/AR-1730 evidence and existing thresholds.
4. Exercise `handoffctl accept` against a disposable task fixture and then use
   the supported acceptance path to close AR-1729 and AR-1730 only after their
   independently verified product merges and exact-main evidence are reviewed.
   Do not fabricate or overwrite acceptance receipts.
5. Obtain independent exact-tree review, publish a signed+DCO PR, wait for all
   exact-head checks, merge using the documented signed two-parent path, rerun
   exact-main checks, reconcile, and run `doctor --live`.

## Boundaries

This AR does not claim a Coordinator v0.4.0 release, does not weaken vendor
integrity, and does not patch the upstream source. A future tagged v0.4.0 may
replace this development vendor only through a separate release upgrade AR.
