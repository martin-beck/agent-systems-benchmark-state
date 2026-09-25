---
{
  "branch": "feature/ar-1441-first-class-install-bootstrap",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-0821", "AR-0822", "AR-0823"],
  "id": "AR-1441",
  "title": "First-class install and bootstrap",
  "next_action": "Promote after AR-0821, AR-0822 and AR-0823 are done; implement the single clean-install/bootstrap path and disposable install qualification.",
  "owner": "",
  "plan": "../plans/AR-1441.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Provide a verified one-command install and first-run bootstrap for ASB and its optional TUI.",
  "task_revision": 1,
  "updated_at": "2026-09-25T15:40:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1441-first-class-install-bootstrap"
}
---

This is the install gate for the first-class user journey. It must compose the
existing installer, bundle verification, and rollback work; it must not create
a second package registry or bypass signed artifact and credential boundaries.
