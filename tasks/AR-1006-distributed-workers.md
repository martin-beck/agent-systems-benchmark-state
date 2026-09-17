---
{
  "branch": "feature/distributed-workers",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-0204",
    "AR-0702",
    "AR-1001"
  ],
  "id": "AR-1006",
  "next_action": "Monitor post-merge workflows for main 4e2820b until terminal; verify exact tree/signature/DCO/policy, then release AR-1006 done.",
  "observed_head": "98acd6d5f5a206b351a54689e7817dd43af406ca",
  "owner": "",
  "plan": "../plans/AR-1006.md",
  "priority": "P3",
  "schema_version": 1,
  "status": "done",
  "summary": "Schedule trials across native-capability workers while preserving per-host capacity meaning.",
  "task_revision": 28,
  "title": "Coordinate distributed experiment workers",
  "updated_at": "2026-09-16T12:44:53+00:00",
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

- 2026-09-16T12:29:35+00:00: Recorded command exit 101; command argv SHA-256
  9e1ba97415b81e1412ed9031c9d7e42233f6ac9f6b496aecf84eae4ae2deb85e.

- 2026-09-16T12:30:01+00:00: Recorded command exit 0; command argv SHA-256
  9e1ba97415b81e1412ed9031c9d7e42233f6ac9f6b496aecf84eae4ae2deb85e.

- 2026-09-16T12:30:18+00:00: Recorded command exit 0; command argv SHA-256
  df7082dea03bb6b76e1896a02121602a9c16d01240080b6c48a6d43940346120.

- 2026-09-16T12:30:40+00:00: Review repair complete in signed+DCO commit 23c9ba4 pushed.
  Coordinator::remove now expires every lease owned by the removed worker before allowing same-ID
  registration; regression test proves an old completion remains StaleLease after re-registration.
  Full asb-analysis package remains green: 28 tests, 5 doctests, clippy -D warnings, formatting and
  diff checks. Prior review blocker is addressed; publication still awaits independent exact-head
  review.

- 2026-09-16T12:30:42+00:00: Heartbeat by asb_ar1006_distributed_workers.

- 2026-09-16T12:31:21+00:00: Recorded command exit 0; command argv SHA-256
  864a5487a7178e431a5dfce37e47acd5c0752d5c5a52a4125137acc2aedcdac8.

- 2026-09-16T12:31:48+00:00: Independent re-review approved signed head
  23c9ba45c2bb602d273d3d7a002d5b05d533cac4: remove() now revokes all worker leases
  (expires_at_ns=0), and duplicate_completion_and_worker_loss_fail_closed re-registers the same
  WorkerId and rejects the old completion. Clean exact tree, diff check clean, SSH signature/DCO
  valid. Focused distributed tests 3/3 and asb-analysis clippy -D warnings pass.

- 2026-09-16T12:31:58+00:00: Recorded command exit 0; command argv SHA-256
  139a1df3ed6a2ced0f51b513a952ce50989c9af60be428bcb6c81e3107c91151.

- 2026-09-16T12:32:09+00:00: Recorded command exit 0; command argv SHA-256
  89c98605324b102512c2c98249d3d4a2309c852df010a30d60ab387693e48bd1.

- 2026-09-16T12:36:34+00:00: Recorded command exit 0; command argv SHA-256
  8ee7e6e2c4199aecb827abfc3ae43ea11d1e30108580bcfb52304851af74c307.

- 2026-09-16T12:39:00+00:00: Recorded command exit 0; command argv SHA-256
  96820bd475f44d26cab477ae9791dbb484dd317bcb8869872abadb6e94c246eb.

- 2026-09-16T12:39:14+00:00: Recorded command exit 0; command argv SHA-256
  248c84ae0822f5936fdd9095aedf89d30cbce1041ad1a921409bc31f4bd84228.

- 2026-09-16T12:40:03+00:00: Heartbeat by asb_ar1006_distributed_workers.

- 2026-09-16T12:40:16+00:00: PR #199 merged via signed local integration as
  4e2820bffe93234d02ca39b59067bf4442b08f95. Exact parents 3e8d58994eb2b3faeda9449e4186498cf86eeb86
  and 23c9ba45c2bb602d273d3d7a002d5b05d533cac4; exact reviewed tree
  5f2c06f795681bf502a02faadad23d1b2268d873; remote ref, SSH signature and DCO verified. Exact-head
  PR checks all green after transient unrelated Loom ExecutableFileBusy rerun succeeded. Post-merge
  runs started: 35097078851 fault, 35097078917 AArch64, 35097078871 repository quality, 35097079080
  Rust, 35097078950 hosted portability, 35097078829 formal; headers 35097078983 green.

- 2026-09-16T12:43:40+00:00: Heartbeat by asb_ar1006_distributed_workers.

- 2026-09-16T12:44:53+00:00: AR-1006 complete. PR #199 exact signed head
  23c9ba45c2bb602d273d3d7a002d5b05d533cac4 merged via signed local integration as
  4e2820bffe93234d02ca39b59067bf4442b08f95. Remote main verified exact with parents 3e8d589 and
  23c9ba4, tree 5f2c06f795681bf502a02faadad23d1b2268d873, valid SSH signature and DCO. All PR checks
  green after unrelated Loom ExecutableFileBusy rerun. All seven post-merge workflows terminal
  SUCCESS: AArch64 35097078917, formal 35097078829, hosted 35097078950, repository quality
  35097078871, Rust 35097079080, fault assurance 35097078851, headers 35097078983. Worker
  capability/capacity leases, fencing, worker-loss invalidation, duplicate/stale completion
  rejection, bounded digests and host-local timing acceptance satisfied.
