---
{
  "branch": "feature/tui-ux-quality",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-0870", "AR-0871", "AR-1010", "AR-1014", "AR-1031", "AR-1032", "AR-1033", "AR-1034", "AR-1035"],
  "id": "AR-1011",
  "next_action": "Integrate and qualify AR-1014 and AR-1031 through AR-1035, closing only cross-screen navigation, accessibility and usability defects after their focused implementations complete.",
  "owner": "",
  "plan": "../plans/AR-1011.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "planned",
  "summary": "Deliver an easy, discoverable, keyboard-first TUI experience for setup and benchmark analysis.",
  "task_revision": 6,
  "title": "Deliver TUI UX quality features",
  "updated_at": "2026-09-11T04:12:48+00:00",
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

- 2026-09-10T21:40:00+00:00: Marked AR-0870 and AR-0871 as read-only migration/behavior inputs;
  they cannot reopen implementation in legacy ASB frontend paths.

- 2026-09-11T04:12:48+00:00: Corrected the next action to integrated qualification rather than
  duplicating focused feature ownership and added mechanical focus/navigation graph acceptance.
