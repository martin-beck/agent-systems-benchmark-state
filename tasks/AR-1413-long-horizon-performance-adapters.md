---
{
  "branch": "codex/ar-1413-long-horizon-performance",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1408",
    "AR-1401"
  ],
  "id": "AR-1413",
  "next_action": "Claim after binding metadata; implement bounded adapters and truthful selectors for long-horizon and performance families.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "0000000000000000000000000000000000000000",
  "owner": "",
  "plan": "../plans/AR-1413-long-horizon-performance-adapters.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "open",
  "summary": "Add truthful long-horizon, refreshed, performance, and reproducibility workload adapters.",
  "task_revision": 2,
  "title": "Long-horizon and performance literature workload adapters",
  "updated_at": "2026-09-24T13:38:06+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1413"
}
---

Live provider/backend connectivity is never required. Development and CI use
bounded local fixtures or LiteLLM-compatible mocks only.

- 2026-09-24T13:38:06+00:00: Dependencies AR-1408 and AR-1401 are done; literature workload family
  adapter is dependency-ready.

- 2026-09-24T14:51:00+00:00: Coordinator bound declared isolated branch
  codex/ar-1413-long-horizon-performance and worktree agent-systems-benchmark-ar-1413 before claim.
