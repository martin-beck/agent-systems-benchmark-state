# AR-1364: Authenticated chain enrollment

## Objective

Provide the control/runtime-owned authenticated certificate-chain enrollment
source required to issue `RuntimeEnrollmentReceiptV1`. The chain must come from
validated enrollment/attestation state, not be synthesized from CLI/config
digests.

## Dependencies

Depends on AR-1362. AR-1363 remains blocked until this chain source exists;
AR-1360 and AR-1329 remain fail-closed.

## Required work

- Define a bounded durable chain enrollment record with validated identity,
  trust-anchor binding, endpoint binding, generation/revocation state, and no
  private key or certificate bytes in public state.
- Add authenticated control-side enrollment/materialization and generation
  fencing; reject missing, tampered, expired, revoked, mismatched, or replayed
  chains.
- Connect the resulting opaque chain authority to the AR-1362 enrollment and
  AR-1363 receipt source without exposing constructors to CLI callers.
- Add persistence/recovery, positive/negative tamper and revocation tests,
  schemas/docs, and privacy checks.

## Acceptance

Focused/full gates, signed+DCO exact-head PR, independent review, protected
merge, and all seven post-merge workflows pass. Only then resume AR-1363 and
AR-1360; do not advance AR-1329 before exact evidence is durable.

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
