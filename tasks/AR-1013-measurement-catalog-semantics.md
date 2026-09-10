---
{
  "branch": "feature/measurement-catalog-semantics",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-11T00:44:21+00:00",
  "depends_on": [
    "AR-0101",
    "AR-1001"
  ],
  "id": "AR-1013",
  "next_action": "Define and review the versioned measurement catalog and semantic grouping contract before implementation.",
  "observed_branch": "feature/measurement-catalog-semantics",
  "observed_dirty": 2,
  "observed_head": "58d0da27736d6c22ca7c43f76ade497165b29919",
  "owner": "codex-ar1013-measurement-catalog-20260910",
  "plan": "../plans/AR-1013.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Define selectable ASB measurements grouped by stable semantic meaning.",
  "task_revision": 9,
  "title": "Version the measurement catalog and semantic groups",
  "updated_at": "2026-09-10T21:58:04+00:00",
  "worktree_key": "agent-systems-benchmark-measurement-catalog-semantics"
}
---
Create a versioned, machine-readable catalog for every selectable benchmark measurement. Group
measurements by semantic meaning (for example system resources, scheduling/contention, latency,
quality/reliability, fairness, cost, and provenance) while preserving individual metric identity,
units, aggregation, sampling overhead, availability, platform support, and evidence limits.

Acceptance criteria: schema and Rust types are versioned; duplicate/ambiguous names and incompatible
units are rejected; groups and metrics have stable IDs; live/replay/unsupported states are explicit;
CSB-derived metrics have provenance and no double counting; fixtures and negative tests cover unknown,
duplicate, unit-mismatch, unavailable, and privacy-sensitive metrics.

- 2026-09-10T21:25:00+00:00: Removed optional AR-0602 monitoring qualification as a hard
  prerequisite. The baseline catalog must represent unsupported or not-yet-qualified CSB measures
  explicitly; AR-0602 may add or qualify versioned catalog entries later without blocking the
  standalone measurement selector.

- 2026-09-10T21:43:33+00:00: AR-0101 and AR-1001 verified done; baseline catalog explicitly excludes
  optional AR-0602 qualification and all UI ownership

- 2026-09-10T21:44:21+00:00: Claimed by codex-ar1013-measurement-catalog-20260910.

- 2026-09-10T21:44:38+00:00: Recorded command exit 0; command argv SHA-256
  321c534968b9c456a64caf5e6d09b63780c507f97548057d2bfe31edcfd73ff4.

- 2026-09-10T21:44:56+00:00: Recorded command exit 0; command argv SHA-256
  bb90acfc3bcc7d3647d0c0b049c9609dba80bcd927f6184e4bc0ad084debdde1.

- 2026-09-10T21:58:04+00:00: Recorded command exit 127; command argv SHA-256
  0079efd3277b8ed9284ec70bd5cb39197b07709e937708b082347986c33de513.
