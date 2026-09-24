# AR-1434: Runtime local mock-attempt adapter

## Objective

Implement the narrowly scoped runtime adapter required by the AR-1432 audit:
exercise scheduler run/sweep against the deterministic local provider mock
through an approved mock-attempt/backend type, while preserving all
production `LiveProviderAttempt` and public-egress authority checks.

## Dependencies and evidence

Runtime prerequisites are AR-1341, AR-1342, AR-1385, AR-1388, and AR-1393;
all are complete. AR-1432 is retained as blocker evidence and is intentionally
not a completion dependency because it is blocked on this exact repair.
AR-1329 and AR-1432 remain blocked and must not be resumed or marked done by
this task. AR-1433 is the earlier planned repair record and remains evidence
only unless separately promoted after its dependency transition.

## Required work

1. Define a runtime-owned, explicitly mock-only attempt/backend adapter. It
   must be impossible to construct from CLI/config authority and impossible to
   pass into production live authority constructors as a real provider attempt.
2. Bind one scheduler attempt identity, the fixed local model, opaque
   credential reference, bounded request, and deterministic response digest.
   Reject replay, stale/revoked/mismatched/oversized/cancelled attempts.
3. Run `asb run` and `asb sweep` through the existing scheduler seam using only
   the mock adapter. Prove one attempt per admission, teardown, cancellation,
   failure propagation, offline/default denial, direct/alternate-egress
   denial, and external-target rejection.
4. Add positive and hostile tests, run focused/full applicable gates, obtain
   independent review, and publish only signed+DCO exact-head changes. No
   external provider connection is required or permitted for qualification.

## Acceptance

The mock journey is bounded, deterministic, local-only, and produces no
credential, prompt, response-body, private-path, or external-provider
evidence. Existing `ProviderEgressTarget`, `NetworkPolicy::Deny`, namespace,
lease, relay, credential, replay, and offline gates remain unchanged and
green.
