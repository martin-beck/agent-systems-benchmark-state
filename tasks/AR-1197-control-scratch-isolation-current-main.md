---
{
  "branch": "fix/ar0908-current-main",
  "checkpoint_commit": "39f90b316faf4bbbce4170d7f0289c99355c9642",
  "claim_expires": "2026-09-15T09:51:50+00:00",
  "depends_on": [],
  "id": "AR-1197",
  "next_action": "Obtain independent immutable-head review of PR #173; then merge only through protected main after exact-head checks remain green, and verify post-merge assurance at the resulting main SHA.",
  "observed_head": "39f90b316faf4bbbce4170d7f0289c99355c9642",
  "owner": "asb-ar1197-registry",
  "plan": "../plans/AR-1197.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Qualify concurrent ASB control scratch-root isolation on current repaired main.",
  "task_revision": 4,
  "title": "Qualify current-main control scratch isolation",
  "updated_at": "2026-09-15T08:52:28+00:00",
  "worktree_key": "agent-systems-benchmark-control-scratch-isolation-current-main"
}
---

PR #173 hardens the `asb-cli` control scratch-state tests on the repaired ASB main. The scope is
backend test isolation only: it must not add Ratatui, Crossterm, terminal rendering or standalone
asb-tui application code. The observed GitHub state at creation is PR #173 base
`4f855514c5086e1a933ba1e5a4f41db135dbf0a8`, head `39f90b316faf4bbbce4170d7f0289c99355c9642`,
with all 12 required checks terminal green. No merge or release is implied by this record.

- 2026-09-15T08:50:19Z: Live GitHub audit found no prior task record tied to PR #173. It has three
  commits (`e951cbc`, `4977bd8`, `39f90b3`) and changes only `crates/asb-cli/src/control.rs`.
- 2026-09-15T08:50:19Z: PR checks were all green: AWQ shadow, bounded fuzz, emulated aarch64,
  headers, Kani, Loom/state models, mutation sentinels, platform evidence, repository quality,
  retained faults, Rust verification, and TLC/Alloy formal assurance. Independent review is still
  missing; keep the task open until review and protected post-merge evidence exist.

- 2026-09-15T08:51:50+00:00: Claimed by asb-ar1197-registry.

- 2026-09-15T08:52:15+00:00: Recorded command exit 0; command argv SHA-256
  2846b5527043de108f01be7bd57d4ee958dc9192f7af073d0571fc5caa4ed06e.

- 2026-09-15T08:52:28+00:00: Recorded command exit 0; command argv SHA-256
  eaf2472e4b0ec29bac3303a6d46474c99be3c0ab077feca87b1c3650d4745e53.
