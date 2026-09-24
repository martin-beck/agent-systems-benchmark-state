---
{
  "branch": "ci/ar-1216-tutorial-freshness",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-25T00:57:14+00:00",
  "depends_on": [
    "AR-1210",
    "AR-1211",
    "AR-1212",
    "AR-1213",
    "AR-1214",
    "AR-1215"
  ],
  "id": "AR-1216",
  "next_action": "Implement the repository-wide tutorial discovery and syntax-freshness CI gate after all tutorial contracts are defined.",
  "owner": "ar1216-tutorial-freshness-luna56",
  "plan": "../plans/AR-1216.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Continuously keep ASB tutorial commands and steps syntactically current.",
  "task_revision": 3,
  "title": "ASB tutorial freshness CI and documentation qualification",
  "updated_at": "2026-09-24T21:57:14+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1216"
}
---

Implement the linked CI gate. It validates syntax and fixtures only and must never execute a
tutorial command or require a provider/LLM connection.

- 2026-09-24T21:55:48+00:00: All tutorial contract predecessors AR-1210 through AR-1215 are durably
  done; promote repository-wide freshness CI implementation.

- 2026-09-24T21:57:14+00:00: Claimed by ar1216-tutorial-freshness-luna56.
