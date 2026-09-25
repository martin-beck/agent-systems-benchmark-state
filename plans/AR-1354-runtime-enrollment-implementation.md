# AR-1354: Runtime enrollment implementation

## Objective

Implement the runtime-owned enrollment source consumed by AR-1353. It must
validate pinned OpenRouter installation configuration, resolve concrete enrolled
targets, obtain runner-owned sandbox capability data, and mint only opaque
`LiveProviderRuntimeHandle` values.

## Dependencies

Depends on merged AR-1352 and the AR-1353 opaque enrollment/dispatch seam.
AR-1329 remains fail-closed. Do not modify asb-tui.

## Required work

Add the asb-config -> asb-runtime enrollment implementation with strict schema,
unknown-field rejection, pinned tool identities, exact target allowlisting,
bounded relay root, and rollback-safe bootstrap. No CLI caller may provide
policy, backend, tool paths, relay roots, namespace identities, tokens, or
credentials. Add positive and negative enrollment/dispatch tests, then run
focused/full gates and publish signed+DCO changes.

## Acceptance

AR-1353 can mint an opaque runtime handle from validated installed enrollment and
`asb run`/`asb sweep` can consume it without injected factories, preserving
offline/replay defaults and `NetworkPolicy::Deny`.

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
