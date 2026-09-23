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
