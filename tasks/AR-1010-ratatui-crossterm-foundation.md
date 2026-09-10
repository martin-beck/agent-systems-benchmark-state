---
{
  "branch": "feature/ratatui-crossterm-foundation",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-10T22:22:07+00:00",
  "depends_on": [
    "AR-0803",
    "AR-0804",
    "AR-0805",
    "AR-0806"
  ],
  "id": "AR-1010",
  "next_action": "Upstream Kasuari then Ratatui selectable std-map features; consume only after reviewed immutable releases eliminate foldhash.",
  "owner": "codex-ar1010-asb-tui-foundation-20260910",
  "plan": "../plans/AR-1010.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Adopt Ratatui and Crossterm as the supported professional TUI foundation.",
  "task_revision": 59,
  "title": "Adopt Ratatui/Crossterm TUI foundation",
  "updated_at": "2026-09-10T19:22:07+00:00",
  "worktree_key": "agent-systems-benchmark-asb-tui-ratatui-foundation"
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

- 2026-09-10T04:36:57+00:00: Recorded command exit 0; command argv SHA-256
  200d21f3406835cd9e805ca16b234098a04f5d89ad4835b0619d16f33ea8e2b8.

- 2026-09-10T04:38:16+00:00: Recorded command exit 0; command argv SHA-256
  044f447ce38981deb923b2b6e36871d2596bb89dca573429c0f9dccf63131b04.

- 2026-09-10T04:38:46+00:00: Recorded command exit 1; command argv SHA-256
  70ee4f26a98d45a10ff8b1e83e8061ee0ea6eb02629896c14354f021a3025aac.

- 2026-09-10T04:39:23+00:00: Full exact-tree checkpoint on signed head
  2754623be3503589b24cbb84341dfcf65ccb8911: PASS workspace fmt, Clippy -D warnings, locked
  tests/doctests, rustdoc -D warnings, release build; PASS formal locked Rust/Loom; PASS TLC 3,709
  states plus stale mutant and Alloy positive/six mutants; PASS mutation sentinels 7/7 caught after
  selecting pinned cargo-mutants 27.1.0 (initial exit 101 was environment-only missing PATH); PASS
  repository policy, contract consistency, actionlint, zizmor, Gitleaks, failure-path fixtures,
  platform manifest/46 tests, and coverage 95.13% regions/97.84% lines. BLOCKED candidate dependency
  closure: cargo deny rejects Ratatui 0.29 transitive foldhash Zlib license, duplicate
  hashbrown/rustix/linux-raw-sys/unicode-width/windows-sys versions, and unmaintained paste
  RUSTSEC-2024-0436; cargo audit additionally rejects lru 0.12.5 RUSTSEC-2026-0253 and
  RUSTSEC-2026-0002. These are candidate-introduced dependency findings, not runner/shared-harness
  failures. Candidate remains clean/unpublished; no policy weakening performed.

- 2026-09-10T04:41:36+00:00: Recorded command exit 101; command argv SHA-256
  73f5e3c8c9a763394b3bbc411a0128c7acaca536e96138023cd7fbfffcb32867.

- 2026-09-10T04:44:44+00:00: Recorded command exit 0; command argv SHA-256
  28fca62e27c74c5426006efac169616c4e41c38d6c7ff24f2a84eea7963aea21.

- 2026-09-10T04:45:12+00:00: Recorded command exit 1; command argv SHA-256
  f82e58d3f30e28aada0e5667bffa06b6632de31928f30ddfdb95a5d56b260edc.

- 2026-09-10T04:47:01+00:00: Recorded command exit 0; command argv SHA-256
  469c501bb2add52d86ceec70fa0a14abbabdeea01b210208d8328d5298c46161.

- 2026-09-10T04:47:22+00:00: Recorded command exit 6; command argv SHA-256
  8e8068be03669e44337cca402339d1fc1db5fafc725baa22d9df29ac999235de.

- 2026-09-10T04:49:06+00:00: Recorded command exit 101; command argv SHA-256
  778d24839e628dbba60fced334002b0eb6bac2dd44c28c9833724865068ad7e5.

- 2026-09-10T04:49:51+00:00: Dependency-closure repair exhausted without policy weakening. Ratatui
  0.30.0 with Crossterm 0.29 removes paste and old rustix/unicode-width duplicates, but fixed lru
  requires >=0.18.2 while 0.30.0 constrains lru ^0.16; time 0.3.44 is vulnerable
  (RUSTSEC-2026-0009). Ratatui 0.30.2 with exact serde 1.0.220, time 0.3.47 and lru 0.18.2 compiles
  the full locked workspace and clears all advisories, but cargo-deny still rejects unavoidable
  foldhash 0.2.0 Zlib and duplicate hashbrown 0.16.1/0.17.1: ratatui-core directly enables hashbrown
  0.17 defaults and kasuari directly enables hashbrown 0.16 defaults. Features cannot disable a
  transitive default feature. Older Ratatui 0.24-0.29 retain vulnerable/unmaintained lru/paste
  closures. All exploratory manifest/lock changes were mechanically restored; product is byte-clean
  at signed 2754623. No successor was committed and no policy was weakened.

- 2026-09-10T04:53:23+00:00: Read-only maintained-patch investigation: current Ratatui main
  99168f8afa2d75f89beeee17f0d15835010177c4 still declares hashbrown 0.17 and kasuari 0.4.9; current
  Kasuari main 4cf0b817a3c333c056a15df1d69c3829ceccbb14 still declares hashbrown 0.17 with defaults.
  Hashbrown 0.16/0.17 default-hasher is foldhash, so neither released 0.30.2 nor current maintained
  upstream has a feature boundary that removes Zlib. GitHub issue/PR search found only closed
  version-bump PRs ratatui#2084/#2495 and kasuari#32, no upstream no-foldhash patch. A local
  crates-io patch would require vendoring/reimplementing Ratatui Core, Widgets and Kasuari hash-map
  construction or a hashbrown compatibility shim, creating a large unmaintained fork and defeating
  the requested focused maintained dependency strategy; git patches would also violate deny.toml
  unknown-git policy. Concrete safe next step is an upstream Ratatui/Kasuari change exposing a
  policy-compatible hasher feature followed by immutable releases. Product remains clean at 2754623;
  no mutation justified.

- 2026-09-10T06:29:41+00:00: Recovered expired claim formerly owned by replay_20260906. Coordinator
  recovery: expired replay lease blocks all state publication; preserve signed candidate and reopen
  task for explicit reassignment.

- 2026-09-10T08:31:39+00:00: Claimed by replay_20260906.

- 2026-09-10T08:33:09+00:00: Upstream design checkpoint, ASB untouched: Ratatui main
  99168f8afa2d75f89beeee17f0d15835010177c4 and Kasuari main 4cf0b817a3c333c056a15df1d69c3829ceccbb14
  remain maintained but have no selectable non-Zlib closure. Hashbrown default-hasher is exactly
  dep:foldhash. Ratatui Core and Widgets use workspace hashbrown defaults; Kasuari uses
  HashMap/HashSet constructors through default hashbrown. A focused viable upstream sequence is: (1)
  Kasuari adds an opt-in std collection backend while declaring hashbrown default-features=false and
  retaining existing default behavior; release it. (2) Ratatui adds a matching feature, routes std
  builds to std collections in core/widgets and Kasuari, declares hashbrown default-features=false,
  retains backward-compatible default, and releases. ASB could then select the std backend with
  defaults disabled. No martin-beck forks currently exist, no upstream patch/release implements
  this, and direct Git/path/vendor consumption would violate maintained immutable-release and
  source-policy requirements. Product worktree remains byte-clean at 2754623.

- 2026-09-10T11:32:25+00:00: Recovered expired claim formerly owned by replay_20260906. Coordinator
  recovery after lease expiry blocked unrelated AR-1017 recording. Preserve clean signed product
  head 2754623be3503589b24cbb84341dfcf65ccb8911 and the recorded upstream immutable-release blocker;
  reopen without changing product or weakening dependency policy.

- 2026-09-10T19:13:56+00:00: Claimed by codex-ar1010-upstream-20260910.

- 2026-09-10T19:14:51+00:00: Repository boundary corrected before worker launch: preserve the
  unpublished ASB candidate only as historical evidence; all Ratatui/render/application work must
  continue in the existing asb-tui repository.

- 2026-09-10T19:20:00+00:00: Re-scoped all application, renderer, Ratatui/Crossterm runtime,
  terminal lifecycle, and UI test ownership to the existing martin-beck/asb-tui repository. The
  unpublished ASB product candidate is historical read-only evidence and must not be merged there.

- 2026-09-10T19:22:07+00:00: Claimed by codex-ar1010-asb-tui-foundation-20260910.
