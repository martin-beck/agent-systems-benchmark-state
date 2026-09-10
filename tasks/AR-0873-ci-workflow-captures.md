---
{
  "branch": "docs/ci-workflow-captures",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-0807",
    "AR-0872"
  ],
  "id": "AR-0873",
  "next_action": "Generate privacy-safe asb-tui workflow screenshots from real synthetic CI executions.",
  "owner": "",
  "plan": "../plans/AR-0873.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Produce reproducible standalone TUI screenshots and text equivalents from workflows executed in CI.",
  "task_revision": 3,
  "title": "Generate asb-tui CI workflow screenshots",
  "updated_at": "2026-09-10T19:20:00+00:00",
  "worktree_key": "agent-systems-benchmark-asb-tui-ci-workflow-captures"
}
---
## AR-0873

Generate documentation screenshots from the same synthetic workflows executed during CI.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-09T10:25:03+00:00: Raised CI TUI workflow capture priority by operator request;
  dependencies and planned status remain unchanged.

- 2026-09-10T19:20:00+00:00: Restricted this AR to standalone asb-tui application captures;
  ASB CLI capture work is tracked separately so renderer dependencies never enter ASB.
