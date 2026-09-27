---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-27T07:53:57+00:00",
  "depends_on": [],
  "id": "AR-1479",
  "next_action": "Promote and claim the isolated repair worktree; reproduce both exact Rust failures before changing any test or synchronization code.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "0000000000000000000000000000000000000000",
  "owner": "coordinator",
  "plan": "../plans/AR-1479-rust-ci-flake-repair.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Repair the unrelated Rust state-root collision and malformed-ready-marker timing flakes blocking AR-1420 exact-head CI.",
  "task_revision": 2,
  "title": "Rust CI timing and state-root flake repair",
  "updated_at": "2026-09-27T07:23:57+00:00",
  "worktree_key": ""
}
---

Created from AR-1420 exact-head CI evidence. Rust failed first in
`control::tests::production_backend_runs_without_frontend_and_recovers_idempotency`
with a state-root ownership collision; the approved retry then failed in
`gemini::tests::malformed_ready_marker_fails_fast_and_cleans_run_root` because
the elapsed-time assertion exceeded one second. Both failures are outside the
AR-1420 product diff and must be independently repaired before that PR can be
requalified. Preserve fail-closed cleanup and bounded execution semantics.

- 2026-09-27T07:23:57+00:00: Claimed by coordinator.
