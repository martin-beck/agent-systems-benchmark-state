# AR-1396: Selectable literature workloads in ASB CLI

## Objective

Expose the qualified/available literature workload IDs beside the built-in
software-engineering fixtures in the ASB workload catalog and experiment-plan
selection flow. Selection must be explicit, reproducible, and truthful about
availability; it must not trigger an implicit download or external provider.

The selectable namespace must cover the built-in engineering fixtures plus all
registry-backed literature families from `docs/WORKLOADS.md` and
`docs/RELATED_WORK.md`: SWE-bench variants, Aider Polyglot and Exercism,
Terminal-Bench, SWE-Perf, SWE-fficiency, CORE-Bench, BigCodeBench, EvalPlus,
LiveCodeBench, SWE-Lancer, SWE-rebench, Harbor, Inspect AI, HAL-compatible
tasks, AgentBench, tau-bench and AgentDojo. Methodology-only references such as
AgentOps and HELM stay visible as non-selectable references unless a concrete
workload record is later added.

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
