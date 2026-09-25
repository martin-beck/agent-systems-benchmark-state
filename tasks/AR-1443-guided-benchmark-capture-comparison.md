---
{
  "branch": "main",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-25T16:32:47+00:00",
  "depends_on": [
    "AR-1442",
    "AR-1447",
    "AR-1437"
  ],
  "id": "AR-1443",
  "next_action": "Promote after AR-1442, AR-1447 and AR-1437 are released; implement and qualify the ASB-only selection-driven benchmark, local capture/replay, and comparison journey. Optional live capture AR-1332/AR-1333 remains separate.",
  "observed_branch": "main",
  "observed_dirty": 7,
  "observed_head": "bd7d10d4a760a84fa42de2b1fa9e97e8ea85ba09",
  "owner": "coordinator-ar1443",
  "plan": "../plans/AR-1443.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Make benchmark, offline capture/replay, and result comparison a single guided workflow.",
  "task_revision": 5,
  "title": "Guided benchmark capture and comparison",
  "updated_at": "2026-09-25T15:34:07+00:00",
  "worktree_key": "agent-systems-benchmark"
}
---

This AR owns the user-visible workflow composition, not a replacement campaign
engine. All live execution remains runtime-owned and all offline execution must
be independently identifiable as replay.

- 2026-09-25T15:32:35+00:00: Dependencies AR-1442, AR-1447, and AR-1437 are done; promote ASB-only
  guided capture/replay/comparison qualification. Optional live capture remains separate.

- 2026-09-25T15:32:47+00:00: Claimed by coordinator-ar1443.

- 2026-09-25T15:33:55+00:00: Recorded command exit 0; command argv SHA-256
  732f90ed0f523aee0478a418c338d1238c21c4ba977cf6d7d7b4ae2d231c6398.
