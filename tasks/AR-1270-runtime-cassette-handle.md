---
{
  "branch": "feature/ar-1270-runtime-cassette-handle",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-17T01:05:11+00:00",
  "depends_on": [
    "AR-1237",
    "AR-1238",
    "AR-1239"
  ],
  "id": "AR-1270",
  "next_action": "Promote after dependency verification; define the runtime-issued cassette-service handle and integrate real supervised replay traffic.",
  "observed_branch": "feature/ar-1270-runtime-cassette-handle",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "asb_ar1024_lifecycle_router",
  "plan": "../plans/AR-1270.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Provide a runtime-issued cassette-service handle for supervised strict replay.",
  "task_revision": 4,
  "title": "Runtime-issued cassette-service handle",
  "updated_at": "2026-09-16T23:06:03+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1270-runtime-cassette-handle"
}
---
## AR-1270

Implement the dependency-neutral runtime-issued cassette-service handle required for real supervised
strict replay. Preserve AR-1269's authority evidence and blocker; do not move service authority into
the CLI.

- 2026-09-16T23:04:53+00:00: Dependencies are done; AR-1269 proves a runtime-issued cassette-service
  handle is required to execute real traffic without a crate cycle.

- 2026-09-16T23:05:11+00:00: Claimed by asb_ar1024_lifecycle_router.

- 2026-09-16T23:06:03+00:00: Recorded command exit 1; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.
