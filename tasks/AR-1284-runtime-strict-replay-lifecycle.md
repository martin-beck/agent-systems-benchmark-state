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
  "next_action": "Split a runtime-owned launch-factory/CLI entrypoint successor: current protected main has only caller-constructible ReplayTransportIssuer and SandboxBackend APIs, so AR-1284 cannot safely wire primary replay without fabricating authority.",
  "observed_branch": "feature/ar-1284-strict-replay-lifecycle",
  "observed_dirty": 0,
  "observed_head": "f9ddf7ef6b3b2a96dd7faee04906f4e5cb3aa8e1",
  "owner": "",
  "plan": "../plans/AR-1284.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "blocked",
  "summary": "Connect authenticated replay transport to the runtime-owned primary strict-replay lifecycle.",
  "task_revision": 12,
  "title": "Runtime-owned strict-replay lifecycle execution",
  "updated_at": "2026-09-17T01:26:40+00:00",
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

- 2026-09-17T01:25:19+00:00: Recorded command exit 0; command argv SHA-256
  771eac905e8dcf88a2538b3b9d4dba74c7c07db8a1a8c4748df8f9c8e0ace411.

- 2026-09-17T01:25:47+00:00: Recorded command exit 0; command argv SHA-256
  36c571ad891aa3f703a376cee9ea11d1c6f71c532e6ba09b743b20cfa7d4d72e.

- 2026-09-17T01:26:28+00:00: Heartbeat by asb_ar1024_lifecycle_router.

- 2026-09-17T01:26:31+00:00: Implementation audit blocker: protected origin/main f9ddf7ef includes
  AR-1282 transport and its focused runtime transport suite passes 6/6. The primary CLI replay() at
  crates/asb-cli/src/lib.rs:399 only decodes/indexes a cassette and emits metadata; it does not
  invoke runtime supervision. ReplayTransportIssuer::bind and SandboxBackend::new/spawn_launch are
  caller-constructible APIs; no runtime-owned factory supplies authenticated SandboxLaunchInput,
  ResourceLease, pinned supervisor/sidecar commands, or a cassette service callback. Adding a
  CLI-side constructor would violate AR acceptance and prior review boundaries. AR-1284 worktree is
  clean at f9ddf7ef; no product mutation and no asb-tui paths touched.

- 2026-09-17T01:26:40+00:00: Release blocked/ownerless after implementation audit. Protected main
  f9ddf7ef includes merged AR-1282 and runtime transport tests pass 6/6, but primary asb-cli
  replay() remains metadata-only. Existing ReplayTransportIssuer::bind and
  SandboxBackend::new/spawn_launch are caller-constructible; no runtime-owned launch factory/opaque
  handoff supplies SandboxLaunchInput, ResourceLease, pinned supervisor/sidecar commands, or
  cassette service callback. Wiring these in CLI would fabricate authority and violate fail-closed
  acceptance. Worktree agent-systems-benchmark-ar-1284-strict-replay-lifecycle is clean at f9ddf7ef;
  no product mutation or asb-tui changes. Next action: create a narrowly scoped runtime-owned
  launch-factory/CLI entrypoint AR, then implement lifecycle and egress fixtures there.
