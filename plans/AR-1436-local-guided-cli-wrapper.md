# AR-1436: Local guided CLI wrapper

## Objective

Add a catalog-driven guided `asb easy` qualification wrapper over the completed
local mock run/sweep path. The wrapper must be deterministic and offline-only;
it must preserve the live-provider path as fail-closed and must not resume
AR-1329 or AR-1338.

## Dependencies and boundaries

Completion dependencies are AR-1435 and AR-1328. AR-1332 and AR-1333 are
future integration references only; they remain planned, and AR-1333 also
reaches the blocked live-provider AR-1329 chain. Do not alter their status or
claim AR-1329/AR-1338.

The wrapper must derive provider/model choices from the authoritative catalog
and config contracts, accept only an explicit local-mock qualification mode,
and delegate execution to the existing `asb run`/`asb sweep --use-config`
paths. It must never contact OpenRouter or another external provider, consume
credential bytes, mint `LiveProviderAttempt`, accept caller endpoints, or
weaken default denial, egress, namespace, lease, or cancellation policy.

## Required work

1. Add the guided wrapper command and stable machine-readable selection flow
   for the local mock fixture, rejecting unknown fields, missing selection,
   external targets, live-provider mode, and ambiguous configuration.
2. Add positive and hostile offline tests covering catalog-derived selection,
   run and sweep delegation, bounded digest evidence, default/live fail-closed
   behavior, cancellation/revocation, and secret/private-output isolation.
3. Update generated documentation and examples without adding runtime
   dependencies or floating versions.
4. Run focused/full offline gates, independent exact-diff review, signed+DCO
   PR checks, exact-head merge, and all seven exact-main post-merge workflows.

## Acceptance

An explicit local qualification invocation completes through the runtime-owned
mock and produces bounded digest-only evidence. Ordinary/default and live or
external-provider invocations remain denied. The wrapper is only a thin,
catalog-driven delegation layer, with no second provider registry or authority
surface, and all applicable gates are green.
