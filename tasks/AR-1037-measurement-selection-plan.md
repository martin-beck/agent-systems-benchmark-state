---
{
  "branch": "feature/measurement-selection-plan",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-0104",
    "AR-1036"
  ],
  "id": "AR-1037",
  "next_action": "After AR-1036, add canonical measurement IDs to validated ASB plans and make collection honor them without any UI code.",
  "owner": "",
  "plan": "../plans/AR-1037.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "open",
  "summary": "Carry catalog-backed measurement choices through ASB plan validation, collection and evidence.",
  "task_revision": 2,
  "title": "Add measurement selection to validated run plans",
  "updated_at": "2026-09-11T03:31:52+00:00",
  "worktree_key": "agent-systems-benchmark-measurement-selection-plan"
}
---
## AR-1037

Implement only the ASB runner/control semantics required to make measurement choices real: closed
plan fields, catalog validation, canonical hashing, source gating and evidence provenance. All
search, group tri-state behavior, selection/deselection controls, rendering and help remain
exclusively in `martin-beck/asb-tui` under AR-1014.

- 2026-09-11T03:31:52+00:00: Dependencies AR-0104 and AR-1036 are done; fully green protected-main
  descendant 1a19b692 qualifies the catalog control boundary. Promote ASB-only measurement selection
  semantics with no frontend implementation.
