# AR-1343: Runtime live-provider relay service and CLI acquisition

## Outcome

Provide the missing runtime-owned live-provider relay service and per-attempt
factory acquisition path needed by `asb run --live-provider` and
`asb sweep --live-provider`. The service must resolve only enrolled credential
references, authorize one concrete provider target through the runtime egress
policy, bind the relay to the runtime-observed child namespace, and return an
opaque one-shot `LiveLaunchContext` consumable by the CLI.

## Dependencies and ownership

Dependencies: AR-1327, AR-1328, AR-1339, and AR-1340. AR-1329 consumes this
repair and is deliberately not a dependency. Owned paths are the runtime live
relay protocol/backend, runtime factory acquisition API, and CLI integration
fixtures. Do not change asb-tui, weaken `NetworkPolicy::Deny`, expose
credentials, or add host-network/direct-provider fallback.

## Required work

1. Define a bounded authenticated child-to-relay request protocol and
   runtime-owned listener/proxy that uses `ProviderEgressAuthorization` and an
   exact concrete allowlist; deny direct and alternate egress.
2. Add a per-attempt runtime factory API that obtains the enrolled credential
   only at the final transport boundary, attests the child namespace, pins the
   live-launch gate executable, and issues `LiveLaunchAuthority` without
   caller-controlled endpoint, namespace, or secret fields.
3. Wire CLI run and sweep live attempts to consume one opaque context per
   attempt, revoke and tear down it on cancellation, and retain offline/replay
   behavior unchanged.
4. Add positive synthetic relay execution tests and negative tests for missing,
   stale, copied, expired, endpoint-mismatched, direct/alternate-egress,
   credential-disclosing, cancellation, and teardown contexts.

## Acceptance criteria

Only runtime-issued namespace-attested contexts can enable live provider
execution. Offline and replay paths remain network-denied and credential-free.
All focused/full quality gates, independent review, exact-head CI, and
post-merge workflows are green.

## Current development and CI qualification boundary

The mandatory development and CI qualification path for this AR is a deterministic
local provider/LLM mock (LiteLLM-compatible where practical), including hostile
negative tests and offline replay where applicable. External/live OpenRouter or
other provider reachability is optional supplementary evidence only; it is never a
completion, dependency-readiness, or CI gate. Production egress policy, credential
non-disclosure, runtime-owned authority, namespace/relay attestation, cancellation
and teardown, and fail-closed denial of unapproved external traffic remain required
contracts. Existing live-provider dependency edges describe production integration
ordering only and must not be used to block local qualification or to claim external
reachability.
