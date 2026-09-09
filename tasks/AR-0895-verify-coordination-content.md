---
{
  "branch": "ci/verify-coordination-content",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-09T12:42:20+00:00",
  "depends_on": [
    "AR-0002",
    "AR-0003"
  ],
  "id": "AR-0895",
  "next_action": "Run full state workflow/schema/generated-view/DCO/failure gates, add any missing hostile trigger cases, then create a focused signed+DCO candidate for independent review.",
  "owner": "quality_20260906",
  "plan": "../plans/AR-0895.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Close the workflow path-filter gap that lets coordination-content pull requests skip strict state consistency and DCO checks.",
  "task_revision": 7,
  "title": "Verify every coordination-content pull request",
  "updated_at": "2026-09-09T09:45:43+00:00",
  "worktree_key": "agent-systems-benchmark-state-verify-coordination-content"
}
---
## AR-0895

Ensure state-content pull requests cannot bypass exact-head schema, generated-view, quality, and DCO enforcement merely because they change only tasks, plans, CURRENT.md, or STATUS.md.

- 2026-09-09T09:42:17+00:00: Selected as the highest-priority compatible dependency-ready task after
  AR-0806 release. P0 tasks remain dependency-blocked; AR-0704 requires external cost/provider
  authorization, AR-0832 owns runner operations, and AR-0890 overlaps active provider/workflow
  integration. AR-0895 is an isolated state-workflow quality lane with AR-0002/AR-0003 done and no
  active path-owner conflict.

- 2026-09-09T09:42:20+00:00: Claimed by quality_20260906.

- 2026-09-09T09:42:43+00:00: Recorded command exit 0; command argv SHA-256
  57554c6619b70809ba3ccdce153dfad37279c32430a38a85fa9f7ed6213db671.

- 2026-09-09T09:45:01+00:00: Recorded command exit 1; command argv SHA-256
  2a4c67d241f80d805bccd3372fd408f4c1b0043b668039f4a37edc72f1b12d24.

- 2026-09-09T09:45:18+00:00: Recorded command exit 0; command argv SHA-256
  e562a9834b4289195fedd27f1b1f9f3020d3485e8cfe49b86dcd7689a2fa9df6.

- 2026-09-09T09:45:43+00:00: Created declared isolated worktree
  /srv/data/projects/agent-systems-benchmark-state-verify-coordination-content on branch
  ci/verify-coordination-content at state base 3a66c5b6. First implementation slice is dirty only in
  .github/workflows/verify.yml, README.md, and new tests/test_workflow_triggers.py. Both push and
  pull_request filters now include tasks/**, plans/**, CURRENT.md, STATUS.md, and the trigger
  regression itself. Three focused tests prove each required path,
  mixed/deleted/renamed/generated-only routing, unrelated-doc exclusion, checker self-routing, exact
  PR-head checkout, fetch-depth zero, and complete base..head DCO revision enumeration. Corrected
  one deterministic Ruff import-order finding; final focused unittest 3/3, Ruff, strict mypy, and
  diff-check pass.
