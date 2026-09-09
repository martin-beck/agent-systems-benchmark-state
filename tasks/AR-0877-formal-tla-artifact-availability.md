---
{
  "branch": "fix/formal-tla-artifact-availability",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-09T16:25:26+00:00",
  "depends_on": [
    "AR-0003",
    "AR-0901",
    "AR-0902"
  ],
  "id": "AR-0877",
  "next_action": "Independent immutable review of f80c53f0; publish only after approval, then require exact-head CI and post-merge exact-main verification.",
  "observed_branch": "fix/formal-tla-artifact-availability",
  "observed_dirty": 4,
  "observed_head": "f80c53f0cdf5be9f81715009f13fbc6a050093ba",
  "owner": "quality_20260906",
  "plan": "../plans/AR-0877.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Repair the formal workflow's unavailable TLA+ artifact pin without weakening provenance or offline verification.",
  "task_revision": 76,
  "title": "Repair formal TLA artifact availability",
  "updated_at": "2026-09-09T14:16:16+00:00",
  "worktree_key": "agent-systems-benchmark-formal-tla-artifact-availability"
}
---
## AR-0877

Replace the TLA+ release-asset URL that returns HTTP 404 with an authoritative, durable,
content-verified acquisition and offline-cache boundary. Preserve all positive and deliberate
mutation formal checks.

Implementation has not started. Read the linked plan before claiming.


- 2026-09-09T01:01:21+00:00: Dependencies AR-0003, AR-0901, and AR-0902 are done; owned formal
  acquisition paths are disjoint from active AR-0806 TUI, AR-0855 state vendor, and AR-0876
  provider-launch scopes. Promote for the blocking TLA+ artifact availability repair.

- 2026-09-09T01:01:25+00:00: Claimed by replay_20260906.

- 2026-09-09T01:01:44+00:00: Recorded command exit 0; command argv SHA-256
  dd885d3beb1c7712be2c40fc7a268651d94964934cea87ee439edf2d698d0f77.

- 2026-09-09T01:02:47+00:00: Claimed clean isolated worktree
  /srv/data/projects/agent-systems-benchmark-formal-tla-artifact-availability at exact product main
  dca243ab7b8cbb0b2b49a568dec99c517e0719c2 after reading required docs and full plan. Initial audit
  found existing signed commit 7add29f already changed four owned paths to GitHub API asset
  551007111, SHA-256 4c7bb1f6..., and 4487756 bytes, but the current shell fetch still follows
  redirects generically and lacks the plan's metadata/approved-final-host, create-new atomic
  concurrency, hardlink/owner-mode, bounded retry, and comprehensive offline/cache fault boundary.
  Preserve this partial repin as provenance and implement the remaining fail-closed acquisition
  contract without changing authoritative TLA/Alloy models.

- 2026-09-09T01:15:21+00:00: Recorded command exit 0; command argv SHA-256
  70f1fead417b3551ce217b80588f20f9dbde4f1dcadb78008ccc4be6ff343440.

- 2026-09-09T01:16:06+00:00: Recorded command exit 0; command argv SHA-256
  5e5ecd106803e960373de65301f4e5653ca8202f0b4a5150d59a5b3ccdeeeded.

- 2026-09-09T01:18:10+00:00: Recorded command exit 0; command argv SHA-256
  ba8ee64e9597bd068dffbae0ae9f9eee17f60682a6c59868f2dcae8a4b48f195.

- 2026-09-09T01:19:30+00:00: Recorded command exit 1; command argv SHA-256
  32b5fe4cf3e4b6847c396e7fc5fd5e904e79d55d6de51d689484ea716904e270.

- 2026-09-09T01:20:05+00:00: Recorded command exit 2; command argv SHA-256
  5f2552aa6dd90afe912fa78e648362c3ca4d79143c30fa8a390c6f20faa59895.

- 2026-09-09T01:21:40+00:00: Recorded command exit 127; command argv SHA-256
  4b17e7752a0c32c0141c6e60bcda040b8eb37f78ac08d824c892eabbe339a747.

- 2026-09-09T01:22:11+00:00: Recorded command exit 125; command argv SHA-256
  511e90a6efd8c1956407c06f49626a12dd557162cdd22cb36acda7c42a27bfb0.

- 2026-09-09T01:22:47+00:00: Recorded command exit 0; command argv SHA-256
  7fee32c1d48c1dd50db6f6ef51a231d7b74f22e25d6c4d7d55d05e96152780ea.

- 2026-09-09T01:23:15+00:00: Recorded command exit 0; command argv SHA-256
  58ce5aefe9171d539aa56c74501defa195cf02ff0703e7eb4486682dcb6a5efa.

- 2026-09-09T01:24:53+00:00: Recorded command exit 0; command argv SHA-256
  6db81dfd389a4e735655ca6c6769d7240798c9a7fe78bbdc832fcaa9fe2785d0.

- 2026-09-09T01:25:24+00:00: Recorded command exit 0; command argv SHA-256
  67a1ac3216b08a8447f308a1f703911a2d34cfca400ab44b12f349632349210f.

- 2026-09-09T01:26:09+00:00: Substantive acquisition implementation checkpoint on exact base
  dca243ab with four owned dirty paths: formal/run_temporal_models.sh, formal/toolchains.toml,
  formal/tests/toolchain_pins.rs, formal/README.md. Live authoritative release evidence changed
  after the earlier partial repin: tag v1.8.0 still resolves to source b123b226, but current release
  25926686 publishes tla2tools.jar asset 551679598 created 2026-09-09T00:59:49Z, 44892330?
  Superseded typo: exact size is 4489230 bytes and SHA-256
  13885c0971b5faf31c89b89b90784c2bf3e2939632aa1ab10499504627e47209. Implementation binds
  release/tag/asset metadata, exact source ref, stable browser route, approved HTTPS final host set,
  bounded retries/bytes/time, exclusive cache lock, create-new partials, atomic no-clobber
  promotion, owner/mode/single-link checks, strict offline reuse, and cleanup. Real online acquire
  and offline zero-network cache reuse pass; cache mode 400/link count 1/digest exact. Offline
  missing, corrupt, symlink, and hardlink cases fail before a curl sentinel. bash -n, diff-check,
  and formal toolchain-pin test pass. One earlier wrapper exit was operator-only PATH loss and
  corrected with pinned cargo; no product failure. ShellCheck is unavailable locally and remains a
  required hosted/final gate.

- 2026-09-09T01:49:17+00:00: Recorded command exit 2; command argv SHA-256
  aa40dbb37fa84371f5b5b2b8fef237998d4b73113063ecdcd7bd4e49080835f6.

- 2026-09-09T01:50:30+00:00: Recorded command exit 0; command argv SHA-256
  a14346543cf4e68d0c93d7e0e9f2c45417c4ddc196c53fae34ae1ac567675bdb.

- 2026-09-09T01:51:08+00:00: Recorded command exit 0; command argv SHA-256
  1048003a12beab80a5c070bfa62dc6bbf9cc0c57bcd6b3b4969de2d26c52513e.

- 2026-09-09T01:51:49+00:00: Exact upstream blocker discovered during full acquisition verification.
  GitHub release 25926686 is a mutable v1.8.0 pre-release rebuilt from the same b123b226 tag: asset
  551007111 is now HTTP 404; asset 551679598 observed at 00:59:49Z with 4489230 bytes/digest
  13885c09 was deleted during this AR and is now HTTP 404; replacement 551717837 created 01:24:53Z
  has 4489229 bytes/digest f3a6ba40 and is HTTP 200. Published_at also changed from 01:01:29Z to
  01:26:05Z. The pre-body redirect hardening and owner/single-link/offline cache prototype remains
  dirty, bash syntax/diff-check and focused pin test pass, but its exact metadata intentionally
  rejects the replacement and full TLC cannot run. Re-pinning each transient rebuild would violate
  AR-0877 durable-asset acceptance; no signed candidate was created.

- 2026-09-09T02:08:16+00:00: Released without discarding the four-path dirty prototype. Exact
  blocker remains: upstream TLA+ v1.8.0 prerelease asset IDs 551007111 and 551679598 were deleted,
  replacement 551717837 changed bytes/digest/publication time, so AR-0877 cannot select a durable
  artifact. Continue only after AR-0878 qualifies an immutable publication or deterministic
  source-build contract.

- 2026-09-09T03:45:56+00:00: Claimed by codex-longrun-tla-20260909.

- 2026-09-09T03:45:59+00:00: Heartbeat by codex-longrun-tla-20260909.

- 2026-09-09T03:46:22+00:00: Reconciled existing prototype: authoritative v1.8.0 prerelease asset
  was deleted/rebuilt with changed bytes; no durable artifact exists. Preserve dirty four-path
  prototype and wait for AR-0878 immutable publication or approved source-build boundary.

- 2026-09-09T06:09:00+00:00: Coordinator metadata maintenance shortened only the stale
  front-matter projection to satisfy the existing schema. Prior value preserved verbatim:
  `Hold the four-path acquisition prototype unchanged and obtain an authoritative immutable TLA+ 1.8.0 artifact publication (or coordinator authorization for a separately specified reproducible source-build boundary); then refresh exact metadata once, finish deterministic faults, and run TLC/Alloy. Do not chase the continuously replaced v1.8.0 pre-release asset.`

- 2026-09-09T13:25:24+00:00: AR-0878 is durably done and supplies the independently qualified
  deterministic source-build manifest and output digest; resume AR-0877 to integrate that immutable
  artifact boundary instead of repinning the mutable v1.8.0 prerelease asset.

- 2026-09-09T13:25:26+00:00: Claimed by quality_20260906.

- 2026-09-09T13:26:19+00:00: Recorded command exit 0; command argv SHA-256
  c78581320d3e12633fef33a74574afb816fe7ba23d209b6b6b0e0143e9ecb31a.

- 2026-09-09T13:26:37+00:00: Recorded command exit 0; command argv SHA-256
  6013953a513ecfd22921b2c034badd44c2c2f70cdda6189ff3d5811efba751c4.

- 2026-09-09T13:35:20+00:00: Recorded command exit 0; command argv SHA-256
  cafd01ec6c28e186f06b27562a07d847df1892ef19eb2056eb33e646e7b6baca.

- 2026-09-09T13:35:39+00:00: Recorded command exit 101; command argv SHA-256
  ea1da65c43465b78823f9b39067dfee3e72ea05fe75e2ff086c9b16946893b92.

- 2026-09-09T13:36:24+00:00: Recorded command exit 101; command argv SHA-256
  133ea1df118454ba013b64456e63149ab94db6abba97e4f7f9204f68d8d74f37.

- 2026-09-09T13:36:58+00:00: Recorded command exit 101; command argv SHA-256
  ea1da65c43465b78823f9b39067dfee3e72ea05fe75e2ff086c9b16946893b92.

- 2026-09-09T13:37:39+00:00: Recorded command exit 0; command argv SHA-256
  1369d5c809bd46b3578e5d66ef11b3341668df701fe2d64b03bf667ba35b66dd.

- 2026-09-09T13:39:47+00:00: Recorded command exit 0; command argv SHA-256
  af697b674346d72fd2d1062eb60e19c8a3da7e839ae2e6a18631dfc6a50270fe.

- 2026-09-09T13:40:21+00:00: Recorded command exit 0; command argv SHA-256
  2b46248d1133fe995051da3408e766a1c0f4c87b210b9c462153c0e835be24cf.

- 2026-09-09T13:40:50+00:00: Recorded command exit 0; command argv SHA-256
  90c97aca0c958127f4373918c6d5fc85fa0ba79ef91e25acc28e233d8550508b.

- 2026-09-09T13:44:01+00:00: Recorded command exit 0; command argv SHA-256
  5eeb5b21ac80d3ad10cdaa66e608eb739c1f6d90cb233de423c4c2bca27556f9.

- 2026-09-09T13:44:28+00:00: Rebased preserved four-path prototype onto product main b6d04a8 and
  replaced mutable prerelease consumption with AR-0878 deterministic source-build output SHA-256
  8c200a88... (4512486 bytes). Exact dirty scope is eight AR-owned paths: formal workflow, README,
  runner, toolchain metadata/pin test, new acquisition test and two fixtures. A real pinned offline
  JAR ran TLC positive (3709 states/depth 17), deliberate stale mutation, Alloy positive and six
  mutants successfully. A clean source build from the exact cached source/Ant inputs reproduced
  8c200a88..., mode 0400/link count 1. Focused acquisition 6/6, provenance 4/4, and pin 1/1 tests
  pass. Earlier focused failures were harness assertions and one shell local-initialization bug;
  both are repaired and superseded by green results. No AR-0704 path changed and no mutable v1.8.0
  digest was repinned.

- 2026-09-09T13:45:28+00:00: Recorded command exit 101; command argv SHA-256
  b355aeb118f5bbd4d6cb86d0cc7884e14ad3040a8189010b68503f51c12e384b.

- 2026-09-09T13:46:01+00:00: Recorded command exit 0; command argv SHA-256
  bdb0ba9ddb445fe024f5d30723941c9989567b5172ea810ae5bedd70d51e1364.

- 2026-09-09T13:49:23+00:00: Recorded command exit 101; command argv SHA-256
  1429eec3c22851ad14a94bfa476b58b82ecedee4743914c40c1899dc29155c22.

- 2026-09-09T13:49:57+00:00: Recorded command exit 0; command argv SHA-256
  ea1da65c43465b78823f9b39067dfee3e72ea05fe75e2ff086c9b16946893b92.

- 2026-09-09T13:50:50+00:00: Recorded command exit 0; command argv SHA-256
  d92f928cf2661abd3fc2a3968ecf5e7cf69aaa839b4747fd10cc053133939487.

- 2026-09-09T13:52:34+00:00: Recorded command exit 0; command argv SHA-256
  771eb8f0e0bb85606686c22acbe4687aeadd8dedcc0ac28c2d9e1305ec80b673.

- 2026-09-09T13:55:32+00:00: Recorded command exit 1; command argv SHA-256
  5024b0ea9893becda16641ffa6bc5aaae6a566512d16c07f6e130461adf90ea3.

- 2026-09-09T13:56:23+00:00: Recorded command exit 1; command argv SHA-256
  de823dd8677742a72f9602e1d7890c90b1be45542e579231d2fe396ea0be26c4.

- 2026-09-09T13:56:52+00:00: Latest exit 1 was not a product failure: Gitleaks directory mode
  scanned generated formal/target build artifacts and found one redacted generated match after
  repository policy and source-header tests passed. Corrective action is a path-scoped scan of the
  exact eight-file dirty diff (and git-range scan after commit), without treating build output as
  source evidence; no retry of the broad generated-artifact scan.

- 2026-09-09T13:59:19+00:00: Recorded command exit 0; command argv SHA-256
  5ab0a9460a00b6b8b324f6e7a4143958abc552642424ba87c985e734e1dd72f3.

- 2026-09-09T13:59:40+00:00: Recorded command exit 0; command argv SHA-256
  4361510b3e02378cfbaf72fa9420e7312e87f254d013e693aec789e840db87f9.

- 2026-09-09T13:59:56+00:00: Recorded command exit 0; command argv SHA-256
  f404c36827be88da41be0562824b3628eaaf6e65ebc026f24a47b68a3edbb96f.

- 2026-09-09T14:00:23+00:00: Recorded command exit 0; command argv SHA-256
  e0ececf2e3fc0bb3a1369024f39c4c229553d084d3a1732951a6a396f214a821.

- 2026-09-09T14:00:44+00:00: Recorded command exit 0; command argv SHA-256
  62c6d86ae3c21d70bad0ec693eb4e7c4d52791e70b7f75f60c529594475711d4.

- 2026-09-09T14:01:14+00:00: Signed immutable AR-0877 candidate
  f80c53f0cdf5be9f81715009f13fbc6a050093ba, tree a1c21ad9a41d1814702e766af66711bd61370490, exact
  parent b6d04a8305ce6d49cc327e4e6d2d6fa42a88050b. Clean exact eight-path scope; SSH signature and
  exact DCO valid; diff-check, exact-range repository policy, path-scoped and commit-range Gitleaks,
  source headers 18/18, privacy scan, ShellCheck, actionlint, zizmor, cargo-deny/audit, 90.64%
  workspace coverage, and failure-path suite pass. Focused acquisition 7/7, source provenance 4/4,
  pin 1/1, full formal tests/docs, root fmt/clippy/workspace tests/docs/release pass. Real offline
  TLC positive (3709 states/depth 17), stale mutation negative, Alloy positive/six mutants, and
  clean deterministic source build reproduce exact 8c200a88 output. One broad directory Gitleaks
  exit was generated target output only and superseded by exact source/range scans; one
  repository-policy exit used literal WORKTREE and was operator-only, superseded by correct checks.
  No mutable prerelease repin, no AR-0704 path, and no prohibited private host identifier.

- 2026-09-09T14:07:54+00:00: Recorded command exit 0; command argv SHA-256
  28576358c51d02a34005100a3efc797dd535da239e0c5f1d643c59bbbd6cf36e.

- 2026-09-09T14:09:58+00:00: Recorded command exit 0; command argv SHA-256
  864c9f0353355f25d91220d3ff4279b4de5b53ffb31a21abc2c2dd96054f5935.

- 2026-09-09T14:10:21+00:00: Recorded command exit 101; command argv SHA-256
  420ad12ed18f0bad5b2ce91293668c0ffbf0829b55ae243d4c7a9ea76eb7d391.

- 2026-09-09T14:10:44+00:00: Recorded command exit 0; command argv SHA-256
  64d824abee31d47eaef0e83d8682f29ddd768152536c331ac33c567f3ee48bde.

- 2026-09-09T14:11:10+00:00: Recorded command exit 0; command argv SHA-256
  ae55530c2919aaf1f117dae14ad8247e9e1190f3ea3ed8f5a6ba1e9e73ee4030.

- 2026-09-09T14:12:01+00:00: Recorded command exit 0; command argv SHA-256
  7f946a6a75ee83cd036ede74cdda17f5fa2394185199b17d4c3f5f6d34b7b541.

- 2026-09-09T14:12:51+00:00: Recorded command exit 2; command argv SHA-256
  45037506241e8b4fb1f08bc496e0dff534dd738ef2483b374ae70607a47d1ad0.

- 2026-09-09T14:14:24+00:00: Recorded command exit 0; command argv SHA-256
  7163bdfd5062efcb65f092b3f607d7bf9ecc43f408293a1534c044fc5aee659c.

- 2026-09-09T14:15:19+00:00: Recorded command exit 0; command argv SHA-256
  b5749877892d35081f46cdb3bf4a0eeb839ba44d9c5a129b23d4d44af6ba4b1e.

- 2026-09-09T14:15:53+00:00: Recorded command exit 0; command argv SHA-256
  3d26d0fd37cbf62fb615e88e8b5e9b47c928be1406c9fa4cd57893c9a7f156b4.

- 2026-09-09T14:16:16+00:00: Recorded command exit 127; command argv SHA-256
  37ccca1df6540576773bda9b719f46832dded6f6a7e338a6e91c3789d1bf922c.
