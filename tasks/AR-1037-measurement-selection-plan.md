---
{
  "branch": "feature/measurement-selection-plan",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-11T06:32:03+00:00",
  "depends_on": [
    "AR-0104",
    "AR-1036"
  ],
  "id": "AR-1037",
  "next_action": "After AR-1036, add canonical measurement IDs to validated ASB plans and make collection honor them without any UI code.",
  "observed_branch": "feature/measurement-selection-plan",
  "observed_dirty": 1,
  "observed_head": "1a19b692d724fd5ba1996470daccbfed06171a0a",
  "owner": "codex-root-ar1037-selection-20260911",
  "plan": "../plans/AR-1037.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Carry catalog-backed measurement choices through ASB plan validation, collection and evidence.",
  "task_revision": 6,
  "title": "Add measurement selection to validated run plans",
  "updated_at": "2026-09-11T03:39:20+00:00",
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

- 2026-09-11T03:32:03+00:00: Claimed by codex-root-ar1037-selection-20260911.

- 2026-09-11T03:32:25+00:00: Recorded command exit 0; command argv SHA-256
  e93ce83471cb6810cbe793116d30cf552be146bcaee414eb9dd68d1b35c47e90.
