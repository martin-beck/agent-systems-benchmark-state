---
{
  "branch": "feature/agent-goose",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-0101",
    "AR-0102",
    "AR-0103"
  ],
  "id": "AR-0307",
  "next_action": "Inspect current release assets, structured run mode, provider configuration and extension failure behavior.",
  "owner": "",
  "plan": "../plans/AR-0307.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "open",
  "summary": "Run pinned AAIF goose in no-session structured mode.",
  "task_revision": 2,
  "title": "Implement goose client adapter",
  "updated_at": "2026-09-07T00:19:28+00:00",
  "worktree_key": "agent-systems-benchmark-agent-goose"
}
---
## AR-0307

Run pinned AAIF goose in no-session structured mode.

Implementation has not started. Read the linked plan before claiming.


- 2026-09-07T00:19:28+00:00: Dependencies AR-0101, AR-0102, and AR-0103 are durably done on
  synchronized signed product main; AR-0307 owns isolated Goose adapter paths and is ready for
  quality-20260906 in its declared distinct worktree while shared registration remains
  coordinator-serialized.
