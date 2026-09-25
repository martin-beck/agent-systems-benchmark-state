---
{
  "branch": "feature/ar-1441-first-class-install-bootstrap",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-25T17:17:30+00:00",
  "depends_on": [
    "AR-0821",
    "AR-0822"
  ],
  "id": "AR-1441",
  "next_action": "Promote and claim against the completed ASB install/lifecycle primitives AR-0821 and AR-0822; implement and qualify the ASB CLI/runtime-bundle clean-install/bootstrap path. Preserve AR-0823 as the separate cross-repository/UI audit.",
  "observed_branch": "main",
  "observed_dirty": 7,
  "observed_head": "bd7d10d4a760a84fa42de2b1fa9e97e8ea85ba09",
  "owner": "coordinator-ar1441",
  "plan": "../plans/AR-1441.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Provide a verified one-command install and first-run bootstrap for ASB CLI/runtime bundles.",
  "task_revision": 6,
  "title": "First-class install and bootstrap",
  "updated_at": "2026-09-25T15:18:09+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1441"
}
---

This is the install gate for the first-class user journey. It must compose the
existing installer, bundle verification, and rollback work; it must not create
a second package registry or bypass signed artifact and credential boundaries.

- 2026-09-25T15:17:21+00:00: Coordinator-approved ASB-only dependency transition: AR-0821 and
  AR-0822 provide completed install/lifecycle primitives. Remove AR-0823 UI/cross-repository audit
  from this CLI/runtime-bundle gate; preserve AR-0823 independently.

- 2026-09-25T15:17:30+00:00: Claimed by coordinator-ar1441.

- 2026-09-25T15:17:56+00:00: Recorded command exit 0; command argv SHA-256
  4637d84ec00d072c019f8a3f5692356eac8f8f82c4e0ce09fe38d36e5298ed4c.
