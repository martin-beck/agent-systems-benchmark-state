---
{
  "branch": "feature/ar-1378-live-control-adapter",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-24T05:08:16+00:00",
  "depends_on": [
    "AR-1377",
    "AR-1366",
    "AR-1364",
    "AR-1362"
  ],
  "id": "AR-1378",
  "next_action": "Promote and claim the dependency-valid successor, refresh an isolated worktree, and implement the authenticated ControlClient-to-runtime bridge.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "codex-asb-runtime-receipt-source-luna56",
  "plan": "../plans/AR-1378-live-control-adapter.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Bind authenticated control receipts to runtime-owned live dispatch.",
  "task_revision": 3,
  "title": "Authenticated live control adapter",
  "updated_at": "2026-09-24T03:08:16+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1378-live-control-adapter"
}
---

Successor to the blocked AR-1376 adapter audit. AR-1377 supplies the opaque
chain store; this task supplies only the authenticated control operation seam.

- 2026-09-24T03:08:14+00:00: Done dependencies AR-1377, AR-1366, AR-1364, AR-1362 verified; blocked
  AR-1376 is audit evidence only.

- 2026-09-24T03:08:16+00:00: Claimed by codex-asb-runtime-receipt-source-luna56.
