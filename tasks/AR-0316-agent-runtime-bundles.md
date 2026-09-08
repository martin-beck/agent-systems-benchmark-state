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
  "observed_dirty": 0,
  "observed_head": "26b7e5f66676302ea86da401c7fe9f103bdf555b",
  "owner": "contracts_20260906",
  "plan": "../plans/AR-0316.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Make supported agent installations reproducible, license-audited, SBOM-backed, and independently verifiable.",
  "task_revision": 6,
  "title": "Publish reproducible agent runtime bundles",
  "updated_at": "2026-09-08T10:36:42+00:00",
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
