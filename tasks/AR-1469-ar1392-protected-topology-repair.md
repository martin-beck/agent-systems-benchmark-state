---
{
  "branch": "repair/ar-1469-ar1392-protected-topology-repair",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [],
  "id": "AR-1469",
  "next_action": "Promote and claim the topology repair, create the reviewed two-parent protected merge, and rerun all exact-head and post-merge gates.",
  "owner": "",
  "plan": "../plans/AR-1469-ar1392-protected-topology-repair.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Repair the single-parent protected merge for AR-1392 without changing its reviewed implementation.",
  "task_revision": 1,
  "title": "AR-1392 protected-main topology repair",
  "updated_at": "2026-09-27T00:00:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1469-ar1392-protected-topology-repair"
}
---

This repair is limited to merge topology and exact evidence. It must preserve
the AR-1392 implementation tree, signatures, DCO, privacy boundaries, and all
green exact-head checks; the failed squash topology remains part of the record.
