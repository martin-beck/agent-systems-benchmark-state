---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1408", "AR-1401"],
  "id": "AR-1413",
  "next_action": "Promote after AR-1408 and AR-1401 are done; implement bounded adapters and truthful selectors for long-horizon and performance families.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "0000000000000000000000000000000000000000",
  "owner": "",
  "plan": "../plans/AR-1413-long-horizon-performance-adapters.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "planned",
  "summary": "Add truthful long-horizon, refreshed, performance, and reproducibility workload adapters.",
  "task_revision": 1,
  "title": "Long-horizon and performance literature workload adapters",
  "updated_at": "2026-09-24T00:00:00+00:00",
  "worktree_key": ""
}
---

Live provider/backend connectivity is never required. Development and CI use
bounded local fixtures or LiteLLM-compatible mocks only.
