---
{
  "branch": "feature/tui-ux-quality",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-0870", "AR-0871", "AR-1010", "AR-1014", "AR-1031", "AR-1032", "AR-1033", "AR-1034", "AR-1035"],
  "id": "AR-1011",
  "next_action": "Implement and test the keyboard-first search, navigation, help, accessibility, and progress UX on the Ratatui foundation.",
  "owner": "",
  "plan": "../plans/AR-1011.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "planned",
  "summary": "Deliver an easy, discoverable, keyboard-first TUI experience for setup and benchmark analysis.",
  "task_revision": 4,
  "title": "Deliver TUI UX quality features",
  "updated_at": "2026-09-10T21:04:37+00:00",
  "worktree_key": "agent-systems-benchmark-asb-tui-ux-quality"
}
---
## AR-1011

Deliver the high-value usability features on top of the adopted TUI foundation.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-10T19:20:00+00:00: Assigned every screen, widget, navigation action, and application
  test to the standalone asb-tui repository.

- 2026-09-10T20:57:16+00:00: Added focused landing, contextual help/hotkey, professional visual,
  configuration, and report/comparison AR dependencies so integrated UX qualification cannot pass
  on broad intentions alone. Grouped measurement selection remains explicitly owned by AR-1014.

- 2026-09-10T21:04:37+00:00: Removed premature AR-0807 qualification dependency and narrowed this
  AR to cross-screen integration and usability defect closure; focused ARs retain their screen and
  widget implementation ownership.
