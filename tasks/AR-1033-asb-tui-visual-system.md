---
{
  "branch": "feature/tui-visual-system",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-0812", "AR-1010", "AR-1025"],
  "id": "AR-1033",
  "next_action": "Create the standalone Ratatui visual system after the application shell is integrated.",
  "owner": "",
  "plan": "../plans/AR-1033.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Create a responsive, accessible and professional visual system for every TUI screen.",
  "task_revision": 2,
  "title": "Establish the professional TUI visual system",
  "updated_at": "2026-09-10T21:04:37+00:00",
  "worktree_key": "agent-systems-benchmark-asb-tui-visual-system"
}
---
Create reusable themes, layouts and presentation widgets only in `martin-beck/asb-tui`, with exact
visual snapshots and accessible fallbacks. ASB must remain free of visual/rendering implementation.

- 2026-09-10T21:04:37+00:00: Added completed AR-0812 as migration input and made the visual,
  contrast and redraw evidence matrix numerically testable without reopening legacy ASB UI paths.
