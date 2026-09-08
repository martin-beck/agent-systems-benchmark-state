---
{
  "branch": "feature/external-code-workloads",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-0401"
  ],
  "id": "AR-0402",
  "next_action": "Add digest verification/acquisition boundary and oracle fixtures, then run Rust/full quality gates.",
  "observed_branch": "feature/external-code-workloads",
  "observed_dirty": 0,
  "observed_head": "aa021eb5272bb7ca45100f2f1d6166ec61744ec8",
  "owner": "",
  "plan": "../plans/AR-0402.md",
  "priority": "P2",
  "schema_version": 1,
  "status": "open",
  "summary": "Add versioned external workload adapters without vendoring datasets.",
  "task_revision": 46,
  "title": "Integrate SWE-bench and Aider Polyglot",
  "updated_at": "2026-09-08T11:59:37+00:00",
  "worktree_key": "agent-systems-benchmark-external-code-workloads"
}
---
## AR-0402

Add versioned external workload adapters without vendoring datasets.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-08T06:53:20+00:00: Dependency AR-0401 verified done; promoted as highest-priority
  compatible ready workload integration after AR-0840 completion.

- 2026-09-08T06:53:25+00:00: Claimed by root-coordination-20260906.

- 2026-09-08T06:53:52+00:00: Recorded command exit 0; command argv SHA-256
  7274b403d710b7d3e396baf17d5bb8f14ad3b1b0e57b2e1e1f0449417f21d260.

- 2026-09-08T06:54:35+00:00: Recorded command exit 0; command argv SHA-256
  8c1c04f6486cf30a6690ab624b0e73b89d40fe7c7f919fbb2f14c062d356c371.

- 2026-09-08T08:32:39+00:00: Recorded command exit 1; command argv SHA-256
  fe8ff2299bb36cc895ef3dd0228ca8659c306b5a24b8cc4bc527990089f8ca3b.

- 2026-09-08T08:32:59+00:00: Recorded command exit 0; command argv SHA-256
  37823ad69b6e6ec4e62a87d7f0b28bcc3bdf70c888b34485acb900649598f0b2.

- 2026-09-08T08:33:11+00:00: Recorded command exit 0; command argv SHA-256
  3fd3bc82bcabf433c605d0717f8b3944583520cc30b9eac636828283d3743aed.

- 2026-09-08T08:38:08+00:00: Recorded command exit 0; command argv SHA-256
  fe568772bdb2f36015ea4d43040686bcb88795e0f5f945a1d305c4030f18353b.

- 2026-09-08T08:38:19+00:00: Fresh official API audit recorded SWE-bench immutable main and MIT
  metadata; Aider Polyglot immutable main is 7e0611e77b54e2dea774cdc0aa00cf9f7ed6144f but repository
  API reports no SPDX license, so adoption is held pending explicit license inspection. No product
  files changed.

- 2026-09-08T08:38:47+00:00: Recorded command exit 0; command argv SHA-256
  b53816b1079217465ce64670b216856415841404399c34dc68b2c7933595383f.

- 2026-09-08T08:39:01+00:00: Recorded command exit 0; command argv SHA-256
  fa545d7d5999a7d4d4842001a285abf86db901d4b5032e860fc0254219f5f6bd.

- 2026-09-08T08:39:10+00:00: Audited pinned README and tree: Polyglot has no repository SPDX
  license, explicitly attributes exercises to six Exercism tracks and says their individual licenses
  govern; adoption must preserve per-exercise attribution/licenses. SWE-bench root LICENSE is MIT.
  No product files changed.

- 2026-09-08T08:41:28+00:00: Recorded command exit 0; command argv SHA-256
  9512e30f4d0a1f2677b2cdcaf766534569d7fe197a99c2a05d9c4a199d8dde62.

- 2026-09-08T08:43:57+00:00: Recorded command exit 0; command argv SHA-256
  9c128dd8e7f3b6c5554ba8c45cfdc5b8904bd153e2456c36b633e5d68ecd6d53.

- 2026-09-08T08:44:09+00:00: Fresh official API audit pinned all six Exercism source repositories
  and found MIT SPDX metadata for each. No source content or datasets were copied; product
  implementation remains pending manifest design and evaluator/image provenance.

- 2026-09-08T08:50:55+00:00: Recorded command exit 0; command argv SHA-256
  e90773ea7ff6a8bdec37246f48ded8d0fd80dd341641f933c33f7cbb83624847.

- 2026-09-08T08:51:10+00:00: Recorded command exit 0; command argv SHA-256
  db3e66c495045099904cfd2e3562b61769de0710fa1938e6b3a73eb4ab371a34.

- 2026-09-08T08:51:24+00:00: Heartbeat by root-coordination-20260906.

- 2026-09-08T08:52:58+00:00: Recorded command exit 2; command argv SHA-256
  48458d4adcbc2714c4ae60f17ec39d916357031118af6e75d9a5cd826c73f20e.

- 2026-09-08T08:53:49+00:00: Recorded command exit 1; command argv SHA-256
  68442886cbedf5f375b3aa46b980d8f1f5d7e97f2e043fbe09e654f594b48bc8.

- 2026-09-08T08:54:19+00:00: Recorded command exit 0; command argv SHA-256
  3c51ce1b7503f71621a56ae302865d720be923387bb300380e953be9bd6638e5.

- 2026-09-08T08:54:39+00:00: Recorded command exit 0; command argv SHA-256
  1f7eecd1225232ce75188640fcd9a33cae6a4d3cab33344712606dac27d8acf1.

- 2026-09-08T09:01:28+00:00: Recorded command exit 0; command argv SHA-256
  9879caf01553413e7c91b54e64ae84a5408825f03d851af58613705efc92257d.

- 2026-09-08T09:01:44+00:00: Recorded command exit 0; command argv SHA-256
  292e17f91fc5eff08ce89e4d68c8eacae2ea4586330496a757ca0554a27dee90.

- 2026-09-08T09:26:33+00:00: Recorded command exit 0; command argv SHA-256
  dbce2d3a55dc7ee01e742c34a7d8c57a551ce2bae1a6a9962b8486d4660b14e1.

- 2026-09-08T09:43:45+00:00: Recorded command exit 0; command argv SHA-256
  c6d91569cb0ce4f520e68d629c505064f6f0a4e7ce235c05599bc164ef9895c2.

- 2026-09-08T09:57:39+00:00: Heartbeat by root-coordination-20260906.

- 2026-09-08T10:04:37+00:00: Recorded command exit 0; command argv SHA-256
  293f02809b4a0545a8b524e8911da9ec5102c197221af8499a87f437f12af3e6.

- 2026-09-08T10:05:37+00:00: Recorded command exit 0; command argv SHA-256
  3c586e578c4b4cefd2a56fafe71170dcc09f13e9b5cb1bb0aaa5fe44ae9d6e88.

- 2026-09-08T10:07:07+00:00: Recorded command exit 0; command argv SHA-256
  816f62d643e01c272b89cf2b45ec4f345c120a9695dc2530542d54d3ca455f06.

- 2026-09-08T10:26:19+00:00: Recorded command exit 0; command argv SHA-256
  77d2335159f7f55cd44897367caab6b28013451773df992d0541f247cb34777c.

- 2026-09-08T11:24:44+00:00: Recorded command exit 0; command argv SHA-256
  bb15374414a45bae02857e1c4d9f0057527d987beac673bb69a3aa971378d1e3.

- 2026-09-08T11:25:00+00:00: Recorded command exit 0; command argv SHA-256
  a7a2382ca77d568f46a5a3ed0cc30d1460da42105ddfa5f821b3771de116b680.

- 2026-09-08T11:25:18+00:00: Implemented external workload provenance registry and non-vendoring
  contract at product commit aa021eb5272bb7ca45100f2f1d6166ec61744ec8; added pinned SWE-bench, Aider
  Polyglot, and six Exercism track source identities, explicit license/platform limitations, and
  registry test (pytest 1/1). Evaluator image digests remain null, so suites remain planned and
  unqualified.

- 2026-09-08T11:25:28+00:00: Recorded command exit 127; command argv SHA-256
  8b918589c9a5abf78f4afb7db1ae341a6c56f607621cccdae67b1c4da43134f7.

- 2026-09-08T11:47:54+00:00: Recorded command exit 0; command argv SHA-256
  e01e02f554f2ce46d617f172a3c037236ae564e3adcad6550869f808d4255bf8.

- 2026-09-08T11:49:01+00:00: Recorded command exit 0; command argv SHA-256
  24d6a10ef448ba1e095ef695d14ca93cdb8919492e09c66a3acb38a908c191bc.

- 2026-09-08T11:49:12+00:00: Recorded command exit 0; command argv SHA-256
  6a9b73829da5e30965c14608c2654810adcbab5bd6a158f647fb98fa6376fc65.

- 2026-09-08T11:53:51+00:00: Recorded command exit 0; command argv SHA-256
  d48fb946d8a9ce16d9b44e11e08d2652de321aa829270821979b58fd7ff07424.

- 2026-09-08T11:54:05+00:00: Recorded command exit 0; command argv SHA-256
  6a9b73829da5e30965c14608c2654810adcbab5bd6a158f647fb98fa6376fc65.

- 2026-09-08T11:54:15+00:00: Recorded command exit 0; command argv SHA-256
  7120abf6e3927d0cdedeb0cd3f91b0588f7425e8ec544de15c1db999f3b35ddd.

- 2026-09-08T11:59:37+00:00: Lease expired during coordinated merge/CI repair; durable effects
  audited, worktree clean, no overlap. Reopen for explicit re-claim.
