# AR-1766: tagged Coordinator v0.4.0 uptake

1. Verify the remote lightweight tag, GitHub release, source tree, formal attestation and Coordinator post-merge checks. Confirm the current ASB vendor manifest is development-classified and compare its vendored runtime bytes against the release.
2. In the claimed isolated ASB-state worktree, use vendor.py sync --version v0.4.0 from a clean checkout of the tag. Verify manifest, all file digests, release classification and byte-for-byte source closure. Do not edit vendored Coordinator files or bindings.
3. Test supported handoffctl accept and release --status done on disposable Git and SQLite ASB-compatible fixtures, including missing acceptance, wrong owner, stale revision, malformed evidence and successful acceptance. Preserve existing ASB acceptance records and inspect generated views and live doctor.
4. Run all ASB-state quality, privacy, schema, coverage, formal, vendor and integration gates at unchanged thresholds. Repair only ASB-owned files with negative tests.
5. Obtain independent exact-head technical review, signed+DCO commit and PR, hosted exact-head checks, signed two-parent merge, exact-main post-CI, final tag/vendor verification, reconciliation and doctor --live. Do not mark the AR done from a development pin or a mere help-text check.
