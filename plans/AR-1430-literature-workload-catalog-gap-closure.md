# AR-1430: Literature workload catalog gap closure

## Objective

Close the gap between benchmarks named by the ASB literature documents and the
machine-selectable workload catalog.  Define stable, namespaced workload
identities for every established benchmark family, while distinguishing a
deterministic local/mock fixture from an official external benchmark.  The
catalog must make all records discoverable beside the seven `original.*`
software-engineering fixtures and fail closed for records that cannot run
offline.

## Scope

Reconcile these documented families: SWE-bench Lite, Verified and Pro;
Terminal-Bench; Aider Polyglot and Exercism; BigCodeBench; EvalPlus
(HumanEval+/MBPP+); LiveCodeBench; SWE-Lancer; SWE-rebench; SWE-Perf;
SWE-fficiency; CORE-Bench; AgentBench; tau-bench; and AgentDojo.  Preserve
framework-only boundaries for Harbor, Inspect AI, HAL, AgentOps and HELM.

Each identity records source/dataset/scorer revisions, license and acquisition
policy, semantic family, execution status, evidence limitations, and whether a
local deterministic fixture exists.  No dataset download, provider call,
native-host claim, or official-score claim is introduced by this AR.

## Dependencies

- AR-1423 (docs-to-registry reconciliation)
- AR-1416 (local/mock cross-product contract)

## Acceptance

- The closed registry and generated docs contain one stable identity for every
  listed family, with no duplicate, stale, or framework-misclassified record.
- CLI workload discovery and planning expose every identity for inspection;
  locally executable identities select deterministic fixtures or a loopback
  LiteLLM-compatible mock, while unavailable identities reject execution before
  network, credentials, privileged containers, or upstream acquisition.
- Family semantics and metrics remain explicit: repository repair, terminal
  interaction, multilingual editing, function correctness, time-windowed
  coding, long-horizon/proposal work, performance/efficiency, reproducibility,
  interactive environments, reliability, and tool-use safety are not collapsed
  into one score.
- Positive and negative tests cover IDs, revisions, unknown fields, duplicate
  identities, unavailable reasons, fixture selection, and fail-closed planning.
- Docs, generated catalog, schemas, and selector output are parity-checked in a
  clean offline-after-install run.

## Verification

Run focused registry/selector tests, full workspace quality, privacy and formal
checks, independent diff review, exact-head CI, and all required post-merge
assurance workflows. Record exact source and merge evidence in the state task.
