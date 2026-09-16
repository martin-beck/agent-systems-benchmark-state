---
{
  "branch": "fix/ar-1247-protected-main-dco-workflow",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-16T12:14:45+00:00",
  "depends_on": [
    "AR-1242"
  ],
  "id": "AR-1247",
  "next_action": "Update verify.yml main-push DCO certification to use protected-main admission and add workflow regression coverage.",
  "observed_branch": "fix/ar-1247-protected-main-dco-workflow",
  "observed_dirty": 2,
  "observed_head": "5a2c1516a0727aba7fd8543599151eaf971d8372",
  "owner": "asb_ar1247_workflow_worker",
  "plan": "../plans/AR-1247.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Route the Rust verification workflow through durable protected-main DCO admission on generated merge commits.",
  "task_revision": 4,
  "title": "Protected-main DCO workflow binding",
  "updated_at": "2026-09-16T10:16:02+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1247"
}
---

Implement only AR-1247 using the ASB development documentation and handoffctl. On protected
main pushes, invoke repository_policy.py in protected-main mode with the immutable push base and
head, preserving strict check_dco.py behavior for pull requests and non-protected contexts. Add
offline regression coverage that prevents workflows from reverting to strict full-range DCO on a
GitHub-generated merge. Do not modify runtime, bundle, or TUI behavior.

- 2026-09-16T10:14:45+00:00: Claimed by asb_ar1247_workflow_worker.

- 2026-09-16T10:16:02+00:00: Recorded command exit 0; command argv SHA-256
  f68e2dbd5fd8c4461e65d40bc39a81c4f45d80e6cfd9637298a192ee2bd4b38c.
