---
{
  "branch": "feature/ar-1255-bundled-mockagents-qemu-runner",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1254", "AR-1253"],
  "id": "AR-1255",
  "next_action": "Provision a digest-pinned bundled transport/QEMU runner and implement real in-container evidence.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1255.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "planned",
  "summary": "Bundle MockAgents transport and QEMU runner.",
  "task_revision": 1,
  "title": "Bundle MockAgents transport and QEMU runner",
  "updated_at": "2026-09-16T14:00:00+02:00",
  "worktree_key": "agent-systems-benchmark-ar-1255"
}
---

Implement only the linked AR-1255 plan using ASB development documentation and handoffctl.
Keep bundles, images, QEMU artifacts, caches, and evidence under `/srv/data/projects`.
