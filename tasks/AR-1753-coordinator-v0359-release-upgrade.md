---
{
  "branch": "upgrade/ar-1753-coordinator-v0.3.59",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1749"
  ],
  "id": "AR-1753",
  "next_action": "Promote and claim; sync the exact v0.3.59 release into an isolated state worktree, repair only downstream-owned compatibility regressions, and run the complete integrity matrix before independent review.",
  "owner": "",
  "plan": "../plans/AR-1753-coordinator-v0359-release-upgrade.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_ref": "specs/AR-1753.json",
  "spec_revision": 1,
  "status": "open",
  "summary": "Adopt the exact Agent Workflow Coordinator v0.3.59 release in ASB state and repair every downstream-owned integrity regression exposed by the upgrade.",
  "task_revision": 2,
  "title": "Coordinator v0.3.59 release upgrade and integrity repair",
  "updated_at": "2026-10-09T06:25:37+00:00",
  "worktree_key": "agent-systems-benchmark-state-ar-1753-coordinator-v0359"
}
---

Upgrade the ASB coordination repository from its current development-class
Coordinator v0.3.57 snapshot to the exact latest release, v0.3.59. Use the
official complete release vendor mechanism from a clean checkout at the exact
tag. Do not patch vendored bytes or misclassify a development snapshot as a
release.

Repair every repository-owned compatibility, fixture, schema, coverage, formal,
or generated-view regression revealed by the update without weakening existing
privacy, integrity, lifecycle, locking, coverage, or development semantics.
Preserve unrelated product and state work.

- 2026-10-09T06:25:37+00:00: AR-1749 is done; exact v0.3.59 release identity and upgrade scope
  verified.
