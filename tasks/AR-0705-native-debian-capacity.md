---
{
  "branch": "feature/native-debian-capacity",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-25T13:49:03+00:00",
  "depends_on": [
    "AR-0704",
    "AR-0201",
    "AR-0401"
  ],
  "id": "AR-0705",
  "next_action": "Qualify native x86_64 Debian and required applicable pinned QEMU AArch64 behavior; document genuine native ARM64 as optional future evidence.",
  "owner": "ar0705_native_debian_luna56",
  "plan": "../plans/AR-0705.md",
  "priority": "P2",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Qualify booted Debian on native x86_64 and applicable QEMU AArch64; keep native ARM64 optional.",
  "task_revision": 4,
  "title": "Provide native Debian capacity",
  "updated_at": "2026-09-25T11:49:03+00:00",
  "worktree_key": "agent-systems-benchmark-native-debian-capacity"
}
---
## AR-0705

Provision a credential-isolated, booted Debian x86_64 cell and optionally an ARM64 cell. Prove
native identity, kernel/distribution provenance, cleanup, cost/availability bounds, and evidence integrity.

- 2026-09-09T10:53:36+00:00: Removed native ARM64 as a completion or downstream blocker.

- 2026-09-25T11:48:59+00:00: Dependencies AR-0704, AR-0201, and AR-0401 are done; begin fail-closed
  native Debian capacity qualification under current runner policy.

- 2026-09-25T11:49:03+00:00: Claimed by ar0705_native_debian_luna56.
