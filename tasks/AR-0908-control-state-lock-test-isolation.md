---
{
  "branch": "fix/control-state-lock-test-isolation",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-09T22:41:04+00:00",
  "depends_on": [
    "AR-0101",
    "AR-0102",
    "AR-0103",
    "AR-0875"
  ],
  "id": "AR-0908",
  "next_action": "Reproduce the post-drop lock failure under coverage and parallel stress, then harden only the embedded control-state test roots without weakening production locking.",
  "owner": "contracts_20260906",
  "plan": "../plans/AR-0908.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Harden asb-cli control-state lock test isolation and deterministic reopen coverage.",
  "task_revision": 5,
  "title": "Harden control-state lock test isolation",
  "updated_at": "2026-09-09T19:42:01+00:00",
  "worktree_key": "agent-systems-benchmark-control-state-lock-test-isolation"
}
---
## AR-0908

Repair the isolated `asb-cli` control-state ownership test boundary exposed by Repository Quality
run 34339927858. The observed failure occurred when reopening after dropping the original backend;
an unchanged focused test subsequently passed repeatedly, so preserve the incident as a
non-deterministic isolation signal rather than claiming a production lock defect without evidence.


- 2026-09-09T19:39:36+00:00: Dependencies AR-0101, AR-0102, AR-0103 and AR-0875 are durably done;
  focused embedded-test-only scope is disjoint from active product lanes.

- 2026-09-09T19:41:04+00:00: Claimed by contracts_20260906.

- 2026-09-09T19:41:27+00:00: Recorded command exit 0; command argv SHA-256
  5345cd4b5f66285dc80cddfe59c0a95475263f9ff88d25d2639fce3c300aa4b9.

- 2026-09-09T19:42:01+00:00: Recorded command exit 1; command argv SHA-256
  63c858d759cea8e2caca2e0c4088189d3f96da31efdb75cb6464ce4089512f2c.
