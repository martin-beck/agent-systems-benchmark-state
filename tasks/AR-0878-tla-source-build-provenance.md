---
{
  "branch": "feature/tla-source-build-provenance",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-09T05:09:52+00:00",
  "depends_on": [
    "AR-0003",
    "AR-0901",
    "AR-0902"
  ],
  "id": "AR-0878",
  "next_action": "Run full locked formal workspace plus Alloy, repository-policy, privacy/Gitleaks, supply and coverage gates; obtain ShellCheck from the authorized pinned quality runner or record its exact unavailable boundary; then sign the exact eight-path candidate for immutable review.",
  "observed_branch": "feature/tla-source-build-provenance",
  "observed_dirty": 3,
  "observed_head": "af9fb7dcaabc162b13d6ee1e77d8915b6d82df20",
  "owner": "replay_20260906",
  "plan": "../plans/AR-0878.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Qualify immutable TLA+ tool provenance through an authoritative publication or deterministic source build.",
  "task_revision": 57,
  "title": "Qualify immutable TLA tool provenance",
  "updated_at": "2026-09-09T03:08:02+00:00",
  "worktree_key": "agent-systems-benchmark-tla-source-build-provenance"
}
---
## AR-0878

Resolve AR-0877's mutable and disappearing upstream release-asset blocker without accepting an
unsupported digest override. Qualify either a durable authoritative publication or a deterministic
source-build boundary whose output can safely seed AR-0877's verified online/offline cache.

Implementation has not started. Read the linked plan before claiming.


- 2026-09-09T02:09:49+00:00: AR-0003, AR-0901, and AR-0902 are durably done. AR-0878 provenance-only
  paths are disjoint from active AR-0806 TUI history and AR-0872 workflow documentation, and AR-0877
  is released open with its four-path prototype preserved. Promote the dependency-free provenance
  repair to resolve the exact mutable-upstream blocker.

- 2026-09-09T02:09:52+00:00: Claimed by replay_20260906.

- 2026-09-09T02:10:21+00:00: Recorded command exit 0; command argv SHA-256
  87591628a4708da948baeca8de57baa3f6a9e497f59362495507839baa5db451.

- 2026-09-09T02:17:02+00:00: Recorded command exit 0; command argv SHA-256
  d08d8411b19e92c040e2cd567daf71d855e13bade075081b5dac56e26d89843a.

- 2026-09-09T02:17:23+00:00: Recorded command exit 0; command argv SHA-256
  4219e4c199150d62da6cf2c66417e42ee4b33de347f0ad2d3729feda716b4992.

- 2026-09-09T02:18:01+00:00: Recorded command exit 0; command argv SHA-256
  55472ab8ad1b582a14fea8d6a164d5db57451bedb3ef23690b5bd97ea4fd768b.

- 2026-09-09T02:18:55+00:00: Recorded command exit 0; command argv SHA-256
  a72c152b345720bf774b58f0a195c9dc83dab2bb1d2a78a8ed69f89822171fc6.

- 2026-09-09T02:20:14+00:00: Recorded command exit 0; command argv SHA-256
  150fe69cdca956b1b20a2ca8c9b9d6e31bea9755873725f9740129b4eaf6f46f.

- 2026-09-09T02:20:52+00:00: Recorded command exit 0; command argv SHA-256
  b79a493ea700e09d46a52b65f082263d1605fae38a3802b431bdc1932d2fcba3.

- 2026-09-09T02:21:29+00:00: Recorded command exit 1; command argv SHA-256
  f937ab5ad620fc6f0614050a586923f21e03553389c78cf7a66b5c303fb7c799.

- 2026-09-09T02:22:32+00:00: Recorded command exit 1; command argv SHA-256
  515806539c16c0ef6421d399b33ad7f0bc5336b0369903a9a111f6e7a9974266.

- 2026-09-09T02:24:03+00:00: Recorded command exit 0; command argv SHA-256
  96889fa9d117224643400da2786044efd66f83596de6e36ae517a105097e47d3.

- 2026-09-09T02:25:16+00:00: Recorded command exit 0; command argv SHA-256
  ba71dce786adebc752b7e3f3aceec7ecd0d2165c3c16ef0cddff88b3a67ae50a.

- 2026-09-09T02:26:07+00:00: Substantive AR-0878 source-build checkpoint; worktree remains clean at
  af9fb7d. The upstream v1.8.0 prerelease is still actively mutable: release 25926686 moved again to
  published_at 2026-09-09T01:53:46Z and asset 551753628 (4490679 bytes, digest a1fc0bfe), so
  immutable-publication branch remains rejected. Exact source archive for b123b226 is 82989507
  bytes/SHA-256 1f96ee7ef950e456794d13b7e4d8123c345a91528257a3a41b7cc1b506d1b58f. Apache Ant 1.10.15
  archive is 6925830 bytes/SHA-256 71334d7e.../published SHA-512 d78427af.... Source includes 31
  vendored JAR inputs. Pinned eclipse-temurin 17.0.20+8 amd64 manifest is sha256:c0d1549d.... Docker
  pull failed before any build with permission denied on /var/run/docker.sock, an
  environment/authorization boundary. A host-only Ubuntu OpenJDK 17.0.20+8 diagnostic built twice
  from independent source trees: raw JARs had equal 4471000-byte size but different hashes; every
  non-directory ZIP entry name and payload was byte-identical. Canonical sorted ZIP repack with
  fixed epoch/mode produced byte-identical 4455492-byte outputs, SHA-256
  0bd598f74102f5c16632fe7dfa2f36b3763479f4757b15fff24a77f6f7268d7e. This proves nondeterminism is
  packaging metadata on this host only, not yet the pinned-container or license-complete acceptance.

- 2026-09-09T02:28:03+00:00: Recorded command exit 0; command argv SHA-256
  2249014c054951d12fa6688e53009f03bed6545243f3ab5b9a7279e8a3d71dd5.

- 2026-09-09T02:28:35+00:00: Recorded command exit 0; command argv SHA-256
  78d53a7aeaa71f22e09d4de3ab6ce37c3c0582db575c286e1210c0db8111edc2.

- 2026-09-09T02:29:12+00:00: Recorded command exit 0; command argv SHA-256
  57b5948513e458d336eda6c0ccc2de5802532235802b60a70c126f3065e98223.

- 2026-09-09T02:29:33+00:00: Recorded command exit 0; command argv SHA-256
  f9c0abf54fcf084921c0f968c000e03b810f9b12f059f7ff554f4a3b1e791803.

- 2026-09-09T02:30:46+00:00: Recorded command exit 1; command argv SHA-256
  529051b2403fc94253b55fa6ba044ff9740e26687b6b302392d554b5b9435c14.

- 2026-09-09T02:32:24+00:00: Recorded command exit 1; command argv SHA-256
  9c33f3b68768d118564eb273c3ec4899a2cb09ba499abc52f271f53b73e2de20.

- 2026-09-09T02:35:59+00:00: Recorded command exit 0; command argv SHA-256
  bd18d9fbab29c5c5b1606d7805df6dcd5a6d1961aea3bf1110243780ccd3be70.

- 2026-09-09T02:36:53+00:00: Recorded command exit 1; command argv SHA-256
  d4ffdadb97617cb3609a61176c46a10e2b46ea320d77ca0fe2ca9d10a240852c.

- 2026-09-09T02:37:48+00:00: Recorded command exit 1; command argv SHA-256
  b1c4baa42c8388a49a5bcab01b0f35f6a32dcabcaed35ec0d4bab5dff5a787c4.

- 2026-09-09T02:38:45+00:00: Recorded command exit 0; command argv SHA-256
  70220b6a8dec4b9485d46244365fee4a74dd7e46906570a02aede74d47fab297.

- 2026-09-09T02:40:15+00:00: Authorized pinned-container acceptance is green. Two independent builds
  ran as non-root inside eclipse-temurin amd64 child manifest
  sha256:c0d1549d1e0f5fa5b83622ec0033b00456107e0b1d0cfcce4c1d831532ce621e with --network none,
  --read-only root, tmpfs /tmp, fixed environment/build metadata, and Apache Ant 1.10.15. Raw
  4,470,998-byte JAR hashes differed (be367230... vs 858e9cfe...) only in packaging metadata;
  extracted 2,087-file trees and sorted file-name lists matched. Pinned JDK jar repack with no
  generated manifest and fixed ZIP time 1980-01-01T00:00:02Z produced byte-identical 4,512,486-byte
  artifacts twice, exact SHA-256 8c200a88d151c6c183c8dbc57a6b633d135e7a2b18242a3afbf243a9e4b68d3e.
  Persistent runner receipts are under .asb-local/ar0878-source-build. Recursive audit confirms
  exactly 31 vendored JARs; each path and SHA-256 has been enumerated against upstream
  vendored-jars.json, with license receipt mapping still required before qualification.

- 2026-09-09T02:47:42+00:00: Recorded command exit 0; command argv SHA-256
  3b0faf535309807c677283bcfb6eef3537d6d1e422727739f2edc89db8b2059d.

- 2026-09-09T02:48:08+00:00: Encoded the complete 31-JAR dependency and license-receipt closure in
  formal/tla-provenance/source-build.toml. Every recursively vendored JAR now has a unique sorted
  source-relative path, exact SHA-256, immutable Maven coordinate or upstream origin,
  runtime/development scope, SPDX expression, and license evidence locator inside the pinned source
  tree or JAR. Added offline build.sh binding the exact source/Ant digests and sizes, pinned
  linux/amd64 Temurin image, non-root/network-none/read-only container, fixed environment/build
  metadata, exclusive output lock, private scratch/cleanup, deterministic JDK repack, verification,
  and create-new publication. Added verify.sh with closed-schema/count/path/digest/license checks
  and safe output ZIP topology/timestamp/size/hash enforcement. Manifest-only verifier and git diff
  --check pass. This is a dirty pre-candidate checkpoint; adversarial fixtures/tests and full gates
  remain.

- 2026-09-09T02:48:32+00:00: Recorded command exit 0; command argv SHA-256
  5683852dbe93f9c75d5f5521ac6c297f774d4c90908fc4d126242b8cd6c2946e.

- 2026-09-09T02:50:31+00:00: Recorded command exit 127; command argv SHA-256
  9827b7e693874e74c7d40ec2ff20ef3037d3586b772f09e22494ba274b0abb90.

- 2026-09-09T02:51:40+00:00: Recorded command exit 0; command argv SHA-256
  c564c25845f3356f66313b640491e4232d035d94a4d960960f553eac88a2d103.

- 2026-09-09T02:51:59+00:00: Recorded command exit 127; command argv SHA-256
  4c4ec74ac673f3062b02bbe77a64f23f1e09deea4d6f5e0ad77a8f8e7adc63fb.

- 2026-09-09T02:53:17+00:00: Recorded command exit 0; command argv SHA-256
  dae8ea9ab58fc0e135a247d280ddba09782324ae23a9550af4a6a58fb380d698.

- 2026-09-09T02:53:55+00:00: Recorded command exit 1; command argv SHA-256
  691da153c8bc17be76511c79d83c117912fc958f79181ce46e65ed47851809e7.

- 2026-09-09T02:54:22+00:00: Recorded command exit 0; command argv SHA-256
  df89abc62d6f99a8cb1eb532fbcc9b7589501f9c9bec8fa1398776e82afeae7f.

- 2026-09-09T02:55:12+00:00: Recorded command exit 0; command argv SHA-256
  710327ada795009fed24385d89399ee4fcd5593217aad14e8762040d5a4d4182.

- 2026-09-09T02:55:39+00:00: Final implementation checkpoint: all eight owned paths are now present.
  Full persistent-source/output verification passes the exact 31-JAR closure and 2,087-entry
  artifact. Fixture-driven Rust suite passes 3/3, including fourteen independent
  provenance/schema/source/container/network/environment/timestamp/dependency/license/output
  mutations. The deterministic build script itself reproduced exact SHA-256 8c200a88... and
  4,512,486 bytes. TLC with that source-built JAR completed Recovery.tla with no error (10,289
  generated/3,709 distinct states), while RecoveryStaleMutation failed with exact StaleEventsFenced
  violation. Real concurrent publication returned fail-closed exit 75; real process-group
  cancellation returned 130 and left no output, partial, lock, or scratch effect. The first focused
  attempt was operator-only PATH exit 127; corrected pinned Cargo passed. A later TLC exit 1 was an
  operator-only subshell path error; corrected absolute model paths passed. ShellCheck is not
  installed on this host and was durably classified exit 127; remaining
  quality/formal/privacy/supply gates are not yet complete.

- 2026-09-09T02:56:17+00:00: Recorded command exit 101; command argv SHA-256
  c2706c3e401862177b7598b104e060528a6e3f8053893bf472082322c14427b7.

- 2026-09-09T02:57:00+00:00: Recorded command exit 0; command argv SHA-256
  0b642e27207d9dc2d846dc487248097b399af96384baec0668b47a082056854d.

- 2026-09-09T02:57:35+00:00: Recorded command exit 0; command argv SHA-256
  db2c8cacaabc20b176f591b53e8511505b9f8c05b472203e43e1fae63e6734df.

- 2026-09-09T02:58:21+00:00: Recorded command exit 1; command argv SHA-256
  563224d4ff9eae90414a4f48f2c20d1c02b414fec3fd38dadce94aca16870501.

- 2026-09-09T02:59:01+00:00: Recorded command exit 100; command argv SHA-256
  717140db4bd0aafa847e09b7a5daa2841ecd2f8abd936ed60b45753464b4f699.

- 2026-09-09T02:59:27+00:00: Recorded command exit 1; command argv SHA-256
  07d4438883f0465ee1c4c97d37e6fd6f5c5f1f692004f33d4dd848641906a376.

- 2026-09-09T03:00:01+00:00: Recorded command exit 0; command argv SHA-256
  16934318b17035cac4f72d2cdb5fe9474588a84d6ed4c29f2fc2009aa1875cee.

- 2026-09-09T03:01:24+00:00: Recorded command exit 0; command argv SHA-256
  55d986014cb245cd7d728aae07aade644c6cfeacfa372feebd1ff8066f9f3b18.

- 2026-09-09T03:02:36+00:00: Recorded command exit 73; command argv SHA-256
  113f09ea74e4c140947d0fc11ffaa6177527c15f9224e474193010247959cf96.

- 2026-09-09T03:02:59+00:00: Recorded command exit 101; command argv SHA-256
  ecf153dea899c0c1e7d37356494e9b94355ed167ec83ad8bc3b3a1ecb76a1543.

- 2026-09-09T03:03:21+00:00: Recorded command exit 1; command argv SHA-256
  167756735e392d22e1fbe4f2b564b3eb9466e1a37200bd48d9da33b5553344af.

- 2026-09-09T03:04:00+00:00: Recorded command exit 0; command argv SHA-256
  a492f9beb4cb5a7902b87a355d576dca2154822230353753a93941cfbd5d909b.

- 2026-09-09T03:04:23+00:00: Recorded command exit 0; command argv SHA-256
  f9abc6e3422e3c0d6c3f381c91f73e1d7d240494af8ea85397477d2204c94700.

- 2026-09-09T03:05:13+00:00: Recorded command exit 1; command argv SHA-256
  57722f2972b6ad69f0e91b8b4a5a0504f89021a1eadc17320240861fe6794362.

- 2026-09-09T03:06:17+00:00: Recorded command exit 1; command argv SHA-256
  1ad3a663e8e432b129b40226b8283d0eec02c0582bca43bfda22261e3d64ad6c.

- 2026-09-09T03:07:38+00:00: Recorded command exit 0; command argv SHA-256
  56fa48a2c04eea022a0f0d13d0b0317a649a19b08c247e7e7247da06479bf0a2.

- 2026-09-09T03:08:02+00:00: Recorded command exit 0; command argv SHA-256
  9a6e35508bddbdbf89ae3740f816b84a5627337d9360e24cb3da0d60e61d3ed0.
