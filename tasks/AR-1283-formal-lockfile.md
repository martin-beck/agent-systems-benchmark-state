---
{
  "branch": "feature/ar-1283-formal-lockfile",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-17T02:47:11+00:00",
  "depends_on": [
    "AR-0003"
  ],
  "id": "AR-1283",
  "next_action": "Promote after dependency verification; regenerate and verify formal/Cargo.lock so hosted --locked formal tests do not attempt updates.",
  "observed_branch": "feature/ar-1283-formal-lockfile",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "asb_ar1024_lifecycle_router",
  "plan": "../plans/AR-1283.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Repair formal workspace lockfile drift that fails the locked CI gate.",
  "task_revision": 3,
  "title": "Formal lockfile CI drift repair",
  "updated_at": "2026-09-17T00:47:11+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1283-formal-lockfile"
}
---

## AR-1283

Repair formal lockfile drift without weakening locked CI or changing formal behavior.

- 2026-09-17T00:46:57+00:00: PR #208 Loom failed before tests because formal/Cargo.lock is stale
  under cargo test --locked; repair the lockfile without weakening the gate.

- 2026-09-17T00:47:11+00:00: Claimed by asb_ar1024_lifecycle_router.
