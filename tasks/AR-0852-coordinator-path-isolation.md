---
{
  "branch": "feature/shared-workflow-coordinator",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [],
  "id": "AR-0852",
  "next_action": "Merge the exact green v0.1.4 follow-up and verify the installed coordinator and project binding on live main.",
  "owner": "",
  "plan": "../plans/AR-0852.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "open",
  "summary": "Adopt the path-exclusive coordinator commit fix discovered during live integration.",
  "task_revision": 2,
  "title": "Adopt coordinator path isolation fix",
  "updated_at": "2026-09-08T07:21:36+00:00",
  "worktree_key": "agent-systems-benchmark-shared-coordinator"
}
---

This follow-up preserves unrelated staged work by updating the pinned shared coordinator from
v0.1.3 to v0.1.4 after AR-0851 was completed.

- 2026-09-08T07:21:36+00:00: The exact v0.1.4 PR head passed implementation and formal CI.
