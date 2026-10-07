---
{
  "branch": "repair/ar-1726-development-rustup-shim-permissions",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-08T01:30:07+00:00",
  "depends_on": [
    "AR-1634",
    "AR-1636",
    "AR-1637"
  ],
  "id": "AR-1726",
  "next_action": "Independent review PR #499 at exact head a3222ae105dcad1a1b8050289a3618c68e3920f8; repair findings, require hosted checks, then protected merge and exact paired post-merge lifecycle qualification.",
  "observed_branch": "repair/ar-1726-development-rustup-shim-permissions",
  "observed_dirty": 0,
  "observed_head": "a3222ae105dcad1a1b8050289a3618c68e3920f8",
  "owner": "codex-ar1726-security-review",
  "plan": "../plans/AR-1726-development-rustup-shim-permissions.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_ref": "specs/AR-1726.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Make development asb tui installation accept a conventional user-owned 0775 rustup shim path with an explicit warning while preserving hard stable and production trust boundaries.",
  "task_revision": 54,
  "title": "Allow user-owned group-writable rustup shim in development",
  "updated_at": "2026-10-07T23:30:45+00:00",
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
