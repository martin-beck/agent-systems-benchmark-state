---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1408",
    "AR-1401"
  ],
  "id": "AR-1412",
  "next_action": "Promote after AR-1408 and AR-1401 are done; implement offline-selectable code-generation control adapters.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "0000000000000000000000000000000000000000",
  "owner": "",
  "plan": "../plans/AR-1412-code-generation-control-adapters.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "open",
  "summary": "Add selectable function-level and time-windowed coding controls without conflating their metrics.",
  "task_revision": 2,
  "title": "Code-generation control workload adapters",
  "updated_at": "2026-09-24T13:38:01+00:00",
  "worktree_key": ""
}
---

Live provider/backend connectivity is never required. Development and CI use
bounded local fixtures or LiteLLM-compatible mocks only.

- 2026-09-24T13:38:01+00:00: Dependencies AR-1408 and AR-1401 are done; literature workload family
  adapter is dependency-ready.
