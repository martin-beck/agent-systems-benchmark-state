# AR-1670 — Repair ASB state strict-mypy baseline

Reproduce the strict-state failure on the exact base and PR heads, then restore
the missing `tools.git_authority_adapter`, `tools.sqlite_authority_adapter`, and
`tools.roles` modules from the exact pinned `coordinator.vendor.json` source
(currently Coordinator v0.3.53), or create a separately reviewed compatibility
diff with byte/source provenance. Preserve barrier status, repository identity,
rollback/commit dispatch, WAL/SHM recovery, and all fail-closed negative checks;
never delete those capabilities to satisfy mypy. Resolve existing strict mypy
errors without ignores or exclusion changes. Run formatting, typing, authority
tests, 95% coverage, doctor, render-status, AWQ, DCO/signature, and fresh
exact-head verification, recording a baseline and repair receipt.
