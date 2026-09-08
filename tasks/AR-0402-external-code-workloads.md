---
{
  "branch": "feature/external-code-workloads",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-08T10:51:24+00:00",
  "depends_on": [
    "AR-0401"
  ],
  "id": "AR-0402",
  "next_action": "Define content-addressed external source manifests for SWE-bench 02e7a74ffd0b707aab73d203fe87bdc7c76afc8e and Polyglot 7e0611e77b54e2dea774cdc0aa00cf9f7ed6144f; include Exercism cpp 413b80a9, go 97472cfe, java f1b22a3d, javascript 9be84b9e, python 1f6aab86, rust 1d3a0f46 (all MIT), then pin evaluator/image metadata.",
  "observed_branch": "feature/external-code-workloads",
  "observed_dirty": 0,
  "observed_head": "123c58f7a971f210873124fccb31daa16139aab4",
  "owner": "root-coordination-20260906",
  "plan": "../plans/AR-0402.md",
  "priority": "P2",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Add versioned external workload adapters without vendoring datasets.",
  "task_revision": 23,
  "title": "Integrate SWE-bench and Aider Polyglot",
  "updated_at": "2026-09-08T08:54:19+00:00",
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
