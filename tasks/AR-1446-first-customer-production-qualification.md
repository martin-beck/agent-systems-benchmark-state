---
{
  "branch": "qualification/ar-1446-first-customer-production",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1433",
    "AR-1441",
    "AR-1442",
    "AR-1443"
  ],
  "id": "AR-1446",
  "next_action": "Done: ASB-only first-customer production-like qualification verified on protected merge 2872a31f2ee90ac5df1a47203b2a618b1829cfec. Disposable bootstrap passed; CLI, runtime, and workspace-library gates passed, including literature/local-mock coverage. No live-provider or asb-tui dependency was required; AR-0903 and AR-1336 remain separate.",
  "observed_branch": "qualification/ar-1446-first-customer-production",
  "observed_dirty": 0,
  "observed_head": "2872a31f2ee90ac5df1a47203b2a618b1829cfec",
  "owner": "",
  "plan": "../plans/AR-1446.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "done",
  "summary": "Qualify ASB in a disposable first-customer production-like environment.",
  "task_revision": 13,
  "title": "First-customer production qualification",
  "updated_at": "2026-09-25T15:43:44+00:00",
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

- 2026-09-25T15:42:43+00:00: Recorded command exit 0; command argv SHA-256
  b945362378f77f64a68eb9e8d400e693e008357f0cc0d69f7bfe3bb93e47ae02.

- 2026-09-25T15:43:16+00:00: Recorded command exit 0; command argv SHA-256
  58ad9b03710727e55f9300c6ae75874f499c788bfe1a1c8715b5d87cd762e594.

- 2026-09-25T15:43:44+00:00: ASB-only first-customer production-like qualification complete on
  protected merge 2872a31f2ee90ac5df1a47203b2a618b1829cfec. Disposable bootstrap/lifecycle test
  passed; cargo test --locked -p asb-cli --tests passed 107 unit + 12 capability + 3 CLI E2E + 5
  guide + 2 setup + 4 lifecycle + 3 transcript; cargo test --locked -p asb-runtime --lib passed 127
  with 1 capability-gated ignore; cargo test --locked --workspace --lib passed all workspace library
  suites including 35 workload/literature tests. A transient no-space build failure was recorded,
  explicit stale target caches were cleaned, and the exact gate reran green. No credentials or
  live-provider reachability were required.
