---
{
  "branch": "feature/ar-1270-runtime-cassette-handle",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1237", "AR-1238", "AR-1239"],
  "id": "AR-1270",
  "next_action": "Promote after dependency verification; define the runtime-issued cassette-service handle and integrate real supervised replay traffic.",
  "observed_branch": "feature/ar-1270-runtime-cassette-handle",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1270.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Provide a runtime-issued cassette-service handle for supervised strict replay.",
  "task_revision": 1,
  "title": "Runtime-issued cassette-service handle",
  "updated_at": "2026-09-16T23:10:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1270-runtime-cassette-handle"
}
---
## AR-1270

Implement the dependency-neutral runtime-issued cassette-service handle required for real supervised
strict replay. Preserve AR-1269's authority evidence and blocker; do not move service authority into
the CLI.
