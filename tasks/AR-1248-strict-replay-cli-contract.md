---
{
  "branch": "feature/ar-1248-strict-replay-cli-contract",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-16T12:40:08+00:00",
  "depends_on": [
    "AR-1231",
    "AR-1232"
  ],
  "id": "AR-1248",
  "next_action": "Run contract consistency, focused CLI replay-contract/schema tests, full locked workspace, policy/privacy/signature gates; then exact-head review and PR.",
  "observed_branch": "feature/ar-1248-strict-replay-cli-contract",
  "observed_dirty": 1,
  "observed_head": "37a9c2b48765bcf20d74d2ea4cabbb749142c0eb",
  "owner": "asb_ar1232_lifecycle_router",
  "plan": "../plans/AR-1248.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Define the strict-replay CLI consumer contract.",
  "task_revision": 31,
  "title": "Bounded strict-replay CLI consumer contract",
  "updated_at": "2026-09-16T10:44:01+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1248"
}
---

Implement only the linked AR-1248 plan using the ASB development documentation and handoffctl.
Preserve zero-runtime-dependency, offline-after-install, provider-egress denial, and all native,
formal, privacy, signature, DCO, and exact-tree gates.

- 2026-09-16T10:33:49+00:00: Dependencies AR-1231 and AR-1232 are durably done on protected main;
  strict replay CLI consumer gap is concrete and dependency-ready.

- 2026-09-16T10:34:06+00:00: Claimed by asb_ar1232_lifecycle_router.

- 2026-09-16T10:34:37+00:00: Heartbeat by asb_ar1232_lifecycle_router.

- 2026-09-16T10:35:47+00:00: Heartbeat by asb_ar1232_lifecycle_router.

- 2026-09-16T10:37:41+00:00: Recorded command exit 101; command argv SHA-256
  2bb0c4f7c650bd58ba047451817300c691716a3e418ef1f08cd31c546e62a17a.

- 2026-09-16T10:38:05+00:00: Recorded command exit 101; command argv SHA-256
  2bb0c4f7c650bd58ba047451817300c691716a3e418ef1f08cd31c546e62a17a.

- 2026-09-16T10:38:27+00:00: Recorded command exit 0; command argv SHA-256
  69487790cd46864562a51f207e108eea84da8519a17023da666d53127f8fc1e6.

- 2026-09-16T10:38:45+00:00: Recorded command exit 0; command argv SHA-256
  2bb0c4f7c650bd58ba047451817300c691716a3e418ef1f08cd31c546e62a17a.

- 2026-09-16T10:39:38+00:00: Recorded command exit 0; command argv SHA-256
  5cd7f7ecbd072b19f8bcf922677100f3be60e4ce8a4254b8d6fd3e991baa2b30.

- 2026-09-16T10:40:08+00:00: Heartbeat by asb_ar1232_lifecycle_router.

- 2026-09-16T10:40:11+00:00: Recorded command exit 1; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-16T10:40:42+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T10:41:00+00:00: Recorded command exit 0; command argv SHA-256
  2bb0c4f7c650bd58ba047451817300c691716a3e418ef1f08cd31c546e62a17a.

- 2026-09-16T10:41:26+00:00: Recorded command exit 0; command argv SHA-256
  e199d35c46ba7dd6836d71cac684338157d26becce51703bbef46d70f4b042b4.

- 2026-09-16T10:41:47+00:00: Recorded command exit 0; command argv SHA-256
  7adfa5f47f2d88e04500f07dc00da634ef9b56c7337415589d392c96b685c882.

- 2026-09-16T10:41:57+00:00: Recorded command exit 0; command argv SHA-256
  86b0d1dd71b4402f8180c78ddf5c60ead0d27e36ce1372707ea4c99ae0cb36e4.

- 2026-09-16T10:42:30+00:00: Signed commit 37a9c2b adds StrictReplayPlanV1 resolver with explicit
  bounded artifact root, symlink/traversal/size/digest/malformed rejection, authenticated
  StrictReplayLaunchRecord construction, schema/fixture/catalog/docs, and positive/negative tests.
  Focused unit tests 2/2 and clippy -D warnings pass; initial locked test failure was missing
  Cargo.lock entries, fixed by offline cargo check and rerun green. Worktree clean.

- 2026-09-16T10:42:55+00:00: Recorded command exit 0; command argv SHA-256
  4ae24a7384177fcaf78f7ffc43e6921296ffaf6f56ce9a884cfa52e0c3ef3a22.

- 2026-09-16T10:43:28+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T10:43:38+00:00: Recorded command exit 0; command argv SHA-256
  2bb0c4f7c650bd58ba047451817300c691716a3e418ef1f08cd31c546e62a17a.

- 2026-09-16T10:43:52+00:00: Recorded command exit 0; command argv SHA-256
  bb6cf3f88c21a8e3c5ac53502ff0baafea79443106425bb6f51eeea82e75b985.

- 2026-09-16T10:44:01+00:00: Recorded command exit 0; command argv SHA-256
  b0d4b6f53dc5fc9c746c248454e3bcceb4f4000c11ced3206a82309d83272144.
