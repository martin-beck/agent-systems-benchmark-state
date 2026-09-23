---
{
  "branch": "feature/ar-1364-authenticated-chain-enrollment",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-24T01:30:25+00:00",
  "depends_on": [
    "AR-1362"
  ],
  "id": "AR-1364",
  "next_action": "Promote after AR-1362 is done, then add authenticated certificate-chain enrollment/materialization for the control receipt source.",
  "observed_branch": "feature/ar-1364-authenticated-chain-enrollment",
  "observed_dirty": 1,
  "observed_head": "e9d4d3d1c6a4d67d0ce0e49fa8eaf696561fe45e",
  "owner": "codex-asb-runtime-attested-enrollment-luna56",
  "plan": "../plans/AR-1364-authenticated-chain-enrollment.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Materialize authenticated certificate-chain authority for control-owned runtime receipt issuance.",
  "task_revision": 5,
  "title": "Authenticated chain enrollment",
  "updated_at": "2026-09-23T23:31:40+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1364-authenticated-chain-enrollment"
}
---

Successor for blocked AR-1363, explicitly depending on AR-1362. Do not touch
asb-tui or synthesize certificate authority from CLI/config input.

- 2026-09-24T00:00:00+00:00: Created after AR-1363 found the control backend
  has no authenticated certificate-chain material or runtime-owned issuer.

- 2026-09-23T23:30:22+00:00: Promote authenticated certificate-chain enrollment successor after
  AR-1363 found no control-owned chain materialization.

- 2026-09-23T23:30:25+00:00: Claimed by codex-asb-runtime-attested-enrollment-luna56.

- 2026-09-23T23:31:30+00:00: Recorded command exit 0; command argv SHA-256
  060858f3c09d8a7ce03dfae54a20a77cf22bbd921bdbef41e45dd9ebed4ea5fa.
