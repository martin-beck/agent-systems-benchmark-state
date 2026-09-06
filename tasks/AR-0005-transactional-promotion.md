---
{
  "branch": "feature/transactional-promotion",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-0002",
    "AR-0004"
  ],
  "id": "AR-0005",
  "next_action": "Implement an atomic dependency-aware promote command and concurrency/failure tests.",
  "owner": "",
  "plan": "../plans/AR-0005.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "planned",
  "summary": "Make planned-to-open promotion a transactional handoffctl operation.",
  "task_revision": 1,
  "title": "Add transactional AR promotion",
  "updated_at": "2026-09-06T20:42:00+00:00",
  "worktree_key": "agent-systems-benchmark-state-promotion"
}
---
## AR-0005

Make planned-to-open promotion a transactional handoffctl operation.

A coordinator race demonstrated that manually changing task source while reconcile regenerated public
views could briefly commit inconsistent task and generated state. Preserve that failure as a regression:
promotion must share handoffctl's lock, validation, commit, replication, and recovery boundary.

Implementation has not started. Read the linked plan before claiming.
