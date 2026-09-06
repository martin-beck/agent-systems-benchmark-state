---
{
  "branch": "feature/agent-opendesk",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-0101",
    "AR-0102"
  ],
  "id": "AR-0302",
  "next_action": "Inspect @bitclub.ai/opendesk-cli commands and protocol version.",
  "owner": "",
  "plan": "../plans/AR-0302.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "open",
  "summary": "Support the bitclub OpenDesk CLI with its own dialect and compatibility record.",
  "task_revision": 2,
  "title": "Implement OpenDesk client adapter",
  "updated_at": "2026-09-06T21:04:14+00:00",
  "worktree_key": "agent-systems-benchmark-agent-opendesk"
}
---
## AR-0302

Support the bitclub OpenDesk CLI with its own dialect and compatibility record.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-06T21:04:14+00:00: Dependencies AR-0101 and AR-0102 are done; asb-agents OpenDesk paths
  are disjoint from active scheduler, workload, and comparability scopes, with shared Cargo/schema
  integration remaining fenced.
