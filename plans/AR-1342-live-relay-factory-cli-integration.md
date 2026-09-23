# AR-1342: Runtime-owned live relay factory and CLI launch context

## Outcome

Provide the missing runtime-owned factory that creates a validated,
namespace-bound live-provider relay and launch context for `asb-cli`. The CLI
must never construct a relay from caller-controlled endpoint, namespace, or
credential data. Offline and replay paths remain denied by default.

## Dependencies and ownership

Dependencies: AR-1327/AR-1328 (provider selection and credential-free
configuration), AR-1339 (runtime-owned provider-egress backend), and AR-1340
(attested child namespace handoff). AR-1329 consumes this repair after its
typed live run/sweep contract is available; it is deliberately not a
dependency, avoiding a cycle.
Owned paths are the runtime launch-context/factory, CLI run and sweep wiring,
and focused denial/integration tests. Do not change asb-tui, weaken
`NetworkPolicy::Deny`, expose credentials, or add host-network fallback.

## Work sequence

1. Define a runtime-issued factory input containing only enrolled provider
   profile identity, route/adapter digests, credential reference, deadline,
   and the authorized relay endpoint.
2. Construct the relay/backend and `SandboxBackend` inside the runtime, bind it
   to the attested child namespace handoff, and return an opaque launch context
   that the CLI cannot forge or copy across launches.
3. Wire explicit `asb run --live-provider` and `sweep --live-provider` to this
   factory; preserve strict offline, replay, and missing-context denial before
   any provider effect.
4. Add positive synthetic relay execution tests plus negative tests for missing,
   stale, copied, endpoint-mismatched, expired, and credential-disclosing
   contexts, including cancellation and restart reconciliation.
5. Run focused and full applicable gates, independent review, exact-head CI,
   and post-merge verification.

## Acceptance criteria

Only a runtime-issued, namespace-attested launch context can enable live
provider execution. The CLI has no direct relay/socket construction path;
offline and replay behavior remains unchanged and network-denied. All required
quality, formal, fault, portability, and exact-head checks are green.
