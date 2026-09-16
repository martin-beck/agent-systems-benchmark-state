---
{
  "branch": "feature/ar-1248-strict-replay-cli-contract",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-16T12:34:37+00:00",
  "depends_on": [
    "AR-1231",
    "AR-1232"
  ],
  "id": "AR-1248",
  "next_action": "Define bounded cassette artifact resolution and authenticated CLI SidecarHandoff inputs; add schemas, docs, and fail-closed tests.",
  "observed_branch": "feature/ar-1248-strict-replay-cli-contract",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "asb_ar1232_lifecycle_router",
  "plan": "../plans/AR-1248.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Define the strict-replay CLI consumer contract.",
  "task_revision": 4,
  "title": "Bounded strict-replay CLI consumer contract",
  "updated_at": "2026-09-16T10:34:37+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1248"
}
---

Implement only the linked AR-1248 plan using the ASB development documentation and handoffctl.
Preserve zero-runtime-dependency, offline-after-install, provider-egress denial, and all native,
formal, privacy, signature, DCO, and exact-tree gates.

- 2026-09-16T10:33:49+00:00: Dependencies AR-1231 and AR-1232 are durably done on protected main;
  strict replay CLI consumer gap is concrete and dependency-ready.

- 2026-09-16T10:34:06+00:00: Claimed by asb_ar1232_lifecycle_router.

- 2026-09-16T10:34:37+00:00: Heartbeat by asb_ar1232_lifecycle_router.
