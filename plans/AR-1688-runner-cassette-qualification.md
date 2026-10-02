# AR-1688 — runner-owned cassette capture and replay qualification

Qualify the ASB runner/control recording campaign and strict offline replay
for selected and all supported workloads. Ensure captures are redacted,
sealed, content-addressed, complete before publication, and consumed without
provider contact.

## Acceptance

- Selected-workload capture produces a sealed cassette with exact provider and
  agent binding.
- All-workload campaign expansion is bounded and succeeds only with complete
  coverage; partial coverage publishes no misleading cassette set.
- Duplicate, mismatched, corrupt, or incomplete captures fail closed.
- Strict offline replay succeeds from the sealed cassette while network contact
  is denied and no credential is required.
- Hosted checks, independent review, exact-head receipt, and no-secret scan
  pass.
