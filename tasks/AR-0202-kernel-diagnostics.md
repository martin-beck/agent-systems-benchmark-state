---
{
  "branch": "feature/kernel-diagnostics",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-08T06:08:16+00:00",
  "depends_on": [
    "AR-0201",
    "AR-0103"
  ],
  "id": "AR-0202",
  "next_action": "Design capability probes and bounded diagnostics profiles.",
  "owner": "quality_20260906",
  "plan": "../plans/AR-0202.md",
  "priority": "P2",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Integrate perf and optional eBPF diagnostics without making privileged tools mandatory.",
  "task_revision": 3,
  "title": "Add optional kernel diagnostics",
  "updated_at": "2026-09-08T03:08:16+00:00",
  "worktree_key": "agent-systems-benchmark-kernel-diagnostics"
}
---
## AR-0202

Integrate perf and optional eBPF diagnostics without making privileged tools mandatory.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-08T03:08:04+00:00: Dependencies AR-0201 and AR-0103 are done. P0 work is
  dependency-blocked; ready P1 AR-0704 lacks required authorized Debian/openEuler provider capacity,
  AR-0904 overlaps active AR-0840 protocol/schema work, and AR-1003 overlaps active AR-1002 analysis
  paths. AR-0202 owns isolated asb-metrics optional kernel collectors and its declared
  branch/worktree are absent.

- 2026-09-08T03:08:16+00:00: Claimed by quality_20260906.
