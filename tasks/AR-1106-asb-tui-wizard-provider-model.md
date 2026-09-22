---
{
  "branch": "feature/asb-tui-wizard-provider-model",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1025", "AR-1033", "AR-1034", "AR-1102", "AR-1103"],
  "id": "AR-1106",
  "next_action": "Extend the TUI wizard with model selection, scope and default after the settings-wizard port and the product config contract exist.",
  "owner": "",
  "plan": "../plans/AR-1106.md",
  "priority": "P2",
  "schema_version": 1,
  "status": "planned",
  "summary": "Extend the TUI setup wizard with model selection, scope and default from the product registry.",
  "task_revision": 1,
  "title": "Extend the TUI wizard with provider model selection",
  "updated_at": "2026-09-13T09:57:00+00:00",
  "worktree_key": "agent-systems-benchmark-asb-tui-wizard-provider-model"
}
---
Extend the asb-tui setup wizard with model selection offered by the selected provider, the
default-vs-selected scope choice and the default provider/model for all agents, driven by the
product registry through a public read-only contract. Repository: `martin-beck/asb-tui`.

- 2026-09-13T09:57:00+00:00: Frozen scope for parallel setup-wizard series AR-1100..AR-1106.
  Registration in the asb-tui coordinator (sqlite-backed, on another development machine) is
  pending; this record tracks the scope here. Depends on the asb-tui settings-wizard foundation
  AR-1025, AR-1033 and AR-1034 and on the product UserConfigV1 and wizard AR-1102 and AR-1103.
