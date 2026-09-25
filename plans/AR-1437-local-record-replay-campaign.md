# AR-1437: Local record/replay campaign qualification

## Objective

Extend the completed local guided wrapper with deterministic record/replay and
multi-agent campaign qualification over the runtime-owned mock. This is an
offline fixture path only; it must not activate or depend on live provider
capture, launch, or replay authorities.

## Dependencies and boundaries

Completion dependencies are AR-1436 and AR-1328. AR-1330, AR-1331, AR-1332,
and AR-1333 are future/live integration references only and must remain
planned or blocked; AR-1329 and AR-1338 are not resumed. No external provider,
OpenRouter endpoint, credential bytes, caller endpoint, relay, namespace,
lease, or live `LiveProviderAttempt` may be used.

The local path must use the deterministic `LocalProviderMockBackend` through
the existing guided/config contracts. Production egress and authority gates,
default denial, cancellation, revocation, and offline replay boundaries must
remain unchanged.

## Required work

1. Add an explicit local qualification mode for bounded record/replay or a
   campaign matrix over supported agents/workloads, reusing the guided wrapper
   and authoritative catalog/config identities.
2. Persist only bounded digest evidence and typed outcomes; reject unknown or
   credential-bearing fields, external targets, live mode, duplicate tuples,
   stale selections, and unsealed or mismatched replay evidence.
3. Add positive and hostile offline tests for one local record/replay journey,
   repeated multi-agent/workload tuples, cancellation/revocation, replay
   without provider fallback, and privacy/retention bounds.
4. Update generated documentation/examples and run focused/full offline gates,
   independent exact-diff review, signed+DCO PR checks, exact-head merge, and
   all seven exact-main post-merge workflows.

## Acceptance

The explicit local qualification command produces deterministic bounded
digest-only records and replays/campaign results strictly offline. Ordinary,
live, and external-provider paths remain denied. The feature adds no provider
authority or second registry, and all local, PR, and post-merge gates are
green.
