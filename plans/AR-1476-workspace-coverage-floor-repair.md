# AR-1476: Repair workspace coverage floor

## Objective

Raise or correctly account for workspace coverage so the exact AR-1474
validation satisfies the enforced 90% line floor. The failed repository-quality
run reported 98,414 lines, 11,761 missed, and 88.05% coverage.

## Dependencies

AR-1200 provides coverage/fixture stability context; AR-1379 and AR-1472 are
the protected-main live-dispatch baseline. This repair is independent of the
blocked AR-1474 implementation and must be applied without changing its exact
head unless the repair is explicitly rebased and revalidated.

## Required work

- Reproduce the exact coverage command and identify uncovered product paths,
  generated/test-only paths, or instrumentation drift; do not hide code from
  coverage merely to pass the floor.
- Add deterministic positive and negative tests for the uncovered behavioral
  paths introduced by AR-1474 or correct narrowly justified coverage
  exclusions for non-executable/generated code with documented evidence.
- Run workspace coverage repeatedly, focused tests, fmt, clippy, formal,
  privacy, and platform gates. Preserve the 90% floor and ensure optional
  evidence classification completes rather than being masked by interruption.
- Publish a signed+DCO PR, obtain exact-head CI and review, merge only green,
  verify all post-merge workflows, then rerun PR #345 validation at its exact
  head with the repair integrated.

## Boundaries

No test skipping, arbitrary threshold reduction, provider/network requirement,
asb-tui changes, synthetic evidence, privacy weakening, or edits to
`handoffctl`.
