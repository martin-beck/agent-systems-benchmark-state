# AR-1426: Evolving literature workload window refresh

## Objective

Maintain truthful, selectable revisions for literature workloads whose task
windows change over time, especially LiveCodeBench and SWE-rebench. A refresh
must produce a new content-addressed workload identity and never mutate an
existing result or silently reuse a stale dataset/evaluator pairing.

## Dependencies and scope

- Depends on AR-1423 and AR-1425.
- Product repository only; `asb-tui` is out of scope.
- Owned paths: workload registry refresh metadata, window manifests, selector
  validation, report provenance, documentation, and tests.

## Acceptance

1. Define a versioned refresh manifest containing source and dataset revisions,
   time-window/contamination cutoff, split selection digest, evaluator and
   image/SBOM identities, license state, and evidence status. Missing or
   mutable fields keep the entry inspection-only/unavailable.
2. Add deterministic offline fixtures for an unchanged window, a new window,
   a changed evaluator, a changed task selection, and a rejected stale or
   mismatched refresh. Existing result manifests remain bound to their exact
   prior identity.
3. Make `plan`, `run`, `record`, `replay`, `compare`, and `report` display the
   window identity and refuse cross-window comparisons unless an explicit
   compatible contract exists. Built-in and stable literature workloads keep
   their existing behavior.
4. Refresh validation must be network-free in CI and must not require a live
   provider, upstream download, native host, credential, or signed bundle.
5. Add positive and negative schema/CLI/report tests, generated documentation
   parity, privacy checks, full quality gates, exact-head CI, independent
   review, and all required post-merge assurance workflows before release.

## Non-goals

No dataset vendoring, automatic network acquisition, score normalization across
windows, provider connectivity, native qualification, or TUI changes.
