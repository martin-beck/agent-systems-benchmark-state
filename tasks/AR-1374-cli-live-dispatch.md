---
{
  "branch": "feature/ar-1374-cli-live-dispatch",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1373", "AR-1339", "AR-1340", "AR-1328"],
  "id": "AR-1374",
  "next_action": "Await dependency completion, then audit and implement runtime-owned asb run/sweep dispatch using the authenticated receipt source.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1374-cli-live-dispatch.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Consume authenticated runtime receipts in production asb run and sweep dispatch.",
  "task_revision": 1,
  "title": "Production live-provider dispatch",
  "updated_at": "2026-09-24T02:35:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1374-cli-live-dispatch"
}
---

Successor to the completed authenticated receipt source AR-1373. This task
must not claim end-to-end OpenRouter readiness until real runtime/provider
execution and teardown are verified.

- 2026-09-24T02:35:00+00:00: Created as the dependency-valid successor for
  AR-1329 production run/sweep dispatch.
