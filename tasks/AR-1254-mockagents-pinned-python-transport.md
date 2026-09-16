---
{
  "branch": "feature/ar-1254-mockagents-pinned-python-transport",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-16T15:44:29+00:00",
  "depends_on": [
    "AR-1252",
    "AR-1253"
  ],
  "id": "AR-1254",
  "next_action": "Implement real bounded MockAgents transport fixture through pinned Python runner.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "asb_ar1254_mockagents_transport",
  "plan": "../plans/AR-1254.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Qualify MockAgents through the pinned Python sandbox.",
  "task_revision": 4,
  "title": "Qualify MockAgents through pinned Python transport",
  "updated_at": "2026-09-16T13:44:37+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1254"
}
---

Implement only the linked AR-1254 plan using ASB development documentation and handoffctl.
Keep fixtures, runtimes, caches, and evidence under `/srv/data/projects`.

- 2026-09-16T13:44:21+00:00: AR-1252 and AR-1253 completed with immutable runner/runtime evidence;
  promote corrected MockAgents transport successor.

- 2026-09-16T13:44:29+00:00: Claimed by asb_ar1254_mockagents_transport.

- 2026-09-16T13:44:37+00:00: Recorded command exit 0; command argv SHA-256
  009884615fa8662c9070d8ce2e9b138e54961ba8bda6bec5fb2208ed2d342059.
