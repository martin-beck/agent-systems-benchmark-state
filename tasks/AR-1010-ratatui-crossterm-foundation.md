---
{
  "branch": "feature/ratatui-crossterm-foundation",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-11T01:38:35+00:00",
  "depends_on": [
    "AR-0803",
    "AR-0804",
    "AR-0805",
    "AR-0806",
    "AR-1030"
  ],
  "id": "AR-1010",
  "next_action": "Run full exact-tree asb-tui gates, review and sign the trust-boundary successor, push PR #9, then wait for exact-head CI and a fresh independent reviewer; no merge.",
  "owner": "codex-ar1010-trust-repair-20260911",
  "plan": "../plans/AR-1010.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Adopt Ratatui and Crossterm as the supported professional TUI foundation.",
  "task_revision": 352,
  "title": "Adopt Ratatui/Crossterm TUI foundation",
  "updated_at": "2026-09-10T23:50:27+00:00",
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

- 2026-09-10T19:22:16+00:00: Recorded command exit 0; command argv SHA-256
  5ad2ffa7a9f242ef20c018a5e85bcb50de039a7041977f9430a4f0c0c1edfad1.

- 2026-09-10T19:23:19+00:00: Recorded command exit 0; command argv SHA-256
  8a508d2671df28ddefaf5ccb619999d66039a79bcbaaacbba9cd838724691bd7.

- 2026-09-10T19:23:29+00:00: Heartbeat by codex-ar1010-asb-tui-foundation-20260910.

- 2026-09-10T19:23:52+00:00: Correct stale pre-migration next action: implementation ownership is
  the standalone asb-tui repository; ASB candidate 2754623 remains read-only evidence.

- 2026-09-10T19:25:28+00:00: Recorded command exit 127; command argv SHA-256
  8a0f78ce55aa89c2fb2a4a98dc84d882734c107a28e9d74a218c90b66f057efe.

- 2026-09-10T19:26:17+00:00: Recorded command exit 0; command argv SHA-256
  dbbaa209260728d1a217f14dd3402f0316aa747eb2f46983f859e3b7a2a95216.

- 2026-09-10T19:28:39+00:00: Recorded command exit 0; command argv SHA-256
  47d91ea44aeacc9274815b90225a4ede29b288661ba230ab1c2eadf0dd91b90c.

- 2026-09-10T19:32:40+00:00: Recorded command exit 101; command argv SHA-256
  b7155dd1c773246c8eaef63aa7cbfba20fbf19e7680696ea2f78beb41648dd3c.

- 2026-09-10T19:32:58+00:00: Recorded command exit 0; command argv SHA-256
  75af878b9c9e19eb01582402fc1cef28a9e1a32c00c867ac240ea202b7966616.

- 2026-09-10T19:33:24+00:00: Recorded command exit 0; command argv SHA-256
  a0e810f66e286ce155f4e312e38adb8e50372feed3e81cfbffb948b5d5be43ba.

- 2026-09-10T19:33:35+00:00: Recorded command exit 0; command argv SHA-256
  efa8f505100deb73d47753f99ae3296bc7997d2fdd7bd56bdbf8c3defa72b907.

- 2026-09-10T19:34:40+00:00: Recorded command exit 0; command argv SHA-256
  75af878b9c9e19eb01582402fc1cef28a9e1a32c00c867ac240ea202b7966616.

- 2026-09-10T19:35:13+00:00: Recorded command exit 0; command argv SHA-256
  53729b7a6a749e4dd59e82f8588dbc80dd5a6a0d00aa701e86887a1fa5d3b723.

- 2026-09-10T19:37:37+00:00: Recorded command exit 0; command argv SHA-256
  30780b055b39980601a387da385afed08d1464fa83fb1337cdb92f2f9bbf056d.

- 2026-09-10T19:37:46+00:00: Recorded command exit 0; command argv SHA-256
  a8329c02ae8a3ba91c34f932a2fe9e61cf8e591ef89ee59328ac50a987eacb88.

- 2026-09-10T19:38:05+00:00: Recorded command exit 0; command argv SHA-256
  dbbaa209260728d1a217f14dd3402f0316aa747eb2f46983f859e3b7a2a95216.

- 2026-09-10T19:38:24+00:00: Recorded command exit 0; command argv SHA-256
  8a508d2671df28ddefaf5ccb619999d66039a79bcbaaacbba9cd838724691bd7.

- 2026-09-10T19:38:34+00:00: Recorded command exit 0; command argv SHA-256
  44009fe24f778415b2bde487104310caf5dd5ef53a6bb6a8bc5338f60d8285b1.

- 2026-09-10T19:38:44+00:00: Recorded command exit 0; command argv SHA-256
  464bd884077c37ac362c9293005faf11a6c7b5bdc7f53ca7ee789e825a2afe12.

- 2026-09-10T19:39:01+00:00: Recorded command exit 0; command argv SHA-256
  3c9eb98e3d66ea2e3f79abe6438968413e8ed54c748a883c3423cb5614f066df.

- 2026-09-10T19:40:58+00:00: Recorded command exit 0; command argv SHA-256
  9ccc3cc99f31a240a7ec2e908d93c2e3be22ed0ff67c55f0c7fddc9dbedbbb9e.

- 2026-09-10T19:41:28+00:00: Recorded command exit 0; command argv SHA-256
  e65b7e6f1260eabd114a54369ae6e79b835cf433f96332e4b7f5fd6e7e65a2c5.

- 2026-09-10T19:41:39+00:00: Recorded command exit 0; command argv SHA-256
  69376b012117bbf4080a7aecf84cb2763ac9806d8847e617c332af41440dabdc.

- 2026-09-10T19:41:52+00:00: Recorded command exit 1; command argv SHA-256
  2f2f23f44b37a94089f12b279b73dd1c170ae7b03a0f5068425f6e6cca7d019a.

- 2026-09-10T19:42:11+00:00: Recorded command exit 0; command argv SHA-256
  14a12adf6d10f64f818e203d2238ebe0031c9b5d06351431ff4d62da9982cadf.

- 2026-09-10T19:42:52+00:00: Recorded command exit 1; command argv SHA-256
  f7e2811dc64e0674f26d41041d97bb7ef35ffebce81fa4f218c2ea752d4b6459.

- 2026-09-10T19:43:52+00:00: Recorded command exit 0; command argv SHA-256
  a4cade1a09446e76a9665f13e0d7f65d86e2017c958b59f462f871ba3e2e0051.

- 2026-09-10T19:44:17+00:00: Recorded command exit 0; command argv SHA-256
  0b17974575dc4f222795a407d4983560127c4503d05536b1b46d8fbd6e298a3a.

- 2026-09-10T19:44:31+00:00: Recorded command exit 0; command argv SHA-256
  4cdae0ba7e16e538f9ee317b6b01a213f04e342b25901fa4b0416f63456df038.

- 2026-09-10T19:44:42+00:00: Recorded command exit 0; command argv SHA-256
  335f70c40ce1954efe5c73ba938bab2662fa24a8e0031745582c5d938f593c70.

- 2026-09-10T19:45:06+00:00: Recorded command exit 0; command argv SHA-256
  70fee75bee540ad56dd9513b90d9fbd095ec6fa798af3f8715832cce5d628a62.

- 2026-09-10T19:45:27+00:00: Signed+DCO standalone checkpoint
  9b3f9fb3e1f52cf0a80c67f89d5dd44356310621 is pushed in draft PR 9. It adds exact-pinned
  policy-clean Crossterm 0.29, deterministic Action/AppState/frame projection, privacy-safe terminal
  policy and doctor, rollback-safe terminal lifecycle, PTY normal/panic restoration tests, exact
  SBOM closure, and 90.75% line coverage. Full fmt, Clippy -D warnings, locked tests/doctests,
  rustdoc, release build, cargo-deny, cargo-audit, schema/publication/channel, shell/workflow, and
  secret gates pass. Ratatui 0.30.2 remains absent: fresh cargo-deny rejects foldhash 0.2.0 Zlib
  plus unavoidable hashbrown 0.16.1/0.17.1 and syn 2.0.119/3.0.5 duplicates; cargo-audit is clean.
  No policy weakening or ASB product change was made; AR remains incomplete.

- 2026-09-10T19:46:13+00:00: Evidence correction: the exact signed+DCO standalone checkpoint and
  pushed PR 9 head is 9b3f9fb746b3ac8a17a7b9ea7541f621650969e8. The prior note transcribed an
  incorrect full object ID; do not use it.

- 2026-09-10T19:46:28+00:00: Recorded command exit 0; command argv SHA-256
  a7c2491006dea572fd657f061af914fd043601421c596c8f472ef97ad4801088.

- 2026-09-10T19:46:42+00:00: Live GitHub verification: draft PR 9 is MERGEABLE at exact head
  9b3f9fb746b3ac8a17a7b9ea7541f621650969e8, and its Repository quality / Rust, supply-chain, and
  privacy gates check completed SUCCESS at 2026-09-10T19:45:54Z. AR remains in_progress because no
  Ratatui renderer exists.

- 2026-09-10T19:47:31+00:00: Clean signed checkpoint is preserved in draft PR 9; release worker
  lease while a separate dependency-resolution AR is authored. AR-1010 remains incomplete and must
  not merge as a finished renderer.

- 2026-09-10T19:50:00+00:00: Added AR-1030 as an explicit prerequisite for the unresolved Ratatui
  release dependency closure. Draft PR 9 remains a non-rendering checkpoint and cannot complete
  this AR until AR-1030 is reviewed and integrated.

- 2026-09-10T20:23:48+00:00: AR-1030 is durably done at verified asb-tui main with the exact Ratatui
  closure; resume standalone renderer work only in asb-tui.

- 2026-09-10T20:24:05+00:00: Claimed by codex-ar1010-asb-tui-renderer-20260910.

- 2026-09-10T20:24:39+00:00: Recorded command exit 0; command argv SHA-256
  622ad1cb102e06262b27e10ee1bcc9eae761fd9cb9ce2104ffe6200b5c671720.

- 2026-09-10T20:24:59+00:00: Recorded command exit 0; command argv SHA-256
  f20c001a878962c9fa1a1f71493f66039bae364eb86300f1dff0e424c2d03939.

- 2026-09-10T20:25:17+00:00: Recorded command exit 1; command argv SHA-256
  324747991c02dd14c530cedae418b72838d7169b822f906bb9d9310045783b95.

- 2026-09-10T20:25:38+00:00: Recorded command exit 0; command argv SHA-256
  7ea2b27ee2a926afe1442d81ced64932a6cb0a0378166fe3191f632fd3aac94b.

- 2026-09-10T20:26:13+00:00: Recorded command exit 0; command argv SHA-256
  26646bccde089b649e633ec376f9743d127cc130d69052e10e1901fdc9dedb6f.

- 2026-09-10T20:26:34+00:00: Recorded command exit 0; command argv SHA-256
  bdd315c3a7c062f72460901728d9467ee4bdecb6f29b883dcfa088fa69b9cd90.

- 2026-09-10T20:26:56+00:00: Recorded command exit 0; command argv SHA-256
  ec5b37f30a288496e6655be7a241825acf215e937626af759510226d992ba26e.

- 2026-09-10T20:29:55+00:00: Recorded command exit 0; command argv SHA-256
  f13ac9689ebd4b8f709beeacf4e09f335c420e8f3461551a63e6eafc37180cc6.

- 2026-09-10T20:30:42+00:00: Recorded command exit 0; command argv SHA-256
  9169ab41bd8b0c84eb5fb8468dd7db89ee87beef62ec8cdeed3aa718e55e2ec6.

- 2026-09-10T20:31:10+00:00: Recorded command exit 0; command argv SHA-256
  d235eb08ffebc47d63947fd47f215eff100930ddc8a24e4f0c873af96453e21f.

- 2026-09-10T20:31:35+00:00: Recorded command exit 101; command argv SHA-256
  8e494adc1ca9af2df5d2b592b059737826a8750fdcd4d4b7697c3ea4d7cfd5bf.

- 2026-09-10T20:32:40+00:00: Recorded command exit 0; command argv SHA-256
  ab6c9ec8182b93ae2021186b1f8ec59321fdbb913e9a2368c116c88741cde63a.

- 2026-09-10T20:32:59+00:00: Recorded command exit 101; command argv SHA-256
  799ea9bb38aeded2140cd9f1acf888d50e4c458766452114dbb8c2231740eb65.

- 2026-09-10T20:33:16+00:00: Recorded command exit 0; command argv SHA-256
  f51bd07f4caf8376a0631592c3563c801cf9a1c6391cf505260ae5bf28d25a0c.

- 2026-09-10T20:33:35+00:00: Recorded command exit 0; command argv SHA-256
  e126385611f18a7bf329b2b15040932e97742c64dbde502b0326026102fc4c26.

- 2026-09-10T20:33:59+00:00: Recorded command exit 1; command argv SHA-256
  6443ca3c6ac2e214a22540e3cd8d2895066f4e8ee058cb2e3c0eecf3130d76d5.

- 2026-09-10T20:34:23+00:00: Recorded command exit 0; command argv SHA-256
  9a5e59e110978822f023fa0477964c98dc648ea0c0bc88f69cb91e581570880f.

- 2026-09-10T20:34:38+00:00: Recorded command exit 0; command argv SHA-256
  ff571cd8b664f1afd4d7754cfe344edee6df451d8eb184fa9cdd18a05c30c685.

- 2026-09-10T20:35:00+00:00: Recorded command exit 0; command argv SHA-256
  1135be4c3cbee63355d31eecf57ebc6cd8a7699d496e8a3094974f027caa8583.

- 2026-09-10T20:35:16+00:00: Recorded command exit 0; command argv SHA-256
  69df4e9d3332b1ec4ac3d3bfcaa8d2443e3bb20c51e2087e41dfbe32bfba996f.

- 2026-09-10T20:35:35+00:00: Recorded command exit 0; command argv SHA-256
  593530a8e9e088a0582082f85d60465bc95edb14b99d27908f1ffe1a33810e53.

- 2026-09-10T20:35:51+00:00: Recorded command exit 101; command argv SHA-256
  4da9d18a2e10bbdf0b4f64c125cabc994451bd57d493ad8d44ac425c3ff47674.

- 2026-09-10T20:36:07+00:00: Recorded command exit 0; command argv SHA-256
  135c89365410f77f3b2573b4f68036a457299c32baea023aa60f5db81a982a5a.

- 2026-09-10T20:36:50+00:00: Recorded command exit 0; command argv SHA-256
  9072dcbefef94ed18ca672d11960b5410e02c12f6279b921c8ec62a8b87f6ee2.

- 2026-09-10T20:37:14+00:00: Recorded command exit 101; command argv SHA-256
  4da9d18a2e10bbdf0b4f64c125cabc994451bd57d493ad8d44ac425c3ff47674.

- 2026-09-10T20:37:30+00:00: Recorded command exit 0; command argv SHA-256
  91d6f260aa75ac21bd408ba81f64b008e1b0bd56ba30a07c98c53e41d41d025c.

- 2026-09-10T20:37:53+00:00: Recorded command exit 0; command argv SHA-256
  651e0a7aa15c7c03482ea9946ac5a346795e2fef20e922986bdd2dd15f8e292e.

- 2026-09-10T20:38:14+00:00: Recorded command exit 101; command argv SHA-256
  4da9d18a2e10bbdf0b4f64c125cabc994451bd57d493ad8d44ac425c3ff47674.

- 2026-09-10T20:38:44+00:00: Recorded command exit 0; command argv SHA-256
  c5c60f57a81c14d47cde302644d95a3bca4a9a0cff2e604ecdf2f62dba858665.

- 2026-09-10T20:39:00+00:00: Recorded command exit 0; command argv SHA-256
  4da9d18a2e10bbdf0b4f64c125cabc994451bd57d493ad8d44ac425c3ff47674.

- 2026-09-10T20:39:45+00:00: Recorded command exit 0; command argv SHA-256
  6d8c2aba405ce53a689b44bd3691a28318676951066e71ab8b652da3a20a7b9c.

- 2026-09-10T20:39:59+00:00: Recorded command exit 0; command argv SHA-256
  67f70edbc9e5263dc4e306365305c1c05e0d935eb403fef8a01c92fb51bcb433.

- 2026-09-10T20:41:02+00:00: Recorded command exit 1; command argv SHA-256
  b583b79621adeaea845f7a7a3598ab9f848d43bf03cc6b7b5ec19ad79ad3efc1.

- 2026-09-10T20:41:24+00:00: Recorded command exit 1; command argv SHA-256
  91ae708febe4ade26cc9e61690e773729830930233a9c8f4115d381f2e8a03e9.

- 2026-09-10T20:41:43+00:00: Recorded command exit 1; command argv SHA-256
  e0af3ba1ceb77dacef6f9fed8f4c0f799d2277699aa9a681400584e196116d1f.

- 2026-09-10T20:42:05+00:00: Recorded command exit 0; command argv SHA-256
  f3c3500a041931d05cbfbe699df50ee45d4381594d0bac8bd5a5d3e955534d98.

- 2026-09-10T20:42:24+00:00: Recorded command exit 1; command argv SHA-256
  ecbd5e538741c9f376667bbf8f0e8276ce96be697389785b461d9f685a29770b.

- 2026-09-10T20:42:48+00:00: Recorded command exit 0; command argv SHA-256
  76ff073f81e842fd97e9f72b694c5530244d96af387d5fc7b63b875f65dd1607.

- 2026-09-10T20:43:44+00:00: Recorded command exit 0; command argv SHA-256
  221b1f7a309ff87128fb9b323b22fe0066d62fe5f4c2aa45f3f4018b9a2a3cf4.

- 2026-09-10T20:45:36+00:00: Recorded command exit 0; command argv SHA-256
  b6cde6a38960710859ec6e2e75bbc28257290fcdc592cad88cdf2248ff0d1e05.

- 2026-09-10T20:46:26+00:00: Recorded command exit 0; command argv SHA-256
  48128b619d0f47878f4baaccf5aa73cb6635699e4137ea8e57f8cf2cbe1f351d.

- 2026-09-10T20:47:44+00:00: Recorded command exit 0; command argv SHA-256
  459c11821aa07136a63397f0882b7417f26a066f911ab3c0d31ecbd0b43b2e37.

- 2026-09-10T20:48:14+00:00: Recorded command exit 0; command argv SHA-256
  be2aa3b18dce6ba23a8f34c105a8e2717e6d339eb2d5d423d54030173ab95261.

- 2026-09-10T20:48:39+00:00: Recorded command exit 101; command argv SHA-256
  a4a54adc80f74104bbc334889b07b0852e4d7aa44110d9797fa9821e9cfbc015.

- 2026-09-10T20:49:00+00:00: Recorded command exit 0; command argv SHA-256
  b8693630f8612a817d74687474ee8f3cd57f5d5aa7963a2dab83b302199076d6.

- 2026-09-10T20:49:33+00:00: Recorded command exit 0; command argv SHA-256
  a4a54adc80f74104bbc334889b07b0852e4d7aa44110d9797fa9821e9cfbc015.

- 2026-09-10T20:51:06+00:00: Recorded command exit 0; command argv SHA-256
  8a508d2671df28ddefaf5ccb619999d66039a79bcbaaacbba9cd838724691bd7.

- 2026-09-10T20:51:19+00:00: Recorded command exit 0; command argv SHA-256
  ba2d737487721239e589fdc4779e8bd9f4c7887c2332bf1a1d292b4710d54ffd.

- 2026-09-10T20:51:32+00:00: Recorded command exit 0; command argv SHA-256
  53a0e6190b0778119fb7625df6b13e1dd0abe9719f66d2510d5f7c3dde91cbe1.

- 2026-09-10T20:51:45+00:00: Recorded command exit 0; command argv SHA-256
  d03f447352e0c44ea4fdc1a8f47e10c2e3eb850542b905c89b9fec20300cc67e.

- 2026-09-10T20:52:15+00:00: Recorded command exit 101; command argv SHA-256
  074af5b28a2ac840114923c3c22f7fb41dc920d60ce79da999b410878faf27d0.

- 2026-09-10T20:52:30+00:00: Recorded command exit 0; command argv SHA-256
  f84a3ba0f8009898e2cda344fa9b106a2949b6ef8e6976330075c3695cbb8b4e.

- 2026-09-10T20:52:46+00:00: Recorded command exit 0; command argv SHA-256
  9ed6b0d0efc4e1aab607d8906a56bf123504942e9c8c0f00e6ab5c8110fd7b32.

- 2026-09-10T20:53:10+00:00: Recorded command exit 2; command argv SHA-256
  48458d4adcbc2714c4ae60f17ec39d916357031118af6e75d9a5cd826c73f20e.

- 2026-09-10T20:53:47+00:00: Recorded command exit 2; command argv SHA-256
  666f6ff33801b199be1662e3e8cd89e5c23d02156c08dbf03ab751c96716c7a6.

- 2026-09-10T20:54:23+00:00: Recorded command exit 0; command argv SHA-256
  7b5c002fe04a9a682e42ffe7ab001e0c29007288a494b6ea04df0be02c58a13d.

- 2026-09-10T20:54:44+00:00: Recorded command exit 0; command argv SHA-256
  ed0202cab60d3aaddd8c239c8f92eea24c29176a2159c73f13f4b9de580b33f0.

- 2026-09-10T20:54:59+00:00: Recorded command exit 0; command argv SHA-256
  ca42c42481a877d594741d2b9227cb0c8a49e0198ffa5b5f6bd288ceda957dd5.

- 2026-09-10T20:55:23+00:00: Recorded command exit 101; command argv SHA-256
  074af5b28a2ac840114923c3c22f7fb41dc920d60ce79da999b410878faf27d0.

- 2026-09-10T20:55:36+00:00: Recorded command exit 0; command argv SHA-256
  de4b17650981954cb55d0e115c3b0089257981b3556eaad954e1e240df681ede.

- 2026-09-10T20:55:47+00:00: Recorded command exit 0; command argv SHA-256
  95b4ddb70131e3302a07e075dd8dfc3bc7ec0312e0888591ee3d115f81131362.

- 2026-09-10T20:56:05+00:00: Recorded command exit 0; command argv SHA-256
  797c15ab2f117c5d60d8530ade854e3707f7d17fde8db6679df2dbd66f14e5fb.

- 2026-09-10T20:56:38+00:00: Recorded command exit 0; command argv SHA-256
  7db572fe8692d7ad572f0d836864a1fd26e122d768e025514c18f1bc3e9e978a.

- 2026-09-10T20:56:50+00:00: Recorded command exit 0; command argv SHA-256
  4b2bd9d3a8ea9ee947b440a09c2407da15bdb36566b60ae06306724453569daa.

- 2026-09-10T20:57:41+00:00: Recorded command exit 0; command argv SHA-256
  0e9adcac2b78dda2bd7aa2cabbb993992bd967e61637632c5715e10a35063adb.

- 2026-09-10T20:58:32+00:00: Recorded command exit 0; command argv SHA-256
  5e269a920cb46fb9ee2b2b9d552194a0633ee982f79aa5910c316b47ecbecab3.

- 2026-09-10T20:58:47+00:00: Recorded command exit 0; command argv SHA-256
  92a2fb010907e4b4fd89869cfa2234caf8cc93019f73b293082947ec53951133.

- 2026-09-10T20:59:30+00:00: Full cargo suite initially exposed two stale tests, not product
  failures: the pre-handoff launcher test expected success without a controlling terminal, and a
  release-lock negative mutation still targeted the former unavailable classification. Both were
  repaired to test the current fail-closed contracts. Focused lifecycle/renderer/PTY tests and the
  subsequent complete cargo fmt, clippy, test, rustdoc, and release build are green. Independent
  review found a genuine partial-startup restoration edge; terminal effects are now issued and
  tracked individually, failed cleanup flags remain active for retry, and injected tests cover
  failure at raw enable, alternate-screen entry, cursor hiding, paste enablement, and restoration
  retry. PTY coverage proves exact memfd frontend bytes render on the controlling terminal, q exits,
  restoration completes, and lifecycle stdout remains exactly one parseable JSON response.

- 2026-09-10T20:59:44+00:00: Recorded command exit 2; command argv SHA-256
  e2354a3fdf988ccf08274251440890581e2ca91ad05f25077e6692f18478a2a1.

- 2026-09-10T21:00:20+00:00: Recorded command exit 0; command argv SHA-256
  33b6a8c90c4f38898bdf451d31fb03666481b8cd87dec61f1d767c25a2495e22.

- 2026-09-10T21:00:46+00:00: Recorded command exit 0; command argv SHA-256
  1def88c18288b4a50114b5ebd7ea4586e932a6dc2ac1a117d44a0cff8c57ba51.

- 2026-09-10T21:01:05+00:00: Recorded command exit 0; command argv SHA-256
  eba9bb461ff8deda75818c4ce3c74682fe32d67b29eb95031ed6c5bb2cd04366.

- 2026-09-10T21:01:23+00:00: Recorded command exit 0; command argv SHA-256
  0b6c664bbfbd470df9dfad888530247cd04b9c89f25052ecd1e366cf153563b0.

- 2026-09-10T21:01:48+00:00: Recorded command exit 0; command argv SHA-256
  cac057a613094ac8726cd86f751a6978c154a75372a08f1dcfed1a51b8b5e167.

- 2026-09-10T21:01:58+00:00: Recorded command exit 0; command argv SHA-256
  f90b63e863a577259e6a37b4ce5efe767bbdedd6fa81d48df53a6f099cf1109c.

- 2026-09-10T21:02:07+00:00: Recorded command exit 0; command argv SHA-256
  4453a4e34b89301bc970928e2eb3ad7202cc7d56ffd4a9ab567e4d3cbc0b46e1.

- 2026-09-10T21:02:27+00:00: Recorded command exit 0; command argv SHA-256
  9e4ab552d23f1cc33b29417c4fef437f00e4ad432756d757cb7c62276d474fcf.

- 2026-09-10T21:02:53+00:00: Recorded command exit 0; command argv SHA-256
  8b9842ed4f48ffe7b790c0b1bb7fc565d98779ef178cf3152ce4a9f899091e7e.

- 2026-09-10T21:03:31+00:00: Recorded command exit 1; command argv SHA-256
  ee966b1d6c48007523be3a58b9fa1aa247ae686e9eca6738b8c23b837c1a59c9.

- 2026-09-10T21:03:50+00:00: Recorded command exit 0; command argv SHA-256
  c045ad18d6cb2f12bb6c439b291a039aca3e8a50a2384cf134dfc1233fd96915.

- 2026-09-10T21:04:07+00:00: Recorded command exit 0; command argv SHA-256
  ccb890e1035709e3e44e1ce71b64afb4a47f2d1d43ca447954f2b6e9c8508acd.

- 2026-09-10T21:04:33+00:00: Recorded command exit 0; command argv SHA-256
  7d88449dbabfc3fa2aec04735ce92994d1d750c1bbde810efe2390970b556bf8.

- 2026-09-10T21:04:49+00:00: Recorded command exit 0; command argv SHA-256
  766dfe1e235be9aa07171488ef7965bd1b17fb0fea3afdf7c3b7b8dce8c0fb70.

- 2026-09-10T21:05:07+00:00: Recorded command exit 0; command argv SHA-256
  edb85f6212d2fb23d41fc4e556434920e848d968ced5ead9cc80f54c9582cb46.

- 2026-09-10T21:05:50+00:00: Recorded command exit 0; command argv SHA-256
  7f8e8672dc2f9884fe051de381dd64360ca9a541e580878d40068798e4dc6ade.

- 2026-09-10T21:06:06+00:00: Recorded command exit 0; command argv SHA-256
  4c72f67524155e6d9b689e14ed9d1784ee63399b67e8741b66e8456283e2a769.

- 2026-09-10T21:06:22+00:00: Recorded command exit 0; command argv SHA-256
  0467e21af1b3d40ef674289d8cee31455c4beb811dc940fb063a0f5905758041.

- 2026-09-10T21:06:40+00:00: Recorded command exit 0; command argv SHA-256
  35632482dc4376ff1fb9d52dea7f60c22d73bc097e2386f5b3a039f6cc548eed.

- 2026-09-10T21:07:08+00:00: Recorded command exit 0; command argv SHA-256
  8b28de97f7db2686fa98997aa763f446e451c0ba770720f577038b0073623be8.

- 2026-09-10T21:09:02+00:00: Published signed+DCO PR 9 head 10df38759371a4f6addb78dcfd970b65b3c90be5
  (tree 4c4339eabf17a1f25e6c35d9f09ce2040bb914d2) on exact d58eda9 main; hosted Repository quality
  is green. Full fmt/clippy/test/rustdoc/release, native/x86_64/AArch64 cargo-deny and cargo checks,
  cargo-audit, SBOM/schema/publication/release-channel/shell/workflow/gitleaks, ASB isolation, and
  clean coverage passed. Coverage is 89.03% regions and 92.13% lines; renderer 100%, runtime 95.88%
  regions and 96.73% lines. One cargo-deny gate command exited 2 solely because target was placed
  after the check subcommand; rerun with the supported global --target position passed for both
  targets. Three wrapped gh operations completed remotely but recorded exit 1 because then-broken
  state rendering lacked AR-1036; exact PR title/body/head/CI were independently verified, and the
  state defect has since been repaired with doctor --live green. No ASB product files were modified.

- 2026-09-10T21:09:49+00:00: Recorded command exit 0; command argv SHA-256
  4abe4d50d3084f2c45b1a7b8f7e34bbf3ce81545eac76a45b215462b95dffdb0.

- 2026-09-10T21:13:52+00:00: Recorded command exit 0; command argv SHA-256
  7d7c01f3b68d5887418534e3fdb2a3e14ccdb7ffc3d358eac863948094e5c0b5.

- 2026-09-10T21:14:10+00:00: Recorded command exit 0; command argv SHA-256
  bbc809459e241c96aedf0cdfd4299e3b01d472a1eb13f7aefa6c9619bde637d2.

- 2026-09-10T21:16:07+00:00: Recorded command exit 0; command argv SHA-256
  3cdfb5655a8883bbc90a3ac8786563844e506df9620c249a6455035106c22a9c.

- 2026-09-10T21:16:21+00:00: Recorded command exit 0; command argv SHA-256
  536405f43cc10ddd326ed1cf79b4bb457bf1b58672def784ab6c6e1b907aee4b.

- 2026-09-10T21:16:54+00:00: Recorded command exit 0; command argv SHA-256
  79b0681ab38249d4d63428e3e827befda081ce8a25716551c40eff6e543c32a4.

- 2026-09-10T21:17:40+00:00: Recorded command exit 0; command argv SHA-256
  4b9b976d14b0fb8719c9a44b975553feb3973b010e19fdaed920a0c87f6a13f1.

- 2026-09-10T21:17:57+00:00: Recorded command exit 0; command argv SHA-256
  4abb8117cee89e75d272b6d3d42199d2207417b3f9dde76565bf4460c8aaa701.

- 2026-09-10T21:18:43+00:00: Recorded command exit 0; command argv SHA-256
  3758f4e66656b8e3cbf61eee32ca84704a2e69b444d15148e153b755b199ab0c.

- 2026-09-10T21:19:21+00:00: Recorded command exit 0; command argv SHA-256
  c0656eb5fe4636df9ce2a282e6cd57d7ac75e1770b298db2001927e39b25b8cb.

- 2026-09-10T21:20:04+00:00: Recorded command exit 0; command argv SHA-256
  109c818d8cf256beee34b2bc4cbde16f7dde5a960f63ac738c105d45cf52fc47.

- 2026-09-10T21:20:21+00:00: Recorded command exit 101; command argv SHA-256
  496459e280cef06b76cfbd57b5d36cdf2a463904445646f3aa83bfd178ad9ca0.

- 2026-09-10T21:20:41+00:00: Recorded command exit 0; command argv SHA-256
  fc7f7230c64e0b8119dc73302dad04406535f27783dc45f6bc0ff635b55180c3.

- 2026-09-10T21:20:57+00:00: Recorded command exit 101; command argv SHA-256
  496459e280cef06b76cfbd57b5d36cdf2a463904445646f3aa83bfd178ad9ca0.

- 2026-09-10T21:21:25+00:00: Recorded command exit 0; command argv SHA-256
  c9f1835183591b918a264a5dfb9f852f60bf6e30fda0dcb0c99805d3d133fb2d.

- 2026-09-10T21:21:42+00:00: Recorded command exit 0; command argv SHA-256
  3fa00205dd77628254ee5f7677c38a9492ebdeb3fb82284bda5f5c5e1fecd24b.

- 2026-09-10T21:22:04+00:00: Recorded command exit 101; command argv SHA-256
  7c6ddd70c51bb9ef7d305e03a0dbaf84ddfba8b184467eef1926a3a68f7a6788.

- 2026-09-10T21:22:38+00:00: Recorded command exit 0; command argv SHA-256
  afca449635597d0554aa31075ecf65d3721d268bed12a6eaed9d3a410e8813ff.

- 2026-09-10T21:22:54+00:00: Recorded command exit 0; command argv SHA-256
  7c6ddd70c51bb9ef7d305e03a0dbaf84ddfba8b184467eef1926a3a68f7a6788.

- 2026-09-10T21:23:28+00:00: Recorded command exit 0; command argv SHA-256
  a176c7e44d293987c3b28974cb46e55681e639553fbc82905b635591f221359d.

- 2026-09-10T21:24:27+00:00: Recorded command exit 0; command argv SHA-256
  a99e2bfc639586a687f5a9820f36736ea9cc540be7f840e8a4507a2d2d76c560.

- 2026-09-10T21:26:21+00:00: Recorded command exit 0; command argv SHA-256
  9b145a9ab7c367201f6ce7dfd0abaf9a2c864ba8d646bf691db76174696200c6.

- 2026-09-10T21:27:02+00:00: Recorded command exit 0; command argv SHA-256
  d9ce2fbee9cdb761ef81f0710fd360507adade7a8537bb4c2c434199f70adca1.

- 2026-09-10T21:27:40+00:00: Recorded command exit 0; command argv SHA-256
  5fc0050825346887962befaba95c073f518e8d9b3a189d2dc409fc605abf033e.

- 2026-09-10T21:28:38+00:00: Recorded command exit 0; command argv SHA-256
  6ecea32f6ff749611e1accffd70350019ffa15334231c28524af6c78f4653899.

- 2026-09-10T21:29:04+00:00: Recorded command exit 0; command argv SHA-256
  7f991b013bc10955de653f1704d0d162d0fa8d412acc3761193ac1fb4db55c6f.

- 2026-09-10T21:29:45+00:00: Recorded command exit 0; command argv SHA-256
  8052b2d8c55bbdd54340a0ddd19c4f4eea2f1241a9c8dfa1da96c282aaefdde1.

- 2026-09-10T21:30:06+00:00: Recorded command exit 101; command argv SHA-256
  b97dea9163e2a377788000fc4af89eea6eb4e679ad0fbb744b240f9ed13c2ed8.

- 2026-09-10T21:30:26+00:00: Recorded command exit 0; command argv SHA-256
  6bc8632fbbc6ff44756f0e02a92302fd5f986d1c2406940ecf452c19af50c7a3.

- 2026-09-10T21:30:55+00:00: Recorded command exit 0; command argv SHA-256
  b97dea9163e2a377788000fc4af89eea6eb4e679ad0fbb744b240f9ed13c2ed8.

- 2026-09-10T21:32:01+00:00: Recorded command exit 0; command argv SHA-256
  0571fa1e8ceb624649f56554640008e85b15538a81a3e8d2a88c9f265e2a02c4.

- 2026-09-10T21:32:34+00:00: Recorded command exit 0; command argv SHA-256
  63e14be4d832799cac95dbebe7b9b0fe02df0c60531d1c5ee4acd2c88e4181fe.

- 2026-09-10T21:33:02+00:00: Recorded command exit 101; command argv SHA-256
  97f1f661de322e2e212fcff2c9b71354492413edb7a304bb6c10a5802595e5aa.

- 2026-09-10T21:33:35+00:00: Recorded command exit 101; command argv SHA-256
  d3b7640dd2ba11a3b7f0e3832ef37c73c3b9e3efe1fccefe78e0f9ebb41e46a8.

- 2026-09-10T21:34:19+00:00: Recorded command exit 101; command argv SHA-256
  2fae91ebf4a36b4090d1c2c71c816943b0edc3219c3fce614f11d58f610a19e9.

- 2026-09-10T21:34:46+00:00: Recorded command exit 0; command argv SHA-256
  b8a9b52b8d81fadd37dbf3aa517c2cdb81fa145819022a1efb024f5515512273.

- 2026-09-10T21:35:06+00:00: Recorded command exit 0; command argv SHA-256
  9d1fc1998636946e8be699e2815fb333ee18660abc789e6b8797a0a486315e80.

- 2026-09-10T21:35:45+00:00: Recorded command exit 1; command argv SHA-256
  7127fca877b56046fbe4bf59db85b2ddeffecf537bc9ac2a51f1f3cc2d5f77bc.

- 2026-09-10T21:36:22+00:00: Recorded command exit 0; command argv SHA-256
  d64bea98f22f9afb5c204e2c746d91741f260177660288cac631fb4e5c5e33b0.

- 2026-09-10T21:36:40+00:00: Recorded command exit 0; command argv SHA-256
  119fac2403871b06df38981b72ea87f68f73c01d0d4615728960f80f65a0757f.

- 2026-09-10T21:37:25+00:00: Recorded command exit 0; command argv SHA-256
  e231e6ec1981163bdefffe220ec8a9a04201768ed20078c95f2f4ac6258b8f28.

- 2026-09-10T21:37:56+00:00: Recorded command exit 0; command argv SHA-256
  e0044aa1e4fbdaf27d3ed56472294f4156e401408b64cc0c146e04051020a24f.

- 2026-09-10T21:38:16+00:00: Recorded command exit 0; command argv SHA-256
  119fac2403871b06df38981b72ea87f68f73c01d0d4615728960f80f65a0757f.

- 2026-09-10T21:39:01+00:00: Recorded command exit 0; command argv SHA-256
  fe247c3a61265d09f66c67a8471a2ae03c3a30b520331e89fc19e373011efc94.

- 2026-09-10T21:39:21+00:00: Recorded command exit 0; command argv SHA-256
  908d378649922e38e06ccdd12beb71a6ff0203d3d316d503c94d56590075f3ed.

- 2026-09-10T21:40:00+00:00: Recorded command exit 0; command argv SHA-256
  67c0fe4c16a57131cbffa0961c98401a9be934dac90c758ed4de8ee02c0dafa9.

- 2026-09-10T21:45:43+00:00: Recorded command exit 0; command argv SHA-256
  f734c0f87120f9e029a7ee89607ba01b70b5e477cdc8456b881a63fa02fb2450.

- 2026-09-10T21:46:40+00:00: Recorded command exit 0; command argv SHA-256
  140ce04b30789d10ab2a7e446485c6cc16478de04749df6e96be79d04cc73ce7.

- 2026-09-10T21:46:56+00:00: Recorded command exit 0; command argv SHA-256
  7882d784c17ba912913ddcbad009cbedcc54c5447e9ab6e9cabaadf426c3f63c.

- 2026-09-10T21:47:09+00:00: Recorded command exit 0; command argv SHA-256
  2fcc3ee52d4be7ff156e68a80f228b989836c7c54df2c88c0df94f9c39f233f1.

- 2026-09-10T21:49:17+00:00: Recorded command exit 127; command argv SHA-256
  03be9ad67fe8d3178df77ff58d5ff6d3e376948eb49d7f5bfd97161b18af13df.

- 2026-09-10T21:50:01+00:00: Recorded command exit 1; command argv SHA-256
  b11084f46b772ddb7f57a74fa0970e353aa45f3a262be02d24a4349e87e07e0d.

- 2026-09-10T21:50:16+00:00: Recorded command exit 0; command argv SHA-256
  ff3fffefc6bcfe5bf9f3eacf9484a41a46f521c8a961fea36e8429c120204f7e.

- 2026-09-10T21:51:01+00:00: Review-repair checkpoint remains dirty on published head 10df387. Typed
  injection/projection only is AR-1010 scope; AR-1025 exclusively owns the live client. Focused
  AppState, signal/termios, NO_COLOR, exact inventory, sealed-memfd, retained-fd XDG, and lifecycle
  self-test tests pass. The first multiplexer test was interrupted after an unbounded GNU screen
  control command leaked exact session asb-tui-test-3272385; the leaked PID/session was terminated
  successfully. Repair now gives every tmux/screen command a 3-second SIGKILL deadline, uses unique
  session names, waits boundedly for an actual rendered Connection frame, has Drop cleanup on all
  exits, and asserts sessions are gone. Recorded exit 127 at 21:49 was cargo fmt invoked without the
  repository toolchain path; recorded exit 1 at 21:50 was the corrected cargo fmt --check reporting
  formatting-only diffs in the new test; cargo fmt then completed successfully. No failure is
  acceptance evidence; the repaired multiplexer test and all broad gates remain pending.

- 2026-09-10T21:51:13+00:00: Recorded command exit 101; command argv SHA-256
  dfd5cd71ee62a1e4aed700db9215b84d026f6aaced8ecbd6c91a1f00c5c3b45b.

- 2026-09-10T21:51:40+00:00: Recorded command exit 137; command argv SHA-256
  c066bca1d6561fcd276a0cae3f701f49b49168105520aab8c75830418eb95ac7.

- 2026-09-10T21:52:11+00:00: Recorded command exit 0; command argv SHA-256
  0f70c01435f071f857f95dc299d36993577269fb0c0e7eb6b603d9127c3fccfd.

- 2026-09-10T21:52:23+00:00: Recorded command exit 0; command argv SHA-256
  dfd5cd71ee62a1e4aed700db9215b84d026f6aaced8ecbd6c91a1f00c5c3b45b.

- 2026-09-10T21:52:51+00:00: Recorded command exit 0; command argv SHA-256
  48f054edfd6b2c7b08dc68feda3fb8a8b55480dbe2fa5fced7bd9075a9a57e50.

- 2026-09-10T21:56:32+00:00: Multiplexer failure classification: the original local test used GNU
  screen option -DmS (capital D), which selects no-fork mode and caused the controller to remain
  attached indefinitely. Interrupting the unbounded run left exact orphan session/PID
  asb-tui-test-3272385/3272400; it was terminated. A diagnostic reproduction intentionally exited
  137 under timeout and created dead socket asb-screen-probe-3374653; the wrong-flag targeted test
  intentionally exited 101 and created dead socket asb-tui-test-3371268-1789077070306040365. Both
  exact dead sockets were wiped, with unrelated active screen sessions preserved. Repair uses
  correct detached -dmS, a unique nonce session, 3-second SIGKILL deadlines for every control
  command, bounded first-render observation, Drop cleanup, and explicit no-leak assertion. Repaired
  targeted test passed 1/1 in 0.12s under a 45-second outer deadline. Next evidence requires at
  least ten repetitions plus artifact audit.

- 2026-09-10T21:56:45+00:00: Recorded command exit 0; command argv SHA-256
  ae84a38f6a7e5835d36fb9814c87866fa3c0ee840a724d833c84ce4278d9b276.

- 2026-09-10T21:57:03+00:00: Recorded command exit 0; command argv SHA-256
  f2cd49801d27137a54efa6b1a5ae8fc080527efc429180bfea1e2f0e9dcddee4.

- 2026-09-10T21:57:27+00:00: Recorded command exit 0; command argv SHA-256
  e2268815b39b7c396f5e12cc639f38d434aeda9a867575d2221e42d13c4ad642.

- 2026-09-10T22:03:08+00:00: Recorded command exit 0; command argv SHA-256
  9420cc46049c64a939ccc7662de66b6e23eec70c86c615d42d398c1cc9888d65.

- 2026-09-10T22:04:26+00:00: Recorded command exit 0; command argv SHA-256
  86cf3827a0c4947aa7ff087350fc1e5b971fcbb54953da4a3338eea245abf678.

- 2026-09-10T22:04:52+00:00: Recorded command exit 0; command argv SHA-256
  f4c543313fc5a6de84e48afffe8324b933cdee37b6bef510e86f63a12afd23e8.

- 2026-09-10T22:05:24+00:00: Recorded command exit 1; command argv SHA-256
  aa792fe93f6bc0e257b0a69c2cf20759ded154253464d3caaa1c8a766ec183a0.

- 2026-09-10T22:06:08+00:00: Recorded command exit 0; command argv SHA-256
  47f130d11f9e7ef32ae73e9c4804e0630ff500bdee900d5559eaf4a1e0174a62.

- 2026-09-10T22:06:27+00:00: Recorded command exit 0; command argv SHA-256
  81671fbf7e407a5b7b9a751f4b6791a2af56995f1d682dd3506e3fc9515b2371.

- 2026-09-10T22:08:36+00:00: Recorded command exit 0; command argv SHA-256
  9420cc46049c64a939ccc7662de66b6e23eec70c86c615d42d398c1cc9888d65.

- 2026-09-10T22:08:58+00:00: Recorded command exit 0; command argv SHA-256
  f4c543313fc5a6de84e48afffe8324b933cdee37b6bef510e86f63a12afd23e8.

- 2026-09-10T22:11:01+00:00: Recorded command exit 0; command argv SHA-256
  a0f923a73152367af6fbae177775c5766c2dee70f53b9b1c95dc1220524e6fba.

- 2026-09-10T22:11:24+00:00: Recorded command exit 101; command argv SHA-256
  203cb7f0a19f7a6f358a126809e9414e51545fb0edc0b9a9b26bbe6a2877c41e.

- 2026-09-10T22:11:51+00:00: Recorded command exit 101; command argv SHA-256
  5dc983d06502ddaebfbadd20a7111f717e11e27be409d568059aa137a6902648.

- 2026-09-10T22:12:20+00:00: Recorded command exit 0; command argv SHA-256
  5dc983d06502ddaebfbadd20a7111f717e11e27be409d568059aa137a6902648.

- 2026-09-10T22:13:38+00:00: Recorded command exit 0; command argv SHA-256
  2bede4dddd182fb1ec2f5ab5256ff9838f1f9234da211f471170aba0e79057e5.

- 2026-09-10T22:14:27+00:00: Recorded command exit 101; command argv SHA-256
  2d38c018db92d548d4274966b3e790d4a29b91bc555c0807141ba0d9fdaed5d8.

- 2026-09-10T22:15:12+00:00: Recorded command exit 0; command argv SHA-256
  c7501e5ffdfe7f18159183affe0bea04c97e4274eedb42e5b2ad90880694bdd8.

- 2026-09-10T22:16:17+00:00: Recorded command exit 101; command argv SHA-256
  7c713010a5e8c5b3cd243399d20c4646554a9e591276a4fa1b52bccc5deb4f26.

- 2026-09-10T22:16:41+00:00: Recorded command exit 0; command argv SHA-256
  7c713010a5e8c5b3cd243399d20c4646554a9e591276a4fa1b52bccc5deb4f26.

- 2026-09-10T22:17:07+00:00: Recorded command exit 1; command argv SHA-256
  bf6218e394c8a9b61abf8d8a06608b5e6c0106013a64bea7b22a5c35a0aad58e.

- 2026-09-10T22:17:21+00:00: Recorded command exit 101; command argv SHA-256
  f76d4e8af6b32498aec0bd15409f2002be048f1b5d67ca7eacfa235864ccbf9f.

- 2026-09-10T22:18:15+00:00: Recorded command exit 0; command argv SHA-256
  a14d2ef224d6c25050c1b6f18ef7c00a759a79b866ac10f22889a16edb0685fa.

- 2026-09-10T22:18:40+00:00: Recorded command exit 1; command argv SHA-256
  b8d5946040b02613bf094aa81a5c36955ffdd808198d435991f935ebbeaa8a57.

- 2026-09-10T22:19:26+00:00: Recorded command exit 1; command argv SHA-256
  b8d5946040b02613bf094aa81a5c36955ffdd808198d435991f935ebbeaa8a57.

- 2026-09-10T22:19:59+00:00: Recorded command exit 0; command argv SHA-256
  b8d5946040b02613bf094aa81a5c36955ffdd808198d435991f935ebbeaa8a57.

- 2026-09-10T22:20:23+00:00: Recorded command exit 0; command argv SHA-256
  1610d02ecb6920b75172656538274893cbfeb5618feb73d5d6f1fb7dd37288ce.

- 2026-09-10T22:22:04+00:00: Recorded command exit 0; command argv SHA-256
  b9171037409f6c2ab992581a283779f9c8c7dcc0ec4515de619e6792c7d418ab.

- 2026-09-10T22:22:24+00:00: Recorded command exit 0; command argv SHA-256
  b27260464ead663dd63f74d5e13842a16f2bfd483bb862f2ddb5725f6cf9f84e.

- 2026-09-10T22:22:45+00:00: Recorded command exit 0; command argv SHA-256
  b7059bf6be088ce6cdc6fbe9430356b65ac5e5aa3755f2a0b407823ccfe64a2a.

- 2026-09-10T22:23:19+00:00: Recorded command exit 0; command argv SHA-256
  900e813ca700edf44966087577c4eb5d0940799955055a94f25a0ef360e45386.

- 2026-09-10T22:23:39+00:00: Recorded command exit 0; command argv SHA-256
  2414b1b64c438a4872121617af1c7569cdcccb596210182aa66adc943c86f078.

- 2026-09-10T22:23:57+00:00: Recorded command exit 0; command argv SHA-256
  8990fc04d8f6ae70f0f0469040647c399a8a4b79b3450efe9681f3580d10c359.

- 2026-09-10T22:24:16+00:00: Recorded command exit 0; command argv SHA-256
  5b7aeec4bacc2df06cce4ed40e2888a20fb0b5008d173b5c420b456cfee37613.

- 2026-09-10T22:25:04+00:00: Published clean SSH-signed+DCO successor
  41c61bdef7e0ae7d5dd3c9c7c0056d5d364b9965 (tree 3515148c613079afee0a1cafbf19b1a2af795ad5, base
  d58eda9b74431752675f784978dd5851f4eb9f18) to draft asb-tui PR 9; live PR reports exact head and
  hosted quality is running. Local acceptance evidence: fmt; Clippy -D warnings; locked full tests
  (42 library and all integration suites, including 10 PTY tests); rustdoc -D warnings; release
  build; cargo-deny advisories/bans/licenses/sources; cargo-audit 93 dependencies against 1243
  advisories; SBOM generator exact check; schema/release/publication/JSON validators;
  shellcheck/shfmt; zizmor; privacy greps; gitleaks over 3 commits/117107 bytes; standalone-to-ASB
  isolation with 16 asb-core tests and 2 doctests; real promoted executable self-test ready=true;
  10/10 real tmux+GNU screen repetitions with per-pass session/process/socket cleanup; coverage
  88.85 percent regions and 92.10 percent lines; clean tree. Exact failure repairs: 22:11 cleanup
  test exit101 was an unsafe-mode 0755 fixture correctly quarantined by policy, fixed fixture mode
  0700 and rerun passed; 22:14 full-suite exit101 was stale lifecycle-self-test CLI args in doctor
  test, updated to explicit ASB/protocol and full rerun passed; 22:16 Clippy exit101 was two
  needless generic borrows, fixed and rerun passed; 22:17 generator exit1 was an incorrect
  CARGO_HOME pointing at a tools-only cache without Ratatui, rerun under the normal repository cache
  passed; 22:18 shell exit1 was ShellCheck SC1007 in the new script, fixed; 22:19 shell exit1 was
  shfmt indentation diff, fixed and complete shell/workflow rerun passed. Earlier wrong exact unit
  filter ran zero tests and was replaced by the fully qualified exact test, which first exposed the
  unsafe fixture then passed after repair. AR-1010 owns typed event injection/projection only;
  AR-1025 owns live client negotiation/polling/responsiveness. No ASB product or UI source changed.

- 2026-09-10T22:30:30+00:00: Recorded command exit 127; command argv SHA-256
  438dc966625bc869a068bae5a5a86a721ecbb630e0187f2519b1c60d1d2ea7b9.

- 2026-09-10T22:31:12+00:00: Recorded command exit 101; command argv SHA-256
  ab758e3cb1e6ec2eef92a395882e374c4d39223ed1108cd0001c36e51157b506.

- 2026-09-10T22:31:34+00:00: Recorded command exit 101; command argv SHA-256
  a030bb1677257aaa5ddcc94839402f784ce54d7ae84b51893151be605969cd85.

- 2026-09-10T22:32:25+00:00: Recorded command exit 101; command argv SHA-256
  d4a211ba8740a4d0e321db227d624219e1836df9860fc4140b25f4d6d5bc1d32.

- 2026-09-10T22:41:34+00:00: Recorded command exit 101; command argv SHA-256
  9420cc46049c64a939ccc7662de66b6e23eec70c86c615d42d398c1cc9888d65.

- 2026-09-10T22:42:59+00:00: Recorded command exit 0; command argv SHA-256
  9420cc46049c64a939ccc7662de66b6e23eec70c86c615d42d398c1cc9888d65.

- 2026-09-10T22:44:11+00:00: Recorded command exit 0; command argv SHA-256
  c9f2d9d29a38b0543d2dd23577569f3cc032e67d2a7201b7ec7b5bd31c02f218.

- 2026-09-10T22:45:07+00:00: Recorded command exit 101; command argv SHA-256
  23e181c63d5564cfe7cfc2003f4d033b45bb58ccf816fd2ae12879383d7c004a.

- 2026-09-10T22:47:00+00:00: Recorded command exit 0; command argv SHA-256
  72aecf5778ffb59abefdb23e16322901216e5f67418b1512ff52185dc962ed2f.

- 2026-09-10T22:47:14+00:00: Recorded command exit 0; command argv SHA-256
  26a707dbfd8b56f19f3e11bab65023ca6c4fb4e41c71039057dbc87cc665b584.

- 2026-09-10T22:48:16+00:00: Recorded command exit 0; command argv SHA-256
  ee43fd63ea2fbccbc633cb8a24a2ffd82cd9f941ad728d347dec564611b0a79f.

- 2026-09-10T22:49:00+00:00: Recorded command exit 0; command argv SHA-256
  c9f2d9d29a38b0543d2dd23577569f3cc032e67d2a7201b7ec7b5bd31c02f218.

- 2026-09-10T22:49:19+00:00: Recorded command exit 0; command argv SHA-256
  3061d0cc6c189e861db35c115d1667734205e1b4804018d47b55ea048e313f6a.

- 2026-09-10T22:49:59+00:00: Recorded command exit 0; command argv SHA-256
  448033347e877b4e102ebe12e8fe34d13e3958c357a34679442a13c267907f21.

- 2026-09-10T22:50:29+00:00: Recorded command exit 0; command argv SHA-256
  9afed5db9788eadb62bc26b58fa266fcc0862b97f33cdd22b96ed47ff76b418a.

- 2026-09-10T22:50:50+00:00: Recorded command exit 0; command argv SHA-256
  71bdb2135b345e13139092019a5761915b58869318e33dff299c500ddceabd29.

- 2026-09-10T22:51:26+00:00: Recorded command exit 0; command argv SHA-256
  900e813ca700edf44966087577c4eb5d0940799955055a94f25a0ef360e45386.

- 2026-09-10T22:52:26+00:00: Recorded command exit 0; command argv SHA-256
  8d9183781070ec578076c1e17fa824c8c3c7ac7df7d428bfb794f755b9e523fc.

- 2026-09-10T22:52:44+00:00: Recorded command exit 0; command argv SHA-256
  f18879d900ea99b63199b1652f4bc367e0c3917be6cca050c943d96b6a1a35f3.

- 2026-09-10T22:52:58+00:00: Recorded command exit 127; command argv SHA-256
  5f51e5a22a0fac2650c2d1db5d71af62365954eb9eec2ece88e2395106378529.

- 2026-09-10T22:54:26+00:00: Recorded command exit 0; command argv SHA-256
  a12174d795ed51fef1caa35e4117c134dd29d0b20ad42df32fe925d5f6e873d5.

- 2026-09-10T22:55:18+00:00: Recorded command exit 0; command argv SHA-256
  ed6fdae57e756c0181eccaedf76aa14895d8176fb8b435d125d075306f85f118.

- 2026-09-10T22:55:34+00:00: Recorded command exit 0; command argv SHA-256
  4ddb7b68bb963d858a13caecda9e6f3e2416a3cad91cdd3b79459387b72a2960.

- 2026-09-10T22:56:00+00:00: Published signed+DCO review-repair successor
  140b4fa2bb38be6fc5e6299a02fd67ae11223339 (tree b89108c5a2cd324c5a35d968a47438ec59feba6a) to draft
  PR #9. It bounds Ratatui backend/frame dimensions before allocation (4096 per dimension, 262144
  cells; deterministic 1x1 transient-zero fallback; oversized initial PTY and resize storms fail
  closed and restore termios) and hardens nested untrusted executable self-tests with a dedicated
  process group, retained pidfd leader fence, bounded nonblocking output, serialized subreaper
  adoption for session escapees, fail-closed Result-based /proc enumeration, and bounded group/pidfd
  kill+reap on success, reject, timeout, malformed, oversized, and signal paths. Adversarial PTY
  proof covers fork/pipe rejection, timeout, success-with-child, SIGTERM, setsid escape, 10 race
  repeats, /proc fault injection, and rejects a preexisting unrelated child while proving it remains
  live/unreaped. Full local exact-tree gates pass: fmt, Clippy -D warnings, 44 lib plus all
  integration/doc tests, 88.24% region/91.44% line coverage, rustdoc, deterministic SBOM,
  compatibility/release/publication validators, cargo-deny, cargo-audit, shellcheck/shfmt,
  workflow/zizmor, real promoted self-test ready, ASB-isolation 16 tests+2 doctests, privacy scans,
  release build, gitleaks, and clean tree. Classified repaired failures: exit101 compile errors from
  forbidden unsafe pre_exec/API imports replaced by safe process_group(0) and correct pidfd APIs;
  exit101 resize fixture inherited TMUX and was repaired with controlled terminal env; exit127
  release command was sanitized PATH only and reran green with explicit pinned Rust 1.93 paths; one
  verification command initially inspected the state checkout due missing git -C, made no product
  mutation, and was immediately rerun against the absolute product path. Scope remains standalone
  asb-tui only; live control belongs to AR-1025 and benchmark runners remain authoritative external
  ASB processes. Lifecycle JSON/schema and bundle fixtures are unchanged by this successor. Hosted
  Repository quality is currently in progress on exact head.

- 2026-09-10T23:00:49+00:00: Recorded command exit 0; command argv SHA-256
  bd2d01465d4deac975bf2fc9483f824488e9979273aa079e14b04d42ef960d4e.

- 2026-09-10T23:01:04+00:00: Recorded command exit 0; command argv SHA-256
  0f8779dd2162b1ab6d41b0557e8ae7642272cc93225371ba820073627b0e7d76.

- 2026-09-10T23:06:25+00:00: Recorded command exit 2; command argv SHA-256
  39f5bf37659926d3938e4cdf34374f4888ec5484d09a3fb3d70311438a424134.

- 2026-09-10T23:09:53+00:00: Recorded command exit 1; command argv SHA-256
  630418c2a2b9ba7c2e46273fe3023843f6229d2052ecd1e7acc6843d38ddcf20.

- 2026-09-10T23:10:04+00:00: Recorded command exit 0; command argv SHA-256
  f86052cdfcc6792992626aec05cc260d5901c99a746a1b47a2509b9c13dac36c.

- 2026-09-10T23:10:39+00:00: Recorded command exit 101; command argv SHA-256
  e4a57bd18619a53897a8597313f62359659129326ab4db7c3f5c3ddb467f3edd.

- 2026-09-10T23:11:07+00:00: Recorded command exit 101; command argv SHA-256
  e4a57bd18619a53897a8597313f62359659129326ab4db7c3f5c3ddb467f3edd.

- 2026-09-10T23:11:39+00:00: Recorded command exit 0; command argv SHA-256
  649721059b079b0184c2f386b8d80798ffddfe8e1c83b66beb99f295458bca7d.

- 2026-09-10T23:12:08+00:00: Recorded command exit 1; command argv SHA-256
  eb1de77e339fbb41210b1147d0a302f07e2bbf7d0287723819e929f0a95342c5.

- 2026-09-10T23:12:26+00:00: Recorded command exit 101; command argv SHA-256
  54f66089c499e18e196088004f2df5b587dabe81c6b1db0ce622dac76fb0c325.

- 2026-09-10T23:13:03+00:00: Recorded command exit 0; command argv SHA-256
  865c51c83a2a85f5619347294a16c68230f679983fb8f4b9d187b4d945de883f.

- 2026-09-10T23:14:43+00:00: Recorded command exit 1; command argv SHA-256
  6ad4f2d13d6138440dd0df769ab8d3c42c34585c08fec9cb9babe9414956a47d.

- 2026-09-10T23:15:13+00:00: Recorded command exit 0; command argv SHA-256
  62c2532c30b0af512169495e2ff5150cd462632a0ebd611f2465d67ce048753b.

- 2026-09-10T23:16:05+00:00: Recorded command exit 0; command argv SHA-256
  e2f230fdbdbe1018d7cce7f4320486d77f705cf762b1bb5e2a34e53ec7a9a5d2.

- 2026-09-10T23:16:35+00:00: Recorded command exit 101; command argv SHA-256
  99045eed2bc259260e245f9cafeb7591b73ac311726384ee9c7ac64f61037b85.

- 2026-09-10T23:17:35+00:00: Recorded command exit 0; command argv SHA-256
  76ab91e1e12a5b16a09fa21baefe7d03f79d252d1145ea4604e741055e8de007.

- 2026-09-10T23:18:07+00:00: Recorded command exit 0; command argv SHA-256
  7ec0c7ecc8364cdb69eb44752e13587071a5124d818675643f6bb12932752dac.

- 2026-09-10T23:18:35+00:00: Recorded command exit 1; command argv SHA-256
  b54a1c4d1623fd849e38bb3161fbd98174a230db9d0a5196f5930ff1c96a40a5.

- 2026-09-10T23:19:06+00:00: Recorded command exit 2; command argv SHA-256
  85bf3c2213a13b1953125f754cd9dad9292d01f319ccfa14fbfc97645b1bb66d.

- 2026-09-10T23:19:40+00:00: Recorded command exit 0; command argv SHA-256
  efa08fc05b17d78b2cb9b1e500a0a17abcacdb9e0210bdd506b1a18e676fded8.

- 2026-09-10T23:19:57+00:00: Recorded command exit 0; command argv SHA-256
  3f192c066ca88efb6c1057825e48dbf0f34e45067320044c1ac31a071c769d31.

- 2026-09-10T23:20:43+00:00: Recorded command exit 0; command argv SHA-256
  d0b6cc8c6f58180c5b512505bc2f32b4858718f754a3c4fce43d348c39a32700.

- 2026-09-10T23:21:03+00:00: Recorded command exit 0; command argv SHA-256
  f18879d900ea99b63199b1652f4bc367e0c3917be6cca050c943d96b6a1a35f3.

- 2026-09-10T23:21:20+00:00: Recorded command exit 0; command argv SHA-256
  adcd5e75b90ca4817f9b709d7fb64d083444bb56a28a1563a6ad49668854d306.

- 2026-09-10T23:21:33+00:00: Recorded command exit 0; command argv SHA-256
  5d880ad4b47a92c538397e52da5284f7057be4fccddeb9cf3178aefee9452384.

- 2026-09-10T23:22:04+00:00: Published signed+DCO ownership-safe cleanup successor
  1bab7ad34cdbf1647c7eea4953c3e60875c19ddc (tree 5876314e4c6a9e54dccb3bcc027c6596f3a03912) to draft
  PR #9. It removes process-global subreaper and /proc child enumeration. The retained trusted
  supervisor is placed in a fresh process group before it installs an inherited seccomp filter
  denying setsid/setpgid and execs the sealed candidate; all candidate forks therefore remain in the
  exact pidfd-fenced group, so cleanup is bounded, proc-independent, and cannot classify/signal/reap
  unrelated concurrent children. Deterministic PTY proof attempts both syscalls, exercises a double
  fork, verifies its child disappears, spawns an unrelated sleep after candidate readiness, and
  proves it remains live/unreaped; the full adversarial self-test matrix passed plus 10 bounded
  repeats. Added exact seccompiler 0.5.0 checksum/empty-feature/SPDX/license sentinels; it adds no
  transitive crate beyond already locked libc 0.2.189, and cargo-deny accepts Apache-2.0 OR
  BSD-3-Clause. Full exact-tree local gates pass: fmt, Clippy -D warnings, 44 lib/all
  integration/doc tests, rustdoc -D warnings, deterministic SBOM and validators, promoted self-test
  ready, shell/workflow/zizmor, cargo-deny, cargo-audit 94 crates/1243 advisories, ASB isolation
  16+2 doctests, release build, Gitleaks, diff check, clean-tree coverage 88.03% regions/91.41%
  lines. Classified non-code failures: two wrapper attempts hit coordinator lock timeouts before
  product commands; first compile exposed the deliberately removed old proc-test reference and was
  repaired; initial source-sentinel matched its own literal and was split then passed; clean
  coverage correctly refused the dirty precommit tree and passed after commit; first isolation
  invocation omitted its required ASB root and reran green. One initial one-line Cargo.toml edit was
  inadvertently applied before wrapper use; it was subsequently captured by all wrapped tests/git
  actions and the signed commit, with no other repository affected. Lifecycle JSON/schema and bundle
  fixture bytes are unchanged. Hosted exact-head Repository quality is IN_PROGRESS.

- 2026-09-10T23:22:58+00:00: Recorded command exit 0; command argv SHA-256
  7076739b9f3b972e8688df94c51f560a98ba12e9ed53da238b6771a006fdff4d.

- 2026-09-10T23:23:24+00:00: Verified GitHub PR #9 still draft at exact head
  1bab7ad34cdbf1647c7eea4953c3e60875c19ddc. Repository quality run 34541773153 job 103085791745
  completed SUCCESS at that exact head. Independent immutable review remains required; no merge
  performed.

- 2026-09-10T23:24:54+00:00: Recovered expired claim formerly owned by
  codex-ar1010-asb-tui-renderer-20260910. Implementation worker completed and stopped; exact
  successor 1bab7ad is frozen with green CI and awaits immutable review. Recover expired lease
  without changing product state.

- 2026-09-10T23:38:35+00:00: Claimed by codex-ar1010-trust-repair-20260911.

- 2026-09-10T23:39:01+00:00: Fresh repair owner active in the existing clean isolated asb-tui
  foundation worktree at exact reviewed-blocked head 1bab7ad/tree 5876314. No product mutation yet;
  preserving all accepted renderer, terminal, lifecycle, and supply-chain work.

- 2026-09-10T23:42:42+00:00: Recorded command exit 2; command argv SHA-256
  39f5bf37659926d3938e4cdf34374f4888ec5484d09a3fb3d70311438a424134.

- 2026-09-10T23:44:12+00:00: Recorded command exit 0; command argv SHA-256
  74cbb5ee2ad2c3619f635c0df184ba03dfe7388cb59156ec6f83afeb00fdc3f2.

- 2026-09-10T23:45:14+00:00: Recorded command exit 0; command argv SHA-256
  d1842caf4af7d2c0245695cfe00da14acbecdf1ccc5d24726403a4233d3f6ce3.

- 2026-09-10T23:45:34+00:00: Recorded command exit 0; command argv SHA-256
  35d02871ab7a04bfecca366a2e3b509332b8d7d769656c54d4345e2acfaff42e.

- 2026-09-10T23:46:16+00:00: Recorded command exit 0; command argv SHA-256
  b703bd1fcbae4b7ce79324b14c06fef4774a9ccd9110469f112768432b01df8c.

- 2026-09-10T23:46:32+00:00: Recorded command exit 101; command argv SHA-256
  7c1bad96750286f9316484b3b06d25e7439b5a6a3a7c3151f610aa93a5e990ce.

- 2026-09-10T23:46:41+00:00: Recorded command exit 0; command argv SHA-256
  5519fc58294c8841ac59d007952ed06d124a50ee1b1f1bcb4ff695d5e838060b.

- 2026-09-10T23:47:10+00:00: Recorded command exit 0; command argv SHA-256
  7c1bad96750286f9316484b3b06d25e7439b5a6a3a7c3151f610aa93a5e990ce.

- 2026-09-10T23:47:52+00:00: Recorded command exit 0; command argv SHA-256
  3249fd82bc29c2bf1e1104c8941135db724a607ab05b8d9c7b21ce6399d597d6.

- 2026-09-10T23:48:13+00:00: Recorded command exit 0; command argv SHA-256
  ccf0ad33a610cf397b068b9514f00fec1fda16f9504c0439ecf003e8babf3c31.

- 2026-09-10T23:49:19+00:00: Recorded command exit 0; command argv SHA-256
  76fb95f2706bc96afa266768e7c3f83cbf41879922eef7ab3b209f3ed8ac237c.

- 2026-09-10T23:49:42+00:00: Recorded command exit 0; command argv SHA-256
  ccf0ad33a610cf397b068b9514f00fec1fda16f9504c0439ecf003e8babf3c31.

- 2026-09-10T23:50:02+00:00: Recorded command exit 0; command argv SHA-256
  73575f2fd4a9ac2da180ec47b9b293ed1c2ef2f5cb96176a9d74b04e72929767.

- 2026-09-10T23:50:27+00:00: Repair implementation checkpoint: README.md, src/lifecycle.rs and
  tests/lifecycle.rs only. Production now seals a copy of the currently executing trusted
  supervisor; the hidden test-only seam requires independent exact bytes, rejects symlink,
  wrong-owner/group/world-writable and equal-length substitution, and seals the authenticated copy
  so demonstrated post-bind same-inode mutation is harmless. Cleanup checks group/pidfd signal
  errors. Adversarial probe covers fork/exec, spawned thread, namespace attempt with bounded
  unavailable errno, and setsid/setpgid denial. Unrelated-child proof now uses a two-way ready ->
  child-live -> acknowledged handshake before candidate response/cleanup. Full lifecycle 13/13,
  focused PTY nested probe, fmt, Clippy -D warnings and diff-check pass. Classified failures: first
  patch command passed no patch argument and made no product change; two wrapper attempts hit
  coordinator lock timeout before mutation; first compile found ambiguous Read/Write by_ref and was
  corrected with Read::by_ref; initial fmt-only failure was corrected.
