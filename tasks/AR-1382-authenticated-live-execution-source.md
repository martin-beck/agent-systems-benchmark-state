---
{
  "branch": "feature/ar-1382-authenticated-live-execution-source",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1381", "AR-1380", "AR-1378", "AR-1377", "AR-1373"],
  "id": "AR-1382",
  "next_action": "Promote and claim this dependency-valid authenticated execution-source successor, then implement runtime-owned scheduler materialization.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1382-authenticated-live-execution-source.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Materialize authenticated runtime-owned live execution for asb run and sweep.",
  "title": "Authenticated live execution source",
  "task_revision": 1,
  "updated_at": "2026-09-24T04:40:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1382-authenticated-live-execution-source"
}
---

AR-1329 re-audit found that the merged scheduler wrapper still requires an
authenticated runtime execution source. This task supplies that source while
preserving the no-caller-authority and fail-closed boundaries.
