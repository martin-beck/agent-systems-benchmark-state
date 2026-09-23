# AR-1351: Runtime-owned live provisioning

## Objective

Provide the private host/runtime provisioning seam required by AR-1349 to
construct a pinned `SandboxBackend` and live launch gate, authenticated
`ProviderEgressPolicy`/handoff, observed namespace identity, and bounded relay
inputs without caller-built authority.

## Dependencies

Depends on completed AR-1339, AR-1340, AR-1347, and AR-1350. AR-1349 and
AR-1329 are downstream consumers. Do not modify asb-tui.

## Required work

Implement one runtime-owned provisioning service with fail-closed discovery and
rollback. It must reject missing or unpinned tools, alternate egress, stale
policy/handoff, unobserved namespaces, and copied authority; provide positive
synthetic tests and negative lifecycle/teardown tests. Expose only the opaque
inputs needed by AR-1349's acquisition coordinator; never expose credentials,
host paths, raw output, or authority internals to CLI callers.

## Acceptance

AR-1349 can atomically compose lease, backend/gate, namespace, token, relay,
sealed credential channel, and opaque attempt from this service. All focused
and full gates, review, exact-head CI, and post-merge checks pass before
AR-1329 is enabled.
