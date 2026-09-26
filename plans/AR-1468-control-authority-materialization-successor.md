# AR-1468: control authority materialization successor

## Objective

Implement the concrete RunnerBackend/Catalog authority boundary identified by
AR-1369/AR-1370, with dependency edges that point only to completed authority
foundations. This successor removes the superseded-task dependency deadlock; it
does not rewrite or claim the historical audits.

## Dependencies and boundaries

Depends on AR-1288, AR-1362, AR-1364, and AR-1366, all of which are complete.
Use the existing authenticated certificate issuer and receipt materializer;
never synthesize trust or launch authority from CLI/config/environment input.
Do not touch asb-tui, require a live provider, use the AR-1308 seed, or weaken
NetworkPolicy::Deny, lease, relay, namespace, teardown, or privacy gates.

## Required work

- Add owner-checked, bounded control/runtime injection of authenticated chain,
  target allowlist, tool pin, lease/relay roots, generation, expiry, revocation,
  namespace and teardown authority into RunnerBackend/Catalog.
- Issue only digest-safe RuntimeReceiptResponseV1 projections; keep credentials,
  private paths, certificate bytes and launch authority private.
- Add positive, tamper, stale, revoked, replay, restart, peer-identity,
  cancellation, teardown and alternate-egress tests using local deterministic
  mocks.

## Acceptance

Signed+DCO implementation, focused/full gates, independent review, exact-head
CI, protected merge, seven post-merge workflows, and durable handoff evidence
must pass before AR-1392/1391/1390 advance.
