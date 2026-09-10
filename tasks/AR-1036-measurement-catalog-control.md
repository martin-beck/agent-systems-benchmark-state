---
{
  "branch": "feature/measurement-catalog-control",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1013", "AR-1023"],
  "id": "AR-1036",
  "next_action": "After AR-1013, publish the bounded measurement-catalog control operation and exact standalone parser fixtures.",
  "owner": "",
  "plan": "../plans/AR-1036.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Expose the versioned ASB measurement catalog to standalone frontends without UI code.",
  "task_revision": 2,
  "title": "Publish the measurement catalog control contract",
  "updated_at": "2026-09-10T21:04:37+00:00",
  "worktree_key": "agent-systems-benchmark-measurement-catalog-control"
}
---
Implement only the bounded ASB control method, types, schema, backend dispatch, capability bit and
cross-repository fixtures required to retrieve the AR-1013 catalog. All search, grouping, selection,
rendering and help behavior remains exclusively in `martin-beck/asb-tui` under AR-1014.

- 2026-09-10T21:40:00+00:00: Clarified that cross-repository parser validation is read-only pinned
  consumer conformance; parser or frontend fixture changes belong only to standalone asb-tui ARs.
