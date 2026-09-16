---
{
  "branch": "feature/ar-1243",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1239", "AR-1240", "AR-1241"],
  "id": "AR-1243",
  "next_action": "Implement reproducible supervisor/sidecar bundle assembly and explicit SSH signing using the project release workflow.",
  "observed_branch": "feature/ar-1243",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1243.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Build, sign, verify, and publish installable supervisor and sidecar runtime bundles.",
  "task_revision": 1,
  "title": "Installable signed runtime bundle assembly",
  "updated_at": "2026-09-16T00:00:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1243"
}
---

Implement only the linked AR-1243 plan. Use an isolated product worktree and the repository
development documentation. Signing must use an explicit operator-provided key without recording
private material; do not alter host networking, firewall, credentials, or unrelated processes.
