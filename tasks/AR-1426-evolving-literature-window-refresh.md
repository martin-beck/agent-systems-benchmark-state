---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-27T12:05:18+00:00",
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
  "task_revision": 3,
  "title": "Evolving literature workload window refresh",
  "updated_at": "2026-09-27T10:05:18+00:00",
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
