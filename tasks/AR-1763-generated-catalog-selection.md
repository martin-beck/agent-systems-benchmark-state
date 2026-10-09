---
{
  "branch": "feature/ar-1763-generated-catalog-selection",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1761", "AR-1762"],
  "id": "AR-1763",
  "next_action": "Implement catalog generation and selection on top of the installer/discovery inventory.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1763-generated-catalog-selection.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {"evidence_class": "contract-test", "evidence_digest": "", "evidence_ref": "", "spec_ref": "specs/AR-1763.json", "spec_revision": 1, "status": "pending"},
  "spec_ref": "specs/AR-1763.json",
  "spec_revision": 1,
  "status": "planned",
  "summary": "Generate selectable agent/harness/benchmark/workload catalogs and persist their provenance.",
  "task_revision": 1,
  "title": "Generate and select ASB project catalogs",
  "updated_at": "2026-10-09T00:00:00+00:00",
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
