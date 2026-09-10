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
  "observed_dirty": 7,
  "observed_head": "58d0da27736d6c22ca7c43f76ade497165b29919",
  "owner": "codex-ar1013-measurement-catalog-20260910",
  "plan": "../plans/AR-1013.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Define selectable ASB measurements grouped by stable semantic meaning.",
  "task_revision": 24,
  "title": "Version the measurement catalog and semantic groups",
  "updated_at": "2026-09-10T22:08:20+00:00",
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

- 2026-09-10T22:00:14+00:00: Recorded command exit 2; command argv SHA-256
  e4233f8770c5b300483a22e0a1eb4bc23917c2faf585291cb0157130eeca10e6.

- 2026-09-10T22:02:52+00:00: Recorded command exit 0; command argv SHA-256
  762ae9c8de069e93026706eaf03c66267c70a700948cb6c9a875fb31c06c9688.

- 2026-09-10T22:03:16+00:00: Recorded command exit 1; command argv SHA-256
  d40baf1381cec1e4b4a91d3638d8a3f4061d6d9323b569959f110a3b6932dc15.

- 2026-09-10T22:03:32+00:00: Recorded command exit 0; command argv SHA-256
  205af411b437012d653cf7d4181938ab95e0627b3cfc89beca92406d60662ba7.

- 2026-09-10T22:03:54+00:00: Recorded command exit 101; command argv SHA-256
  8f8e4634040d6917ed5f7fb09b4ca62c903a80d34fa95a1ba2be1144f912bbe8.

- 2026-09-10T22:04:41+00:00: Recorded command exit 0; command argv SHA-256
  f6a04f71d243493e0afeb79eeed366d6049b0c7457de2922b535bf844cf9ef95.

- 2026-09-10T22:05:02+00:00: Recorded command exit 101; command argv SHA-256
  bf1ec98a41cd2ce289b7dcbf9d0bee99e295b63e9c1e5d4a88d94ce0a3da459d.

- 2026-09-10T22:06:18+00:00: Recorded command exit 0; command argv SHA-256
  ee313bf3940b01b04cee7c97fa57a91082f3e84c258bef5db6e9c7815401291b.

- 2026-09-10T22:06:47+00:00: Recorded command exit 101; command argv SHA-256
  ef217a99a6e1021b0630dd2b0c0fa01adc845e76952ba0fa33ac1c3b04a5e1fd.

- 2026-09-10T22:07:08+00:00: Recorded command exit 0; command argv SHA-256
  7afa6fa1210d56b440d69b5dd1b34b4ef68496432a2dc3346b22a1a060aed88c.

- 2026-09-10T22:07:24+00:00: Recorded command exit 0; command argv SHA-256
  4290a212f503755e92daed95120abeea5118e2c4fe34340babfc99050f34d850.

- 2026-09-10T22:08:02+00:00: Recorded command exit 0; command argv SHA-256
  217fab3b16efcdeb9a82395734f9be72e41f68e6603da79b7f0b2fbafe257fb0.

- 2026-09-10T22:08:20+00:00: Recorded command exit 0; command argv SHA-256
  a2e82e837ce7e0c52f3abfe9aa2d2ed7ee17dd7920786014f25e55d4ec0d1b94.
