---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-24T17:28:54+00:00",
  "depends_on": [
    "AR-1405"
  ],
  "id": "AR-1406",
  "next_action": "Promote after AR-1405; qualify immutable action commits for PRs #235/#234/#148 and merge only after policy and exact-head gates pass.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "0000000000000000000000000000000000000000",
  "owner": "ar1406-action-pin-luna56",
  "plan": "../plans/AR-1406-action-pin-policy-migration.md",
  "priority": "P2",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Qualify and merge remaining immutable GitHub action pin updates without weakening policy.",
  "task_revision": 4,
  "title": "Action pin policy migration",
  "updated_at": "2026-09-24T15:28:54+00:00",
  "worktree_key": ""
}
---

No floating action reference or unverifiable release identity is acceptable.


- 2026-09-24T15:19:44+00:00: AR-1405 is done; promote immutable action-pin qualification for PRs
  #235, #234, and #148 without weakening policy.

- 2026-09-24T15:28:12+00:00: Claimed by ar1406-action-pin-luna56.

- 2026-09-24T15:28:54+00:00: Heartbeat by ar1406-action-pin-luna56.
