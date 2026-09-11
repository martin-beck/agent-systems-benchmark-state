---
{
  "branch": "fix/tmux-alternate-screen-readiness",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [],
  "id": "AR-1042",
  "next_action": "Replace primary-pane readiness polling with isolated alternate-screen capture and bounded diagnostics, then rerun trusted-main qualification.",
  "owner": "",
  "plan": "../plans/AR-1042.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Make tmux TUI readiness capture deterministic on the actual alternate screen.",
  "task_revision": 1,
  "title": "Capture alternate-screen TUI readiness deterministically",
  "updated_at": "2026-09-11T00:42:00+00:00",
  "worktree_key": "agent-systems-benchmark-asb-tui-tmux-alternate-screen-readiness"
}
---

Trusted-main run 34546963576 failed twice because the probe captured tmux's primary pane while the
application rendered in alternate storage. Use a clean tmux server, alternate capture and bounded
diagnostics; do not change renderer or application semantics.
