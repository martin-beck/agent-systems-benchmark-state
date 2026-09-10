---
{
  "branch": "feature/standalone-asb-tui-application",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-0804", "AR-0805", "AR-0806", "AR-0870", "AR-0871", "AR-1010", "AR-1022", "AR-1023"],
  "id": "AR-1025",
  "next_action": "Port the reviewed frontend state machines into the standalone repository and connect a real Ratatui application to the versioned ASB control protocol.",
  "owner": "",
  "plan": "../plans/AR-1025.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Deliver the actual standalone interactive asb-tui application without an ASB workspace dependency.",
  "task_revision": 1,
  "title": "Build the standalone asb-tui application",
  "updated_at": "2026-09-10T19:00:00+00:00",
  "worktree_key": "agent-systems-benchmark-standalone-asb-tui-application"
}
---
Move reviewed behavior from the legacy in-tree frontend into the separate repository, add the real
Ratatui/Crossterm renderer and implement the bounded owner-authenticated ASB control wire client.
The standalone source must not depend on the ASB Cargo workspace or assume benchmark ownership.

Acceptance requires settings, launch/status/cancel, history/analysis, repeat and record/replay
journeys; terminal restoration and accessibility fallbacks; reconnect and stale-event correctness;
cross-contract fixtures; complete tests and audits; exact-head CI and post-merge verification.
