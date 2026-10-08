---
{
  "branch": "repair/ar-1734-development-tui-tool-environment",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-08T04:45:40+00:00",
  "depends_on": [
    "AR-1726",
    "AR-1727"
  ],
  "id": "AR-1734",
  "next_action": "Integrate approved PR #502 with tools/integration/merge_pr.py against base 736a65cd8904b8f4a6f1715fc86ae1c854fe2232, head 40f618b9389c594c4274bc08195f93f3cd2dd547, tree e5c4645c9e4384fb57424eaa42139a99b78c5c69; then require exact-main CI and immutable post-merge evidence.",
  "observed_branch": "repair/ar-1734-development-tui-tool-environment",
  "observed_dirty": 0,
  "observed_head": "40f618b9389c594c4274bc08195f93f3cd2dd547",
  "owner": "codex-ar1734-pr502-integrate",
  "plan": "../plans/AR-1734-development-tui-tool-environment.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_ref": "specs/AR-1734.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Provide the installed development TUI a minimal validated tool environment without inheriting ambient PATH or weakening stable launch.",
  "task_revision": 77,
  "title": "Propagate validated development tools to installed TUI",
  "updated_at": "2026-10-08T02:45:40+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1734-development-tui-tool-environment"
}
---

AR-1713 proved that development bundle installation and status succeed, while
bare launch, dynamic catalog, and live-provider routes fail before provider
dispatch because ASB clears the standalone frontend environment without
reconstructing the bounded tool environment required by its preflight.

Repair the ASB development broker boundary only. Preserve `env_clear`, reuse
the exact validated development tools and descriptor-bound rustup selection,
and pass a minimal environment that cannot be redirected by an ambient PATH or
post-validation pathname swap. Development warnings remain nonblocking; stable
and production policy remains fail closed and unchanged.


- 2026-10-08T01:36:35+00:00: Claimed by codex-ar1734-planning.

- 2026-10-08T01:36:43+00:00: Recorded command exit 0; command argv SHA-256
  a0a5101c89c1881d8ddb910a6fd38534f58d1c35f702171439b1c42e63920303.

- 2026-10-08T01:37:20+00:00: Published detailed P0 dependency for the bounded validated tool
  environment required by installed ASB-TUI launch; ready for an isolated ASB implementation worker
  after current TUI review/repair capacity permits.

- 2026-10-08T01:41:07+00:00: Claimed by codex-ar1734-tool-environment.

- 2026-10-08T01:41:15+00:00: Recorded command exit 0; command argv SHA-256
  5345cd4b5f66285dc80cddfe59c0a95475263f9ff88d25d2639fce3c300aa4b9.

- 2026-10-08T01:41:47+00:00: Recorded command exit 0; command argv SHA-256
  a5118f9a2a9d79ac48d8faac3ac684782a5c24e73c2d9f509e3b43c2c10db367.

- 2026-10-08T01:47:59+00:00: Recorded command exit 0; command argv SHA-256
  462f99fb6c13a94edf35bcd2beffd9d7ab45129bbf1e6a663c89769c174d0be5.

- 2026-10-08T01:48:54+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-08T01:49:37+00:00: Recorded command exit 0; command argv SHA-256
  82fba3ffee0a29793f76427ab377e730473bc6fd33811ecdc0a51de40f76cd27.

- 2026-10-08T01:50:06+00:00: Recorded command exit 101; command argv SHA-256
  e39d977690fe97611b2341f71e9f6d8866cdb42b6a991dffbdc54b5b85b9a8a8.

- 2026-10-08T01:50:58+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-08T01:51:20+00:00: Recorded command exit 101; command argv SHA-256
  e39d977690fe97611b2341f71e9f6d8866cdb42b6a991dffbdc54b5b85b9a8a8.

- 2026-10-08T01:51:46+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-08T01:52:08+00:00: Recorded command exit 101; command argv SHA-256
  e2d38c280b8d8c46b7371c37ae0d25e6d25a007cb8c10c2b14a9989c33fda35f.

- 2026-10-08T01:52:34+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-08T01:53:07+00:00: Recorded command exit 101; command argv SHA-256
  e2d38c280b8d8c46b7371c37ae0d25e6d25a007cb8c10c2b14a9989c33fda35f.

- 2026-10-08T01:53:58+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-08T01:54:31+00:00: Recorded command exit 0; command argv SHA-256
  e2d38c280b8d8c46b7371c37ae0d25e6d25a007cb8c10c2b14a9989c33fda35f.

- 2026-10-08T01:56:47+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-10-08T01:57:26+00:00: Recorded command exit 101; command argv SHA-256
  2ddd222d5ab3dbbc5824e8367ff0d1151a6168041a569b52fb97c11e3c8515c1.

- 2026-10-08T01:57:56+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-10-08T01:58:28+00:00: Recorded command exit 0; command argv SHA-256
  2cd6e91752974ac59b48671237ddf930cad2e53bff9f153193c794b07e985545.

- 2026-10-08T01:59:25+00:00: Recorded command exit 0; command argv SHA-256
  95395ce61f1b783b8ea272706ba78c152183c6b4f42018c61c38fbc22692c0de.

- 2026-10-08T02:00:33+00:00: Recorded command exit 0; command argv SHA-256
  f2e590bbecafd942675030c8632cddabd4d88498a2a3e9a4e48bbf81f69aa4e3.

- 2026-10-08T02:01:17+00:00: Recorded command exit 0; command argv SHA-256
  95395ce61f1b783b8ea272706ba78c152183c6b4f42018c61c38fbc22692c0de.

- 2026-10-08T02:02:26+00:00: Recorded command exit 4; command argv SHA-256
  61e0bf2f1bd07b014e0770582eefe6d8deddc8e7c0271a513c36cb69bab4e0b0.

- 2026-10-08T02:03:19+00:00: Recorded command exit 0; command argv SHA-256
  dddf947698aee5c7251b09fe1bcf75337f5d16145d0143887d81ecb361bc8e99.

- 2026-10-08T02:04:06+00:00: Recorded command exit 1; command argv SHA-256
  2e6d8ddc1232121b3bc5fc13375c90ef4475eca14d86d9cdfd6c2c45169d31c1.

- 2026-10-08T02:04:41+00:00: Recorded command exit 0; command argv SHA-256
  3003ffad7a32a97d8164c80a3cbe79b8fb35cc4d05e8368f355f953afd824ac8.

- 2026-10-08T02:05:15+00:00: Recorded command exit 0; command argv SHA-256
  58f415d37d50ac31f03d42027dc7b759e4b6c435d34c29c5cff23cdff32b44d4.

- 2026-10-08T02:05:48+00:00: Recorded command exit 0; command argv SHA-256
  e9d8d42ec131d5783715cea087e35ac29160f37fe8aa491a600f6c6be152271c.

- 2026-10-08T02:06:51+00:00: Recorded command exit 101; command argv SHA-256
  534f8613e1c316db8f0f46dd989e44e14a8ca74304a94791b4e4a1c59b2fbb1d.

- 2026-10-08T02:07:50+00:00: Recorded command exit 0; command argv SHA-256
  ca1524eed79153b44e76d56a3f18d7e3048b2ef8a466cb7ccc5328e99fb4ed96.

- 2026-10-08T02:08:22+00:00: Recorded command exit 0; command argv SHA-256
  d04aa803a9fcb854b247572f9b417fd1935a57ca978bb887d2e7c188e99db043.

- 2026-10-08T02:08:53+00:00: Recorded command exit 0; command argv SHA-256
  7c730eec3ea71bd24ffc5a9255bf7f542481bf601dba6c72bed6e00f6c2fab3c.

- 2026-10-08T02:09:27+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-10-08T02:10:11+00:00: Recorded command exit 0; command argv SHA-256
  1024fc1e6cefa31b078f0b5d2ed85c7ea4586897b388bf1e308f62db58574461.

- 2026-10-08T02:10:45+00:00: Recorded command exit 0; command argv SHA-256
  8f020a8266d9eda8e0ed704996e99736ad1cf29c0294cefaaa456dc2d9fb4d92.

- 2026-10-08T02:11:52+00:00: Recorded command exit 0; command argv SHA-256
  b49a90ee600c1023cee9ee9f9e8a4f9a06c53eef8c48d3932d88e482126c7c01.

- 2026-10-08T02:13:21+00:00: Recorded command exit 0; command argv SHA-256
  7b80382008cb01e3ea6fa6e88054b624464f9801b40ed57f947b01892a686ae8.

- 2026-10-08T02:14:08+00:00: Recorded command exit 0; command argv SHA-256
  ca99b5a10295bded484eb593d2cee41502083c20fecd1bf8462bce5abbf3173e.

- 2026-10-08T02:14:37+00:00: Recorded command exit 0; command argv SHA-256
  81bd002ebb11cfbe4a75141d434969b10d94493c6bc41017bd204a12ded43fef.

- 2026-10-08T02:15:16+00:00: Recorded command exit 0; command argv SHA-256
  1c4aafd2e66e0c5ef7f4527dab971ff1286ec76cabc073ce635539aaaa70e25a.

- 2026-10-08T02:15:47+00:00: Recorded command exit 0; command argv SHA-256
  8b31c3873540a6e13ce47f6591580dfb79fc6de80d1341580dce263b04fab1d1.

- 2026-10-08T02:16:20+00:00: Recorded command exit 0; command argv SHA-256
  321c534968b9c456a64caf5e6d09b63780c507f97548057d2bfe31edcfd73ff4.

- 2026-10-08T02:16:49+00:00: Recorded command exit 0; command argv SHA-256
  2d11b4304f7137d5a02f7807548a99db1824772241b165b4225a47e37d8548b7.

- 2026-10-08T02:17:29+00:00: Recorded command exit 0; command argv SHA-256
  b4738512f2b646da3dfa81c9eb55e674a1c52556eabbe77c415503b5a23c69e1.

- 2026-10-08T02:18:10+00:00: Recorded command exit 0; command argv SHA-256
  21d18b9109ce235db3edafa363c8014481685d4546a17b93038a7e35d3d45db9.

- 2026-10-08T02:18:47+00:00: Implementation published for independent review in ASB PR #502 at
  signed+DCO head 40f618b9389c594c4274bc08195f93f3cd2dd547 (tree
  e5c4645c9e4384fb57424eaa42139a99b78c5c69). Local focused and CI-equivalent serial workspace gates,
  clippy, fmt, rustdoc, release build, repository policy, and scoped Gitleaks passed. Exact pinned
  installed TUI install/status/bare-launch/dynamic-catalog/provider-free boundary passed with
  network denied. Hosted CI is running; reviewer must verify exact-head checks and merge integrity.
  Development-only; no provider-backed live or public-release qualification. Do not merge without
  independent review.

- 2026-10-08T02:22:23+00:00: Claimed by codex-ar1734-pr502-review.

- 2026-10-08T02:22:32+00:00: Replaced stale implementation action with the exact immutable review,
  qualification, and hosted-CI action after reconciliation.

- 2026-10-08T02:22:49+00:00: Recorded command exit 0; command argv SHA-256
  2426d20ffa1ce8dbf2952be3358cc5b7d60d6011b4b0cd82ac02baf066d21cd6.

- 2026-10-08T02:23:19+00:00: Recorded command exit 0; command argv SHA-256
  4dc06e469823e4994a8ee826be2867ab8e97866de43dc7a7171cb464ea7c6157.

- 2026-10-08T02:25:30+00:00: Recorded command exit 0; command argv SHA-256
  3a15b46f601adff2fa1ee3c60c07c97e96549bea1f7850125b7efe24dd24bb2c.

- 2026-10-08T02:27:26+00:00: Recorded command exit 0; command argv SHA-256
  aea70530024a991886a7eecd46de5ece80befb3e6af12d80f5f16e2bc01bfd62.

- 2026-10-08T02:28:24+00:00: Recorded command exit 0; command argv SHA-256
  6ac799c7c49a1ae507079dfbbd69c3b7232b61cac92b7dc1af41f7b446ccf9fb.

- 2026-10-08T02:29:02+00:00: Recorded command exit 1; command argv SHA-256
  aae2166fb85952673258ebad6c2310b7059df81a5bcb742bf51f6d12ca29e8ea.

- 2026-10-08T02:29:58+00:00: Recorded command exit 1; command argv SHA-256
  6ebcea9f2d74d11c2b241d2662c6f29bd84807b2a4458719ae074a68e9b1af73.

- 2026-10-08T02:30:51+00:00: Recorded command exit 0; command argv SHA-256
  43ee1362cfdd92e63342aa7b60de4f8fa85719d081cbe38bba612653b0459071.

- 2026-10-08T02:31:29+00:00: Recorded command exit 1; command argv SHA-256
  84e8ff4a21c235042389b8081717646cd8303a4f53f7d0f32848386fc1ddf458.

- 2026-10-08T02:32:47+00:00: Recorded command exit 4; command argv SHA-256
  222f1d427c941b93b00dec9644d74301028b0bd6a53c5410f6947eb40a5b2e0d.

- 2026-10-08T02:33:22+00:00: Recorded command exit 141; command argv SHA-256
  ef11816994dbac2bed1f6000ad1b5f4bdf003b9ad709f2b4b6e3574753118781.

- 2026-10-08T02:33:58+00:00: Recorded command exit 0; command argv SHA-256
  caf5923f7fc061626c0958ea7399afe5e73d992f222b47a84dad9c55b3c51336.

- 2026-10-08T02:34:46+00:00: Recorded command exit 0; command argv SHA-256
  dcaa9223956780b28d312c6c05c079d7653f1f532ce1f69a0456687c7f85f49d.

- 2026-10-08T02:36:01+00:00: Recorded command exit 101; command argv SHA-256
  3e281a8e5621a7b6a79c7efb846eb1519cef0ec77bc8521b4c360346b9aaf3fa.

- 2026-10-08T02:36:39+00:00: Recorded command exit 0; command argv SHA-256
  615b0c4972372e5e25b0507f1d3be9401fdd115675afb2a57a369d965d40d314.

- 2026-10-08T02:37:49+00:00: Recorded command exit 101; command argv SHA-256
  190898007bbadeda1b49b9b72c2d8d999e14e43aced6533b92cf1c6cddc72cc9.

- 2026-10-08T02:38:23+00:00: Recorded command exit 101; command argv SHA-256
  c98aeed89f49d13d2291bd0b53f0da54b734a062c3eab68c03be4a85b973fd44.

- 2026-10-08T02:39:13+00:00: Recorded command exit 0; command argv SHA-256
  89d850e581e82af10cb6e40f943f55bab6850a8270f6e011410578f342bcd170.

- 2026-10-08T02:41:49+00:00: Recorded command exit 0; command argv SHA-256
  02645c0f521b0a3623dbef3330b23eebc8d4d62d29a7bb636912d4c1f81fb3c8.

- 2026-10-08T02:42:47+00:00: Recorded command exit 0; command argv SHA-256
  e4b5df171d0c2c09d9320e02030312931340d5033661b45bfab2ac190690934a.

- 2026-10-08T02:43:27+00:00: Independent technical approval: no actionable findings at exact
  signed+DCO head 40f618b9389c594c4274bc08195f93f3cd2dd547/tree
  e5c4645c9e4384fb57424eaa42139a99b78c5c69/base 736a65cd8904b8f4a6f1715fc86ae1c854fe2232. Audited
  env_clear retention, absent ambient PATH, development-only validated
  git/setsid/cc/ar/ld/rustup-home policy, same-toolchain descriptor-bound Cargo/Rustc, and CLOEXEC
  rollback/restoration on success and every error. Hostile replacement, symlink/missing tool,
  descriptor inheritance/leak, spawn/exit/descendant cleanup, and typed human/JSON tests pass. Exact
  pinned installed TUI install/status/bare PTY launch/dynamic-catalog/provider-free network-denied
  journeys pass. Serial locked workspace tests, fmt, clippy -D warnings, rustdoc -D warnings,
  release build, repository policy, diff check, and scoped Gitleaks pass locally. All 14 exact-head
  hosted checks are terminal success; PR is open and mergeable. Review only; no merge performed.
  Initial PROJECT_STATE discrepancy was only stale live-CI projection refreshed by reconcile, not
  product-head drift or another worker mutation.

- 2026-10-08T02:43:36+00:00: Released ownerless after independent technical approval. Next authority
  is the coordinator/integrator: use the repository merge_pr.py path with the recorded exact
  base/head/tree, do not substitute a hosted merge, and retain AR-1734 open until exact-main
  post-merge workflows and immutable merge evidence pass.

- 2026-10-08T02:45:40+00:00: Claimed by codex-ar1734-pr502-integrate.
