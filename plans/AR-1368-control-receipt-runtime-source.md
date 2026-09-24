# AR-1368: Control receipt runtime source

## Objective

Add the authenticated control/runtime source that materializes a
`RuntimeReceiptRequestV1`/`RuntimeReceiptResponseV1` for production live
dispatch. The source must be reachable only through the owner-authenticated
control boundary and must return validated runtime-owned material, never
credentials, private paths, or caller-provided authority.

## Dependencies

Depends on AR-1366's response consumer and AR-1367's production integration
audit. AR-1329 remains fail-closed until this source exists and is consumed by
the runtime-owned `LiveProviderRuntimeService`.

## Required work

- Add a versioned control operation and `ControlClient` path for a bounded
  receipt request, bound to provider, generation, nonce, enrolled chain, and
  revocation state.
- Materialize the response only from control-owned enrollment records and
  authenticated chain state; reject forged, stale, replayed, mismatched,
  unknown-field, and unauthorized peer requests.
- Keep wire payloads credential-free and path-free; return only opaque or
  digest-based runtime metadata needed by the private consumer.
- Connect the runtime source to AR-1367's run/sweep factory without exposing
  constructors or endpoint/lease/relay/namespace authority to CLI/config.
- Add positive, tamper, replay, peer-identity, lifecycle, and cancellation
  tests plus schema/docs updates.

## Acceptance

Focused/full gates, independent review, signed+DCO exact-head PR, all required
CI, protected merge, and all seven post-merge workflows pass before AR-1367 or
AR-1329 may advance.
