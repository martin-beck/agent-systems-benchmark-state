---
{
  "branch": "feature/agent-qwen-code",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-07T00:56:44+00:00",
  "depends_on": [
    "AR-0101",
    "AR-0102",
    "AR-0103"
  ],
  "id": "AR-0306",
  "next_action": "Inspect the current stable release, stream-JSON contract, provider override and ambient context loading.",
  "owner": "root-coordination-20260906",
  "plan": "../plans/AR-0306.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Run pinned Qwen Code through isolated headless stream-JSON.",
  "task_revision": 3,
  "title": "Implement Qwen Code client adapter",
  "updated_at": "2026-09-06T23:56:44+00:00",
  "worktree_key": "agent-systems-benchmark-agent-qwen-code"
}
---
## AR-0306

Run pinned Qwen Code through isolated headless stream-JSON.

Implementation has not started. Read the linked plan before claiming.


- 2026-09-06T23:56:35+00:00: Dependencies AR-0101, AR-0102, and AR-0103 are durably done on
  synchronized signed product main; Aider integration released its module fence; Qwen Code owns a
  distinct adapter module and fixture worktree. Shared registration remains serialized with AR-0304,
  AR-0305, and AR-0310.

- 2026-09-06T23:56:44+00:00: Claimed by root-coordination-20260906.
