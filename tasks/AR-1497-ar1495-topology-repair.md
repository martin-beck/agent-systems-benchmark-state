---
{
  "branch": "repair/ar-1495-topology",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1493"
  ],
  "id": "AR-1497",
  "next_action": "Promote and claim AR-1497, inspect protected-main topology, and construct the smallest signed+DCO repair preserving the AR-1495 tree.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1497-ar1495-topology-repair.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "open",
  "summary": "Repair AR-1495 protected-main synchronization topology without changing product semantics.",
  "task_revision": 2,
  "title": "AR-1495 protected-main topology repair",
  "updated_at": "2026-09-28T13:37:15+00:00",
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
