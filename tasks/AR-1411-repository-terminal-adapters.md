---
{
  "branch": "codex/ar-1411-repository-terminal",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-24T14:47:07+00:00",
  "depends_on": [
    "AR-1408",
    "AR-1401"
  ],
  "id": "AR-1411",
  "next_action": "Claim after binding metadata; implement offline-selectable repository and terminal workload adapters.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "0000000000000000000000000000000000000000",
  "owner": "ar1411_repository_terminal_luna56",
  "plan": "../plans/AR-1411-repository-terminal-adapters.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Add selectable, provenance-preserving repository-repair and terminal benchmark adapters.",
  "task_revision": 3,
  "title": "Repository and terminal literature workload adapters",
  "updated_at": "2026-09-24T14:17:07+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1411"
}
---

Live provider/backend connectivity is never required. Development and CI use
bounded local fixtures or LiteLLM-compatible mocks only.

- 2026-09-24T13:37:58+00:00: Dependencies AR-1408 and AR-1401 are done; literature workload family
  adapter is dependency-ready.

- 2026-09-24T14:16:00+00:00: Coordinator bound declared isolated branch
  codex/ar-1411-repository-terminal and worktree agent-systems-benchmark-ar-1411 before claim.

- 2026-09-24T14:17:07+00:00: Claimed by ar1411_repository_terminal_luna56.
