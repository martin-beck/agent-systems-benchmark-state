---
{
  "branch": "build/ratatui-dependency-closure",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1017"],
  "id": "AR-1030",
  "next_action": "Resolve the exact Ratatui release dependency closure through a reviewed upstream feature or narrowly justified fail-closed policy decision.",
  "owner": "",
  "plan": "../plans/AR-1030.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "open",
  "summary": "Make the maintained Ratatui release consumable by standalone asb-tui without hiding supply-chain exceptions.",
  "task_revision": 1,
  "title": "Resolve the Ratatui dependency closure",
  "updated_at": "2026-09-10T19:50:00+00:00",
  "worktree_key": "agent-systems-benchmark-asb-tui-ratatui-dependency-closure"
}
---
The exact Ratatui 0.30.2 graph is advisory-clean but fails the repository's zero-exception
supply-chain policy because it necessarily contains Zlib-licensed foldhash, hashbrown 0.16/0.17,
and syn 2/3. Resolve this visibly before AR-1010 adds a renderer.
