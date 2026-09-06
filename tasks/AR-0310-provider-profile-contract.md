---
{
  "branch": "feature/provider-profile-contract",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-07T00:59:17+00:00",
  "depends_on": [
    "AR-0101",
    "AR-1001"
  ],
  "id": "AR-0310",
  "next_action": "Await AR-0401 fence transfer, then wire provider module, schemas, fixtures, adapter interface, and full gates.",
  "observed_branch": "feature/provider-profile-contract",
  "observed_dirty": 16,
  "observed_head": "ff2aaa913545763acd036e0f040e13377f8636b9",
  "owner": "quality-20260906",
  "plan": "../plans/AR-0310.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Normalize one provider configuration for safe translation across heterogeneous agent adapters.",
  "task_revision": 93,
  "title": "Define common provider profiles",
  "updated_at": "2026-09-06T23:29:17+00:00",
  "worktree_key": "agent-systems-benchmark-provider-profile-contract"
}
---
## AR-0310

Normalize one provider configuration for safe translation across heterogeneous agent adapters.

Profiles contain no credentials. Every adapter must negotiate which normalized fields it can honor
exactly and fail closed on unsupported or lossy translations.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-06T21:33:37+00:00: Dependencies AR-0101 and AR-1001 are durably done; promote the
  credential-free provider contract for isolated implementation under the coordinator Cargo/schema
  fence.

- 2026-09-06T21:33:39+00:00: Claimed by quality-20260906.

- 2026-09-06T21:37:38+00:00: Recorded command exit 0; command argv SHA-256
  f83a5eebd861223334c6a87ec97e8efc27c408440b71a39ccee6d585c599d2f8.

- 2026-09-06T21:37:51+00:00: Heartbeat by quality-20260906.

- 2026-09-06T21:41:17+00:00: Recorded command exit 2; command argv SHA-256
  48458d4adcbc2714c4ae60f17ec39d916357031118af6e75d9a5cd826c73f20e.

- 2026-09-06T21:43:31+00:00: Recorded command exit 0; command argv SHA-256
  fdecd0af6596065fdfeac5d3df1d362d2773cde8817fb0ebd96a5e749a0eac4e.

- 2026-09-06T21:43:45+00:00: Recorded command exit 0; command argv SHA-256
  788bf3e8b263ae9546e56ed516b8146e8390addf38f8156e6431f43e16f21c8b.

- 2026-09-06T21:43:57+00:00: Recorded command exit 0; command argv SHA-256
  ba989f0238d4def9c81d240ddf654a4a73e1f9e0d5699ac95248768237a9e485.

- 2026-09-06T21:44:14+00:00: Recorded command exit 0; command argv SHA-256
  976bdce1d6c40cf0782b4988fe1fc21842c1c4e6e08db82db9e5c7ac0b1bc718.

- 2026-09-06T21:44:25+00:00: Recorded command exit 1; command argv SHA-256
  03fb460f22751258c2e5dcda15414dad3b327e2a3b6ef665086066fef34a71b9.

- 2026-09-06T21:44:49+00:00: Recorded command exit 101; command argv SHA-256
  a2240ab8182fe2cd1714abbe3a7bfe42234aab0909ea75886ad90889cb50f402.

- 2026-09-06T21:45:10+00:00: Recorded command exit 0; command argv SHA-256
  5119a1977ecb6c5e609911b11b91157564d1b67b021f1d78cf9d3299adde291b.

- 2026-09-06T21:45:29+00:00: Recorded command exit 0; command argv SHA-256
  7a2c3b8f5f4a68db08677a2c93ce255bc9aa4c56081f7febb1cef28d80b601e7.

- 2026-09-06T21:45:38+00:00: Recorded command exit 101; command argv SHA-256
  eefcb8df6110ce9c444bd3194af9a10cf84815ad8fa6395c4d7ad3e01929c5e5.

- 2026-09-06T21:46:14+00:00: Recorded command exit 0; command argv SHA-256
  fcae3edb32ad9920cba221a23c99c1fcd76af63dfe036d9eb465d44a31041dc1.

- 2026-09-06T21:46:33+00:00: Recorded command exit 0; command argv SHA-256
  48afbae084b266771dd85b52a2c048175c7357c15ebeb3bdc6d69d649ae9dd43.

- 2026-09-06T21:46:53+00:00: Recorded command exit 1; command argv SHA-256
  88b3feb77070a7c5b158a9e9b4dc5d2d24165c43b3ee46a184dbad9527fb5b52.

- 2026-09-06T21:47:20+00:00: Recorded command exit 0; command argv SHA-256
  e513d67da82d245a1a53a56c311a2c68f2d2769bde6c499b7619acf3ab7e88c1.

- 2026-09-06T21:47:32+00:00: Recorded command exit 0; command argv SHA-256
  88b3feb77070a7c5b158a9e9b4dc5d2d24165c43b3ee46a184dbad9527fb5b52.

- 2026-09-06T21:48:03+00:00: Recorded command exit 101; command argv SHA-256
  a1d89a9e5e282d7ab9b3937101d86c89f4648225ab5a82b931ab1f3d9915a31d.

- 2026-09-06T21:48:20+00:00: Recorded command exit 0; command argv SHA-256
  af548e158e179e12034a268f0a2d46f4fbb82783e4fef9cdaabdd35e8e154c31.

- 2026-09-06T21:48:31+00:00: Recorded command exit 0; command argv SHA-256
  bace997cd80ab6e5afac9e75c95806b4da375e754c9d8ef89a084ce49ea3de66.

- 2026-09-06T21:49:01+00:00: Recorded command exit 0; command argv SHA-256
  b46ed02433bee977b4106003b028da45e4a7cc69d54e9c76a756aafa3cb29a39.

- 2026-09-06T21:49:16+00:00: Recorded command exit 0; command argv SHA-256
  a65ed4c8baa6fae6bb468c622c6186ea30ded3aac7fc35377cf78e4905917dc1.

- 2026-09-06T21:49:31+00:00: Recorded command exit 0; command argv SHA-256
  45aa11970a1900e1fde4cf2a890d41a44980be0bb6d371763e2d9bf19d7cd23e.

- 2026-09-06T21:49:42+00:00: Recorded command exit 0; command argv SHA-256
  af548e158e179e12034a268f0a2d46f4fbb82783e4fef9cdaabdd35e8e154c31.

- 2026-09-06T21:50:06+00:00: Isolated provider contract added without touching the AR-0401-fenced
  Cargo/workspace/schema/fixture/adapter paths. Strict missing-docs compile, 7 unit tests, and
  clippy -D warnings pass in an external same-drive harness; llvm-cov reports 97.57% regions, 99.59%
  lines, 100% functions. Stable rustc cannot emit branch coverage because cargo-llvm-cov --branch
  requires nightly; failure was recorded, and branch-aware full coverage remains an integration
  gate. Initial fmt and missing scratch lock failures were corrected.

- 2026-09-06T21:50:16+00:00: Recorded command exit 0; command argv SHA-256
  0ecf1b6b7e7ee0c26c650f94d85c87ea12a7356653c9fbd4df516c4f21947e16.

- 2026-09-06T21:50:26+00:00: Recorded command exit 0; command argv SHA-256
  51578da570badc3d136f1236b6f1b5a4f877434595118e5a5627d4672641b2bd.

- 2026-09-06T21:51:11+00:00: Recorded command exit 0; command argv SHA-256
  02f3112a451e1aee701fa2185600d4db027cb3532f8a9158d0fcfcaf81b3ef7a.

- 2026-09-06T21:51:27+00:00: Recorded command exit 0; command argv SHA-256
  45aa11970a1900e1fde4cf2a890d41a44980be0bb6d371763e2d9bf19d7cd23e.

- 2026-09-06T21:51:37+00:00: Recorded command exit 0; command argv SHA-256
  708b35dbaf9aed5a0e3e07ec3dab5251b6a85cfffb75d0322559fa53c1c024f6.

- 2026-09-06T21:52:13+00:00: Recorded command exit 0; command argv SHA-256
  a3e7cb62702c637e9e5f7f9edab896f07535d9623e93259d7cdeb076cfea1fa1.

- 2026-09-06T21:52:26+00:00: Recorded command exit 0; command argv SHA-256
  90c9e613389021e0e870447c41089d1cccff2c85a4373bc49a5b62cfee5c0345.

- 2026-09-06T21:52:39+00:00: Recorded command exit 101; command argv SHA-256
  9812f78569aae114fc653cc10d4a5064c9e6bd3519667a9467dc8b393df11bbb.

- 2026-09-06T21:53:16+00:00: Recorded command exit 0; command argv SHA-256
  db791d5b5cde74ac73847f663664ed300fc8d16dcd29c85cfdb0a523b9792f32.

- 2026-09-06T21:53:32+00:00: Recorded command exit 0; command argv SHA-256
  f79143f6fb428896bb63739f19cfbef1edbcdb1d81623094fe7b862f514148ee.

- 2026-09-06T21:53:46+00:00: Recorded command exit 0; command argv SHA-256
  d3193aaf39cdbc7f6c78dd3ea0ed4ae29f6ec9de299bc211d9e0bc2c02427ecb.

- 2026-09-06T21:56:11+00:00: Independent Python golden-vector attempt first used a literal
  backslash-zero domain separator and correctly disagreed with Rust. Recomputed with an actual NUL
  byte via bytes([0]); Python and Rust now agree on
  3ef77e8fcc34900d8cece0e1bccf3bb3b23cb389669ca6eb857853be93612ae5. Signed DCO checkpoint range
  b3868b4..b8114d1 is clean; credential-source capability gap found in self-review is closed.

- 2026-09-06T21:57:19+00:00: Recorded command exit 0; command argv SHA-256
  cec080bc7ae8d562c638872d92e21033c67e7458cf7e5d1b2049d76172da7c6e.

- 2026-09-06T21:57:35+00:00: Recorded command exit 0; command argv SHA-256
  45aa11970a1900e1fde4cf2a890d41a44980be0bb6d371763e2d9bf19d7cd23e.

- 2026-09-06T21:57:50+00:00: Recorded command exit 0; command argv SHA-256
  a9baf5676fb4beabfd5cf80483e4e5ba9f193a2af79672401a21ab69c019c890.

- 2026-09-06T21:58:06+00:00: Recorded command exit 0; command argv SHA-256
  75dc8de30d8e6bfc4d5054b0c402876d405b6cb0b3aa358953372ae02c7c1c30.

- 2026-09-06T21:58:30+00:00: Recorded command exit 101; command argv SHA-256
  bdd933d74b6161f9c28f4d868eb786dcf0dca0daa9736995000f487b2c775eef.

- 2026-09-06T21:58:56+00:00: Recorded command exit 0; command argv SHA-256
  1f965baa2ce1e716b8ce823f964c44740275d719ded4999644e1e8f0009e6fd5.

- 2026-09-06T21:59:07+00:00: Recorded command exit 0; command argv SHA-256
  68dea35caeef5019ba02c621fb8516f85c9bca03153d1f78ad93ae786276dd9d.

- 2026-09-06T21:59:19+00:00: Recorded command exit 101; command argv SHA-256
  6f391f02f37470bd46c1b53f6115e7d03f53616c37215dfef4ea644bf0ac5140.

- 2026-09-06T21:59:44+00:00: Recorded command exit 0; command argv SHA-256
  d538d0ec8f782fc4e4f2de71c56c2b2db962e21fcaebd485855a484e0d9da482.

- 2026-09-06T22:00:05+00:00: Recorded command exit 0; command argv SHA-256
  45aa11970a1900e1fde4cf2a890d41a44980be0bb6d371763e2d9bf19d7cd23e.

- 2026-09-06T22:00:18+00:00: Recorded command exit 0; command argv SHA-256
  6e8c4ae5b6fa16ca0f484dd587514b7065f73c74c7780e7bd8c4396d034cb0ed.

- 2026-09-06T22:00:36+00:00: Recorded command exit 0; command argv SHA-256
  af548e158e179e12034a268f0a2d46f4fbb82783e4fef9cdaabdd35e8e154c31.

- 2026-09-06T22:00:47+00:00: Heartbeat by quality-20260906.

- 2026-09-06T22:02:14+00:00: Recorded command exit 0; command argv SHA-256
  2668481def98b52c999b1650cff4e9baeafe8d05e8ec8833dac7ba33763fbf41.

- 2026-09-06T22:02:30+00:00: Recorded command exit 0; command argv SHA-256
  99d4724f0211faf156e0ab5e1b6fd32d40b579bdaba6d64a69cfaa9304a3b2c7.

- 2026-09-06T22:13:46+00:00: Process-boundary failure: a read-only remote-main check invoked git
  fetch outside the required handoffctl run wrapper. Audit immediately showed origin/main and local
  main both remained b7e9078, owned HEAD ef4d3d8 stayed clean, and origin/main reflog did not
  advance; only transient FETCH_HEAD may have refreshed. No product ref/tree/worktree mutation
  occurred. All future Git commands, including fetch, remain wrapper-bound.

- 2026-09-06T22:51:07+00:00: Heartbeat by quality-20260906.

- 2026-09-06T23:17:11+00:00: Recorded command exit 0; command argv SHA-256
  321c534968b9c456a64caf5e6d09b63780c507f97548057d2bfe31edcfd73ff4.

- 2026-09-06T23:17:15+00:00: Recorded command exit 0; command argv SHA-256
  ff6d1fa7a7185010f75fcfafe4bdc1bdd5b9804d8c2b3e7abdd8a1b96cd81c63.

- 2026-09-06T23:17:24+00:00: Recorded command exit 0; command argv SHA-256
  c5eccc3d1afed1e6c68b3d8252fcde0a62c5de59707b7ce3eef97e992da3b50c.

- 2026-09-06T23:17:33+00:00: Recorded command exit 0; command argv SHA-256
  57a866ad036c2447041fde85a6301e927078433a5cd4bd0e85acb57c892d977c.

- 2026-09-06T23:17:46+00:00: Recorded command exit 0; command argv SHA-256
  b4d94f9b619437c6f71c56fe4b19ecf3c4cbd818e088d7ff2f1dfba27d792c44.

- 2026-09-06T23:17:58+00:00: Recorded command exit 0; command argv SHA-256
  6d0672dd720be9fd380ae9a56f0ec5d360f750047b50a4590bd50fa711d640d7.

- 2026-09-06T23:18:03+00:00: Recorded command exit 0; command argv SHA-256
  ff6d1fa7a7185010f75fcfafe4bdc1bdd5b9804d8c2b3e7abdd8a1b96cd81c63.

- 2026-09-06T23:18:08+00:00: Recorded command exit 0; command argv SHA-256
  d53bb4d91f518f8dbd46e3d9e2a8e128b1ebe6b1fb397684a02a0efa85398124.

- 2026-09-06T23:22:33+00:00: Recorded command exit 0; command argv SHA-256
  7f2cab7742868adf0c241a8508cc6dd5eb323d7b8abfeba2cf2556ae229d47e9.

- 2026-09-06T23:23:30+00:00: Recorded command exit 0; command argv SHA-256
  69949db07350e9a718670ca1c05693206fe4808c283a56bdaeee4ae4177e8b2f.

- 2026-09-06T23:24:45+00:00: Recorded command exit 0; command argv SHA-256
  51e49a84069dc9f2d10ba775f5430601e1475f92c25c07663246d54fd31fb142.

- 2026-09-06T23:25:44+00:00: Recorded command exit 1; command argv SHA-256
  58180c4febd24253fd0ef6ba9c5271dd9a3f56b01069e8f8e5017aca80c68e17.

- 2026-09-06T23:26:33+00:00: Recorded command exit 0; command argv SHA-256
  2b61603638d645e8ff3ae3e8c0009414fa003f0c68ba1bf6e333b79de04f59a6.

- 2026-09-06T23:27:34+00:00: Recorded command exit 0; command argv SHA-256
  259c7b4bc549f407b3cba1cad9db382ef57891b850d7c63255a2f7b9b9084652.

- 2026-09-06T23:27:46+00:00: Recorded command exit 0; command argv SHA-256
  79da272f7e4e7a786ca90e5ea99a1b051339fd1ac5cd8d61b67c8ebfbc695ad8.

- 2026-09-06T23:28:24+00:00: Recorded command exit 0; command argv SHA-256
  e4f935e3a0fb455ba101fd1fdf9e4c25a40e78234e32c519cc35cfd759aebc91.

- 2026-09-06T23:28:52+00:00: Recorded command exit 0; command argv SHA-256
  d4c8d08df0d20d2d4bc9c6b21a784bf5657fea50e28ce7ec24532af779f355f6.

- 2026-09-06T23:28:56+00:00: Recorded command exit 0; command argv SHA-256
  811b8abc9ae364f78822ceb030b20f6dae5dc9795c55bafef015b7ba173bc7d0.

- 2026-09-06T23:29:17+00:00: Heartbeat by quality-20260906.
