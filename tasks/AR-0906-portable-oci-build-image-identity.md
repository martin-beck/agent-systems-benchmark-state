---
{
  "branch": "fix/formal-oci-image-identity",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-0003",
    "AR-0878",
    "AR-0901",
    "AR-0902"
  ],
  "id": "AR-0906",
  "next_action": "Implement and test portable digest-plus-platform OCI identity verification for the deterministic TLA source build.",
  "owner": "",
  "plan": "../plans/AR-0906.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "planned",
  "summary": "Make deterministic formal source builds verify OCI image identity portably across Docker engines.",
  "task_revision": 1,
  "title": "Verify formal OCI build identity portably",
  "updated_at": "2026-09-09T14:33:11+00:00",
  "worktree_key": "agent-systems-benchmark-formal-oci-image-identity"
}
---
## AR-0906

Repair the Docker image identity boundary exposed by hosted formal CI without weakening the exact
AR-0878 source-build provenance. Verify the immutable repository digest and platform independently
instead of assuming an engine's local configuration ID equals the registry manifest digest.

