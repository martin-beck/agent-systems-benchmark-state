---
{
  "branch": "feature/ar-1240-native-signed-bundle-fixture",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1238", "AR-1239"],
  "id": "AR-1240",
  "next_action": "Materialize and verify a signed supervisor/sidecar bundle fixture, then run the native Bubblewrap isolation matrix.",
  "observed_branch": "feature/ar-1240-native-signed-bundle-fixture",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1240.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Add native signed-bundle fixture and end-to-end supervisor isolation tests.",
  "task_revision": 1,
  "title": "Native signed-bundle supervisor fixture",
  "updated_at": "2026-09-16T08:35:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1240"
}
---

Own only native test fixture materialization and isolation evidence for the supervisor/sidecar
bundle. Preserve fail-closed behavior and all existing privacy and non-interference constraints.
