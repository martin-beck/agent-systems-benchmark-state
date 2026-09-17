---
{
  "branch": "feature/ar-1300-runtime-cassette-dispatch-seam",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-17T09:01:32+00:00",
  "depends_on": [
    "AR-1282",
    "AR-1285"
  ],
  "id": "AR-1300",
  "next_action": "Promote after AR-1282 and AR-1285 dependency verification; implement and test the runtime-to-replay cassette operation seam from protected main.",
  "observed_branch": "feature/ar-1300-runtime-cassette-dispatch-seam",
  "observed_dirty": 0,
  "observed_head": "bd7d10d4a760a84fa42de2b1fa9e97e8ea85ba09",
  "owner": "ar1300_dispatch",
  "plan": "../plans/AR-1300.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Connect runtime-issued cassette operations to the real strict-replay dispatch path.",
  "task_revision": 10,
  "title": "Runtime-to-replay cassette dispatch seam",
  "updated_at": "2026-09-17T07:04:07+00:00",
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


- 2026-09-17T07:00:52+00:00: Dependencies AR-1282 and AR-1285 verified done; promote ASB-only
  runtime-to-replay dispatch seam

- 2026-09-17T07:01:32+00:00: Claimed by ar1300_dispatch.

- 2026-09-17T07:01:39+00:00: Recorded command exit 0; command argv SHA-256
  ea07ab3b67665f619b9a1dca7e44f093e0a7340deef748997c47ffda5e5acdda.

- 2026-09-17T07:02:04+00:00: Recorded command exit 0; command argv SHA-256
  1a8de5a310175902c47bab2296114b0ba62bc78073a6a3259b840ed586598472.

- 2026-09-17T07:02:21+00:00: Recorded command exit 0; command argv SHA-256
  dc3aa8e23b2d27a4f64dfa2d2aaba633d9f7eb7a552d995b24593f293ce06b25.

- 2026-09-17T07:02:36+00:00: Recorded command exit 0; command argv SHA-256
  a0e1f3fa60f9cb555044f5c56212713cabe21b943de015c19b5c1a47264d7790.

- 2026-09-17T07:03:55+00:00: Recorded command exit 0; command argv SHA-256
  9436ed4df3eda71a5127f63b07db1e1dcd3bcd92e61f5010c5bde8c9cb82fe2a.

- 2026-09-17T07:04:07+00:00: Recorded command exit 255; command argv SHA-256
  b5ee3857d808cc2b617700d589910a7a1ddc72ba808914702dbe8ba0c08b1a5d.
