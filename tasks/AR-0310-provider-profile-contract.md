---
{
  "branch": "feature/provider-profile-contract",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-06T23:07:51+00:00",
  "depends_on": [
    "AR-0101",
    "AR-1001"
  ],
  "id": "AR-0310",
  "next_action": "Await AR-0401 fence transfer, then wire provider module, schemas, fixtures, adapter interface, and full gates.",
  "observed_branch": "feature/provider-profile-contract",
  "observed_dirty": 0,
  "observed_head": "b3868b47b33023bc5fadbabc6d14ca59919ea118",
  "owner": "quality-20260906",
  "plan": "../plans/AR-0310.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Normalize one provider configuration for safe translation across heterogeneous agent adapters.",
  "task_revision": 33,
  "title": "Define common provider profiles",
  "updated_at": "2026-09-06T21:50:26+00:00",
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
