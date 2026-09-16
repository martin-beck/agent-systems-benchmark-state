---
{
  "branch": "feature/ar-1271-cassette-operation-contract",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1237",
    "AR-1238",
    "AR-1239"
  ],
  "id": "AR-1271",
  "next_action": "Promote after dependency verification; implement the shared bounded cassette request/response operation contract and runtime/CLI adapters.",
  "observed_branch": "feature/ar-1271-cassette-operation-contract",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1271.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "open",
  "summary": "Define a dependency-neutral cassette request/response operation contract.",
  "task_revision": 2,
  "title": "Dependency-neutral cassette operation contract",
  "updated_at": "2026-09-16T23:12:37+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1271-cassette-operation"
}
---
## AR-1271

Implement the shared cassette operation envelope needed for runtime-supervised strict replay.
Preserve AR-1270's blocked evidence and do not fabricate responses or authority.

- 2026-09-16T23:12:37+00:00: Dependencies are done; AR-1270 identified the missing
  dependency-neutral cassette request/response operation boundary.
