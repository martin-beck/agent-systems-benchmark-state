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
  "next_action": "Complete fake-Docker effect-order negatives, source-build regression and full formal/privacy gates; then create signed candidate for review.",
  "observed_branch": "fix/formal-oci-image-identity",
  "observed_dirty": 6,
  "observed_head": "b6d04a8305ce6d49cc327e4e6d2d6fa42a88050b",
  "owner": "quality_20260906",
  "plan": "../plans/AR-0906.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Make deterministic formal source builds verify OCI image identity portably across Docker engines.",
  "task_revision": 10,
  "title": "Verify formal OCI build identity portably",
  "updated_at": "2026-09-09T14:47:54+00:00",
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

- 2026-09-09T14:41:12+00:00: Recorded command exit 2; command argv SHA-256
  9bdfb50edf62a5f583f5dfd9b9303eeb8aec5fd1bd4898891922e71db68dbb56.

- 2026-09-09T14:46:45+00:00: Recorded command exit 0; command argv SHA-256
  fd8cc47177c54ff0956e5de741ed1304bc7769bf6b41750ec8cc10f168717371.

- 2026-09-09T14:47:28+00:00: Recorded command exit 0; command argv SHA-256
  79ee00f5fb02a02c5f835f3fcb6d14de21cd6dc98153635aa06a22527555d128.

- 2026-09-09T14:47:54+00:00: Initial AR-0906 verifier checkpoint on exact product base b6d04a8.
  Dirty scope is exactly six owned paths: build.sh, new bounded verifier, positive/mutation
  fixtures, focused Rust test and public design note. Verifier distinguishes OCI config ID from
  repository digest; it requires a closed <=16384-byte JSON projection, exactly one pinned
  name-at-digest, linux/amd64, and redacts all failures. Focused test passes 3/3: two positive
  config-ID representations and all 20 unique declared mutations fail closed, plus static effect
  ordering. Real local Docker projection for the pinned digest passes. No AR-0877 PR path or AR-0704
  path changed.
