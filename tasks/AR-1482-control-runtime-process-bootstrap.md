---
{
  "branch": "feature/ar-1482-control-runtime-process-bootstrap",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1472", "AR-1473", "AR-1480"],
  "id": "AR-1482",
  "next_action": "Promote and claim, then inspect control/runtime process bootstrap APIs on protected main.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1482-control-runtime-process-bootstrap.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Compose authenticated control enrollment into the ordinary CLI process bootstrap.",
  "task_revision": 1,
  "title": "Control-runtime process bootstrap",
  "updated_at": "2026-09-27T00:00:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1482-control-runtime-process-bootstrap"
}
---

Narrow successor to AR-1481. It owns only process-level composition over the
completed opaque-source contracts and must not modify asb-tui, require live
providers, accept caller-built authority, or weaken fail-closed boundaries.

