---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-27T12:07:11+00:00",
  "depends_on": [
    "AR-1423",
    "AR-1425"
  ],
  "id": "AR-1426",
  "next_action": "Promote after AR-1423 and AR-1425 are released; implement content-addressed refresh manifests and fail-closed window validation for LiveCodeBench and SWE-rebench.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "0000000000000000000000000000000000000000",
  "owner": "ar1332-record-replay-luna56",
  "plan": "../plans/AR-1426-evolving-literature-window-refresh.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Refresh evolving literature benchmark windows without stale or incomparable results.",
  "task_revision": 6,
  "title": "Evolving literature workload window refresh",
  "updated_at": "2026-09-27T10:07:21+00:00",
  "worktree_key": ""
}
---

This AR keeps time-windowed and continuously refreshed literature workloads
selectable without treating a mutable source as a stable benchmark. It never
requires live providers or upstream downloads during development or CI.

- 2026-09-24: Added after the literature audit identified stale-window risk for
  LiveCodeBench and SWE-rebench. Existing built-in and stable literature IDs are
  unaffected; every refresh is a new content-addressed identity.

- 2026-09-27T10:05:16+00:00: AR-1423 and AR-1425 are released done; promote the dependency-ready
  offline refresh-manifest implementation.

- 2026-09-27T10:05:18+00:00: Claimed by ar1332-record-replay-luna56.

- 2026-09-27T10:05:29+00:00: Recorded command exit 0; command argv SHA-256
  1d96b88e0f9d8fc7de759f6c96696434c0868b7259e3dae18a69288d99e85bf1.

- 2026-09-27T10:07:11+00:00: Heartbeat by ar1332-record-replay-luna56.

- 2026-09-27T10:07:21+00:00: Recorded command exit 0; command argv SHA-256
  83c84b7ac070d1aac6e30d26c8e7594032ea08b02fde5ebba86c365365ccd50f.
