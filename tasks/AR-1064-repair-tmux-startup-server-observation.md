---
{
  "branch": "fix/tmux-startup-server-observation-recovery",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1062"
  ],
  "id": "AR-1064",
  "next_action": "After AR-1063 publishes the diagnostic candidate and exact-main evidence confirms the same failure, promote this repair and isolate the first failing startup/server predicate before changing any behavior.",
  "owner": "",
  "plan": "../plans/AR-1064.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Repair the proven asb-tui tmux startup/server observation failure without weakening authority or cleanup.",
  "task_revision": 1,
  "title": "Repair tmux startup and server observation",
  "updated_at": "2026-09-14T12:30:00+00:00",
  "worktree_key": "agent-systems-benchmark-asb-tui-tmux-startup-server-observation-recovery"
}
---

Trusted-main run `34831918221` at exact asb-tui main `db612b6f07029b34caf7a80998b6cd1b10929567`
failed 5/31 terminal-foundation tests. AR-1063 must first publish the diagnostic-only candidate and
reproduce the failure on exact main; this repair is not permission to bypass that publication gate.
No ASB source, Ratatui renderer, application UI, lifecycle protocol, dependency, release workflow,
authentication, or coordinator state is in scope.

- 2026-09-14T12:30:00+00:00: Reserved after live Trusted-main evidence showed all five affected
  fixtures failing below their intended assertions. AR-1063 already occupies the publication
  successor for AR-1062; AR-1064 is the next unused identifier and owns only the later behavioral
  repair.
