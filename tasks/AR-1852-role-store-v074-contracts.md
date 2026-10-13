---
{
  "branch": "codex/ar1852-role-store-v074-contracts",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [],
  "id": "AR-1852",
  "next_action": "Bind to the exact v0.7.4 candidate worktree at ASB commit 180c96b25d, then reproduce and repair only non-vendor role-store compatibility tests.",
  "owner": "",
  "plan": "../plans/AR-1852-role-store-v074-contracts.md",
  "priority": "P1",
  "schema_version": 1,
  "spec_acceptance": {"evidence_class": "mechanical", "evidence_digest": "", "evidence_ref": "", "spec_ref": "specs/AR-1852.json", "spec_revision": 1, "status": "pending"},
  "spec_ref": "specs/AR-1852.json",
  "spec_revision": 1,
  "status": "planned",
  "summary": "Align role-store authorization tests with Coordinator v0.7.4.",
  "task_revision": 1,
  "title": "Role-store v0.7.4 compatibility contracts",
  "updated_at": "2026-10-13T13:10:00+00:00",
  "worktree_key": "agent-systems-benchmark-state-ar-1852"
}
---

Create a dependency-safe, non-vendor repair for role doctor and lifecycle
authorization contract failures exposed by exact Coordinator v0.7.4 adoption.
