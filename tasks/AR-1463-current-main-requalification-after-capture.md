---
{
  "branch": "qualification/ar-1463-current-main-requalification-after-capture",
  "checkpoint_commit": "01b70e87ce8e7913f614447c0c530cb22e235256",
  "claim_expires": "2026-09-26T22:47:57+00:00",
  "depends_on": [
    "AR-1330",
    "AR-1461"
  ],
  "id": "AR-1463",
  "next_action": "Promote and qualify exact protected main after AR-1330 across the first-customer install, local/mock benchmark, capture/replay, recovery, privacy and release gates; publish no release unless all gates pass.",
  "observed_branch": "qualification/ar-1463-current-main-requalification-after-capture",
  "observed_dirty": 0,
  "observed_head": "01b70e87ce8e7913f614447c0c530cb22e235256",
  "owner": "coordinator-ar1463-requal",
  "plan": "../plans/AR-1463.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Requalify current protected main for first-customer production-like use after capture/replay integration.",
  "task_revision": 8,
  "title": "Current-main first-customer requalification after capture integration",
  "updated_at": "2026-09-26T20:49:40+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1463-current-main-requalification-after-capture"
}
---

This P0 assurance AR closes the evidence gap created when AR-1330 advanced
protected main after the first-customer release. It must qualify the exact
current main with the mandatory credential-free local/mock paths and strict
offline capture/replay, while preserving all privacy, cancellation, cleanup,
egress-denial, formal, supply-chain and release gates. External provider
reachability, native ARM hardware, asb-tui changes and external signing are not
required. Any release decision must remain fail-closed and exact-head bound.

- 2026-09-26T20:48:00+00:00: Created because AR-1330 merged after the v0.1.0
  release; prior first-customer evidence did not cover the new protected-main
  capture/replay implementation.

- 2026-09-26T20:47:02+00:00: AR-1330 capture integration is merged; promote current-main
  first-customer requalification at exact merge 01b70e87ce8e7913f614447c0c530cb22e235256.

- 2026-09-26T20:47:05+00:00: Claimed by coordinator-ar1463-requal.

- 2026-09-26T20:47:57+00:00: Heartbeat by coordinator-ar1463-requal.

- 2026-09-26T20:49:00+00:00: Recorded command exit 0; command argv SHA-256
  ff6d1fa7a7185010f75fcfafe4bdc1bdd5b9804d8c2b3e7abdd8a1b96cd81c63.

- 2026-09-26T20:49:18+00:00: Recorded command exit 0; command argv SHA-256
  6840d2f0cea6f9cf6ffce81b9b1b74dcdddaff8701fc6cc1705c309033813254.

- 2026-09-26T20:49:40+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.
