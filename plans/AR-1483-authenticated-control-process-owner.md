# AR-1483: Authenticated control process owner

## Objective

Add the runtime-owned process owner that holds the authenticated control
session, certificate-chain store, authority-input resolver, and lifecycle
teardown binding needed to mint the opaque dispatch source for normal CLI
`run` and `sweep`. The owner is the only component allowed to compose these
private inputs; the CLI receives only a one-shot opaque source.

## Dependencies

AR-1472, AR-1473, and AR-1480 are complete. AR-1481 and AR-1482 document the
missing process owner. Do not depend on or revive AR-1374 or AR-1375.

## Acceptance

- A runtime/control-owned owner constructs from an authenticated local control
  session and enrolled chain, requests a bounded receipt, resolves private
  launch inputs, mints an opaque source, and binds cancellation/teardown.
- No caller, CLI flag, config, environment, endpoint, credential, policy,
  root, tool, namespace, or launch-token input can construct or replace it.
- Missing, stale, revoked, malformed, mismatched, replayed, disconnected, or
  unavailable control state fails closed before launch/network effects.
- Deterministic local/mock/replay tests cover success, restart, cancellation,
  teardown, hostile receipts, and unavailable control state; no live provider,
  network, credentials, synthetic authority, or asb-tui.
- Signed/DCO PR, exact-head CI, normal merge, eight post-merge workflows, and
  durable evidence are required.

