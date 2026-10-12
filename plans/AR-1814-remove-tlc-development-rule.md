# AR-1814: remove stale TLC development ruleset requirement

Update the ASB GitHub main ruleset so ordinary development pull requests no
longer require the obsolete `TLC and Alloy recovery models` status context.
AR-1811 moved TLC/Alloy into the explicitly labelled future final-delivery
workflow; the protected-main development ruleset must match that contract.

## Scope and safety

- Read and record the current ruleset before mutation.
- Remove only the TLC/Alloy required-status entry from ruleset 24750310.
- Preserve required signatures, non-fast-forward/deletion protections, zero
  approval policy (independent state review remains mandatory), all other
  required status checks, and merge-method restrictions.
- Validate the exact ruleset after mutation and record a digest-only receipt.
- Do not alter final-delivery formal workflow files or bypass branch rules.

## Acceptance

- Exact before/after ruleset evidence proves only the TLC entry changed.
- PR #606 becomes mergeable with all ordinary checks green; no TLC run is
  required for development.
- Independent review, signed DCO state evidence, and post-merge verification
  complete for the affected AR.
