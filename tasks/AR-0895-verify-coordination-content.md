---
{
  "branch": "ci/verify-coordination-content",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-09T12:42:20+00:00",
  "depends_on": [
    "AR-0002",
    "AR-0003"
  ],
  "id": "AR-0895",
  "next_action": "Make task, plan, CURRENT.md, and STATUS.md pull-request changes trigger exact-head Coordination verification and DCO, with path-filter regression tests.",
  "owner": "quality_20260906",
  "plan": "../plans/AR-0895.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Close the workflow path-filter gap that lets coordination-content pull requests skip strict state consistency and DCO checks.",
  "task_revision": 4,
  "title": "Verify every coordination-content pull request",
  "updated_at": "2026-09-09T09:42:43+00:00",
  "worktree_key": "agent-systems-benchmark-state-verify-coordination-content"
}
---
## AR-0895

Ensure state-content pull requests cannot bypass exact-head schema, generated-view, quality, and DCO enforcement merely because they change only tasks, plans, CURRENT.md, or STATUS.md.

- 2026-09-09T09:42:17+00:00: Selected as the highest-priority compatible dependency-ready task after
  AR-0806 release. P0 tasks remain dependency-blocked; AR-0704 requires external cost/provider
  authorization, AR-0832 owns runner operations, and AR-0890 overlaps active provider/workflow
  integration. AR-0895 is an isolated state-workflow quality lane with AR-0002/AR-0003 done and no
  active path-owner conflict.

- 2026-09-09T09:42:20+00:00: Claimed by quality_20260906.

- 2026-09-09T09:42:43+00:00: Recorded command exit 0; command argv SHA-256
  57554c6619b70809ba3ccdce153dfad37279c32430a38a85fa9f7ed6213db671.
