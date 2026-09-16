---
{
  "branch": "feature/ar-1237-strict-replay-launch-bridge",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1233", "AR-1236"],
  "id": "AR-1237",
  "next_action": "Extend the reviewed strict-replay launch contract to map ReplayRelayHandoff into the child-visible HTTP loopback endpoint, with authenticated route/generation metadata and bounded lifecycle ownership.",
  "observed_branch": "feature/ar-1237-strict-replay-launch-bridge",
  "observed_dirty": 0,
  "observed_head": "11d37da2ec59fb5e2afe26c35d9c1bab1787f034",
  "owner": "",
  "plan": "../plans/AR-1237.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Map the authenticated relay into the strict-replay child launch contract.",
  "task_revision": 1,
  "title": "Strict-replay child launch bridge",
  "updated_at": "2026-09-16T07:08:39+00:00",
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
