---
{
  "branch": "feature/ar-1231-strict-replay-execution-seam",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-16T03:40:25+00:00",
  "depends_on": [
    "AR-0505",
    "AR-1100",
    "AR-1230"
  ],
  "id": "AR-1231",
  "next_action": "Planned prerequisite for AR-1151: implement the versioned strict-replay adapter/run-path seam, process egress denial, and bounded cancellation/restart recovery with complete positive and negative evidence.",
  "observed_branch": "feature/ar-1231",
  "observed_dirty": 0,
  "observed_head": "a83ba8e278e40b538160e87a2a40c0fb26418dae",
  "owner": "asb_ar1231_replay_seam",
  "plan": "../plans/AR-1231.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Execute real agents through strict replay without provider egress or live fallback.",
  "task_revision": 6,
  "title": "Strict replay execution and egress-isolation seam",
  "updated_at": "2026-09-16T01:40:25+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1231"
}
---

- 2026-09-16T01:32:00+00:00: Created from the AR-1151 implementation audit. The existing CLI
  replay command only decodes/indexes/selects cassettes and emits metadata; no adapter-facing
  launch seam passes `StrictReplayService`, and network denial is declarative only. AR-1151 must
  consume this prerequisite before claiming executable strict replay.

- 2026-09-16T01:37:59+00:00: Dependencies AR-0505, AR-1100 and AR-1230 are done; promote strict
  replay execution seam.

- 2026-09-16T01:38:02+00:00: Claimed by asb_ar1231_replay_seam.

- 2026-09-16T01:38:13+00:00: Recorded command exit 0; command argv SHA-256
  5e07e0e6986aeb142788e646e8cc7f05df4d452a96f447c0bbaee46f095dd24e.

- 2026-09-16T01:40:25+00:00: Heartbeat by asb_ar1231_replay_seam.
