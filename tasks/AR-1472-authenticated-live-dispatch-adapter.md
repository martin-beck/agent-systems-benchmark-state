---
{
  "branch": "feature/ar-1472-authenticated-live-dispatch-adapter",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-27T03:34:43+00:00",
  "depends_on": [
    "AR-1373",
    "AR-1363"
  ],
  "id": "AR-1472",
  "next_action": "Promote and implement the authenticated control-to-runtime live-dispatch adapter with local/mock tests; do not synthesize authority.",
  "observed_branch": "feature/ar-1472-authenticated-live-dispatch-adapter",
  "observed_dirty": 0,
  "observed_head": "4ee5a4ed843c7dd7dda0b92dbe392f3787b4039f",
  "owner": "ar1332_record_replay_luna56",
  "plan": "../plans/AR-1472-authenticated-live-dispatch-adapter.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Connect authenticated control receipts to runtime-owned CLI live dispatch without a dependency cycle.",
  "task_revision": 5,
  "title": "Authenticated live-dispatch adapter",
  "updated_at": "2026-09-27T01:35:55+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1472-authenticated-live-dispatch-adapter"
}
---

Successor for the circular AR-1374/AR-1375 dependency. It must not touch
asb-tui, require a live provider, expose credentials, or fabricate runtime
authority. Mandatory qualification is deterministic local/mock or replay.

- 2026-09-27T01:33:00+00:00: Created after AR-1374 current-main audit found
  AR-1375 circularly depended on the blocked dispatch AR. Depends only on
  completed authenticated receipt-source ARs.

- 2026-09-27T01:34:40+00:00: Circular AR-1374/AR-1375 dependency repaired; dependencies AR-1373 and
  AR-1363 are done. Implement the narrow authenticated adapter successor.

- 2026-09-27T01:34:43+00:00: Claimed by ar1332_record_replay_luna56.

- 2026-09-27T01:35:44+00:00: Recorded command exit 0; command argv SHA-256
  59bb9a1153647e6dc218582c1538eb832e176b1bda204242704cd5898afc7806.
