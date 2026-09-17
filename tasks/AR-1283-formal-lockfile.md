---
{
  "branch": "feature/ar-1283-formal-lockfile",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-0003"],
  "id": "AR-1283",
  "next_action": "Promote after dependency verification; regenerate and verify formal/Cargo.lock so hosted --locked formal tests do not attempt updates.",
  "observed_branch": "feature/ar-1283-formal-lockfile",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1283.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Repair formal workspace lockfile drift that fails the locked CI gate.",
  "title": "Formal lockfile CI drift repair",
  "task_revision": 1,
  "updated_at": "2026-09-17T00:00:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1283-formal-lockfile"
}
---

## AR-1283

Repair formal lockfile drift without weakening locked CI or changing formal behavior.
