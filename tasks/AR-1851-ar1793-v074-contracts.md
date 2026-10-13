---
{
  "branch": "codex/ar1851-ar1793-v074-contracts",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-13T14:45:46+00:00",
  "depends_on": [],
  "id": "AR-1851",
  "next_action": "Bind to the exact v0.7.4 candidate worktree at ASB commit 180c96b25d, then reproduce and repair only non-vendor AR-1793 compatibility fixtures.",
  "owner": "ar1851-ar1793-v074-luna",
  "plan": "../plans/AR-1851-ar1793-v074-contracts.md",
  "priority": "P1",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "mechanical",
    "evidence_digest": "",
    "evidence_ref": "",
    "spec_ref": "specs/AR-1851.json",
    "spec_revision": 1,
    "status": "pending"
  },
  "spec_ref": "specs/AR-1851.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Align AR-1793 compatibility fixtures with Coordinator v0.7.4.",
  "task_revision": 5,
  "title": "AR-1793 v0.7.4 compatibility contracts",
  "updated_at": "2026-10-13T13:16:16+00:00",
  "worktree_key": ""
}
---

Create a dependency-safe, non-vendor repair for the AR-1793 fixture and error
contract failures exposed by the exact Coordinator v0.7.4 adoption.

- 2026-10-13T13:13:51+00:00: Candidate binding 180c96b25d recorded; promote AR-1851 as the
  dependency-safe AR-1793 compatibility repair.

- 2026-10-13T13:15:46+00:00: Claimed by ar1851-ar1793-v074-luna.

- 2026-10-13T13:15:55+00:00: Recorded command exit 0; command argv SHA-256
  eacb532e7a13c28da36ab86a14cc56351a306bc50e9b7d7a1931cf9cf9b25d3f.

- 2026-10-13T13:16:16+00:00: Recorded command exit 1; command argv SHA-256
  a844b4305d8478de5c94b94a27c7b0e540a60894729682e891b92969bf76d0c5.
