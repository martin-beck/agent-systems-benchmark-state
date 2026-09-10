---
{
  "branch": "test/asb-tui-cross-repository-integration",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1024", "AR-1025", "AR-1029"],
  "id": "AR-1026",
  "next_action": "Prove the ASB router and standalone frontend against exact cross-repository revisions through install, launch, run continuity and lifecycle faults.",
  "owner": "",
  "plan": "../plans/AR-1026.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Integrate and adversarially test the exact ASB and asb-tui revisions together.",
  "task_revision": 2,
  "title": "Qualify cross-repository ASB and asb-tui integration",
  "updated_at": "2026-09-10T19:20:00+00:00",
  "worktree_key": "agent-systems-benchmark-asb-tui-cross-repository-integration"
}
---
Build exact local release candidates for both repositories and test the public command surface from
clean homes. Bind every result to both commits/trees and prove that malformed, incompatible,
tampered, interrupted and concurrent paths fail without damaging ASB or a running benchmark.

Acceptance requires the full lifecycle command sequence, a real synthetic benchmark through the
interactive frontend, disconnect/reconnect and upgrade/remove continuity, platform/terminal matrix
evidence, independent review, exact-head CI and post-merge verification.
