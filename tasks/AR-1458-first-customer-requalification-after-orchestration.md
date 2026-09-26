---
{
  "branch": "qualification/ar-1458-first-customer-requalification-after-orchestration",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-26T19:21:45+00:00",
  "depends_on": [
    "AR-1446",
    "AR-1453",
    "AR-1456"
  ],
  "id": "AR-1458",
  "next_action": "Promote and run the disposable first-customer install/configure/local-mock benchmark/strict-replay/recovery/cleanup qualification against the exact current protected main after the central orchestration merge; publish a privacy-safe readiness report or record any deterministic repair AR.",
  "owner": "coordinator-ar1458-requal",
  "plan": "../plans/AR-1458.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Requalify the first-customer production-like journey after central orchestration became authoritative.",
  "task_revision": 3,
  "title": "First-customer requalification after central orchestration",
  "updated_at": "2026-09-26T18:36:45+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1458-first-customer-requalification-after-orchestration"
}
---

AR-1446 qualified the disposable first-customer path on merge 2872a31 before
the central orchestration design, implementation, and frontend routing landed.
This AR reruns the complete ASB-only customer-like journey on the current
protected main: clean install/bootstrap, explicit local/mock configuration,
multi-agent workload execution, evidence inspection, strict offline replay,
cancellation/restart recovery, and cleanup/rollback. It must not contact a
remote provider or modify asb-tui. Any live-provider evidence remains optional
and separately classified.

- 2026-09-26T18:36:36+00:00: Current main now includes central orchestration after AR-1446
  qualification; requalify the customer journey on the updated exact main.

- 2026-09-26T18:36:45+00:00: Claimed by coordinator-ar1458-requal.
