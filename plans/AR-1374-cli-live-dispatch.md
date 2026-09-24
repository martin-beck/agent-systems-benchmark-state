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

