---
{
  "branch": "repair/ar-1397-protected-main-postmerge-concurrency",
  "checkpoint_commit": "123ba915d2732ee8a6c99fae301bfd64cf0aac4f",
  "claim_expires": "2026-09-24T11:35:34+00:00",
  "depends_on": [
    "AR-1337"
  ],
  "id": "AR-1397",
  "next_action": "PR #286 merged at 123ba915d2732ee8a6c99fae301bfd64cf0aac4f. Monitor exact-main post-merge runs 35983130559, 35983130497, 35983130461, 35983130427, 35983130387, 35983130338, and 35983130335 until all seven are terminal-success; then preserve evidence and release AR-1397 done.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "0000000000000000000000000000000000000000",
  "owner": "ar1397-protected-main-repair-luna56",
  "plan": "../plans/AR-1397-protected-main-postmerge-concurrency-repair.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Repair protected-main merge-tree admission and serialize exact post-merge evidence across concurrent main pushes.",
  "task_revision": 16,
  "title": "Protected-main post-merge concurrency and tree repair",
  "updated_at": "2026-09-24T09:46:35+00:00",
  "worktree_key": ""
}
---

# AR-1397

This repair owns the integration boundary only. It must not change ASB bundle
profiles, workload semantics, OpenRouter behavior, native evidence policy, or
asb-tui. External providers are never required for development evidence.

The prior ARs remain authoritative for their product diffs. This AR may add
only the smallest coordinator/integration-flow repair and its regression tests;
it must retain the default signature-required and exact-tree gates.

- 2026-09-24T09:22:58+00:00: Promote narrowly scoped protected-main post-merge concurrency/tree
  repair after AR-1314 merge c58b0b0 and AR-1395 merge c130ff91 failures; preserve original evidence
  and do not weaken gates.

- 2026-09-24T09:25:39+00:00: Promoted and pushed in signed state commits
  d8f79e433a54a5834041ec3561f9c4725d4595bd and prior AR-1397 creation evidence. Covers AR-1314 merge
  c58b0b0 and AR-1395 merge c130ff91 without altering either AR evidence.

- 2026-09-24T09:25:44+00:00: Claimed by ar1397-protected-main-repair-luna56.

- 2026-09-24T09:27:29+00:00: Heartbeat by ar1397-protected-main-repair-luna56.

- 2026-09-24T09:28:50+00:00: Recorded command exit 0; command argv SHA-256
  2334642cd77a45f898a2584fde2a2a6d012d9a48240a54f211bc956ddffdfcba.

- 2026-09-24T09:34:15+00:00: Recorded command exit 0; command argv SHA-256
  ebfebfed4e3ff9fe1aac20188ed12ece01bb44d2763f29a5f1b52506be21e4b5.

- 2026-09-24T09:34:29+00:00: Recorded command exit 0; command argv SHA-256
  03fc982a4fa7c6e4f71cb0c198b141e1b339c6c8fcb3a1dca3ed2a0dc207cea4.

- 2026-09-24T09:35:01+00:00: Recorded command exit 0; command argv SHA-256
  5bd4bfb2f7842a1096a7f2696b0ff04664193b4c70be381574c8ae521d0f7cfc.

- 2026-09-24T09:35:17+00:00: Recorded command exit 0; command argv SHA-256
  dd728b78c56f26c19fbceb9adb22137c6b8a367b571fd4a11acc2f256d9e99ac.

- 2026-09-24T09:35:34+00:00: Heartbeat by ar1397-protected-main-repair-luna56.

- 2026-09-24T09:35:50+00:00: Implementation committed signed+DCO as
  1bcd946b30a2fa40e27174ebbbecc0af23d82b33 and published as PR #286. Focused 11-test integration
  suite, repository policy, fmt, Clippy, and locked workspace tests passed. PR checks are currently
  in progress; no merge yet.

- 2026-09-24T09:44:59+00:00: Recorded command exit 1; command argv SHA-256
  c31e3e361df5c97d060f9debcf63ff3b5a82541646dcfb236a91aaecb42913dc.

- 2026-09-24T09:45:25+00:00: Recorded command exit 0; command argv SHA-256
  ea6bf194b9186d854702c04d172912279539249edb39b7e80b32922b13d67b8d.

- 2026-09-24T09:45:46+00:00: Recorded command exit 1; command argv SHA-256
  7d4816ae42e593c06430c7ad06c4290cd2b679fc95d5f4362f3c42eeeff72380.

- 2026-09-24T09:46:35+00:00: Protected merge observed and independently verified: PR #286 head
  1bcd946 was merged as 123ba915. The local exact merge command had failed closed earlier when
  target advanced, preserving the invariant. Seven exact-main post-merge workflows dispatched for
  the merge; headers already succeeded.
