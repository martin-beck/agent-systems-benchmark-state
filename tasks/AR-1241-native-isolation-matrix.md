---
{
  "branch": "feature/ar-1241-native-isolation-matrix",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-16T10:41:09+00:00",
  "depends_on": [
    "AR-1240"
  ],
  "id": "AR-1241",
  "next_action": "Add provider/external/descendant egress denial and timeout/cancel/crash/non-interference tests for the signed native bundle.",
  "observed_branch": "feature/ar-1241-native-isolation-matrix",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "asb_ar1241_native_isolation_worker",
  "plan": "../plans/AR-1241.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Complete native signed-bundle isolation negative and lifecycle evidence.",
  "task_revision": 3,
  "title": "Native isolation negative and lifecycle matrix",
  "updated_at": "2026-09-16T08:41:09+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1241"
}
---

Own only native negative egress, failure lifecycle, and unrelated-process non-interference coverage
for the verified supervisor/sidecar bundle. Preserve fail-closed policy and do not alter host or
global network state.

- 2026-09-16T08:40:58+00:00: AR-1240 complete with native signed cassette forwarding; begin
  remaining negative egress and lifecycle matrix.

- 2026-09-16T08:41:09+00:00: Claimed by asb_ar1241_native_isolation_worker.
