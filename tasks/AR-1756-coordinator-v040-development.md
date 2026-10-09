---
{
  "branch": "upgrade/ar-1756-coordinator-v0.4.0-development",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-09T13:57:40+00:00",
  "depends_on": [
    "AR-1753"
  ],
  "id": "AR-1756",
  "next_action": "Promote and claim; independently verify upstream main c2692d0 and the absence of a v0.4.0 tag, then sync it through sync-development in an isolated state worktree without patching vendored bytes.",
  "owner": "codex-asb-ar1756-coordinator-v040-20261009",
  "plan": "../plans/AR-1756-coordinator-v040-development-vendor.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_ref": "specs/AR-1756.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Adopt the exact upstream Coordinator main containing the supported spec-acceptance command as an explicitly development-only vendor so merged ASB ARs can be durably accepted.",
  "task_revision": 3,
  "title": "Coordinator v0.4.0 development vendor for supported acceptance",
  "updated_at": "2026-10-09T11:57:40+00:00",
  "worktree_key": "agent-systems-benchmark-state-ar-1756-coordinator-v040"
}
---

The ASB state currently vendors Coordinator v0.3.59, while upstream `origin/main`
contains the reviewed owner- and revision-bound `accept` command and declares
version 0.4.0. There is currently no upstream `v0.4.0` tag. This AR adopts the
exact upstream main commit through the documented development-only vendor path;
it must not misrepresent that snapshot as a release.

The purpose is to restore the supported lifecycle operation needed to record the
already-reviewed AR-1729 and AR-1730 acceptance evidence. Existing product merge,
CI, and acceptance evidence remains authoritative and must be preserved. No
vendored Coordinator bytes may be edited downstream, and no lifecycle gate may
be bypassed.

- 2026-10-09T11:57:36+00:00: AR-1753 is done; exact upstream main with supported acceptance command
  independently verified and AR-1756 state files are integrated on protected main.

- 2026-10-09T11:57:40+00:00: Claimed by codex-asb-ar1756-coordinator-v040-20261009.
