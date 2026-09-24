---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-24T21:38:31+00:00",
  "depends_on": [
    "AR-1316"
  ],
  "id": "AR-1422",
  "next_action": "Promote and claim with a coordinator worker; verify PR #306 is a stale duplicate of current main, record exact evidence, comment, and close it as superseded without merging.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "0000000000000000000000000000000000000000",
  "owner": "open-pr-triage-luna56",
  "plan": "../plans/AR-1422.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Close stale conflicting agent-catalog PR #306 through durable coordinator evidence.",
  "task_revision": 4,
  "title": "Stale agent-catalog PR cleanup",
  "updated_at": "2026-09-24T19:38:31+00:00",
  "worktree_key": ""
}
---

This task has no product implementation scope. It exists to make the stale PR
disposition auditable and to prevent a duplicate branch from remaining open.


- 2026-09-24T19:37:32+00:00: AR-1316 is terminal done; PR #306 is independently confirmed
  conflicting and stale. Open bounded closure task without product mutation.

- 2026-09-24T19:37:54+00:00: Claimed by open-pr-triage-luna56.

- 2026-09-24T19:38:31+00:00: Heartbeat by open-pr-triage-luna56.
