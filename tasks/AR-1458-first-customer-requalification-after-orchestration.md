---
{
  "branch": "qualification/ar-1458-first-customer-requalification-after-orchestration",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-26T20:37:08+00:00",
  "depends_on": [
    "AR-1446",
    "AR-1453",
    "AR-1456"
  ],
  "id": "AR-1458",
  "next_action": "Promote and run the disposable first-customer install/configure/local-mock benchmark/strict-replay/recovery/cleanup qualification against the exact current protected main after the central orchestration merge; publish a privacy-safe readiness report or record any deterministic repair AR.",
  "observed_branch": "qualification/ar-1458-first-customer-requalification-after-orchestration",
  "observed_dirty": 0,
  "observed_head": "ad4f96ab3f7e57916208406b2f56aa9ec4e54885",
  "owner": "coordinator-ar1458-requal",
  "plan": "../plans/AR-1458.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Requalify the first-customer production-like journey after central orchestration became authoritative.",
  "task_revision": 18,
  "title": "First-customer requalification after central orchestration",
  "updated_at": "2026-09-26T18:40:55+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1458-first-customer-requalification-after-orchestration"
}
---

AR-1446 qualified the disposable first-customer path on merge 2872a31 before
the central orchestration design, implementation, and frontend routing landed.
This AR reruns the complete ASB-only customer-like journey on the current
protected main: clean install/bootstrap, explicit local/mock configuration,
multi-agent workload execution, evidence inspection, strict offline replay,
cancellation/restart recovery, and cleanup/rollback. It must not contact a
remote provider or modify asb-tui. Any live-provider evidence remains optional
and separately classified.

- 2026-09-26T18:36:36+00:00: Current main now includes central orchestration after AR-1446
  qualification; requalify the customer journey on the updated exact main.

- 2026-09-26T18:36:45+00:00: Claimed by coordinator-ar1458-requal.

- 2026-09-26T18:37:08+00:00: Heartbeat by coordinator-ar1458-requal.

- 2026-09-26T18:37:43+00:00: Recorded command exit 0; command argv SHA-256
  2f602dfc8040280fd88f215231a03c121de4408a979329e226de138849af5ff8.

- 2026-09-26T18:37:58+00:00: Recorded command exit 0; command argv SHA-256
  ff6d1fa7a7185010f75fcfafe4bdc1bdd5b9804d8c2b3e7abdd8a1b96cd81c63.

- 2026-09-26T18:38:12+00:00: Recorded command exit 0; command argv SHA-256
  1a847ab650e54b0917c49b13b598160388b9426690d357206f8b6e100b62f73b.

- 2026-09-26T18:38:28+00:00: Recorded command exit 0; command argv SHA-256
  1d00b38b7a9770e5e963cafa06d94543076b0a3fe68f0bd5b28e675dc542c761.

- 2026-09-26T18:38:43+00:00: Recorded command exit 0; command argv SHA-256
  2433f9cb82d926274d5e891c5edcc765e9bf67b77443c07b1449e6acf6e146ca.

- 2026-09-26T18:38:59+00:00: Recorded command exit 0; command argv SHA-256
  b1872b8700740f8f9c9f76d3e577b5c45e53a23d3c5f68b1bca41f93e273ed07.

- 2026-09-26T18:39:13+00:00: Recorded command exit 0; command argv SHA-256
  6562de1aecb54fa6d93ab9c9a1b341d0692a229ce5c7ea06fe0df750c577722c.

- 2026-09-26T18:39:28+00:00: Recorded command exit 0; command argv SHA-256
  0506218d93aba0f897152e511b753bfb435291b4d327af1406574275d323f1e6.

- 2026-09-26T18:39:52+00:00: Recorded command exit 0; command argv SHA-256
  5e3d7817f0afba28e5aaab104bd49513090d0424642bd97634a5373b02bde924.

- 2026-09-26T18:40:07+00:00: Recorded command exit 0; command argv SHA-256
  38550d7758b709d26549f061419ee5c2db89afe198ca21f317a9e36df066a303.

- 2026-09-26T18:40:26+00:00: Recorded command exit 0; command argv SHA-256
  d668e070629151f918df1cdbc00849848752c2f3d85bdca0a78ae5b794cb3d4a.

- 2026-09-26T18:40:41+00:00: Recorded command exit 0; command argv SHA-256
  2a9339303dd144fa361326d713de072ed50ff2dcfcda3b9fb1bf6fef10b99ae6.

- 2026-09-26T18:40:55+00:00: Recorded command exit 0; command argv SHA-256
  2820e956ea95a29ec25997101b9b4cb478cea6c13c7b2f58da619cdb3784eb07.
