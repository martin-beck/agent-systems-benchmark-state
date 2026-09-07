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
  "next_action": "Monitor PR #28 exact e6c6231 runs: fault 34077596424, quality 34077596437, Rust 34077596423 and formal 34077596425; investigate any failure and do not merge.",
  "observed_branch": "feature/fault-assurance",
  "observed_dirty": 0,
  "observed_head": "e6c623113c15c99950889b26cd70b29c6966b1d4",
  "owner": "contracts-20260906",
  "plan": "../plans/AR-0902.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Stress parser, archive, path, recovery and cleanup boundaries with meaningful failure injection.",
  "task_revision": 94,
  "title": "Add fuzz mutation and lifecycle fault campaigns",
  "updated_at": "2026-09-07T02:50:31+00:00",
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

- 2026-09-07T02:34:20+00:00: Recorded command exit 0; command argv SHA-256
  eedc2fabd73ad176757039b641e38694c8367a82f3d39416c9c56735dfebf195.

- 2026-09-07T02:34:51+00:00: Recorded command exit 101; command argv SHA-256
  34b8bfd0f73b6f259871abf5b8696737397a51332c1ea16e4f8a680bf3b201d0.

- 2026-09-07T02:35:18+00:00: Recorded command exit 127; command argv SHA-256
  1981a992fab5cd5a9c761bf09537596b060c3feb156f35b7169c3592916146a6.

- 2026-09-07T02:35:37+00:00: Recorded command exit 0; command argv SHA-256
  4eb4ddd2dda094072e1c5209125fccd86840f9bfa74022711554f76929046c31.

- 2026-09-07T02:36:35+00:00: Recorded command exit 0; command argv SHA-256
  8161396622b23cb97870e327bfd19cf647f50b2f7355ba9fdb5b22b001180b70.

- 2026-09-07T02:37:15+00:00: Recorded command exit 0; command argv SHA-256
  b22407d9041ac3777b28b897653e70f9612d8de43d1925f091d4dfee2b05a8de.

- 2026-09-07T02:37:59+00:00: Recorded command exit 2; command argv SHA-256
  50b5d2e8ceabf75d95f74d259f8bf2ec46e378847a48b863daf790f568300400.

- 2026-09-07T02:38:15+00:00: Recorded command exit 0; command argv SHA-256
  9687874040dea86ff8100e43b241d0afee6d84b4444df1406f789adbf9e5d19a.

- 2026-09-07T02:38:43+00:00: Recorded command exit 0; command argv SHA-256
  7bda09615358e1b3bf3e77562cc1a458fdad5b45253c1dff50d6582c6cfcce1a.

- 2026-09-07T02:39:02+00:00: Recorded command exit 0; command argv SHA-256
  3f445927c05aac0b6b33a340fa938f3f1e1f6338cda442c6877a701f023554a9.

- 2026-09-07T02:39:24+00:00: Superseded 68ecb4e with focused signed+DCO hygiene repair ad00e8b:
  crash child now runs inside its owned scratch root and writes an asserted cwd proof; cargo-fuzz
  0.13.2 help was inspected and has no --locked option, so bounded fuzz performs cargo metadata
  --locked preflight plus lock checksum verification, external target placement, git diff and status
  cleanliness; README now says all six mutation sentinels. Focused store fault 3/3, workspace
  fmt/clippy/test/docs/release, coverage 91.81% regions and 94.87% lines with configured critical
  floors, deny/audit, formal tests, failure fixtures, platform validator/tests, actionlint, offline
  zizmor, repository policy, signatures/DCO, exact-range Gitleaks, scope and clean tree passed.
  Initial focused compile failed only because the new external TMPDIR was absent and passed after
  wrapped creation. Local offline fuzz metadata remains unable to fetch uncached target-specific
  getrandom 0.4.3; no network was used and hosted online locked preflight is the publication proof
  gate.

- 2026-09-07T02:42:11+00:00: Recorded command exit 0; command argv SHA-256
  5306d1801303684f66d472708f91bd97290ef10307324988eddb83ca5dc1b0f0.

- 2026-09-07T02:42:23+00:00: Coordinator independently approved immutable AR-0902 candidate
  ad00e8b1ea1607043eea9bfe6d86d8d4828abe92 for publication. Immediately before publication, exact
  base e85548d, two-commit ancestry, clean tree, both SSH signatures, exact DCO trailers, 19-path
  additive scope, repository policy, privacy review, exact-range Gitleaks and absent remote feature
  ref were reverified.

- 2026-09-07T02:42:38+00:00: Recorded command exit 0; command argv SHA-256
  ff3e2ec359fe6a64fd716d4e36c99b2656ffaa94b020f4c859d0e346e9267489.

- 2026-09-07T02:43:00+00:00: Recorded command exit 0; command argv SHA-256
  a1576363288ea0ea0fa55f8af23fce1d85e0dae99e47b16cea2cf649f29736a5.

- 2026-09-07T02:43:22+00:00: Published immutable approved head ad00e8b with explicit absent-ref
  force-with-lease and verified remote equality. Opened focused product PR #28
  https://github.com/martin-beck/agent-systems-benchmark/pull/28 at exact base e85548d and head
  ad00e8b. All four exact-head workflow runs started.

- 2026-09-07T02:45:16+00:00: Exact-head fault run 34077199689 bounded-fuzz job 101605557698 failed
  before fuzz execution in cargo deny: asb-fuzz lacked a license, its three local path dependencies
  were classified as wildcard, and libfuzzer-sys 0.4.13 requires NCSA in addition to MIT/Apache-2.0.
  This is deterministic policy configuration, not a fuzz finding or platform-specific failure.
  Retained faults passed both architectures; formal run is green.

- 2026-09-07T02:45:38+00:00: Recorded command exit 0; command argv SHA-256
  d3c3d131027537036820bee6afd0d4f8ba976ccdd9c367bdce36af701ead29b0.

- 2026-09-07T02:46:07+00:00: Recorded command exit 0; command argv SHA-256
  8d2e48323be967ef9cb4e7667d4e98cefd1a856d40aa116059ff16e4e92a4eaf.

- 2026-09-07T02:46:29+00:00: Recorded command exit 0; command argv SHA-256
  d68ee43e2875019bf9de85ebc185d595177ae8a7465eec7712de3d757dd75e3b.

- 2026-09-07T02:46:46+00:00: Recorded command exit 0; command argv SHA-256
  ca96336b36cfb812548f0a6d6c33bcefccfd7e41b22e7ee57a793234077f3769.

- 2026-09-07T02:47:31+00:00: Recorded command exit 0; command argv SHA-256
  5b402021788fe3dd83b03dab560251d0f9bafe95bd6747fb8e25201dc50b627d.

- 2026-09-07T02:47:48+00:00: Focused successor e6c6231 adds MIT package metadata, exact =0.1.0 local
  path dependency versions, and fuzz/deny.toml retaining root bans/sources while narrowly allowing
  audited NCSA required by pinned libfuzzer-sys 0.4.13. Root deny.toml is unchanged. Offline
  Linux-target cargo-deny now reports advisories/bans/licenses/sources all ok; all four fuzz bins
  compile locked/offline; TOML, actionlint, offline zizmor, repository policy, exact-range Gitleaks,
  signature/DCO, diff/scope and clean-tree checks pass. PR #28 remains at prior ad00e8b pending
  review; no rerun or push performed.

- 2026-09-07T02:49:49+00:00: Independent immutable review approved exact successor
  e6c623113c15c99950889b26cd70b29c6966b1d4. Before the authorized update, local tree was clean, SSH
  signature and exact DCO were valid, and both remote branch and PR #28 remained exact ad00e8b.

- 2026-09-07T02:50:09+00:00: Recorded command exit 0; command argv SHA-256
  601796a68f81f1c98c74af6be59c0a1a52611e5c680a9ceae7fccc8dfee3c094.

- 2026-09-07T02:50:31+00:00: Updated PR #28 remote branch from ad00e8b to independently approved
  exact e6c6231 using explicit force-with-lease against ad00e8b; remote and PR head equality
  verified. Fresh exact-head fault, quality, Rust and formal runs started.
