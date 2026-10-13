---
{
  "branch": "feature/ar1850-development-tui-interactive-lifetime",
  "checkpoint_commit": "2b42c8c1d24495d1155484b0b3d76bd7f7d0c11d",
  "claim_expires": "2026-10-13T16:00:53+00:00",
  "depends_on": [],
  "id": "AR-1850",
  "next_action": "Promote, claim an isolated current-main worktree, reproduce the development `asb tui` PTY lifetime failure, and repair the launcher without weakening broker admission or cleanup.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "ar1850-development-tui-lifetime-luna",
  "plan": "../plans/AR-1850-development-tui-interactive-lifetime.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_ref": "specs/AR-1850.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Stop the development ASB launcher from killing a successfully admitted interactive TUI after its fixed 15-second lifetime deadline.",
  "task_revision": 4,
  "title": "Repair development ASB TUI interactive lifetime",
  "updated_at": "2026-10-13T14:02:32+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1850-development-tui-interactive-lifetime"
}
---

Current ASB main starts the development broker and TUI, completes both broker
handshakes, and then applies an unconditional 15-second child deadline in
`launch_development_broker_with_backend`. The normal interactive child is
killed and the user receives `ASB could not complete the terminal interface
launch`. That deadline may bound admission only, never a healthy operator
session.

This is an ASB launcher repair. It must preserve private process-group cleanup,
bounded handshake failure handling, terminal restoration, and the existing
PTY/inherited-fd contract. It must not alter asb-tui rendering or weaken the
cross-repository qualification.

- 2026-10-13T12:08:38+00:00: P0 user-reported development TUI launcher lifetime repair is
  dependency-ready.

- 2026-10-13T14:00:53+00:00: Claimed by ar1850-development-tui-lifetime-luna.

- 2026-10-13T14:02:32+00:00: Checkpointed source commit 2b42c8c1d24495d1155484b0b3d76bd7f7d0c11d.
