---
{
  "branch": "feature/runtime-bundle-manifest",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-0101",
    "AR-0102",
    "AR-0701"
  ],
  "id": "AR-0317",
  "next_action": "Define signed runtime-bundle manifests and an offline verifier for content, architecture, libc, license, and SBOM identity.",
  "owner": "",
  "plan": "../plans/AR-0317.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "open",
  "summary": "Define common signed runtime bundle manifests and offline verification.",
  "task_revision": 2,
  "title": "Define runtime bundle manifest and verifier",
  "updated_at": "2026-09-07T10:35:24+00:00",
  "worktree_key": "agent-systems-benchmark-runtime-bundle-manifest"
}
---
## AR-0317

Define the common signed, content-addressed runtime-bundle manifest and offline verifier used by
per-agent bundle leaves. Cover complete transitive contents, architecture/libc, SPDX/CycloneDX
parity, license evidence, tamper detection, and offline operation.

- 2026-09-07T10:35:24+00:00: Dependencies AR-0101, AR-0102, and AR-0701 are done; promote the common
  signed runtime-bundle manifest and offline verifier with shared Cargo/schema/release integration
  serialized by the coordinator.
