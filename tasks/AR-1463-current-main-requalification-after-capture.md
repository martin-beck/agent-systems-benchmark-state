---
{
  "branch": "qualification/ar-1463-current-main-requalification-after-capture",
  "checkpoint_commit": "01b70e87ce8e7913f614447c0c530cb22e235256",
  "claim_expires": "2026-09-26T23:02:24+00:00",
  "depends_on": [
    "AR-1330",
    "AR-1461"
  ],
  "id": "AR-1463",
  "next_action": "No new release publication; retain v0.1.0 as the verified customer release and repeat qualification only for a later protected-main revision.",
  "observed_branch": "qualification/ar-1463-current-main-requalification-after-capture",
  "observed_dirty": 0,
  "observed_head": "01b70e87ce8e7913f614447c0c530cb22e235256",
  "owner": "coordinator-ar1463-requal",
  "plan": "../plans/AR-1463.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Exact protected main is requalified for first-customer production-like use: install/build, local/mock workloads, capture redaction and content-addressed sealing, strict offline replay, recovery/privacy/egress denial, coverage and deterministic/formal gates pass; existing v0.1.0 remains the verified release.",
  "task_revision": 32,
  "title": "Current-main first-customer requalification after capture integration",
  "updated_at": "2026-09-26T21:02:54+00:00",
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

- 2026-09-26T20:58:01+00:00: Recorded command exit 0; command argv SHA-256
  31714387755d8ca244c0da980bf43e334d2d5729874c3a8b55ec4a8c79c83916.

- 2026-09-26T20:58:22+00:00: Recorded command exit 0; command argv SHA-256
  9e0ce6e8ca0b7ea9d5a19bdd4999186cafa3d77a9c35fc3701a08ecc14f396a8.

- 2026-09-26T20:59:30+00:00: Recorded command exit 0; command argv SHA-256
  0ec1a1819623771695b22918c237241dc22c57f44d2b70c197126270f8cd8cd4.

- 2026-09-26T20:59:56+00:00: Recorded command exit 0; command argv SHA-256
  f52d7117bff5b817c45898a43532d74fdecd3759af131fc1ad6a70475a1b3215.

- 2026-09-26T21:00:51+00:00: Recorded command exit 0; command argv SHA-256
  5c8da9b34935360f7399b9d4b260d9a460b442f2f0ca08eddaee6e8f11776ef0.

- 2026-09-26T21:01:12+00:00: Recorded command exit 101; command argv SHA-256
  26cab572440e6bf245b6728d204770653b1bec1a123a452c9397607f5427d8d5.

- 2026-09-26T21:01:40+00:00: Recorded command exit 0; command argv SHA-256
  f5fc2faa127dd619356b77c7f29043e649b28033de05341e0f9295dc08578000.

- 2026-09-26T21:02:02+00:00: Recorded command exit 0; command argv SHA-256
  834fc7db89bcfa4bc26491cd80a3548be4f56075d780500a3912826a4268c0d0.

- 2026-09-26T21:02:24+00:00: Heartbeat by coordinator-ar1463-requal.

- 2026-09-26T21:02:54+00:00: Qualified exact protected main 01b70e87ce8e7913f614447c0c530cb22e235256
  in isolated branch qualification/ar-1463-current-main-requalification-after-capture. Passed cargo
  fmt --check, clippy locked workspace warnings denied, full cargo test workspace, rustdoc -D
  warnings, release build, focused capture/redaction/content-addressed cassette and strict replay
  tests, CLI network-denial/local-mock/cancellation tests, cargo llvm coverage (workspace and
  critical crates above floors), repository policy, pinned actionlint 1.7.12, zizmor 1.30.0,
  gitleaks 8.30.1, failure-path suite, signature policy, and formal/Cargo model tests. Exact-main
  hosted workflows all green at this SHA: Huawei 36269742977, hosted 36269743033, fault 36269743013,
  formal 36269743068, AArch64 36269743143, repository quality 36269743049, Rust 36269743060. Local
  cargo-deny 0.20.2, cargo-audit 0.22.2 and cargo-kani 0.67.0 executables are unavailable; no gate
  was weakened or skipped because exact-main CI evidence is green. Existing public v0.1.0 release
  verified via gh release view with artifact asb-v0.1.0.tar.gz; no new tag/release published. No
  live provider, native ARM, asb-tui or external signing required.
