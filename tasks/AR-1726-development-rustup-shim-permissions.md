---
{
  "branch": "repair/ar-1726-development-rustup-shim-permissions",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-08T02:19:49+00:00",
  "depends_on": [
    "AR-1634",
    "AR-1636",
    "AR-1637"
  ],
  "id": "AR-1726",
  "next_action": "Repair PR #499 by deriving and opening rustc descriptor-relatively from the same retained selected toolchain/bin identity as Cargo without canonicalizing the mutable Cargo pathname; retain the deterministic cross-toolchain replacement regression, rerun exact gates, and obtain fresh independent review.",
  "observed_branch": "repair/ar-1726-development-rustup-shim-permissions",
  "observed_dirty": 1,
  "observed_head": "d9ef0bce9bf656f07b3a64f306ed65d6204177cb",
  "owner": "codex-ar1726-pr499-pairing-repair",
  "plan": "../plans/AR-1726-development-rustup-shim-permissions.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_ref": "specs/AR-1726.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Make development asb tui installation accept a conventional user-owned 0775 rustup shim path with an explicit warning while preserving hard stable and production trust boundaries.",
  "task_revision": 109,
  "title": "Allow user-owned group-writable rustup shim in development",
  "updated_at": "2026-10-08T00:40:16+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1726-development-rustup-shim-permissions"
}
---

This is a development-only compatibility repair. The current host has a regular,
current-user-owned Rust 1.93 Cargo/rustc toolchain beneath a conventional rustup
shim, while `~/.cargo` and `~/.cargo/bin` are mode 0775. The user explicitly
authorized that layout for development execution.

Accept only current-user-owned group-writable shim ancestors and surface a
development warning. World-writable, non-user-owned, symlinked-parent, escaping,
missing, malformed, or substituted paths remain hard failures. Stable and
production installation policy is unchanged.

Completion requires focused positive and hostile-path tests, exact paired
ASB/asb-tui install/status/bare-launch/upgrade/remove evidence, independent
review, protected merge, and terminal-green post-merge CI.

- 2026-10-07T22:37:38+00:00: Dependencies AR-1634, AR-1636, and AR-1637 are done. User authorized
  the bounded development-only 0775 rustup shim exception; promote implementation and paired
  qualification.

- 2026-10-07T22:42:10+00:00: Claimed by codex-ar1726-rustup.

- 2026-10-07T22:42:29+00:00: Recorded command exit 0; command argv SHA-256
  5345cd4b5f66285dc80cddfe59c0a95475263f9ff88d25d2639fce3c300aa4b9.

- 2026-10-07T22:42:54+00:00: Recorded command exit 0; command argv SHA-256
  ad5023ea3aab7e906a3bd6149245b11179886f084e63677dbcbd7ea34b00dfa9.

- 2026-10-07T22:45:02+00:00: Recorded command exit 1; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-10-07T22:45:34+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-07T22:46:07+00:00: Heartbeat by codex-ar1726-rustup.

- 2026-10-07T22:46:30+00:00: Recorded command exit 0; command argv SHA-256
  e104325b6323d4e30c2bd59bfcd21152fd18d5c5ae3d0de40a0ff7c3bc52b3e9.

- 2026-10-07T22:46:58+00:00: Recorded command exit 0; command argv SHA-256
  e104325b6323d4e30c2bd59bfcd21152fd18d5c5ae3d0de40a0ff7c3bc52b3e9.

- 2026-10-07T22:47:49+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-07T22:48:11+00:00: Recorded command exit 0; command argv SHA-256
  2de104f310725c13a0b36af497e338a982936597c2d69b986302f0e6383b2814.

- 2026-10-07T22:48:49+00:00: Recorded command exit 3; command argv SHA-256
  6967d705005b60fdd714abe0558f8e0327916639818c212fac5fa57b7c27c139.

- 2026-10-07T22:49:24+00:00: Recorded command exit 3; command argv SHA-256
  6967d705005b60fdd714abe0558f8e0327916639818c212fac5fa57b7c27c139.

- 2026-10-07T22:50:29+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-07T22:50:55+00:00: Recorded command exit 0; command argv SHA-256
  6967d705005b60fdd714abe0558f8e0327916639818c212fac5fa57b7c27c139.

- 2026-10-07T22:51:19+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-07T22:51:50+00:00: Recorded command exit 0; command argv SHA-256
  9f2517616c433918dfa824b636b17588a4e17c379654f0c68783b83e4e04c0f2.

- 2026-10-07T22:52:47+00:00: Recorded command exit 0; command argv SHA-256
  6967d705005b60fdd714abe0558f8e0327916639818c212fac5fa57b7c27c139.

- 2026-10-07T22:53:10+00:00: Recorded command exit 0; command argv SHA-256
  c69866e52db6308516456ef9de68995e3708c0b93436bc892714e53fd7a10be5.

- 2026-10-07T22:53:57+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-10-07T22:54:31+00:00: Recorded command exit 101; command argv SHA-256
  22fc19d872be75a975891ff0abd53f1c305974a409b50c49c5df5d842d033e81.

- 2026-10-07T22:55:01+00:00: Recorded command exit 101; command argv SHA-256
  22fc19d872be75a975891ff0abd53f1c305974a409b50c49c5df5d842d033e81.

- 2026-10-07T22:55:34+00:00: Recorded command exit 0; command argv SHA-256
  359d399dbe516e4a6c82de7a61b736b7d34fb7b6e8ffe552245ab234d396de60.

- 2026-10-07T22:57:24+00:00: Heartbeat by codex-ar1726-rustup.

- 2026-10-07T22:57:49+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-10-07T22:58:31+00:00: Recorded command exit 0; command argv SHA-256
  22fc19d872be75a975891ff0abd53f1c305974a409b50c49c5df5d842d033e81.

- 2026-10-07T22:59:42+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-07T23:00:09+00:00: Recorded command exit 0; command argv SHA-256
  9f2517616c433918dfa824b636b17588a4e17c379654f0c68783b83e4e04c0f2.

- 2026-10-07T23:00:45+00:00: Recorded command exit 0; command argv SHA-256
  eb8648d78be9d44db5631385c3fcbaaeaac0114989924fef6dc1415045ce0bfa.

- 2026-10-07T23:01:20+00:00: Recorded command exit 0; command argv SHA-256
  f18e072e46744378f76df3e77bc8d90904575c50688ba02c3e20406868458fc0.

- 2026-10-07T23:01:52+00:00: Recorded command exit 0; command argv SHA-256
  cc4e69dc1814d935830614eb4b186e826208ea83bed4a8b7edf2cd3d24ca692a.

- 2026-10-07T23:03:06+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-10-07T23:04:43+00:00: Recorded command exit 101; command argv SHA-256
  534f8613e1c316db8f0f46dd989e44e14a8ca74304a94791b4e4a1c59b2fbb1d.

- 2026-10-07T23:05:42+00:00: Recorded command exit 101; command argv SHA-256
  ea80ab75f67abc17ba8e38c5dd19501691dbc4fd67697c54523ad9f414c35508.

- 2026-10-07T23:08:03+00:00: Recorded command exit 0; command argv SHA-256
  c5ab1585746ccbc1d55e4b025bf3c4eaaf5a9b363f7f0a35459b6b94d1821fc2.

- 2026-10-07T23:10:19+00:00: Recorded command exit 3; command argv SHA-256
  08c6495c8f0aae52e023a74a98c328388d710851c0415746de9590654b4c21c7.

- 2026-10-07T23:11:24+00:00: Recorded command exit 0; command argv SHA-256
  9f2517616c433918dfa824b636b17588a4e17c379654f0c68783b83e4e04c0f2.

- 2026-10-07T23:12:05+00:00: Recorded command exit 0; command argv SHA-256
  08c6495c8f0aae52e023a74a98c328388d710851c0415746de9590654b4c21c7.

- 2026-10-07T23:12:40+00:00: Recorded command exit 0; command argv SHA-256
  ca99b5a10295bded484eb593d2cee41502083c20fecd1bf8462bce5abbf3173e.

- 2026-10-07T23:13:08+00:00: Recorded command exit 0; command argv SHA-256
  94060f205e325aacbbd2e1730c052f4f938370a5f35552f93b0bc6d18efc1595.

- 2026-10-07T23:13:44+00:00: Recorded command exit 0; command argv SHA-256
  4dee1dd1f5d49d0b0097a718ee35b2d71dacf27d71b4f1593bc577e5ffeeba42.

- 2026-10-07T23:15:52+00:00: Recorded command exit 0; command argv SHA-256
  ee1741888df0ec254dd681a0d0b13eea18a9d56c2671fba52cc75e9c64522c9d.

- 2026-10-07T23:16:29+00:00: Implemented and pushed signed DCO head
  a3222ae105dcad1a1b8050289a3618c68e3920f8 tree ca7cf753962ae05872ba4c9518a5fff09644c5ab; PR #499
  open. Focused rustup tests 8/8, exact-host release preflight human/JSON warning, fmt, workspace
  Clippy, rustdoc, release build, and asb-cli 228/228 passed. Full workspace had one unrelated
  parallel runtime scratch-root collision that passes isolated. Paired
  install/status/launch/upgrade/remove remains post-merge because source identity must equal remote
  main.

- 2026-10-07T23:16:41+00:00: PR #499 is open at signed DCO head
  a3222ae105dcad1a1b8050289a3618c68e3920f8 tree ca7cf753962ae05872ba4c9518a5fff09644c5ab. Exact-host
  release preflight and focused gates pass; hosted checks are running. Independent reviewer must
  bind findings/approval to this head, then merge only after required checks and run exact paired
  post-merge install/status/bare-launch/upgrade/remove qualification.

- 2026-10-07T23:30:07+00:00: Claimed by codex-ar1726-security-review.

- 2026-10-07T23:30:16+00:00: Recorded command exit 0; command argv SHA-256
  4d8372c3ac47fbacd54e192666127d47ce57f2e7ae8657874c9a5c411dc435a6.

- 2026-10-07T23:30:45+00:00: Recorded command exit 0; command argv SHA-256
  48be8e731b2e588ff6af9300621b922550debca87b6e7bb3bd046415b8a4154e.

- 2026-10-07T23:32:09+00:00: Reviewer execution ended before producing evidence because its task
  wording triggered an automated safety filter. Release the lease for a fresh independent
  correctness review; no product mutation or review conclusion was recorded.

- 2026-10-07T23:33:53+00:00: Claimed by codex-ar1726-pr499-correctness-review.

- 2026-10-07T23:35:05+00:00: Recorded command exit 101; command argv SHA-256
  f33b585651edce4e4935cd9a0c3697094b012ddd3ac85938863f97e98d7162a2.

- 2026-10-07T23:35:37+00:00: Independent exact-head review of
  a3222ae105dcad1a1b8050289a3618c68e3920f8 found a blocking P1 validation-to-execution substitution
  gap. validate_development_rustup_tool accepts group-write on selected toolchain directories and
  returns only a PathBuf; materialize_development later executes Cargo and exports rustc by pathname
  after remote discovery and checkout. A temporary deterministic regression resolved an accepted
  fixture, replaced Cargo at that pathname, then observed execution output substituted rather than
  validated. The temporary test was removed and the review worktree restored clean at tree
  ca7cf753962ae05872ba4c9518a5fff09644c5ab. The actual host compatibility need includes 0775
  user-owned Cargo shim and selected toolchain directories plus 0664 settings; current local primary
  group has no additional listed member, but the contract must not depend on mutable group
  membership. Stable code path remains unchanged; exact commit signature, author-matching DCO, diff
  check, and all 14 exact-head hosted checks passed.

- 2026-10-07T23:37:13+00:00: Recorded command exit 0; command argv SHA-256
  e8eb8a2c40fb4ab7b10c5645774f10c2d93c6f273d1cefd7e4ad3fe30b688606.

- 2026-10-07T23:38:28+00:00: Independent review completed against a3222ae/tree ca7cf7 and published
  as GitHub review 5449688892. Do not merge PR #499: repair the P1 Cargo/rustc
  validation-to-execution substitution gap with an object-bound execution design and retain a
  deterministic post-validation replacement regression. Existing exact-head CI, signature, DCO,
  stable boundary, and warning behavior are otherwise acceptable. Fresh independent review is
  required after the head changes.

- 2026-10-07T23:40:38+00:00: Claimed by codex-ar1726-pr499-repair.

- 2026-10-07T23:45:45+00:00: Recorded command exit 1; command argv SHA-256
  c3699fc1b8efb9be2369b056d9961b5f56728cd33639780a266f0a7014536608.

- 2026-10-07T23:46:20+00:00: Recorded command exit 0; command argv SHA-256
  c3699fc1b8efb9be2369b056d9961b5f56728cd33639780a266f0a7014536608.

- 2026-10-07T23:46:52+00:00: Recorded command exit 0; command argv SHA-256
  fbfc9b1298fa0cc672782bf58ebdb823d3528837409c813e0a6de8f260307281.

- 2026-10-07T23:47:22+00:00: Recorded command exit 0; command argv SHA-256
  9ebdf0ebe2890abef64856317c01fb14d053b80b09c9be3ac12bea6c0b40a0d8.

- 2026-10-07T23:49:17+00:00: Recorded command exit 101; command argv SHA-256
  b3f5e011e60ef5c71bfa91e4f8731ef42e7b810feada2a1609cb8929c8a8ce65.

- 2026-10-07T23:50:07+00:00: Recorded command exit 0; command argv SHA-256
  555ef4b5c4706176a50181b8a633290fd6e7f6a9add90115417805abf0845c17.

- 2026-10-07T23:50:45+00:00: Recorded command exit 0; command argv SHA-256
  b3f5e011e60ef5c71bfa91e4f8731ef42e7b810feada2a1609cb8929c8a8ce65.

- 2026-10-07T23:51:25+00:00: Recorded command exit 101; command argv SHA-256
  83cb7dd21a89596992d424b3fc922cf1f89ac1a53125794c1bec835aa0603cc9.

- 2026-10-07T23:51:57+00:00: Recorded command exit 0; command argv SHA-256
  83cb7dd21a89596992d424b3fc922cf1f89ac1a53125794c1bec835aa0603cc9.

- 2026-10-07T23:52:20+00:00: Recorded command exit 0; command argv SHA-256
  c3699fc1b8efb9be2369b056d9961b5f56728cd33639780a266f0a7014536608.

- 2026-10-07T23:52:43+00:00: Recorded command exit 127; command argv SHA-256
  e038b9eefcd2b4699d6c130ea5546e1c188581e190dd652f30790037ee74166e.

- 2026-10-07T23:53:19+00:00: Recorded command exit 0; command argv SHA-256
  782614372279e75602414c1493412e102d5c8cdb7102eb78a561db3e5e9bdca4.

- 2026-10-07T23:54:02+00:00: Recorded command exit 0; command argv SHA-256
  4b8a6cf66833777712f18d01fd32de2874c7e1bb087decc23b370918f2fe7732.

- 2026-10-07T23:55:10+00:00: Recorded command exit 0; command argv SHA-256
  a40e62f07f63c87895a897fbf40ed4e8b867358d9c01b20fbb8a96d24e9b85c9.

- 2026-10-07T23:55:59+00:00: Recorded command exit 101; command argv SHA-256
  203ae9db498ba4fc79567ad8964f839902c2c83dd6d84e5dc2549b995cc8c89e.

- 2026-10-07T23:56:32+00:00: Recorded command exit 0; command argv SHA-256
  61d94ff4a16c327b3cdafe4147958c72161ea3921e435b8643b855592645f87a.

- 2026-10-07T23:57:09+00:00: Recorded command exit 128; command argv SHA-256
  d9ea4f17a5824ab2595e847d7357491879d1ba04561ca24875e427f9bd72254d.

- 2026-10-07T23:57:41+00:00: Recorded command exit 0; command argv SHA-256
  7a699b37c9fe43db23f7bcd02f41bd87f94270f2c86e4cd012b4a641665ba8ca.

- 2026-10-07T23:58:17+00:00: Recorded command exit 0; command argv SHA-256
  44762267dc2da621b73866924fe89bb17488086f70d241e7b53ef5c22731b23e.

- 2026-10-07T23:58:57+00:00: Recorded command exit 0; command argv SHA-256
  68898b05008101e43c21167b962a52ea89aae5da2e3d8ff52752727f481b1bdc.

- 2026-10-07T23:59:30+00:00: Repaired PR #499 at signed+DCO head
  d9ef0bce9bf656f07b3a64f306ed65d6204177cb tree 3d15a55982be6ae04f64a9675603a12aacca5216.
  Descriptor-relative O_NOFOLLOW traversal retains exact Cargo/rustc objects and executes them
  through inherited descriptor handles; deterministic replacement, restoration, cleanup, and hostile
  symlink regressions pass. Full asb-cli 229 plus integrations, fmt, workspace Clippy, rustdoc,
  release build, and exact-host human/JSON preflight pass. Full workspace exposed only the known
  parallel runtime scratch collision, whose exact test passed isolated. Hosted exact-head checks are
  running; obtain fresh independent review, then merge only after terminal green.

- 2026-10-08T00:02:13+00:00: Claimed by codex-ar1726-pr499-rereview.

- 2026-10-08T00:02:42+00:00: Recorded command exit 0; command argv SHA-256
  8835ca6afa124b5f0cfd058e18f654c75cfea93cbe35cb3c57d7948687d35db1.

- 2026-10-08T00:06:21+00:00: Recorded command exit 0; command argv SHA-256
  20d3503a0070b89b5d7a10fc83d2db0b0ab3b75934e072199ae6a961496c2049.

- 2026-10-08T00:08:05+00:00: Recorded command exit 0; command argv SHA-256
  28df747baeaad0cf1ec9f6d363e04d887de618a806f27a497861406ea43e7869.

- 2026-10-08T00:08:44+00:00: Recorded command exit 0; command argv SHA-256
  b8397a49962d2f188ed40388f0db2e98b9b98aaa4d2f79d33759917da255c10c.

- 2026-10-08T00:12:05+00:00: Recorded command exit 0; command argv SHA-256
  2c7277796aa4bf3ca9a45480b3e85a7712c3ababd24c1a121a95f9f82ba412e3.

- 2026-10-08T00:15:12+00:00: Recorded command exit 0; command argv SHA-256
  023471af2a51b5a7dd71276d1a71ef9014072e396c6b87e142a58cbdd77d0d5b.

- 2026-10-08T00:15:47+00:00: Independent rereview of exact signed+DCO head
  d9ef0bce9bf656f07b3a64f306ed65d6204177cb tree 3d15a55982be6ae04f64a9675603a12aacca5216 found a
  blocking P1 Cargo/Rustc pairing race. After descriptor-binding selected Cargo A, a deterministic
  review-only regression replaced its accepted group-writable pathname with a symlink to Cargo B;
  production resolve_development_rustc_bound reopened that pathname by canonicalize, selected Rustc
  B, and pinned Cargo A executed Rustc B with output alternate-rustc. Temporary test removed;
  isolated review worktree restored clean. GitHub exact-head review PRR_kwDOUQSsRs8AAAABRNcp2g
  records repair guidance. All 14 hosted checks green, signatures/DCO/diff/privacy acceptable,
  stable remains strict, and independent actual-host human+JSON preflight passed with the bounded
  warning. Do not merge until repaired and freshly reviewed.

- 2026-10-08T00:15:59+00:00: Released for repair after exact-head independent review confirmed the
  cross-toolchain Cargo/Rustc pairing race. Preserve PR #499, repair the descriptor-relative
  same-toolchain binding, retain the reproduction, and require fresh exact-head review.

- 2026-10-08T00:17:59+00:00: Claimed by codex-ar1726-pr499-pairing-repair.

- 2026-10-08T00:19:49+00:00: Heartbeat by codex-ar1726-pr499-pairing-repair.

- 2026-10-08T00:19:52+00:00: Recorded command exit 2; command argv SHA-256
  48458d4adcbc2714c4ae60f17ec39d916357031118af6e75d9a5cd826c73f20e.

- 2026-10-08T00:23:19+00:00: Recorded command exit 0; command argv SHA-256
  0fe5c74e162fc6da0909febcf33f9d9ece5ff616b2846c31e00d4622dbd88286.

- 2026-10-08T00:28:52+00:00: Recorded command exit 0; command argv SHA-256
  c8795cc77ac09b3dfddc1448a1457a99a632ed200a0ab501c9f936210fc55257.

- 2026-10-08T00:29:27+00:00: Recorded command exit 0; command argv SHA-256
  79da272f7e4e7a786ca90e5ea99a1b051339fd1ac5cd8d61b67c8ebfbc695ad8.

- 2026-10-08T00:30:04+00:00: Recorded command exit 0; command argv SHA-256
  6783a82505fe9699124dfcb1739fdcd59547eea8dca4d229fb0abd07c27364e7.

- 2026-10-08T00:36:19+00:00: Recorded command exit 0; command argv SHA-256
  ccddac8fd2e77fa49c0709e2997277873753d5b1ea427d766e348f4e699badea.

- 2026-10-08T00:36:50+00:00: Recorded command exit 0; command argv SHA-256
  0f50b755977151fcac363d0652f91bcdc391b62a5b332583e13356809b0b347d.

- 2026-10-08T00:37:19+00:00: Recorded command exit 101; command argv SHA-256
  b3f5e011e60ef5c71bfa91e4f8731ef42e7b810feada2a1609cb8929c8a8ce65.

- 2026-10-08T00:37:58+00:00: Recorded command exit 0; command argv SHA-256
  67137831ca34b0f693c4589e43d6724811ca7b52d8732e2c132bd19e1e266659.

- 2026-10-08T00:38:31+00:00: Recorded command exit 1; command argv SHA-256
  c3699fc1b8efb9be2369b056d9961b5f56728cd33639780a266f0a7014536608.

- 2026-10-08T00:39:07+00:00: Recorded command exit 0; command argv SHA-256
  79da272f7e4e7a786ca90e5ea99a1b051339fd1ac5cd8d61b67c8ebfbc695ad8.

- 2026-10-08T00:39:39+00:00: Recorded command exit 0; command argv SHA-256
  2bddff813953cb70c9e51c289349b9977cce2e2917ae5aeee2b3729cde32c192.

- 2026-10-08T00:40:16+00:00: Recorded command exit 0; command argv SHA-256
  cb98a04a18d6a6ed2ecd5001e658f24a6b9c86a3e919d9cc89cb302820bd1a9f.
