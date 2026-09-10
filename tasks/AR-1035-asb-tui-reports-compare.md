---
{
  "branch": "feature/tui-reports-compare",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-0875", "AR-1025", "AR-1033"],
  "id": "AR-1035",
  "next_action": "Implement recent-runs, report and comparison screens from the published ASB history/analysis contract.",
  "owner": "",
  "plan": "../plans/AR-1035.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Add searchable recent runs, report inspection and evidence-qualified comparison workspaces.",
  "task_revision": 2,
  "title": "Build recent-runs, report and comparison workspaces",
  "updated_at": "2026-09-10T21:04:37+00:00",
  "worktree_key": "agent-systems-benchmark-asb-tui-reports-compare"
}
---
Implement recent-run discovery, report inspection and comparison entirely in standalone `asb-tui`,
using only the versioned ASB history/analysis protocol and privacy-safe public evidence.

- 2026-09-10T21:04:37+00:00: Bound pagination, retained pages, rendered overscan, latency and
  incremental memory; required argv round trips, reviewed shell quoting and redaction tests.
