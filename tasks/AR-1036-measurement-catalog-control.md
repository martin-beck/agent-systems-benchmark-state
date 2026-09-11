---
{
  "branch": "feature/measurement-catalog-control",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-11T03:39:48+00:00",
  "depends_on": [
    "AR-1013",
    "AR-1023"
  ],
  "id": "AR-1036",
  "next_action": "After AR-1013, publish the bounded measurement-catalog control operation and exact standalone parser fixtures.",
  "observed_branch": "feature/measurement-catalog-control",
  "observed_dirty": 0,
  "observed_head": "2ecb876b82a91a8103926b298c42ad49ce8dd143",
  "owner": "codex-root-ar1036-catalog-20260911",
  "plan": "../plans/AR-1036.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Expose the versioned ASB measurement catalog to standalone frontends without UI code.",
  "task_revision": 6,
  "title": "Publish the measurement catalog control contract",
  "updated_at": "2026-09-11T01:40:21+00:00",
  "worktree_key": "agent-systems-benchmark-measurement-catalog-control"
}
---
Implement only the bounded ASB control method, types, schema, backend dispatch, capability bit and
cross-repository fixtures required to retrieve the AR-1013 catalog. All search, grouping, selection,
rendering and help behavior remains exclusively in `martin-beck/asb-tui` under AR-1014.

- 2026-09-10T21:40:00+00:00: Clarified that cross-repository parser validation is read-only pinned
  consumer conformance; parser or frontend fixture changes belong only to standalone asb-tui ARs.

- 2026-09-11T01:39:45+00:00: Dependencies AR-1013 and AR-1023 are done; root approves the
  protocol-only plan and repository boundary.

- 2026-09-11T01:39:48+00:00: Claimed by codex-root-ar1036-catalog-20260911.

- 2026-09-11T01:40:15+00:00: Recorded command exit 0; command argv SHA-256
  ea153b531f1106f5d94913543b5962bf799305c4e35ed4d05dd3cd19dab1610a.
