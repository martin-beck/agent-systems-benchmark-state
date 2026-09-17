---
{
  "branch": "repair/ar-1297-task-schema-metadata",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [],
  "id": "AR-1297",
  "next_action": "Repair every reported task schema/metadata error from durable evidence, add strict superseded_by schema coverage, regenerate views, and rerun all state gates.",
  "observed_branch": "repair/ar-1297-task-schema-metadata",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1297.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Repair task schema and metadata consistency without weakening coordinator validation.",
  "task_revision": 1,
  "title": "Task schema and metadata consistency",
  "updated_at": "2026-09-17T00:00:00+00:00",
  "worktree_key": "agent-systems-benchmark-state-ar-1297-task-schema"
}
---

## AR-1297

AR-1296 exposed repository-wide schema failures in historical task metadata.
This AR owns only evidence-based task metadata and the versioned schema/test
contract. It must not relax validation, fabricate provenance, touch product or
asb-tui source, modify handoffctl implementation, or alter formal gates.
