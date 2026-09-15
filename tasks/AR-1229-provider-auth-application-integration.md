---
{
  "branch": "feature/ar-1229-auth-application-integration",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1228"],
  "id": "AR-1229",
  "next_action": "Promote after AR-1228 is complete; implement durable config registry and authenticated CLI/control enrollment integration, then requalify AR-1120.",
  "owner": "",
  "plan": "../plans/AR-1229.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Integrate provider authentication into ASB config, control and CLI surfaces.",
  "task_revision": 1,
  "title": "Provider authentication application integration",
  "updated_at": "2026-09-15T18:20:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1229-auth-application-integration"
}
---

Own the cross-crate application integration split from AR-1228. Do not add credential values to
public state or weaken the existing resolver and authenticated-control boundaries.

- 2026-09-15T18:20:00+00:00: Created after AR-1228 implementation review identified that durable
  config/registry and authenticated CLI/control enrollment are a separate cross-crate contract.
