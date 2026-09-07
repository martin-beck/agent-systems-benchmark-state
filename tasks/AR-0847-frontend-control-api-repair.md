---
{
  "branch": "feature/frontend-control-api-repair",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-07T23:29:31+00:00",
  "depends_on": [
    "AR-0101",
    "AR-0104",
    "AR-0204",
    "AR-0801"
  ],
  "id": "AR-0847",
  "next_action": "Monitor PR #54 exact head 0d2534f614cdc3ec43199bcb6da25083ef680f24; merge only after all required exact-head checks are terminal green and coordinator authorization.",
  "observed_branch": "feature/frontend-control-api-repair",
  "observed_dirty": 0,
  "observed_head": "0d2534f614cdc3ec43199bcb6da25083ef680f24",
  "owner": "replay_20260906",
  "plan": "../plans/AR-0847.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Repair and independently qualify the blocked frontend control API candidate.",
  "task_revision": 77,
  "title": "Frontend control API repair",
  "updated_at": "2026-09-07T22:01:56+00:00",
  "worktree_key": "agent-systems-benchmark-frontend-control-api-repair"
}
---
## AR-0847

Repair the blocked AR-0803 candidate without mutating its dirty worktree in place. Wire the protocol into a real runner endpoint/client and lifecycle recovery path; enforce absolute operation deadlines; restrict negotiation to offered versions; validate the initial envelope through the common path; and enforce bounded privacy for backend responses/errors. Add focused positive and negative tests, formal/fault/privacy evidence, exact immutable review, exact-head CI, integration, and post-merge verification. On completion, reconcile AR-0803's umbrella status and unblock its child frontend ARs.

- 2026-09-07T21:11:02+00:00: Promote focused repair for AR-0803 immutable-review findings;
  dependencies are complete and isolated worktree is available.

- 2026-09-07T21:11:04+00:00: Claimed by replay_20260906.

- 2026-09-07T21:13:31+00:00: Recorded command exit 0; command argv SHA-256
  7c145cae25b02f870487e3a09450303496a9a72f7b01b10b754f5034e73197ad.

- 2026-09-07T21:14:04+00:00: Recorded command exit 0; command argv SHA-256
  658fb5a97909c6f127ef833e6ff3e20add5ec672faf7819331111bc4da915c77.

- 2026-09-07T21:14:45+00:00: Recorded command exit 1; command argv SHA-256
  2d548922f2047456a47a0eeb3dbf48554efec24c5cc9323c131afb3b9bda7f8f.

- 2026-09-07T21:15:37+00:00: Recorded command exit 2; command argv SHA-256
  48458d4adcbc2714c4ae60f17ec39d916357031118af6e75d9a5cd826c73f20e.

- 2026-09-07T21:16:09+00:00: Recorded command exit 1; command argv SHA-256
  5c188617dec83f9f1010f73ca05003594c52bbc2b2659b0a180c3cd28785aa9c.

- 2026-09-07T21:17:35+00:00: Recorded command exit 0; command argv SHA-256
  c5d51883a7ef7dc025b0e911117a4a085f969f1e14a9642431c6f86b5292b019.

- 2026-09-07T21:17:49+00:00: Recorded command exit 0; command argv SHA-256
  4fec215f1bf600ab04757b8ce8ac2d4440f4c52bed405bd31581924757e16c3d.

- 2026-09-07T21:17:55+00:00: Recorded command exit 0; command argv SHA-256
  3177e091f96c86bc611ad9642929a7d37b185a320c1633263cba1eba3e40d88d.

- 2026-09-07T21:18:14+00:00: Recorded command exit 0; command argv SHA-256
  86b687f725cee36dba2a311ad07d2521b7f63589c3487007deb354b8aa25fb18.

- 2026-09-07T21:19:01+00:00: Recorded command exit 127; command argv SHA-256
  3ae507d85a97643c36d8319289be5b2fb008391efbdea064d236728dede86fed.

- 2026-09-07T21:21:16+00:00: Recorded command exit 0; command argv SHA-256
  98716b8379a7a16e4f2ec8e2154d9b0f04e40aec3e50692c7f25495685796cea.

- 2026-09-07T21:22:02+00:00: Recorded command exit 0; command argv SHA-256
  7c245a83e20bdc3ddf80a1130350c6beea96868eb2e7b3e21d1d9c578f020705.

- 2026-09-07T21:22:35+00:00: Recorded command exit 101; command argv SHA-256
  111541959c64681c19c974d4807b5b75186e59c992c7af70c8c7f4bff10261e8.

- 2026-09-07T21:22:45+00:00: Recorded command exit 0; command argv SHA-256
  0c2715ed55ffbce1d3113a3fb02dc4f09c7bce7eb2af02f5a5049c1383250f59.

- 2026-09-07T21:23:03+00:00: Recorded command exit 101; command argv SHA-256
  111541959c64681c19c974d4807b5b75186e59c992c7af70c8c7f4bff10261e8.

- 2026-09-07T21:23:40+00:00: Recorded command exit 0; command argv SHA-256
  a4ae643830492890b6269bd5ac6ec3e61656dd5e798da8a0b4212a934a829510.

- 2026-09-07T21:24:34+00:00: Recorded command exit 0; command argv SHA-256
  3c8536d6edc3b59d7c2360fd114f9d64c1d6c776369eb365f7fb998a63ad7417.

- 2026-09-07T21:24:56+00:00: Recorded command exit 101; command argv SHA-256
  1320fabc3ae5ece3c6533a47b31bfa1d7389481c083691ac109bea7be8d183d2.

- 2026-09-07T21:25:15+00:00: Recorded command exit 0; command argv SHA-256
  641f43cc4497e53dc84db1c8064978e11478ff516aeb6ed615c55b76ae69ddff.

- 2026-09-07T21:25:32+00:00: Recorded command exit 0; command argv SHA-256
  111541959c64681c19c974d4807b5b75186e59c992c7af70c8c7f4bff10261e8.

- 2026-09-07T21:28:29+00:00: Recorded command exit 0; command argv SHA-256
  c6b4f365620212c8c6373d76bc6d72c1ef4e3f570db859fa984b3e6b5175de1f.

- 2026-09-07T21:29:24+00:00: Recorded command exit 0; command argv SHA-256
  72d2d2c20cd07fa16f653e1af52e28a4ee8af6fa036bd194fe434a81bfcecfb8.

- 2026-09-07T21:29:38+00:00: Recorded command exit 0; command argv SHA-256
  9cbdfcea7a08c5cc8d8a5508513cfdcd72ec7c8e52aee5f5b47581578c88ff99.

- 2026-09-07T21:29:56+00:00: Recorded command exit 0; command argv SHA-256
  111541959c64681c19c974d4807b5b75186e59c992c7af70c8c7f4bff10261e8.

- 2026-09-07T21:30:36+00:00: Recorded command exit 0; command argv SHA-256
  5dd7387544ffaf96fc6b948c4807e0026f882caff903180c74f653a41624ff18.

- 2026-09-07T21:31:35+00:00: Recorded command exit 1; command argv SHA-256
  4cd4471c1c4ba65ed1e82bdf59129ea4ef34ee6dd2836ed2f587cf4d8e8a59c6.

- 2026-09-07T21:32:34+00:00: Recorded command exit 0; command argv SHA-256
  1996ae1d17b5e8feb7c8cc0121aa51630df8ae656bfe5b02d920a80f74ff3998.

- 2026-09-07T21:32:55+00:00: Recorded command exit 0; command argv SHA-256
  9cbdfcea7a08c5cc8d8a5508513cfdcd72ec7c8e52aee5f5b47581578c88ff99.

- 2026-09-07T21:33:01+00:00: Recorded command exit 0; command argv SHA-256
  17a8ab923f871ad30f50441eb572890294874791247caf820b5d0e27c8b28ae0.

- 2026-09-07T21:33:27+00:00: Recorded command exit 101; command argv SHA-256
  efe7203abb65d5c98cf8850391b98af96324965358d6907dc7d5885e10974de7.

- 2026-09-07T21:33:48+00:00: Recorded command exit 0; command argv SHA-256
  2170d834cbae8627043a26aa9d3d86f5af2535cb43b6232f0b01928181c85785.

- 2026-09-07T21:34:04+00:00: Recorded command exit 101; command argv SHA-256
  efe7203abb65d5c98cf8850391b98af96324965358d6907dc7d5885e10974de7.

- 2026-09-07T21:34:28+00:00: Recorded command exit 0; command argv SHA-256
  ff7157414de0a4137b45e1aa25b4ae955bd992b623ea27e7876d39f9b45c346e.

- 2026-09-07T21:34:47+00:00: Recorded command exit 0; command argv SHA-256
  efe7203abb65d5c98cf8850391b98af96324965358d6907dc7d5885e10974de7.

- 2026-09-07T21:35:27+00:00: Recorded command exit 0; command argv SHA-256
  7b2e77a47b8401ec343055d9fca7f78780d5e0d10a269d7a7fb7210ab7b0af22.

- 2026-09-07T21:35:46+00:00: Recorded command exit 1; command argv SHA-256
  ccaeaeff1ddde5f211cfbde513936a31e28df7a42385fb4a8aea2819cf96928f.

- 2026-09-07T21:36:04+00:00: Recorded command exit 0; command argv SHA-256
  9cbdfcea7a08c5cc8d8a5508513cfdcd72ec7c8e52aee5f5b47581578c88ff99.

- 2026-09-07T21:36:21+00:00: Recorded command exit 101; command argv SHA-256
  ccaeaeff1ddde5f211cfbde513936a31e28df7a42385fb4a8aea2819cf96928f.

- 2026-09-07T21:36:35+00:00: Recorded command exit 0; command argv SHA-256
  dbe037157a22c7b4043888aba71c2e82e66487911be32c589dc1dba326e2c0cf.

- 2026-09-07T21:36:58+00:00: Recorded command exit 0; command argv SHA-256
  2c9eb6b56db7196bde37f76627738b9edf5a7e0de31d16b8eb3cda2b6fe7cfe0.

- 2026-09-07T21:38:25+00:00: Recorded command exit 0; command argv SHA-256
  b6c009ecb1abe0ab9865905eaf780473cda2ebdcf47c1d9fcf6943f1b6335a40.

- 2026-09-07T21:39:00+00:00: Recorded command exit 1; command argv SHA-256
  ea2c36336ef3e17433e23038ea0a91ac6a33babe3eed877b1d8c2882ce4e663b.

- 2026-09-07T21:39:25+00:00: Recorded command exit 0; command argv SHA-256
  40aee6b77ec1bbd2d28e733694b0f3bf63019db5eaeddd1f95e43744fcbd626a.

- 2026-09-07T21:39:47+00:00: Recorded command exit 0; command argv SHA-256
  b6450fb33bd18bdb348b5e3e1dad74c5db4965302693cc1da65835a21886c7ef.

- 2026-09-07T21:40:15+00:00: Recorded command exit 1; command argv SHA-256
  ae32b28528c5e86dcc3daf6da47cde4eb387c993cf347ff2292e20406332de8c.

- 2026-09-07T21:41:05+00:00: Recorded command exit 0; command argv SHA-256
  905458f558d29278e6475e7b4f64dd87d6305d88331897ab68f912c71bb707ba.

- 2026-09-07T21:41:23+00:00: Recorded command exit 0; command argv SHA-256
  885185b783c38b79a26bfa277d4dd81b8596f780ef176258d2aa2606207944b5.

- 2026-09-07T21:42:13+00:00: Recorded command exit 0; command argv SHA-256
  d08049e16caf104876c7fb6c84b684d7b71ccb3dcb8fac55167f3cd7a85285f2.

- 2026-09-07T21:45:52+00:00: Recorded command exit 1; command argv SHA-256
  e65488dce8db00868a7a8ee94ef31ae01ad442d0b8fc3d3fc99bc37e306ccb21.

- 2026-09-07T21:46:27+00:00: Recorded command exit 0; command argv SHA-256
  b3d51888f327e4cd9ee4b33aec6842e671853e71f7472c8e6424ebcf8c3d367e.

- 2026-09-07T21:47:47+00:00: Recorded command exit 0; command argv SHA-256
  cb9eb5fcc9c4cfa3e402da5dc9f3c341d941d6e6bf8a56b9633662f00991e70c.

- 2026-09-07T21:48:31+00:00: Recorded command exit 2; command argv SHA-256
  b9db2366d9826cebda577956d0fcf073c1ce8fa9757efe733d37aed3d9d0eed7.

- 2026-09-07T21:48:58+00:00: Recorded command exit 1; command argv SHA-256
  36135485b8f8d455e3878139ed584214be9aaf565dddbc5974b9ef9f4cd1d1a9.

- 2026-09-07T21:49:23+00:00: Recorded command exit 0; command argv SHA-256
  9d2c5026833cc968e9a37fd7e93f7b10bc881bc5999cfeef116f33c235fa93c2.

- 2026-09-07T21:50:01+00:00: Candidate bcb4f8643b309f46f0b93eeb3a66ef98e4d30586 (tree
  bf4945643e78d1b11f926b1eaf419839c1b4d3ad, exact base 5a819633552f5d59885bc23c5e5127b1f131c102) is
  one focused 30-path SSH-signed Martin DCO commit. Repairs bind durable plan/run/attempt/event
  evidence, gate runner start until durable Running commit, enforce absolute mutation
  deadlines/no-late-effect checks, and make SettingsValidation schema/runtime parity explicit.
  Focused control/CLI tests, parallel lifecycle tests, full workspace test/clippy/fmt/docs/release,
  formal model tests, Kani 6/6 plus failing negative, coverage floors, cargo-deny/audit, repository
  policy, failure fixtures, actionlint/zizmor, Gitleaks, bounded four-target fuzz 256 each, and
  mutation 7/7 are green. Recorded failures were environmental/tooling or assertion corrections:
  cargo was initially absent from PATH; formal lock required offline regeneration; Kani needed
  declared tool homes; fuzz created its documented disposable artifacts directory then all 4 targets
  passed and the exact directory was removed; two immutable scope commands used incorrect local
  script/regex names and were corrected without product changes. Exact diff-check, signature/DCO,
  30-path scope, no private-host paths, clean worktree, and preservation hash of the original
  AR-0803 dirty worktree are verified. No publication yet.

- 2026-09-07T21:51:06+00:00: Recorded command exit 1; command argv SHA-256
  636494725e144477bb865a7f3afb02b94e2a329e6a4a2eeb7a396d49f8c6bdd1.

- 2026-09-07T21:52:12+00:00: Recorded command exit 0; command argv SHA-256
  a026fe0b2757f260dd0a5714b2fd719b40f7d65dd894309de423e87a1986f91b.

- 2026-09-07T21:53:50+00:00: Recorded command exit 2; command argv SHA-256
  721e5616fb9f3d65785a537b401ce3f9c34f99eb1f70a26e7688064bca46eebf.

- 2026-09-07T21:55:47+00:00: Recorded command exit 0; command argv SHA-256
  81d6f2ca3de76c5c8665e9886de4ff61707f44e224b3fc0663e54ac000acaac4.

- 2026-09-07T21:56:23+00:00: Recorded command exit 0; command argv SHA-256
  ed1c5e7400e5809855b2d722107754c90d6040478378fded3fb2a0ea9c2ce257.

- 2026-09-07T21:57:03+00:00: Recorded command exit 0; command argv SHA-256
  ae8df6dbe6aa2209fefd9947265e8a4d290395e6899d04910cfa1f2125890be6.

- 2026-09-07T21:58:13+00:00: Recorded command exit 0; command argv SHA-256
  90d70d384880488f268bbe454ebe22d736459cfdb333a7e1fccf30b9aeef6c73.

- 2026-09-07T21:59:04+00:00: Recorded command exit 0; command argv SHA-256
  81f058e2e8f8fdbe96c8b436af6f2a5968928e1e6173638b51e34efb6805bfff.

- 2026-09-07T21:59:31+00:00: Heartbeat by replay_20260906.

- 2026-09-07T21:59:59+00:00: Publication preflight found origin/main advanced to
  111be970534fbf72332a80c2291fe1fe21acb694 before any push or PR. Coordinator authorized serialized
  rebase. The intervening Goose-only two-path change had no overlap; rebase was conflict-free and
  exact range-diff equals the prior reviewed bcb4f864 candidate. Successor
  0d2534f614cdc3ec43199bcb6da25083ef680f24 (tree ed743519089568f809076c425b6d3d7aed90fb42, parent
  111be970534fbf72332a80c2291fe1fe21acb694) is a clean one-commit SSH-signed Martin DCO candidate.
  Post-rebase focused and parallel control tests, full workspace fmt/clippy/tests/docs/release,
  formal tests, Kani 6/6 plus negative, repository/failure/workflow/platform policy, dependency
  audit, coverage floors, bounded four-target fuzz 256 each, mutation 7/7, Gitleaks,
  diff/scope/private-path checks all pass. One quality rerun first omitted the required
  failure-fixture bin-dir argument; corrected invocation passed without product changes. Original
  AR-0803 dirty worktree remains exact and unchanged. No remote feature branch or PR exists.

- 2026-09-07T22:01:09+00:00: Recorded command exit 0; command argv SHA-256
  711daa7247d2b15e017565267e3999b1edd5654bfce0568d4f4bc8d4a1de47af.

- 2026-09-07T22:01:56+00:00: Published immutable successor 0d2534f614cdc3ec43199bcb6da25083ef680f24
  with an exact absent-branch lease after verifying origin/main remained
  111be970534fbf72332a80c2291fe1fe21acb694. Opened focused PR #54 with exact base/head identity.
  Exact-head runs started: repository quality 34165176857; Rust x86_64+aarch64 34165176859;
  formal/Kani x86_64+aarch64 34165176880; fault/fuzz/mutation x86_64+aarch64 34165176887. All were
  in progress at recording; merge is held.
