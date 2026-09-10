---
{
  "branch": "feature/asb-tui-compatibility-detection",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-10T16:16:31+00:00",
  "depends_on": [
    "AR-1017"
  ],
  "id": "AR-1018",
  "next_action": "Obtain independent immutable review of f5edd558; do not publish or mutate the candidate before approval.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "contracts_20260906",
  "plan": "../plans/AR-1018.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Detect whether an asb-tui bundle is compatible before installation or launch.",
  "task_revision": 75,
  "title": "Add asb-tui compatibility and terminal capability detection",
  "updated_at": "2026-09-10T13:34:50+00:00",
  "worktree_key": "agent-systems-benchmark-asb-tui-compatibility-detection"
}
---
Detect OS/distribution, architecture, ASB version, protocol version, exact coordinator and
workflow-quality release compatibility, terminal dimensions/features,
SSH/tmux/screen context, and filesystem/runtime requirements. Select only compatible bundles and fail
closed with actionable diagnostics for unsupported combinations.

Acceptance criteria: deterministic machine-readable capability report, resize/channel tests, negative
fixtures for mismatches, privacy-safe diagnostics, and no host identifiers in public artifacts.

- 2026-09-10T12:40:02+00:00: AR-1017 is durably done at state 9aa38bcc with public exact-head checks
  and protection verified; AR-1018 is dependency-ready and owns disjoint compatibility detection.

- 2026-09-10T12:40:09+00:00: Claimed by contracts_20260906.

- 2026-09-10T12:40:29+00:00: Recorded command exit 0; command argv SHA-256
  263e132bbd0547042ae890d6380355f5364a45e5528910bdc3a67484dad324a6.

- 2026-09-10T12:45:28+00:00: Heartbeat by contracts_20260906.

- 2026-09-10T12:48:53+00:00: Recorded command exit 0; command argv SHA-256
  420472530e9d05303c33574061da3466b08bd64279b64a0008c4823f781a749a.

- 2026-09-10T12:49:04+00:00: Recorded command exit 101; command argv SHA-256
  59ec19432c7293e890383e067eeb07cf9a2ffae1aa12643fbdd0d792c7fa7fc0.

- 2026-09-10T12:51:21+00:00: Recorded command exit 0; command argv SHA-256
  420472530e9d05303c33574061da3466b08bd64279b64a0008c4823f781a749a.

- 2026-09-10T12:51:32+00:00: Recorded command exit 0; command argv SHA-256
  c9be30c10bf536e6c31fe8e5e3c2dbea49e29970e128dab52c3e4c45b3406367.

- 2026-09-10T12:51:42+00:00: Recorded command exit 0; command argv SHA-256
  4f2ddd9f039f2d8ae863160f907b82991d379b3ba87df7ab44fd95b9335a2491.

- 2026-09-10T12:55:13+00:00: Recorded command exit 0; command argv SHA-256
  420472530e9d05303c33574061da3466b08bd64279b64a0008c4823f781a749a.

- 2026-09-10T12:55:23+00:00: Recorded command exit 0; command argv SHA-256
  6fc8a14fcd761c01f586439ca0091c5ece7e229c7583879466962175a026dcde.

- 2026-09-10T12:55:32+00:00: Recorded command exit 0; command argv SHA-256
  4f2ddd9f039f2d8ae863160f907b82991d379b3ba87df7ab44fd95b9335a2491.

- 2026-09-10T12:55:41+00:00: Recorded command exit 0; command argv SHA-256
  e0396fd60d3a67d470b76f8925a026ebe7b817491604aeeeaecb79ccb38b4797.

- 2026-09-10T12:56:47+00:00: Recorded command exit 0; command argv SHA-256
  51c68dba96c0ef380a9368725f4aeb5819cd8ddf081c7a26a03d9c07cc018064.

- 2026-09-10T12:56:58+00:00: Recorded command exit 0; command argv SHA-256
  4e083eb5b3e77fb3ba1dd4f2ebb048bdf8151a497d2c7e2017cac7521e6d3800.

- 2026-09-10T12:57:15+00:00: Recorded command exit 0; command argv SHA-256
  9f3a2440bff01b4d24d2919beeb6d9737d350456482bee38ad7a277dff3e2e84.

- 2026-09-10T12:57:27+00:00: Recorded command exit 0; command argv SHA-256
  30a140d28210fcc3dccbbac332b10dfcc658d7918ef74ed6db6ced64a261183e.

- 2026-09-10T12:57:37+00:00: Recorded command exit 0; command argv SHA-256
  0edf3596ea0b07b191facdd776911433caa7cd521df6f4a7172e76b95c412cd5.

- 2026-09-10T12:57:45+00:00: Recorded command exit 0; command argv SHA-256
  d769193a8d50b9d7fa9f6f5f77c928dfc84c527a52f3a1e7f77daedcb6eeb9e9.

- 2026-09-10T12:57:55+00:00: Recorded command exit 0; command argv SHA-256
  d1b77cdc839fe95285cefcab486f47433cb3668f860ac98898c4845d9a16b6c5.

- 2026-09-10T12:58:28+00:00: Recorded command exit 0; command argv SHA-256
  1e432592b40c53a69194cff35ccd165f4dac63a22362c50b7e071883b490c17e.

- 2026-09-10T12:58:36+00:00: Recorded command exit 0; command argv SHA-256
  e43205235f188e57cc2535216051ffed3d3a0b6d003e100e2a7967bd140f4962.

- 2026-09-10T12:59:02+00:00: Recorded command exit 0; command argv SHA-256
  18bffdfc42466344d07f3b24f54205227d50df78b1e78174ed11a49c41b4a166.

- 2026-09-10T12:59:24+00:00: Recorded command exit 0; command argv SHA-256
  3828cfb12503069208247b7f6ebdae50f814294ce56ddcab2342a8325206a82d.

- 2026-09-10T12:59:37+00:00: Recorded command exit 0; command argv SHA-256
  ed1b8ab0753de1174529384365d93305c8bba1a8fa0261ee48d3ee4932dd7da2.

- 2026-09-10T12:59:45+00:00: Recorded command exit 0; command argv SHA-256
  0325f233f7b139f84e5a3f3c528b7299e1860d6ddcd06fc03318a6965c16e9c2.

- 2026-09-10T12:59:53+00:00: Recorded command exit 0; command argv SHA-256
  8810c52e3f82557e363f63b0bf2d37c0dd3da2133a4a9342201b571fb591d5d9.

- 2026-09-10T13:00:02+00:00: Recorded command exit 0; command argv SHA-256
  1f46cc71a57b572f7a8840331cf1d4e8093cafe922185fcd01790d9fe57be343.

- 2026-09-10T13:00:11+00:00: Recorded command exit 0; command argv SHA-256
  84e189320995361983fcf56c37a7b816a1cc838b3cd66c49dab3f0b068145df6.

- 2026-09-10T13:00:19+00:00: Recorded command exit 0; command argv SHA-256
  05b71d6f7e1a710594ddaa08e5e4030ecd1fc14afe2293a7eed4d94755cb8097.

- 2026-09-10T13:00:27+00:00: Recorded command exit 0; command argv SHA-256
  f83d1e654052d38912e7eef20bbbe8187a645d1788712022b66bd6cf25080f81.

- 2026-09-10T13:01:03+00:00: Immutable AR-1018 candidate
  f5edd5583f78ba333af7b29fee428c7d0b3fb8e1/tree b46502b9de37208f06b13c114a35dd3c0ff47131, exact
  parent public main c2fcb7221db24c847ef81cde010735de15cb10f3, is SSH-signed with exact DCO and
  clean 11-path scope. It adds closed probe/report schemas and deterministic stdin CLI evaluation
  for normalized Linux distribution, x86_64/AArch64, installed ASB/protocol versions, exact
  coordinator v0.3.5 and quality v0.23.0 commits, terminal
  size/color/Unicode/resize/channel/SSH/tmux/screen facts, storage/filesystem/verifier requirements,
  and compatible bundle selection. Fixed reason codes fail closed without input-controlled
  diagnostics or host/path/credential fields. Positive, mismatch, malformed, oversized,
  wrong-version/type, unsupported platform, boundary resize/channel, tooling/runtime exhaustive
  negatives, context, schema, privacy, deterministic output, and executable exit tests pass. One
  initial test failed because it incorrectly expected unsupported_distribution for a supported
  Ubuntu token paired with Windows; implementation correctly returned inconsistent_platform, and the
  fixture expectation was corrected. Full 27 tests, fmt, Clippy -D warnings, rustdoc -D warnings,
  release build, cargo-deny, cargo-audit, JSON schemas, ShellCheck/shfmt, actionlint/Zizmor,
  Gitleaks/privacy, ASB-core absence (16 tests plus 2 doctests), diff/scope, and clean llvm-cov
  passed. Coverage is 90.42% lines and 88.01% regions; worktree is clean with no in-checkout
  profiles.

- 2026-09-10T13:09:27+00:00: Recorded command exit 0; command argv SHA-256
  1b63e3a086eded049150930a3fa8b967acc421ae4f7cc14a275c2532cefaa6c6.

- 2026-09-10T13:12:15+00:00: Recorded command exit 0; command argv SHA-256
  435d3402335484310ee61e6f7a3febd605a7cef65429f809d5af347f1da8bb4b.

- 2026-09-10T13:13:40+00:00: Heartbeat by contracts_20260906.

- 2026-09-10T13:13:43+00:00: Recorded command exit 0; command argv SHA-256
  420472530e9d05303c33574061da3466b08bd64279b64a0008c4823f781a749a.

- 2026-09-10T13:13:52+00:00: Recorded command exit 0; command argv SHA-256
  4f2ddd9f039f2d8ae863160f907b82991d379b3ba87df7ab44fd95b9335a2491.

- 2026-09-10T13:14:03+00:00: Recorded command exit 0; command argv SHA-256
  6fc8a14fcd761c01f586439ca0091c5ece7e229c7583879466962175a026dcde.

- 2026-09-10T13:15:42+00:00: Recorded command exit 0; command argv SHA-256
  e0396fd60d3a67d470b76f8925a026ebe7b817491604aeeeaecb79ccb38b4797.

- 2026-09-10T13:16:31+00:00: Heartbeat by contracts_20260906.

- 2026-09-10T13:16:45+00:00: Recorded command exit 0; command argv SHA-256
  35f24c28baa91f237b176d1f256b55749476d4a413dbf57f5a290a8dfa1d2be2.

- 2026-09-10T13:16:55+00:00: Recorded command exit 0; command argv SHA-256
  059e6a152e09bbf6ae3742f6f6271fcf216e064ca8967875c57bc45c400d0c18.

- 2026-09-10T13:17:04+00:00: Recorded command exit 0; command argv SHA-256
  4b01de94b998ff6efadcd371fbf5845eb3a917ad40bcd22829b30c4fa611b3e6.

- 2026-09-10T13:17:25+00:00: Recorded command exit 0; command argv SHA-256
  5b3375e3cc031e37e8fde1c9abfe73350db366801d81872fda2afa3a82ba0de7.

- 2026-09-10T13:17:35+00:00: Recorded command exit 0; command argv SHA-256
  47dab87005c62c329fd263d1034197b77205eec76c23386e9f2320fb5aa8af21.

- 2026-09-10T13:17:43+00:00: Recorded command exit 0; command argv SHA-256
  09c8704ab04930c292618cb5706dd1575ff966c2ae1ed6eb7e91036cf1d484a9.

- 2026-09-10T13:17:52+00:00: Recorded command exit 0; command argv SHA-256
  2b1f17d9af718b7bb07ed05d7b47c688b44861d246620eab8bf340538adde4b5.

- 2026-09-10T13:18:24+00:00: Recorded command exit 0; command argv SHA-256
  ecf623d8cec98a5a4182ee9de7d33dfc0de8e186091c44a4c2bb2bae8c439487.

- 2026-09-10T13:18:34+00:00: Recorded command exit 0; command argv SHA-256
  7e44c349371b5487599919817e76c4e004b4d1338d65a6ca034f4a902d418922.

- 2026-09-10T13:18:42+00:00: Recorded command exit 0; command argv SHA-256
  95ae97b7257dc9978c94ea0d3e2af3ec28989fd3f2bbee9dec2d1f23ab4df45c.

- 2026-09-10T13:18:50+00:00: Recorded command exit 0; command argv SHA-256
  5181f057872e31f91ae5a350c93057860a0a9fd22f5dba9de98ab37249669f97.

- 2026-09-10T13:19:01+00:00: Recorded command exit 0; command argv SHA-256
  8a7cded50f89394b0393eef846ada0db21ea6dd16229c09a21ae3c0c31f5ecc9.

- 2026-09-10T13:19:43+00:00: Recorded command exit 0; command argv SHA-256
  e2298269cf1efd277173e95a427f30eda2990eea9d3a3dccea717e5b50946dea.

- 2026-09-10T13:19:51+00:00: Recorded command exit 0; command argv SHA-256
  5622f2b0a461d793487db522f5dbfb2f0f42f8d4bf38a8c18d20edc502ff44e8.

- 2026-09-10T13:20:00+00:00: Recorded command exit 0; command argv SHA-256
  68aac84351e5eb6ff1d77d3f981e02b02f6d4c63961c6d8823da9b2284598678.

- 2026-09-10T13:20:09+00:00: Recorded command exit 0; command argv SHA-256
  d9d943ae0547b67a0c64795c51381fb9effa2ce8b2d83f279017624840d1e648.

- 2026-09-10T13:20:28+00:00: Recorded command exit 0; command argv SHA-256
  ee3d772f5fbc578359310c1bbd405bcefe2c14a8f043997a1037c1974f7555c6.

- 2026-09-10T13:20:38+00:00: Recorded command exit 0; command argv SHA-256
  f53f6dbdcd061779a6a6c6bfe55671c7a4364c258e7cd981299fa25339dc0cb1.

- 2026-09-10T13:20:48+00:00: Recorded command exit 0; command argv SHA-256
  7a3e4396e18db02a19b30b579e94a09c567f535ce58feb634b8b4f7817f8d140.

- 2026-09-10T13:24:21+00:00: Recorded command exit 101; command argv SHA-256
  8a62776d99ae6c6069285dd3f66a66129da72bcdc382c71a5d752de61c6783d6.

- 2026-09-10T13:24:43+00:00: Recorded command exit 101; command argv SHA-256
  3f7d5d0a9c3a59c0c824cea7f9f1a60701fc84ef6fd992ce18f333e5ddec003c.

- 2026-09-10T13:25:35+00:00: Recorded command exit 127; command argv SHA-256
  262d50bd575b0241150803b9e3be7fe643f983ba01f8e9b667eb8edd239f0e6a.

- 2026-09-10T13:26:02+00:00: Recorded command exit 101; command argv SHA-256
  8deddfdca7884b0a4415aef332e4e26a6780d67c4c002de5c8903b931e1122ff.

- 2026-09-10T13:27:21+00:00: Recorded command exit 101; command argv SHA-256
  8deddfdca7884b0a4415aef332e4e26a6780d67c4c002de5c8903b931e1122ff.

- 2026-09-10T13:28:42+00:00: Recorded command exit 101; command argv SHA-256
  8deddfdca7884b0a4415aef332e4e26a6780d67c4c002de5c8903b931e1122ff.

- 2026-09-10T13:29:42+00:00: Recorded command exit 101; command argv SHA-256
  8deddfdca7884b0a4415aef332e4e26a6780d67c4c002de5c8903b931e1122ff.

- 2026-09-10T13:30:24+00:00: Recorded command exit 101; command argv SHA-256
  8deddfdca7884b0a4415aef332e4e26a6780d67c4c002de5c8903b931e1122ff.

- 2026-09-10T13:30:50+00:00: Recorded command exit 101; command argv SHA-256
  272e4586928b3548aa3fe9735f36371798234e2b90b05b47d344f88ee605379f.

- 2026-09-10T13:31:25+00:00: Recorded command exit 101; command argv SHA-256
  8deddfdca7884b0a4415aef332e4e26a6780d67c4c002de5c8903b931e1122ff.

- 2026-09-10T13:32:18+00:00: Recorded command exit 101; command argv SHA-256
  b8f363cab874b09f185cacf2e4edcff594a8d16fe43bf7d3fd11064213884079.

- 2026-09-10T13:32:32+00:00: Recorded command exit 101; command argv SHA-256
  8deddfdca7884b0a4415aef332e4e26a6780d67c4c002de5c8903b931e1122ff.

- 2026-09-10T13:33:22+00:00: Recorded command exit 101; command argv SHA-256
  272e4586928b3548aa3fe9735f36371798234e2b90b05b47d344f88ee605379f.

- 2026-09-10T13:34:00+00:00: Recorded command exit 101; command argv SHA-256
  272e4586928b3548aa3fe9735f36371798234e2b90b05b47d344f88ee605379f.

- 2026-09-10T13:34:50+00:00: Recorded command exit 101; command argv SHA-256
  8deddfdca7884b0a4415aef332e4e26a6780d67c4c002de5c8903b931e1122ff.
