---
{
  "branch": "feature/ar-1392-control-authority-materializer",
  "checkpoint_commit": "10bffbf015bd7ca78d8c0d18f04cf0190195e933",
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
  "next_action": "Claim the pre-bound isolated worktree, implement the control-owned private authority resolver required by AR-1391, and publish a signed PR.",
  "observed_branch": "feature/ar-1392-control-authority-materializer",
  "observed_dirty": 0,
  "observed_head": "10bffbf015bd7ca78d8c0d18f04cf0190195e933",
  "owner": "",
  "plan": "../plans/AR-1392-control-authority-materializer.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "open",
  "summary": "Resolve private live authority from authenticated control enrollment without caller injection.",
  "task_revision": 2,
  "title": "Control-owned private authority materializer",
  "updated_at": "2026-09-24T07:45:20+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1392-control-authority-materializer"
}
---

This successor owns the control-side authority gap found by AR-1391. It must
not touch asb-tui, expose secrets, synthesize authority, or require external
provider connectivity in development or CI.

- 2026-09-24T07:45:20+00:00: Runtime authority dependencies verified; AR-1391 audit identifies
  missing private control authority materialization.
