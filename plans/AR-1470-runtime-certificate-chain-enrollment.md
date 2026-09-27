# AR-1470: Runtime-owned certificate-chain enrollment materialization

## Objective

Provide the missing authenticated certificate-chain issuer and enrollment
materialization that lets `asb-runtime` issue a verifiable runtime receipt
without exposing provider targets, credentials, lease roots, relay roots, or
launch authority to `asb-cli`.

## Dependencies

AR-1357 and AR-1359 provide the versioned enrollment and control/runtime
attestation contracts; AR-1362 provides durable authority enrollment storage.
AR-1363, AR-1368, AR-1390, and AR-1391 remain blocked predecessors and must not
be marked complete by this successor alone.

## Required work

- Define a bounded, versioned certificate-chain record rooted in the
  runtime/control trust boundary, with freshness, generation, revocation,
  target/tool/lease/relay binding, and audience checks.
- Materialize and persist only digest/opaque-handle evidence publicly; keep
  credential values and private paths inside the runtime-owned authority
  boundary.
- Reject forged, stale, replayed, revoked, mismatched, alternate-egress, and
  caller-supplied authority records. Ensure generation fencing and teardown
  authority survive restart and cancellation.
- Expose the smallest runtime-owned source needed by downstream receipt and
  live-dispatch consumers, with positive and negative local/mock tests. Live
  providers are optional supplementary evidence and never a CI or completion
  requirement.
- Update schemas and documentation, run focused and full locked gates, and
  publish through signed+DCO review, exact-head CI, normal merge, and all
  post-merge workflows.

## Boundaries

No asb-tui changes, no credentials or live-provider dependency, no caller-built
authority, no weakening of privacy/egress/lifecycle/formal gates, and no edits
to `handoffctl`.
