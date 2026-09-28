---
{
  "branch": "feature/ar-1498-authenticated-lifecycle-executor",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1018", "AR-1019", "AR-1020", "AR-1190", "AR-1191", "AR-1496"],
  "id": "AR-1498",
  "next_action": "Promote after coordinator review; define and implement the authenticated artifact executor and activation authority required by ASB lifecycle calls, with fail-closed restart-safe tests.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1498.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Provide the authenticated artifact executor and activation authority behind the ASB agent lifecycle router.",
  "task_revision": 1,
  "title": "Authenticated lifecycle artifact executor",
  "updated_at": "2026-09-28T00:00:00+00:00",
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
