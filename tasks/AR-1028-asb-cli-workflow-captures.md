---
{
  "branch": "docs/asb-cli-workflow-captures",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-10T23:01:59+00:00",
  "depends_on": [
    "AR-0872"
  ],
  "id": "AR-1028",
  "next_action": "Generate deterministic privacy-safe ASB CLI workflow captures without importing terminal UI dependencies.",
  "owner": "codex-ar1028-cli-captures-20260910",
  "plan": "../plans/AR-1028.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Produce reproducible ASB CLI transcripts separately from standalone TUI screenshots.",
  "task_revision": 3,
  "title": "Generate ASB CLI workflow captures",
  "updated_at": "2026-09-10T20:01:59+00:00",
  "worktree_key": "agent-systems-benchmark-asb-cli-workflow-captures"
}
---
Generate documentation transcripts from actual synthetic ASB CLI executions. This AR owns no
renderer, terminal application, Ratatui/Crossterm dependency, or asb-tui source.

- 2026-09-10T20:01:56+00:00: AR-0872 is durably done; CLI-only capture scope is dependency-ready and
  disjoint from all standalone TUI work.

- 2026-09-10T20:01:59+00:00: Claimed by codex-ar1028-cli-captures-20260910.
