---
{
  "branch": "feature/frontend-control-api",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-07T04:26:28+00:00",
  "depends_on": [
    "AR-0101",
    "AR-0104",
    "AR-0204",
    "AR-0801"
  ],
  "id": "AR-0803",
  "next_action": "Define a bounded versioned control/status API between the runner and independent frontends.",
  "observed_branch": "feature/frontend-control-api",
  "observed_dirty": 2,
  "observed_head": "61b5dd33ba04295a476e444d8bfd338ab972507a",
  "owner": "root-coordination-20260906",
  "plan": "../plans/AR-0803.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Expose runner planning, launch, status, cancellation, history, and analysis through a stable frontend boundary.",
  "task_revision": 11,
  "title": "Define the frontend control API",
  "updated_at": "2026-09-07T03:17:52+00:00",
  "worktree_key": "agent-systems-benchmark-frontend-control-api"
}
---
## AR-0803

Expose runner planning, launch, status, cancellation, history, and analysis through a stable frontend boundary.

The benchmark runner remains independently operable when no frontend is present or when a frontend crashes.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-07T02:56:13+00:00: Dependencies AR-0101, AR-0104, AR-0204 and AR-0801 are durably done;
  AR-0801 exact-main b2833ab CI and post-merge verification are green. Promote the highest-priority
  compatible frontend control boundary after releasing its Cargo/scheduler fences.

- 2026-09-07T02:56:28+00:00: Claimed by root-coordination-20260906.

- 2026-09-07T03:12:45+00:00: Recorded command exit 0; command argv SHA-256
  2112362c51cef85781237610d9b9e060605ef818fbc3842b7637243011b6072d.

- 2026-09-07T03:14:02+00:00: Recorded command exit 2; command argv SHA-256
  48458d4adcbc2714c4ae60f17ec39d916357031118af6e75d9a5cd826c73f20e.

- 2026-09-07T03:14:55+00:00: Recorded command exit 1; command argv SHA-256
  119a2544b57bc260d3736a8c380cb862336dcb3828b84394350db9659ad2e775.

- 2026-09-07T03:15:19+00:00: Recorded command exit 2; command argv SHA-256
  8bc998ab7b97ddd3689435d527789bef02f835b0eaf4edea3eb44d40eda18b6d.

- 2026-09-07T03:16:20+00:00: Recorded command exit 0; command argv SHA-256
  0abe16459841183b1c87533de5496a6b32348f12b93116537775513a95c9fca7.

- 2026-09-07T03:17:52+00:00: Recorded command exit 0; command argv SHA-256
  fca74cf20e25dfa6f5c081431044ca67513dad3c8d08f41a256e74b0f8c1d7ea.
