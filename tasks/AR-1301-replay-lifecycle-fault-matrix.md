---
{
  "branch": "feature/ar-1301-replay-lifecycle-fault-matrix",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-17T10:55:48+00:00",
  "depends_on": [
    "AR-1287",
    "AR-1300"
  ],
  "id": "AR-1301",
  "next_action": "Promote only after AR-1287 and AR-1300 are done; implement the executable supervised replay lifecycle fault matrix and qualify it on the approved runner.",
  "observed_branch": "feature/ar-1301-replay-lifecycle-fault-matrix",
  "observed_dirty": 1,
  "observed_head": "7ea3e001dffa13eca5ff0f05444c2b3b9d4df928",
  "owner": "coordinator-ar1301-lifecycle-20260917",
  "plan": "../plans/AR-1301.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Qualify strict-replay supervised lifecycle faults, isolation and cleanup end to end.",
  "task_revision": 30,
  "title": "Supervised replay lifecycle fault matrix",
  "updated_at": "2026-09-17T09:30:29+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1301-replay-lifecycle-fault-matrix"
}
---

## AR-1301

Add and qualify the executable ASB integration matrix still missing from PR #215: successful
strict-replay request/response, provider and descendant egress denial, timeout, cancellation,
crash, restart, cleanup/reaping, unrelated-process isolation and no-live-fallback behavior.
Every case must run through the real runtime-owned dispatch and supervised child lifecycle; no
ignored or caller-simulated test may be used as completion evidence.

This is a focused follow-on to AR-1300 and the blocked AR-1286 lifecycle work. AR-1287 provides the
approved signed multi-architecture Bubblewrap/systemd runner and is a hard dependency because host
namespace capability is not sufficient. Preserve AR-1286 and AR-1287 history; do not weaken their
gates or revive old PR branches. Scope is ASB only: lifecycle runner integration, test fixtures,
schemas/docs and bounded evidence under `crates/asb-runtime`, `crates/asb-replay`, `crates/asb-cli`
and repository test infrastructure. Do not modify asb-tui or coordinator implementation.


- 2026-09-17T09:04:13+00:00: Dependencies AR-1287 and AR-1300 are now durably done; AR-1287
  runner/KVM qualification and repaired exact-main gates are green. Promote for implementation of
  the real supervised replay lifecycle fault matrix.

- 2026-09-17T09:04:33+00:00: Claimed by coordinator-ar1301-lifecycle-20260917.

- 2026-09-17T09:04:53+00:00: Recorded command exit 0; command argv SHA-256
  e3f8b27bf55cc5a899f6fbef1e50d3d7d4f1d4aea9cc10f0b6d093e1d278001e.

- 2026-09-17T09:10:12+00:00: Recorded command exit 0; command argv SHA-256
  98d7da7c8f339087cb458fcc6a9a8de62dc00f691bd8bb3cb3b637c423a5a38e.

- 2026-09-17T09:13:36+00:00: Recorded command exit 1; command argv SHA-256
  31e231953d8a0d5bbdfae1f833e30156183cdf9a73ecf83b810e158abfeb9c6d.

- 2026-09-17T09:15:27+00:00: Recorded command exit 1; command argv SHA-256
  d895c37b205165b0192e4ab4e19944fc2127b66e99d4c71a2a9b435c36347580.

- 2026-09-17T09:15:37+00:00: Recorded command exit 1; command argv SHA-256
  e0ddf609d0da21c540090189fd8225abb05fee0f56710ccbd5b0d3bda989c192.

- 2026-09-17T09:16:21+00:00: Recorded command exit 255; command argv SHA-256
  18c27e0f363eb006b95d1a1908652c624d05bd12d4b75248b1f7754f0a986652.

- 2026-09-17T09:17:09+00:00: Recorded command exit 1; command argv SHA-256
  cbe7279d6b1db469ac8eb5412d4c15714b2e3a130f3410903ce6734d12bad4d3.

- 2026-09-17T09:18:20+00:00: Recorded command exit 0; command argv SHA-256
  f663c16ba03070c3f0962c7ba018a53d439741581d768c4797eb671389f6dc69.

- 2026-09-17T09:18:44+00:00: Recorded command exit 1; command argv SHA-256
  19f1162efd99befcf48aa723806b5dfe259bd82446da6a6c5fe68c439d7ffae6.

- 2026-09-17T09:18:59+00:00: Recorded command exit 32; command argv SHA-256
  4d070b83878e8695e4940457427bc6913d2106905d1011a12ead64bae7f96839.

- 2026-09-17T09:19:16+00:00: Recorded command exit 1; command argv SHA-256
  9f6e65ff172658bdcf829961164cedc8fc086c994aa979e5d3a5e0e86545cb86.

- 2026-09-17T09:19:47+00:00: Recorded command exit 0; command argv SHA-256
  9f6e65ff172658bdcf829961164cedc8fc086c994aa979e5d3a5e0e86545cb86.

- 2026-09-17T09:23:43+00:00: Recorded command exit 0; command argv SHA-256
  830309b4035a180a11c454cc5becab08f0a387b419cf9b6aaf3dfbedf12d5c00.

- 2026-09-17T09:25:48+00:00: Heartbeat by coordinator-ar1301-lifecycle-20260917.

- 2026-09-17T09:25:51+00:00: Recorded command exit 101; command argv SHA-256
  548cbf08f922ba65a7606053d8957418a7ba3f684f3d5830d1ba9ba64d09cd6a.

- 2026-09-17T09:26:09+00:00: Recorded command exit 101; command argv SHA-256
  aef90ad837a90e25ed5f224f7352b79f46b3c2f0bd42d034d9be7804d0bfeb46.

- 2026-09-17T09:26:18+00:00: Recorded command exit 0; command argv SHA-256
  d93ecdb078dcc73bd5e583dc7ee2a9c51757876456749d8cf0dbd6ebd1116523.

- 2026-09-17T09:26:48+00:00: Recorded command exit 1; command argv SHA-256
  eb30afcb41b351282fc60335418aa4b5b408a36075a19a250b73d64c66db04b8.

- 2026-09-17T09:27:10+00:00: Recorded command exit 0; command argv SHA-256
  40e97611e5c80a882600f001119d8d61489fe0e002cd3c0db0e761a1b4c4c0d2.

- 2026-09-17T09:28:11+00:00: Recorded command exit 1; command argv SHA-256
  da9db2dbe742113f306c044d1a16c1e21ffb1aec08f3f41d58d55c2eecac6c84.

- 2026-09-17T09:28:51+00:00: Recorded command exit 1; command argv SHA-256
  da9db2dbe742113f306c044d1a16c1e21ffb1aec08f3f41d58d55c2eecac6c84.

- 2026-09-17T09:29:08+00:00: Recorded command exit 101; command argv SHA-256
  a76666b22fdcfdca396667b4fce9e9e6be13ae40edd06f493bd2f944dc8187bf.

- 2026-09-17T09:30:29+00:00: Recorded command timeout; classification=SUBPROCESS_TIMEOUT;
  deadline=20.0s; command argv SHA-256
  a76666b22fdcfdca396667b4fce9e9e6be13ae40edd06f493bd2f944dc8187bf.
