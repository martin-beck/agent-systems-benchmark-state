---
{
  "branch": "feature/ar-1199-authenticated-tui-install-router",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1018",
    "AR-1019",
    "AR-1020",
    "AR-1160",
    "AR-1190",
    "AR-1191"
  ],
  "id": "AR-1199",
  "next_action": "Promote only after dependencies are independently complete; implement the renderer-neutral authenticated CLI/control route and full integration tests.",
  "observed_head": "98acd6d5f5a206b351a54689e7817dd43af406ca",
  "owner": "",
  "plan": "../plans/AR-1199.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Expose an authenticated renderer-neutral ASB router for asb tui install and lifecycle operations.",
  "task_revision": 1,
  "title": "Authenticated TUI install router",
  "updated_at": "2026-09-15T00:00:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1199"
}
---

ASB does not currently dispatch a top-level `asb tui` command and its control backend returns
`CapabilityUnavailable` for the catalog/lifecycle calls. Implement the detailed plan only after
the pinned bundle, catalog, lifecycle, and configuration dependencies are complete. The actual
TUI executable, UI state, terminal handling, and rendering are owned by the standalone asb-tui
repository.
