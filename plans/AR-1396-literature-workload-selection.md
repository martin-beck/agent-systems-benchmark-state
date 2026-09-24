# AR-1396: Selectable literature workloads in ASB CLI

## Objective

Expose the qualified/available literature workload IDs beside the built-in
software-engineering fixtures in the ASB workload catalog and experiment-plan
selection flow. Selection must be explicit, reproducible, and truthful about
availability; it must not trigger an implicit download or external provider.

## Acceptance

- `list/describe/plan/run/sweep` (or their current equivalents) enumerate
  built-in and literature IDs from one versioned catalog, with source/revision,
  evaluator, license, adaptation, platform, availability, and evidence status.
- Unknown, provenance-only, unavailable, unsupported-platform, unqualified, or
  evaluator-missing IDs fail closed with actionable bounded errors; built-in
  behavior remains unchanged.
- Experiment identity, reports, replay records, and comparison outputs carry
  stable workload ID, source revision, task digest, scorer digest and status;
  aggregate scores never combine incompatible families without explicit strata.
- CLI tests cover positive selection of each supported family, hostile IDs,
  offline default, explicit acquisition authorization, local mock execution,
  and no-network/privacy boundaries. Documentation and guide contracts update.
