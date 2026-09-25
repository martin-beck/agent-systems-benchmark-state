---
{
  "branch": "qualification/ar-1446-first-customer-production",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-0903", "AR-1336", "AR-1433", "AR-1441", "AR-1442", "AR-1443", "AR-1444"],
  "id": "AR-1446",
  "next_action": "Remain planned until install, guided setup, benchmark capture/comparison, first-class journey, support-matrix, and deterministic runtime mock dependencies are independently released; then qualify a disposable first-customer environment and publish the bounded readiness report. AR-1329 optional external-provider integration must not block this local production-like gate.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1446.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Qualify ASB in a disposable first-customer production-like environment.",
  "task_revision": 1,
  "title": "First-customer production qualification",
  "updated_at": "2026-09-25T15:00:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1446-first-customer-production"
}
---

This is the customer-facing integration gate. The deterministic local mock path remains the mandatory development and hosted qualification route; operator live-provider smoke evidence is optional and separately classified.

- 2026-09-25T15:00:00+00:00: Created from the production-readiness audit. Existing feature ARs cover individual capabilities but no AR verifies the complete disposable first-customer install/configure/benchmark/replay/recovery/cleanup journey with an explicit support and rollback report.
