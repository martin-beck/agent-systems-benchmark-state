---
{
  "branch": "ci/verify-coordination-content",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-0002", "AR-0003"],
  "id": "AR-0895",
  "next_action": "Make task, plan, CURRENT.md, and STATUS.md pull-request changes trigger exact-head Coordination verification and DCO, with path-filter regression tests.",
  "owner": "",
  "plan": "../plans/AR-0895.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "planned",
  "summary": "Close the workflow path-filter gap that lets coordination-content pull requests skip strict state consistency and DCO checks.",
  "task_revision": 1,
  "title": "Verify every coordination-content pull request",
  "updated_at": "2026-09-09T07:25:00+00:00",
  "worktree_key": "agent-systems-benchmark-state-verify-coordination-content"
}
---
## AR-0895

Ensure state-content pull requests cannot bypass exact-head schema, generated-view, quality, and DCO enforcement merely because they change only tasks, plans, CURRENT.md, or STATUS.md.
