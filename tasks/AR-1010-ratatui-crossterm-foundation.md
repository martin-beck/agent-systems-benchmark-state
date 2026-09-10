---
{
  "branch": "feature/tui-ratatui-crossterm-foundation",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-10T06:28:12+00:00",
  "depends_on": [
    "AR-0803",
    "AR-0804",
    "AR-0805",
    "AR-0806"
  ],
  "id": "AR-1010",
  "next_action": "Run full exact-tree assurance gates on signed baseline repair 2754623; no publication.",
  "observed_branch": "feature/tui-ratatui-crossterm-foundation",
  "observed_dirty": 0,
  "observed_head": "2754623be3503589b24cbb84341dfcf65ccb8911",
  "owner": "replay_20260906",
  "plan": "../plans/AR-1010.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Adopt Ratatui and Crossterm as the supported professional TUI foundation.",
  "task_revision": 35,
  "title": "Adopt Ratatui/Crossterm TUI foundation",
  "updated_at": "2026-09-10T04:35:34+00:00",
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

- 2026-09-10T00:45:25+00:00: Recorded command exit 0; command argv SHA-256
  319d2f0fc8d18987d7bce2c0c125229deb7b0b73db1b2dbcae0b77d039bcbd49.

- 2026-09-10T00:46:03+00:00: Review-repair successor 9ba39a58c7e5492e1c69db642ff6c20e33192244 (tree
  a8535f8882dccff00cb66a8c901c8f3bb0991745, parent df92c0513f742ce3f22a7f2d8808441537cf3dbb) is
  SSH-signed, DCO-trailed, and clean. It uses checked_add so u64::MAX event cursors fail atomically;
  binds the runtime to an explicit owner-authenticated ControlClient socket with negotiated bounded
  polling and Connected/Control/Disconnected actions; injects terminal evidence for deterministic
  non-TTY behavior; and adds real util-linux pseudo-terminal success/error tests proving
  alternate-screen, cursor, bracketed-paste and raw-mode restoration boundaries. Focused fmt, 42
  library tests, 2 PTY integration tests, doctests, Clippy -D warnings, and diff-check pass. The
  earlier full workspace command was deliberately interrupted after review blockers arrived, so its
  partial output is not completion evidence; full exact-tree gates remain pending on this repaired
  successor.

- 2026-09-10T00:54:01+00:00: Recorded command exit 0; command argv SHA-256
  75b57252787825a94cf7b853b5167a648a63f339122730033b0e2ffac1309ec0.

- 2026-09-10T00:54:20+00:00: Recorded command exit 0; command argv SHA-256
  5aa65be359ee080f5775b933bf69f6a9044d7dda9f3e7d4256d9319e7d72ccbf.

- 2026-09-10T04:27:09+00:00: Recovered expired claim formerly owned by replay_20260906. Recover
  expired lease; preserve signed candidate 2754623 for full gates.

- 2026-09-10T04:28:12+00:00: Claimed by replay_20260906.

- 2026-09-10T04:28:25+00:00: Reclaimed preserved clean signed+DCO baseline repair
  2754623be3503589b24cbb84341dfcf65ccb8911, tree 5fc76ef3ec34f853daa535c31355e161729457cb, parent
  9ba39a58c7e5492e1c69db642ff6c20e33192244. Negotiated latest_revision now seeds AppState;
  standalone and negotiated first-event stale/skipped/max-wrap negatives plus real ControlServer
  page integration pass. Prior focused result: fmt, 43 library tests, 3 integration/PTY tests,
  doctests, Clippy -D warnings and diff-check green. Resume full gates without tree mutation.

- 2026-09-10T04:31:33+00:00: Recorded command exit 0; command argv SHA-256
  d46f7921bb52b7bf8c5ed90223d276cb43f20338b59e2b45da321e42dfccb691.

- 2026-09-10T04:32:17+00:00: Recorded command exit 0; command argv SHA-256
  1407de3dfbf71a2e295c370cf0dc36b693ab2c2c31b94de37de365085da8f647.

- 2026-09-10T04:33:06+00:00: Recorded command exit 0; command argv SHA-256
  104dbd73d6ae754c03b19a6c51c699468b087d5f2a628c13fb7659f9cdf0e947.

- 2026-09-10T04:33:29+00:00: Recorded command exit 101; command argv SHA-256
  2ff5122d559f8a5aa7c31b5b36cdb56e92e22d4fa902b7f27d1c5556df86d162.

- 2026-09-10T04:34:38+00:00: Recorded command exit 0; command argv SHA-256
  f8ab9b03d4dd2e71de52db4d4d7013fdac2d5d8e3ea952d63cb61e79558c1a21.

- 2026-09-10T04:35:34+00:00: Recorded command exit 7; command argv SHA-256
  91b8f6fe13559cc9d2bda605baebacc8395df29ef59597ee0ac6533ae15e0b07.
