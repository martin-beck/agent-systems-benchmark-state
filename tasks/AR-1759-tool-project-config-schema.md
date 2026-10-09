---
{
  "branch": "feature/ar-1759-tool-project-config-schema",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-09T17:37:33+00:00",
  "depends_on": [
    "AR-1745"
  ],
  "id": "AR-1759",
  "next_action": "Open the schema/config contract for implementation after AR-1745 is reconciled.",
  "observed_branch": "feature/ar-1759-tool-project-config-schema",
  "observed_dirty": 0,
  "observed_head": "36dab7a7addb33afad2ba1874a2b884e81635a6c",
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
  "task_revision": 22,
  "title": "ASB project and external-tool configuration schema",
  "updated_at": "2026-10-09T14:39:36+00:00",
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

- 2026-10-09T14:36:53+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-09T14:37:08+00:00: Recorded command exit 0; command argv SHA-256
  31a05f46a65b4172cfcc5ef4e1ed2b4ddd54c042ac56eff6dc51f4205a4051b1.

- 2026-10-09T14:37:21+00:00: Recorded command exit 0; command argv SHA-256
  81d627797efc6b08acda359548826bb5f1563136a4a8aed103c98d28146a9563.

- 2026-10-09T14:37:33+00:00: Heartbeat by codex-asb-ar1759-project-config-20261009.

- 2026-10-09T14:37:39+00:00: Recorded command exit 0; command argv SHA-256
  283344263d625f4c14a16d461b38d09f6a9da33cd44c52da7e69e01121db979f.

- 2026-10-09T14:37:51+00:00: Recorded command exit 0; command argv SHA-256
  ea018ecf558c6ed440c6178fea3e9a5858e6e0ff877df4ed39303522e4d54012.

- 2026-10-09T14:38:07+00:00: Recorded command exit 0; command argv SHA-256
  cf0b7ede6484a32c45328a1e7dd3fed9564d664a707240c7dbe1ab37bbfc4a0e.

- 2026-10-09T14:38:20+00:00: Recorded command exit 0; command argv SHA-256
  a94bb85538ea9c3be972ee5aa7b8d9f6142aab719fe5f739ca47be61c8fad230.

- 2026-10-09T14:38:50+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-09T14:39:02+00:00: Recorded command exit 0; command argv SHA-256
  31a05f46a65b4172cfcc5ef4e1ed2b4ddd54c042ac56eff6dc51f4205a4051b1.

- 2026-10-09T14:39:13+00:00: Recorded command exit 0; command argv SHA-256
  81d627797efc6b08acda359548826bb5f1563136a4a8aed103c98d28146a9563.

- 2026-10-09T14:39:29+00:00: Recorded command exit 0; command argv SHA-256
  6311d2e1eb4f71d3efc61b1359db284d4cecf10f20dca57c5cc29600f11c7e05.
