---
{
  "branch": "feature/ar-1265-runtime-owned-replay-entrypoint",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1237",
    "AR-1238",
    "AR-1239"
  ],
  "id": "AR-1265",
  "next_action": "Promote after dependency verification; implement the runtime-owned authenticated replay entrypoint and real supervised lifecycle evidence described in the plan.",
  "observed_branch": "feature/ar-1265-runtime-owned-replay-entrypoint",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1265.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "open",
  "summary": "Provide a real runtime-owned strict-replay CLI entrypoint.",
  "task_revision": 2,
  "title": "Runtime-owned strict-replay CLI entrypoint",
  "updated_at": "2026-09-16T22:19:31+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1265-runtime-replay-entrypoint"
}
---
## AR-1265

Implement the runtime-owned strict-replay entrypoint and supervised lifecycle contract. AR-1262's
unmerged implementation is not an input; preserve its review as the reason this separate AR exists.

- 2026-09-16T22:19:31+00:00: Dependencies AR-1237, AR-1238, and AR-1239 are done; AR-1262 review
  proves a separate runtime-owned entrypoint is required.
