# AR-1687 — development/mock provider-bound comparison qualification

Qualify the current ASB comparison route against provider-bound run
provenance. Cover available and unavailable provider selections, asymmetric
baseline/candidate availability, differing provider/model identities, and
multi-candidate output. Preserve opaque run identifiers and typed unavailable
reasons.

## Acceptance

- Exact-main mock runs produce truthful comparable/confounded results.
- Missing baseline or candidate provider selection is reported by side and
  cannot produce a comparable claim.
- Provider/model or execution-binding differences are surfaced as confounders.
- Multi-candidate comparisons retain per-pair and aggregate availability.
- No provider contact or credential is needed; development auth warnings are
  visible and non-blocking.
- Hosted checks, independent review, exact-head evidence, and no-secret scan
  pass.
