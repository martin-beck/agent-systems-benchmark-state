---
{
  "branch": "fix/tmux-window-option-portability",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [],
  "id": "AR-1048",
  "next_action": "Promote and claim the pre-approved test-only recovery, then replace ambiguous remain-on-exit setup with the exact portable window-option command.",
  "owner": "",
  "plan": "../plans/AR-1048.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "open",
  "summary": "Use an explicit tmux window-option command so trusted-main terminal qualification is portable.",
  "task_revision": 2,
  "title": "Make tmux window-option setup portable",
  "updated_at": "2026-09-11T02:19:29+00:00",
  "worktree_key": "agent-systems-benchmark-asb-tui-tmux-window-option-portability"
}
---

Trusted-main run 34553880557 at exact merge `f5434c938883b4f756f525038dc1b6e6c0a90761`
passed 17 of 21 terminal tests but failed every tmux integration fixture at the ambiguous
`set-option -t <session> remain-on-exit on` command. Make the window-option namespace and exact
first-window target explicit, preserve bounded sanitized diagnostics and all established cleanup
authority, and change no renderer or application behavior.

- 2026-09-11T02:19:29+00:00: Pre-approved P0 test-only recovery is dependency-ready after
  trusted-main run 34553880557 exposed the portable window-option command requirement.
