# AR-1687 — provider-bound development comparison qualification

## Scope

Exercise the comparison seam created by AR-1686 with a selected provider/model
profile and deterministic development/mock responses. The receipt must bind the
provider profile, model, agent, workload, executable, experiment digest, and
comparison output while retaining a secret-free offline path.

## Acceptance

- A fresh generated plan runs the provider-bound development/mock comparison.
- Provider/model identity and experiment digest are present and consistent in
  human and JSON receipts, with no credential values.
- Missing or unavailable provider credentials produce typed warning-only
  development diagnostics; malformed or mismatched identity fails closed.
- Exact-head checks, independent review, generated projections, and no-secret
  scan pass.

The paired TUI consumer is tracked in TUI-state AR-1679; its cross-repository
relationship is recorded here as evidence, not as a local dependency.
