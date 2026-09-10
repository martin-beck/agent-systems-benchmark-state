---
{
  "branch": "feature/asb-tui-install-selftest",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-10T18:53:34+00:00",
  "depends_on": [
    "AR-1019"
  ],
  "id": "AR-1020",
  "next_action": "Implement isolated user-space installation, self-test, status, upgrade, remove, and launch commands.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "contracts_20260906",
  "plan": "../plans/AR-1020.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Install and operate asb-tui safely as an optional extension.",
  "task_revision": 3,
  "title": "Add isolated asb-tui install and self-test lifecycle",
  "updated_at": "2026-09-10T15:53:34+00:00",
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

- 2026-09-10T15:53:31+00:00: AR-1019 is complete on public exact main
  990517eda77d4d42ff51ca5d1da03b56e7b8cdda with hosted and trusted local validation; isolated
  install lifecycle may begin.

- 2026-09-10T15:53:34+00:00: Claimed by contracts_20260906.
