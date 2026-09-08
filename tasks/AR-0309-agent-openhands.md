---
{
  "branch": "feature/agent-openhands",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-08T06:49:55+00:00",
  "depends_on": [
    "AR-0101",
    "AR-0102",
    "AR-0103"
  ],
  "id": "AR-0309",
  "next_action": "Await coordinator disposition for main advancement to 123c58f after approval of e73767d; do not publish or perform another rebase without explicit authorization.",
  "observed_branch": "feature/agent-openhands",
  "observed_dirty": 0,
  "observed_head": "fec0487e4fd8a78b86ce5caba023e30fe40a0cd8",
  "owner": "contracts_20260906",
  "plan": "../plans/AR-0309.md",
  "priority": "P2",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Run a maintained MIT OpenHands SDK or canonical headless client.",
  "task_revision": 118,
  "title": "Implement maintained OpenHands SDK client adapter",
  "updated_at": "2026-09-08T06:45:24+00:00",
  "worktree_key": "agent-systems-benchmark-agent-openhands"
}
---
## AR-0309

Run a maintained MIT OpenHands SDK or canonical headless client.

Implementation has not started. Read the linked plan before claiming.


- 2026-09-08T03:49:45+00:00: Verified AR-0101, AR-0102 and AR-0103 are durably done. Selected
  highest-priority safe disjoint leaf after P1 authorization/dependency/path blockers; OpenHands
  module and fixtures do not overlap active frontend protocol, verifier integrity, or kernel
  diagnostics paths.

- 2026-09-08T03:49:55+00:00: Claimed by contracts_20260906.

- 2026-09-08T03:50:41+00:00: Recorded command exit 0; command argv SHA-256
  07036c4ad1b996ca80da9bef22d326a3298e0fa2af6aa940f96f17b07676a4b3.

- 2026-09-08T03:55:22+00:00: Official-source boundary resolved: use active MIT
  OpenHands/software-agent-sdk v1.45.0, signed tag commit 49ea74587c376b90700f6eff128c3d9b57585d27
  and tree 639a6850375c0d8e04c9f045a5a74c15fea0406c. Exclude OpenHands/OpenHands enterprise paths.
  Do not use OpenHands-CLI 1.16.0 for this adapter: although MIT and maintained, its latest release
  pins older SDK/tools 1.21.0 and documented headless operation is always-approve, so it cannot
  expose the required bounded confirmation policy as cleanly as the SDK.

- 2026-09-08T03:57:02+00:00: Recorded command exit 1; command argv SHA-256
  10c15ae9e6c277a981542655bf485392a3392b9b9505a04cd20806bfee47a5f6.

- 2026-09-08T03:57:30+00:00: Recorded command exit 1; command argv SHA-256
  66da4fbe5e6464ee9d68e3834c74fb42921242e766b1a2034ec420c1ef435f21.

- 2026-09-08T03:57:44+00:00: Recorded command exit 1; command argv SHA-256
  a70f1bec1335a8a298c55d63e5fc86519af84c76b83ea9cd68b18201618a534f.

- 2026-09-08T03:57:56+00:00: Recorded command exit 0; command argv SHA-256
  e046063cdec35e5ac2dbf813eb115fc953730f3e03311593c44b06f6516ac43b.

- 2026-09-08T03:58:16+00:00: Recorded command exit 0; command argv SHA-256
  9fe3ace62ad35d411bb905dd2705e9f7d79b3ceb478a126d89f6a69420d7abe6.

- 2026-09-08T04:00:15+00:00: Recorded command exit 2; command argv SHA-256
  cb76f2eadc7d84a08940326c617e2bf9e8f94bdca84bf86b5de2ac1eaaae9c80.

- 2026-09-08T04:04:01+00:00: Recorded command exit 0; command argv SHA-256
  62f7e88cca66e94b3960fdd21aea322fc297518ec6d1f8e85a57859d59815363.

- 2026-09-08T04:04:30+00:00: Recorded command exit 1; command argv SHA-256
  6d819964b1301e94d9f87cb995f8e740fe9292a49829e809bcd0459299e90be5.

- 2026-09-08T04:04:42+00:00: Recorded command exit 0; command argv SHA-256
  6fc8587a9a6a662fe07b64324f08c93893fd0642ce7d3a85c73afd2fc988b76a.

- 2026-09-08T04:05:10+00:00: Recorded command exit 0; command argv SHA-256
  b843a942da9e23c42becd7c8321107d1e2604df3eb69e56d1497f6f28962d4a4.

- 2026-09-08T04:06:18+00:00: Native credential-free SDK probe succeeded with OpenHands SDK 1.45.0 on
  CPython 3.12: isolated HOME/XDG roots, no persistence_dir (InMemoryFileStore), AlwaysConfirm
  pending-action validation, a custom bounded write tool, finish event, positive aggregate usage (20
  input/8 output), and exact workspace edit. Closed proxies exposed one denied LiteLLM remote
  cost-map attempt, so production must force the local cost map and reject diagnostics. The first
  all-wheel install failed because func-timeout 4.3.5 is sdist-only; sdk-only resolves 136 packages,
  while adding openhands-tools/workspace expands to 194 packages. Use SDK-only plus ASB-owned
  bounded tool to minimize attack surface.

- 2026-09-08T04:13:03+00:00: Recorded command exit 0; command argv SHA-256
  f1ed95d4565d704f631d934aaba61d6ff0d10990eb20b1c29fe6b01067540429.

- 2026-09-08T04:13:41+00:00: Recorded command exit 0; command argv SHA-256
  f03f14a4247d608d63dd21bc9152c3cfbcb749c39750ac882aff3713eac8bfb5.

- 2026-09-08T04:14:07+00:00: Recorded command exit 101; command argv SHA-256
  73ace59d4f0fe2f69761406da10d9d0939a4b3f693e34b49bb753040bb97450d.

- 2026-09-08T04:14:16+00:00: Recorded command exit 0; command argv SHA-256
  1eaa9f61492f2fa1edf39d0edf9b9a06d9fed16270d338827188a7b0d21f64ba.

- 2026-09-08T04:14:44+00:00: Recorded command exit 101; command argv SHA-256
  14a63e3bea35a89d4ad3486f63c95f0799d2369b8ea961c6a9fe0d578f3dd77f.

- 2026-09-08T04:14:57+00:00: Recorded command exit 0; command argv SHA-256
  763962ff3b0e6a2f13ff08bc4467a1ec365ad6efaff40757cc7a074492f3b1ce.

- 2026-09-08T04:15:12+00:00: Recorded command exit 0; command argv SHA-256
  14a63e3bea35a89d4ad3486f63c95f0799d2369b8ea961c6a9fe0d578f3dd77f.

- 2026-09-08T04:15:40+00:00: Recorded command exit 0; command argv SHA-256
  fe167aadf3ab5243ef1c89cc19a5d83748303e4ac63fc017fcad23703e07b109.

- 2026-09-08T04:16:01+00:00: Recorded command exit 0; command argv SHA-256
  531b9f90f5f44de6e479e1a3ae7762a516f07d37bfa0224448d15838d76abfde.

- 2026-09-08T04:16:19+00:00: Recorded command exit 22; command argv SHA-256
  4361bfb8a54af48cb9c5c3320b0c554ac3350719262a8712779b286f1a0f9bdc.

- 2026-09-08T04:16:41+00:00: Recorded command exit 0; command argv SHA-256
  a718cc544b283cf7e07efd1fdfce7bdaabece280dbf5868d441f8986e4ed3167.

- 2026-09-08T04:17:35+00:00: Recorded command exit 0; command argv SHA-256
  3ce2ab4c31361a8955878a1aa819adb8c2414f77e819c19caed3b5a473acfa15.

- 2026-09-08T04:18:57+00:00: Recorded command exit 0; command argv SHA-256
  ba28b285a03f66cccfa4eec432ead2320829d85d5b615e7272000ba91c045618.

- 2026-09-08T04:19:15+00:00: Recorded command exit 0; command argv SHA-256
  1eaa9f61492f2fa1edf39d0edf9b9a06d9fed16270d338827188a7b0d21f64ba.

- 2026-09-08T04:19:29+00:00: Recorded command exit 0; command argv SHA-256
  14a63e3bea35a89d4ad3486f63c95f0799d2369b8ea961c6a9fe0d578f3dd77f.

- 2026-09-08T04:21:57+00:00: Isolated module and real fixture now exist in the declared worktree
  only. Focused compile/parser/config tests pass (3 passed, native ignored). Real credential-free
  SDK 1.45.0 test passed in 100.41s after content-verifying and privately copying 16,168 environment
  entries / 271,861,732 bytes: exact public sentinel auth, loopback-only request, AlwaysConfirm
  allowlist, one bounded write, finish, positive usage, empty private state, and cleanup.
  OpenHands/LiteLLM stdout and stderr were empty with local cost-map forcing. The wrapper
  evidence-record phase was interrupted while waiting on the shared state lock after the test had
  completed; no product or fixture residue remained.

- 2026-09-08T04:22:18+00:00: Recorded command exit 0; command argv SHA-256
  f973b1b00d8ef44cc057c439be98a059a4c095ca2591bf4a480693241e9805b9.

- 2026-09-08T04:23:06+00:00: Recorded command exit 1; command argv SHA-256
  a6635dd33f93e324c2835eec64ce508566d51eb4b340d8b9b26d8ed629b463e1.

- 2026-09-08T04:23:26+00:00: Recorded command exit 0; command argv SHA-256
  efcead93d4f345fcd9a05f6573f652228dcb288f10c8c4d9e55e0eba2b30a64e.

- 2026-09-08T04:23:53+00:00: Recorded command exit 0; command argv SHA-256
  f6d43615efafbbffd8a86df38f85d7c24acf169ba32d5fd7efcc735375a647b7.

- 2026-09-08T04:24:23+00:00: Recorded command exit 0; command argv SHA-256
  83a8b957bd3f6fb383d2333a77ffa903033c543696fcdf58eac689660dedf410.

- 2026-09-08T04:24:50+00:00: Recorded command exit 101; command argv SHA-256
  90aa1e8fe5e2eac3c795a2f8bbea5f42b5bfc1272fbf786ce93746e8d3bc2cf6.

- 2026-09-08T04:24:56+00:00: Recorded command exit 0; command argv SHA-256
  4924ef45fbaf0378af3ea6923746c20494cc87a01d8fc3a5668cec4698f045f4.

- 2026-09-08T04:25:14+00:00: Recorded command exit 0; command argv SHA-256
  5b4943d1ea56c24ad972cc0a28351ccfe4860920c3bcaee11c6846b4669e6209.

- 2026-09-08T04:25:40+00:00: Recorded command exit 0; command argv SHA-256
  790a009e741575e7c8951b389f84d9f707c77acfa8790d6f26e79a59c1294365.

- 2026-09-08T04:26:12+00:00: Signed+DCO isolated checkpoint 725c40bd41b18947d25a4a986dab4a3ba46f0cd6
  (tree 34eb8e470d879c701dc88ccab6446855b96f419e) adds only openhands.rs, openhands_boundary.rs and
  the 136-package exact freeze fixture. Focused rustfmt, 3 unit/contract tests and Clippy -D
  warnings pass; the real SDK fixture passed separately. Shared crates/asb-agents/src/lib.rs is
  intentionally untouched pending coordinator fence.

- 2026-09-08T04:27:20+00:00: Recorded command exit 1; command argv SHA-256
  96d8523cda3fe97b86a5b045170925c8f207b9f288878c9baf92757324b14493.

- 2026-09-08T04:28:01+00:00: Recorded command exit 0; command argv SHA-256
  edcfbed5462a80e00772e667d93baf42a4c5ac0339ed93379613cefdc65fa760.

- 2026-09-08T04:28:53+00:00: Recorded command exit 0; command argv SHA-256
  a613d10dfd08f1f641d75ff33b450ea149f2548068c5f2c454c52f4f8830a271.

- 2026-09-08T04:29:15+00:00: Recorded command exit 0; command argv SHA-256
  7801bda850e206ad701a1ab067be8d4c0930ded2684c102f016dd88599ec35a7.

- 2026-09-08T04:29:42+00:00: Recorded command exit 0; command argv SHA-256
  87d3733c7dbcba6482d99c63077993d80681429487d1fb28178b59989656077a.

- 2026-09-08T04:30:28+00:00: Recorded command exit 0; command argv SHA-256
  44b91f25e32038d1c57ad775c17b3bebdc7a2e92197d9c25a3dbc932a7687de2.

- 2026-09-08T04:31:04+00:00: Recorded command exit 0; command argv SHA-256
  0063246ff96023dbb8ebc44ebc7f5fe89f7745cd4686820ceec4ab79fbcc32a9.

- 2026-09-08T04:31:20+00:00: Recorded command exit 0; command argv SHA-256
  16a45b65981bfa4f98de7c169e8b1eaf1950e2edfa0cfaaa3e1837b64e697749.

- 2026-09-08T04:31:36+00:00: Recorded command exit 0; command argv SHA-256
  9a845769bcbe6eaf1d2d324f1ee96be0ac34028f726759f239844b21045535be.

- 2026-09-08T04:32:14+00:00: Recorded command exit 1; command argv SHA-256
  b71d40d81de2e7c7e14a7b4050927ef8acebf4fcb9cfddd4832f40a8f343f705.

- 2026-09-08T04:32:42+00:00: Recorded command exit 0; command argv SHA-256
  40f6e41434ad9095ad6004e16b6e617e1ffca1734ac98d4a639a1d9b69e63fe8.

- 2026-09-08T04:33:07+00:00: Recorded command exit 0; command argv SHA-256
  ee65662127af0bca492b404cbac9f3d64fa31a1f36bba2231afaca02564a1022.

- 2026-09-08T04:33:33+00:00: Recorded command exit 0; command argv SHA-256
  b30ab8e43a4cb1a11d68dcded7d3c68728747b862c0c82b50bc21ff351d6c20b.

- 2026-09-08T04:34:02+00:00: Recorded command exit 0; command argv SHA-256
  30aa8e3f7918cde3bdc80988d188b61f27566497500ae2c7e95b75cdec892f99.

- 2026-09-08T04:37:48+00:00: Recorded command exit 0; command argv SHA-256
  e967abb6900d82c278667522ed773901c2b64e62a0898e7254f0a638fc0590a6.

- 2026-09-08T04:38:48+00:00: Recorded command exit 0; command argv SHA-256
  01f26b344fefa555fa3badf05ffcfba0260f0c50e8e5e948e732ad9667bd6fff.

- 2026-09-08T04:41:16+00:00: Recorded command exit 0; command argv SHA-256
  deab9e9b699f6d87df8ca2ded7438689d354bfb4271b11b02e69502ddf50f7e9.

- 2026-09-08T04:41:29+00:00: Recorded command exit 0; command argv SHA-256
  3883dbef1393c0406a83e21384d1d1b0eb5f9aff04dad793aeae61ef3383e227.

- 2026-09-08T04:42:44+00:00: Recorded command exit 0; command argv SHA-256
  a6faeb61aa6a96dee3b9b7b4c001d0af93ade15546bb61876c8acec64182f02e.

- 2026-09-08T04:43:32+00:00: Recorded command exit 2; command argv SHA-256
  8ab970e8092af70133f566018d8db973255084dc64b224364430f7ea6d6e59ff.

- 2026-09-08T04:44:20+00:00: Recorded command exit 0; command argv SHA-256
  641421048d86a384ae58788b4173e6de5a61bacd804dba8773ecd89666b501a2.

- 2026-09-08T04:46:26+00:00: Recorded command exit 1; command argv SHA-256
  b9a34ebf6f7741c60effbc09bd5b6bd2086b1e5fd093662b7e3fa2860cc037f3.

- 2026-09-08T04:47:10+00:00: Recorded command exit 0; command argv SHA-256
  05843d2e65f0dd7c766c67d00120209e2371adf1f42a3271c0e03dd3eab24e16.

- 2026-09-08T04:50:46+00:00: Recorded command exit 0; command argv SHA-256
  3586b977699ac1ac5a4c022afef25ad24c7b060f990418f69d2bf3aaf63acb14.

- 2026-09-08T04:52:22+00:00: Recorded command exit 2; command argv SHA-256
  48458d4adcbc2714c4ae60f17ec39d916357031118af6e75d9a5cd826c73f20e.

- 2026-09-08T04:53:19+00:00: Recorded command exit 1; command argv SHA-256
  8cdb703d8c9c368b4e66af18e070d5f10f49be16b78891fb3b5d632d53e7d90a.

- 2026-09-08T04:54:30+00:00: Recorded command exit 1; command argv SHA-256
  4522541adb966146eb7efacf336a193e149c6f362c06281645fbc44906e699f0.

- 2026-09-08T04:55:18+00:00: Recorded command exit 0; command argv SHA-256
  7b08290d85b442aba829bc680eecf2d2df8873a8972499a462d2e7cfac67c74d.

- 2026-09-08T04:55:39+00:00: Recorded command exit 0; command argv SHA-256
  0df6d965e2ecd158db43921924c47f010f7e367bfbfd86bb358a88df157ce1eb.

- 2026-09-08T04:56:13+00:00: Recorded command exit 0; command argv SHA-256
  d9d8766f5f079643423c3e993c3ca3e723358ad762841d88db1483d97d050f26.

- 2026-09-08T04:56:58+00:00: Recorded command exit 0; command argv SHA-256
  f032e69f04fff64cacdabb2ff2f782851a491ed564e3caba0127be2218b5b277.

- 2026-09-08T04:57:24+00:00: Recorded command exit 127; command argv SHA-256
  e51dc8f1856392185c035b967defd35e8d11c0444e2e002bfc3c9bd1300cb23b.

- 2026-09-08T04:58:02+00:00: Recorded command exit 0; command argv SHA-256
  515ab6a4703966f9ae2f90c51ed59809a23c133886fea8a88d390e3a3ae41b8f.

- 2026-09-08T04:59:31+00:00: Recorded command exit 0; command argv SHA-256
  ce29f6ff24dd109973135e1a2a3af9b38248e7a8f5a10263e68db8bf0fa500f9.

- 2026-09-08T05:00:15+00:00: Changed dependency conclusion after fail-closed audit: reject SDK
  v1.45.0 because its required lmnr 0.7.62 hard-requires LicenseRef-Proprietary
  lmnr-claude-code-proxy 0.1.24. The latest upstream release family with a license-complete official
  lock is OpenHands software-agent-sdk v1.17.0: lightweight tag commit
  aabf40723d308da0d5f9063008c6793cc86df282, tree 850dd602d64b8d19560e63c2d9a4d44c48db82f4, MIT
  source, official uv.lock pinning lmnr 0.7.24 and agent-client-protocol 0.8.1. A fresh Python 3.12
  install from the locked hashed dependency export plus PyPI wheel SHA-256
  3b771e72209453871c3036a562cf33e9ad9642a54bd48edb44f89915ac54709d passed uv pip check with 120
  packages; proxy absent, metadata/license-file audit found no proprietary dependency. Source
  archive SHA-256 is 2434fe9ef7de2e7ab8e6ca5b771ec82e9a6737d8d091a2ded16b5d23c02da2a7. Exact
  environment digest is 6372756912734f6275362a8b66c3758fd2b2adeab776eb2a0be7935f34abb9b2. The first
  native probe failed only because the exploratory server expected /chat/completions while a /v1
  base correctly generated /v1/chat/completions; corrected-path native probe passed write,
  AlwaysConfirm, finish, and 20 input/8 output usage. The real Rust process-boundary fixture then
  passed in 70.82s with the exact pinned runtime. Unit 6/6, boundary 1/1, Clippy -D warnings and
  rustdoc -D warnings pass. A mistyped venv command and two initially malformed patch hunks were
  rejected without product effect; subsequent exact patches were verified. AR remains in progress;
  v1.45.0 is unsupported and unapproved distributions fail closed.

- 2026-09-08T05:02:43+00:00: Recorded command exit 0; command argv SHA-256
  fe204399f220f841bee9c39db2ae7784fe4736d9a531e274985da7e821c202c8.

- 2026-09-08T05:03:57+00:00: Recorded command exit 0; command argv SHA-256
  a38cb0c1057cdb575888f702a810a0aee77c0b40e33bde1a0400da7b666e92a9.

- 2026-09-08T05:04:48+00:00: Recorded command exit 1; command argv SHA-256
  cb2aa7be715686405a3231f74e301aa5c3ebefd1ddedbdbcd09a8c2dc8415272.

- 2026-09-08T05:05:47+00:00: Recorded command exit 0; command argv SHA-256
  a6476dc7b13f478fa0d30ad0af71d6e41a7529fd857ef614ce371e730fc98c67.

- 2026-09-08T05:06:43+00:00: Recorded command exit 0; command argv SHA-256
  3f4683d9ccc488ad3ea1e70552de805b6e96e521f2fd7995129b681fafe21276.

- 2026-09-08T05:08:54+00:00: Recorded command exit 0; command argv SHA-256
  324a5335943122eda99cdbbdc0ce6522311c0987344c38079e40f23ec59925ea.

- 2026-09-08T05:09:42+00:00: Recorded command exit 1; command argv SHA-256
  2119a2f534a88784005bcaf996219fec25f06d8ade96ad56069f7d1cc927774f.

- 2026-09-08T05:09:56+00:00: Recorded command exit 101; command argv SHA-256
  fb4b8baf40d5dd4a8518e90f3cbf47f476b8dc680bacf8835e9d4ed7ffa22ef4.

- 2026-09-08T05:10:09+00:00: Recorded command exit 101; command argv SHA-256
  73ace59d4f0fe2f69761406da10d9d0939a4b3f693e34b49bb753040bb97450d.

- 2026-09-08T05:10:23+00:00: Recorded command exit 0; command argv SHA-256
  80a5d3075befdc1606cd0a18c8984845cefc2101dfb82df3b08880f6fe592dc9.

- 2026-09-08T05:12:04+00:00: Recorded command exit 0; command argv SHA-256
  0f8c7b8bd01e6baf1abbc3c0480d6e2bf7abc45f3556b7f0857111d435c221b9.

- 2026-09-08T05:12:33+00:00: Recorded command exit 0; command argv SHA-256
  b08b7f96f8b1da52d81f9353fad460f3e5cbfa4f4479bcec46439ff2b4ca881d.

- 2026-09-08T05:13:08+00:00: Recorded command exit 0; command argv SHA-256
  b882f06b589667f76188e4ff297edb476870d8f0b85f066732f833ad17499697.

- 2026-09-08T05:14:03+00:00: Recorded command exit 0; command argv SHA-256
  ec5da320353eb97254d128366a7fb810f5ac578b4deec99a752ad317c4ead3cc.

- 2026-09-08T05:16:43+00:00: Recorded command exit 0; command argv SHA-256
  d70308cdf766954a5dde371e7a5d66477048fd5b0d4658d7aa2c0fdfbe91700d.

- 2026-09-08T05:18:05+00:00: Prepared clean signed+DCO OpenHands SDK v1.17.0 replacement candidate
  e2b312cf8fa3fcc452e1f5a708dcfe2d1c06adf1, tree 8f6f630da1b23ba27037dc70c5528ba7681fd15d, on base
  3a07b57b8265d98eeebbcd4fd21339d72fac0663. Exact four-path scope: agents lib registration,
  openhands module, v1.17 freeze, boundary test. Fail-closed license audit rejects v1.45 because
  required lmnr 0.7.62 pulls proprietary proxy; pinned v1.17 official lock uses lmnr 0.7.24 and has
  a fresh 120-package hashed install with uv pip check green, audited permissive closure, proxy
  absent, exact source/wheel/environment digests, and unapproved distributions rejected before
  spawn. Focused unit 6/6, provenance 1/1, native real process boundary repeated green with
  write/approval/terminal/20-input/8-output/cleanup/privacy evidence; workspace
  fmt/clippy/tests/docs/release, deny/audit/policy/actionlint/zizmor/Gitleaks/failure fixtures
  green. Final rustdoc -D warnings green. Coverage gate green with OpenHands 86.13% lines and
  applicable workspace/critical thresholds passing; an earlier 89.29% artifact was environmental
  because project-local rustup std sources polluted the tiny critical denominator, and rerun with
  identical toolchain outside project storage passed. Live fetch found origin/main advanced
  disjointly to d3e2dfa979d85b8b443a07f93e7dd7b9a226bc2f, so candidate is held unpublished pending
  controlled rebase authorization.

- 2026-09-08T06:35:40+00:00: Recorded command exit 0; command argv SHA-256
  cd31df240fb13ffcf25c7aa1fc6bd6546fec8fa9814e5dfc7624a6f71d7d712c.

- 2026-09-08T06:38:27+00:00: Recorded command exit 0; command argv SHA-256
  453949fab16e28b524b5e56135b3154e3176431439345657d950c143823f3ee7.

- 2026-09-08T06:39:58+00:00: Recorded command exit 0; command argv SHA-256
  e00b38d32dec923dcb15649c98610ee57ebe4d4ed39312c1043948d999c81dd0.

- 2026-09-08T06:40:44+00:00: Recorded command exit 0; command argv SHA-256
  81301e6ec667f399e75c253525f408b58aeba77b75d35c4de3df0994a073a85b.

- 2026-09-08T06:41:56+00:00: Recorded command exit 0; command argv SHA-256
  aa6d0b65b29c45354968569be943c96adac9649a5448f85786eb8c95c7db71ef.

- 2026-09-08T06:42:29+00:00: Controlled rebase completed onto exact main
  7a435fb6a4acc59300771b8478ee342f72555c96. Successor e73767d959a0c640685deaf84335be84649df7c0, tree
  116573c1d4459357bf55dc954a9f66a523b208b0; range-diff marks all four commits equal, every rewritten
  commit has a good SSH signature and exact DCO, and exact scope remains four OpenHands agent paths.
  Rebased exact-tree gates pass: fmt; OpenHands unit 6/6; provenance 1/1; workspace all-target
  Clippy -D warnings; full workspace tests including native sandbox; rustdoc -D warnings; release
  build; cargo-deny/audit; repository policy/DCO/Gitleaks; coverage gate with OpenHands 86.13%
  lines; and the real pinned v1.17 SDK boundary 1/1 in 66.40s. The combined gate product command
  completed successfully but its wrapper state-record phase once hit coordinator LOCK_TIMEOUT;
  subsequent exact records and this note preserve the outcome. An initial native invocation used a
  nonexistent exact filter and selected zero tests; it was immediately replaced by the correct exact
  ignored test, which passed. Worktree is clean; no blocker remains beyond immutable review.

- 2026-09-08T06:43:38+00:00: Publication preflight stopped before mutation: local candidate remains
  clean exact e73767d959a0c640685deaf84335be84649df7c0, remote feature branch absent, and no
  existing PR. However product origin/main advanced after immutable review from approved base
  7a435fb6a4acc59300771b8478ee342f72555c96 to signed merge 123c58f7a971f210873124fccb31daa16139aab4
  (executable offline guides; README, CLI guide test, docs only). No branch push or PR creation
  occurred.

- 2026-09-08T06:44:15+00:00: Recorded command exit 0; command argv SHA-256
  d7b077b03cca6c2e046808e88c4a480c198252e8e1746a40ba94c28355944142.

- 2026-09-08T06:45:24+00:00: Recorded command exit 101; command argv SHA-256
  6d28612af604fac613f24aebc8ac7a4a6755535ced770ee8827013a739bd400d.
