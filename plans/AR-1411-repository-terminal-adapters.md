# AR-1411: Repository and terminal workload adapters

## Objective

Make the established repository-repair and terminal-workflow benchmarks named
in `docs/WORKLOADS.md` selectable beside the built-in software-engineering
workloads: SWE-bench Lite/Verified, Terminal-Bench, Aider Polyglot, and the
licensed Exercism tracks recorded by the Aider entry. Preserve each upstream
task, dataset, evaluator, and license identity instead of flattening them into
one score.

## Dependencies

- AR-1408 (closed literature inventory and provenance boundaries)
- AR-1401 (bounded deterministic local/mock execution)

## Acceptance

- Every family has a stable catalog ID, pinned source/dataset/evaluator
  revisions, license fields, capability tags, attempt budget, and explicit
  evidence status.
- Offline local fixtures cover repository checkout, patch collection,
  terminal commands, test grading, reset, timeout, malformed patch, and
  network-egress failure paths without contacting an upstream provider or
  downloading a dataset during a run.
- CLI, plan, run, sweep, record, replay, and report paths can select each
  locally executable family beside built-in workloads; external-only or
  unqualified selections fail closed with an actionable reason.
- Aider's language tracks remain independently identified and their licenses
  and attribution are retained. No private task data, credentials, or raw
  transcripts are stored.
- Positive and negative tests reject stale revisions, unknown IDs, duplicate
  identities, mutable references, missing evaluator evidence, and attempts to
  claim native qualification from a container or cross-build.

## Verification

Run focused adapter/mock and registry tests, generated catalog parity, full
workspace quality gates, exact-head CI, independent diff review, and all
post-merge assurance workflows.
