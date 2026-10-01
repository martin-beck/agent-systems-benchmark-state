# AR-1574 — ASB development control transport wiring

## Scope

Wire the ASB development launch to the producer control bridge and inherited
asb-tui broker stream after AR-1573.

## Acceptance

- Valid exact-head development launch completes broker negotiation and returns
  a bounded result.
- Descriptor, packet, generation, protocol, and identities are all bound.
- Child and channel cleanup is deterministic under success, timeout, and
  failure.
- Stable/non-development launches remain unchanged.
- Exact-head cross-project tests pass without credentials.

## Boundaries

Development/mock only; missing authentication, signatures, and key management
must not block the prototype.
