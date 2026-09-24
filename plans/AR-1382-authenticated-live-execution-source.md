# AR-1382: Authenticated live execution source

## Objective

Materialize the runtime-owned live execution source needed by `asb run` and
`asb sweep`: consume an authenticated control receipt and enrolled certificate
chain, construct the private bootstrap inputs inside runtime, and return only
the opaque `LiveProviderRuntimeScheduler`.

## Dependencies

AR-1381, AR-1380, AR-1378, AR-1377, and AR-1373 are done. AR-1329 remains
blocked with its audit evidence preserved.

## Acceptance

- only authenticated control/runtime state can create the scheduler;
- provider, target, credential reference, lease, relay root, namespace,
  backend pins, and NetworkPolicy::Deny are bound inside runtime;
- absent, stale, mismatched, replayed, cancelled, or revoked authority fails
  closed without secrets or private paths;
- focused/full, exact-head, and post-merge gates pass.

