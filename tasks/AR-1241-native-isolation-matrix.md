---
{
  "branch": "feature/ar-1241-native-isolation-matrix",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-16T10:42:40+00:00",
  "depends_on": [
    "AR-1240"
  ],
  "id": "AR-1241",
  "next_action": "Add provider/external/descendant egress denial and timeout/cancel/crash/non-interference tests for the signed native bundle.",
  "observed_branch": "feature/ar-1241-native-isolation-matrix",
  "observed_dirty": 1,
  "observed_head": "fd4192d2d76761d100415f199faf26982c6a1cf4",
  "owner": "asb_ar1241_matrix_worker",
  "plan": "../plans/AR-1241.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Complete native signed-bundle isolation negative and lifecycle evidence.",
  "task_revision": 8,
  "title": "Native isolation negative and lifecycle matrix",
  "updated_at": "2026-09-16T08:45:21+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1241"
}
---

Own only native negative egress, failure lifecycle, and unrelated-process non-interference coverage
for the verified supervisor/sidecar bundle. Preserve fail-closed policy and do not alter host or
global network state.

- 2026-09-16T08:40:58+00:00: AR-1240 complete with native signed cassette forwarding; begin
  remaining negative egress and lifecycle matrix.

- 2026-09-16T08:41:09+00:00: Claimed by asb_ar1241_native_isolation_worker.

- 2026-09-16T08:42:26+00:00: Release stale claimed lease so the assigned matrix worker can take
  over; no product changes were made under the stale lease.

- 2026-09-16T08:42:40+00:00: Claimed by asb_ar1241_matrix_worker.

- 2026-09-16T08:45:21+00:00: Recorded command exit 101; command argv SHA-256
  6363ce9ae09b6744d6ae6ddb2ad58a4809bf91b65c77994d8ad22f5ab57c08e9.
