---
{
  "branch": "feature/ar-1365-control-receipt-source-integration",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-24T01:54:24+00:00",
  "depends_on": [
    "AR-1362",
    "AR-1364"
  ],
  "id": "AR-1365",
  "next_action": "Promote after AR-1362 and AR-1364 are done, then integrate authenticated chain and authority enrollment into the versioned control receipt source.",
  "observed_branch": "feature/ar-1365-control-receipt-source-integration",
  "observed_dirty": 1,
  "observed_head": "3a4007be828db04f3b57492e5c5f230199cb8d5a",
  "owner": "codex-asb-runtime-attested-enrollment-luna56",
  "plan": "../plans/AR-1365-control-receipt-source-integration.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Integrate authenticated chain and authority enrollment into the versioned control receipt source.",
  "task_revision": 6,
  "title": "Control receipt source integration",
  "updated_at": "2026-09-23T23:56:04+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1365-control-receipt-source-integration"
}
---

Successor for blocked AR-1363, explicitly depending on completed AR-1362 and
AR-1364. Do not touch asb-tui or synthesize authority from CLI/config input.

- 2026-09-24T00:00:00+00:00: Created after AR-1364 supplied authenticated
  chain enrollment materialization and all post-merge workflows passed.

- 2026-09-23T23:54:21+00:00: Promote receipt-source integration after AR-1362 and AR-1364 completed
  authority and chain primitives with all post-merge gates.

- 2026-09-23T23:54:24+00:00: Claimed by codex-asb-runtime-attested-enrollment-luna56.

- 2026-09-23T23:55:36+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-23T23:56:04+00:00: Recorded command exit 0; command argv SHA-256
  d9dd06c9e77766238089b3c04fcddb575442cf1887a2ccc06521948ea874e7cc.
