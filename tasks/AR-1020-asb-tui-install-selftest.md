---
{
  "branch": "feature/asb-tui-install-selftest",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1019"],
  "id": "AR-1020",
  "next_action": "Implement isolated user-space installation, self-test, status, upgrade, remove, and launch commands.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1020.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "planned",
  "summary": "Install and operate asb-tui safely as an optional extension.",
  "task_revision": 1,
  "title": "Add isolated asb-tui install and self-test lifecycle",
  "updated_at": "2026-09-10T00:00:00+00:00",
  "worktree_key": "agent-systems-benchmark-asb-tui-install-selftest"
}
---
Provide `asb tui install`, `asb tui`, `asb tui status`, `asb tui upgrade`, and `asb tui remove`. Install
only into an isolated user directory, never overwrite ASB core files, run a protocol/terminal self-test
before launch, validate the locked coordinator and workflow-quality release versions, and show the
extension's verified/unverified boundary and exact versions. Preserve the
main benchmark process when the TUI disconnects or is removed.

Acceptance criteria: fresh install/upgrade/remove/reconnect tests, interrupted-install recovery,
read-only status, detached-run continuity, permissions/privacy checks, and clear actionable errors.
