---
{
  "branch": "codex/ar-1409-interactive-literature",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-24T18:15:18+00:00",
  "depends_on": [
    "AR-1408",
    "AR-1401"
  ],
  "id": "AR-1409",
  "next_action": "Promote after AR-1408 and AR-1401 are done; implement local deterministic adapters and catalog selection for AgentBench, tau-bench, and AgentDojo.",
  "observed_branch": "codex/ar-1409-interactive-literature",
  "observed_dirty": 0,
  "observed_head": "e4d8e7a70b2cce6f740bb8ababd145295ecc2665",
  "owner": "ar1409_interactive_literature_luna56",
  "plan": "../plans/AR-1409-interactive-literature-adapters.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Add offline-selectable interactive and tool-use literature workload adapters.",
  "task_revision": 4,
  "title": "Interactive literature workload adapters",
  "updated_at": "2026-09-24T15:16:56+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1409"
}
---

Live provider/backend connectivity is never required. Local deterministic or
LiteLLM-compatible mocks are the only development and CI execution path.

- 2026-09-24T15:09:21+00:00: Dependencies AR-1401 and AR-1408 are done; promote interactive
  literature adapters for local deterministic/mock execution.

- 2026-09-24T15:15:18+00:00: Claimed by ar1409_interactive_literature_luna56.
