# AR-1400: Literature workload catalog activation

## Objective

Expose every established benchmark recorded in `docs/WORKLOADS.md` and
`docs/RELATED_WORK.md` through one versioned ASB workload catalog, alongside the
seven built-in software-engineering fixtures. The catalog must make the
distinction between selectable metadata, locally mock-runnable workloads, and
externally qualified workloads explicit.

## Scope

- Include the registry IDs for SWE-bench Lite/Verified/Pro, SWE-rebench,
  SWE-Lancer, Terminal-Bench, Aider Polyglot, Exercism, BigCodeBench,
  HumanEval+/MBPP+ (EvalPlus), LiveCodeBench, SWE-Perf, SWE-fficiency,
  CORE-Bench, AgentBench, tau-bench, AgentDojo, Harbor, Inspect AI, and
  HAL-compatible tasks.
- Keep AgentOps and HELM as methodology-only references unless a concrete
  workload record exists.
- Add stable catalog metadata for source revision, split/window, license,
  evaluator/scorer identity, adaptation, availability, platform cells, and
  evidence status.
- `list`, `describe`, and plan validation may select any catalog record as a
  declared *candidate*; `run`/`sweep` must reject records lacking a qualified
  evaluator or local mock with a specific actionable error.

## Acceptance

- Catalog output and experiment identity are deterministic and include the
  exact workload and scorer digests; unknown fields and hostile IDs fail closed.
- Candidate selection never downloads data, contacts a provider, or changes
  the status of a record. Reports cannot aggregate incompatible families.
- Positive and negative CLI tests cover every family, methodology-only records,
  unavailable evaluators, unsupported platforms, stale digests, and built-in
  regression behavior. Generated docs and schemas remain synchronized.
- A strict typed catalog is the single source for built-ins, literature
  records, and methodology-only references; duplicate/missing-ID and docs/
  registry parity tests fail closed.
