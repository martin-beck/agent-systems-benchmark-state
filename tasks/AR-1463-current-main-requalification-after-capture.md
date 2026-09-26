---
{
  "branch": "qualification/ar-1463-current-main-requalification-after-capture",
  "checkpoint_commit": "01b70e87ce8e7913f614447c0c530cb22e235256",
  "claim_expires": "2026-09-26T22:47:57+00:00",
  "depends_on": [
    "AR-1330",
    "AR-1461"
  ],
  "id": "AR-1463",
  "next_action": "Promote and qualify exact protected main after AR-1330 across the first-customer install, local/mock benchmark, capture/replay, recovery, privacy and release gates; publish no release unless all gates pass.",
  "observed_branch": "qualification/ar-1463-current-main-requalification-after-capture",
  "observed_dirty": 0,
  "observed_head": "01b70e87ce8e7913f614447c0c530cb22e235256",
  "owner": "coordinator-ar1463-requal",
  "plan": "../plans/AR-1463.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Requalify current protected main for first-customer production-like use after capture/replay integration.",
  "task_revision": 22,
  "title": "Current-main first-customer requalification after capture integration",
  "updated_at": "2026-09-26T20:57:42+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1463-current-main-requalification-after-capture"
}
---

This P0 assurance AR closes the evidence gap created when AR-1330 advanced
protected main after the first-customer release. It must qualify the exact
current main with the mandatory credential-free local/mock paths and strict
offline capture/replay, while preserving all privacy, cancellation, cleanup,
egress-denial, formal, supply-chain and release gates. External provider
reachability, native ARM hardware, asb-tui changes and external signing are not
required. Any release decision must remain fail-closed and exact-head bound.

- 2026-09-26T20:48:00+00:00: Created because AR-1330 merged after the v0.1.0
  release; prior first-customer evidence did not cover the new protected-main
  capture/replay implementation.

- 2026-09-26T20:47:02+00:00: AR-1330 capture integration is merged; promote current-main
  first-customer requalification at exact merge 01b70e87ce8e7913f614447c0c530cb22e235256.

- 2026-09-26T20:47:05+00:00: Claimed by coordinator-ar1463-requal.

- 2026-09-26T20:47:57+00:00: Heartbeat by coordinator-ar1463-requal.

- 2026-09-26T20:49:00+00:00: Recorded command exit 0; command argv SHA-256
  ff6d1fa7a7185010f75fcfafe4bdc1bdd5b9804d8c2b3e7abdd8a1b96cd81c63.

- 2026-09-26T20:49:18+00:00: Recorded command exit 0; command argv SHA-256
  6840d2f0cea6f9cf6ffce81b9b1b74dcdddaff8701fc6cc1705c309033813254.

- 2026-09-26T20:49:40+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-26T20:50:15+00:00: Recorded command exit 0; command argv SHA-256
  1024fc1e6cefa31b078f0b5d2ed85c7ea4586897b388bf1e308f62db58574461.

- 2026-09-26T20:51:28+00:00: Recorded command exit 0; command argv SHA-256
  534f8613e1c316db8f0f46dd989e44e14a8ca74304a94791b4e4a1c59b2fbb1d.

- 2026-09-26T20:51:54+00:00: Recorded command exit 0; command argv SHA-256
  b36d15881eb65027724bc584f1b04db05666cd79896b100806e528307c04b65c.

- 2026-09-26T20:52:42+00:00: Recorded command exit 0; command argv SHA-256
  b49a90ee600c1023cee9ee9f9e8a4f9a06c53eef8c48d3932d88e482126c7c01.

- 2026-09-26T20:53:06+00:00: Recorded command exit 0; command argv SHA-256
  f87a67bde50298a74ae4792b80439510a590dc0e09c5a89367566c896ccea7ae.

- 2026-09-26T20:53:38+00:00: Recorded command exit 0; command argv SHA-256
  18d00fc6101ee5d875113b525b19360d83ad223b1702bc53e4fc0d7f7c6448f7.

- 2026-09-26T20:54:02+00:00: Recorded command exit 0; command argv SHA-256
  457985951aef25dd21f9e303d28fc8a05179de5cfb5df9da39049dd86c32be73.

- 2026-09-26T20:54:22+00:00: Recorded command exit 0; command argv SHA-256
  c47a58154a4afadf61058f8d2a445578e32c5f22e61ccccd609eb994eacbc09c.

- 2026-09-26T20:56:02+00:00: Recorded command exit 0; command argv SHA-256
  428457ea9cc6a21bd46c5be6651ba2faccb5b0b07ddc2fd6f96eca730dea5ab7.

- 2026-09-26T20:56:21+00:00: Recorded command exit 101; command argv SHA-256
  09106a58846d62b60a8b096e311be2bf71836cd7e41e5bfbac061fcad43c19de.

- 2026-09-26T20:56:36+00:00: Recorded command exit 101; command argv SHA-256
  c97a7f810cbcaf336269f7053d237169f9132cd3c846c01c90a9281753a77713.

- 2026-09-26T20:56:56+00:00: Recorded command exit 0; command argv SHA-256
  5fbf8cf5f7a5033b168f87348a1437fc40d72ecd1e1d68cf72198b21c522c119.

- 2026-09-26T20:57:20+00:00: Recorded command exit 0; command argv SHA-256
  fdef15f98b9f15eb014309487558bb767993e6528fd1844a6fbdbd939651dd58.

- 2026-09-26T20:57:42+00:00: Recorded command exit 0; command argv SHA-256
  d6513f06fd9c78a0af6a2eccd989294545871661504881d49705db7c107f7e26.
