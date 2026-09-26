---
{
  "branch": "feature/ar-1444-first-class-journey-qualification",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-26T19:35:49+00:00",
  "depends_on": [
    "AR-1443"
  ],
  "id": "AR-1444",
  "next_action": "Promote after AR-1443 and paired asb-tui AR-1327 are done; run the disposable cross-repository journey and publish the support/release gate.",
  "owner": "ar1444-journey-qualification-luna56",
  "plan": "../plans/AR-1444.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Make the complete install-to-comparison journey a cross-repository release qualification gate.",
  "task_revision": 4,
  "title": "First-class journey qualification",
  "updated_at": "2026-09-26T17:35:49+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1444-first-class-journey-qualification"
}
---

This AR is a qualification and release gate. It must not claim live OpenRouter
reachability from local mocks or replay evidence.

- 2026-09-26T17:33:23+00:00: AR-1443 and the paired asb-tui AR-1327 are durably done. Promote
  ASB-owned first-class journey qualification; do not modify asb-tui, use pinned external acceptance
  artifacts and local/mock qualification.

- 2026-09-26T17:34:39+00:00: Claimed by ar1444-journey-qualification-luna56.

- 2026-09-26T17:35:49+00:00: Heartbeat by ar1444-journey-qualification-luna56.
