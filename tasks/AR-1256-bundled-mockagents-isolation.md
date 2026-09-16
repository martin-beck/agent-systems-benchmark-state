---
{
  "branch": "feature/ar-1256-bundled-mockagents-isolation",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1252", "AR-1253"],
  "id": "AR-1256",
  "next_action": "Implement bundled in-container MockAgents transport and digest-pinned arm64 QEMU evidence.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1256.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "planned",
  "summary": "Execute bundled MockAgents transport in isolation.",
  "task_revision": 1,
  "title": "Execute bundled MockAgents transport in isolation",
  "updated_at": "2026-09-16T14:10:00+02:00",
  "worktree_key": "agent-systems-benchmark-ar-1256"
}
---

Implement only the linked AR-1256 plan using ASB development documentation and handoffctl.
Keep bundles, images, QEMU artifacts, caches, and evidence under `/srv/data/projects`.
