---
{
  "branch": "feature/native-debian-capacity",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-25T13:50:18+00:00",
  "depends_on": [
    "AR-0704",
    "AR-0201",
    "AR-0401"
  ],
  "id": "AR-0705",
  "next_action": "Qualify native x86_64 Debian and required applicable pinned QEMU AArch64 behavior; document genuine native ARM64 as optional future evidence.",
  "observed_branch": "feature/native-debian-capacity",
  "observed_dirty": 0,
  "observed_head": "7390bcd2082700d0c9f04409732b48de8e9f8628",
  "owner": "ar0705_native_debian_luna56",
  "plan": "../plans/AR-0705.md",
  "priority": "P2",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Qualify booted Debian on native x86_64 and applicable QEMU AArch64; keep native ARM64 optional.",
  "task_revision": 11,
  "title": "Provide native Debian capacity",
  "updated_at": "2026-09-25T11:50:35+00:00",
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

- 2026-09-25T11:49:35+00:00: Recorded command exit 0; command argv SHA-256
  ff6d1fa7a7185010f75fcfafe4bdc1bdd5b9804d8c2b3e7abdd8a1b96cd81c63.

- 2026-09-25T11:49:49+00:00: Recorded command exit 0; command argv SHA-256
  54ef1dd5d38b4a65fb85227d8a9a05348bcc52ed52376680c3df877030db5276.

- 2026-09-25T11:50:04+00:00: Recorded command exit 0; command argv SHA-256
  10c9e0d6a71a4f2245c476901f5d64b0da811fc833a4d1dffb8ac6a76fdeb497.

- 2026-09-25T11:50:18+00:00: Heartbeat by ar0705_native_debian_luna56.

- 2026-09-25T11:50:21+00:00: Recorded command exit 0; command argv SHA-256
  cdda59958d683ab8ce154ffdf009a02e9725eeb3299ee0b2998606b764555732.

- 2026-09-25T11:50:35+00:00: Recorded command exit 0; command argv SHA-256
  0ed28ab2d231d0b2bd8ef8fcc7c11bb59995fd48770e67cf2eb8a98065389117.
