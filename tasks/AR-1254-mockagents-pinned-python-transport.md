---
{
  "branch": "feature/ar-1254-mockagents-pinned-python-transport",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1252",
    "AR-1253"
  ],
  "id": "AR-1254",
  "next_action": "Implement real bounded MockAgents transport fixture through pinned Python runner.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1254.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "open",
  "summary": "Qualify MockAgents through the pinned Python sandbox.",
  "task_revision": 2,
  "title": "Qualify MockAgents through pinned Python transport",
  "updated_at": "2026-09-16T13:44:21+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1254"
}
---

Implement only the linked AR-1254 plan using ASB development documentation and handoffctl.
Keep fixtures, runtimes, caches, and evidence under `/srv/data/projects`.

- 2026-09-16T13:44:21+00:00: AR-1252 and AR-1253 completed with immutable runner/runtime evidence;
  promote corrected MockAgents transport successor.
