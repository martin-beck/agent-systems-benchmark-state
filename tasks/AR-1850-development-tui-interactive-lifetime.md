---
{
  "branch": "feature/ar1850-development-tui-interactive-lifetime",
  "checkpoint_commit": "2b42c8c1d24495d1155484b0b3d76bd7f7d0c11d",
  "claim_expires": "2026-10-13T16:00:53+00:00",
  "depends_on": [],
  "id": "AR-1850",
  "next_action": "Obtain independent exact-head review, publish reviewed PR, and run required CI.",
  "observed_branch": "feature/ar1850-development-tui-interactive-lifetime",
  "observed_dirty": 0,
  "observed_head": "671f898b6a859655952a009b9a4468e685d74013",
  "owner": "ar1850-development-tui-lifetime-luna",
  "plan": "../plans/AR-1850-development-tui-interactive-lifetime.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_ref": "specs/AR-1850.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Stop the development ASB launcher from killing a successfully admitted interactive TUI after its fixed 15-second lifetime deadline.",
  "task_revision": 9,
  "title": "Repair development ASB TUI interactive lifetime",
  "updated_at": "2026-10-13T14:06:18+00:00",
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

- 2026-10-13T14:02:40+00:00: Product checkpoint 671f898b6a859655952a009b9a4468e685d74013
  (SSH-signed, DCO): removed post-admission 15s child deadline; retained bounded admission and
  cleanup; extended pinned PTY qualification idle assertion to 16s. cargo fmt --all -- --check and
  focused spawn/early-exit cleanup tests pass; cross-repo PTY test compiles with --no-run.

- 2026-10-13T14:03:18+00:00: Full cargo test -p asb-cli --no-fail-fast passes: 459 unit tests plus
  all package integration/doc tests, 0 failed. cargo fmt check remains green; product HEAD remains
  signed 671f898b6a859655952a009b9a4468e685d74013.

- 2026-10-13T14:05:05+00:00: Recorded command exit 0; command argv SHA-256
  6023d9dd2abd13ac06f5483e5e87a5dc322906b2df5745d38e5a6c5e9515aff2.

- 2026-10-13T14:06:18+00:00: Recorded command exit 0; command argv SHA-256
  63d9c7861e91dbbf674cb4e284f9b9aa7e1751619bc89d3a42579ccd9be12ea3.
