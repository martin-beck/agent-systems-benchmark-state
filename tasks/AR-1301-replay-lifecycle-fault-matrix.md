---
{
  "branch": "feature/ar-1301-replay-lifecycle-fault-matrix",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1287",
    "AR-1300"
  ],
  "id": "AR-1301",
  "next_action": "Promote only after AR-1287 and AR-1300 are done; implement the executable supervised replay lifecycle fault matrix and qualify it on the approved runner.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "98acd6d5f5a206b351a54689e7817dd43af406ca",
  "owner": "",
  "plan": "../plans/AR-1301.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "open",
  "summary": "Qualify strict-replay supervised lifecycle faults, isolation and cleanup end to end.",
  "task_revision": 2,
  "title": "Supervised replay lifecycle fault matrix",
  "updated_at": "2026-09-17T09:04:13+00:00",
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
