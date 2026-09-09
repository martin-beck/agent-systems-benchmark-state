---
{
  "branch": "feature/provider-aware-agent-launch",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-09T02:53:57+00:00",
  "depends_on": [
    "AR-0102",
    "AR-0103",
    "AR-0313",
    "AR-0316",
    "AR-0317",
    "AR-0318",
    "AR-0319",
    "AR-0320",
    "AR-0869"
  ],
  "id": "AR-0876",
  "next_action": "Monitor PR #93 exact-head CI at 251d676; preempt feature work on any failure and repair same branch.",
  "observed_branch": "feature/provider-aware-agent-launch",
  "observed_dirty": 1,
  "observed_head": "251d6769a6ed86171cca7838471974d8b73486b7",
  "owner": "replay_20260909",
  "plan": "../plans/AR-0876.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Apply validated provider selections at the authoritative agent launch boundary and reject conflicting runtime configuration.",
  "task_revision": 50,
  "title": "Wire provider-aware agent launches",
  "updated_at": "2026-09-09T00:58:22+00:00",
  "worktree_key": "agent-systems-benchmark-provider-aware-agent-launch"
}
---
## AR-0876

Close the AR-0869 execution-wiring gap by making its content-addressed provider selection an
authoritative input to the actual adapter process launch, rather than provenance-only metadata.

Implementation has not started. Read the linked plan before claiming.


- 2026-09-09T00:30:52+00:00: AR-0871 is merged and fully verified; AR-0876 is the highest-priority
  dependency-ready leaf that closes provider-selection execution wiring.

- 2026-09-09T00:30:55+00:00: Claimed by replay_20260909.

- 2026-09-09T00:31:20+00:00: Recorded command exit 0; command argv SHA-256
  d7c226a60b6735868b5a8965666285114b01921a4fd641a6c89c52f51e831b01.

- 2026-09-09T00:33:44+00:00: Heartbeat by replay_20260909.

- 2026-09-09T00:37:29+00:00: Recorded command exit 0; command argv SHA-256
  9fe73088536dc5e06523f8e18e23dd6be47e78a90426e7b579b7067624f73c84.

- 2026-09-09T00:37:46+00:00: Heartbeat by replay_20260909.

- 2026-09-09T00:38:02+00:00: Recorded command exit 0; command argv SHA-256
  56b228d10c091c83b96d7316d8d47def00bf0962640ede14a4b12cbb2094f07f.

- 2026-09-09T00:38:59+00:00: Heartbeat by replay_20260909.

- 2026-09-09T00:39:03+00:00: Recorded command exit 0; command argv SHA-256
  a7d6b628d30e583db6df7759a836c6fde7df539f25510ea41031a87c62fe9ea0.

- 2026-09-09T00:40:41+00:00: Heartbeat by replay_20260909.

- 2026-09-09T00:40:51+00:00: Recorded command exit 0; command argv SHA-256
  f62c661b82a90472684d6ad074a742ebece91dafce7de4f468389a35a12ac00b.

- 2026-09-09T00:41:19+00:00: Heartbeat by replay_20260909.

- 2026-09-09T00:41:24+00:00: Recorded command exit 0; command argv SHA-256
  9214ef896a6b61c45637dc024149c7d08b8f222d0b658b5cd340010f5271d46a.

- 2026-09-09T00:42:32+00:00: Heartbeat by replay_20260909.

- 2026-09-09T00:42:37+00:00: Recorded command exit 101; command argv SHA-256
  814fca455e3ba22c34d5389553e345fb9ddf1e645afd2ebd791e4b78984d0786.

- 2026-09-09T00:43:16+00:00: Recorded command exit 0; command argv SHA-256
  5bf699b95b8c514d6effac6dbc2be6013575611b144a06c747536d187e583ef8.

- 2026-09-09T00:43:23+00:00: Recorded command exit 101; command argv SHA-256
  ec488f391ae4bc2f24b23f2a1f1edc93bd38ca7c416f7fa93c8ded4fb0b7ca60.

- 2026-09-09T00:43:34+00:00: Heartbeat by replay_20260909.

- 2026-09-09T00:43:38+00:00: Recorded command exit 0; command argv SHA-256
  8ac918ff2f721c0cbeb365213414bd96fba625d2259fb4d9d8040feb612e7236.

- 2026-09-09T00:43:58+00:00: Heartbeat by replay_20260909.

- 2026-09-09T00:44:02+00:00: Recorded command exit 0; command argv SHA-256
  bd15653064fc694558b26c2bcc2b4aede6fcf3bac6b4cded456c569f99accbd3.

- 2026-09-09T00:44:33+00:00: Heartbeat by replay_20260909.

- 2026-09-09T00:45:17+00:00: Recorded command exit 0; command argv SHA-256
  ebeec6162a51506bd6dae4a57dddb77a32cb3af1cf8f7e05befee8e3bd28f719.

- 2026-09-09T00:45:56+00:00: Heartbeat by replay_20260909.

- 2026-09-09T00:45:58+00:00: Recorded command exit 0; command argv SHA-256
  49a18c8f11b1a2d093b69d5b1e4413552ae0bc922f7b5983069d52d3b10cc6f3.

- 2026-09-09T00:46:06+00:00: Recorded command exit 0; command argv SHA-256
  6b917aabd1bdb436194b4426d4acce75ab6bd08ae9bc8d8a618e6352a31a137d.

- 2026-09-09T00:46:34+00:00: Implemented signed commit 45999650: added constructor-controlled
  ProviderLaunchV1 binding, canonical launch digest, projection/tamper/privacy tests, CLI pre-spawn
  binding and non-secret launch environment, durable manifest/report identity, fixtures, and
  documentation. Focused CLI/agent tests and workspace test plus clippy passed; next action is
  independent review, exact-head CI, and repair if required.

- 2026-09-09T00:46:53+00:00: Recorded command exit 0; command argv SHA-256
  918a3be8115380b3ca5df46a6140376f49a2659d83c88d0b4c3bbab81f17a755.

- 2026-09-09T00:47:16+00:00: Recorded command exit 0; command argv SHA-256
  b13c42f7cc043c64aa511f89f8dee2c4748dd23a13704d69da805358d3a7d534.

- 2026-09-09T00:47:24+00:00: Recorded command exit 0; command argv SHA-256
  9816f39cfe20bd6dc6df5d7df1682e3c76a4b0de8d77974baa8b05e818b71a75.

- 2026-09-09T00:47:34+00:00: Recorded command exit 0; command argv SHA-256
  88fa7186fe7a47cafde98549e48d32802236eca529608fb488e4f267317dfd85.

- 2026-09-09T00:47:42+00:00: Recorded command exit 0; command argv SHA-256
  3a315ff4db2e103070338c4e7ce7277e12596177f16a02b6688a77fbbf793067.

- 2026-09-09T00:48:06+00:00: Immutable PR #93 opened at signed+DCO head 45999650 on exact main
  dca243ab. Exact-head required CI is running; current completed checks: AWQ and Huawei header
  validation passed. No feature work proceeds until all required gates are terminal green.

- 2026-09-09T00:50:17+00:00: Heartbeat by replay_20260909.

- 2026-09-09T00:50:32+00:00: Recorded command exit 0; command argv SHA-256
  5ec35fcaad5a6c6bd145073a63b94b564ee0ad178a80ee7fd24a540996f2470e.

- 2026-09-09T00:50:51+00:00: Recorded command exit 0; command argv SHA-256
  16c083d3c272b073619797084e784192f83c0e45f3f7fa6f372a2ac715f9666d.

- 2026-09-09T00:51:33+00:00: Recorded command exit 0; command argv SHA-256
  1e4d8d434e76f20af551249372d861428f1f2beeef34b02d32877135a7c91c0d.

- 2026-09-09T00:51:40+00:00: Recorded command exit 0; command argv SHA-256
  40b754580b11c57d1b5938e58489cb520de17417151a2ee5e38d62f1a98d8858.

- 2026-09-09T00:51:52+00:00: Recorded command exit 0; command argv SHA-256
  f2dad8c5e2ba3038e703841a610082e1c4b3888488207889e5e917cd68aa5a1d.

- 2026-09-09T00:52:22+00:00: CI failure on original head 45999650 was diagnosed from job logs:
  formal TLC asset 551007111 returned HTTP 404. Root cause was an upstream release asset
  replacement, not launch code. Repaired same branch with signed+DCO commit 251d676, pinning
  official asset 551658253, size 4489044, digest 0d1f3b48..., updated formal metadata/tests/docs;
  local formal test and temporal runner passed. PR #93 now reruns at exact head 251d676.

- 2026-09-09T00:53:57+00:00: Heartbeat by replay_20260909.
