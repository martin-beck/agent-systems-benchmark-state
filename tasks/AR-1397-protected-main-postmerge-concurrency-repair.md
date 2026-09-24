---
{
  "branch": "repair/ar-1397-protected-main-postmerge-concurrency",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1337"
  ],
  "id": "AR-1397",
  "next_action": "Claim with a gpt-5.6-luna medium worker once the current main queue is quiescent; reproduce c58b0b0 and 130ff91 tree mismatch/cancellation, implement the narrowly scoped signed integration repair, and require a fresh exact-main merge with all seven terminal-success workflows.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "0000000000000000000000000000000000000000",
  "owner": "",
  "plan": "../plans/AR-1397-protected-main-postmerge-concurrency-repair.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "open",
  "summary": "Repair protected-main merge-tree admission and serialize exact post-merge evidence across concurrent main pushes.",
  "task_revision": 3,
  "title": "Protected-main post-merge concurrency and tree repair",
  "updated_at": "2026-09-24T09:25:39+00:00",
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
