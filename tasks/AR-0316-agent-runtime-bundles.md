---
{
  "branch": "feature/agent-runtime-bundles",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-08T13:35:28+00:00",
  "depends_on": [
    "AR-0301",
    "AR-0302",
    "AR-0303",
    "AR-0304",
    "AR-0305",
    "AR-0306",
    "AR-0307",
    "AR-0308",
    "AR-0309"
  ],
  "id": "AR-0316",
  "next_action": "Extend the fail-closed nine-agent catalog from top-level pins to complete per-component dependency nodes sourced from each retained lock/provenance record; do not mark any closure complete or redistribute until manifest, SBOM, license, and reproducibility evidence agree. Request serialized schema/release/platform fences only after crate-local closure tests are ready.",
  "observed_branch": "feature/agent-runtime-bundles",
  "observed_dirty": 0,
  "observed_head": "1249fd87d46d54556bca835fcc3e6570df15cc2c",
  "owner": "contracts_20260906",
  "plan": "../plans/AR-0316.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Make supported agent installations reproducible, license-audited, SBOM-backed, and independently verifiable.",
  "task_revision": 22,
  "title": "Publish reproducible agent runtime bundles",
  "updated_at": "2026-09-08T11:39:26+00:00",
  "worktree_key": "agent-systems-benchmark-agent-runtime-bundles"
}
---

## AR-0316

Make supported agent installations reproducible, license-audited, SBOM-backed,
and independently verifiable.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-08T10:35:21+00:00: Promote after verifying AR-0301 through AR-0309 are durably done.
  AR-0313 is deferred because its run-plan/asb-agents integration overlaps active AR-1003 and
  serialized Cargo/schema paths; AR-0316 begins only with disjoint runtime-manifest inventory,
  provenance, and verification fixtures, while shared release/platform/Cargo/schema integration
  remains deferred to a coordinator fence.

- 2026-09-08T10:35:28+00:00: Claimed by contracts_20260906.

- 2026-09-08T10:35:54+00:00: Recorded command exit 0; command argv SHA-256
  06beead18a298e3f0d6879a8d09cb13c5142d75dbbdb2239cd76e6afa586ecc8.

- 2026-09-08T10:36:42+00:00: Selected AR-0316 as the highest-priority dependency-ready compatible
  leaf after fresh snapshot. AR-0301 through AR-0309 are durably done. Deferred AR-0313 because
  run-plan/asb-agents integration overlaps active AR-1003; AR-0704 lacks its plan-required
  provider/account/quota/cost authorization; AR-0832 plan additionally requires blocked AR-0703;
  AR-0844 requires shared integration paths. Claimed as contracts_20260906 through
  2026-09-08T13:35:28Z. Created declared
  /srv/data/projects/agent-systems-benchmark-agent-runtime-bundles worktree on
  feature/agent-runtime-bundles at exact product main 26b7e5f66676302ea86da401c7fe9f103bdf555b.
  Initial audit confirms AR-0317 already supplies signed v1 manifest/offline verification; AR-0316
  must add complete per-agent graphs, provenance/license/SBOM agreement, and fail-closed
  acquisition/materialization without modifying shared fences yet.

- 2026-09-08T11:32:56+00:00: Recorded command exit 127; command argv SHA-256
  c0db99a2702ae9a4f09471850ba78de431d9dcb0cfbe382d43c5e46fccc9e47e.

- 2026-09-08T11:33:26+00:00: Recorded command exit 0; command argv SHA-256
  c0db99a2702ae9a4f09471850ba78de431d9dcb0cfbe382d43c5e46fccc9e47e.

- 2026-09-08T11:33:47+00:00: Recorded command exit 1; command argv SHA-256
  1881dd749231d145ef5e53964ebc86cc236a35626bd7b69ebca79faaca1f8f8a.

- 2026-09-08T11:34:09+00:00: Recorded command exit 0; command argv SHA-256
  4ce7a0bf7c07c131875d27d5e3e0d987b364320904f7a21041ac5c01eda961d8.

- 2026-09-08T11:34:33+00:00: Recorded command exit 0; command argv SHA-256
  c0555703195f3d873db6d8de79aec158c261211a486e5659ba6b218978a00e41.

- 2026-09-08T11:34:53+00:00: Recorded command exit 0; command argv SHA-256
  c9087b3f3701eff346a7fbf4de37cc291c39123ae681bbbcdc8610c33ba01890.

- 2026-09-08T11:35:50+00:00: Recorded command exit 0; command argv SHA-256
  7c9fac8015ba175734637a63c321ce2391e8a342b15538f479faf903f1ed2490.

- 2026-09-08T11:36:07+00:00: Recorded command exit 0; command argv SHA-256
  c0555703195f3d873db6d8de79aec158c261211a486e5659ba6b218978a00e41.

- 2026-09-08T11:36:51+00:00: Recorded command exit 0; command argv SHA-256
  0e0abd6009a29a2b9505620cb6012c3d7e07378c59c1618a5eed993c50164330.

- 2026-09-08T11:37:05+00:00: Recorded command exit 0; command argv SHA-256
  700521ddec16d8270ef08c0cb16f00891407a2c1fc3a0b9afed1d657432af5b2.

- 2026-09-08T11:37:45+00:00: Created clean signed+DCO checkpoint
  1249fd87d46d54556bca835fcc3e6570df15cc2c tree a311664f1a94e99977795a3a43ab8e47afc5f8bd on base
  26b7e5f. Exact three-path scope: new strict crates/asb-bundle/src/catalog.rs, nine-agent
  fixtures/agents/v1/catalog.json, and lib.rs export. Catalog requires the exact sorted
  released-agent roster, bounded canonical IDs/revisions/artifact hashes, explicit redistribution
  status, and complete-vs-incomplete closure evidence; require_complete rejects all current
  top-level-only inventories. Negatives cover omitted/reordered agents, uppercase digest, empty gap
  evidence, and falsely complete unverified closure. Focused tests 2/2, Clippy -D warnings,
  formatting, JSON parse, and diff-check pass from external target. Classified recorded fmt exit 1
  as formatting-only and corrected it; recorded script exit 127 was a stale apply_patch helper path
  and caused no product change. One initial partial patch effect preceded the wrapper after a
  malformed external patch target; scope was immediately inspected, all subsequent
  completion/fixes/tests/staging/commit used handoffctl, and the exact final tree is clean and
  reviewable. Corrected OpenDesk license evidence to MulanPSL-2.0 from durable AR-0302 provenance.

- 2026-09-08T11:39:03+00:00: Recorded command exit 0; command argv SHA-256
  f84751cb813d5060a10e4aed79d1ef32800e2e359fca8dc16daab90819436b1c.

- 2026-09-08T11:39:26+00:00: Recorded command exit 0; command argv SHA-256
  fa8cf073c93cfc06c2ada10bb4d1d0b2c0926e9105c89056c4ab5a79b14fa505.
