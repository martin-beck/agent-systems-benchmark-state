---
{
  "branch": "feature/measurement-catalog-semantics",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-0101",
    "AR-1001"
  ],
  "id": "AR-1013",
  "next_action": "Define and review the versioned measurement catalog and semantic grouping contract before implementation.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1013.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "open",
  "summary": "Define selectable ASB measurements grouped by stable semantic meaning.",
  "task_revision": 3,
  "title": "Version the measurement catalog and semantic groups",
  "updated_at": "2026-09-10T21:43:33+00:00",
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
