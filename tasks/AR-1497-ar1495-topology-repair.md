---
{
  "branch": "repair/ar-1495-topology",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-28T15:37:28+00:00",
  "depends_on": [
    "AR-1493"
  ],
  "id": "AR-1497",
  "next_action": "Promote and claim AR-1497, inspect protected-main topology, and construct the smallest signed+DCO repair preserving the AR-1495 tree.",
  "observed_branch": "repair/ar-1495-topology",
  "observed_dirty": 0,
  "observed_head": "6db0d3cdf5c5e5961b61c7a262d90a63763ac4ef",
  "owner": "ar1332-record-replay-luna56",
  "plan": "../plans/AR-1497-ar1495-topology-repair.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Repair AR-1495 protected-main synchronization topology without changing product semantics.",
  "task_revision": 9,
  "title": "AR-1495 protected-main topology repair",
  "updated_at": "2026-09-28T13:38:54+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1497-ar1495-topology-repair"
}
---

AR-1496 is already occupied by an unrelated provider-capture worker. This
successor preserves AR-1495's merged implementation and repairs only the
protected-main topology failure reported by Repository Quality.

The repair must not alter the unsigned-development verifier semantics, the
production/default signature-required boundary, or AR-1490's external signed
customer-release gate. It must use a clean isolated worktree, signed+DCO
history, normal two-parent protected merge, exact-head CI, and all eight
post-merge workflows.

- 2026-09-28: Created because AR-1495 merge 03d2d070 was rejected by
  Repository Quality: protected-main topic synchronization merge must be at
  the tip. AR-1495 behavior remains merged and unchanged.

- 2026-09-28T13:37:15+00:00: AR-1496 is occupied by unrelated provider capture; AR-1497 is narrow
  topology-only repair for AR-1495 protected-main policy failure and preserves AR-1495 evidence
  without product changes.

- 2026-09-28T13:37:24+00:00: Claimed by ar1332-record-replay-luna56.

- 2026-09-28T13:37:28+00:00: Heartbeat by ar1332-record-replay-luna56.

- 2026-09-28T13:37:52+00:00: Recorded command exit 0; command argv SHA-256
  fe520199f971edc0f636e18c09ee56142b7bd8b1991a8efc54489eb95766b2d9.

- 2026-09-28T13:38:33+00:00: Recorded command exit 0; command argv SHA-256
  5b07b489a3267c59a24a067bbd68b7a3ca26e6abd841f40f73ba1c312e80ae3d.

- 2026-09-28T13:38:54+00:00: Recorded command exit 0; command argv SHA-256
  708d0efba8b908587b7d69ddfe22df394cb4e60ce44dcf08beb6301bced2fb6c.
