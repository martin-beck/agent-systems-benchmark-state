---
{
  "branch": "feature/ar-1300-runtime-cassette-dispatch-seam",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1282",
    "AR-1285"
  ],
  "id": "AR-1300",
  "next_action": "Promote after AR-1282 and AR-1285 dependency verification; implement and test the runtime-to-replay cassette operation seam from protected main.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "98acd6d5f5a206b351a54689e7817dd43af406ca",
  "owner": "",
  "plan": "../plans/AR-1300.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Connect runtime-issued cassette operations to the real strict-replay dispatch path.",
  "task_revision": 1,
  "title": "Runtime-to-replay cassette dispatch seam",
  "updated_at": "2026-09-17T06:53:53Z",
  "worktree_key": "agent-systems-benchmark-ar-1300-runtime-cassette-dispatch-seam"
}
---

## AR-1300

Implement the missing ASB-only runtime-to-replay cassette operation seam identified by the
independent review of PRs #197 and #207. The primary replay command must consume a runtime-issued,
authenticated, single-use operation context and perform a real bounded request/response against
the strict-replay service. It must never accept caller-assembled launch authority, fabricate relay
or readiness state, contact a live provider, or fall back when the cassette operation fails.

This is a successor/follow-on implementation slice for the blocked AR-1271, AR-1273, AR-1262 and
AR-1286 evidence. Those records remain historical and must not be revived or treated as source
branches. AR-1282 supplies the authenticated transport and AR-1285 supplies the runtime launch
factory; both are required dependencies. The scope is ASB only: `crates/asb-core`,
`crates/asb-runtime`, `crates/asb-replay`, `crates/asb-cli`, their schemas/docs and credential-free
fixtures/tests. Do not modify asb-tui or coordinator implementation.

