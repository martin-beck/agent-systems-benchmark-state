---
{
  "branch": "feature/ar-1365-control-receipt-source-integration",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1362",
    "AR-1364"
  ],
  "id": "AR-1365",
  "next_action": "Promote after AR-1362 and AR-1364 are done, then integrate authenticated chain and authority enrollment into the versioned control receipt source.",
  "observed_branch": "feature/ar-1365-control-receipt-source-integration",
  "observed_dirty": 0,
  "observed_head": "3a4007be828db04f3b57492e5c5f230199cb8d5a",
  "owner": "",
  "plan": "../plans/AR-1365-control-receipt-source-integration.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Integrate authenticated chain and authority enrollment into the versioned control receipt source.",
  "task_revision": 1,
  "title": "Control receipt source integration",
  "updated_at": "2026-09-24T00:00:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1365-control-receipt-source-integration"
}
---

Successor for blocked AR-1363, explicitly depending on completed AR-1362 and
AR-1364. Do not touch asb-tui or synthesize authority from CLI/config input.

- 2026-09-24T00:00:00+00:00: Created after AR-1364 supplied authenticated
  chain enrollment materialization and all post-merge workflows passed.
