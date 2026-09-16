---
{
  "branch": "feature/distributed-workers",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-16T14:28:01+00:00",
  "depends_on": [
    "AR-0204",
    "AR-0702",
    "AR-1001"
  ],
  "id": "AR-1006",
  "next_action": "Repair worker-loss restart fencing: remove/revoke lease epoch or otherwise reject old completion after same-ID re-registration; add regression test, rerun gates, then request review before publication.",
  "owner": "asb_ar1006_distributed_workers",
  "plan": "../plans/AR-1006.md",
  "priority": "P3",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Schedule trials across native-capability workers while preserving per-host capacity meaning.",
  "task_revision": 12,
  "title": "Coordinate distributed experiment workers",
  "updated_at": "2026-09-16T12:28:55+00:00",
  "worktree_key": "agent-systems-benchmark-distributed-workers"
}
---
## AR-1006

Schedule trials across native-capability workers while preserving per-host capacity meaning.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-16T12:24:16+00:00: Dependencies AR-0204, AR-0702 and AR-1001 are complete; promote
  distributed-worker coordination.

- 2026-09-16T12:24:19+00:00: Claimed by asb_ar1006_distributed_workers.

- 2026-09-16T12:24:34+00:00: Recorded command exit 0; command argv SHA-256
  c1fd55a9d07171b8bd8e3da0dd0b73827d43b091027d081376d30b02d3a72bb8.

- 2026-09-16T12:26:09+00:00: Recorded command exit 1; command argv SHA-256
  426f163981be08df5024ad1c5e3dadf7ef4c423b178ed383440d14f2c7513bc2.

- 2026-09-16T12:26:33+00:00: Recorded command exit 101; command argv SHA-256
  f84916c3e0174121a57a24b947ea267fc6b1b1160b38f8606d58555b81db140b.

- 2026-09-16T12:27:00+00:00: Recorded command exit 0; command argv SHA-256
  f84916c3e0174121a57a24b947ea267fc6b1b1160b38f8606d58555b81db140b.

- 2026-09-16T12:27:21+00:00: Recorded command exit 0; command argv SHA-256
  1c1debec106f03aeb91d21e665446491ac8f0c18fe677af397c5a8d694b2ffca.

- 2026-09-16T12:27:36+00:00: Recorded command exit 0; command argv SHA-256
  f9c93ecbdf553febd48da88ae4e098fbc275b84b9beb4b3e159f50b19c3d66ef.

- 2026-09-16T12:27:58+00:00: Implemented pure bounded asb-analysis distributed coordinator in
  signed+DCO commit 1a41d0b and pushed feature/distributed-workers. Added validated worker
  capabilities, capacity-aware leases, monotonic expiry fencing, retry-distinct attempts,
  worker-loss invalidation, duplicate/stale completion rejection, bounded artifact digests, and
  host-local duration plus uncertainty (no cross-host subtraction). Focused distributed tests 3/3
  pass; full asb-analysis package 28 unit/integration + 5 doctests pass; clippy -D warnings passes;
  diff check clean. PR publication/review/CI remain.

- 2026-09-16T12:28:01+00:00: Heartbeat by asb_ar1006_distributed_workers.

- 2026-09-16T12:28:55+00:00: Independent exact-head review of signed 1a41d0b found blocker:
  Coordinator::remove clears worker and active_attempts but leaves leases entry/fence.
  Re-registering the same WorkerId before old expiry can therefore allow the old completion
  (worker/fence still match), violating worker-loss/restart invalidation acceptance. Existing
  negative test removes worker but does not re-register same ID. PR publication paused pending
  fail-closed repair.
