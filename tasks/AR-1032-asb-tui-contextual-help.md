---
{
  "branch": "feature/tui-contextual-help",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1014", "AR-1031", "AR-1034", "AR-1035"],
  "id": "AR-1032",
  "next_action": "Add the contextual action registry, search field, fitted hotkey window and complete help coverage after the user-facing screens exist.",
  "owner": "",
  "plan": "../plans/AR-1032.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Provide a context-fitted hotkey window, global action search and mechanically complete help.",
  "task_revision": 1,
  "title": "Add contextual hotkeys and complete action help",
  "updated_at": "2026-09-10T20:57:16+00:00",
  "worktree_key": "agent-systems-benchmark-asb-tui-contextual-help"
}
---
Implement all hotkey, help-overlay, action-search and help-coverage behavior in the standalone
`asb-tui` application. ASB may advertise capabilities but must not render or own these interactions.
