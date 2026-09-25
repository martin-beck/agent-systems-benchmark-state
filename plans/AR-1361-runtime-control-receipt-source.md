# AR-1361: Runtime control receipt source

## Objective

Add the missing runtime/control-owned source that delivers an authenticated
`RuntimeEnrollmentReceiptV1` plus validated chain to the runtime, and compose a
per-attempt opaque `LiveProviderAttemptFactory` usable by `asb run` and `asb
sweep`. CLI callers must receive only opaque capabilities and secret-free
outcomes.

## Dependencies

Depends on AR-1359. AR-1360 remains blocked until this source is merged and
verified; AR-1329 remains fail-closed.

## Required work

- Extend the versioned control protocol with a bounded receipt-source operation
  whose server implementation obtains receipt and chain from enrolled,
  runtime-owned state; reject unknown fields, stale/replayed/tampered receipts,
  provider mismatch, and network-policy violations.
- Keep certificate/private bootstrap and policy/tool/lease/relay/namespace
  constructors runtime/control-private; expose no endpoint or credential bytes.
- Add a runtime-owned composition API that turns one authenticated source into
  one opaque attempt per scheduler attempt, including cancellation and teardown.
- Wire a bounded CLI `run`/`sweep` dispatch entrypoint to that opaque factory
  without adding caller authority arguments.
- Add positive and negative cross-crate tests and generated schema/docs updates.

## Acceptance

Focused/full gates, signed+DCO commit, exact-head PR and required CI, protected
merge, and all seven post-merge workflows must pass. Preserve offline/replay
fail-closed behavior and record exact evidence before reopening AR-1360 or
advancing AR-1329.

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
