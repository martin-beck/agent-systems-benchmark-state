# AR-1399: Complete the literature workload registry

## Objective

Extend the versioned external-workload registry with every workload suite or
benchmark boundary named by the ASB literature snapshot and related-work docs
that is not already represented. This includes Harbor task environments,
Inspect AI scenarios, HAL-compatible tasks, AgentBench interactive OS/database
tasks, tau-bench simulated-user tasks, and AgentDojo tool-use robustness
tasks. AgentOps and HELM remain methodology/observability references unless a
specific executable workload is identified. Existing SWE, coding-control and
systems-performance records remain authoritative and must not be duplicated.

## Acceptance

- Each added ID has a stable kind, source revision, separate dataset/evaluator
  provenance, license, acquisition policy, adaptation relation, contamination
  status, platform matrix and limitations; unknown or incomplete evidence is
  explicitly planned/unavailable rather than upgraded to executable.
- Registry schema, generated docs and catalog tests cover every docs-listed
  workload family and reject duplicate IDs, mutable revisions, missing license
  or evaluator/reset evidence, and accidental network/default execution.
- No dataset or provider is vendored; local deterministic fixtures exercise
  record parsing and selection, while real provider connectivity remains
  optional and never a completion gate.
- The change is independently reviewed, signed+DCO, and passes exact-head and
  post-merge gates before AR-1396 selection work consumes it.
