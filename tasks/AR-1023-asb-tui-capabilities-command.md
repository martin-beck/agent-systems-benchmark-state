---
{
  "branch": "feature/asb-tui-capabilities-command",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-10T22:23:58+00:00",
  "depends_on": [
    "AR-0803",
    "AR-0840",
    "AR-0841",
    "AR-0842",
    "AR-0843",
    "AR-0844",
    "AR-0904"
  ],
  "id": "AR-1023",
  "next_action": "Run full pinned workspace and repository gates, inspect exact diff, then create a signed DCO commit and publish the review branch.",
  "observed_branch": "feature/asb-tui-capabilities-command",
  "observed_dirty": 15,
  "observed_head": "66ca27afc2fb5a82b171e849e6dda4145735c8d2",
  "owner": "codex-ar1023-capabilities-20260910",
  "plan": "../plans/AR-1023.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Publish the ASB capability negotiation command required by the standalone frontend.",
  "task_revision": 47,
  "title": "Add the ASB frontend capabilities command",
  "updated_at": "2026-09-10T19:42:33+00:00",
  "worktree_key": "agent-systems-benchmark-asb-tui-capabilities-command"
}
---
Add `asb capabilities --format json` as a bounded, deterministic, side-effect-free description of
the installed ASB/frontend protocol contract. It must match the separately published asb-tui schema
and expose only capabilities the authoritative runner API actually implements.

Acceptance requires exact schema/type/fixture parity, malformed-argument and output-bound tests,
privacy-safe output, CLI help/completion/docs updates, cross-repository parser conformance, complete
local gates, independent review, exact-head CI and post-merge verification.

- 2026-09-10T19:14:02+00:00: Claimed by codex-ar1023-capabilities-20260910.

- 2026-09-10T19:22:26+00:00: Recorded command exit 0; command argv SHA-256
  5fc886b4070fa3ab0ac6f393b844d9a9add78751cef9f4fa0a626ebafbee8e8b.

- 2026-09-10T19:23:58+00:00: Heartbeat by codex-ar1023-capabilities-20260910.

- 2026-09-10T19:24:09+00:00: Reconciled standalone asb-tui capability schema at origin/main
  3d2b6b537da817469bf8a39841ccf9a79a4c370f with ASB control v1: all eight advertised frontend
  operations have authoritative typed control methods and RunnerBackend implementations;
  implementing closed side-effect-free JSON command and parity tests.

- 2026-09-10T19:26:25+00:00: Recorded command exit 2; command argv SHA-256
  48458d4adcbc2714c4ae60f17ec39d916357031118af6e75d9a5cd826c73f20e.

- 2026-09-10T19:27:22+00:00: Recorded command exit 0; command argv SHA-256
  bfb5188cf3d2030cf5658de848191cc7f96026c089e31d4d791af020d03400c7.

- 2026-09-10T19:28:05+00:00: Recorded command exit 101; command argv SHA-256
  be876d1bcca7e3e12fa64d46b3e64da1cdb663bec004b092515642b6f175e2d5.

- 2026-09-10T19:28:23+00:00: Recorded command exit 101; command argv SHA-256
  4b278de755613b78597ac2970f556ae4ae554bfa9d42830965b21f9d22aba0b0.

- 2026-09-10T19:28:49+00:00: Recorded command exit 0; command argv SHA-256
  a9e1bab5405e7d2e8a571e68aad8fe78689f3c24397666c235700b69d96b9c10.

- 2026-09-10T19:29:01+00:00: Recorded command exit 0; command argv SHA-256
  07476c6e4570343836e41901724b6228737461095cf8902ca5eb0d9879502034.

- 2026-09-10T19:30:34+00:00: Recorded command exit 0; command argv SHA-256
  db484ea5660bcaefdea0e3aa4ece54f75c15e990f0b7bbd0ebd1f6abdda73a69.

- 2026-09-10T19:30:49+00:00: Recorded command exit 101; command argv SHA-256
  a13af163dd7164811aebfda4c5a82ea97e0d5033f5e53a58404ea89e0f92a946.

- 2026-09-10T19:31:02+00:00: Recorded command exit 1; command argv SHA-256
  ff4e95699f82983812d9c1228696e3949290e8414339927a58aaf0487e910259.

- 2026-09-10T19:31:13+00:00: Recorded command exit 0; command argv SHA-256
  d89e2051fee94ddc5f9f67b2d47054170ab688793445eb223279386af8ea4f4e.

- 2026-09-10T19:31:26+00:00: Recorded command exit 101; command argv SHA-256
  215e0d02ad8c97fb7914acb252ab73c0130ff66eeae4fabed631f24a53154e96.

- 2026-09-10T19:31:42+00:00: Recorded command exit 1; command argv SHA-256
  0b90adb3c4f09e46ca9eaee396dfa79c30e5a52cbc7079422154a99a9f78d6bc.

- 2026-09-10T19:32:02+00:00: Recorded command exit 0; command argv SHA-256
  73137c665bbf77df98c23131203a4adeb9c6c14b236a5b81e8dd740b68dddac9.

- 2026-09-10T19:32:18+00:00: Recorded command exit 0; command argv SHA-256
  215e0d02ad8c97fb7914acb252ab73c0130ff66eeae4fabed631f24a53154e96.

- 2026-09-10T19:33:11+00:00: Recorded command exit 1; command argv SHA-256
  16d498e8ebf6466f86c5395c4d8ab53e2d776b2460e4b03ab43e026e3aa74e26.

- 2026-09-10T19:33:45+00:00: Recorded command exit 1; command argv SHA-256
  d5f773e04dd5c024d4c599b66eed41aec3a933825b19fcf51e0c7cc52213aaf1.

- 2026-09-10T19:34:17+00:00: Recorded command exit 0; command argv SHA-256
  400ddc2b2b8b05c35cd53e1b4ff0858e14fb4518bc5ab554c50281483f820498.

- 2026-09-10T19:34:43+00:00: Debugged wrapped failures: initial cargo/rustc lookup failures were
  sanitized-PATH environment issues resolved with absolute pinned Rust 1.93.0 tools; one focused
  test failure was an invalid duplicate-key schema oracle and is fixed by testing raw duplicate
  rejection separately; two apply_patch context misses were no-op incremental-edit conflicts.
  Focused capability contract now passes, with exact emitted fixture, generated schema equality,
  strict drift rejection and malformed CLI coverage.

- 2026-09-10T19:35:03+00:00: Recorded command exit 1; command argv SHA-256
  b8c8ec6288c650b38396769a302d4ee87b422c44d5ef3389ce1d7b0fd0bb8174.

- 2026-09-10T19:35:25+00:00: Recorded command exit 1; command argv SHA-256
  b8c8ec6288c650b38396769a302d4ee87b422c44d5ef3389ce1d7b0fd0bb8174.

- 2026-09-10T19:35:44+00:00: Recorded command exit 0; command argv SHA-256
  d89e2051fee94ddc5f9f67b2d47054170ab688793445eb223279386af8ea4f4e.

- 2026-09-10T19:36:04+00:00: Recorded command exit 0; command argv SHA-256
  541f24a7340d841f4e200bb17fe1ab68c6131ed047547feaf77db16d261ad56f.

- 2026-09-10T19:36:35+00:00: Recorded command exit 101; command argv SHA-256
  c6fcf25589c56109a7e80a637dbe60af5d812754ff44fa2a298516a5a7428b36.

- 2026-09-10T19:36:45+00:00: Recorded command exit 0; command argv SHA-256
  899e6e7eabb3e272ae17ad8572c1a7f06a7e013c37c65650fde1157370a25ea3.

- 2026-09-10T19:37:05+00:00: Recorded command exit 0; command argv SHA-256
  231b315180b6e814feecba90aebb181b61df7154383a44ba315dc79723a080f4.

- 2026-09-10T19:37:56+00:00: Recorded command exit 0; command argv SHA-256
  c6fcf25589c56109a7e80a637dbe60af5d812754ff44fa2a298516a5a7428b36.

- 2026-09-10T19:39:30+00:00: Recorded command exit 0; command argv SHA-256
  781416034844b103d35a9c62a87407362ab88ce88d43eebf024b5faee6f8b37f.

- 2026-09-10T19:39:47+00:00: Recorded command exit 1; command argv SHA-256
  bf49deb5c3dedbf401ddd540562b6003820e04585dc92a4b113f1b1ee220f199.

- 2026-09-10T19:40:02+00:00: Recorded command exit 0; command argv SHA-256
  fac61630979a4239ce571073af5c23897d845e07e4d1b9e7057d1a3297c518d8.

- 2026-09-10T19:40:20+00:00: Recorded command exit 0; command argv SHA-256
  bf49deb5c3dedbf401ddd540562b6003820e04585dc92a4b113f1b1ee220f199.

- 2026-09-10T19:40:51+00:00: Recorded command exit 0; command argv SHA-256
  d89e2051fee94ddc5f9f67b2d47054170ab688793445eb223279386af8ea4f4e.

- 2026-09-10T19:41:18+00:00: Recorded command exit 0; command argv SHA-256
  dc640d4198a158c359c38a445fdf84cf38c6ddf1a3c70a670da6a75791281f54.

- 2026-09-10T19:42:00+00:00: Recorded command exit 0; command argv SHA-256
  e9585d38fcd99009806d2ca77782dd17b38abaca5156e14aa076a165a3781037.

- 2026-09-10T19:42:33+00:00: Recorded command exit 0; command argv SHA-256
  3cdbd4177f7353f909405f1d4381f91a10173dc4dea64547e632b1dcd1734047.
