---
{
  "branch": "feature/ar-1379-live-dispatch-integration",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1378", "AR-1377", "AR-1366", "AR-1364", "AR-1362"],
  "id": "AR-1379",
  "next_action": "Promote and claim this dependency-valid production dispatch successor, refresh an isolated worktree, and wire the authenticated adapter into asb run/sweep.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1379-live-dispatch-integration.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Integrate authenticated runtime live dispatch into asb run and sweep.",
  "title": "Production live dispatch integration",
  "task_revision": 1,
  "updated_at": "2026-09-24T03:40:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1379-live-dispatch-integration"
}
---

This task advances AR-1329 without reopening blocked historical tasks. It must
not claim provider or OpenRouter readiness until real runtime execution is
verified through the completed gates.
