---
{
  "branch": "fix/tmux-nested-server-connect-diagnostics-signed",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1062"
  ],
  "id": "AR-1063",
  "next_action": "After reviewed state integration, promote and publish one signed diagnostic commit on exact asb-tui main; require exact-head and Trusted-main evidence before AR-1010 can advance.",
  "owner": "",
  "plan": "../plans/AR-1063.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Publish and qualify the exact AR-1062 tmux diagnostics.",
  "task_revision": 1,
  "title": "Publish nested tmux diagnostics",
  "updated_at": "2026-09-13T20:10:00+00:00",
  "worktree_key": "agent-systems-benchmark-asb-tui-tmux-nested-diagnostics-publication"
}
---

## AR-1063

Publish the already-tested AR-1062 diagnostic diff through one cryptographically signed commit and
protected `asb-tui` pull request, then use exact-main Trusted evidence to select any later behavioral
repair. This successor preserves AR-1062's terminal history because the coordinator has no supported
`done`-to-`open` transition.

The unsigned source commit is `defffe34caf27ac293dee34d12ada5c30a3aea17`; signed child
`6d0fe4b986f23077066c87b5bf019fac5d889c63` attests the same tree but cannot be published because
its range retains the unsigned parent. Both identify tree `0a84455ca544a68999721e4744dc8c885071154d`
and are evidence inputs only, never publication authority.
