---
{
  "branch": "feature/ar-1509-authenticated-authority-provider-receipt",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-29T04:34:45+00:00",
  "depends_on": [
    "AR-1473",
    "AR-1474",
    "AR-1480",
    "AR-1484",
    "AR-1485",
    "AR-1502",
    "AR-1505"
  ],
  "id": "AR-1509",
  "next_action": "Promote after dependency verification; implement a real runtime-owned authority-provider receipt, independent claim verification, and post-materialization lifecycle fencing.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "ar1509-receipt-luna56",
  "plan": "../plans/AR-1509-authenticated-authority-provider-receipt.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Replace the AR-1508 test fa\u00e7ade with an authenticated production authority-provider receipt and lifecycle fence.",
  "task_revision": 3,
  "title": "Authenticated authority-provider receipt",
  "updated_at": "2026-09-29T02:34:45+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1509-authenticated-authority-provider-receipt"
}
---

AR-1508 established the intended private provider boundary but independent
review found it is only a test façade. This AR owns the concrete production
contract required before the launcher can serve first-customer workloads.

Acceptance requires:

- a non-test runtime/control provider implementation that obtains private
  roots, namespace, tools, policy, credential capability, and enrollment/receipt
  material from an authenticated platform source;
- a signed/attested provider receipt or equivalent independently verifiable
  binding that proves endpoint identity, namespace, lease/relay roots, tool
  bundle, policy/allowlist, credential reference, generation, restart,
  cancellation, and expiry claims—not merely a provider-selected digest;
- runtime materialization and ordinary CLI dispatch consume only this provider
  receipt; no caller/config/PATH/fixed-path/synthetic authority injection;
- expiry, revocation, cancellation, restart, teardown, and alternate-egress
  fences remain active after materialization, with deterministic provider-free
  tests for every negative path;
- independent exact-head review, SSH-signed DCO, hosted checks, protected
  merge, and terminal post-merge assurance.

Non-goals: asb-tui, live provider reachability, public credentials, fixed or
mock production authority, or weakening formal/privacy/native gates.

- 2026-09-29T04:33:00+02:00: Created from independent AR-1508 P1/P2 review.
  Its signed local commits remain unmerged evidence only.

- 2026-09-29T02:32:37+00:00: Dependencies through AR-1505 verified done; AR-1508 review established
  the need for an independently verifiable production provider receipt and lifecycle fence.

- 2026-09-29T02:34:45+00:00: Claimed by ar1509-receipt-luna56.
