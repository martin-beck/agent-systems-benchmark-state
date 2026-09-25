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
  "observed_branch": "feature/ar-1441-first-class-install-bootstrap",
  "observed_dirty": 0,
  "observed_head": "2872a31f2ee90ac5df1a47203b2a618b1829cfec",
  "owner": "coordinator-ar1441",
  "plan": "../plans/AR-1441.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Provide a verified one-command install and first-run bootstrap for ASB CLI/runtime bundles.",
  "task_revision": 8,
  "title": "First-class install and bootstrap",
  "updated_at": "2026-09-25T15:19:06+00:00",
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

- 2026-09-25T15:18:50+00:00: Recorded command exit 0; command argv SHA-256
  38b2da1a2a7a8a2d72e901aedee845bb5a52337aa930fb6c17e0b27c7e0e7606.
