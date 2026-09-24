# AR-1378: Authenticated live control adapter

## Objective

Connect the authenticated `ControlClient` RuntimeReceipt operation and the
runtime-owned certificate-chain store to the live-provider bridge. The adapter
must return only validated enrollment records/opaque runtime handles and keep
CLI callers away from chain, lease, relay, namespace, and credential authority.

## Dependencies

AR-1377, AR-1366, AR-1364, and AR-1362 are done. AR-1376 remains blocked audit
evidence and is intentionally not a dependency.

## Acceptance

- authenticated control response and stored opaque chain are bound before use;
- wrong result, unavailable chain, transport failure, replay, mismatch, expiry,
  revoke, and teardown fail closed;
- run/sweep bridge integration tests and privacy checks pass;
- signed/DCO, focused/full, exact-head, review, merge, and post-merge gates pass.

