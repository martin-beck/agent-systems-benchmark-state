---
{
  "branch": "feature/ar-1367-ar1329-production-dispatch-integration",
  "checkpoint_commit": "0c6dc52e1f4aa5854f73081711dbd9a5bc1a5d7c",
  "claim_expires": "",
  "depends_on": [
    "AR-1366",
    "AR-1340",
    "AR-1339",
    "AR-1328"
  ],
  "id": "AR-1367",
  "next_action": "Promote and claim this fresh AR-1329 successor, refresh an isolated worktree to protected main, audit the production run/sweep dispatch seam, and implement only through runtime-owned bridge inputs.",
  "observed_branch": "feature/ar-1367-ar1329-production-dispatch-integration",
  "observed_dirty": 0,
  "observed_head": "0c6dc52e1f4aa5854f73081711dbd9a5bc1a5d7c",
  "owner": "",
  "plan": "../plans/AR-1367-ar1329-production-dispatch-integration.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Complete production asb run/sweep live-provider dispatch through runtime-owned authenticated acquisition and teardown.",
  "task_revision": 1,
  "title": "AR-1329 production dispatch integration",
  "updated_at": "2026-09-24T00:45:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1367-ar1329-production-dispatch-integration"
}
---

Successor for the blocked AR-1329 execution path. Do not resume stale AR-1329
metadata, touch asb-tui, or expose live authority through CLI/config input.
