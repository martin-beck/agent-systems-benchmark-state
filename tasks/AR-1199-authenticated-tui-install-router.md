---
{
  "branch": "feature/ar-1199-authenticated-tui-install-router",
  "checkpoint_commit": "45df6590cbf9ab75f07dcc0b753335949e28d937",
  "claim_expires": "",
  "depends_on": [
    "AR-1018",
    "AR-1019",
    "AR-1020",
    "AR-1190",
    "AR-1191",
    "AR-1496",
    "AR-1498"
  ],
  "id": "AR-1199",
  "next_action": "Blocked: authenticated renderer-neutral router and owner-only control transport are already on protected main; remaining AgentInstall/Status/Cancel/Retry/Remove backend is intentionally fail-closed at crates/asb-cli/src/control.rs:3088 because no lifecycle artifact executor/activation authority exists. Need an authorized lifecycle executor contract or successor AR before implementation.",
  "observed_branch": "feature/ar-1199-authenticated-tui-install-router",
  "observed_dirty": 0,
  "observed_head": "45df6590cbf9ab75f07dcc0b753335949e28d937",
  "owner": "",
  "plan": "../plans/AR-1199.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "blocked",
  "summary": "Expose an authenticated renderer-neutral ASB router for asb tui install and lifecycle operations.",
  "task_revision": 7,
  "title": "Authenticated TUI install router",
  "updated_at": "2026-09-28T15:00:25+00:00",
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

- 2026-09-28T14:55:49+00:00: Checkpoint: claimed AR at exact origin/main base; isolated worktree
  creation and renderer-neutral routing inspection are next.

- 2026-09-28T14:58:45+00:00: Inspection evidence: origin/main 45df659 contains asb tui router,
  SO_PEERCRED owner socket, broker handoff, control v1.4/v1.5 schemas, signed catalog refresh, and
  integration fixtures. RunnerBackend lifecycle calls explicitly return CapabilityUnavailable;
  AgentPackage exposes only digests/provenance, so claiming Active would be fabricated. No safe
  source mutation made.

- 2026-09-28T15:00:25+00:00: Blocked after exact-main inspection: authenticated router/owner-only
  transport and v1.4/v1.5 fixtures already exist, but lifecycle calls intentionally return
  CapabilityUnavailable because no authenticated artifact executor/activation authority exists.
  Focused tui_lifecycle and capability_contract tests passed 16/16; create a scoped
  lifecycle-executor successor AR before implementation.
