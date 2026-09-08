---
{
  "branch": "upgrade/coordinator-v0.2.0",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [],
  "id": "AR-0854",
  "next_action": "Promote and claim the upgrade, vendor signed v0.2.0 in an isolated worktree, and publish only after exact-head gates pass.",
  "owner": "",
  "plan": "../plans/AR-0854.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "planned",
  "summary": "Adopt coordinator v0.2.0 concurrency, recovery, durable-run, replica, and vendor hardening.",
  "task_revision": 1,
  "title": "Upgrade shared workflow coordinator to v0.2.0",
  "updated_at": "2026-09-08T10:09:00+00:00",
  "worktree_key": "agent-systems-benchmark-coordinator-v020"
}
---

This task upgrades only the pinned shared coordinator artifact and its directly associated
verification and documentation.
