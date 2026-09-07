---
{
  "branch": "feature/reliability-fairness",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-07T05:27:20+00:00",
  "depends_on": [
    "AR-0203",
    "AR-0204",
    "AR-0401"
  ],
  "id": "AR-1004",
  "next_action": "Add trial/epoch aggregation following tau-bench and Inspect concepts.",
  "observed_branch": "feature/reliability-fairness",
  "observed_dirty": 4,
  "observed_head": "4a59593c0c55e0ad72656363473a404d8be1054b",
  "owner": "contracts-20260906",
  "plan": "../plans/AR-1004.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Report repeated-attempt reliability and prevent aggregate results from hiding starvation or hard strata.",
  "task_revision": 15,
  "title": "Measure reliability and mixed-workload fairness",
  "updated_at": "2026-09-07T03:36:37+00:00",
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

- 2026-09-07T03:27:20+00:00: Claimed by contracts-20260906.

- 2026-09-07T03:27:46+00:00: Recorded command exit 0; command argv SHA-256
  95d17f4eb08fbda8ab0832bb2ee42c62d939545eff69c8cd25ce253283420c83.

- 2026-09-07T03:31:21+00:00: Recorded command exit 2; command argv SHA-256
  48458d4adcbc2714c4ae60f17ec39d916357031118af6e75d9a5cd826c73f20e.

- 2026-09-07T03:33:09+00:00: Recorded command exit 0; command argv SHA-256
  c519f43ba3b5d096908f69ee04349e26ec55bab7fa7aaf32c0d3e1689526bded.

- 2026-09-07T03:34:10+00:00: Recorded command exit 0; command argv SHA-256
  c519f43ba3b5d096908f69ee04349e26ec55bab7fa7aaf32c0d3e1689526bded.

- 2026-09-07T03:34:38+00:00: Recorded command exit 101; command argv SHA-256
  71855465d58a14c2a688a4b1274b5ab8828d5cbd3d8f4a99dcc72cbdec81fa4b.

- 2026-09-07T03:34:53+00:00: Recorded command exit 0; command argv SHA-256
  c519f43ba3b5d096908f69ee04349e26ec55bab7fa7aaf32c0d3e1689526bded.

- 2026-09-07T03:35:15+00:00: Recorded command exit 0; command argv SHA-256
  71855465d58a14c2a688a4b1274b5ab8828d5cbd3d8f4a99dcc72cbdec81fa4b.

- 2026-09-07T03:35:39+00:00: Recorded command exit 0; command argv SHA-256
  96267ae6178bc8a81d2bd589503ac621cc69c92687335eccb0c0a81916f6e5fd.

- 2026-09-07T03:36:37+00:00: Recorded command exit 0; command argv SHA-256
  33e9962ad00866c6616045365339c9f3bd27b0ebfeaba60a8acaf4f363e008db.
