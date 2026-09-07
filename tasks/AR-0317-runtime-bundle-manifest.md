---
{
  "branch": "feature/runtime-bundle-manifest",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-07T13:35:27+00:00",
  "depends_on": [
    "AR-0101",
    "AR-0102",
    "AR-0701"
  ],
  "id": "AR-0317",
  "next_action": "Define signed runtime-bundle manifests and an offline verifier for content, architecture, libc, license, and SBOM identity.",
  "observed_branch": "feature/runtime-bundle-manifest",
  "observed_dirty": 1,
  "observed_head": "b1669203308db5a75fee1e78a45c6fc8e71f17ce",
  "owner": "contracts-20260906",
  "plan": "../plans/AR-0317.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Define common signed runtime bundle manifests and offline verification.",
  "task_revision": 7,
  "title": "Define runtime bundle manifest and verifier",
  "updated_at": "2026-09-07T10:42:53+00:00",
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

- 2026-09-07T10:35:27+00:00: Claimed by contracts-20260906.

- 2026-09-07T10:35:50+00:00: Recorded command exit 0; command argv SHA-256
  65768c45e18cb2d475428c52888be464156e9a0c6569f8921105f7698ff2a908.

- 2026-09-07T10:42:29+00:00: Recorded command exit 2; command argv SHA-256
  48458d4adcbc2714c4ae60f17ec39d916357031118af6e75d9a5cd826c73f20e.
