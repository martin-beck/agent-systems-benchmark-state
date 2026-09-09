---
{
  "branch": "feature/tla-source-build-provenance",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-09T07:15:50+00:00",
  "depends_on": [
    "AR-0003",
    "AR-0901",
    "AR-0902"
  ],
  "id": "AR-0878",
  "next_action": "Request fresh independent immutable review of signed candidate 7ae562dbb15a686f3e1ef304de0fd5dfbeb0613b, tree ee763d09fba2119c88f3e6b30a22e8f8d3c570d3, parent 905607b8f57b1d3248c16a565443d39e5245af7c, base 096dc4f275c05ad81772f443b6f22dddfb92da3d. Do not publish or merge before review; hosted exact-head Kani remains required after publication authorization.",
  "observed_branch": "feature/tla-source-build-provenance",
  "observed_dirty": 0,
  "observed_head": "7ae562dbb15a686f3e1ef304de0fd5dfbeb0613b",
  "owner": "replay_20260906",
  "plan": "../plans/AR-0878.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Qualify immutable TLA+ tool provenance through an authoritative publication or deterministic source build.",
  "task_revision": 229,
  "title": "Qualify immutable TLA tool provenance",
  "updated_at": "2026-09-09T06:41:48+00:00",
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

- 2026-09-09T03:08:44+00:00: Recorded command exit 0; command argv SHA-256
  8316e8eeb39dfe6a7718362423fcb1bd937541316752ab59ea2336bf360fdc91.

- 2026-09-09T03:09:18+00:00: Signed+DCO candidate is c6aed713080c40ff24ec095cb83a1af4ff74d59e, tree
  99b8faaf9cf3c7445bc11ae34bdc4ea56adabbfe, parent af9fb7dcaabc162b13d6ee1e77d8915b6d82df20;
  worktree clean and exact eight owned paths/696 insertions. Full workspace tests and locked formal
  suite pass; source-built TLC positive/stale negative and pinned Alloy positive/mutations pass;
  mutation sentinels found/caught 7/7; fmt, repository policy, Gitleaks, cargo-deny/audit, exact
  build/verify, concurrency/cancel, and authorized Ubuntu-digest ShellCheck 0.9.0 pass. Focused
  llvm-cov ran all three tests but reports zero instrumentable Rust regions because the production
  boundary is shell/Python; no coverage percentage is claimed. Workspace Clippy fails only on six
  inherited formal/src/recovery.rs field_reassign_with_default findings outside this eight-path
  diff. Local Kani remains the previously proven incomplete-install environment boundary: cargo-kani
  0.67.0 internally resolves an absent default Kani-home cargo and fails before proofs; hosted
  exact-head formal Kani remains required. Fresh fetch shows origin/main 9aad1317, six commits
  beyond candidate parent with zero changed-path overlap, so candidate is not publishable until an
  authorized controlled rebase.

- 2026-09-09T03:19:50+00:00: Recorded command exit 0; command argv SHA-256
  8dd7a398b1e7449ac828a2e1cc3e6a9e1a784137bf3acb7edc42c3cbb9a3d42f.

- 2026-09-09T03:20:50+00:00: Recorded command exit 1; command argv SHA-256
  29e64c14e02a8cdfddf14bf78f92cdabaa7c6dc9f85dfa62ef54549b80854b8d.

- 2026-09-09T03:21:30+00:00: Recorded command exit 0; command argv SHA-256
  07defd429630db81f448098573cae4d400a8df06aaa6c78d4cbfcc2ed3ad05d4.

- 2026-09-09T03:22:13+00:00: Recorded command exit 0; command argv SHA-256
  5d866a4be8eef4b69dffee5eded8ad5e7e8ad2c6feb4d169bcd4661ec646ef7e.

- 2026-09-09T03:22:32+00:00: Recorded command exit 1; command argv SHA-256
  30baf84094ca88bee494de17d65c41dcc081dc8f7a1788d864fd49b41042c1d7.

- 2026-09-09T03:22:55+00:00: Recorded command exit 0; command argv SHA-256
  16934318b17035cac4f72d2cdb5fe9474588a84d6ed4c29f2fc2009aa1875cee.

- 2026-09-09T03:23:30+00:00: Controlled rebase complete. Preserved old candidate c6aed713 under
  evidence/ar-0878-c6aed713; initial rebased ff4e88e had exact equals range-diff. Exact-range
  repository policy then found the new shell scripts lacked the mandatory adjacent Huawei copyright
  line, a real metadata-only candidate issue missed while files were untracked. Added only those two
  header lines and signed/DCO-amended to 6cbd169f6ba6a1f1db95ea7b254ba2fdb4c5351b, tree
  747081681880e1221433a7fd7853ecf8b96cf1fc, exact parent 9aad1317bdcaabcec2e62a856ff6d0b3ac757f46.
  Scope remains the same eight owned paths/698 lines. Post-rebase full workspace and locked formal
  suites pass; exact focused tests 3/3, mutation sentinels 7/7, exact-range policy, Gitleaks,
  diff-check, SSH signature/DCO, and digest-pinned Ubuntu ShellCheck 0.9.0 pass. The grouped
  post-rebase wrapper stopped only at the policy header finding after full tests/formal had passed;
  later wrong /srv/data/data path was an operator-only pre-execution ShellCheck retry failure and
  the corrected exact command passed. Prior source-built TLC/Alloy, deterministic repeats,
  concurrency/cancel, supply, and honest zero-instrumentable-Rust coverage evidence transfer because
  the semantic patch is identical except mandatory comments. Local Kani remains the recorded
  incomplete-install boundary; hosted exact-head Kani is required.

- 2026-09-09T03:31:35+00:00: Recorded command exit 0; command argv SHA-256
  29bf36144e3069ba5a2340df225a452967c40ea4d7062a2e39cde34ef29cd1c0.

- 2026-09-09T03:35:28+00:00: Recorded command exit 0; command argv SHA-256
  182a8d8915dfad69c448f31523231d1c631ffd7643fefedaf39724f7b6e1cd02.

- 2026-09-09T03:35:47+00:00: Recorded command exit 1; command argv SHA-256
  32ec445295bc348aca8262e5c46b6f71e28bb641ef724f34c9c56b703c94f737.

- 2026-09-09T03:36:20+00:00: Recorded command exit 0; command argv SHA-256
  32ec445295bc348aca8262e5c46b6f71e28bb641ef724f34c9c56b703c94f737.

- 2026-09-09T03:36:57+00:00: Recorded command exit 0; command argv SHA-256
  bd1c4d24fe50644e20cde0b6594cbfac380154dd9bb392b21714add6b852a724.

- 2026-09-09T03:37:16+00:00: Recorded command exit 0; command argv SHA-256
  c5a6193643e57a4c22f4071474f000fde190a30eda9e433ea6239d603be67d08.

- 2026-09-09T03:38:46+00:00: Recorded command exit 0; command argv SHA-256
  7baf2f06c865026dc087ddd098a82d450601e3d68e96a4715dc77c917d69de98.

- 2026-09-09T03:39:31+00:00: License review block repaired in signed/DCO candidate
  c157cedc744373ef75aba686c00e97ce61aa3bfc/tree 8a86ce5c4cef3d879a156596cbdae64d2a116899/parent
  9aad1317bdcaabcec2e62a856ff6d0b3ac757f46. Every one of 31 JAR mappings now points to a
  SHA-256-bound actual license text, never pom.properties or manifest-only metadata; verifier binds
  the allowed SPDX-to-text path/digest map and rejects substituted/non-license evidence. Manifest
  additionally binds Ant LICENSE+NOTICE and three Temurin JDK plus four exact container-tool legal
  receipts; build verifies their bytes inside the exact archives/digest-pinned image before
  compilation. Added wrong-license-digest, non-license, missing-JDK-receipt and wrong-Ant-license
  negatives. Corrected one real docker stdin bug (--interactive required for receipt checksum
  stream); actual offline build then reproduced exact 8c200a88... output and full 31-JAR
  verification. Exact candidate full workspace/formal, focused 3/3, mutation 7/7, exact-range
  policy, ShellCheck, Gitleaks, cargo-deny/audit and clean-tree gates pass. Current origin/main
  advanced to 7d9191c via two TUI-only AR-0819 commits, with no overlap, so publication remains
  blocked on authorized rebase.

- 2026-09-09T03:48:25+00:00: Independent license review remains blocked after a bounded
  authoritative-history audit. Exact TLA+ commit 69396292697edceb0ac5d4696a772fe8e9f01652 binds
  jpf.jar and jpf-classes.jar to upstream jpf-core commit 0916082fac91405e11ec7ce55f9068ce84d61aaa,
  whose Apache-2.0 text is available. Exact TLA+ commit 3117a6daa561a9ff16acc167e1337c45adec7cb4
  introduced jpf-shell.jar and jpf-visual.jar; its message identifies only
  https://bitbucket.org/qiyitang71/jpf-visual and says issue 48 was manually fixed in
  jpf-visual.jar, without an upstream source revision. The Bitbucket repository is no longer
  anonymously retrievable; neither JAR contains LICENSE, NOTICE, POM, or coordinate metadata. Their
  exact Git blob identities remain 5da542e93f1b135d74e19b1cf53683da3dccf106 and
  2fa0b7fcb560be4936b9129a15279837a9501a60, but those prove bytes, not applicable terms/source
  provenance. Therefore the required closed 31-JAR package-specific license applicability cannot
  currently be proven. Candidate c157cedc remains clean and unchanged; its generic same-SPDX reuse
  is not accepted evidence.

- 2026-09-09T03:54:32+00:00: Recorded command exit 1; command argv SHA-256
  68df855a7c2e6b145d72439f1790de4cb86accd19a20e354769c722bf4ab3f8f.

- 2026-09-09T03:55:25+00:00: Recorded command exit 0; command argv SHA-256
  d90e481d71d4794fd3e482241c7ab451d895211a17febc671b8844536419c355.

- 2026-09-09T03:56:28+00:00: Recorded command exit 0; command argv SHA-256
  01cb79b80aa89c35c0e967b7c71f23d1eae6d9ce583ee21548709b08e90f96fd.

- 2026-09-09T03:57:53+00:00: Authoritative archive research narrows the prior blocker. Software
  Heritage origin qiyitang71/jpf-visual preserves revision
  swh:1:rev:8aeba829ca1e2c672a40aea6b42a3c54421677dd and directory
  swh:1:dir:86a5e46e13e2bdd6b35269107391d769cae24039, including package-specific Apache-2.0 text
  SHA-256 cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30. Origin sbadame/jpf-shell
  preserves revision swh:1:rev:1f2dba3499b3e009227bec5a7209f6d47cf959eb and directory
  swh:1:dir:b2c97e85b42cd74a7b5b9194a8ca669319c72e73, including actual NOSA-1.3-JPF text SHA-256
  e98e5fa95e37dcbac4013f36be94966172c181321bee5ac863e6405d10e58eeb; therefore c157cedc's Apache-2.0
  assertion for jpf-shell is false. The archived shell source has only 28 main classes while the
  exact vendored jar has 73, so it still cannot bind that binary to source. Two controlled
  pinned-container experiments establish a safe alternative boundary: deleting all five JPF jars,
  then deleting all 17 non-read jars while retaining exactly 14 direct compile/dist inputs, both
  reproduce exact normalized output SHA-256
  8c200a88d151c6c183c8dbc57a6b633d135e7a2b18242a3afbf243a9e4b68d3e byte-for-byte. The first
  experiment's exit 1 was operator-only Docker permission; corrected sudo -n Docker passed. This
  proves the opaque JPF artifacts are source-tree inventory, not build inputs, and supports an
  honest 14-input license closure rather than a false 31-input claim.

- 2026-09-09T04:05:02+00:00: Recorded command exit 2; command argv SHA-256
  5279f62b2a4f75953378efdc0d20dadcae713ce5381b07fb73f36e6c44898191.

- 2026-09-09T04:05:37+00:00: Recorded command exit 0; command argv SHA-256
  04ee6eed5c63ecbaa87e0d6b417092491172ce70597d6daee441ac5e6d20e94f.

- 2026-09-09T04:07:38+00:00: Recorded command exit 0; command argv SHA-256
  66c99363c28cc4d5d3566800e5e02af6eb2f799e1ae320d4144dc77787723d68.

- 2026-09-09T04:08:50+00:00: Recorded command exit 0; command argv SHA-256
  e6480ff0f0fc77f6c105ad99ed470be1b58bab2156635a00ef7a6eff0e6e0788.

- 2026-09-09T04:09:42+00:00: Recorded command exit 2; command argv SHA-256
  48458d4adcbc2714c4ae60f17ec39d916357031118af6e75d9a5cd826c73f20e.

- 2026-09-09T04:26:38+00:00: Recorded command exit 0; command argv SHA-256
  d6fe5301cfc7253ec28f4d4a3e0e434915d67f67dcc8514f0386b6aa872cdfd2.

- 2026-09-09T04:32:42+00:00: Recorded command exit 127; command argv SHA-256
  ab134fa089aad9a67eea7f54ce8b0d425c6a6aa07677d887a02693b7d78373b2.

- 2026-09-09T04:33:30+00:00: Recorded command exit 101; command argv SHA-256
  e3a17e0bafdd39c865484e0af3bd22c1017a73cd94bb9d38bb995d9d67d58430.

- 2026-09-09T04:34:12+00:00: Recorded command exit 0; command argv SHA-256
  86091f5b890ef4d6f94cb9d699b66d786285f3f601f526ece6877026fc564b9d.

- 2026-09-09T04:35:19+00:00: Recorded command exit 65; command argv SHA-256
  6572b87d6bc22d535312b3a5ef28e3cfb8f4f5fd8bf54523c5770e1020dd15cc.

- 2026-09-09T04:36:35+00:00: Heartbeat by replay_20260906.

- 2026-09-09T04:37:04+00:00: Implemented closed 31 = 14 build_input + 17 excluded_source_artifact
  manifest/verifier, pre-Ant pruning, exact post-prune allowlist, two-run build, retained deletion
  loop, runtime and manifest negatives, and honest docs. Focused Rust suite passed 4/4. End-to-end
  cache build exited 65 at the second retained trial: gson deletion failed compilation as expected,
  but jacocoant.jar deletion built the exact reviewed output, triggering retained input is not
  necessary. This is a product-contract contradiction, not environment/operator failure; no
  candidate created.

- 2026-09-09T04:40:18+00:00: Recorded command exit 1; command argv SHA-256
  cbe022e5c3f013b84c394dfe804c6596f8671cff44942620035ae8aee7d3d630.

- 2026-09-09T04:41:54+00:00: Recorded command exit 0; command argv SHA-256
  e668f8120ad133cc2e5850590d9430fb99b118abe84273d33320c6c7638a3f1d.

- 2026-09-09T04:43:03+00:00: Recorded command exit 101; command argv SHA-256
  cfc691a912cd99a5301ce28982a3849eb861ffee04b16c7245caa08be5891b4b.

- 2026-09-09T04:44:26+00:00: Recorded command exit 0; command argv SHA-256
  1c8cd4d65b8540ccc6dcb35cf877494e5461fb69549469d72d7da69e3c7615d5.

- 2026-09-09T04:45:54+00:00: Recorded command exit 0; command argv SHA-256
  a66a62b83470bccd5098b0615939e0a7575353877cd1fdcc33f160ef63569e42.

- 2026-09-09T04:47:21+00:00: Recorded command exit 127; command argv SHA-256
  8f887c4bf4d1fa6c28235aa50e7031726b2efe7c98b3e89b1051e4c838a32c55.

- 2026-09-09T04:47:52+00:00: Recorded command exit 101; command argv SHA-256
  34d3cbc452d89973a7a3f9387b905ac6efb0946ac62c2e99850ef2e381961225.

- 2026-09-09T04:48:45+00:00: Recorded command exit 0; command argv SHA-256
  1d1285a21283a36dcca24a20f4ae83bbe6f23c0dacd8bca677fd12b4aad5650a.

- 2026-09-09T04:49:29+00:00: Recorded command exit 0; command argv SHA-256
  a0ac1e65c8c02a923a45c600945d1cafb67efc80e67e0852ff27ccc272b16ef1.

- 2026-09-09T04:50:55+00:00: Recorded command exit 1; command argv SHA-256
  8e80ec2f811fa41b71ac7d6c12b2a36f50108383236e8fa893de32405e5f92a8.

- 2026-09-09T04:51:51+00:00: Recorded command exit 100; command argv SHA-256
  95042ec9b916ea5437f372cc24127f2ae834f8848aa0e098b99d7e4ec574efa1.

- 2026-09-09T04:52:34+00:00: Recorded command exit 126; command argv SHA-256
  812c4a11311985c49aca4e5caae2e81b0542bb44952d56cd48146d1279dd9a49.

- 2026-09-09T04:53:31+00:00: Recorded command exit 126; command argv SHA-256
  812c4a11311985c49aca4e5caae2e81b0542bb44952d56cd48146d1279dd9a49.

- 2026-09-09T04:54:12+00:00: Recorded command exit 0; command argv SHA-256
  7175ee3e85621f920a5cbb4b5cacd6a15727720c5a8edd2c0f5640cc63dab2af.

- 2026-09-09T04:54:31+00:00: Recorded command exit 0; command argv SHA-256
  09b9667d50d128ce6da6bc203f61889132cb8eb2487595e7cdf727972093281d.

- 2026-09-09T04:54:42+00:00: Recorded command exit 0; command argv SHA-256
  f94377735c803f0960b44fcfee8e506440ed8021bbc1da556f200ceb5196c564.

- 2026-09-09T04:55:37+00:00: Recorded command exit 101; command argv SHA-256
  5a0a67ed07b6be15561965679b82f980ae61203cc748b953cbea7b4ec68cb037.

- 2026-09-09T04:55:50+00:00: Recorded command exit 0; command argv SHA-256
  3dde0b791c892483191b92b9e43e24001e0b95fb87a10dc2a9c4236e0e3eef06.

- 2026-09-09T04:56:31+00:00: Recorded command exit 0; command argv SHA-256
  7c3f4ce14d1986098c9ed4d9272330d6f49fb1adc2b3a616989403b29c457e4d.

- 2026-09-09T04:57:28+00:00: Recorded command exit 2; command argv SHA-256
  dc2ab7cbce84067d10b31c1096a026e34de4fa270fd00b99474be93a43bf81af.

- 2026-09-09T04:58:07+00:00: Recorded command exit 0; command argv SHA-256
  cc49951de09262970d65eee03d5f6822d863274ffa6f415c348e81ce76d873e5.

- 2026-09-09T04:59:33+00:00: Recorded command exit 0; command argv SHA-256
  4aa668b4aa7ee3c739cb0c6d1a4c46ce59aee0e4442e9d2810f4437c839d5607.

- 2026-09-09T05:01:01+00:00: Recorded command exit 0; command argv SHA-256
  7b38df1989727a96ab6023a373517caaacc421a72f1317eb9ce320713be8381e.

- 2026-09-09T05:01:25+00:00: Recorded command exit 0; command argv SHA-256
  315d8237244eef17e75c8076a3728b7d3ef72066bea84ef95ebef25985e96946.

- 2026-09-09T05:02:00+00:00: Recorded command exit 0; command argv SHA-256
  07af3ac8781a9da0f77faa253852cb1af8ab02574b62dfed752295ca4a71ef75.

- 2026-09-09T05:02:51+00:00: Completed corrected fail-closed 31=13 build_input+18
  excluded_source_artifact repair. Exact pinned final campaign validates all 31, prunes all 18
  before Ant, validates 13 survivors, individually deletes each retained input and observes build
  failure, then performs two independent offline builds with identical 4,512,486-byte SHA256
  8c200a88d151c6c183c8dbc57a6b633d135e7a2b18242a3afbf243a9e4b68d3e outputs. Excluded entries are
  path/hash/classification only; jpf-shell and jacoco are reintroduction negatives; jpf-shell
  license license applicability remains unknown/unclaimed. Exact candidate gates: focused 4/4; full
  workspace fmt/Clippy/tests/docs/release green on Rust 1.93.0; locked formal tests green;
  source-built TLC positive and stale negative plus Alloy positive/mutants green; mutation 7/7; real
  concurrency/cancel cleanup green; digest-pinned Ubuntu ShellCheck 0.9.0 green; cargo-deny/audit,
  actionlint/zizmor, scoped Gitleaks, Ruff, exact-range policy/DCO/signature/diff-check clean.
  Focused llvm-cov executes 4/4 but has zero instrumentable Rust regions because production is
  shell/Python. Formal all-target Clippy retains inherited recovery.rs field_reassign_with_default
  findings outside this 11-path diff; local Kani remains the documented incomplete-install boundary.

- 2026-09-09T05:06:59+00:00: Recorded command exit 0; command argv SHA-256
  2aa4b670b0dc6247260797a1ba7351f1ce072c5268eb88bd8640f662fe1e25be.

- 2026-09-09T05:15:50+00:00: Heartbeat by replay_20260906.

- 2026-09-09T05:16:01+00:00: Recorded command exit 1; command argv SHA-256
  8f1743ebd4aa1c9a08314f294e654761544fb6b4fd92ff48db789472d69f43c1.

- 2026-09-09T05:16:33+00:00: Recorded command exit 101; command argv SHA-256
  8af45e69b8658c77028aa578406bc006d4395ac06d635c1e83c8032e37b42d58.

- 2026-09-09T05:16:54+00:00: Recorded command exit 0; command argv SHA-256
  4673b44c285fc472005605e12c0dbe80bd7ca6571f1dee42489945c8e0151359.

- 2026-09-09T05:18:17+00:00: Recorded command exit 0; command argv SHA-256
  79d526b9861d6d872bbfd4836a448b951aca5dea301a867e8d8248bce8c44630.

- 2026-09-09T05:19:01+00:00: Recorded command exit 0; command argv SHA-256
  2d406d36ac0ba6690bf449d04d23f79d1ac830427bb2a17cd39ec3922ddef482.

- 2026-09-09T05:20:52+00:00: Recorded command exit 0; command argv SHA-256
  74d4aca4f47df89d00746f272032c7446bc4a1f1e6677b3ed44427e7132cd11d.

- 2026-09-09T05:21:37+00:00: Recorded command exit 0; command argv SHA-256
  75455666038ecca2d9d1fb5e19d5071d62bc7f9abdfb86f61fb08250935727c4.

- 2026-09-09T05:23:13+00:00: Recorded command exit 0; command argv SHA-256
  dea64e254205026b1b139240b4e096824c33f4965333ccf6b7824d2f847bbb5d.

- 2026-09-09T05:23:31+00:00: Recorded command exit 0; command argv SHA-256
  7f4d66072c1d9f714d4380b71d17261f2adf65010f3ab7998eb223da6b77765a.

- 2026-09-09T05:24:20+00:00: Recorded command exit 0; command argv SHA-256
  0550dac451dfa2c1b360da5e38127629c0bbae7057f73fc114f08affa4fb8a87.

- 2026-09-09T05:24:54+00:00: Recorded command exit 0; command argv SHA-256
  97560a1c65f030173a360d6208d241fc40c2983bbe68669d20d6d79c70852bd8.

- 2026-09-09T05:26:11+00:00: Recorded command exit 1; command argv SHA-256
  13eedb842e2f8522a2f9bb0dbb4af3f5517a6179557062e30adb3ef9bfb786a6.

- 2026-09-09T05:26:36+00:00: Recorded command exit 100; command argv SHA-256
  6ff7d3321b4270f2a1e542af35111458895821d124dfbb644d86efb74cf44669.

- 2026-09-09T05:27:02+00:00: Recorded command exit 126; command argv SHA-256
  2db37ed4c8a0ac7b6d77a97afd43e462b390161ad8f8503459fa81205470da44.

- 2026-09-09T05:27:37+00:00: Recorded command exit 0; command argv SHA-256
  7b319e3a7e339242797a18d282e6be4da33b85f31b7b6013cbf2a57f56e8e2e7.

- 2026-09-09T05:28:19+00:00: Recorded command exit 0; command argv SHA-256
  9b14985c1203c67931ab36489811b6790f593848bcfa9bb5ce45bd74b74b6a2a.

- 2026-09-09T05:28:50+00:00: Recorded command exit 0; command argv SHA-256
  699b115957de62ea73e0b797275ee5236b50137416b468e5db7e3654228d23fc.

- 2026-09-09T05:30:59+00:00: Recorded command exit 0; command argv SHA-256
  e8f0ac4cb4bb1979b0fe81157c19e59f4fa2bb49bfbb45d7488f18942cd1419b.

- 2026-09-09T05:32:31+00:00: Recorded command exit 0; command argv SHA-256
  4fd647dfe40870f63ec985659e7279c2aaf9ee314933daadfe0e0ce659fb54e7.

- 2026-09-09T05:33:10+00:00: Recorded command exit 0; command argv SHA-256
  c848dee716d793b13bdadb822d77d65ccd57e7b4ad79ab619ea8ff1fcc9c0f2d.

- 2026-09-09T05:33:52+00:00: Recorded command exit 0; command argv SHA-256
  783b6ba3ed26dda30ce44034d1287b6969b95043505c1432b739456d3d748902.

- 2026-09-09T05:34:46+00:00: Recorded command exit 0; command argv SHA-256
  fbcee77f954457682798e3bf3763badb10970db48f1036945884826d7ab64b8a.

- 2026-09-09T05:35:14+00:00: Recorded command exit 0; command argv SHA-256
  ea5cde9519609a542cfece79a516bc2e2785ff8b4fe54c1e954935307742d001.

- 2026-09-09T05:36:10+00:00: Recorded command exit 0; command argv SHA-256
  7692ae8bbfb95c9bdd2f9192a9000ca2c697e2139500341c8ec0dd97e7521392.

- 2026-09-09T05:36:43+00:00: Recorded command exit 0; command argv SHA-256
  51d85908efdb1f6a6eaaa32cee6d96c35d4f2435218bce356a26a4b2a2e19de7.

- 2026-09-09T05:38:28+00:00: Review-block repair complete. Signed state commits
  ba4e7de0b4aa92409e31eea33948ecb2eebc36dd and b40d8e4dac82ed303430287dfeb7595b4320776a amend the
  owned-path fence from eight to the exact 11-path candidate scope. Corrected intermediate identity
  is 6e83e0893a0e64f2e529deae17147216eaf3cf17/tree b0c805783b616d3e748797c3228dbde40b88ec85/parent
  e4730653b112d733fb2a1157f65481663c4e073c. Final signed/DCO successor
  bcbdfe03e77d815467cb4341e0b9c1abef05f48b/tree 2b52b379968d2e37344f42c5416e7020c548d138 names the
  JavaCC per-line normalization exactly. JavaCC release_40@368da687 archive SHA256
  712420087c0ae91fd221062f0407a47e7abf6478b5ce24b40c7eda509910d27f and prettier4j v0.3.2@48a56fca
  archive SHA256 9f7bf63096ed8974b64b5489886e11831b962768f78ab5844da347d665ff75bd are bound-bound
  with raw license and applicability digests; all provenance-field mutation negatives fail closed.
  Exact candidate gates green: focused 4/4; 13 retained deletion trials; two offline builds
  identical at 4,512,486 bytes/SHA256
  8c200a88d151c6c183c8dbc57a6b633d135e7a2b18242a3afbf243a9e4b68d3e; workspace
  fmt/Clippy/tests/docs/release; locked formal; source-built TLC positive/stale negative and Alloy
  positive/mutants; mutation ubel

- 2026-09-09T05:39:07+00:00: Correction to the immediately preceding truncated checkpoint: the two
  external source receipts are exactly bound, and the fault gate was mutation sentinels 7/7 caught.
  Remaining exact-tree evidence is green: lock-contention exit 75 and cancellation exit 130 with no
  output/partial/lock residue; ShellCheck 0.9.0 on unchanged build and verifier script blobs;
  focused llvm-cov executes 4/4 with zero instrumentable Rust regions because production is
  shell/Python; repository policy over c157cedc..bcbdfe03; Ruff; actionlint; offline pedantic
  zizmor; scoped Gitleaks with no leaks; cargo-deny and cargo-audit. Final immutable audit verifies
  clean 11-path tree, diff-check, DCO and allowed SSH signatures for all three package commits.
  Local Kani remains the previously documented incomplete-install boundary; hosted exact-head Kani
  is required after publication authorization. Candidate for fresh review is
  bcbdfe03e77d815467cb4341e0b9c1abef05f48bb, tree 2b52b379968d2e37344f42c5416e7020c548d138, parent
  6e83e0893a0e64f2e529deae17147216eaf3cf17, package base c157cedc744373ef75aba686c00e97ce61aa3bfc.

- 2026-09-09T05:39:31+00:00: Identity correction: the final review candidate is exactly commit
  bcbdfe03e77d815467cb4341e0b9c1abef05f48b, tree 2b52b379968d2e37344f42c5416e7020c548d138, parent
  6e83e0893a0e64f2e529deae17147216eaf3cf17. This supersedes the extra-character candidate typo in
  the preceding prose note; frontmatter observed_head and next_action already contain the correct
  exact object. The prior intermediate repair is exactly 6e83e0893a0e64f2e529deae17147216eaf3cf17,
  tree b0c805783b616d3e748797c3228dbde40b88ec85, parent e4730653b112d733fb2a1157f65481663c4e073c.

- 2026-09-09T05:43:30+00:00: Recorded command exit 1; command argv SHA-256
  6ce5d23848ef4086bedd4104e51d5f5b70914fb9182aa682b89968ee26eb2cb9.

- 2026-09-09T05:44:30+00:00: Recorded command exit 1; command argv SHA-256
  a8a48ea515356afdb3e0a63df15017a771ff924331b1a690996b00cf67baff2f.

- 2026-09-09T05:45:08+00:00: Recorded command exit 0; command argv SHA-256
  49b0c3e8d45f97b944ba4ca05a43a44f45cee7b07ca924237fe3fe34c6f17da1.

- 2026-09-09T05:46:16+00:00: Recorded command exit 0; command argv SHA-256
  71a6569208a4d305f5e0ca5966bd477f9daeb3d87510fbcebcca673803e3e0da.

- 2026-09-09T05:48:02+00:00: Recorded command exit 0; command argv SHA-256
  6416fd9c4722423e393769ff954c45d2caa3635d32dc0c9890595d12dbf13347.

- 2026-09-09T05:48:35+00:00: Recorded command exit 2; command argv SHA-256
  ee3a2d2de3b23b5b8c9750993ac494e97ebec98d078da67e87b6115ca9fd4b1c.

- 2026-09-09T05:49:17+00:00: Recorded command exit 0; command argv SHA-256
  9be3dba6cfc43d1a8cc9e74547b13ef026430b80fc84579537cdce5f273e7083.

- 2026-09-09T05:49:41+00:00: Recorded command exit 1; command argv SHA-256
  e11c82f3e9f5c9186c851a7a9f0ece1ea33d95808b0b961e37ffa4d46018e4aa.

- 2026-09-09T05:50:57+00:00: Recorded command exit 1; command argv SHA-256
  cbc01ba0e29b86d71cd1600465f4b0d829aff7e9c095f906f45d66c5090e954c.

- 2026-09-09T05:51:22+00:00: Recorded command exit 0; command argv SHA-256
  6069da84853856863582065cd9bbd767974240c7c43bd69fff84ae802f1e3bcb.

- 2026-09-09T05:51:58+00:00: Recorded command exit 127; command argv SHA-256
  75ab5f46b22f5bff837c044cfc650259ce1b3bc4b114bc69be864ed2c40b4501.

- 2026-09-09T05:52:27+00:00: Recorded command exit 101; command argv SHA-256
  4953c778c4aaf4f072984e60ae8c6ee0a4a6cfb1e588d1b2d9c6f0bed85abf25.

- 2026-09-09T05:53:30+00:00: Recorded command exit 0; command argv SHA-256
  4235c71576608e8f082905fee3cbe3f950e84619a03f3055f0a0e962ea85ab45.

- 2026-09-09T05:54:09+00:00: Recorded command exit 1; command argv SHA-256
  08a19c7dcd3b36897ac9fe2c48757a382d4578a7586ebfcc4f274b49fcf241bc.

- 2026-09-09T05:54:30+00:00: Recorded command exit 0; command argv SHA-256
  e7d9629a69fe3dd1b39548ce08cf0e8f6567bf270e6e7bda1e1d46eea68e859d.

- 2026-09-09T05:54:57+00:00: Recorded command exit 0; command argv SHA-256
  a1b057d70b98186d40474c0d1f1eee65e094d2f7333833dc13a276c09236021a.

- 2026-09-09T05:55:26+00:00: Recorded command exit 0; command argv SHA-256
  699b115957de62ea73e0b797275ee5236b50137416b468e5db7e3654228d23fc.

- 2026-09-09T05:55:59+00:00: Recorded command exit 0; command argv SHA-256
  3118c7e04e02a8af8ee497bf78e7da28445b828f1328aa427e4aafbc79d27da4.

- 2026-09-09T05:56:36+00:00: Recorded command exit 0; command argv SHA-256
  81a8d7c9dc9081a7ac7185b0af604626fadcd74ceb2f9d93cf74e6420938b851.

- 2026-09-09T05:56:52+00:00: Recorded command exit 125; command argv SHA-256
  de6e0935b2fd95e89f09f2180fd1dabe1a4fe9c3e8a12d0300f3c6047d640740.

- 2026-09-09T05:57:31+00:00: Recorded command exit 0; command argv SHA-256
  7b319e3a7e339242797a18d282e6be4da33b85f31b7b6013cbf2a57f56e8e2e7.

- 2026-09-09T05:58:58+00:00: Controlled rebase completed onto live origin/main
  ecdfae42d5768fc5bc74ea6e3f4d45d8bceb96ff. backup/ar0878-bcbdfe03 preserves the approved original.
  Rebased range is 3e22529ba08a910e973c2c5db517ffc9de088def,
  717258f6cd53646ec846576c89fab98cb0efbc2d, 4bd2bd95c9273a19f50ffeae81a04605bc6956d1,
  962e8f510947aa7c97bbeb7c31789f5ce156d4b4. Range-diff is four exact equals; final diff remains the
  authorized 11 paths.

- 2026-09-09T06:00:26+00:00: Correction: exact tree is be4eb3371df02744040b9773e17f5890073d18bd. All
  post-rebase gates are green; local Kani remains unavailable and hosted exact-head Kani is required
  after publication.

- 2026-09-09T06:01:16+00:00: Corrected next_action to exact Git object identities after prior
  malformed base text.

- 2026-09-09T06:10:38+00:00: Recorded command exit 0; command argv SHA-256
  faf50d3c983e0dea07cfe3f32fdbd37faf85cc4abf7c5aec6efe96f6cbbe05eb.

- 2026-09-09T06:11:24+00:00: Recorded command exit 101; command argv SHA-256
  24d5a660c0ab3f3c6937ed76ac54bd34c490f8f2df89d482e7341acb59e93a4c.

- 2026-09-09T06:11:51+00:00: Recorded command exit 0; command argv SHA-256
  e8e194dddc614d8ea09843aa6d06065e6a1e0e832d485aae5aa29c76af11d0ea.

- 2026-09-09T06:12:40+00:00: Recorded command exit 0; command argv SHA-256
  89255255c88d1492dc1fb1083a13ee2d26cecb408028084e5ca2ca694ed2fca9.

- 2026-09-09T06:13:25+00:00: Recorded command exit 0; command argv SHA-256
  f1c9a0a4c1c1cbee6dd796f21d0a2b6f451e2da52d50403329e83e68dfb9f22a.

- 2026-09-09T06:13:44+00:00: Recorded command exit 1; command argv SHA-256
  a6819da40e1fdb8aa00ec748932887d16fe8bba474ed9ac497b32abca8ca0764.

- 2026-09-09T06:15:16+00:00: Recorded command exit 0; command argv SHA-256
  24565bed33c53549903e06a5c44e4aa155ce509095e83d68ba91ca3e677cd65b.

- 2026-09-09T06:16:03+00:00: Recorded command exit 0; command argv SHA-256
  2489c49411b8a3322c6b09b09acf981036f8bf4832e471402bea3af928706796.

- 2026-09-09T06:17:16+00:00: Recorded command exit 0; command argv SHA-256
  2ccd59f6b280ae439ad28ba3e3c0cd45de01cd702539523c4ebb8e24eb22d3cc.

- 2026-09-09T06:17:49+00:00: Recorded command exit 0; command argv SHA-256
  28ea9a874eb3b56f1f48e816eb47b5a31f63cb0b08863e98adaaae4b3a5b802e.

- 2026-09-09T06:18:08+00:00: Recorded command exit 0; command argv SHA-256
  740d4d1400a80c377e52768d15733e79ac80cf0203646f584928c8ac5dcc0a27.

- 2026-09-09T06:18:44+00:00: Recorded command exit 0; command argv SHA-256
  7b319e3a7e339242797a18d282e6be4da33b85f31b7b6013cbf2a57f56e8e2e7.

- 2026-09-09T06:19:08+00:00: Recorded command exit 0; command argv SHA-256
  763179e6930ada862784e2e00feff1aa1571299fd421609a0830421b0744f141.

- 2026-09-09T06:19:57+00:00: Controlled rebase onto live ca6e75916a8c9831b9107377cd48d731463c272a is
  complete. Range 660610b5ff5be76930ad9355bc909b16a5e51fb0,
  66e510454ed4d3a5f909c890c9c2e726f1f8d3f6, 38c729425309b3061ea361fbd349a961374bd64b,
  71d0f914d3b9b353dd7cde840538b5d5fdec2cab is four exact equals against the approved 962e8f5 package
  and remains exactly 11 authorized paths. Gates green: workspace fmt, Clippy, tests, docs, release;
  locked formal and focused 4/4; 13 deletion trials and exact dual offline output 4512486 bytes
  SHA256 8c200a88d151c6c183c8dbc57a6b633d135e7a2b18242a3afbf243a9e4b68d3e; TLC positive and stale
  negative; Alloy positive and mutants; mutation 7/7; contention and cancellation cleanup; policy,
  Ruff, ShellCheck 0.9.0, actionlint, zizmor, Gitleaks, cargo-deny, cargo-audit; signatures, DCO,
  diff-check, clean tree. llvm-cov executes 4/4 with zero instrumentable Rust regions; local Kani
  remains unavailable and hosted exact-head Kani is required after publication.

- 2026-09-09T06:22:38+00:00: Recorded command exit 0; command argv SHA-256
  bc4c4c53528716b4da4be0cd4c9f9f98155207b89f2dedd95c50629f9ffc0b57.

- 2026-09-09T06:23:52+00:00: Recorded command exit 0; command argv SHA-256
  04efe36de6a305d11dc5990aac653e0d37bebdd0869639c24d7b8b9f45b4ada6.

- 2026-09-09T06:25:28+00:00: Recorded command exit 0; command argv SHA-256
  5b93191f7c380a21b1684ba93cbf27806b33e512bbe14de260fc1e180d7fbfb6.

- 2026-09-09T06:26:09+00:00: Recorded command exit 0; command argv SHA-256
  ddd594781d3710780ac3e250a01ef28af8b3c55e4e0b660046740e69593350d6.

- 2026-09-09T06:26:57+00:00: Recorded command exit 0; command argv SHA-256
  4ede6a6f8cac1ebb7d8a31ab1524f03214bcc3f59e0391b7db17c9f2941671e5.

- 2026-09-09T06:27:39+00:00: Recorded command exit 0; command argv SHA-256
  6d413441dfc0deb2ce5aab5a814b4d45a5efb278d2976c9bca24d002bdb39294.

- 2026-09-09T06:28:08+00:00: Recorded command exit 0; command argv SHA-256
  740d4d1400a80c377e52768d15733e79ac80cf0203646f584928c8ac5dcc0a27.

- 2026-09-09T06:28:34+00:00: Recorded command exit 0; command argv SHA-256
  37cadf19f4b2d10f9f166fc9461cc9b38fa3203ebc094a345b60776a94fd0a0a.

- 2026-09-09T06:29:08+00:00: Recorded command exit 0; command argv SHA-256
  ddce4ccaba6421c205a7bf6eef798f2146e79b497633f8832974d143ae174cca.

- 2026-09-09T06:29:38+00:00: Controlled rebase onto live 096dc4f275c05ad81772f443b6f22dddfb92da3d
  complete. Exact signed DCO range: fd23184b9f4d6190552597e87e070ebf9c17fa3b,
  e8dfa4c11f57dd8480840b6f4472dfa268b3d8ae, 905607b8f57b1d3248c16a565443d39e5245af7c,
  7ae562dbb15a686f3e1ef304de0fd5dfbeb0613b. Range-diff is four exact equals and scope remains 11
  paths. Gates green: workspace fmt, Clippy, tests, docs, release; full locked formal and focused
  4/4; 13 deletion trials and dual offline output SHA256
  8c200a88d151c6c183c8dbc57a6b633d135e7a2b18242a3afbf243a9e4b68d3e; TLC positive/stale negative;
  Alloy positive/mutants; mutation 7/7; contention/cancel cleanup; policy, Ruff, ShellCheck 0.9.0,
  actionlint, zizmor, Gitleaks, cargo-deny/audit; signatures, DCO, diff-check, clean tree. llvm-cov
  runs 4/4 with zero instrumentable Rust regions; local Kani unavailable, hosted exact-head required
  after publication.

- 2026-09-09T06:32:06+00:00: Recorded command exit 0; command argv SHA-256
  bd6a824ecb8dc716b4145b31c8ffb7f019167750d07bace97961dab993648512.

- 2026-09-09T06:33:37+00:00: Recorded command exit 0; command argv SHA-256
  2342857581e619bdb074ec3e5fa7a86c9732a816d84c09f264eeaf11c4147aa5.

- 2026-09-09T06:39:36+00:00: Recorded command exit 0; command argv SHA-256
  cc9f689f11ed15728195d9876f9ddac5304c8db690633aec1d9523edb3bab862.

- 2026-09-09T06:41:48+00:00: Recorded command exit 0; command argv SHA-256
  7ae36de73e475b02f0b18eda056c4e8696c4d128a307cf892660cf3d17b268dc.
