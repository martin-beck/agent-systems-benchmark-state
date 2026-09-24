# AR-1413: Long-horizon and performance workload adapters

## Objective

Add truthful selectors and bounded local adapters for the remaining documented
long-horizon, continuously refreshed, performance, and computational
reproducibility families: SWE-bench Pro, SWE-Lancer, SWE-rebench, SWE-Perf,
SWEfficiency, and Core-Bench. Keep unavailable archives, missing licenses,
mutable evaluation windows, and unqualified HAL infrastructure explicit.

## Dependencies

- AR-1408 (closed literature inventory and provenance boundaries)
- AR-1401 (bounded deterministic local/mock execution)

## Acceptance

- Every family has an immutable source/dataset/evaluator identity, license and
  archive status, split/window or task identity, metric kind, and platform
  evidence state in the catalog.
- Locally runnable fixtures cover patch/task setup, reset, grading, performance
  measurement boundaries, timeout/failure, and reproducibility metadata without
  requiring a live provider, public network, privileged host, or HAL service.
- Continuously refreshed suites require an explicit evaluation-window pin and
  contamination cutoff. Unavailable or unlicensed sources remain cataloged but
  are rejected before execution.
- Performance claims retain paired-trial, uncertainty, hardware-control, and
  correctness boundaries; simulated/container evidence cannot become native or
  timing qualification.
- Selector and report paths keep these families separate from ordinary
  repository-repair scores, with positive/negative tests for stale windows,
  mutable references, missing oracle evidence, and unsupported platforms.

## Verification

Run focused adapter/metric tests, registry and docs parity, full workspace
quality gates, exact-head CI, independent provenance/privacy review, and all
post-merge assurance workflows.
