---
{
  "branch": "",
  "checkpoint_commit": "5e577e6a4b278fc79dc8b695cd6b3723d04cc609",
  "claim_expires": "2026-09-27T12:28:15+00:00",
  "depends_on": [
    "AR-1423",
    "AR-1425"
  ],
  "id": "AR-1426",
  "next_action": "Rerun failed AArch64 workflow 36312453084 once; then finish Rust/Repository Quality and all post-merge green verification.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "0000000000000000000000000000000000000000",
  "owner": "ar1332-record-replay-luna56",
  "plan": "../plans/AR-1426-evolving-literature-window-refresh.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Refresh evolving literature benchmark windows without stale or incomparable results.",
  "task_revision": 52,
  "title": "Evolving literature workload window refresh",
  "updated_at": "2026-09-27T10:33:45+00:00",
  "worktree_key": ""
}
---

This AR keeps time-windowed and continuously refreshed literature workloads
selectable without treating a mutable source as a stable benchmark. It never
requires live providers or upstream downloads during development or CI.

- 2026-09-24: Added after the literature audit identified stale-window risk for
  LiveCodeBench and SWE-rebench. Existing built-in and stable literature IDs are
  unaffected; every refresh is a new content-addressed identity.

- 2026-09-27T10:05:16+00:00: AR-1423 and AR-1425 are released done; promote the dependency-ready
  offline refresh-manifest implementation.

- 2026-09-27T10:05:18+00:00: Claimed by ar1332-record-replay-luna56.

- 2026-09-27T10:05:29+00:00: Recorded command exit 0; command argv SHA-256
  1d96b88e0f9d8fc7de759f6c96696434c0868b7259e3dae18a69288d99e85bf1.

- 2026-09-27T10:07:11+00:00: Heartbeat by ar1332-record-replay-luna56.

- 2026-09-27T10:07:21+00:00: Recorded command exit 0; command argv SHA-256
  83c84b7ac070d1aac6e30d26c8e7594032ea08b02fde5ebba86c365365ccd50f.

- 2026-09-27T10:08:00+00:00: Recorded command exit 101; command argv SHA-256
  7c50f518ef4f65f5fc0220fd26969854e2f8a8796393c29f5376716d6c2d793a.

- 2026-09-27T10:08:57+00:00: Recorded command exit 0; command argv SHA-256
  013aecd2ab27d39f6fd6e04aac60832985368c7c4d7bbf9e4477a1d59b2bc05a.

- 2026-09-27T10:09:45+00:00: Recorded command exit 0; command argv SHA-256
  dee750d0a840ceafafe8ca38552c64951e15258468c0e24c7c53a2d274663b85.

- 2026-09-27T10:10:14+00:00: Implementation checkpoint: added strict RefreshManifestV1 and
  RefreshManifestInput to asb-workloads. Manifest content-addresses
  source/dataset/window/cutoff/split/evaluator/image/SBOM/license/evidence fields; unknown fields,
  invalid digests, unsupported workloads, incomplete evidence, tampering, and cross-window/evaluator
  comparisons fail closed. Four positive/negative unit tests pass; full asb-workloads lib 39/39
  passes; fmt and clippy pass. The earlier exit-101 was product-related clippy denial
  (too-many-arguments, manual-flatten, collapsible-if) in the new module; fixed by constructor input
  struct, iterator flatten, and rerun success. Docs/WORKLOADS.md records the contract. Signed+DCO
  head 73b5fd1.

- 2026-09-27T10:10:22+00:00: Heartbeat by ar1332-record-replay-luna56.

- 2026-09-27T10:14:02+00:00: Recorded command exit 0; command argv SHA-256
  6cfc1756ce40c64fc72c055819aa9ee8f6f3e2f97559af881cfed7da0a1cdb34.

- 2026-09-27T10:14:21+00:00: Recorded command exit 0; command argv SHA-256
  b26ed33ec125f5141530e85d7eaa4762280eb6ee4c4b32767cc032bcb447eafd.

- 2026-09-27T10:15:11+00:00: Recorded command exit 0; command argv SHA-256
  8d8d5af421ea23523a19c1452d5b46deed22baac4f2fd240e5c9f5fd75a08f88.

- 2026-09-27T10:15:46+00:00: Recorded command exit 0; command argv SHA-256
  7c2ca081db965d6d85c7be2b711c0588a788efec0def10360907700b163ea033.

- 2026-09-27T10:16:10+00:00: Recorded command exit 0; command argv SHA-256
  fee4862bed24b320334758df17ee053f67cccf59d2536dbb7bab768194d45eac.

- 2026-09-27T10:16:32+00:00: Heartbeat by ar1332-record-replay-luna56.

- 2026-09-27T10:17:10+00:00: Recorded command exit 0; command argv SHA-256
  2f2d21c06f911315badd79af1d0f107fee0ea488467c90364bd9ff0ddc4fb4c3.

- 2026-09-27T10:17:33+00:00: Recorded command exit 0; command argv SHA-256
  2f2d21c06f911315badd79af1d0f107fee0ea488467c90364bd9ff0ddc4fb4c3.

- 2026-09-27T10:18:28+00:00: Recorded command exit 0; command argv SHA-256
  2f2d21c06f911315badd79af1d0f107fee0ea488467c90364bd9ff0ddc4fb4c3.

- 2026-09-27T10:18:48+00:00: Recorded command exit 0; command argv SHA-256
  2f2d21c06f911315badd79af1d0f107fee0ea488467c90364bd9ff0ddc4fb4c3.

- 2026-09-27T10:19:24+00:00: Recorded command exit 0; command argv SHA-256
  2f2d21c06f911315badd79af1d0f107fee0ea488467c90364bd9ff0ddc4fb4c3.

- 2026-09-27T10:20:30+00:00: Heartbeat by ar1332-record-replay-luna56.

- 2026-09-27T10:20:39+00:00: Recorded command exit 0; command argv SHA-256
  75f984b97c3a9a14ed6ee72aa70d02691b7fe4b55d66a0588efa8bbc20578ec4.

- 2026-09-27T10:21:03+00:00: Recorded command exit 0; command argv SHA-256
  8ec3ee45c8f35ca2a6cf3d091364dfa70255937997638eafe23e0681633b7382.

- 2026-09-27T10:21:37+00:00: Recorded command exit 0; command argv SHA-256
  8ec3ee45c8f35ca2a6cf3d091364dfa70255937997638eafe23e0681633b7382.

- 2026-09-27T10:21:57+00:00: Heartbeat by ar1332-record-replay-luna56.

- 2026-09-27T10:22:27+00:00: Recorded command exit 0; command argv SHA-256
  8ec3ee45c8f35ca2a6cf3d091364dfa70255937997638eafe23e0681633b7382.

- 2026-09-27T10:22:52+00:00: Recorded command exit 0; command argv SHA-256
  8ec3ee45c8f35ca2a6cf3d091364dfa70255937997638eafe23e0681633b7382.

- 2026-09-27T10:23:15+00:00: Recorded command exit 0; command argv SHA-256
  8ec3ee45c8f35ca2a6cf3d091364dfa70255937997638eafe23e0681633b7382.

- 2026-09-27T10:23:37+00:00: Recorded command exit 0; command argv SHA-256
  2ab175fdb482b2e1fa647bd2b6e4a7278e4bed4a6b349140aab246ccc59bec0f.

- 2026-09-27T10:24:00+00:00: Recorded command exit 0; command argv SHA-256
  8ec3ee45c8f35ca2a6cf3d091364dfa70255937997638eafe23e0681633b7382.

- 2026-09-27T10:24:36+00:00: Independent review complete: one scoped ASB-only change in
  crates/asb-workloads/src/refresh.rs plus docs/WORKLOADS.md; signed+DCO head
  73b5fd1d14fa0343a7f3cc6d73acc91187d46333. Strict content-addressed LiveCodeBench/SWE-rebench
  manifest validates source/dataset/window/cutoff/split/evaluator/image/SBOM/license/evidence
  identity, rejects unknown/tampered/incomplete/cross-window inputs, and has positive/negative
  tests. No asb-tui, provider, network, or credential changes. PR #355 exact-head all 13 required
  checks SUCCESS.

- 2026-09-27T10:24:49+00:00: Recorded command exit 0; command argv SHA-256
  20f3f61fe754a0f00783e9c2be0917d9cdf06374c5c05671e10718108086a4c5.

- 2026-09-27T10:25:14+00:00: Recorded command exit 2; command argv SHA-256
  a7cb7f030eb278c0a4176a2b9d0cd1df0c824db937dbeab0a32531537f267e68.

- 2026-09-27T10:25:38+00:00: Recorded command exit 0; command argv SHA-256
  77ade6007801d106477aa5c49fa00a58f5952c5f4e6b1348312672fbb7c46fd0.

- 2026-09-27T10:26:02+00:00: Recorded command exit 0; command argv SHA-256
  355b6f244f6fc49a19b63a7fc3bf5420a18ec5561b988f2500454c7166ebf44e.

- 2026-09-27T10:26:45+00:00: Recorded command exit 0; command argv SHA-256
  355b6f244f6fc49a19b63a7fc3bf5420a18ec5561b988f2500454c7166ebf44e.

- 2026-09-27T10:27:08+00:00: Recorded command exit 0; command argv SHA-256
  355b6f244f6fc49a19b63a7fc3bf5420a18ec5561b988f2500454c7166ebf44e.

- 2026-09-27T10:27:57+00:00: Recorded command exit 0; command argv SHA-256
  355b6f244f6fc49a19b63a7fc3bf5420a18ec5561b988f2500454c7166ebf44e.

- 2026-09-27T10:28:15+00:00: Heartbeat by ar1332-record-replay-luna56.

- 2026-09-27T10:28:24+00:00: Recorded command exit 0; command argv SHA-256
  355b6f244f6fc49a19b63a7fc3bf5420a18ec5561b988f2500454c7166ebf44e.

- 2026-09-27T10:29:12+00:00: Recorded command exit 0; command argv SHA-256
  355b6f244f6fc49a19b63a7fc3bf5420a18ec5561b988f2500454c7166ebf44e.

- 2026-09-27T10:30:06+00:00: Recorded command exit 0; command argv SHA-256
  355b6f244f6fc49a19b63a7fc3bf5420a18ec5561b988f2500454c7166ebf44e.

- 2026-09-27T10:30:34+00:00: PR #355 is merged normally: merge SHA
  5e577e6a4b278fc79dc8b695cd6b3723d04cc609, reviewed head 73b5fd1d14fa0343a7f3cc6d73acc91187d46333,
  base a36b86b49a347b3e5e32154c465c3ef3e9a03a11. Exact-main post-merge runs: Huawei 36312453082
  SUCCESS; Formal 36312453087 SUCCESS; Fault 36312453109 SUCCESS; Credential-free 36312453110
  SUCCESS; Hosted 36312453113 SUCCESS; Rust 36312453077, Emulated AArch64 36312453084, Repository
  quality 36312453096 remain in progress. The earlier exit-2 record was only malformed jq quoting in
  a run-list query; merge API had already returned merged=true.

- 2026-09-27T10:31:19+00:00: Recorded command exit 0; command argv SHA-256
  355b6f244f6fc49a19b63a7fc3bf5420a18ec5561b988f2500454c7166ebf44e.

- 2026-09-27T10:31:43+00:00: Recorded command exit 0; command argv SHA-256
  88d3c551fd5c45c03b355d45eb12c10b4d7575d24921187a53fa8b84c2847261.

- 2026-09-27T10:32:07+00:00: Recorded command exit 0; command argv SHA-256
  c295214ec39843a80fc3d0eeaf99a7a796730abff8b8045ef0be4ecc20f8b7fd.

- 2026-09-27T10:32:46+00:00: Recorded command exit 0; command argv SHA-256
  da127d4e69d4b7cfde3550464c3283e4c1651d494e540f57165deb65fbffa5c1.

- 2026-09-27T10:33:12+00:00: Post-merge AArch64 run 36312453084 failed unrelated existing asb-agents
  goose::tests::diagnostic_and_symlink_fail_closed: 186 passed, one failed because unwrap_err
  received an Ok GooseOutcome with redacted failed RPC and exit 127. Isolated serial focused
  reproduction in AR-1426 worktree passed 1/1, confirming runner-sensitive flake; no AR-1426 path
  involved. Preserve failure and retry exact failed workflow once; do not waive.

- 2026-09-27T10:33:21+00:00: Recorded command exit 0; command argv SHA-256
  b5e5ed59f8f840d4b53252fbba5ce93102a11c2cccc6064998028e323102f992.

- 2026-09-27T10:33:45+00:00: Recorded command exit 0; command argv SHA-256
  1cdef511c02d6c41abd9e62231f3c2af96bde31a21ea789087971315c9836c1e.
