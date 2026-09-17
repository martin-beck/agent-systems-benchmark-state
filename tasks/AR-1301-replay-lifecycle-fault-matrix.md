---
{
  "branch": "feature/ar-1301-replay-lifecycle-fault-matrix",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-17T10:34:33+00:00",
  "depends_on": [
    "AR-1287",
    "AR-1300"
  ],
  "id": "AR-1301",
  "next_action": "Promote only after AR-1287 and AR-1300 are done; implement the executable supervised replay lifecycle fault matrix and qualify it on the approved runner.",
  "observed_branch": "feature/ar-1301-replay-lifecycle-fault-matrix",
  "observed_dirty": 0,
  "observed_head": "7ea3e001dffa13eca5ff0f05444c2b3b9d4df928",
  "owner": "coordinator-ar1301-lifecycle-20260917",
  "plan": "../plans/AR-1301.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Qualify strict-replay supervised lifecycle faults, isolation and cleanup end to end.",
  "task_revision": 11,
  "title": "Supervised replay lifecycle fault matrix",
  "updated_at": "2026-09-17T09:17:09+00:00",
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
