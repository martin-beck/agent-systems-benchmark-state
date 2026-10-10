---
{
  "branch": "feature/ar-1763-generated-catalog-selection",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-10T11:32:02+00:00",
  "depends_on": [
    "AR-1761",
    "AR-1762",
    "AR-1769"
  ],
  "id": "AR-1763",
  "next_action": "Implement deterministic project catalog generation, list/show/select, provenance and compatibility/digest/secret-boundary tests in the isolated worktree; then obtain independent exact-head review.",
  "observed_branch": "feature/ar-1763-generated-catalog-selection",
  "observed_dirty": 7,
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
  "task_revision": 14,
  "title": "Generate and select ASB project catalogs",
  "updated_at": "2026-10-10T09:36:59+00:00",
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
