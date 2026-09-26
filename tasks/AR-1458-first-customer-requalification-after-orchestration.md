---
{
  "branch": "qualification/ar-1458-first-customer-requalification-after-orchestration",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1446",
    "AR-1453",
    "AR-1456"
  ],
  "id": "AR-1458",
  "next_action": "Promote and run the disposable first-customer install/configure/local-mock benchmark/strict-replay/recovery/cleanup qualification against the exact current protected main after the central orchestration merge; publish a privacy-safe readiness report or record any deterministic repair AR.",
  "owner": "",
  "plan": "../plans/AR-1458.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Requalify the first-customer production-like journey after central orchestration became authoritative.",
  "task_revision": 1,
  "title": "First-customer requalification after central orchestration",
  "updated_at": "2026-09-26T20:10:00+00:00",
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
