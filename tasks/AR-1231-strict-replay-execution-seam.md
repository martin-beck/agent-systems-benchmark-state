---
{
  "branch": "feature/ar-1231-strict-replay-execution-seam",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-0505",
    "AR-1100",
    "AR-1230"
  ],
  "id": "AR-1231",
  "next_action": "Planned prerequisite for AR-1151: implement the versioned strict-replay adapter/run-path seam, process egress denial, and bounded cancellation/restart recovery with complete positive and negative evidence.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1231.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Execute real agents through strict replay without provider egress or live fallback.",
  "task_revision": 1,
  "title": "Strict replay execution and egress-isolation seam",
  "updated_at": "2026-09-16T01:32:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1231"
}
---

- 2026-09-16T01:32:00+00:00: Created from the AR-1151 implementation audit. The existing CLI
  replay command only decodes/indexes/selects cassettes and emits metadata; no adapter-facing
  launch seam passes `StrictReplayService`, and network denial is declarative only. AR-1151 must
  consume this prerequisite before claiming executable strict replay.
