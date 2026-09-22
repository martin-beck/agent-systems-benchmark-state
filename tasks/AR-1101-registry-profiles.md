---
{
  "branch": "feature/registry-profiles",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-0310",
    "AR-0313",
    "AR-1100"
  ],
  "id": "AR-1101",
  "next_action": "Refactor the OpenAI and Ollama profile construction and adapter translation to be registry-driven after the registry exists.",
  "observed_branch": "feature/registry-profiles",
  "observed_dirty": 0,
  "observed_head": "298227a2379c03c651d2ef5a572c2954c07be933",
  "owner": "",
  "plan": "../plans/AR-1101.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Make provider profile construction and adapter translation fully registry-driven.",
  "task_revision": 2,
  "title": "Refactor provider profiles and translation to be registry-driven",
  "updated_at": "2026-09-22T10:16:40+00:00",
  "worktree_key": "agent-systems-benchmark-registry-profiles"
}
---
Remove the compile-time model constants from profile construction and adapter translation so that
profiles are built from validated registry entries while keeping every default settings digest and
translation byte-identical. Repository: `martin-beck/agent-systems-benchmark`.

- 2026-09-13T09:57:00+00:00: Frozen scope for parallel setup-wizard series AR-1100..AR-1106.
  All existing tests must pass unchanged because the default registry reproduces the current
  constants exactly.
