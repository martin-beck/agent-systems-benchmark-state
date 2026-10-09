---
{
  "branch": "feature/ar-1759-tool-project-config-schema",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1745"],
  "id": "AR-1759",
  "next_action": "Open the schema/config contract for implementation after AR-1745 is reconciled.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1759-tool-project-config-schema.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {"evidence_class": "contract-test", "evidence_digest": "", "evidence_ref": "", "spec_ref": "specs/AR-1759.json", "spec_revision": 1, "status": "pending"},
  "spec_ref": "specs/AR-1759.json",
  "spec_revision": 1,
  "status": "planned",
  "summary": "Define one versioned ASB project/tool inventory and catalog-selection configuration contract.",
  "task_revision": 1,
  "title": "ASB project and external-tool configuration schema",
  "updated_at": "2026-10-09T00:00:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1759-tool-project-config-schema"
}
---

Define the canonical machine-readable project configuration used by all later
commands. Model agent, harness, benchmark, workload, and support-tool records
with source/version/platform/path/digest/capabilities/status, project roots,
active selections, and generated catalog references (id, schema, source/ref,
digest, generation time). Preserve credential references or digests only; do
not persist API keys or tokens. Integrate with existing ASB config/catalog
types rather than creating a competing authority, with migration and bounded
unknown-field/path validation.
