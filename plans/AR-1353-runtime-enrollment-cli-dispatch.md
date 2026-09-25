# AR-1353: Runtime enrollment and CLI dispatch

## Objective

Provide the safe cross-crate enrollment seam that mints an opaque
`LiveProviderRuntimeHandle` from the merged AR-1352 runtime bootstrap and wires
`asb run`/`asb sweep` without caller-injected attempt factories.

## Dependencies

Depends on merged AR-1352. AR-1349 and AR-1329 are downstream consumers and
remain fail-closed. Do not modify asb-tui.

## Required work

Add a runtime-owned enrollment source/transport carrying no policy, backend,
paths, credentials, or authority internals across the crate boundary. Replace
the production live factory requirement in run/sweep with the opaque handle and
runtime service acquisition. Add positive dispatch and negative tests for
offline/replay, missing enrollment, copied handle, alternate egress, wrong
selection digest, cancellation, and teardown. Run all focused/full gates and
publish only signed+DCO exact-head changes.

## Acceptance

Only runtime enrollment can mint the handle; CLI receives and consumes opaque
per-attempt capabilities, preserving NetworkPolicy::Deny and credential
non-disclosure. AR-1329 can consume the merged result without caller-built
authority.

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
