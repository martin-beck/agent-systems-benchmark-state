# AR-1363: Authenticated control receipt source

## Objective

Expose a bounded, versioned control operation that returns a runtime receipt
only from the enrolled authority record introduced by AR-1362. The response
must be secret-free and bound to the authenticated request, generation, and
provider identity.

## Dependencies

Depends on AR-1362. AR-1361 and AR-1360 remain blocked until this source and
the downstream runtime-owned dispatch consumer are merged. AR-1329 remains
fail-closed.

## Required work

- Add a versioned `RuntimeReceipt` control request/result with strict schemas,
  bounded sizes, request binding, freshness and generation fencing.
- Have the runner backend load only the durable AR-1362 authority record and
  issue a `RuntimeEnrollmentReceiptV1`; reject absent, revoked, stale,
  mismatched, replayed, private/link-local, or unpinned authority.
- Preserve owner authentication, deadline/admission limits, offline/replay
  policy, and secret/path-free public output.
- Add positive and negative protocol/backend/endpoint tests and generated schema
  fixtures; do not expose certificate bytes or runtime private constructors.

## Acceptance

Focused/full gates, signed+DCO exact-head PR, independent review, protected
merge, and all seven post-merge workflows pass. Record exact evidence before
advancing the AR-1360 consumer or AR-1329.

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
