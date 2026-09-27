---
{
  "branch": "feature/ar-1489-first-customer-package-consumption",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1461",
    "AR-1462",
    "AR-1488"
  ],
  "id": "AR-1489",
  "next_action": "Promote and claim, then verify exact release package installation and credential-free owner-backed local/mock/replay consumption.",
  "observed_branch": "feature/ar-1489-first-customer-package-consumption",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1489-first-customer-package-consumption.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "open",
  "summary": "Verify first-customer release package installation and owner-backed local/mock/replay consumption.",
  "task_revision": 2,
  "title": "First-customer package consumption",
  "updated_at": "2026-09-27T15:08:05+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1489-first-customer-package-consumption"
}
---

Dependency-safe successor after AR-1488. It verifies the package/install
boundary and a fresh credential-free local/mock/replay journey without
touching asb-tui or requiring a live provider.

- 2026-09-27T15:05:00+00:00: Created after AR-1488 completion to close the
  remaining fresh package installation and consumption evidence gap.

- 2026-09-27T15:08:05+00:00: Dependencies AR-1461, AR-1462, and AR-1488 are done. Promote ASB-only
  first-customer package/install consumption qualification with local/mock/replay evidence.
