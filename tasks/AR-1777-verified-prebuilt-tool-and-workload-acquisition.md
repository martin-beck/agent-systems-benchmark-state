---
{
  "branch": "feature/ar-1777-verified-prebuilt-tool-and-workload-acquisition",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-11T12:42:33+00:00",
  "depends_on": [
    "AR-1776"
  ],
  "id": "AR-1777",
  "next_action": "Await required checks for PR #574 at 0a389a2f (coverage repaired to 90.28%); then obtain independent exact-head review, merge only through signed local merge-integrity, and verify exact-main workflows.",
  "observed_branch": "feature/ar-1777-verified-prebuilt-tool-and-workload-acquisition-repair-v2",
  "observed_dirty": 0,
  "observed_head": "0a389a2f8aa3c0801e1b82d70d0d0021a9abd1b1",
  "owner": "codex-ar1777-verified-prebuilt-tool-and-workload-acquisition-luna56",
  "plan": "../plans/AR-1777-verified-prebuilt-tool-and-workload-acquisition.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "contract-test",
    "evidence_digest": "",
    "evidence_ref": "",
    "spec_ref": "specs/AR-1777.json",
    "spec_revision": 1,
    "status": "pending"
  },
  "spec_ref": "specs/AR-1777.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Acquire, verify, and atomically install official compatible prebuilt executable tools into a project-local root.",
  "task_revision": 71,
  "title": "Verified prebuilt tool acquisition",
  "updated_at": "2026-10-11T10:51:25+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1777-verified-prebuilt-tool-and-workload-acquisition"
}
---

Implement catalog-driven acquisition for a compatible existing system binary and
for official prebuilt executable tools. The resolver selects only an entry
matching the current OS, architecture, libc/ABI and catalog identity; downloads
only from the catalog's primary source; verifies TLS transfer policy, immutable
digest, signature/provenance when declared, archive boundaries, executable
entrypoint, and license metadata before atomically publishing under the
selected project. It records the exact catalog revision, source identity,
artifact digest, verifier outcome, platform, and usable entrypoint.

No partial output becomes active. Failed transfer, checksum/signature mismatch,
wrong platform, archive traversal, unsafe executable, revoked artifact, and
offline/unavailable source must be separately diagnosed and leave the previous
usable installation intact. Do not execute downloaded installer scripts, require
root, persist credentials, or use a package manager. Use the shared human status
reporting contract when available while keeping machine-mode output safe.

- 2026-10-11T08:19:13+00:00: AR-1776 dependency is accepted on protected main; open AR-1777 for
  implementation.

- 2026-10-11T08:19:17+00:00: Claimed by
  codex-ar1777-verified-prebuilt-tool-and-workload-acquisition-luna56.

- 2026-10-11T08:20:50+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-11T08:21:48+00:00: Recorded command exit 101; command argv SHA-256
  09de3547b72d103e84c99b9d48ae326ffdc04a44851acde9c6a3f2bacafe2f00.

- 2026-10-11T08:22:09+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-11T08:22:40+00:00: Recorded command exit 0; command argv SHA-256
  09de3547b72d103e84c99b9d48ae326ffdc04a44851acde9c6a3f2bacafe2f00.

- 2026-10-11T08:24:01+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-11T08:24:23+00:00: Recorded command exit 101; command argv SHA-256
  bf5fcb6fc92c4de38ff2147178dd3a153eae3976f2b397ae65308300d2d8bafb.

- 2026-10-11T08:24:52+00:00: Recorded command exit 0; command argv SHA-256
  bf5fcb6fc92c4de38ff2147178dd3a153eae3976f2b397ae65308300d2d8bafb.

- 2026-10-11T08:25:14+00:00: Recorded command exit 0; command argv SHA-256
  5049a9f7f59f1c6a2a9a01db4a5e2d1744178900d10126367f823600583fe2ff.

- 2026-10-11T08:25:33+00:00: Recorded command exit 0; command argv SHA-256
  38f4dbdf79a077b55761808a83ccaa00eb1ab4128b256d42e633598470885d2f.

- 2026-10-11T08:25:58+00:00: Recorded command exit 0; command argv SHA-256
  8f9b6c1dfb961b5cdd4b75169caa06c61f3be5335277e2672faf1eae2004e617.

- 2026-10-11T08:26:44+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-11T08:27:06+00:00: Recorded command exit 0; command argv SHA-256
  e274074a17e0682b5edf79b5caca577a41520ed9ca8daf9342f0433b678582a1.

- 2026-10-11T08:27:20+00:00: Recorded command exit 0; command argv SHA-256
  354d1ffbaab3d1c7bc32de06e4a142bdace02fc6138f7607d3a169eabfddf873.

- 2026-10-11T08:27:55+00:00: Recorded command exit 101; command argv SHA-256
  bbfa4cb9328e16865a97a7cfe74f9cc4cdfc93b196b5430ed320e8cbe21e8c7c.

- 2026-10-11T08:28:10+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-11T08:28:35+00:00: Recorded command exit 101; command argv SHA-256
  bbfa4cb9328e16865a97a7cfe74f9cc4cdfc93b196b5430ed320e8cbe21e8c7c.

- 2026-10-11T08:29:25+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-11T08:30:30+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-11T08:31:00+00:00: Recorded command exit 101; command argv SHA-256
  bbfa4cb9328e16865a97a7cfe74f9cc4cdfc93b196b5430ed320e8cbe21e8c7c.

- 2026-10-11T08:31:40+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-11T08:34:17+00:00: Recorded command exit 0; command argv SHA-256
  e274074a17e0682b5edf79b5caca577a41520ed9ca8daf9342f0433b678582a1.

- 2026-10-11T08:34:43+00:00: Recorded command exit 0; command argv SHA-256
  03b416bbb8e22e4e2bcae4be3fc0fa086b50a50a3a030b7d5785e7a97a708a94.

- 2026-10-11T08:35:01+00:00: Recorded command exit 0; command argv SHA-256
  b7c438686581cf292b6cd41497ceabb3af42dfed57e04dfd6cc89efed8e2d15b.

- 2026-10-11T08:35:38+00:00: Recorded command exit 1; command argv SHA-256
  a63677a4dcf9ed9da39adf1097cbb429418eb2461709ba7d566b53ba93404179.

- 2026-10-11T08:36:11+00:00: Recorded command exit 101; command argv SHA-256
  2ddd222d5ab3dbbc5824e8367ff0d1151a6168041a569b52fb97c11e3c8515c1.

- 2026-10-11T08:38:57+00:00: Recorded command exit 0; command argv SHA-256
  aeb0bcd3a22b8d01f21ce0d1991cfe7400ccbec51a04a91e01fb4579b8bf0bef.

- 2026-10-11T08:39:46+00:00: Recorded command exit 0; command argv SHA-256
  e326d31c2924fd732e602b84db153137c57a1fbe605652a3c5d18d60e3ce31fa.

- 2026-10-11T08:40:09+00:00: Recorded command exit 0; command argv SHA-256
  f505d2cddb097144c5e5d56b966326acc5125db1b1af4f1d89f4c8f9b0df3127.

- 2026-10-11T08:46:07+00:00: Recorded command exit 0; command argv SHA-256
  38f4dbdf79a077b55761808a83ccaa00eb1ab4128b256d42e633598470885d2f.

- 2026-10-11T08:46:39+00:00: Recorded command exit 0; command argv SHA-256
  067cac0958a3194d0d12796f51d8609886d2307167ed09f9d8730fb88919aaf9.

- 2026-10-11T08:46:57+00:00: Recorded command exit 0; command argv SHA-256
  17ca6592995956b5a5950ab7f58410ce3653626e0c10126aec0cd3e2b546200c.

- 2026-10-11T08:49:19+00:00: Recorded command exit 0; command argv SHA-256
  165d69016939033b705f5f43c8b018bdc2a25f7fcf89ae0dd7386c97c2a1a53d.

- 2026-10-11T08:49:33+00:00: Recorded command exit 0; command argv SHA-256
  1113eca75b7e10af035a2cf4f89f2007c2e6e2296ec8e700df34e59ef2c5e070.

- 2026-10-11T08:49:47+00:00: Recorded command exit 0; command argv SHA-256
  17ca6592995956b5a5950ab7f58410ce3653626e0c10126aec0cd3e2b546200c.

- 2026-10-11T10:18:03+00:00: Heartbeat by
  codex-ar1777-verified-prebuilt-tool-and-workload-acquisition-luna56.

- 2026-10-11T10:21:23+00:00: Signed/DCO repair 37fcf269 adds 316 diagnostic identities, refreshes
  provenance, and local focused/full asb-cli gates pass. Hosted publication is pending because PR
  #571 conflicts with main advanced by AR-1781 merge.

- 2026-10-11T10:21:33+00:00: Transferring active repair ownership to ar1781-luna56 for conflict
  reconciliation; preserve signed repair 37fcf269 and all evidence.

- 2026-10-11T10:21:40+00:00: Claimed by
  codex-ar1777-verified-prebuilt-tool-and-workload-acquisition-luna56.

- 2026-10-11T10:22:53+00:00: Clean-topic/superseding workflow created PR #574 at signed/DCO head
  fc4e8c9d after PR #571 conflict. Local focused/full asb-cli gates pass; hosted checks pending. No
  force-push or merge performed.

- 2026-10-11T10:30:46+00:00: Exact-head PR #574 fc4e8c9 is based on af75cd06 and all checks except
  Policy coverage and Rust are successful; Policy reports 89.99% workspace lines, no merge yet.

- 2026-10-11T10:35:31+00:00: Coverage repair pushed as signed/DCO 0a389a2f: bounded
  oversized-artifact, digest-mismatch, and local typed-error tests; focused 10/10 and full asb-cli
  357+ integrations/docs pass. Hosted checks restarting.

- 2026-10-11T10:40:17+00:00: Heartbeat by
  codex-ar1777-verified-prebuilt-tool-and-workload-acquisition-luna56.

- 2026-10-11T10:42:33+00:00: Heartbeat by
  codex-ar1777-verified-prebuilt-tool-and-workload-acquisition-luna56.
