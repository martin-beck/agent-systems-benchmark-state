---
{
  "branch": "feature/ar-1498-authenticated-lifecycle-executor",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-28T17:03:11+00:00",
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
  "owner": "ar1498-lifecycle-executor",
  "plan": "../plans/AR-1498.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Provide the authenticated artifact executor and activation authority behind the ASB agent lifecycle router.",
  "task_revision": 6,
  "title": "Authenticated lifecycle artifact executor",
  "updated_at": "2026-09-28T15:06:28+00:00",
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
