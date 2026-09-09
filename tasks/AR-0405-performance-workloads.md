---
{
  "branch": "feature/performance-workloads",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-09T04:28:46+00:00",
  "depends_on": [
    "AR-0401",
    "AR-0601",
    "AR-1002",
    "AR-1007"
  ],
  "id": "AR-0405",
  "next_action": "Audit the six-path fail-closed provenance checkpoint, run the complete applicable quality/privacy gates, and determine whether any suite can advance beyond planned without missing license and native paired-oracle evidence.",
  "observed_branch": "feature/performance-workloads",
  "observed_dirty": 0,
  "observed_head": "0f303b3ec1798906a8ecb37652e080046fd42eee",
  "owner": "replay_20260909",
  "plan": "../plans/AR-0405.md",
  "priority": "P2",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Assess SWE-Perf, SWE-fficiency and CORE-Bench for correctness-preserving optimization and reproducibility.",
  "task_revision": 51,
  "title": "Add performance and reproducibility workloads",
  "updated_at": "2026-09-09T02:28:58+00:00",
  "worktree_key": "agent-systems-benchmark-performance-workloads"
}
---
## AR-0405

Assess SWE-Perf, SWE-fficiency and CORE-Bench for correctness-preserving optimization and reproducibility.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-08T21:06:46+00:00: Dependencies AR-0401, AR-0601, AR-1002, and AR-1007 are durably done.
  Selected as the highest-priority compatible unclaimed leaf after AR-0869 was concurrently claimed:
  P1 AR-0819 overlaps active AR-0806 frontend paths, AR-0832 lacks plan-required
  AR-0703/native-isolation capacity, and AR-0704 lacks explicit provider/account/cost authorization.
  AR-0405 owns isolated asb-workloads performance/reproducibility plugin paths; shared Cargo/schema
  changes remain separately fenced.

- 2026-09-08T21:06:49+00:00: Claimed by contracts_20260906.

- 2026-09-08T21:38:26+00:00: Recorded command exit 0; command argv SHA-256
  7d538c03358de61b5bffffd97f01190afc2e69175ea45f97ada177734453e82a.

- 2026-09-08T21:41:55+00:00: Recorded command exit 0; command argv SHA-256
  8ed5d33113c9938b3ea588958844e2f701613b10dd15eeda7bf2e6ae3c9c0c67.

- 2026-09-08T21:45:35+00:00: Recorded command exit 0; command argv SHA-256
  e9a90e835f854182aa6ec1de3c27c13064b7beacd0beaf7ba3d1b2c315edf8bd.

- 2026-09-08T21:46:05+00:00: Recorded command exit 1; command argv SHA-256
  d8a8031fe2565c30bb123323ae03c106e9903803f0028023767ef1a8bfa2257d.

- 2026-09-08T21:46:48+00:00: Recorded command exit 0; command argv SHA-256
  8a09ca1edbfc6d293546082d9c70fd3d2ab91aa2d7804df2c74487a54876d4e4.

- 2026-09-08T21:47:13+00:00: Recorded command exit 0; command argv SHA-256
  d8a8031fe2565c30bb123323ae03c106e9903803f0028023767ef1a8bfa2257d.

- 2026-09-08T21:47:43+00:00: Recorded command exit 1; command argv SHA-256
  37ef758e03fca3f14cd5dde7222f256afd337d93e6730e180942b12083030927.

- 2026-09-08T21:48:13+00:00: Recorded command exit 0; command argv SHA-256
  0bdd0cbf88dc6b192fc6b3eb70b8e67a2a8b89381cc5df9b4470176b9964c809.

- 2026-09-08T21:48:33+00:00: Recorded command exit 0; command argv SHA-256
  aedca27882b56568314a8f22652fde8eb8637ec4f5a3cb387cc9299bfe23c70c.

- 2026-09-08T21:49:14+00:00: Substantive signed+DCO checkpoint
  5294c471425d75ef10759d766a296c0c3d841eab (tree fbeb6e45bcb2576203947c55e959d42c3ad10bd9, parent
  exact main 559fbcc825234bb98a64ba554a53f38b004d24f6) adds provenance-only SWE-Perf, SWE-fficiency,
  and CORE-Bench records plus exact validation and planner negatives in six owned workload paths.
  Source archives are pinned by commit/SHA-256; dataset revisions are pinned separately.
  Compatibility remains fail-closed: SWE-Perf source has no license file, SWE-fficiency dataset
  declares no license, and the recommended archived HAL evaluator for CORE-Bench has no license; no
  suite has evaluator image/SBOM, paired native trials, uncertainty, controlled hardware, or
  oracle-parity evidence. The planner rejects all three as unqualified. Focused JSON validation,
  registry digest, Ruff check/format, pytest 12/12, three planner negatives, and diff-check pass.
  Initial 5-test failure was test-order coupling to Terminal-Bench as the final array item;
  corrected to stable ID lookup and rerun green. No dataset was downloaded or executed and no
  support/native claim is made.

- 2026-09-08T21:51:50+00:00: Recorded command exit 0; command argv SHA-256
  8f4dc5a3ba13b1ba2a686992c290a65e8e45e23ea7f02cc07b1e0da35c5688bd.

- 2026-09-08T21:52:24+00:00: Recorded command exit 0; command argv SHA-256
  574f0c8e1bde59cfe1231e22bb0a6fb24cfa2b63228bb1722f745e295e8b3e57.

- 2026-09-08T23:02:26+00:00: Recorded command exit 2; command argv SHA-256
  48458d4adcbc2714c4ae60f17ec39d916357031118af6e75d9a5cd826c73f20e.

- 2026-09-08T23:05:08+00:00: Recorded command exit 0; command argv SHA-256
  4e03eb7780eb5ee632ca6bddd2b14ce9594395a6a259cab3d5873bf554055046.

- 2026-09-08T23:05:38+00:00: Recorded command exit 0; command argv SHA-256
  1c00e6e83119b8aeb3abb95c65102437c4e261c2e4d0b3e51e0a7abc88b3c00f.

- 2026-09-08T23:05:49+00:00: Recorded command exit 0; command argv SHA-256
  367360d8844444a4c39e48dbeb958d13dbd6ffd0e4b25ece4a2330a97e984e7a.

- 2026-09-08T23:06:26+00:00: Recorded command exit 0; command argv SHA-256
  4f759e59c77fad7e9c58bdbf5c225c4d79f659aafeeae8e700e39a424f2b0a65.

- 2026-09-08T23:06:36+00:00: Recorded command exit 0; command argv SHA-256
  a27c4169431a4c66f1d1da0fe11ea0829742549cca9064ccc980ba7300b5eeca.

- 2026-09-08T23:06:44+00:00: Recorded command exit 1; command argv SHA-256
  da1371343dc579096f456193c9fd415313933b3137bf26e19dd0176e42e5b66b.

- 2026-09-08T23:07:18+00:00: Recorded command exit 0; command argv SHA-256
  2d0688eccda42904981826536a42f78aba74cfeb8918274d17c44127b4c47bdd.

- 2026-09-08T23:07:28+00:00: Recorded command exit 0; command argv SHA-256
  73f9955b98d559c2b06ace66138b995891af97bf31e3ccac58358f49ca9f9a2e.

- 2026-09-08T23:07:36+00:00: Recorded command exit 0; command argv SHA-256
  2a5f18a018eac4703aa065a1484ea3190893d02da0a4a6cf358510cff78afa0c.

- 2026-09-08T23:07:47+00:00: Recorded command exit 0; command argv SHA-256
  7b93352e51f78dc4ed72a795d29c5e89d5aa8e4c9befb79add0f6ea85c2404d5.

- 2026-09-08T23:07:59+00:00: Recorded command exit 0; command argv SHA-256
  854044105d96dfd3261a3910fb75635b09691f8eabbc07389318bf0936e4caf5.

- 2026-09-08T23:08:08+00:00: Recorded command exit 0; command argv SHA-256
  7b93352e51f78dc4ed72a795d29c5e89d5aa8e4c9befb79add0f6ea85c2404d5.

- 2026-09-08T23:08:32+00:00: Recorded command exit 0; command argv SHA-256
  854044105d96dfd3261a3910fb75635b09691f8eabbc07389318bf0936e4caf5.

- 2026-09-08T23:08:40+00:00: Recorded command exit 0; command argv SHA-256
  854044105d96dfd3261a3910fb75635b09691f8eabbc07389318bf0936e4caf5.

- 2026-09-09T00:07:52+00:00: Recovered expired claim formerly owned by contracts_20260906. Lease
  expired at 2026-09-09T00:06:49Z; no active owner process found, declared worktree is clean at
  5294c471; preserving worktree and returning task to open for future claim.

- 2026-09-09T02:25:45+00:00: Claimed by replay_20260909.

- 2026-09-09T02:25:48+00:00: Heartbeat by replay_20260909.

- 2026-09-09T02:26:11+00:00: Recorded command exit 0; command argv SHA-256
  76155e7da7be1f5f2cf10e28f84fd412418bec91c6f60d14604f11e887989d9f.

- 2026-09-09T02:26:20+00:00: Recorded command exit 0; command argv SHA-256
  5345cd4b5f66285dc80cddfe59c0a95475263f9ff88d25d2639fce3c300aa4b9.

- 2026-09-09T02:26:27+00:00: Recorded command exit 0; command argv SHA-256
  8d7f9afce51569180881a98eb8f427f4a04b51cc48d801bb7d8fe11d1486058f.

- 2026-09-09T02:26:34+00:00: Recorded command exit 0; command argv SHA-256
  2665c9ae788cf8f35dad12df7937d7229e73699c084ec97dcc1fc3b974ce8a93.

- 2026-09-09T02:26:49+00:00: Recorded command exit 0; command argv SHA-256
  a0ef889f8d4a0250f25854095804ecab7ac3c7eda4a8a01a6232bfd049960e3b.

- 2026-09-09T02:26:57+00:00: Recorded command exit 0; command argv SHA-256
  76155e7da7be1f5f2cf10e28f84fd412418bec91c6f60d14604f11e887989d9f.

- 2026-09-09T02:27:04+00:00: Recorded command exit 0; command argv SHA-256
  1f581f9a026d5b160417b8f2c8c4fb5cac313bc746b6473643c0716200e79081.

- 2026-09-09T02:27:43+00:00: Heartbeat by replay_20260909.

- 2026-09-09T02:27:46+00:00: Recorded command exit 0; command argv SHA-256
  6f965c75556d28b123ff50e69736dcf49bf1e3151b731fec8588a1d52f8188ca.

- 2026-09-09T02:27:55+00:00: Recorded command exit 0; command argv SHA-256
  5af53aa7233afbb2fa97993e3ab81cc03c403270e053d4439a589c742911aca5.

- 2026-09-09T02:28:10+00:00: Recorded command exit 0; command argv SHA-256
  d8388cb51f9740f209554e2cc2147b3e0781421564b034235b674d8f81dfe057.

- 2026-09-09T02:28:46+00:00: Heartbeat by replay_20260909.

- 2026-09-09T02:28:49+00:00: Recorded command exit 0; command argv SHA-256
  eba4f2d1785d1999e5f70b27d9836b6830b8871eb5b11f472864c31f2f4dba2e.

- 2026-09-09T02:28:58+00:00: Recorded command exit 0; command argv SHA-256
  d5dc0ce9698956b748f89a34b17e34e39b1d2c04fc90975825ec46c171c77f2b.
