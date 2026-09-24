---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1423", "AR-1425"],
  "id": "AR-1426",
  "next_action": "Promote after AR-1423 and AR-1425 are released; implement content-addressed refresh manifests and fail-closed window validation for LiveCodeBench and SWE-rebench.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "0000000000000000000000000000000000000000",
  "owner": "",
  "plan": "../plans/AR-1426-evolving-literature-window-refresh.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "planned",
  "summary": "Refresh evolving literature benchmark windows without stale or incomparable results.",
  "title": "Evolving literature workload window refresh",
  "task_revision": 1,
  "updated_at": "2026-09-24T00:00:00+00:00",
  "worktree_key": ""
}
---

This AR keeps time-windowed and continuously refreshed literature workloads
selectable without treating a mutable source as a stable benchmark. It never
requires live providers or upstream downloads during development or CI.

- 2026-09-24: Added after the literature audit identified stale-window risk for
  LiveCodeBench and SWE-rebench. Existing built-in and stable literature IDs are
  unaffected; every refresh is a new content-addressed identity.
