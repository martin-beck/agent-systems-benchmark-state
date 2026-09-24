---
{
  "branch": "feature/ar-1381-live-cli-scheduler-wiring",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1380", "AR-1378", "AR-1377", "AR-1373", "AR-1366", "AR-1364", "AR-1362"],
  "id": "AR-1381",
  "next_action": "Promote and claim this dependency-valid CLI scheduler wiring successor, then implement run/sweep runtime-owned live dispatch.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1381-live-cli-scheduler-wiring.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Wire runtime-owned live scheduler authority into production asb run and sweep.",
  "title": "Runtime-owned live CLI scheduler wiring",
  "task_revision": 1,
  "updated_at": "2026-09-24T04:01:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1381-live-cli-scheduler-wiring"
}
---

AR-1380 merged the runtime-owned per-attempt factory. This successor connects
that factory to the existing CLI run/sweep execution boundary while retaining
all fail-closed authority and privacy contracts.
