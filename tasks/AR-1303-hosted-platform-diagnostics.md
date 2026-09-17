---
{
  "branch": "feature/ar-1303-hosted-platform-diagnostics",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-0907",
    "AR-1252"
  ],
  "id": "AR-1303",
  "next_action": "Promote only after confirming AR-1301 remains blocked and no worker owns the hosted platform tooling; then implement fixed privacy-safe failure classifications and tests without weakening the fail-closed gate.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1303.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "planned",
  "summary": "Add privacy-safe fixed diagnostics for hosted platform evidence failures.",
  "task_revision": 1,
  "title": "Privacy-safe hosted platform failure diagnostics",
  "updated_at": "2026-09-17T12:15:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1303-hosted-platform-diagnostics"
}
---

## AR-1303

The hosted portability helper currently collapses sandbox spawn failures, nonzero
exits, timeouts, output-limit violations, and evidence/source failures into one
generic error. Add bounded fixed diagnostics for infrastructure debugging while
preserving fail-closed status, privacy, schema compatibility, and the independent
native qualification route. This AR must not modify runtime behavior or asb-tui.

- 2026-09-17T12:15:00+00:00: Created from repeated AR-1301 hosted platform failures;
  local exact collector passes, while hosted jobs 105192558571 and 105195340454 fail.
  No owner or implementation claim yet.
