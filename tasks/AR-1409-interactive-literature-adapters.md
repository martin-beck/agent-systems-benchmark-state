---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1408", "AR-1401"],
  "id": "AR-1409",
  "next_action": "Promote after AR-1408 and AR-1401 are done; implement local deterministic adapters and catalog selection for AgentBench, tau-bench, and AgentDojo.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "0000000000000000000000000000000000000000",
  "owner": "",
  "plan": "../plans/AR-1409-interactive-literature-adapters.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "planned",
  "summary": "Add offline-selectable interactive and tool-use literature workload adapters.",
  "task_revision": 1,
  "title": "Interactive literature workload adapters",
  "updated_at": "2026-09-24T00:00:00+00:00",
  "worktree_key": ""
}
---

Live provider/backend connectivity is never required. Local deterministic or
LiteLLM-compatible mocks are the only development and CI execution path.
