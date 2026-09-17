---
{
  "branch": "repair/ar-1295-vendor-fixtures",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-17T07:11:59+00:00",
  "depends_on": [],
  "id": "AR-1295",
  "next_action": "Update stale coordinator vendor test fixtures from v0.3.5 to verified immutable v0.3.7 and rerun the complete state test suite without changing vendor or handoffctl code.",
  "observed_branch": "repair/ar-1295-vendor-fixtures",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "asb-ar1295-vendor-tests",
  "plan": "../plans/AR-1295.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Align stale coordinator vendor tests with the verified immutable v0.3.7 pin.",
  "task_revision": 4,
  "title": "Coordinator vendor v0.3.7 fixture alignment",
  "updated_at": "2026-09-17T05:12:05+00:00",
  "worktree_key": "agent-systems-benchmark-state-ar-1295-vendor-fixtures"
}
---

## AR-1295

AR-1294 restored the exact v0.3.7 coordinator payload and manifest. Existing
vendor tests still encode the superseded v0.3.5 fixture. This AR owns only the
fixture/test expectation update and must not alter vendor implementation,
handoffctl, formal runner behavior, ASB product, or asb-tui.

- 2026-09-17T05:11:42+00:00: Verified immutable v0.3.7 payload is present; stale v0.3.5 fixtures are
  an independent deterministic gate defect.

- 2026-09-17T05:11:59+00:00: Claimed by asb-ar1295-vendor-tests.

- 2026-09-17T05:12:05+00:00: Recorded command exit 0; command argv SHA-256
  d86cbe2231c7a3eb40e69e7556d13b1a845c3940bec346e84ad1d3f700d9ba9c.
