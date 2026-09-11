---
{
  "branch": "fix/tmux-authenticated-startup-readiness",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [],
  "id": "AR-1050",
  "next_action": "Promote and claim the pre-approved test-only recovery, then add bounded stable authenticated tmux startup acquisition before option setup.",
  "owner": "",
  "plan": "../plans/AR-1050.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Wait for bounded stable authenticated tmux server, session and window readiness after detached creation.",
  "task_revision": 1,
  "title": "Acquire authenticated tmux startup readiness",
  "updated_at": "2026-09-11T03:06:00+00:00",
  "worktree_key": "agent-systems-benchmark-asb-tui-tmux-authenticated-startup-readiness"
}
---

Trusted-main run 34556679585 at exact merge aacf672c018706ef8a361e1a2dd6c19d890f02d8
passed 19 of 24 terminal tests, while all five live tmux fixtures completed new-session and then
failed the immediate server observation. Add bounded evidence-based startup acquisition with stable
server/session/window identity and retained pane authority. Change no renderer or application code.
