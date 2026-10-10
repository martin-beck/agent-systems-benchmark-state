---
{
  "branch": "feature/ar-1763-generated-catalog-selection",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-10T11:49:29+00:00",
  "depends_on": [
    "AR-1761",
    "AR-1762",
    "AR-1769"
  ],
  "id": "AR-1763",
  "next_action": "Implement deterministic project catalog generation, list/show/select, provenance and compatibility/digest/secret-boundary tests in the isolated worktree; then obtain independent exact-head review.",
  "observed_branch": "feature/ar-1763-generated-catalog-selection",
  "observed_dirty": 13,
  "observed_head": "772bc46537b0574008635ebfc27d6b147c12c805",
  "owner": "codex-asb-ar1763-catalog-terra",
  "plan": "../plans/AR-1763-generated-catalog-selection.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "contract-test",
    "evidence_digest": "",
    "evidence_ref": "",
    "spec_ref": "specs/AR-1763.json",
    "spec_revision": 1,
    "status": "pending"
  },
  "spec_ref": "specs/AR-1763.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Generate selectable agent/harness/benchmark/workload catalogs and persist their provenance.",
  "task_revision": 47,
  "title": "Generate and select ASB project catalogs",
  "updated_at": "2026-10-10T09:50:58+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1763-generated-catalog-selection"
}
---

Generate catalogs from the validated installer/discovery inventory and existing
ASB catalog sources. Store catalog artifacts under the project catalogs area
and record selectable metadata in config: stable ID, kind, schema revision,
source/ref, digest, generated time, compatibility, and active selection.
Reject incompatible or digest-mismatched selections with actionable output;
support human and `--json` listing/selection. Do not turn catalogs into a
secret store or require production signatures in development mode.

- 2026-10-09T17:21:34+00:00: Added AR-1769 as a dependency so new catalog errors and warnings
  cannot bypass the fine-grained human diagnostic catalog and required completeness gate.

- 2026-10-10T09:29:02+00:00: AR-1769 is accepted/done with merged protected-main and post-merge
  evidence; promote generated catalog implementation.

- 2026-10-10T09:29:59+00:00: Claimed by codex-asb-ar1763-catalog-terra.

- 2026-10-10T09:30:10+00:00: Recorded command exit 0; command argv SHA-256
  5345cd4b5f66285dc80cddfe59c0a95475263f9ff88d25d2639fce3c300aa4b9.

- 2026-10-10T09:30:27+00:00: Recorded command exit 0; command argv SHA-256
  29599af8132dec402789720e6015a4d85ea47fd36537254dde889df99cacf1a3.

- 2026-10-10T09:31:35+00:00: AR-1769 is accepted/done; claimed AR-1763 and created isolated worktree
  at protected main 772bc465.

- 2026-10-10T09:32:02+00:00: Heartbeat by codex-asb-ar1763-catalog-terra.

- 2026-10-10T09:36:19+00:00: Recorded command exit 0; command argv SHA-256
  b6095aecae37155753bbaceb030ec6735f50e0adecb30265cb0965e243f8fbe2.

- 2026-10-10T09:36:55+00:00: Recorded command exit 101; command argv SHA-256
  aefe05b0a469704e2df3e1a9071271143e9fa833be4a2d36b2ad03eb2272ed94.

- 2026-10-10T09:37:15+00:00: Recorded command exit 0; command argv SHA-256
  b6095aecae37155753bbaceb030ec6735f50e0adecb30265cb0965e243f8fbe2.

- 2026-10-10T09:37:28+00:00: Recorded command exit 0; command argv SHA-256
  d2162f50a59617d91b5abf539c955d5552420a5530d1b1b9423cab9d34bfdbcf.

- 2026-10-10T09:37:59+00:00: Recorded command exit 0; command argv SHA-256
  522b5de9996858e9958d5109c4ad41ab5d35ec632bfe0d2181c5560c3e8de350.

- 2026-10-10T09:38:52+00:00: Recorded command exit 0; command argv SHA-256
  b6095aecae37155753bbaceb030ec6735f50e0adecb30265cb0965e243f8fbe2.

- 2026-10-10T09:39:05+00:00: Recorded command exit 101; command argv SHA-256
  ebdcf8c34e07eed25ab40854f341e0e06f99c5b0121a097c57b0d859b303f6e5.

- 2026-10-10T09:40:16+00:00: Recorded command exit 0; command argv SHA-256
  b6095aecae37155753bbaceb030ec6735f50e0adecb30265cb0965e243f8fbe2.

- 2026-10-10T09:40:38+00:00: Recorded command exit 0; command argv SHA-256
  ebdcf8c34e07eed25ab40854f341e0e06f99c5b0121a097c57b0d859b303f6e5.

- 2026-10-10T09:41:57+00:00: Recorded command exit 0; command argv SHA-256
  b6095aecae37155753bbaceb030ec6735f50e0adecb30265cb0965e243f8fbe2.

- 2026-10-10T09:42:20+00:00: Recorded command exit 0; command argv SHA-256
  522b5de9996858e9958d5109c4ad41ab5d35ec632bfe0d2181c5560c3e8de350.

- 2026-10-10T09:42:30+00:00: Recorded command exit 101; command argv SHA-256
  ebdcf8c34e07eed25ab40854f341e0e06f99c5b0121a097c57b0d859b303f6e5.

- 2026-10-10T09:42:54+00:00: Recorded command exit 0; command argv SHA-256
  b6095aecae37155753bbaceb030ec6735f50e0adecb30265cb0965e243f8fbe2.

- 2026-10-10T09:43:37+00:00: Recorded command exit 101; command argv SHA-256
  ebdcf8c34e07eed25ab40854f341e0e06f99c5b0121a097c57b0d859b303f6e5.

- 2026-10-10T09:44:00+00:00: Recorded command exit 101; command argv SHA-256
  ebdcf8c34e07eed25ab40854f341e0e06f99c5b0121a097c57b0d859b303f6e5.

- 2026-10-10T09:44:29+00:00: Recorded command exit 101; command argv SHA-256
  ebdcf8c34e07eed25ab40854f341e0e06f99c5b0121a097c57b0d859b303f6e5.

- 2026-10-10T09:44:46+00:00: Recorded command exit 0; command argv SHA-256
  ebdcf8c34e07eed25ab40854f341e0e06f99c5b0121a097c57b0d859b303f6e5.

- 2026-10-10T09:45:21+00:00: Recorded command exit 0; command argv SHA-256
  6ca4edc69ef2e19b27e480162675146ebb82035dbfd8f95eb8189277c15e9917.

- 2026-10-10T09:45:36+00:00: Recorded command exit 0; command argv SHA-256
  d2a2d80aab269aeced03dbe4fe466b73b0b35781a44f2c43c7a70a8f2322df1d.

- 2026-10-10T09:45:40+00:00: Recorded command exit 0; command argv SHA-256
  69154eff9546e6e41cfb8c7f7a5ff2623ad6c7bbb37c1cc5f86042d97f23adde.

- 2026-10-10T09:45:42+00:00: Recorded command exit 0; command argv SHA-256
  edfd683b2d445c10bc2cd0a2956d713048560629a9d3b1baf5ae4aa3031cbbc2.

- 2026-10-10T09:46:11+00:00: Recorded command exit 101; command argv SHA-256
  00476688e6634e09ba536da89c760361173244004a602428217517c8f3b663a7.

- 2026-10-10T09:46:37+00:00: Recorded command exit 0; command argv SHA-256
  6ca4edc69ef2e19b27e480162675146ebb82035dbfd8f95eb8189277c15e9917.

- 2026-10-10T09:46:51+00:00: Recorded command exit 0; command argv SHA-256
  00476688e6634e09ba536da89c760361173244004a602428217517c8f3b663a7.

- 2026-10-10T09:47:28+00:00: Recorded command exit 101; command argv SHA-256
  ac97cc4f9d55709f94faef42e011309fa9bd5faa99f2d61f108833581624e757.

- 2026-10-10T09:48:17+00:00: Heartbeat by codex-asb-ar1763-catalog-terra.

- 2026-10-10T09:48:34+00:00: Recorded command exit 101; command argv SHA-256
  ac97cc4f9d55709f94faef42e011309fa9bd5faa99f2d61f108833581624e757.

- 2026-10-10T09:49:29+00:00: Heartbeat by codex-asb-ar1763-catalog-terra.

- 2026-10-10T09:49:35+00:00: Recorded command exit 0; command argv SHA-256
  f4c59ff5e5fd3eee192c530d7cfa18d57cc7a04750098211f770a9b269a0c498.

- 2026-10-10T09:50:04+00:00: Recorded command exit 101; command argv SHA-256
  ac97cc4f9d55709f94faef42e011309fa9bd5faa99f2d61f108833581624e757.

- 2026-10-10T09:50:58+00:00: Recorded command exit 1; command argv SHA-256
  d8eab8e3bbe174c036af2649a5f54ae51a26b051121bc2de96ada795a22eaa4f.
