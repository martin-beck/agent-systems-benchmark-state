# AR-1410: Literature selector completeness and parity

## Objective

Close the final selection and documentation gap across all literature-derived
workload families.  Ensure every catalog entry that is executable through a
local fixture is discoverable, selectable, plan-able, runnable, recordable,
replayable, and reportable through the same paths as built-in workloads, while
preserving truthful evidence states for external-only entries.

## Dependencies

- AR-1402 (CLI dispatch integration)
- AR-1404 (documentation and matrix contract)
- AR-1409 (interactive adapters)

## Acceptance

- `doctor` and catalog output expose a deterministic inventory containing all
  literature workload IDs, kinds, capabilities, source revisions, adapters,
  and evidence status beside the built-in suite.
- Selector filters support workload family, capability, local/mock readiness,
  evaluator availability, and platform status without silently upgrading
  `planned`, `unsupported`, or `unqualified` cells.
- End-to-end offline tests cover plan, run, sweep, record, replay, comparison,
  and report for every locally executable family; external-only selections fail
  closed before any network/provider attempt.
- Generated docs and schemas match the registry and CLI inventory in CI, with
  negative tests for omissions, duplicate IDs, stale digests, and hand-edited
  drift.

## Verification

Run focused selector/CLI tests, generated-doc parity, full workspace gates,
exact-head CI, independent review, and merged-commit post-merge verification.
