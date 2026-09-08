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
  "next_action": "Define content-addressed offline runtime manifests for every supported agent and its complete transitive environment.",
  "owner": "contracts_20260906",
  "plan": "../plans/AR-0316.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Make supported agent installations reproducible, license-audited, SBOM-backed, and independently verifiable.",
  "task_revision": 3,
  "title": "Publish reproducible agent runtime bundles",
  "updated_at": "2026-09-08T10:35:28+00:00",
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
