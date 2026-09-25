---
{
  "branch": "feature/ar-1442-guided-setup-wizard-orchestration",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1441", "AR-1316", "AR-1328", "AR-1436"],
  "id": "AR-1442",
  "title": "Guided setup wizard orchestration",
  "next_action": "Promote after dependencies are done; implement the shared catalog-driven first-run and reconfiguration contract for CLI and TUI.",
  "owner": "",
  "plan": "../plans/AR-1442.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Unify first-run and reconfiguration of agents, providers, auth methods, models and defaults in one guided flow.",
  "task_revision": 1,
  "updated_at": "2026-09-25T15:40:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1442-guided-setup-wizard-orchestration"
}
---

The wizard is a first-class product boundary, not a documentation layer. It
must delegate to authoritative ASB catalogs and runtime-owned credential
enrollment and remain safe when the provider is not reachable.
