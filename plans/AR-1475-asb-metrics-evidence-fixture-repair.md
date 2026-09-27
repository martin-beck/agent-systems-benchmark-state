# AR-1475: Repair asb-metrics evidence fixture classification

## Objective

Repair the deterministic hosted `asb-metrics` fixture failure that blocks PR
#345 and causes the repository-quality coverage job to abort. The failing
`missing_malformed_and_unsafe_configuration_fail_closed` test observes
`ProbeRejected` where it expects `MalformedEvidence`.

## Dependencies

AR-1200 supplies the existing metrics timeout/fixture-stability context;
AR-1379 and AR-1472 provide the current protected-main live-dispatch baseline.
This repair is intentionally independent of blocked AR-1474 so it can unblock
its exact-head validation.

## Required work

- Reproduce the failure on the exact PR/main baseline and determine whether
  the fixture, probe ordering, or classification contract is wrong.
- Make the smallest deterministic fix preserving fail-closed behavior and
  existing malformed/unsafe distinction; add positive and negative tests for
  the repaired boundary and repeat the relevant test enough times to rule out
  flakiness.
- Run focused metrics tests, workspace tests, coverage, fmt, clippy, and all
  applicable formal/privacy/platform gates. Do not waive the existing failure
  or weaken evidence classification.
- Publish a clean signed+DCO PR, require exact-head CI and independent review,
  merge only when green, verify all post-merge workflows, then rerun PR #345
  validation at its unchanged product head if compatible.

## Boundaries

No asb-tui changes, no provider/network requirement, no test skipping, no
synthetic evidence, no privacy weakening, and no edits to `handoffctl`.
