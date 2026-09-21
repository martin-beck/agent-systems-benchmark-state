---
{
  "branch": "feature/ar-1316-authenticated-agent-catalog-producer",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1190", "AR-1191", "AR-1310", "AR-1319"],
  "id": "AR-1316",
  "next_action": "Implement and publish the authenticated ASB AgentCatalog producer; keep unavailable entries explicit and prove exact TUI wizard compatibility.",
  "owner": "",
  "plan": "../plans/AR-1316.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "open",
  "summary": "Publish the verified ASB agent catalog required by the first-run setup wizard.",
  "task_revision": 1,
  "title": "Authenticated agent catalog producer",
  "updated_at": "2026-09-21T00:00:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1316-authenticated-agent-catalog-producer"
}
---

Current ASB main still returns `CapabilityUnavailable` for `ControlCall::AgentCatalog`,
so the already-merged asb-tui wizard cannot populate live supported coding-agent
choices. Implement the linked plan without changing the renderer or exposing secrets.
