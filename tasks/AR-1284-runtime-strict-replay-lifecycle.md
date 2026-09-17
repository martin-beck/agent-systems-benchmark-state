---
{
  "branch": "feature/ar-1284-strict-replay-lifecycle",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-17T03:23:52+00:00",
  "depends_on": [
    "AR-1282",
    "AR-1237",
    "AR-1238",
    "AR-1239"
  ],
  "id": "AR-1284",
  "next_action": "Inspect merged AR-1282 transport and implement the smallest runtime-issued primary replay lifecycle entrypoint; then focused tests.",
  "observed_branch": "feature/ar-1284-strict-replay-lifecycle",
  "observed_dirty": 0,
  "observed_head": "f9ddf7ef6b3b2a96dd7faee04906f4e5cb3aa8e1",
  "owner": "asb_ar1024_lifecycle_router",
  "plan": "../plans/AR-1284.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Connect authenticated replay transport to the runtime-owned primary strict-replay lifecycle.",
  "task_revision": 7,
  "title": "Runtime-owned strict-replay lifecycle execution",
  "updated_at": "2026-09-17T01:24:50+00:00",
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

- 2026-09-17T01:23:41+00:00: AR-1282 merged; dependencies verified; promote runtime-owned lifecycle
  successor

- 2026-09-17T01:23:52+00:00: Claimed by asb_ar1024_lifecycle_router.

- 2026-09-17T01:24:30+00:00: Setup complete: declared worktree
  agent-systems-benchmark-ar-1284-strict-replay-lifecycle created from protected origin/main
  f9ddf7ef6b3b2a96dd7faee04906f4e5cb3aa8e1, which includes merged AR-1282 PR #208. Worktree is
  isolated and clean; no asb-tui paths touched.

- 2026-09-17T01:24:36+00:00: Recorded command exit 0; command argv SHA-256
  5e5d4bd1c068a67556bc6853653a8b06f2a1e0bcc663f81fe9ec267d4ade80ec.

- 2026-09-17T01:24:50+00:00: Recorded command exit 0; command argv SHA-256
  e2aff9b950e59fca66955f04fa51dbea4a898e0e7cf1e76a46b5d34b50fda729.
