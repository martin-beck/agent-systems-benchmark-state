# AR-1374: Production live-provider dispatch

## Objective

Wire the authenticated runtime receipt source from AR-1373 into the production
`asb run` and `asb sweep` dispatch path. The CLI may request an opaque runtime
operation only; it must not provide provider authority, credentials, relay
roots, namespace identity, or lease material.

## Dependencies

AR-1373, AR-1339, AR-1340, and AR-1328 must be done.

## Acceptance

- runtime-owned bridge is the only source of provider receipt/attempt authority;
- run and sweep dispatch bind provider, generation, nonce, lease, relay, and
  namespace to the authenticated receipt;
- offline, replay, mismatch, expired, revoked, unavailable, and teardown paths
  fail closed;
- positive and negative tests cover the complete CLI-to-runtime seam without
  secrets, private paths, or synthetic authority;
- signed+DCO commit, focused/full gates, exact-head CI, independent review,
  protected merge, and all post-merge workflows pass.

## Current development and CI qualification boundary

The mandatory development and CI qualification path for this AR is a deterministic
local provider/LLM mock (LiteLLM-compatible where practical), including hostile
negative tests and offline replay where applicable. External/live OpenRouter or
other provider reachability is optional supplementary evidence only; it is never a
completion, dependency-readiness, or CI gate. Production egress policy, credential
non-disclosure, runtime-owned authority, namespace/relay attestation, cancellation
and teardown, and fail-closed denial of unapproved external traffic remain required
contracts. Existing live-provider dependency edges describe production integration
ordering only and must not be used to block local qualification or to claim external
reachability.
