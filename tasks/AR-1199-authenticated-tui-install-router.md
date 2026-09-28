---
{
  "branch": "feature/ar-1199-authenticated-tui-install-router",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-28T16:55:06+00:00",
  "depends_on": [
    "AR-1018",
    "AR-1019",
    "AR-1020",
    "AR-1190",
    "AR-1191",
    "AR-1496"
  ],
  "id": "AR-1199",
  "next_action": "Promote after AR-1496 successor evidence and all router dependencies are reconciled; implement the renderer-neutral authenticated CLI/control route and full integration tests.",
  "owner": "ar1199-router-impl",
  "plan": "../plans/AR-1199.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Expose an authenticated renderer-neutral ASB router for asb tui install and lifecycle operations.",
  "task_revision": 3,
  "title": "Authenticated TUI install router",
  "updated_at": "2026-09-28T14:55:06+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1199"
}
---

ASB does not currently dispatch a top-level `asb tui` command and its control backend returns
`CapabilityUnavailable` for the catalog/lifecycle calls. Implement the detailed plan only after
the pinned bundle, catalog, lifecycle, and configuration dependencies are complete. The actual
TUI executable, UI state, terminal handling, and rendering are owned by the standalone asb-tui
repository.

- 2026-09-28T14:53:05+00:00: Promoted after replacing historical blocked AR-1160 dependency with
  completed successor AR-1496; all router dependencies are done.

- 2026-09-28T14:55:06+00:00: Claimed by ar1199-router-impl.
