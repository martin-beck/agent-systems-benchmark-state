---
{
  "branch": "feature/ar-1443-guided-benchmark-capture-comparison",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1442", "AR-1332", "AR-1333", "AR-1437"],
  "id": "AR-1443",
  "title": "Guided benchmark capture and comparison",
  "next_action": "Promote after dependencies are done; implement the selection-driven benchmark, capture/replay, and comparison journey over the existing campaign contracts.",
  "owner": "",
  "plan": "../plans/AR-1443.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Make benchmark, offline capture/replay, and result comparison a single guided workflow.",
  "task_revision": 1,
  "updated_at": "2026-09-25T15:40:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1443-guided-benchmark-capture-comparison"
}
---

This AR owns the user-visible workflow composition, not a replacement campaign
engine. All live execution remains runtime-owned and all offline execution must
be independently identifiable as replay.
