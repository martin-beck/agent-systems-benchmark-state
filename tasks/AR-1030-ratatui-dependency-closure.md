---
{
  "branch": "build/ratatui-dependency-closure",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-10T22:52:14+00:00",
  "depends_on": [
    "AR-1017"
  ],
  "id": "AR-1030",
  "next_action": "Resolve the exact Ratatui release dependency closure through a reviewed upstream feature or narrowly justified fail-closed policy decision.",
  "owner": "codex-ar1030-ratatui-policy-20260910",
  "plan": "../plans/AR-1030.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Make the maintained Ratatui release consumable by standalone asb-tui without hiding supply-chain exceptions.",
  "task_revision": 5,
  "title": "Resolve the Ratatui dependency closure",
  "updated_at": "2026-09-10T19:52:20+00:00",
  "worktree_key": "agent-systems-benchmark-asb-tui-ratatui-dependency-closure"
}
---
The exact Ratatui 0.30.2 graph is advisory-clean but fails the repository's zero-exception
supply-chain policy because it necessarily contains Zlib-licensed foldhash, hashbrown 0.16/0.17,
and syn 2/3. Resolve this visibly before AR-1010 adds a renderer.

- 2026-09-10T19:50:04+00:00: Claimed by codex-ar1030-ratatui-policy-20260910.

- 2026-09-10T19:50:21+00:00: Recorded command exit 0; command argv SHA-256
  7e0d0efe0ae08a4c308f06db576693eff2b55df1b1195c580afd000b6237ceef.

- 2026-09-10T19:52:14+00:00: Heartbeat by codex-ar1030-ratatui-policy-20260910.

- 2026-09-10T19:52:20+00:00: Recorded command exit 0; command argv SHA-256
  70c299ac34f80fb148951f6d687b81c0133841c6f66036e826bbc90974c0544e.
