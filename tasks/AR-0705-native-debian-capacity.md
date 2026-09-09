---
{
  "branch": "feature/native-debian-capacity",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-0704",
    "AR-0201",
    "AR-0401"
  ],
  "id": "AR-0705",
  "next_action": "Qualify native x86_64 Debian and required applicable pinned QEMU AArch64 behavior; document genuine native ARM64 as optional future evidence.",
  "owner": "",
  "plan": "../plans/AR-0705.md",
  "priority": "P2",
  "schema_version": 1,
  "status": "planned",
  "summary": "Qualify booted Debian on native x86_64 and applicable QEMU AArch64; keep native ARM64 optional.",
  "task_revision": 2,
  "title": "Provide native Debian capacity",
  "updated_at": "2026-09-09T10:53:36+00:00",
  "worktree_key": "agent-systems-benchmark-native-debian-capacity"
}
---
## AR-0705

Provision credential-isolated, booted Debian x86_64 and aarch64 cells. Prove native identity,
kernel/distribution provenance, cleanup, cost/availability bounds, and evidence integrity.

- 2026-09-09T10:53:36+00:00: Removed native ARM64 as a completion or downstream blocker.
