---
{
  "branch": "codex/ar-1421-protected-main-race",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-24T21:44:24+00:00",
  "depends_on": [
    "AR-1416",
    "AR-1398"
  ],
  "id": "AR-1421",
  "next_action": "Promote after AR-1417's product merge is preserved and the failed run 36048870322 is recorded; repair the protected-main merge admission/requalification path without weakening the tree invariant.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "0000000000000000000000000000000000000000",
  "owner": "ar1421-protected-main-race-luna56",
  "plan": "../plans/AR-1421.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Repair protected-main merge-tree requalification after a literature PR merges onto an advanced main.",
  "task_revision": 6,
  "title": "Protected-main literature merge race repair",
  "updated_at": "2026-09-24T19:44:24+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1421"
}
---

The failed post-merge Repository Quality result is preserved as evidence. This AR
must not waive the exact-tree check, add a commit-specific exception, or classify
the merge released before fresh exact-main evidence succeeds.

- 2026-09-24T19:36:35+00:00: Incident evidence recorded in AR-1417; completed AR-1416 and AR-1398
  permit this independent repair while AR-1417 remains open.

- 2026-09-24T19:37:03+00:00: Claimed by ar1421-protected-main-race-luna56.

- 2026-09-24T19:37:29+00:00: Heartbeat by ar1421-protected-main-race-luna56.

- 2026-09-24T19:37:51+00:00: Heartbeat by ar1421-protected-main-race-luna56.

- 2026-09-24T19:44:24+00:00: Heartbeat by ar1421-protected-main-race-luna56.
