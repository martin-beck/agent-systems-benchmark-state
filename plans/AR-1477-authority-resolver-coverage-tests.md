# AR-1477: Cover authority resolver behavior

## Objective

Close the exact hosted workspace coverage gap on PR #345. CI reports 89.88%
line coverage (98,431 total, 11,780 missed) after the signed synchronization
merge, just below the enforced 90% floor.

## Dependencies

AR-1200, AR-1379, and AR-1472 provide the stable metrics and live-dispatch
baseline. AR-1475 repaired the asb-metrics contention; this task addresses
only uncovered authority-resolver behavior introduced by AR-1474.

## Required work

- Reproduce the exact hosted coverage command on the exact PR head and inspect
  the uncovered lines; distinguish instrumentation variance from genuinely
  untested resolver behavior.
- Add deterministic local/mock/replay tests for resolver success, owner and
  generation fencing, stale/revoked records, malformed persistence,
  cancellation, teardown, and restart boundaries as applicable. Do not add
  dead-code exclusions or reduce the 90% floor.
- Run the exact coverage command repeatedly, focused/full tests, fmt, clippy,
  formal, privacy, and platform gates. Preserve fail-closed authority
  semantics and keep provider access optional.
- Publish a signed+DCO PR, pass exact-head review/CI, merge only green, verify
  all seven post-merge workflows, then revalidate PR #345 with the repair.

## Boundaries

No asb-tui changes, no live-provider requirement, no test skipping, no
synthetic authority, no privacy/gate weakening, and no edits to `handoffctl`.
