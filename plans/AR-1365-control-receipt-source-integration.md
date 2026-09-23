# AR-1365: Control receipt source integration

## Objective

Integrate the completed AR-1362 authority enrollment and AR-1364 authenticated
chain materialization into a bounded versioned `ControlClient` operation that
issues a `RuntimeEnrollmentReceiptV1` to the runtime-owned consumer.

## Dependencies

Depends on AR-1362 and AR-1364. AR-1363 remains blocked until this integration
is merged; AR-1360 and AR-1329 remain fail-closed.

## Required work

- Add a versioned request/result with strict schema and request binding for one
  provider/generation receipt retrieval.
- Have the runner backend load only durable authority+chain enrollment state,
  enforce revocation/freshness/replay and deadlines, then issue the receipt.
- Return only digest/target metadata and receipt fields; never certificate bytes,
  private keys, credentials, private paths, or runtime constructors.
- Add endpoint/backend/schema positive and negative tests, then connect the
  resulting opaque source to the runtime dispatch consumer in the next AR.

## Acceptance

Focused/full gates, signed+DCO exact-head PR, independent review, protected
merge, and all seven post-merge workflows pass. Record exact evidence before
resuming AR-1363/1360 or advancing AR-1329.
