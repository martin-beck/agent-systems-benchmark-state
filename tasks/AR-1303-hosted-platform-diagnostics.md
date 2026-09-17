---
{
  "branch": "feature/ar-1303-hosted-platform-diagnostics",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-17T14:17:33+00:00",
  "depends_on": [
    "AR-0907",
    "AR-1252"
  ],
  "id": "AR-1303",
  "next_action": "Promote only after confirming AR-1301 remains blocked and no worker owns the hosted platform tooling; then implement fixed privacy-safe failure classifications and tests without weakening the fail-closed gate.",
  "observed_branch": "feature/ar-1303-hosted-platform-diagnostics",
  "observed_dirty": 0,
  "observed_head": "7ea3e001dffa13eca5ff0f05444c2b3b9d4df928",
  "owner": "ar1303_ci_diagnostics",
  "plan": "../plans/AR-1303.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Add privacy-safe fixed diagnostics for hosted platform evidence failures.",
  "task_revision": 5,
  "title": "Privacy-safe hosted platform failure diagnostics",
  "updated_at": "2026-09-17T12:18:23+00:00",
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

- 2026-09-17T12:17:30+00:00: Dependencies AR-0907 and AR-1252 are done; promote CI diagnostics
  follow-up for repeated AR-1301 hosted platform failures.

- 2026-09-17T12:17:33+00:00: Claimed by ar1303_ci_diagnostics.

- 2026-09-17T12:18:15+00:00: Recorded command exit 0; command argv SHA-256
  633f1b0dff81a4b4b88f3c9fa5dbfb5676db285dc905a2996fa23829bc079873.
