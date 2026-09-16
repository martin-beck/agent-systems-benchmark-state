---
{
  "branch": "feature/ar-1256-bundled-mockagents-isolation",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-16T15:58:27+00:00",
  "depends_on": [
    "AR-1252",
    "AR-1253"
  ],
  "id": "AR-1256",
  "next_action": "Implement bundled in-container MockAgents transport and digest-pinned arm64 QEMU evidence.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "asb_ar1256_bundled_isolation",
  "plan": "../plans/AR-1256.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Execute bundled MockAgents transport in isolation.",
  "task_revision": 3,
  "title": "Execute bundled MockAgents transport in isolation",
  "updated_at": "2026-09-16T13:58:27+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1256"
}
---

Implement only the linked AR-1256 plan using ASB development documentation and handoffctl.
Keep bundles, images, QEMU artifacts, caches, and evidence under `/srv/data/projects`.

- 2026-09-16T13:58:24+00:00: AR-1252 and AR-1253 are complete; promote independent bundled
  transport/QEMU successor.

- 2026-09-16T13:58:27+00:00: Claimed by asb_ar1256_bundled_isolation.
