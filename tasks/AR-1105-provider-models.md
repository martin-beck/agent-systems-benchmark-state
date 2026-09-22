---
{
  "branch": "feature/provider-models",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1100"
  ],
  "id": "AR-1105",
  "next_action": "Add the read-only provider-models command with an optional bounded live probe after the registry exists.",
  "observed_branch": "feature/provider-models",
  "observed_dirty": 0,
  "observed_head": "bdd3997afb9f18b11359b3891b98d0cd6805efd4",
  "owner": "",
  "plan": "../plans/AR-1105.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "planned",
  "summary": "Add the read-only provider-models command with an optional bounded live probe.",
  "task_revision": 2,
  "title": "Add the provider model discovery diagnostic",
  "updated_at": "2026-09-22T10:16:40+00:00",
  "worktree_key": "agent-systems-benchmark-provider-models"
}
---
Add the read-only `asb provider-models` command that lists pinned registry models and, with
`--probe`, performs bounded live discovery for Ollama and OpenAI, always returning an explicit
unavailable reason and never auto-selecting a discovered model. Repository:
`martin-beck/agent-systems-benchmark`.

- 2026-09-13T09:57:00+00:00: Frozen scope for parallel setup-wizard series AR-1100..AR-1106.
  Shipped as a diagnostic: discovery never mutates the registry or config and requires no
  credentials; absence of a daemon or key yields a clean unavailable result.
