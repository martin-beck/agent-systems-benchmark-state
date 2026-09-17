---
{
  "branch": "feature/ar-1284-strict-replay-lifecycle",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1282",
    "AR-1237",
    "AR-1238",
    "AR-1239"
  ],
  "id": "AR-1284",
  "next_action": "Promote after dependency verification; implement runtime-issued primary replay lifecycle and bounded supervised fixtures.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1284.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Connect authenticated replay transport to the runtime-owned primary strict-replay lifecycle.",
  "task_revision": 1,
  "title": "Runtime-owned strict-replay lifecycle execution",
  "updated_at": "2026-09-17T01:21:57Z",
  "worktree_key": "agent-systems-benchmark-ar-1284-strict-replay-lifecycle"
}
---

## AR-1284

Implement the next ASB-only runtime boundary after AR-1282. Consume the merged authenticated
transport through a runtime-issued handoff and connect the actual primary strict-replay command to
supervised cassette execution without claiming asb-tui behavior.

- 2026-09-17T01:21:57Z: Created as the dependency-safe successor to the repeatedly blocked
  AR-1260--AR-1281 lifecycle slices. AR-1282 is merged and supplies the transport foundation;
  the blocked predecessors remain historical evidence and are not reused.

### Scope and ownership

Repository: `martin-beck/agent-systems-benchmark` only. Owned paths are the runtime, replay, and
CLI primary dispatch/lifecycle code plus focused integration fixtures and tests. No asb-tui source,
renderer, terminal, or frontend paths are in scope.

### Acceptance

- The primary strict-replay command receives an opaque runtime-issued handoff rather than creating
  an untrusted relay or literal namespace readiness value.
- Supervised cassette request/response execution is bounded and authenticated, with malformed,
  stale, duplicate, missing-endpoint, and fallback paths rejected fail closed.
- Positive child execution proves provider and descendant egress denial; cancellation, timeout,
  crash, restart, cleanup, and unrelated-process non-interference are covered.
- Fixtures are offline, digest/policy bounded, privacy-safe, and do not retain credentials or
  unbounded subprocess output.
- Focused and full locked tests, fmt, Clippy, rustdoc, repository policy, formal, portability,
  independent exact-head review, signed/DCO PR merge, and exact-main post-merge workflows pass.

Do not claim completion from transport-only tests, mock-only lifecycle evidence, or a CLI path that
constructs its own relay. If runtime-owned attestation or sandbox capability is still missing,
record the exact blocker and split a further dependency-safe successor instead of weakening gates.
