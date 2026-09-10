---
{
  "branch": "refactor/remove-legacy-in-tree-tui",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1024", "AR-1025"],
  "id": "AR-1029",
  "next_action": "Remove the legacy ASB renderer only after the standalone application and trusted router are complete.",
  "owner": "",
  "plan": "../plans/AR-1029.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Ensure agent-systems-benchmark contains no TUI renderer or terminal application implementation.",
  "task_revision": 1,
  "title": "Remove the legacy in-tree TUI implementation",
  "updated_at": "2026-09-10T19:20:00+00:00",
  "worktree_key": "agent-systems-benchmark-remove-legacy-in-tree-tui"
}
---
After the standalone frontend and lifecycle router are proven, remove the legacy `crates/asb-tui`
implementation and every ASB-owned renderer/runtime dependency. Preserve only protocol, installer,
router, runner, and conformance surfaces in ASB.
