---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-24T16:25:00+00:00",
  "depends_on": [
    "AR-1408",
    "AR-1401"
  ],
  "id": "AR-1412",
  "next_action": "Promote after AR-1408 and AR-1401 are done; implement offline-selectable code-generation control adapters.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "0000000000000000000000000000000000000000",
  "owner": "ar1412_code_generation_luna56b",
  "plan": "../plans/AR-1412-code-generation-control-adapters.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Add selectable function-level and time-windowed coding controls without conflating their metrics.",
  "task_revision": 3,
  "title": "Code-generation control workload adapters",
  "updated_at": "2026-09-24T14:25:00+00:00",
  "worktree_key": ""
}
---

Live provider/backend connectivity is never required. Development and CI use
bounded local fixtures or LiteLLM-compatible mocks only.

- 2026-09-24T13:38:01+00:00: Dependencies AR-1408 and AR-1401 are done; literature workload family
  adapter is dependency-ready.

- 2026-09-24T14:25:00+00:00: Claimed by ar1412_code_generation_luna56b.
