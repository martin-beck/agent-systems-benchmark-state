# AR-1381: Runtime-owned live CLI scheduler wiring

## Objective

Wire the runtime-owned scheduler composition seam into production `asb run`
and `asb sweep` without exposing provider, credential, namespace, lease,
relay, backend, or endpoint authority to CLI callers.

## Dependencies

AR-1380, AR-1378, AR-1377, AR-1373, AR-1366, AR-1364, and AR-1362 are done.
Historical blocked AR-1374/1376/1379 evidence remains preserved and is not a
dependency.

## Acceptance

- run and sweep consume only runtime-issued opaque factories;
- missing authority, provider mismatch, replay, expiry, cancellation, teardown,
  and NetworkPolicy::Deny failures are fail-closed;
- no secrets, private paths, or caller-supplied authority enter CLI output;
- focused, full, exact-head, and post-merge gates pass.

