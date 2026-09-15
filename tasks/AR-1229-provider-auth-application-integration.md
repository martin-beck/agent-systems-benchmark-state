---
{
  "branch": "feature/ar-1229-auth-application-integration",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-15T23:39:19+00:00",
  "depends_on": [
    "AR-1228",
    "AR-1230"
  ],
  "id": "AR-1229",
  "next_action": "Promote after AR-1228 and AR-1230 are complete; implement durable config registry and authenticated CLI/control enrollment integration, then requalify AR-1120.",
  "owner": "asb_ar1229_auth_application",
  "plan": "../plans/AR-1229.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Integrate provider authentication into ASB config, control and CLI surfaces.",
  "task_revision": 4,
  "title": "Provider authentication application integration",
  "updated_at": "2026-09-15T21:39:19+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1229-auth-application-integration"
}
---

Own the cross-crate application integration split from AR-1228. Do not add credential values to
public state or weaken the existing resolver and authenticated-control boundaries.

- 2026-09-15T18:20:00+00:00: Created after AR-1228 implementation review identified that durable
  config/registry and authenticated CLI/control enrollment are a separate cross-crate contract.

- 2026-09-15T21:38:42+00:00: Dependencies AR-1228 and AR-1230 complete; AR-1228 merged at
  efe741a75a8a3e7bd14afd8c6cef119f46a21c74 with all required checks green.

- 2026-09-15T21:38:45+00:00: Claimed by asb_ar1229_auth_application.

- 2026-09-15T21:39:19+00:00: Heartbeat by asb_ar1229_auth_application.
