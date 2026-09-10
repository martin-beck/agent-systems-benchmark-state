---
{
  "branch": "feature/tui-ratatui-crossterm-foundation",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-10T01:43:48+00:00",
  "depends_on": [
    "AR-0803",
    "AR-0804",
    "AR-0805",
    "AR-0806"
  ],
  "id": "AR-1010",
  "next_action": "Adopt pinned Ratatui and Crossterm dependencies in an isolated TUI worktree, then implement the capability-aware application shell and event loop.",
  "observed_branch": "feature/tui-ratatui-crossterm-foundation",
  "observed_dirty": 0,
  "observed_head": "b6d04a8305ce6d49cc327e4e6d2d6fa42a88050b",
  "owner": "replay_20260906",
  "plan": "../plans/AR-1010.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Adopt Ratatui and Crossterm as the supported professional TUI foundation.",
  "task_revision": 5,
  "title": "Adopt Ratatui/Crossterm TUI foundation",
  "updated_at": "2026-09-10T00:26:51+00:00",
  "worktree_key": "agent-systems-benchmark-tui-ratatui-crossterm-foundation"
}
---
## AR-1010

Adopt Ratatui with Crossterm as the supported ASB terminal UI foundation.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-09T23:43:45+00:00: All dependencies AR-0803, AR-0804, AR-0805, and AR-0806 are durably
  done. No remote branch, PR, or declared worktree exists. Owned asb-tui/workspace dependency scope
  is disjoint from active AR-0909 mini_swe.rs, AR-0859 OpenJiuwen live fixtures, and held formal
  lanes; no active Cargo/schema fence was found.

- 2026-09-09T23:43:48+00:00: Claimed by replay_20260906.

- 2026-09-10T00:26:45+00:00: Recorded command exit 0; command argv SHA-256
  32365df186a2a78c0fd3c125d218afd1ecfff97ce53e357fb3dcc527a42e60fc.
