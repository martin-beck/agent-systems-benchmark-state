# AR-1423: Exhaustive literature docs-to-registry reconciliation

## Objective

Build a machine-checked reconciliation between every benchmark or workload
family named in `docs/WORKLOADS.md`, `docs/RELATED_WORK.md`, `docs/PLAN.md`,
and the versioned workload registries.  The reconciliation must make every
established benchmark visible as either a selectable workload, a selectable
but unavailable/provenance-only record, or an explicitly classified
framework/harness/scorer boundary.  No literature mention may silently
disappear, and no framework may be exposed as an executable workload without
an independent task protocol and grader.

The audit must include SWE-bench Lite/Verified and Pro, Terminal-Bench, Aider
Polyglot and its Exercism tracks, BigCodeBench, HumanEval+/MBPP+ via EvalPlus,
LiveCodeBench, SWE-Lancer, SWE-rebench, SWE-Perf, SWEfficiency, Core-Bench,
AgentBench, tau-bench, and AgentDojo, plus explicit non-workload treatment for
Harbor, Inspect AI, HAL, AgentOps, and HELM.

## Dependencies

- AR-1415 (total literature selector coverage)
- AR-1419 (framework/workload boundaries)
- AR-1403 (optional external qualification boundary)

## Acceptance

- A generated, schema-validated parity artifact maps each docs-listed name to
  exactly one stable registry identity and records family, kind, source and
  dataset revisions, license state, evaluator state, and evidence status.
- Missing, conflicting, duplicate, mutable, or unlicensed identities fail
  closed with an actionable diagnostic; framework-only references cannot be
  selected for execution.
- The parity check covers both the seven built-in software-engineering
  fixtures and every literature identity, preserving distinct metric families
  (repository repair, terminal, code generation, interactive/tool-use,
  performance, and computational reproducibility).
- Positive and negative tests prove docs drift, omitted records, duplicate
  aliases, stale revisions, and accidental framework activation are rejected.
- Documentation is generated from the registry or parity source; no private
  paths, credentials, datasets, or live provider access are introduced.

## Verification

Run focused registry/parity tests, generated-document checks, full workspace
quality, exact-head CI, independent review, and every required post-merge
assurance workflow.
