---
{
  "branch": "feature/ar-1241-native-isolation-matrix",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1240"
  ],
  "id": "AR-1241",
  "next_action": "Add provider/external/descendant egress denial and timeout/cancel/crash/non-interference tests for the signed native bundle.",
  "observed_branch": "feature/ar-1241-native-isolation-matrix",
  "observed_dirty": 0,
  "observed_head": "7523fde1d87edc0a22e40c79c866b12d4f11599b",
  "owner": "",
  "plan": "../plans/AR-1241.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "done",
  "summary": "Complete native signed-bundle isolation negative and lifecycle evidence.",
  "task_revision": 11,
  "title": "Native isolation negative and lifecycle matrix",
  "updated_at": "2026-09-16T08:47:58+00:00",
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

- 2026-09-16T08:47:43+00:00: Recorded command exit 0; command argv SHA-256
  6363ce9ae09b6744d6ae6ddb2ad58a4809bf91b65c77994d8ad22f5ab57c08e9.

- 2026-09-16T08:47:58+00:00: Completed native isolation matrix in signed commit 7523fde. Added
  provider/external/descendant egress denial, timeout descendant reaping, crash cleanup,
  cancellation non-interference, and supervisor cassette lifecycle assertions. Sandbox boundary
  17/17 passed; runtime package, locked workspace, fmt, clippy and rustdoc gates passed. No host
  networking, firewall, ambient ip, credentials, or unrelated-process mutation.
