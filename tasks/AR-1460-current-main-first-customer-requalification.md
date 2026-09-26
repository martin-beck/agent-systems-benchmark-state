---
{
  "branch": "qualification/ar-1460-current-main-first-customer-requalification",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-26T19:42:00+00:00",
  "depends_on": [
    "AR-1456",
    "AR-1458"
  ],
  "id": "AR-1460",
  "next_action": "Run the complete ASB-only first-customer production-like qualification against current protected main 36d4bdf35a644a36a8acfdb31078eb7f668a17c4; release only after local/mock campaign, replay, recovery, cleanup, privacy, full gates, and exact-main evidence pass.",
  "owner": "coordinator-ar1460-current-main",
  "plan": "../plans/AR-1460.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Requalify first-customer readiness after the latest local-mock campaign merge.",
  "task_revision": 3,
  "title": "Current-main first-customer requalification",
  "updated_at": "2026-09-26T18:57:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1460-current-main-first-customer-requalification"
}
---

AR-1458 qualified protected main before the later AR-1456 local/mock
multi-agent campaign merge became the current origin/main. This AR repeats the
ASB-only customer-like journey on the exact current main, including explicit
local/mock campaign selection, literature workloads, strict offline replay,
cancellation/restart recovery, cleanup and privacy-safe evidence. It must not
contact a remote provider or modify asb-tui. Any deterministic failure gets a
narrow repair AR; no release claim is made from stale evidence.

- 2026-09-26T18:56:57+00:00: Origin/main advanced to AR-1456 merge 36d4bdf after AR-1458 evidence;
  require fresh first-customer qualification against current main.

- 2026-09-26T18:57:00+00:00: Claimed by coordinator-ar1460-current-main.
