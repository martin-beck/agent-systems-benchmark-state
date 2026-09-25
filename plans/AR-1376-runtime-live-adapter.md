# AR-1376: Runtime-owned live adapter

## Objective

Build the runtime-owned adapter that turns the authenticated AR-1373 control
receipt operation and completed runtime authority primitives into the opaque
`LiveProviderAttemptFactory` consumed by `asb run`/`asb sweep`. The CLI must not
construct or receive provider authority, chain material, credentials, relay
roots, leases, or namespace identities.

## Dependencies

AR-1373, AR-1366, AR-1364, and AR-1362 are done. AR-1374/1375 audit evidence
identified the missing source but are not dependencies because they are blocked.

## Acceptance

- runtime-owned control client obtains and validates receipt plus chain;
- bridge issues only opaque, one-shot live attempts with provider/generation/
  nonce/lease/relay/namespace binding;
- replay, mismatch, expiry, revocation, offline, and teardown fail closed;
- positive/negative cross-crate tests, privacy checks, signed+DCO, full gates,
  exact-head CI, review, merge, and post-merge workflows pass.

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
