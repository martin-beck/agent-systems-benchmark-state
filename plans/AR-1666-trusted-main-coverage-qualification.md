# AR-1666 — trusted-main broad TUI coverage qualification

Reproduce the trusted-main coverage result for TUI main `06e96770` (89.43%
total line coverage versus the strict 90% gate). Add focused tests for the
lowest-covered wizard, runtime, and UI behavior paths, including success,
failure, restart, and warning-only development cases. Preserve thresholds,
fail-closed production checks, and development nonblocking authentication,
signature, and key-management behavior. Record exact head, coverage report,
and hosted qualification evidence.
