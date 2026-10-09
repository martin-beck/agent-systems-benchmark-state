---
{
  "branch": "feature/ar-1759-tool-project-config-schema",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-09T16:54:46+00:00",
  "depends_on": [
    "AR-1745"
  ],
  "id": "AR-1759",
  "next_action": "Wait for exact-main runs 37947479451, 37947479455, and 37947479450 to reach terminal success; then publish evidence and accept/release AR-1759.",
  "observed_branch": "main",
  "observed_dirty": 0,
  "observed_head": "27d7c931a6f3e0adbbe7f4ea9606717f369e9779",
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
  "task_revision": 37,
  "title": "ASB project and external-tool configuration schema",
  "updated_at": "2026-10-09T15:02:38+00:00",
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

- 2026-10-09T14:39:43+00:00: Recorded command exit 0; command argv SHA-256
  39cf5398131881d6bebfeb6940a170dba53287cbad205a984f34c80a6dbe58e7.

- 2026-10-09T14:40:06+00:00: Implementation complete at signed SSH+DCO commits f45082a and 36dab7a;
  PR #531 open at exact head 36dab7a. ProjectConfigV1, JSON Schema, documentation, positive/negative
  tests, focused cargo test/clippy pass. Independent review and exact-head CI remain before merge.

- 2026-10-09T14:41:20+00:00: Recorded command exit 0; command argv SHA-256
  534f8613e1c316db8f0f46dd989e44e14a8ca74304a94791b4e4a1c59b2fbb1d.

- 2026-10-09T14:42:01+00:00: Recorded command exit 0; command argv SHA-256
  c57fb8825b91d1f3c73dbfd14a226ab92073ded1e78e284cd06a8de29cbc74da.

- 2026-10-09T14:51:56+00:00: Recorded command exit 1; command argv SHA-256
  5080a893c48ddb34f796b355566b6f31a5839028e6273d6d31a28a5efd6f6d0b.

- 2026-10-09T14:52:12+00:00: Recorded command exit 0; command argv SHA-256
  d3ebb705a0624e2006dc8057a8b42c20783432ea8b3731c7f9f1710be8d4ab77.

- 2026-10-09T14:52:19+00:00: Recorded command exit 0; command argv SHA-256
  6de916dc52d4ad6a33a1b81da58e5b230c67a2688ad7c4446173ef6351c6358c.

- 2026-10-09T14:52:28+00:00: Recorded command exit 0; command argv SHA-256
  8d50fb73a61a6e271c0ea3dd3da2f7ad4dae61e9b91127e9c50771cefa64a801.

- 2026-10-09T14:52:47+00:00: Recorded command exit 0; command argv SHA-256
  5080a893c48ddb34f796b355566b6f31a5839028e6273d6d31a28a5efd6f6d0b.

- 2026-10-09T14:54:46+00:00: Heartbeat by codex-asb-ar1759-project-config-20261009.

- 2026-10-09T14:54:55+00:00: PR #531 merged at signed merge commit
  64843f1967370a0fe4df675b4a59f42f58342a14; origin/main tree
  3376d5b8f1f171576f2a72cc5a01bee8a192e460 exactly contains reviewed head 36dab7a. All PR checks
  were terminal green. Post-merge exact-main workflows are now running; acceptance waits for their
  terminal success.

- 2026-10-09T14:56:49+00:00: Post-merge exact-main monitoring: Formal assurance (run 37947479338) is
  terminal success. Emulated aarch64 (37947479451), Rust verification (37947479455), and Repository
  quality (37947479450) remain in progress; acceptance still waits for all three.

- 2026-10-09T15:02:38+00:00: Recorded command exit 0; command argv SHA-256
  42339310fe201bea44a4eaa9f4b4471d4657643cb4b9c51ac8c3c4ddb732e25d.
