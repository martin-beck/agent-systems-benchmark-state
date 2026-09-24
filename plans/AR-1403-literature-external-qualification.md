# AR-1403: Optional external literature workload qualification

## Objective

Provide a governed, opt-in path to qualify real literature workloads after
their source, license, evaluator, reset, image/SBOM, platform, and oracle
evidence are independently available. This AR must remain separate from local
development and must never block candidate selection or mock execution.

## Acceptance

- Reuse the existing external artifact verification, materialization, bounded
  planning, oracle validation, comparison, and report helpers.
- Require immutable source/evaluator revisions, separate code and dataset
  licenses, exact task split/window, evaluator and image digests, adaptation
  parity evidence, contamination/exposure records, and platform cells.
- Partial, stale, mutable, or mismatched artifacts fail closed; container,
  QEMU, or mock runs are recorded as such and never substitute for native
  qualification. Mixed scorer/evaluator identities cannot be aggregated.

