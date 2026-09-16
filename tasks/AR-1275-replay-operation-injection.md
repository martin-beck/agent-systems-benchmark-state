---
{
  "branch": "feature/ar-1275-replay-operation-injection",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-17T01:48:01+00:00",
  "depends_on": [
    "AR-1237",
    "AR-1238",
    "AR-1239"
  ],
  "id": "AR-1275",
  "next_action": "Promote after dependency verification; add the required runtime operation-handle injection point to actual replay dispatch and test real supervised traffic.",
  "observed_branch": "feature/ar-1275-replay-operation-injection",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "asb_ar1024_lifecycle_router",
  "plan": "../plans/AR-1275.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Inject runtime-owned operation handles into actual strict-replay dispatch.",
  "task_revision": 4,
  "title": "Runtime operation injection into replay dispatcher",
  "updated_at": "2026-09-16T23:49:22+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1275-operation-injection"
}
---
## AR-1275

Implement the runtime operation injection seam for actual strict-replay dispatch. Preserve AR-1274's
blocked evidence and do not accept metadata-only or caller-fabricated execution.

- 2026-09-16T23:47:42+00:00: Dependencies AR-1237, AR-1238, and AR-1239 are done; AR-1274 proves the
  actual replay dispatcher still lacks a runtime-issued operation-handle injection point.

- 2026-09-16T23:48:01+00:00: Claimed by asb_ar1024_lifecycle_router.

- 2026-09-16T23:49:22+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.
