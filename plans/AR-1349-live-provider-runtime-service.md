# AR-1349: Production live-provider runtime service

## Objective

Implement the production-owned `LiveProviderRuntimeService` required by
AR-1329. The service must atomically acquire one bounded live attempt from
validated provider-selection and credential references, then expose only the
opaque `LiveProviderAttempt` consumed by `asb run` and `asb sweep`.

## Dependencies and ownership

This repair depends on the completed OpenRouter prerequisites AR-1327 and
AR-1328, the authenticated egress backend AR-1339, the attested relay and
namespace handoff AR-1340, the neutral composition contract AR-1347, and the
validated lifecycle slice AR-1348. It owns the runtime coordinator and the
single production CLI call site. It must not modify asb-tui.

## Required work

1. Resolve the enrolled provider policy, exact concrete allowlisted target, and
   credential reference without exposing credential bytes or accepting caller
   authority.
2. Discover and pin the approved live gate, construct the denied
   `SandboxLaunchInput`, reserve the benchmark `ResourceLease`, observe the
   child namespace, issue a short-lived launch token and
   `LiveProviderNamespaceHandoff`, and construct the per-attempt
   `LiveProviderRelay` inside one rollback-safe acquisition boundary.
3. Wire `asb run` and `asb sweep` through that service for every admitted
   scheduler attempt, preserving offline/replay defaults and
   `NetworkPolicy::Deny`.
4. Add positive synthetic lifecycle tests and negative tests for missing or
   stale policy, credential, gate, lease, target, namespace, token, relay,
   direct/alternate egress, copied authority, cancellation, timeout, child
   failure, duplicate use and teardown/recovery.
5. Update generated schema/docs only if public contracts change. Never claim
   synthetic provider contact as real execution evidence.

## Acceptance criteria

Only the runtime service can enable live execution. CLI state contains no
authority internals, credentials, host paths or raw subprocess output.
Acquisition rolls back every partially acquired resource, cancellation and
normal completion revoke the namespace/token/relay, and offline/replay remain
credential-free and network-denied. Focused/full gates, independent review,
exact-head CI, protected merge and post-merge evidence are required before
AR-1329 can consume the service.
