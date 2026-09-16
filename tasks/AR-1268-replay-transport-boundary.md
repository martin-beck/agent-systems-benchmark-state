---
{
  "branch": "feature/ar-1268-replay-transport-boundary",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-17T00:45:23+00:00",
  "depends_on": [
    "AR-1237",
    "AR-1238",
    "AR-1239"
  ],
  "id": "AR-1268",
  "next_action": "Promote after dependency verification; define and implement the dependency-safe runtime/CLI replay transport boundary.",
  "observed_branch": "feature/ar-1268-replay-transport-boundary",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "asb_ar1024_lifecycle_router",
  "plan": "../plans/AR-1268.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Break the strict-replay runtime/CLI dependency cycle with a shared transport contract.",
  "task_revision": 3,
  "title": "Break strict-replay runtime/CLI dependency cycle",
  "updated_at": "2026-09-16T22:45:23+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1268-replay-transport"
}
---
## AR-1268

Resolve the dependency-safe transport seam required for runtime-owned strict-replay execution.
Preserve AR-1267's blocked evidence; do not fabricate authority or weaken crate boundaries.

- 2026-09-16T22:45:10+00:00: Dependencies AR-1237/1238/1239 are done; AR-1267 proves a
  dependency-safe runtime/CLI transport boundary is required.

- 2026-09-16T22:45:23+00:00: Claimed by asb_ar1024_lifecycle_router.
