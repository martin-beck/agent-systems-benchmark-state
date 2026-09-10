---
{
  "branch": "feature/tui-landing-screen",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1025", "AR-1033"],
  "id": "AR-1031",
  "next_action": "Implement the standalone landing screen after the application shell and visual system are integrated.",
  "owner": "",
  "plan": "../plans/AR-1031.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Add a state-aware landing screen with primary journeys and bounded recent activity.",
  "task_revision": 1,
  "title": "Build the standalone TUI landing screen",
  "updated_at": "2026-09-10T20:57:16+00:00",
  "worktree_key": "agent-systems-benchmark-asb-tui-landing-screen"
}
---
Build the actual landing screen in `martin-beck/asb-tui`, including authoritative connection/run
state, bounded recent activity, primary actions, empty/error/stale states and keyboard-first
navigation. No screen, widget, renderer or UI state belongs in the ASB repository.
