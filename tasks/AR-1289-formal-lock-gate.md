---
{
  "branch": "fix/ar-1289-formal-lock-gate",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [],
  "id": "AR-1289",
  "next_action": "Promote and claim; reproduce formal/Cargo.lock failure on protected main, determine exact lock drift, and repair the smallest ASB formal gate scope.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "2fd90557a4e7be32fab590f47bc501462127c1c1",
  "owner": "",
  "plan": "../plans/AR-1289.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "open",
  "summary": "Repair the stale formal Cargo.lock required by hosted exact-head gates.",
  "task_revision": 2,
  "title": "Repair formal lock gate",
  "updated_at": "2026-09-17T03:12:39+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1289-formal-lock-gate"
}
---

## AR-1289

The required formal workflow currently fails before model tests because `formal/Cargo.lock` cannot
be used with `--locked`. Repair and verify this gate independently of feature ARs.

- 2026-09-17T03:12:39+00:00: Hosted exact-head formal job fails because formal/Cargo.lock is stale
  under --locked; repair independently of certificate feature.
