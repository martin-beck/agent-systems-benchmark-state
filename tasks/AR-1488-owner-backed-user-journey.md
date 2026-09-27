---
{
  "branch": "feature/ar-1488-owner-backed-user-journey",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1441",
    "AR-1442",
    "AR-1450",
    "AR-1455",
    "AR-1487"
  ],
  "id": "AR-1488",
  "next_action": "Promote and claim, then qualify the owner-backed install/setup/run/sweep/replay/evidence journey on current protected main.",
  "observed_branch": "feature/ar-1488-owner-backed-user-journey",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1488-owner-backed-user-journey.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "open",
  "summary": "Qualify the owner-backed first-customer install, operation, replay, evidence, and cleanup journey.",
  "task_revision": 2,
  "title": "Owner-backed first-customer user journey",
  "updated_at": "2026-09-27T14:38:20+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1488-owner-backed-user-journey"
}
---

Dependency-safe successor after AR-1487. This is ASB-only and uses local/mock
and strict offline replay evidence; it does not modify asb-tui or require a
live provider.

- 2026-09-27T14:40:00+00:00: Created after AR-1487 completed with owner-backed
  run/sweep, replay, evidence, recovery, and teardown qualification. This
  successor composes the supported install/setup and user-facing workflow into
  one bounded first-customer acceptance path.

- 2026-09-27T14:38:20+00:00: Dependencies AR-1441, AR-1442, AR-1450, AR-1455, and AR-1487 are done.
  Promote ASB-only owner-backed first-customer install/setup/run/sweep/replay/evidence
  qualification; no asb-tui or live provider.
