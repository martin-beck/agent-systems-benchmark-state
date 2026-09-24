# AR-1402: Literature workload CLI dispatch integration

## Objective

Replace every execution seam that assumes `OriginalWorkloads` with the unified
catalog and adapter dispatch, while preserving built-in behavior. Literature
fixtures must work through normal plan, run, sweep, recording, replay, report,
and comparison flows; external candidates must remain fail-closed.

## Acceptance

- `doctor`, plan creation, stored-run validation, recording campaigns, `run`,
  `sweep`, reports, comparison, and replay carry source/revision, task/content
  digest, scorer digest, adaptation, and evidence status.
- Every executable local literature family has end-to-end positive coverage;
  unknown, methodology-only, unavailable-evaluator, stale-digest, and
  unsupported-platform inputs produce actionable bounded errors.
- Built-in fixtures remain behaviorally unchanged and all paths remain offline
  by default with no provider credentials or network access.

