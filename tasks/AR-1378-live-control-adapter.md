---
{
  "branch": "feature/ar-1378-live-control-adapter",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1377", "AR-1366", "AR-1364", "AR-1362"],
  "id": "AR-1378",
  "next_action": "Promote and claim the dependency-valid successor, refresh an isolated worktree, and implement the authenticated ControlClient-to-runtime bridge.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1378-live-control-adapter.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Bind authenticated control receipts to runtime-owned live dispatch.",
  "title": "Authenticated live control adapter",
  "task_revision": 1,
  "updated_at": "2026-09-24T03:05:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1378-live-control-adapter"
}
---

Successor to the blocked AR-1376 adapter audit. AR-1377 supplies the opaque
chain store; this task supplies only the authenticated control operation seam.
