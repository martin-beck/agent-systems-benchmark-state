---
{
  "branch": "qualification/ar-1447-asb-local-campaign",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-25T17:27:16+00:00",
  "depends_on": [
    "AR-1433",
    "AR-1437",
    "AR-1442"
  ],
  "id": "AR-1447",
  "next_action": "Remain planned until local mock AR-1433, recording/replay AR-1437, and ASB setup AR-1442 are released; then qualify the existing bounded easy run/sweep and offline local campaign journey. The broader AR-1338 interactive wrapper remains a separate enhancement.",
  "observed_branch": "main",
  "observed_dirty": 7,
  "observed_head": "bd7d10d4a760a84fa42de2b1fa9e97e8ea85ba09",
  "owner": "coordinator-ar1447",
  "plan": "../plans/AR-1447.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Qualify the complete credential-free ASB local campaign and replay journey.",
  "task_revision": 5,
  "title": "ASB local campaign qualification",
  "updated_at": "2026-09-25T15:27:49+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1447"
}
---

This is the ASB-only local campaign gate. It intentionally does not replace or
close the optional live capture chain AR-1330 through AR-1333.

- 2026-09-25T15:40:00+00:00: Created to separate first-customer credential-free
  qualification from optional live-provider capture dependencies.

- 2026-09-25T15:27:13+00:00: Local ASB campaign qualification is dependency-ready: AR-1433, AR-1437
  and ASB CLI setup AR-1442 are released. Optional live capture and broad wrapper remain separate.

- 2026-09-25T15:27:16+00:00: Claimed by coordinator-ar1447.

- 2026-09-25T15:27:34+00:00: Recorded command exit 0; command argv SHA-256
  b90815e56704d6579354b40d8bbf8af9f68ad57bc438b40ba42c594845b7247d.
