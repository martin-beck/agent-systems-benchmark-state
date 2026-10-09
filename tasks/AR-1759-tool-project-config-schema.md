---
{
  "branch": "feature/ar-1759-tool-project-config-schema",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-09T17:35:19+00:00",
  "depends_on": [
    "AR-1745"
  ],
  "id": "AR-1759",
  "next_action": "Open the schema/config contract for implementation after AR-1745 is reconciled.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "codex-asb-ar1759-project-config-20261009",
  "plan": "../plans/AR-1759-tool-project-config-schema.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "contract-test",
    "evidence_digest": "",
    "evidence_ref": "",
    "spec_ref": "specs/AR-1759.json",
    "spec_revision": 1,
    "status": "pending"
  },
  "spec_ref": "specs/AR-1759.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Define one versioned ASB project/tool inventory and catalog-selection configuration contract.",
  "task_revision": 4,
  "title": "ASB project and external-tool configuration schema",
  "updated_at": "2026-10-09T14:35:32+00:00",
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

- 2026-10-09T14:35:14+00:00: AR-1745 is done and reconciled; opening schema/config contract
  implementation.

- 2026-10-09T14:35:19+00:00: Claimed by codex-asb-ar1759-project-config-20261009.

- 2026-10-09T14:35:32+00:00: Recorded command exit 0; command argv SHA-256
  acafe79cf9c102642feef818c5a891c5b1e8cadae67d4601ef8837ce06cbc4ae.
