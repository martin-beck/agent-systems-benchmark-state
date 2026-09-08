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
  "next_action": "Inventory the nine released agent runtime graphs against the existing asb-bundle v1 verifier, then add only disjoint agent-runtime manifest/provenance fixtures; defer Cargo/schema/release/platform and adapter registration to an explicit serialized fence.",
  "observed_branch": "feature/agent-runtime-bundles",
  "observed_dirty": 3,
  "observed_head": "26b7e5f66676302ea86da401c7fe9f103bdf555b",
  "owner": "contracts_20260906",
  "plan": "../plans/AR-0316.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Make supported agent installations reproducible, license-audited, SBOM-backed, and independently verifiable.",
  "task_revision": 17,
  "title": "Publish reproducible agent runtime bundles",
  "updated_at": "2026-09-08T11:36:51+00:00",
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
