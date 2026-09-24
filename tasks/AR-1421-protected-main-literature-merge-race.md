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
  "observed_branch": "codex/ar-1421-protected-main-race",
  "observed_dirty": 0,
  "observed_head": "5ddac12fc0b2d9fbff2b056af888b9ec76edeee5",
  "owner": "ar1421-protected-main-race-luna56",
  "plan": "../plans/AR-1421.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Repair protected-main merge-tree requalification after a literature PR merges onto an advanced main.",
  "task_revision": 9,
  "title": "Protected-main literature merge race repair",
  "updated_at": "2026-09-24T19:44:43+00:00",
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

- 2026-09-24T19:44:27+00:00: Recorded command exit 0; command argv SHA-256
  ff6d1fa7a7185010f75fcfafe4bdc1bdd5b9804d8c2b3e7abdd8a1b96cd81c63.

- 2026-09-24T19:44:43+00:00: Recorded command exit -13; command argv SHA-256
  52daa64da4c722e38bf9042a32f8caf51ba53857690e83796d7235916a29c648.
