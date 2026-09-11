---
{
  "branch": "fix/tmux-pane-foreground-group-recovery",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-11T03:24:35+00:00",
  "depends_on": [],
  "id": "AR-1044",
  "next_action": "Claim the task, create the declared isolated asb-tui worktree from exact merged main eb4960e, and implement foreground-group observation fixtures before integration changes.",
  "owner": "codex-ar1044-tmux-foreground-20260911",
  "plan": "../plans/AR-1044.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Bind tmux cleanup to the exact pane TTY foreground process group across acquisition and signalling.",
  "task_revision": 4,
  "title": "Recover tmux foreground-group qualification",
  "updated_at": "2026-09-11T01:25:21+00:00",
  "worktree_key": "agent-systems-benchmark-asb-tui-tmux-pane-foreground-group-recovery"
}
---

AR-1042 merged the reviewed test-only readiness repair as `eb4960e`, but trusted-main run
34550197610 proved that tmux's pane PID is not necessarily the pane's foreground process-group ID.
Recover the qualification without weakening ownership: acquire and retain one bounded exact
`pane_pid`/`pane_tty`/foreground-`tpgid` observation, and signal only after the same live tuple is
revalidated. Always clean the uniquely owned tmux server and socket even when group authority is
absent or changes. Do not change renderer or application behavior.


- 2026-09-11T01:24:35+00:00: Claimed by codex-ar1044-tmux-foreground-20260911.

- 2026-09-11T01:24:55+00:00: Recorded command exit 128; command argv SHA-256
  010ac80d31c060eeee068ab0f46eb6c978ebd81062aa03d4c7238b338840d59a.

- 2026-09-11T01:25:21+00:00: Recorded command exit 0; command argv SHA-256
  5a44054869e3537ce393c5cbc4da3dbf228826668ae93ab7a7fcd4c5f6179014.
