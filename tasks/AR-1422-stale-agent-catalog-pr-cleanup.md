---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1316"
  ],
  "id": "AR-1422",
  "next_action": "Promote and claim with a coordinator worker; verify PR #306 is a stale duplicate of current main, record exact evidence, comment, and close it as superseded without merging.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "0000000000000000000000000000000000000000",
  "owner": "",
  "plan": "../plans/AR-1422.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "planned",
  "summary": "Close stale conflicting agent-catalog PR #306 through durable coordinator evidence.",
  "title": "Stale agent-catalog PR cleanup",
  "task_revision": 1,
  "updated_at": "2026-09-24T19:40:00+00:00",
  "worktree_key": ""
}
---

This task has no product implementation scope. It exists to make the stale PR
disposition auditable and to prevent a duplicate branch from remaining open.

