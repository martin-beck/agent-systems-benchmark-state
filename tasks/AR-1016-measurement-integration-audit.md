---
{
  "branch": "feature/measurement-integration-audit",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1014", "AR-1015", "AR-1002", "AR-1007"],
  "id": "AR-1016",
  "next_action": "Add end-to-end live/replay comparison, release documentation, and independent audit after AR-1014 and AR-1015.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1016.md",
  "priority": "P2",
  "schema_version": 1,
  "status": "planned",
  "summary": "Audit selectable and CSB-backed measurements across live and replay runs.",
  "task_revision": 1,
  "title": "Integrate and audit measurement selection and CSB evidence",
  "updated_at": "2026-09-10T00:00:00+00:00",
  "worktree_key": "agent-systems-benchmark-measurement-integration-audit"
}
---
Verify that TUI-selected measurements produce identical validated plans for CLI, live, and replay
execution, and that CSB-backed signals compare without semantic or unit drift. Add end-to-end fixtures,
redaction/provenance checks, reproducibility and artifact/SBOM evidence, and user documentation.

Acceptance criteria: live/replay parity tests, comparison reports grouped by semantic category,
explicit missing/unsupported evidence, exact-head CI, independent diff/privacy/license review, and
release notes documenting capabilities and limits.
