---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1408",
    "AR-1401"
  ],
  "id": "AR-1411",
  "next_action": "Promote after AR-1408 and AR-1401 are done; implement offline-selectable repository and terminal workload adapters.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "0000000000000000000000000000000000000000",
  "owner": "",
  "plan": "../plans/AR-1411-repository-terminal-adapters.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "open",
  "summary": "Add selectable, provenance-preserving repository-repair and terminal benchmark adapters.",
  "task_revision": 2,
  "title": "Repository and terminal literature workload adapters",
  "updated_at": "2026-09-24T13:37:58+00:00",
  "worktree_key": ""
}
---

Live provider/backend connectivity is never required. Development and CI use
bounded local fixtures or LiteLLM-compatible mocks only.

- 2026-09-24T13:37:58+00:00: Dependencies AR-1408 and AR-1401 are done; literature workload family
  adapter is dependency-ready.
