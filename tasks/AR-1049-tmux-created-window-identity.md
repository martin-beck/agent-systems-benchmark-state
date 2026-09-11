---
{
  "branch": "fix/tmux-created-window-identity",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-11T04:38:34+00:00",
  "depends_on": [],
  "id": "AR-1049",
  "next_action": "Promote and claim the pre-approved test-only recovery, then acquire and target the exact tmux window identity returned by new-session.",
  "owner": "codex-ar1049-tmux-window-identity-20260911",
  "plan": "../plans/AR-1049.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Bind tmux remain-on-exit setup to the exact created window identity instead of a fixed index.",
  "task_revision": 4,
  "title": "Bind tmux setup to its created window",
  "updated_at": "2026-09-11T02:38:51+00:00",
  "worktree_key": "agent-systems-benchmark-asb-tui-tmux-created-window-identity"
}
---

Trusted-main run 34555068496 at exact merge 6853d319469ad28ee9ff8b115b7c4c79da1ab777
passed 18 of 22 terminal tests but all four tmux fixtures rejected the fixed session:0 window
target. Acquire #{window_id} from each bounded creation, strictly validate it, target that immutable
ID, and preserve all established cleanup authority. Change no renderer or application behavior.

- 2026-09-11T02:38:31+00:00: Pre-approved P0 recovery is dependency-ready after trusted-main run
  34555068496 falsified fixed window-index targeting.

- 2026-09-11T02:38:34+00:00: Claimed by codex-ar1049-tmux-window-identity-20260911.

- 2026-09-11T02:38:51+00:00: Recorded command exit 0; command argv SHA-256
  871993554182fbd81a15e292265b972cf120013893cd0de80765f83de1cd07ac.
