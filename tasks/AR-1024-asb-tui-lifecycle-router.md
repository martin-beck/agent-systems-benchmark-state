---
{
  "branch": "feature/asb-tui-lifecycle-router",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-10T22:31:26+00:00",
  "depends_on": [
    "AR-0820",
    "AR-0821",
    "AR-0822",
    "AR-1022",
    "AR-1023"
  ],
  "id": "AR-1024",
  "next_action": "Implement typed asb tui dispatch, safe XDG state, signed channel and bundle acquisition, exact-byte lifecycle delegation, and adversarial tests without frontend or rendering code.",
  "observed_branch": "feature/asb-tui-lifecycle-router",
  "observed_dirty": 0,
  "observed_head": "32df706413a6f165f086941426a5c793bd5e01e8",
  "owner": "codex-ar1024-router-20260910",
  "plan": "../plans/AR-1024.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Add the trusted ASB-side bootstrap and lifecycle router for the optional frontend.",
  "task_revision": 8,
  "title": "Implement `asb tui` lifecycle routing",
  "updated_at": "2026-09-10T20:36:31+00:00",
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

- 2026-09-10T20:31:20+00:00: AR-1022 and AR-1023 are durably done; begin the trusted ASB-side
  lifecycle router without renderer or UI ownership.

- 2026-09-10T20:31:26+00:00: Claimed by codex-ar1024-router-20260910.

- 2026-09-10T20:32:17+00:00: Recorded command exit 0; command argv SHA-256
  1629c9f9a24c48825d6b7660c64f1bb238f910e17d68a4d23bb57a3efb94f807.

- 2026-09-10T20:34:34+00:00: Initial audit complete at exact ASB origin/main
  32df706413a6f165f086941426a5c793bd5e01e8. Read repository AGENTS, DEVELOPMENT, ARCHITECTURE,
  QUALITY, AR task/plan, current asb-cli/asb-bundle/control boundaries, and exact merged asb-tui
  d58eda9 lifecycle request/response/bundle contracts. First implementation target is
  crates/asb-cli/src/tui.rs with crates/asb-cli/tests/tui_lifecycle.rs; ASB will contain only
  trusted installation/lifecycle routing, never Ratatui/Crossterm/render/UI application code or a
  source link to asb-tui.

- 2026-09-10T20:35:59+00:00: Recorded command exit 1; command argv SHA-256
  bc1a8e34e1b3da829c192d079e163f6453d39b19ad42cea81cd9a33bf24802b8.

- 2026-09-10T20:36:31+00:00: Recorded command exit 2; command argv SHA-256
  b84823fb21760eb3782237a6d4cb3b2dd5929b7f0b5a350df8f49035886353b1.
