# AR-1503: Runtime/control process owner

## Objective

Implement the runtime/platform-owned process owner missing after AR-1502. It
must establish an authenticated local control session, enroll a source-issued
certificate chain, retain private authority inputs behind the runtime resolver,
mint one opaque AR-1480 dispatch source, and bind cancellation and teardown.

## Dependencies

AR-1473, AR-1474, AR-1480, AR-1484, AR-1485, and AR-1502 are complete. AR-1483
is the blocked audit that identifies this precise gap. Do not revive AR-1374,
AR-1375, or any caller/config/endpoint authority path.

## Acceptance

- Only a runtime/platform-owned launcher constructs the authenticated control
  session and source-issued chain; caller, CLI, config, environment, endpoint,
  credential, policy, root, tool, namespace, and launch-token inputs cannot
  construct or replace the owner.
- The owner validates receipt, generation, nonce, chain, expiry, revocation,
  private resolver state, and restart fences before minting the opaque source.
- Cancellation, disconnect, expiry, revocation, and teardown revoke the chain
  and private resolver before any later issuance; failures are bounded and
  fail closed.
- Deterministic local/mock and strict-replay tests cover success, restart,
  hostile receipt/chain, unavailable control state, cancellation, and teardown.
  No live provider, network, credentials, synthetic production authority, or
  asb-tui changes are allowed.
- Signed/DCO implementation, independent review, exact-head CI, protected
  merge, eight post-merge workflows, and durable release evidence are required.

## Implementation boundary

Do not expose a public constructor that accepts a socket path, ControlClient,
certificate authority, chain, policy, roots, tools, or launch input. If the
runtime/platform-owned launcher is still unavailable, record the exact missing
platform seam and leave this task blocked rather than fabricating authority.
