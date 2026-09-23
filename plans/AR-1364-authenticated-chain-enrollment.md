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
