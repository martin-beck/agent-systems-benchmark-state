---
{
  "branch": "feature/all-agents-provider",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-0311",
    "AR-0312"
  ],
  "id": "AR-0313",
  "next_action": "Add atomic all-agent provider selection with complete preflight capability reporting.",
  "owner": "",
  "plan": "../plans/AR-0313.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "open",
  "summary": "Let test plans select one provider profile for every chosen supported agent atomically.",
  "task_revision": 2,
  "title": "Configure one provider for all agents",
  "updated_at": "2026-09-08T11:13:52+00:00",
  "worktree_key": "agent-systems-benchmark-all-agents-provider"
}
---
## AR-0313

Let test plans select one provider profile for every chosen supported agent atomically.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-08T11:13:52+00:00: Highest-priority dependency-ready P1 after AR-1005 release: AR-0311 and
  AR-0312 are done. Scope fence: do not modify active AR-0844 path crates/asb-cli/src/control.rs or
  AR-0316 runtime-bundle paths; implement provider-plan/config/preflight surfaces only.
