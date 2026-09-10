---
{
  "branch": "docs/asb-cli-workflow-captures",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-0872"],
  "id": "AR-1028",
  "next_action": "Generate deterministic privacy-safe ASB CLI workflow captures without importing terminal UI dependencies.",
  "owner": "",
  "plan": "../plans/AR-1028.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "planned",
  "summary": "Produce reproducible ASB CLI transcripts separately from standalone TUI screenshots.",
  "task_revision": 1,
  "title": "Generate ASB CLI workflow captures",
  "updated_at": "2026-09-10T19:20:00+00:00",
  "worktree_key": "agent-systems-benchmark-asb-cli-workflow-captures"
}
---
Generate documentation transcripts from actual synthetic ASB CLI executions. This AR owns no
renderer, terminal application, Ratatui/Crossterm dependency, or asb-tui source.
