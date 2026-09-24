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
  "task_revision": 21,
  "title": "Protected-main literature merge race repair",
  "updated_at": "2026-09-24T19:48:21+00:00",
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

- 2026-09-24T19:44:52+00:00: Recorded command exit 0; command argv SHA-256
  2a6a5eca83c9f6060f288863588c33f1bbe35a8c6ac82db701c4ff8d4945b470.

- 2026-09-24T19:45:09+00:00: Recorded command exit 0; command argv SHA-256
  f9da2774b0df6431e804390585d848213c1e084b6f27b387a9a56d0be3fc4244.

- 2026-09-24T19:45:23+00:00: Recorded command exit 0; command argv SHA-256
  37c422c5bbac4dcd43eb3d0efafdb22cff608963502aeae8ac7e01b35af4809a.

- 2026-09-24T19:45:42+00:00: Recorded command exit 0; command argv SHA-256
  81651cc4c7f4ab1eb97b677d5d71989a56646776147d75eb43936ade3ec75a46.

- 2026-09-24T19:46:08+00:00: Recorded command exit 0; command argv SHA-256
  e5107e4d1283679910bc2ca2dfc677d1fd756367e9fd1b0ba3bfc5a917329bbe.

- 2026-09-24T19:46:30+00:00: Recorded command exit 0; command argv SHA-256
  377d90cefb534c83f4e4c93fc8d9b8969fdeadc9665c7668d3b61fccdfe87005.

- 2026-09-24T19:46:48+00:00: Recorded command exit 0; command argv SHA-256
  bb352b8e6baaddb9d3de402a3dca1a4aa0b06e91398cb92d40b2064099f0a696.

- 2026-09-24T19:47:05+00:00: Recorded command exit 0; command argv SHA-256
  a36cec07c42242108d530dc4de4a288507e9548109c0918e6f0160654ffc253d.

- 2026-09-24T19:47:19+00:00: Recorded command exit 0; command argv SHA-256
  453ec73d1508d8ad13f8ad10dd3b1dd19b1d5365c8ec56b6add85677253d9b5c.

- 2026-09-24T19:47:38+00:00: Recorded command exit 0; command argv SHA-256
  5666b0a050fc97aa1b3fb26da72b4058350b85ff0e5081b15c12b7ef21d4e3f3.

- 2026-09-24T19:47:53+00:00: Recorded command exit 0; command argv SHA-256
  f407f0389c6d949f3e23f14e21f6a17725297cde91e83383fd75e298011832ce.

- 2026-09-24T19:48:07+00:00: Recorded command exit 0; command argv SHA-256
  3c752766688dda4842b1f16d9fb5e7700ea8a524ad7178c582386c727bd898d0.

- 2026-09-24T19:48:21+00:00: Recorded command exit 0; command argv SHA-256
  7ca3f8d61e2724c7888011b1b015c9a61f815ada816215c678cf52a474d1c159.
