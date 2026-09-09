---
{
  "branch": "fix/formal-oci-image-identity",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-09T17:36:00+00:00",
  "depends_on": [
    "AR-0003",
    "AR-0878",
    "AR-0901",
    "AR-0902"
  ],
  "id": "AR-0906",
  "next_action": "Implement and test portable digest-plus-platform OCI identity verification for the deterministic TLA source build.",
  "observed_branch": "fix/formal-oci-image-identity",
  "observed_dirty": 0,
  "observed_head": "b6d04a8305ce6d49cc327e4e6d2d6fa42a88050b",
  "owner": "quality_20260906",
  "plan": "../plans/AR-0906.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Make deterministic formal source builds verify OCI image identity portably across Docker engines.",
  "task_revision": 5,
  "title": "Verify formal OCI build identity portably",
  "updated_at": "2026-09-09T14:36:33+00:00",
  "worktree_key": "agent-systems-benchmark-formal-oci-image-identity"
}
---
## AR-0906

Repair the Docker image identity boundary exposed by hosted formal CI without weakening the exact
AR-0878 source-build provenance. Verify the immutable repository digest and platform independently
instead of assuming an engine's local configuration ID equals the registry manifest digest.

- 2026-09-09T14:35:26+00:00: Dependencies AR-0003, AR-0878, AR-0901 and AR-0902 are done; the
  six-path OCI verifier fence is disjoint from active AR-0877 and AR-0704 work.

- 2026-09-09T14:36:00+00:00: Claimed by quality_20260906.

- 2026-09-09T14:36:27+00:00: Recorded command exit 0; command argv SHA-256
  cdcd326ab164f572ec8097b3acfae0b1487ac6fcd2490f76eaff129bd3f80646.
