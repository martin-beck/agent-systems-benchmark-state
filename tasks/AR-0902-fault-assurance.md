---
{
  "branch": "feature/fault-assurance",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-07T04:01:33+00:00",
  "depends_on": [
    "AR-0103",
    "AR-0104",
    "AR-0503"
  ],
  "id": "AR-0902",
  "next_action": "Await coordinator instruction for one controlled rebase onto current signed product main, then rerun affected exact-tree gates and independent immutable review before publication.",
  "observed_branch": "feature/fault-assurance",
  "observed_dirty": 3,
  "observed_head": "68ecb4e97d848ff59f51aaf64030271f72a200aa",
  "owner": "contracts-20260906",
  "plan": "../plans/AR-0902.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Stress parser, archive, path, recovery and cleanup boundaries with meaningful failure injection.",
  "task_revision": 65,
  "title": "Add fuzz mutation and lifecycle fault campaigns",
  "updated_at": "2026-09-07T02:33:57+00:00",
  "worktree_key": "agent-systems-benchmark-fault-assurance"
}
---
## AR-0902

Stress parser, archive, path, recovery and cleanup boundaries with meaningful failure injection.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-07T01:49:31+00:00: Coordinator verified AR-0103, AR-0104, and AR-0503 are durably done;
  AR-0902 fuzz/fault/scheduled-workflow paths are dependency-ready and disjoint from active AR-0801
  CLI, AR-0307 Goose registration/native workflow serialization, and AR-0308 mini-SWE isolated
  adapter work. Promotion authorizes only its declared bounded campaigns; shared workspace/schema
  changes remain coordinator-serialized.

- 2026-09-07T01:49:58+00:00: Claimed by contracts-20260906.

- 2026-09-07T01:50:14+00:00: Recorded command exit 0; command argv SHA-256
  9e6176fef0338084555f6e038c7a58f8f9d802b950b675780d3496a1eee59ccc.

- 2026-09-07T01:50:27+00:00: Claimed AR-0902 after signed+DCO promotion e04bdbb and created clean
  declared feature/fault-assurance worktree at exact product main e85548d. Exclusive fence before
  mutation: new fuzz targets, fault tests and a dedicated scheduled workflow only. No asb-cli paths,
  asb-agents/lib.rs, Goose or mini-SWE files; shared Cargo/workspace/schema remains
  coordinator-serialized. Workflow overlap must be acknowledged by AR-0307 before editing.

- 2026-09-07T01:51:28+00:00: AR-0307 owner confirmed no workflow overlap: AR-0902 exclusively owns
  new .github/workflows/fault-assurance.yml; verify.yml, quality.yml, formal.yml and all Goose paths
  remain excluded. Existing repository-policy/actionlint/zizmor expectations will be validated
  rather than changed without coordination.

- 2026-09-07T01:52:33+00:00: Heartbeat by contracts-20260906.

- 2026-09-07T01:54:46+00:00: Recorded command exit 0; command argv SHA-256
  458bab1b2166e0c145e1674942cae2bdd6cf91d78845fb9d62e3590af76f5681.

- 2026-09-07T01:55:07+00:00: Pinned cargo-fuzz 0.13.2 and cargo-mutants 27.1.0 installed
  successfully under /srv/data/projects/.asb-local/fault-tools through the AR wrapper without
  product-tree changes. A first evidence update invocation failed before mutation because update
  requires --expected-revision; corrected against fresh revision 9.

- 2026-09-07T02:03:47+00:00: Recorded command exit 0; command argv SHA-256
  6366629e62d3a7812026aa8926be8bb8fe27edc9b527575265acdd5bf1b754e2.

- 2026-09-07T02:04:00+00:00: Recorded command exit 101; command argv SHA-256
  5459c696e63d376e29c37e46169c5c1d8954e160487694704f8e21270cb889c0.

- 2026-09-07T02:04:11+00:00: Recorded command exit 0; command argv SHA-256
  89caf2d75d72f38a4ec90a6a9fc78b32c561ef3334d780682428eeecbe409920.

- 2026-09-07T02:04:35+00:00: Recorded command exit 101; command argv SHA-256
  5459c696e63d376e29c37e46169c5c1d8954e160487694704f8e21270cb889c0.

- 2026-09-07T02:05:17+00:00: Recorded command exit 0; command argv SHA-256
  53ca6d565a568971b812cde415b02e94c4953fb03601aa0996038cc0c6e4d07d.

- 2026-09-07T02:05:26+00:00: Recorded command exit 0; command argv SHA-256
  9e1abd45fe789d7a35901c61696bcef281f5d623d0c9b5556f78a5d654630d64.

- 2026-09-07T02:06:45+00:00: Recorded command exit 0; command argv SHA-256
  a50d1dd085e1cee41f06f6fb6c140298b95c49cf853d272eb5a7232f9f4b418d.

- 2026-09-07T02:07:41+00:00: Recorded command exit 0; command argv SHA-256
  d618142e53613401f51c15787bc8a24729b562ac3df10911391b0b03e5066e27.

- 2026-09-07T02:08:26+00:00: Recorded command exit 0; command argv SHA-256
  8379ea8a2ca088a8dd1804adfae4b72508177533d28de690dc3856acab8005f7.

- 2026-09-07T02:08:50+00:00: Recorded command exit 0; command argv SHA-256
  17380d5b45d5d092043d25c4be29d6ae9c927983beb1618cba417415dac2c43e.

- 2026-09-07T02:09:03+00:00: Recorded command exit 0; command argv SHA-256
  0abcb0dedce3c7cc023426eb97dd7f78ca449acbaf5ce470efaba5f3c155abaa.

- 2026-09-07T02:09:32+00:00: Recorded command exit 0; command argv SHA-256
  4d54dce721f1a89441a75a32a5fccf0ec34f711cb7d3fe98b0fab9307db02da2.

- 2026-09-07T02:10:33+00:00: Recorded command exit 0; command argv SHA-256
  1c15cd831df0c6dc943cd1cecc1569c11f5f1d4e9e1d8b83855bb43dc23e71a9.

- 2026-09-07T02:11:00+00:00: Recorded command exit 0; command argv SHA-256
  7ed22880e0aebf7e936b06fd011ba9b5f2a3995d15ef3ef5e57167d652bc019a.

- 2026-09-07T02:11:47+00:00: Recorded command exit 2; command argv SHA-256
  bc2c6fc569616e2b891ec958229f0ad3b1ff50652256682ccea74c3ea41bf427.

- 2026-09-07T02:12:12+00:00: Recorded command exit 0; command argv SHA-256
  6ca34b96570d3f6d0d09a8ba9fcf234a7220bea9ca9c49ef5c5ed394b5207c1e.

- 2026-09-07T02:12:49+00:00: Recorded command exit 2; command argv SHA-256
  02285b424bea293899cf8a7120c6d799c8a8545f533084cd83ed5b97996c870b.

- 2026-09-07T02:13:31+00:00: Recorded command exit 0; command argv SHA-256
  0a6c03543d45d0be70be24347857d59ae7d1543f2dd44cf6ad4918a42fdf7ce3.

- 2026-09-07T02:13:51+00:00: Recorded command exit 0; command argv SHA-256
  6ca34b96570d3f6d0d09a8ba9fcf234a7220bea9ca9c49ef5c5ed394b5207c1e.

- 2026-09-07T02:14:04+00:00: Focused native fault evidence passed: store integration 3/3 including
  real child SIGABRT recovery and storage-reader failure cleanup; existing atomic disk-full/crash
  boundary 1/1; replay real loopback disconnect 1/1 with retry-safe cursor. Initial cargo-mutants
  selectors were invalid assurance: return-value mutants were unviable, and a 2-job shared-target
  run cross-contaminated fingerprints; a serial rerun exposed one genuinely surviving SLO guard.
  Changed campaign to four viable matcher comparisons, one viable SLO minimum-bound comparison, and
  one accounting-field mutant; fresh isolated run caught all 6/6 with zero missed/timeout/unviable.
  Do not claim the superseded all-caught parallel result.

- 2026-09-07T02:14:58+00:00: Recorded command exit 0; command argv SHA-256
  13370c0bb4eebc09d3ee4946e362c08c8776d80d36272637472457b791765fe2.

- 2026-09-07T02:15:46+00:00: Recorded command exit 0; command argv SHA-256
  683d93022d881f5f64dc74a0586cafa6940b98b6677120f2d06f485a7227c358.

- 2026-09-07T02:16:12+00:00: Recorded command exit 0; command argv SHA-256
  c7a2ff947116955fa0e72592d07ffe6d9bcbc7e884e131f62ccf5223b2db5583.

- 2026-09-07T02:16:27+00:00: Recorded command exit 1; command argv SHA-256
  90b0982d3edc6dd04b425781f9647269a3cb2063545e2062aec231f79027b31a.

- 2026-09-07T02:16:53+00:00: Recorded command exit 0; command argv SHA-256
  cd226dfee1fc90a143556cbf5f7a4bcbd15c7171fe87cd629d558af570ce7694.

- 2026-09-07T02:17:19+00:00: Recorded command exit 0; command argv SHA-256
  4e5210e1cc137a32b25fc378c17085e21d09baef526df2c719441e2d8741a513.

- 2026-09-07T02:17:33+00:00: Recorded command exit 0; command argv SHA-256
  902791fee109e79ae976a22840158be2decf7fd62185b5c195b2fda76fb11e51.

- 2026-09-07T02:17:45+00:00: Recorded command exit 0; command argv SHA-256
  b27a440401d7b0d722a869ea20c4669e36a46180d461f825bc5ae2f3c93013eb.

- 2026-09-07T02:18:17+00:00: Recorded command exit 0; command argv SHA-256
  518e63910987c688481699d3b5707f8e101b475a2037070efb8997c342ce288c.

- 2026-09-07T02:18:39+00:00: Recorded command exit 0; command argv SHA-256
  4dffa2221ea82f39eab2fe03911b1a358325bd7dcf7059f9266c09cf9961fa07.

- 2026-09-07T02:19:12+00:00: Recorded command exit 0; command argv SHA-256
  d930ec9d3dccc5d56719161844b1d3d8e4a577e6725847dd4a5d6f741345bfa1.

- 2026-09-07T02:19:23+00:00: Recorded command exit 0; command argv SHA-256
  0fd9ff1e1c38f3ddfd6f3b5de5a9cf7194e00dfea4d1aaf2fe25c38aac7ddba6.

- 2026-09-07T02:19:38+00:00: Recorded command exit 0; command argv SHA-256
  cb6d36ea0b47a8fe26c1431d4d3efe9c2565b579a2ed1da78b8b917be5bbcb47.

- 2026-09-07T02:20:30+00:00: Recorded command exit 1; command argv SHA-256
  1005cafcadab0ec0a0e7ad0b3963a32b0bd5f127f20c68a79ca4fc72569ff7bb.

- 2026-09-07T02:20:58+00:00: Recorded command exit 0; command argv SHA-256
  baa090ad05cfac5218778fdd1b5ed09599726a4f1ba17b7329110107df6f8b33.

- 2026-09-07T02:21:41+00:00: Recorded command exit 0; command argv SHA-256
  6c25efa0d090e71256e1e82b1f933477702ce2d0efab454a5550ce1a2a0f6318.

- 2026-09-07T02:22:11+00:00: Safe offline validation completed: seeded cargo-fuzz targets
  protocol_jsonrpc/cassette_decode/replay_sse/store_paths passed 32 runs each using pinned
  cargo-fuzz 0.13.2, libfuzzer-sys 0.4.13, installed nightly-2025-11-21; no worktree corpus/artifact
  or store-scratch residuals. Full workspace tests, clippy, rustdoc, release build, root cargo-deny,
  root cargo-audit no-fetch, platform validation, coverage floors, actionlint and offline zizmor
  passed; Gitleaks directory scan found no leaks. Independent fuzz cargo-deny could not complete
  offline because target-specific getrandom 0.4.3 was not cached and network use is currently
  prohibited; dedicated hosted workflow installs pinned deny/audit and makes this a publication
  gate. Physical ENOSPC/power-loss remains explicitly unsupported.

- 2026-09-07T02:22:38+00:00: Recorded command exit 0; command argv SHA-256
  0e5962c0519a91b9d472cadf46d01bd228bff0bac284bfd1f09770b73072d5d4.

- 2026-09-07T02:22:52+00:00: Recorded command exit 1; command argv SHA-256
  1280bff0d3a8f622069e3f22cf477c4b010624f7bb6d6169dae58ad9a75d57a2.

- 2026-09-07T02:23:20+00:00: Recorded command exit 0; command argv SHA-256
  a59ba6d9a29e8e614d0fbb57ccf1db0964aaa7fc404b7c7364278086d8dee9aa.

- 2026-09-07T02:23:34+00:00: Recorded command exit 0; command argv SHA-256
  99e4d74e450072bcc9980db09cea19ddcdfba6fb8901906908895f92e7bd976e.

- 2026-09-07T02:23:52+00:00: Created clean focused SSH-signed exact-DCO candidate
  68ecb4e97d848ff59f51aaf64030271f72a200aa, tree 1de9afa8013c51a614e42a682dd877a57b533758, base
  e85548d00cffcc3a014bfbc04b8fc79c5fe35da0. Exact-commit DCO, repository policy, Gitleaks,
  diff-check, actionlint and offline zizmor pass. First candidate a13a2a8 failed repository policy
  because a new upload-artifact pin was absent from shared policy; honoring the no-platform-policy
  boundary, removed that upload step and now retain reviewed corpus seeds only. New failures are
  disposable-runner-only until reproduced/minimized/privacy-reviewed and committed; this limitation
  is explicit.

- 2026-09-07T02:31:33+00:00: Heartbeat by contracts-20260906.

- 2026-09-07T02:31:43+00:00: Recorded command exit 101; command argv SHA-256
  8c02a6901fe37a4820df929524704e90c05cfc961a3d581643efa354b4c067ef.

- 2026-09-07T02:32:08+00:00: Recorded command exit 0; command argv SHA-256
  6a19ab419bdbd81680b5966f7f06d436780640d808a5120ee7d7dfcc314c9da6.

- 2026-09-07T02:33:09+00:00: Recorded command exit 0; command argv SHA-256
  3dac80f98a84bd147489166cda22fea0ac01f910ac9c928e4e4000842ba58748.

- 2026-09-07T02:33:29+00:00: Recorded command exit 101; command argv SHA-256
  d6d9ac8bf85a329ea813441d4f7c5f3f1e047fdc3b4ab887baec442a3a6108b0.

- 2026-09-07T02:33:57+00:00: Recorded command exit 0; command argv SHA-256
  584ae8edd568b6d633e57f3a62300069b5d46f84f501a32e86f78718753e1d28.
