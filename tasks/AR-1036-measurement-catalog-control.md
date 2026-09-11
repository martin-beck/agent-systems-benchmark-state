---
{
  "branch": "feature/measurement-catalog-control",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-11T03:39:48+00:00",
  "depends_on": [
    "AR-1013",
    "AR-1023"
  ],
  "id": "AR-1036",
  "next_action": "Open protected PR for approved exact head 95fa9dc55f2aedc8c7dba8cb1deab5f225b66782, require all exact-head checks, merge, and verify postmerge.",
  "observed_branch": "feature/measurement-catalog-control",
  "observed_dirty": 0,
  "observed_head": "8e8d37e8c7ca7a4f673e8ae84d7395d512d45197",
  "owner": "codex-root-ar1036-catalog-20260911",
  "plan": "../plans/AR-1036.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Expose the versioned ASB measurement catalog to standalone frontends without UI code.",
  "task_revision": 153,
  "title": "Publish the measurement catalog control contract",
  "updated_at": "2026-09-11T03:01:01+00:00",
  "worktree_key": "agent-systems-benchmark-measurement-catalog-control"
}
---
Implement only the bounded ASB control method, types, schema, backend dispatch, exact-version
advertisement and cross-repository fixtures required to retrieve the AR-1013 catalog. Preserve the
immutable 1.0 capability shape; exact 1.2 selection advertises catalog support. All search, grouping, selection,
rendering and help behavior remains exclusively in `martin-beck/asb-tui` under AR-1014.

- 2026-09-10T21:40:00+00:00: Clarified that cross-repository parser validation is read-only pinned
  consumer conformance; parser or frontend fixture changes belong only to standalone asb-tui ARs.

- 2026-09-11T01:39:45+00:00: Dependencies AR-1013 and AR-1023 are done; root approves the
  protocol-only plan and repository boundary.

- 2026-09-11T01:39:48+00:00: Claimed by codex-root-ar1036-catalog-20260911.

- 2026-09-11T01:40:15+00:00: Recorded command exit 0; command argv SHA-256
  ea153b531f1106f5d94913543b5962bf799305c4e35ed4d05dd3cd19dab1610a.

- 2026-09-11T01:42:58+00:00: Recorded command exit 101; command argv SHA-256
  02168a3f9e679202c03514861d51c419643a82f2d5e15349b0ef923a64b0b489.

- 2026-09-11T01:43:23+00:00: Recorded command exit 101; command argv SHA-256
  ba030ce5d94b6bba6e9ad15dbcab5e6ff607b17af41c5ea4fea1652868a54a5f.

- 2026-09-11T01:45:03+00:00: Recorded command exit 0; command argv SHA-256
  02168a3f9e679202c03514861d51c419643a82f2d5e15349b0ef923a64b0b489.

- 2026-09-11T01:45:23+00:00: Recorded command exit 0; command argv SHA-256
  0cf2915f4a267b5bd71189368ab134f456a244810ec78e29f957d23b8d35f0cf.

- 2026-09-11T01:46:59+00:00: Recorded command exit 0; command argv SHA-256
  0cf2915f4a267b5bd71189368ab134f456a244810ec78e29f957d23b8d35f0cf.

- 2026-09-11T01:48:17+00:00: Recorded command exit 0; command argv SHA-256
  6a3dffbd227f4bab0c2c58cce7f86b7c72a1be32a3cfabb404020872de59bd3a.

- 2026-09-11T01:49:11+00:00: Recorded command exit 0; command argv SHA-256
  2b01e6df558910928f77cab50be4efae19a20fa4b1838c77a25688947433157f.

- 2026-09-11T01:49:31+00:00: Recorded command exit 0; command argv SHA-256
  00a2dd7d07160d247713f7b5d4487ca8edc6c9d0870831f923f5fb123759f6d7.

- 2026-09-11T01:50:38+00:00: Recorded command exit 0; command argv SHA-256
  0cf2915f4a267b5bd71189368ab134f456a244810ec78e29f957d23b8d35f0cf.

- 2026-09-11T01:50:59+00:00: Recorded command exit 0; command argv SHA-256
  00a2dd7d07160d247713f7b5d4487ca8edc6c9d0870831f923f5fb123759f6d7.

- 2026-09-11T02:02:04+00:00: Recorded command exit 101; command argv SHA-256
  b22e56a69216f38bdad47ce064330cd61caab0372493799dcbf840ee4526eebd.

- 2026-09-11T02:02:44+00:00: Recorded command exit 101; command argv SHA-256
  b22e56a69216f38bdad47ce064330cd61caab0372493799dcbf840ee4526eebd.

- 2026-09-11T02:03:53+00:00: Recorded command exit 101; command argv SHA-256
  3db3f570dd188a5f7dc7854fec4d87800dc16e6f6440558b982969f1936bcab9.

- 2026-09-11T02:04:20+00:00: Recorded command exit 0; command argv SHA-256
  287e4e893ad270a06f805cce4da233661ff9edb5aaf0e9866fa8826863c1cb34.

- 2026-09-11T02:04:58+00:00: Recorded command exit 0; command argv SHA-256
  69c7444d737e529a648320e375ea513823ffb1b498c5cfd12227971dbc8f9fe0.

- 2026-09-11T02:05:14+00:00: Recorded command exit 0; command argv SHA-256
  49b2c755524a36344bffab6f41432a82a145092bade33d9008a9aa87b564339c.

- 2026-09-11T02:06:06+00:00: Recorded command exit 0; command argv SHA-256
  cbefea14a0e90659dc8f255e5900b002a1b56902b68720e9dc53ac4bf7c77fa4.

- 2026-09-11T02:07:38+00:00: Recorded command exit 1; command argv SHA-256
  d3c98b73457006c16d2af1b3fa0923f5a9501585006738919d618b03af9a14a8.

- 2026-09-11T02:08:07+00:00: Recorded command exit 0; command argv SHA-256
  5a142f89cd9284a2161fbd8e7233fa78a8b2273177c5139351e494de37b76d27.

- 2026-09-11T02:08:45+00:00: Recorded command exit 101; command argv SHA-256
  cbefea14a0e90659dc8f255e5900b002a1b56902b68720e9dc53ac4bf7c77fa4.

- 2026-09-11T02:09:10+00:00: Recorded command exit 0; command argv SHA-256
  7c11a933bf08539d8bd88e00e11fefa963442021d4e2af3a1c3492cf28b3e20c.

- 2026-09-11T02:10:10+00:00: Recorded command exit 1; command argv SHA-256
  867206790f33111679421a45e27f9b910cb92cc9e8400eb1d33fe1d5547c648a.

- 2026-09-11T02:10:34+00:00: Recorded command exit 0; command argv SHA-256
  cddcef2e64dad82530c0205f0347dac34cc840d7290c981556e565660ab29f6b.

- 2026-09-11T02:11:40+00:00: Recorded command exit 0; command argv SHA-256
  ec30ebe069578ad423c91ee8b0ffb2cb11db3f867a37a762f73f9a4b96f8e197.

- 2026-09-11T02:12:40+00:00: Recorded command exit 0; command argv SHA-256
  915a2df3d6cb8e8fa53a03e3fea248e46b55e78b6b4eebea49fca895d4590578.

- 2026-09-11T02:12:48+00:00: Recorded command exit 0; command argv SHA-256
  b97ea1d63b168226e0924f05a9d5453ae84e4839a684f5034a82abd347edb049.

- 2026-09-11T02:14:01+00:00: Recorded command exit 0; command argv SHA-256
  46c58e4018a568d6c8158b1cb5473361e3f8c51fc332f5ec7697bee035b7f150.

- 2026-09-11T02:14:14+00:00: Recorded command exit 0; command argv SHA-256
  4836a69533bb3ddfa6fe2d555166fdf63d3c6fb6d83e3b67fb52934125deece3.

- 2026-09-11T02:14:48+00:00: Recorded command exit 0; command argv SHA-256
  e9be9ec1ddde064efbc86ee7901e60b5757ff702e401ecfae8bf81c64e40220c.

- 2026-09-11T02:15:27+00:00: Recorded command exit 0; command argv SHA-256
  befa83057919fe49624c182b68bc0c4e789e0802905c589df649fe9533bca1fa.

- 2026-09-11T02:16:07+00:00: Recorded command exit 0; command argv SHA-256
  ee23364ebb556356850c68f0f2f7ed96e554929a1a78782511018825f2811c4d.

- 2026-09-11T02:17:05+00:00: Recorded command exit 0; command argv SHA-256
  21d62822f2a13e52ff09179fd6bc0f6100a3010e0f75387d92df524c2a8713bb.

- 2026-09-11T02:17:29+00:00: Recorded command exit 0; command argv SHA-256
  f1bf628fdf8fad5d14c4c711fc584c2adf25a976283ae200289ad2bab6ad12bf.

- 2026-09-11T02:18:07+00:00: Recorded command exit 0; command argv SHA-256
  7d975eacbeb7641c9b5fbedbe4097c805caf42fc5b87d6615ed9ad9b27cd8c73.

- 2026-09-11T02:19:07+00:00: Recorded command exit 0; command argv SHA-256
  cddcef2e64dad82530c0205f0347dac34cc840d7290c981556e565660ab29f6b.

- 2026-09-11T02:19:22+00:00: Recorded command exit 0; command argv SHA-256
  7c11a933bf08539d8bd88e00e11fefa963442021d4e2af3a1c3492cf28b3e20c.

- 2026-09-11T02:20:06+00:00: Recorded command exit 0; command argv SHA-256
  cddcef2e64dad82530c0205f0347dac34cc840d7290c981556e565660ab29f6b.

- 2026-09-11T02:20:17+00:00: Recorded command exit 101; command argv SHA-256
  cbefea14a0e90659dc8f255e5900b002a1b56902b68720e9dc53ac4bf7c77fa4.

- 2026-09-11T02:20:48+00:00: Recorded command exit 0; command argv SHA-256
  cddcef2e64dad82530c0205f0347dac34cc840d7290c981556e565660ab29f6b.

- 2026-09-11T02:20:56+00:00: Recorded command exit 0; command argv SHA-256
  cbefea14a0e90659dc8f255e5900b002a1b56902b68720e9dc53ac4bf7c77fa4.

- 2026-09-11T02:21:08+00:00: Recorded command exit 0; command argv SHA-256
  8b31fbfec24722742ffb67cb66c08a0b74a720bc35f2848ea35e562f6f35e653.

- 2026-09-11T02:21:18+00:00: Recorded command exit 0; command argv SHA-256
  a3fcd7aebd5cee13a64b26b7f894810e2874fbfd39bffb7248d031bf52670dd6.

- 2026-09-11T02:21:54+00:00: Recorded command exit 0; command argv SHA-256
  8e5f7e52745641ce056e681ffc16a5343048bc23d3f9045e9f1ab377ae09e5f4.

- 2026-09-11T02:22:11+00:00: Recorded command exit 0; command argv SHA-256
  4cb8fb4e0381ebefe22fd0f617d94c762694dead1bb36de8e7eb792afca0b0f0.

- 2026-09-11T02:22:54+00:00: Recorded command exit 0; command argv SHA-256
  cddcef2e64dad82530c0205f0347dac34cc840d7290c981556e565660ab29f6b.

- 2026-09-11T02:23:14+00:00: Recorded command exit 0; command argv SHA-256
  aabfa52733ee4cbbf1009b57838335e160dcba7f211310f3183d8a85697af462.

- 2026-09-11T02:24:03+00:00: Recorded command exit 0; command argv SHA-256
  cddcef2e64dad82530c0205f0347dac34cc840d7290c981556e565660ab29f6b.

- 2026-09-11T02:24:24+00:00: Recorded command exit 101; command argv SHA-256
  bdf4545080047d6c98fb35174f989f0f3d9efe6cc5773292fc3432b6e2d0391a.

- 2026-09-11T02:24:50+00:00: Recorded command exit 0; command argv SHA-256
  cddcef2e64dad82530c0205f0347dac34cc840d7290c981556e565660ab29f6b.

- 2026-09-11T02:25:26+00:00: Recorded command exit 0; command argv SHA-256
  c1680b7086c0937a9ca1e4d8f81cc5b7967a5c7e11d1fc67a8232200c04c5d6b.

- 2026-09-11T02:25:34+00:00: Recorded command exit 0; command argv SHA-256
  a3fcd7aebd5cee13a64b26b7f894810e2874fbfd39bffb7248d031bf52670dd6.

- 2026-09-11T02:25:57+00:00: Recorded command exit 101; command argv SHA-256
  9d9af5518562cdc4b455aa65a94878df909477c00ebdef5272804709bd5e7384.

- 2026-09-11T02:27:46+00:00: Recorded command exit 0; command argv SHA-256
  cddcef2e64dad82530c0205f0347dac34cc840d7290c981556e565660ab29f6b.

- 2026-09-11T02:28:13+00:00: Recorded command exit 0; command argv SHA-256
  9d9af5518562cdc4b455aa65a94878df909477c00ebdef5272804709bd5e7384.

- 2026-09-11T02:28:33+00:00: Recorded command exit 0; command argv SHA-256
  c2aad07bac119a9089d3d6d064bdabef854dcb98ba1eafc8322c0008ea02e142.

- 2026-09-11T02:28:43+00:00: Recorded command exit 0; command argv SHA-256
  a3fcd7aebd5cee13a64b26b7f894810e2874fbfd39bffb7248d031bf52670dd6.

- 2026-09-11T02:29:37+00:00: Recorded command exit 0; command argv SHA-256
  c2aad07bac119a9089d3d6d064bdabef854dcb98ba1eafc8322c0008ea02e142.

- 2026-09-11T02:29:50+00:00: Recorded command exit 0; command argv SHA-256
  a3fcd7aebd5cee13a64b26b7f894810e2874fbfd39bffb7248d031bf52670dd6.

- 2026-09-11T02:32:12+00:00: Recorded command exit 0; command argv SHA-256
  cddcef2e64dad82530c0205f0347dac34cc840d7290c981556e565660ab29f6b.

- 2026-09-11T02:32:28+00:00: Recorded command exit 101; command argv SHA-256
  9d9af5518562cdc4b455aa65a94878df909477c00ebdef5272804709bd5e7384.

- 2026-09-11T02:33:04+00:00: Recorded command exit 0; command argv SHA-256
  cddcef2e64dad82530c0205f0347dac34cc840d7290c981556e565660ab29f6b.

- 2026-09-11T02:33:16+00:00: Recorded command exit 0; command argv SHA-256
  9d9af5518562cdc4b455aa65a94878df909477c00ebdef5272804709bd5e7384.

- 2026-09-11T02:33:42+00:00: Recorded command exit 0; command argv SHA-256
  cddcef2e64dad82530c0205f0347dac34cc840d7290c981556e565660ab29f6b.

- 2026-09-11T02:33:53+00:00: Recorded command exit 101; command argv SHA-256
  aabfa52733ee4cbbf1009b57838335e160dcba7f211310f3183d8a85697af462.

- 2026-09-11T02:34:42+00:00: Recorded command exit 0; command argv SHA-256
  cddcef2e64dad82530c0205f0347dac34cc840d7290c981556e565660ab29f6b.

- 2026-09-11T02:35:20+00:00: Recorded command exit 0; command argv SHA-256
  d60f03278a2179bfdf5229edb504ca45b71dc41ad0ab11fbe1ce787f9bb12095.

- 2026-09-11T02:35:27+00:00: Recorded command exit 0; command argv SHA-256
  a3fcd7aebd5cee13a64b26b7f894810e2874fbfd39bffb7248d031bf52670dd6.

- 2026-09-11T02:36:15+00:00: Recorded command exit 0; command argv SHA-256
  4a0ea3e9a9c7b9f8a0ac58101d85474187c9976d78f57671b0a50460b61c4caf.

- 2026-09-11T02:39:01+00:00: Recorded command exit 0; command argv SHA-256
  867206790f33111679421a45e27f9b910cb92cc9e8400eb1d33fe1d5547c648a.

- 2026-09-11T02:39:32+00:00: Recorded command exit 0; command argv SHA-256
  9d9af5518562cdc4b455aa65a94878df909477c00ebdef5272804709bd5e7384.

- 2026-09-11T02:39:51+00:00: Recorded command exit 0; command argv SHA-256
  4a0ea3e9a9c7b9f8a0ac58101d85474187c9976d78f57671b0a50460b61c4caf.

- 2026-09-11T02:40:12+00:00: Recorded command exit 0; command argv SHA-256
  4077c05f70f8af41452c7603dc0fe5c6d318ef1970c9af2df61dfed1c7c22460.

- 2026-09-11T02:40:20+00:00: Recorded command exit 0; command argv SHA-256
  52b043a50e0d883a991c2a6481a9b502980bfe5f36aaa14e922561bd97012cd6.

- 2026-09-11T02:41:28+00:00: Recorded command exit 0; command argv SHA-256
  809316a678080364e0b556ed8776da9fb279818d5c3b918496df46ad87e70e33.

- 2026-09-11T02:42:23+00:00: Recorded command exit 0; command argv SHA-256
  1c7322890309a39dfa97ecef2cc0c5c594b630cb4d6cf33e7876368df6521d29.

- 2026-09-11T02:42:49+00:00: Recorded command exit 0; command argv SHA-256
  537e2e5e756a46fe0cbeb30d07663e7a1bcace097544c5ecd5c504dc847532af.

- 2026-09-11T02:43:14+00:00: Recorded command exit 0; command argv SHA-256
  1e9a3b28362b05b92c2a7302afa92ab75a3814e5363457f1840b3789be4c4c31.

- 2026-09-11T02:43:39+00:00: Recorded command exit 0; command argv SHA-256
  befa83057919fe49624c182b68bc0c4e789e0802905c589df649fe9533bca1fa.

- 2026-09-11T02:44:17+00:00: Recorded command exit 0; command argv SHA-256
  8ba79f8a648e8817f47dc7b23cb0a6f2968c3194bcd49f5eda568bf8935d5bf7.

- 2026-09-11T02:44:29+00:00: Recorded command exit 1; command argv SHA-256
  6aa059eac29f93ce734265924e108e4ece140a741e710c5e6e9de1c7f305d07b.

- 2026-09-11T02:44:46+00:00: Recorded command exit 0; command argv SHA-256
  541f51c4f03c8910479acf49153c05fe70d78e18ab45e609dc8d294a0b30f6a9.

- 2026-09-11T02:45:06+00:00: Recorded command exit 0; command argv SHA-256
  199d28615859b7271a35e742f39d249d4e4230ea4f2640cb9e550643a29d1ece.

- 2026-09-11T02:45:20+00:00: Recorded command exit 0; command argv SHA-256
  d89891896a30c11e230093a94ec7b651bd2ac90dbc5cf131651a96b46c115eed.

- 2026-09-11T02:45:37+00:00: Recorded command exit 0; command argv SHA-256
  b1438151ba9e3fe2a3f860a059709716221f3d9464b0c691312cc0732af17974.

- 2026-09-11T02:45:55+00:00: Recorded command exit 2; command argv SHA-256
  a1ca2f1c7f1228225d92ac60d21836832ead6fcbd267a35ad6c7203358fd27b9.

- 2026-09-11T02:48:53+00:00: Rebased single signed DCO commit onto postmerge-green ASB main
  23530dfc808650a8f3019c87a1c69fe3d0d654b5. Exact head d77e4a681f26f694cf0911188cb7996e5271c325 tree
  7147fe39efab91319d52da5a3359aef221f5c201. Full workspace all-target tests, clippy -D warnings,
  rustdoc -D warnings, release build and CLI help/version/invalid exit 2, contract consistency unit
  and run-tests gates all pass. Pre-rebase immutable review approved explicit-null presence fix;
  final post-rebase immutable review pending.

- 2026-09-11T02:50:50+00:00: Recorded command exit 1; command argv SHA-256
  867206790f33111679421a45e27f9b910cb92cc9e8400eb1d33fe1d5547c648a.

- 2026-09-11T02:51:16+00:00: Recorded command exit 0; command argv SHA-256
  cddcef2e64dad82530c0205f0347dac34cc840d7290c981556e565660ab29f6b.

- 2026-09-11T02:51:35+00:00: Recorded command exit 0; command argv SHA-256
  9d9af5518562cdc4b455aa65a94878df909477c00ebdef5272804709bd5e7384.

- 2026-09-11T02:51:52+00:00: Recorded command exit 101; command argv SHA-256
  4a0ea3e9a9c7b9f8a0ac58101d85474187c9976d78f57671b0a50460b61c4caf.

- 2026-09-11T02:52:09+00:00: Recorded command exit 0; command argv SHA-256
  4a0ea3e9a9c7b9f8a0ac58101d85474187c9976d78f57671b0a50460b61c4caf.

- 2026-09-11T02:52:40+00:00: Recorded command exit 0; command argv SHA-256
  72bb18ffbdd6c0d3c3d98b7079c149818c515cc1f39016d7250754a7bc25c71d.

- 2026-09-11T02:52:51+00:00: Recorded command exit 0; command argv SHA-256
  52b043a50e0d883a991c2a6481a9b502980bfe5f36aaa14e922561bd97012cd6.

- 2026-09-11T02:53:52+00:00: Recorded command exit 0; command argv SHA-256
  1c7322890309a39dfa97ecef2cc0c5c594b630cb4d6cf33e7876368df6521d29.

- 2026-09-11T02:54:12+00:00: Recorded command exit 0; command argv SHA-256
  537e2e5e756a46fe0cbeb30d07663e7a1bcace097544c5ecd5c504dc847532af.

- 2026-09-11T02:54:29+00:00: Recorded command exit 0; command argv SHA-256
  199d28615859b7271a35e742f39d249d4e4230ea4f2640cb9e550643a29d1ece.

- 2026-09-11T02:55:03+00:00: Immutable reviewer approved exact head/tree after fixing both blockers:
  public invalid version offers now reject before socket connect with no-accept regression, and raw
  publication wrapper bytes are capped before decode with outer-whitespace regression. Exact head
  full workspace tests and workspace clippy are green; contract consistency run-tests is green.

- 2026-09-11T02:55:12+00:00: Recorded command exit 0; command argv SHA-256
  187242ee63f931b31e01491ffc5dd693173bcd99728ad810d0e637a53836ac68.

- 2026-09-11T02:55:40+00:00: Recorded command exit 0; command argv SHA-256
  22e2b750e8ce85c2cb07368eed1b041ed39fd4bc8a6be3f84bf2743530760ab4.

- 2026-09-11T02:57:11+00:00: Recorded command exit 101; command argv SHA-256
  4c77b4abdc4442b9cd824b6f421dcdac6e2e4fa6e0910d590f9b49d2ffe71d40.

- 2026-09-11T02:57:31+00:00: Recorded command exit 0; command argv SHA-256
  6b16045eacaa86a0a6bc684174e44c23fcf0f7d082595fd4a3914f22ec850c6a.

- 2026-09-11T02:58:11+00:00: Recorded command exit 101; command argv SHA-256
  4c77b4abdc4442b9cd824b6f421dcdac6e2e4fa6e0910d590f9b49d2ffe71d40.

- 2026-09-11T02:58:35+00:00: Recorded command exit 0; command argv SHA-256
  2bd9aecb4ab741b2254e77e9d9302dc3194fe0084b398cd71717aa3d38ab27b0.

- 2026-09-11T02:59:07+00:00: Recorded command exit 0; command argv SHA-256
  4c77b4abdc4442b9cd824b6f421dcdac6e2e4fa6e0910d590f9b49d2ffe71d40.

- 2026-09-11T02:59:39+00:00: Recorded command exit 0; command argv SHA-256
  7d97e6d7ed825b3d847807e6021bd53ed133ff2768f056d4781801f2b0f11d70.

- 2026-09-11T02:59:47+00:00: Recorded command exit 0; command argv SHA-256
  52b043a50e0d883a991c2a6481a9b502980bfe5f36aaa14e922561bd97012cd6.

- 2026-09-11T03:01:01+00:00: Recorded command exit 0; command argv SHA-256
  09fc1aa6e36945f0ad44ca44c02246777698ea1a59571a8fb1083c9669880de5.
