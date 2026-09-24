# AR-1380: Runtime scheduler composition for live dispatch

## Objective

Expose a runtime-owned scheduler composition seam that receives authenticated
receipt records and constructs the opaque `LiveProviderAttemptFactory` only
after binding launch input, lease, relay, namespace, credential channel,
NetworkPolicy, cancellation, and teardown. CLI must never receive authority.

## Dependencies

AR-1378, AR-1377, AR-1366, AR-1364, and AR-1362 are done. AR-1379 remains an
audit record and is not a dependency.

## Acceptance

- per-attempt runtime inputs are composed inside the runtime, not CLI;
- provider mismatch, replay, expiry, cancellation, offline/network deny, and
  teardown fail closed;
- run and sweep positive/negative integration tests pass with full gates.

