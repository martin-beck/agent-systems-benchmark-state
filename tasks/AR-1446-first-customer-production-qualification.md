---
{
  "branch": "qualification/ar-1446-first-customer-production",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-25T17:11:34+00:00",
  "depends_on": [
    "AR-1433",
    "AR-1441",
    "AR-1442",
    "AR-1443"
  ],
  "id": "AR-1446",
  "next_action": "Promote and claim this ASB-only disposable first-customer qualification gate. Verify clean install/bootstrap, setup/reconfiguration, local benchmark matrix, strict offline replay, recovery, cleanup, rollback, and bounded readiness evidence. AR-0903's broad release package and AR-1336's optional live-provider documentation remain separate; AR-1444/asb-tui and AR-1329 external-provider integration must not block this gate.",
  "observed_branch": "qualification/ar-1446-first-customer-production",
  "observed_dirty": 0,
  "observed_head": "2872a31f2ee90ac5df1a47203b2a618b1829cfec",
  "owner": "coordinator-ar1446",
  "plan": "../plans/AR-1446.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Qualify ASB in a disposable first-customer production-like environment.",
  "task_revision": 10,
  "title": "First-customer production qualification",
  "updated_at": "2026-09-25T15:42:04+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1446-first-customer-production"
}
---

This is the customer-facing integration gate. The deterministic local mock path remains the mandatory development and hosted qualification route; operator live-provider smoke evidence is optional and separately classified.

- 2026-09-25T15:00:00+00:00: Created from the production-readiness audit. Existing feature ARs cover individual capabilities but no AR verifies the complete disposable first-customer install/configure/benchmark/replay/recovery/cleanup journey with an explicit support and rollback report.

- 2026-09-25T17:15:00+00:00: Deterministic runtime mock dependency AR-1433 is now
  released and exact-main verified. Remaining prerequisites are the install/setup,
  campaign/journey, support-matrix, and milestone release ARs; optional AR-1329
  external-provider integration is intentionally not a prerequisite.

- 2026-09-25T17:20:00+00:00: Scope clarified as ASB-only. Removed the separate
  cross-repository AR-1444/asb-tui qualification from this gate's dependencies;
  that UI gate remains independently tracked and is not modified here.

- 2026-09-25T15:38:27+00:00: ASB-only dependencies AR-1433, AR-1441, AR-1442, and AR-1443 are done.
  Removed broad AR-0903 and optional live-doc AR-1336 blockers; promote disposable first-customer
  qualification.

- 2026-09-25T15:38:30+00:00: Claimed by coordinator-ar1446.

- 2026-09-25T15:38:51+00:00: Recorded command exit 0; command argv SHA-256
  ca95b856be82e838da8e97f906281cede2302b242d9cc8057278f96ec4a512c0.

- 2026-09-25T15:39:35+00:00: Recorded command exit 0; command argv SHA-256
  3d5811df1ef4712c2f0b86ccd1a7ae38494283569f69b0a201f79d19ec456381.

- 2026-09-25T15:41:34+00:00: Heartbeat by coordinator-ar1446.

- 2026-09-25T15:42:04+00:00: Recorded command exit 0; command argv SHA-256
  008f3a8824b64ae468ae900d7bbac2a871a8d29892d84aba5b02a0cc1c0aedff.
