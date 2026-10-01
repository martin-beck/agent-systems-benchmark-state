# AR-1570 — ASB dynamic development broker handoff

## Scope

Complete the ASB-side launch integration against the dynamic asb-tui broker
entrypoint after identity propagation is available.

## Acceptance

- Exact current ASB/asb-tui identities are passed in a bounded descriptor.
- `run --broker --development` is invoked for development launch and its typed
  result is handled without bypassing the broker.
- Stale, malformed, unsupported, and missing descriptors fail closed.
- Stable launch path and existing non-development behavior are unchanged.
- Exact-head cross-repository integration tests and hosted checks pass.

## Boundaries

Development/mock only. Missing authentication, signatures, and key management
must not block this prototype.
