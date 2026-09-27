---
{
  "branch": "feature/ar-1472-authenticated-live-dispatch-adapter",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1373", "AR-1363"],
  "id": "AR-1472",
  "next_action": "Promote and implement the authenticated control-to-runtime live-dispatch adapter with local/mock tests; do not synthesize authority.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1472-authenticated-live-dispatch-adapter.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Connect authenticated control receipts to runtime-owned CLI live dispatch without a dependency cycle.",
  "task_revision": 1,
  "title": "Authenticated live-dispatch adapter",
  "updated_at": "2026-09-27T01:33:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1472-authenticated-live-dispatch-adapter"
}
---

Successor for the circular AR-1374/AR-1375 dependency. It must not touch
asb-tui, require a live provider, expose credentials, or fabricate runtime
authority. Mandatory qualification is deterministic local/mock or replay.

- 2026-09-27T01:33:00+00:00: Created after AR-1374 current-main audit found
  AR-1375 circularly depended on the blocked dispatch AR. Depends only on
  completed authenticated receipt-source ARs.
