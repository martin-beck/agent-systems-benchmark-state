---
{
  "branch": "feature/ar-1380-runtime-scheduler-composition",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1378", "AR-1377", "AR-1366", "AR-1364", "AR-1362"],
  "id": "AR-1380",
  "next_action": "Promote and claim this dependency-valid scheduler composition successor, then implement runtime-owned per-attempt live dispatch inputs.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1380-runtime-scheduler-composition.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Compose runtime-owned live attempts for production run and sweep scheduling.",
  "title": "Runtime scheduler composition for live dispatch",
  "task_revision": 1,
  "updated_at": "2026-09-24T03:50:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1380-runtime-scheduler-composition"
}
---

AR-1379 audit found the existing CLI factory callback receives only input id
and warmup flags, while runtime acquisition requires validated launch input,
lease, adapter identity, and teardown context. This successor closes that
composition gap without weakening authority boundaries.
