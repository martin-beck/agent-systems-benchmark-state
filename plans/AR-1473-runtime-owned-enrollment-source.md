# AR-1473: Runtime-owned authenticated enrollment source

## Objective

Provide the missing runtime/control-owned enrollment operation that turns a
validated control enrollment into an opaque runtime authority source for the
normal ASB `run` and `sweep` paths. The source must be created inside the
runtime authority boundary; callers must not supply policy, credentials,
lease/relay roots, tool pins, namespaces, or teardown authority.

## Dependencies

AR-1471 provides authenticated control-to-runtime certificate-chain binding;
AR-1472 provides the authenticated live-dispatch adapter; AR-1379 integrates
that adapter into production `run` and `sweep`. These are prerequisites for
this focused enrollment-source bridge.

## Required work

- Define the smallest versioned runtime-owned enrollment request and response
  needed to resolve a persisted, authenticated chain and authority profile.
- Resolve all policy, target, tool, lease, relay, credential-capability,
  namespace, cancellation, and teardown inputs from runtime/control-owned
  stores only; expose only opaque handles and public digest metadata.
- Bind the resulting source to generation, freshness, revocation, audience,
  target/tool, alternate-egress, and cancellation checks. Reject forged,
  stale, replayed, mismatched, caller-supplied, and incomplete authority.
- Wire the source into normal CLI `run` and `sweep` while retaining the
  argument-only fail-closed boundary. Add positive and negative local/mock or
  replay tests; live provider access is optional and never a completion gate.
- Update public schemas/docs and run focused, full, formal, privacy, and
  platform gates. Publish only from a clean signed+DCO exact head, merge after
  exact-head CI is green, and verify all post-merge workflows.

## Boundaries

No asb-tui changes, no live-provider or remote credential requirement, no
synthetic authority, no caller-built authority, no private paths or secrets,
no weakening of lifecycle/egress/formal gates, and no edits to `handoffctl`.
