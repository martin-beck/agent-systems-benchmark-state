---
{
  "branch": "feature/ar-1354-runtime-enrollment-implementation",
  "checkpoint_commit": "d83a85926f2c4c42317617f4f6b7b3c9a3195874",
  "claim_expires": null,
  "depends_on": [
    "AR-1352"
  ],
  "id": "AR-1354",
  "next_action": "Implement strict asb-config to asb-runtime enrollment, validate pinned targets/tools/relay root, and mint opaque handles for AR-1353 dispatch.",
  "observed_branch": "feature/ar-1354-runtime-enrollment-implementation",
  "observed_dirty": 0,
  "observed_head": "d83a85926f2c4c42317617f4f6b7b3c9a3195874",
  "owner": null,
  "plan": "../plans/AR-1354-runtime-enrollment-implementation.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "open",
  "summary": "Implement config-backed runtime-owned enrollment for live CLI dispatch.",
  "task_revision": 3,
  "title": "Runtime enrollment implementation",
  "updated_at": "2026-09-23T20:55:39+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1354-runtime-enrollment-implementation"
}
---

Successor for AR-1353's exact missing implementation: the opaque enrollment
transport exists, but no config/control source can safely mint its handle.
AR-1353 remains evidence and is superseded only after this dependency is
durably promoted; AR-1329 remains fail-closed.

- 2026-09-23T20:55:39+00:00: Coordinator repaired stale superseded dependency edge: AR-1353
  transport evidence remains preserved, while AR-1354 now depends directly on merged AR-1352.
  Promote config-backed enrollment implementation; AR-1329 remains fail-closed.
