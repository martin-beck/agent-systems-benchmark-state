# AR-1412: Code-generation control adapters

## Objective

Integrate the documented function-level and time-windowed coding controls as
selectable workload families: BigCodeBench, HumanEval+/MBPP+ via EvalPlus, and
LiveCodeBench. They must sit beside the built-in and agent-oriented workloads
while remaining clearly labeled as code-generation/correctness controls, not
complete autonomous-agent evaluations.

## Dependencies

- AR-1408 (closed literature inventory and provenance boundaries)
- AR-1401 (bounded deterministic local/mock execution)

## Acceptance

- Each control has a stable ID, exact source and dataset revisions, license,
  split/window identity, evaluator/scorer revision, and evidence state.
- Local deterministic fixtures exercise generation input, execution checks,
  timeout/resource bounds, malformed output, reset, and scorer mismatch paths;
  no remote execution service or provider is contacted.
- Selection, planning, recording, replay, comparison, and reporting preserve
  the control's distinct metric semantics and never combine them with
  repository-agent scores.
- Time-window identity and contamination boundaries are explicit; mutable
  latest references, missing licenses, missing evaluator images, and
  unsupported platform claims fail closed.
- Positive and negative registry, selector, and generated-document tests are
  included, with no vendored datasets, credentials, or private traces.

## Verification

Run focused fixtures and scorer-contract tests, catalog/docs parity, full
workspace gates, exact-head CI, independent review, and post-merge assurance.
