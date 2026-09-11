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
  "observed_dirty": 15,
  "observed_head": "2ecb876b82a91a8103926b298c42ad49ce8dd143",
  "owner": "codex-root-ar1036-catalog-20260911",
  "plan": "../plans/AR-1036.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Expose the versioned ASB measurement catalog to standalone frontends without UI code.",
  "task_revision": 23,
  "title": "Publish the measurement catalog control contract",
  "updated_at": "2026-09-11T01:49:11+00:00",
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

- 2026-09-11T01:42:58+00:00: Recorded command exit 101; command argv SHA-256
  02168a3f9e679202c03514861d51c419643a82f2d5e15349b0ef923a64b0b489.

- 2026-09-11T01:43:23+00:00: Recorded command exit 101; command argv SHA-256
  ba030ce5d94b6bba6e9ad15dbcab5e6ff607b17af41c5ea4fea1652868a54a5f.

- 2026-09-11T01:45:03+00:00: Recorded command exit 0; command argv SHA-256
  02168a3f9e679202c03514861d51c419643a82f2d5e15349b0ef923a64b0b489.

- 2026-09-11T01:45:23+00:00: Recorded command exit 0; command argv SHA-256
  0cf2915f4a267b5bd71189368ab134f456a244810ec78e29f957d23b8d35f0cf.

- 2026-09-11T01:46:59+00:00: Recorded command exit 0; command argv SHA-256
  0cf2915f4a267b5bd71189368ab134f456a244810ec78e29f957d23b8d35f0cf.

- 2026-09-11T01:48:17+00:00: Recorded command exit 0; command argv SHA-256
  6a3dffbd227f4bab0c2c58cce7f86b7c72a1be32a3cfabb404020872de59bd3a.

- 2026-09-11T01:49:11+00:00: Recorded command exit 0; command argv SHA-256
  2b01e6df558910928f77cab50be4efae19a20fa4b1838c77a25688947433157f.
