# AR-1375: Runtime-owned live control dispatch source

## Objective

Provide the missing runtime-owned adapter that obtains an authenticated
`RuntimeReceipt` response and certificate chain for the CLI run/sweep bridge.
The adapter must own the control transport, chain material, replay/expiry
checks, and teardown; CLI callers receive only an opaque attempt factory.

## Dependencies

AR-1373 and AR-1374.

## Acceptance

- no public caller can construct provider authority or inject a receipt/chain;
- authenticated control transport and runtime bridge are wired to the live
  attempt factory;
- replay, nonce/provider/generation mismatch, offline, expiry, revoke, and
  teardown fail closed with bounded privacy-safe evidence;
- focused/full gates, signed+DCO, exact-head CI, review, merge, and postmerge
  workflows pass.

