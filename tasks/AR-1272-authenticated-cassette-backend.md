---
{
  "branch": "feature/ar-1272-authenticated-cassette-backend",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1237", "AR-1238", "AR-1239"],
  "id": "AR-1272",
  "next_action": "Promote after dependency verification; implement runtime-authenticated immutable cassette backend content binding and real supervised replay.",
  "observed_branch": "feature/ar-1272-authenticated-cassette-backend",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1272.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Bind immutable cassette content to a runtime-authenticated replay backend handle.",
  "task_revision": 1,
  "title": "Authenticated immutable cassette backend",
  "updated_at": "2026-09-16T23:30:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1272-cassette-backend"
}
---
## AR-1272

Implement the runtime-authenticated immutable cassette backend required for real strict-replay
execution. Preserve AR-1271's blocked evidence and do not accept caller-supplied cassette bytes or
paths as authority.
