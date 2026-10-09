---
{
  "branch": "feature/ar-1760-project-init-workspace",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-09T17:04:33+00:00",
  "depends_on": [
    "AR-1759"
  ],
  "id": "AR-1760",
  "next_action": "Repair complete: update the generated guide command inventory for project init, rerun the workspace gate to terminal success, then review and verify PR #532 exact head.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "codex-asb-ar1760-project-init-20261009",
  "plan": "../plans/AR-1760-project-init-workspace.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "contract-test",
    "evidence_digest": "",
    "evidence_ref": "",
    "spec_ref": "specs/AR-1760.json",
    "spec_revision": 1,
    "status": "pending"
  },
  "spec_ref": "specs/AR-1760.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Add an idempotent ASB project initializer containing config, results, and catalog areas.",
  "task_revision": 22,
  "title": "Initialize an ASB benchmark project workspace",
  "updated_at": "2026-10-09T15:11:54+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1760-project-init-workspace"
}
---

Implement `asb project init [PATH]` using the AR-1759 contract. It must create
the project configuration, results store, and catalog directory in a bounded
project layout, be safe and idempotent, refuse to overwrite unrelated files,
and recover cleanly from partial initialization. It must print the next simple
commands for a fresh user and support `--json` without leaking host secrets.

- 2026-10-09T15:04:30+00:00: AR-1759 schema is merged, accepted, released, and dependency-ready.

- 2026-10-09T15:04:33+00:00: Claimed by codex-asb-ar1760-project-init-20261009.

- 2026-10-09T15:04:43+00:00: Recorded command exit 0; command argv SHA-256
  03d9fe5791f2da017ecf4f0e815462d8fa0df4b590d3db050e5855f3ee6c8b46.

- 2026-10-09T15:04:57+00:00: Recorded command exit 0; command argv SHA-256
  0c9e7e234ecef0ada5ab70152a1b18bee6c8d9e247b80e39b1612a4e2d0a6275.

- 2026-10-09T15:05:04+00:00: Recorded command exit 0; command argv SHA-256
  064e8b6760e2a8b9269baa1776da1b65ee7d2ae0a00f570726f71394792f2b54.

- 2026-10-09T15:06:59+00:00: Recorded command exit 0; command argv SHA-256
  3cf13a5edc254b85c4d447ce67a1ffdea4e2bf581375435f08beb65055741b39.

- 2026-10-09T15:07:10+00:00: Recorded command exit 1; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-09T15:07:21+00:00: Recorded command exit 0; command argv SHA-256
  6f25c271a70927d75fec926d61ffa949ce0ab9d62261aa338a7702469464fc50.

- 2026-10-09T15:07:52+00:00: Recorded command exit 0; command argv SHA-256
  294e7c15e0bfdd7f1b3311b2e9e0aab99a2eb2f22deb9b899e5b2f988bf9825b.

- 2026-10-09T15:08:27+00:00: Recorded command exit 0; command argv SHA-256
  eefa48c34d461da04e4f596fa0c3f390263714e8a8b7d186a2f0527cfa563495.

- 2026-10-09T15:08:41+00:00: Recorded command exit 0; command argv SHA-256
  6f25c271a70927d75fec926d61ffa949ce0ab9d62261aa338a7702469464fc50.

- 2026-10-09T15:08:55+00:00: Recorded command exit 0; command argv SHA-256
  3cf13a5edc254b85c4d447ce67a1ffdea4e2bf581375435f08beb65055741b39.

- 2026-10-09T15:09:06+00:00: Recorded command exit 0; command argv SHA-256
  976af255f2a87000bf8b9e6df4d4ffa3ce971dc172efc9bd36677545bf0aa606.

- 2026-10-09T15:09:16+00:00: Recorded command exit 0; command argv SHA-256
  6e66c73cea40dede94bcf3305a001f15eac900721391c2f1e341f314aa33aca0.

- 2026-10-09T15:09:33+00:00: Recorded command exit 0; command argv SHA-256
  78c5ff54baa515b3bd48741f6b8f8e2482964b95419246f1e73a94ad8819fdda.

- 2026-10-09T15:09:48+00:00: Recorded command exit 0; command argv SHA-256
  d70bd269a0af7ac1ae3bdd120f7a9e2b92023c48f6448cf053be9d11646f2e4d.

- 2026-10-09T15:10:11+00:00: Recorded command exit 101; command argv SHA-256
  534f8613e1c316db8f0f46dd989e44e14a8ca74304a94791b4e4a1c59b2fbb1d.

- 2026-10-09T15:10:54+00:00: Recorded command exit 101; command argv SHA-256
  e722ed1403701d5b7aa87509d78c9e1d3bcfaeb05459ab381d3f44bc7160a842.

- 2026-10-09T15:11:08+00:00: Two exit-101 records at 15:10 were the workspace capability_contract
  test rejecting the intentionally extended bash completion list (it still expected doctor setup
  capabilities provider-catalog). No product runtime failure: repair the assertion to require doctor
  setup capabilities project provider-catalog, then rerun the full workspace gate.

- 2026-10-09T15:11:28+00:00: Recorded command exit 101; command argv SHA-256
  e722ed1403701d5b7aa87509d78c9e1d3bcfaeb05459ab381d3f44bc7160a842.

- 2026-10-09T15:11:54+00:00: The subsequent full-workspace run exposed one additional exit-101:
  guide_inventory_matches_doctor_and_stale_claims_fail_closed expected the old doctor command list.
  Repaired docs/examples/guide-contract.json to include project init; rerunning the full gate now.
