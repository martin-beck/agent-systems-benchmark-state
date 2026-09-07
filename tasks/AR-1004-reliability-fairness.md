---
{
  "branch": "feature/reliability-fairness",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-0203",
    "AR-0204",
    "AR-0401"
  ],
  "id": "AR-1004",
  "next_action": "Add trial/epoch aggregation following tau-bench and Inspect concepts.",
  "owner": "",
  "plan": "../plans/AR-1004.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "open",
  "summary": "Report repeated-attempt reliability and prevent aggregate results from hiding starvation or hard strata.",
  "task_revision": 2,
  "title": "Measure reliability and mixed-workload fairness",
  "updated_at": "2026-09-07T03:26:36+00:00",
  "worktree_key": "agent-systems-benchmark-reliability-fairness"
}
---
## AR-1004

Report repeated-attempt reliability and prevent aggregate results from hiding starvation or hard strata.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-07T03:26:36+00:00: Dependencies AR-0203, AR-0204, and AR-0401 are durably done. Promote
  this P1 analysis task for contracts-20260906 after AR-0902 release; its asb-analysis
  reliability/report scope is independent of active frontend-control, mini-SWE, and native-platform
  paths.
