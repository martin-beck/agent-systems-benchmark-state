---
{
  "branch": "feature/ar-1237-strict-replay-launch-bridge",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-16T10:57:22+00:00",
  "depends_on": [
    "AR-1233",
    "AR-1236"
  ],
  "id": "AR-1237",
  "next_action": "Extend the reviewed strict-replay launch contract to map ReplayRelayHandoff into the child-visible HTTP loopback endpoint, with authenticated route/generation metadata and bounded lifecycle ownership.",
  "observed_branch": "feature/ar-1237-strict-replay-launch-bridge",
  "observed_dirty": 0,
  "observed_head": "fc2fa39e1107169412d6629d3bf9072c32f1c5c4",
  "owner": "asb_ar1237_launch_bridge_worker",
  "plan": "../plans/AR-1237.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Map the authenticated relay into the strict-replay child launch contract.",
  "task_revision": 15,
  "title": "Strict-replay child launch bridge",
  "updated_at": "2026-09-16T08:59:38+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1237"
}
---

Own the contract boundary between the approved LoopbackOnly runtime and strict-replay adapters.
Expose only the authenticated cassette endpoint, never provider endpoints or credentials. Reject
unknown, stale, duplicate, mismatched, or externally supplied route identities. Supervise the
sidecar and adapter together and tear down all sockets/routes on every terminal path.

Acceptance: real child cassette success, provider and descendant egress denial, unmatched request,
timeout, cancellation, restart, crash, partial launch, stale route, duplicate attempt, privacy-safe
bounded evidence, and unrelated-process non-interference. No TUI changes. Run signed-DCO focused/full
locked, privacy, policy, native, exact-head, and post-merge gates.

- 2026-09-16T08:48:43+00:00: AR-1233 and AR-1236 complete; promote strict-replay launch bridge
  implementation.

- 2026-09-16T08:49:14+00:00: Claimed by asb_ar1237_launch_bridge_worker.

- 2026-09-16T08:55:59+00:00: Clean origin/main branch 74150c3 adds focused launch_bridge contract
  and 2 rejection tests; locked workspace tests and Clippy pass. Full runtime integration is blocked
  because origin/main lacks the AR-1233/1236 runtime-issued ReplayRelayHandoff and SupervisorPlan
  types. Apply commit after those dependency payloads are merged, then add concrete runtime
  adapter/native lifecycle tests.

- 2026-09-16T08:57:16+00:00: Runtime handoff dependencies AR-1233/1236 are complete; reopen to
  integrate reviewed heads and run native launch-bridge tests.

- 2026-09-16T08:57:22+00:00: Claimed by asb_ar1237_launch_bridge_worker.

- 2026-09-16T08:59:30+00:00: Recorded command exit 0; command argv SHA-256
  107d2c928b5e3277e5bc61a7ec649e03d54bf54174b822dccfd7c1804547689b.
