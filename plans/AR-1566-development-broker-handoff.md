# AR-1566 — ASB development broker handoff integration

## Scope

Wire the ASB development launch path to the standalone asb-tui development
broker descriptor and authenticated `run --broker` entry point.

## Acceptance

- Dev launch invokes the broker handoff with an exact identity-bound descriptor.
- Stale, malformed, unsupported, and missing descriptors fail closed with
  development-only diagnostics.
- Stable launch behavior is unchanged.
- Exact-head cross-repository integration tests pass without credentials.

## Boundaries

Development/mock only. No production authentication or secret-management gate
may block this prototype.

