# AR-1484: Runtime/control process-owner contract

## Objective

Define the stable runtime/control process-owner contract that the missing
bootstrap implementation must satisfy. The owner is responsible for the
authenticated control session, certificate-chain store, private authority
resolver, opaque dispatch-source minting, cancellation, and teardown. The
contract must be implementable independently of any live provider.

## Dependencies

AR-1472, AR-1473, and AR-1480 are complete. AR-1481, AR-1482, and AR-1483
document the missing owner. This design slice excludes stale/circular
AR-1374 and AR-1375.

## Acceptance

- Stable public identifiers define owner identity, enrollment generation,
  receipt nonce, chain digest, lifecycle state, and bounded error classes;
  unknown fields/identifiers fail closed.
- Lifecycle is explicit and bounded: `Prepared -> Enrolled -> Issued`, with
  `Cancelled`, `Revoked`, `Expired`, `Disconnected`, and `TornDown` terminal
  states; only the owner may transition it.
- The contract exposes only an opaque dispatch-source handoff and never
  credentials, endpoints, policy, roots, tools, namespace, or launch tokens.
- Local deterministic mock and strict-replay examples/tests cover positive
  issuance plus stale, replayed, mismatched, unavailable, cancellation, and
  teardown negatives; no network, credentials, live provider, synthetic
  production authority, or asb-tui.
- Documentation and contract tests are reviewed, signed+DCO, and pass exact
  focused/full gates; implementation successors consume these identifiers.

