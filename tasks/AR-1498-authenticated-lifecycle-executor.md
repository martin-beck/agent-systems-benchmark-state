---
{
  "branch": "feature/ar-1498-authenticated-lifecycle-executor",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-28T18:49:25+00:00",
  "depends_on": [
    "AR-1018",
    "AR-1019",
    "AR-1020",
    "AR-1190",
    "AR-1191",
    "AR-1496"
  ],
  "id": "AR-1498",
  "next_action": "Promote after coordinator review; define and implement the authenticated artifact executor and activation authority required by ASB lifecycle calls, with fail-closed restart-safe tests.",
  "observed_branch": "feature/ar-1498-authenticated-lifecycle-executor",
  "observed_dirty": 1,
  "observed_head": "8c53a4a62ecaa6fecc9eb195a105fc368a3395c8",
  "owner": "ar1498-repair-luna56",
  "plan": "../plans/AR-1498.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Provide the authenticated artifact executor and activation authority behind the ASB agent lifecycle router.",
  "task_revision": 19,
  "title": "Authenticated lifecycle artifact executor",
  "updated_at": "2026-09-28T16:52:39+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1498"
}
---

AR-1199 correctly exposes the authenticated renderer-neutral lifecycle route but remains
fail-closed because `AgentPackage` currently carries only public digest/provenance and no
runtime-owned executor or activation authority. This AR owns that missing ASB backend seam.
It must not add TUI rendering or accept arbitrary paths, ambient credentials, unsigned artifacts,
or raw secrets.

Acceptance requires an authenticated, owner-bound executor that validates signed artifact identity,
target/libc compatibility, generation and idempotency, performs transactional install/activation,
and persists restart-safe lifecycle state for install, status, cancel, retry and remove. Missing,
stale, malformed, unauthorized, interrupted or unavailable artifacts must remain explicit typed
failures. Add clean-home, cancellation/restart, privacy and negative-boundary tests plus exact
protocol/schema fixtures consumed by AR-1199 and downstream asb-tui.

- 2026-09-28T15:02:01+00:00: Promoted as the scoped successor required by blocked AR-1199: implement
  authenticated lifecycle artifact executor and activation authority before reopening router/TUI
  lifecycle support.

- 2026-09-28T15:03:11+00:00: Claimed by ar1498-lifecycle-executor.

- 2026-09-28T15:04:22+00:00: Recorded command exit 0; command argv SHA-256
  9535b5c71d4da7776f57501570e066f9abc80c9403a1abe7a165e323102ef2c4.

- 2026-09-28T16:42:24+00:00: Coordinator-authorized takeover: owner process absent; partial attempt
  independently reviewed as incomplete/non-compiling. Release claim for repair worker without
  deleting worktree or evidence.

- 2026-09-28T16:42:51+00:00: Claimed by ar1498-repair-luna56.

- 2026-09-28T16:45:22+00:00: Recorded command exit 0; command argv SHA-256
  ff6d1fa7a7185010f75fcfafe4bdc1bdd5b9804d8c2b3e7abdd8a1b96cd81c63.

- 2026-09-28T16:46:10+00:00: Heartbeat by ar1498-repair-luna56.

- 2026-09-28T16:49:25+00:00: Heartbeat by ar1498-repair-luna56.

- 2026-09-28T16:49:28+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-28T16:50:02+00:00: Recorded command exit 101; command argv SHA-256
  73d005d4c4983870f0c5405c6c97dffbf521d57825b14d75dae888988fbdcd03.

- 2026-09-28T16:50:39+00:00: Focused cargo check failed closed: Catalog initializer omitted newly
  required agent_lifecycles field at crates/asb-cli/src/control.rs:1179 (E0063). Next action:
  initialize lifecycle journal/generation/idempotency fields, rerun cargo check through handoffctl.

- 2026-09-28T16:50:51+00:00: Recorded command exit 0; command argv SHA-256
  73d005d4c4983870f0c5405c6c97dffbf521d57825b14d75dae888988fbdcd03.

- 2026-09-28T16:51:34+00:00: Recorded command exit 101; command argv SHA-256
  1c69a4443966f5d335a0a526d0dac73a6d618685bc20a635e78578f17fe0d354.

- 2026-09-28T16:51:56+00:00: Focused lifecycle test failed: unavailable-roster fixture intentionally
  supplies placeholder catalog digest, but binding validation returned StaleIdentity before the
  expected CapabilityUnavailable. Next action: preserve fail-closed unavailable behavior by checking
  unavailable catalog identity before requiring digest, then rerun focused test.

- 2026-09-28T16:52:20+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-28T16:52:39+00:00: Recorded command exit 0; command argv SHA-256
  7fa4b9472adbf204ff68328115c1faea12b166e891b8fe3ae77e6bccd27d5563.
