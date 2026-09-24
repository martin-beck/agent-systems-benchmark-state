---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1388",
    "AR-1385",
    "AR-1373",
    "AR-1366",
    "AR-1341",
    "AR-1342",
    "AR-1339",
    "AR-1340"
  ],
  "id": "AR-1392",
  "next_action": "Promote after dependencies are verified, then bind an isolated worktree and implement the control-owned private authority resolver required by AR-1391.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "0000000000000000000000000000000000000000",
  "owner": "",
  "plan": "../plans/AR-1392-control-authority-materializer.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "open",
  "summary": "Resolve private live authority from authenticated control enrollment without caller injection.",
  "task_revision": 2,
  "title": "Control-owned private authority materializer",
  "updated_at": "2026-09-24T07:45:20+00:00",
  "worktree_key": ""
}
---

This successor owns the control-side authority gap found by AR-1391. It must
not touch asb-tui, expose secrets, synthesize authority, or require external
provider connectivity in development or CI.

- 2026-09-24T07:45:20+00:00: Runtime authority dependencies verified; AR-1391 audit identifies
  missing private control authority materialization.
