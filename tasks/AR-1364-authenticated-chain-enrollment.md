---
{
  "branch": "feature/ar-1364-authenticated-chain-enrollment",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1362"
  ],
  "id": "AR-1364",
  "next_action": "Promote after AR-1362 is done, then add authenticated certificate-chain enrollment/materialization for the control receipt source.",
  "observed_branch": "feature/ar-1364-authenticated-chain-enrollment",
  "observed_dirty": 0,
  "observed_head": "e9d4d3d1c6a4d67d0ce0e49fa8eaf696561fe45e",
  "owner": "",
  "plan": "../plans/AR-1364-authenticated-chain-enrollment.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Materialize authenticated certificate-chain authority for control-owned runtime receipt issuance.",
  "task_revision": 1,
  "title": "Authenticated chain enrollment",
  "updated_at": "2026-09-24T00:00:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1364-authenticated-chain-enrollment"
}
---

Successor for blocked AR-1363, explicitly depending on AR-1362. Do not touch
asb-tui or synthesize certificate authority from CLI/config input.

- 2026-09-24T00:00:00+00:00: Created after AR-1363 found the control backend
  has no authenticated certificate-chain material or runtime-owned issuer.
