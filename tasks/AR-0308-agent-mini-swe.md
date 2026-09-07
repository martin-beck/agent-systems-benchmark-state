---
{
  "branch": "feature/agent-mini-swe",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-07T02:15:34+00:00",
  "depends_on": [
    "AR-0101",
    "AR-0102",
    "AR-0103"
  ],
  "id": "AR-0308",
  "next_action": "Inspect the current package, trajectory contract, LiteLLM override and environment isolation.",
  "owner": "replay-20260906",
  "plan": "../plans/AR-0308.md",
  "priority": "P2",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Run pinned mini-SWE-agent as a bounded batch engineering agent.",
  "task_revision": 3,
  "title": "Implement mini-SWE-agent client adapter",
  "updated_at": "2026-09-07T00:45:34+00:00",
  "worktree_key": "agent-systems-benchmark-agent-mini-swe"
}
---
## AR-0308

Run pinned mini-SWE-agent as a bounded batch engineering agent.

Implementation has not started. Read the linked plan before claiming.


- 2026-09-07T00:44:24+00:00: Dependencies AR-0101, AR-0102, and AR-0103 are durably done on
  synchronized signed product main 2579362; AR-0308 owns isolated mini-SWE-agent adapter paths and
  is ready for replay-20260906 in its declared distinct worktree while shared registration remains
  coordinator-serialized.

- 2026-09-07T00:45:34+00:00: Claimed by replay-20260906.
