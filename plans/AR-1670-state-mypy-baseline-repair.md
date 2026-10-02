# AR-1670 — Repair ASB state strict-mypy baseline

Reproduce the strict-state failure on the exact base and PR heads, then restore
the missing `tools.git_authority_adapter`, `tools.sqlite_authority_adapter`, and
`tools.roles` modules from the correct Coordinator-compatible source or repair
their imports. Resolve existing strict mypy errors without ignores or exclusion
changes. Run formatting, typing, doctor, render-status, AWQ, DCO/signature, and
fresh exact-head verification, recording a baseline and repair receipt.
