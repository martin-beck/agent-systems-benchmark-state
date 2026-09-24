# AR-1433: Runtime mock-attempt backend

## Objective

Provide an explicitly test-only/runtime-mock backend that can exercise the
`asb run` and `asb sweep` scheduler and lifecycle paths against the
deterministic loopback provider mock without manufacturing production live
authority. The backend must preserve the existing `LiveProviderAttempt`
invariants and leave the production public-egress path unchanged.

## Dependencies and boundaries

Depends on AR-1432 and therefore remains blocked until the local mock boundary
is accepted. AR-1329 remains blocked and is not resumed by this repair. The
mock backend may use only an in-process or loopback deterministic server and
must never contact OpenRouter or another external provider. It must not accept
caller-supplied endpoint, credential bytes, namespace, lease, relay, tool,
certificate authority, or launch token. Production `ProviderEgressTarget`
validation and `NetworkPolicy::Deny` behavior remain unchanged.

## Required work

1. Define a runtime-owned mock-attempt type or backend adapter with an explicit
   test/mock marker that cannot be constructed through CLI/config input and
   cannot be converted into production provider authority.
2. Bind one scheduler attempt identity, fixed local model, opaque credential
   reference, bounded request body, and deterministic response digest per
   invocation. Reject replayed, stale, mismatched, oversized, cancelled, and
   revoked attempts without exposing secrets or private paths.
3. Exercise `asb run` and `asb sweep` through the existing scheduler seam,
   including one-attempt-per-admission, cancellation, teardown, failure
   propagation, offline/default denial, direct/alternate-egress denial, and
   external-target rejection.
4. Add positive and hostile unit/integration tests, run focused and full
   applicable gates, obtain independent review, and publish only a signed+DCO
   exact-head PR. External provider access is neither required nor evidence.

## Acceptance

The local mock completes bounded run/sweep fixture journeys only through an
explicit runtime mock API; no mock object is accepted by production live
authority constructors. All existing egress, namespace, credential, lease,
relay, replay, and offline gates remain green, and evidence contains no
credentials, prompts, response bodies, private paths, or external-provider
claims.
