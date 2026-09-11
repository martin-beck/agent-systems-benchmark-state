---
{
  "branch": "fix/tmux-startup-observation-diagnostics",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [],
  "id": "AR-1058",
  "next_action": "Add privacy-safe stable-startup and pane observation substages at exact asb-tui main 37613e81, obtain trusted-main evidence, then repair only the proven predicate.",
  "owner": "",
  "plan": "../plans/AR-1058.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Diagnose and repair the remaining trusted tmux stable-startup observation failure.",
  "task_revision": 1,
  "title": "Diagnose tmux startup observation",
  "updated_at": "2026-09-11T05:05:00+00:00",
  "worktree_key": "agent-systems-benchmark-asb-tui-tmux-startup-observation-diagnostics"
}
---

Trusted-main run 34564426538 at exact merge
37613e8128ac6ee2a6bc692fb8dea6bc031ba949 proved server acquisition succeeds but all five live tmux
fixtures still fail later at generic `tmux_startup_not_ready`. Add closed startup/pane substages
first, then repair only the observed portability gap. No renderer, UI, lifecycle protocol,
dependency, workflow or ASB source change is in scope.
