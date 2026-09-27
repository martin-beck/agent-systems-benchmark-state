# AR-1472 — Authenticated live-dispatch adapter

## Objective

Provide the missing cross-crate adapter that obtains authenticated control
receipts and constructs the runtime-owned live dispatch source. This successor
breaks the AR-1374/AR-1375 dependency cycle without synthesizing authority.

## Dependencies

- AR-1373 (done)
- AR-1363 (done)

## Scope and gates

Implement only the control-to-runtime adapter and its positive/negative local
mock tests. Preserve fail-closed target, tool, lease, relay, nonce, teardown,
and egress policy checks. No asb-tui changes and no live-provider requirement;
CI must use deterministic local/mock or replay evidence. Use signed+DCO
commits, exact-head review, all required checks, normal merge, and post-merge
verification through handoffctl.
