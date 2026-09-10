---
{
  "branch": "feature/asb-tui-lifecycle-router",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-0820", "AR-0821", "AR-0822", "AR-1022", "AR-1023"],
  "id": "AR-1024",
  "next_action": "Implement trusted release discovery, acquisition and typed `asb tui` lifecycle routing after the hardened lifecycle and capability contracts merge.",
  "owner": "",
  "plan": "../plans/AR-1024.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Add the trusted ASB-side bootstrap and lifecycle router for the optional frontend.",
  "task_revision": 1,
  "title": "Implement `asb tui` lifecycle routing",
  "updated_at": "2026-09-10T19:00:00+00:00",
  "worktree_key": "agent-systems-benchmark-asb-tui-lifecycle-router"
}
---
Implement `asb tui install`, launch, status, upgrade, doctor and remove without linking the frontend
into the ASB runtime. ASB owns trusted channel discovery and first verification; the exact verified
candidate independently reverifies and performs its transactional lifecycle.

Acceptance requires safe default XDG paths, signed immutable release selection, downgrade and
redirect resistance, bounded/resumable acquisition, offline support, typed delegation, network-free
status/launch/remove, removal of the legacy bundled-TUI bootstrap assumption, adversarial tests,
complete gates, exact-head CI and post-merge verification.
