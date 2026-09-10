---
{
  "branch": "feature/tui-ratatui-crossterm-foundation",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-10T01:43:48+00:00",
  "depends_on": [
    "AR-0803",
    "AR-0804",
    "AR-0805",
    "AR-0806"
  ],
  "id": "AR-1010",
  "next_action": "Run full workspace, formal, fault, privacy, policy, and supply gates on signed df92c05.",
  "observed_branch": "feature/tui-ratatui-crossterm-foundation",
  "observed_dirty": 4,
  "observed_head": "df92c0513f742ce3f22a7f2d8808441537cf3dbb",
  "owner": "replay_20260906",
  "plan": "../plans/AR-1010.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Adopt Ratatui and Crossterm as the supported professional TUI foundation.",
  "task_revision": 19,
  "title": "Adopt Ratatui/Crossterm TUI foundation",
  "updated_at": "2026-09-10T00:45:05+00:00",
  "worktree_key": "agent-systems-benchmark-tui-ratatui-crossterm-foundation"
}
---
## AR-1010

Adopt Ratatui with Crossterm as the supported ASB terminal UI foundation.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-09T23:43:45+00:00: All dependencies AR-0803, AR-0804, AR-0805, and AR-0806 are durably
  done. No remote branch, PR, or declared worktree exists. Owned asb-tui/workspace dependency scope
  is disjoint from active AR-0909 mini_swe.rs, AR-0859 OpenJiuwen live fixtures, and held formal
  lanes; no active Cargo/schema fence was found.

- 2026-09-09T23:43:48+00:00: Claimed by replay_20260906.

- 2026-09-10T00:26:45+00:00: Recorded command exit 0; command argv SHA-256
  32365df186a2a78c0fd3c125d218afd1ecfff97ce53e357fb3dcc527a42e60fc.

- 2026-09-10T00:33:19+00:00: Recorded command exit 101; command argv SHA-256
  ca0684257d947fe7f2e83a3345a15381ce96aba5098dc998474be630e3df1a58.

- 2026-09-10T00:34:23+00:00: Recorded command exit 101; command argv SHA-256
  4e84eb1a9203dfeb7502db0412b17939985d95374a4db8fd93545e54172a9c68.

- 2026-09-10T00:34:57+00:00: Recorded command exit 0; command argv SHA-256
  a1a9ac81601e06f5cfe2747a595d35b269b496b89eb23c33b4f92f92bb4d14f8.

- 2026-09-10T00:35:42+00:00: Recorded command exit 0; command argv SHA-256
  167094bba547a0cfc94b5b5ff1b2eefdaaba0cd6b1c44f022006f02efde5cdd1.

- 2026-09-10T00:36:14+00:00: Signed+DCO foundation checkpoint
  df92c0513f742ce3f22a7f2d8808441537cf3dbb (tree 7e101bd5d0a1f02deaa775447451c0b1aa0c95bb,
  parent/base b6d04a8305ce6d49cc327e4e6d2d6fa42a88050b) is clean in the declared isolated worktree.
  Six-path scope: Cargo.lock, asb-tui manifest, lib/main, and new app/runtime modules. Ratatui
  0.29.0 and matching sole Crossterm 0.28.1 are exact-pinned MIT dependencies; attempted Ratatui
  0.30.2 was rejected because its transitive serde_core 1.0.228 conflicts with the workspace exact
  serde 1.0.219, then corrected without weakening pins. The slice adds typed single-writer actions,
  atomic contiguous control-event projection, pure TestBackend rendering, stable non-TTY plain text,
  bounded resize/quit loop, and rollback/idempotent restoration on startup failure, normal exit,
  drop, and panic. Focused cargo check/test/Clippy and fmt pass; 40 asb-tui tests pass, dependency
  uniqueness/license assertions pass, non-TTY executable smoke passes, diff-check and clean-tree
  checks pass. Cargo lock change contains only the resolved Ratatui/Crossterm closure.

- 2026-09-10T00:42:58+00:00: Recorded command exit 0; command argv SHA-256
  bc34be9c1ef600c5e6d408b0f264a8e0e9c04ee7d81bffba39294acef6ff9363.

- 2026-09-10T00:44:39+00:00: Recorded command exit 101; command argv SHA-256
  bc34be9c1ef600c5e6d408b0f264a8e0e9c04ee7d81bffba39294acef6ff9363.

- 2026-09-10T00:45:05+00:00: Recorded command exit 0; command argv SHA-256
  bc34be9c1ef600c5e6d408b0f264a8e0e9c04ee7d81bffba39294acef6ff9363.
