---
{
  "branch": "fix/ar0908-current-main",
  "checkpoint_commit": "39f90b316faf4bbbce4170d7f0289c99355c9642",
  "claim_expires": "2026-09-15T12:09:19+00:00",
  "depends_on": [],
  "id": "AR-1197",
  "next_action": "Obtain independent immutable-head review of PR #173; then merge only through protected main after exact-head checks remain green, and verify post-merge assurance at the resulting main SHA.",
  "observed_head": "39f90b316faf4bbbce4170d7f0289c99355c9642",
  "owner": "root-pr173-rebase",
  "plan": "../plans/AR-1197.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Qualify concurrent ASB control scratch-root isolation on current repaired main.",
  "task_revision": 9,
  "title": "Qualify current-main control scratch isolation",
  "updated_at": "2026-09-15T10:17:12+00:00",
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

- 2026-09-15T08:52:51+00:00: Recorded command exit 0; command argv SHA-256
  eaf2472e4b0ec29bac3303a6d46474c99be3c0ab077feca87b1c3650d4745e53.

- 2026-09-15T09:55:32+00:00: Recovered expired claim formerly owned by asb-ar1197-registry.
  Recovered expired claim before publishing the new tutorial AR series; no product implementation
  change was made.

- 2026-09-15T10:09:19+00:00: Claimed by root-pr173-rebase.

- 2026-09-15T10:09:21+00:00: Current-main rebase audit completed in isolated worktree outside the
  repository: origin/main ef82484fa78dd31c0d7b5ad48e2dc51a93ec1339 rebased PR #173 topic to
  temporary head 75785c151fc193c2c79f629c6addcebe0a5c14af; ASB_TEST_ROOT=/tmp cargo test -p asb-cli
  --lib --locked passed and git diff --check passed. Prior failure was only because the temporary
  worktree lived under /tmp, making the default scratch root overlap the repository. Do not merge
  the old remote head; guarded force-with-lease update and fresh exact-head CI/independent review
  remain required.

- 2026-09-15T10:17:12+00:00: Guarded force-with-lease updated PR #173 from
  39f90b316faf4bbbce4170d7f0289c99355c9642 to current-main rebased head
  81a81cfdb913a273fa2c4b9785f5515787e1a524. Independent review confirmed three signed/DCO commits,
  no conflicts, focused tests 20/20 serial and 20/20 with 8 threads, fmt/clippy/diff checks pass.
  Fresh GitHub checks are running on exact head; do not merge until all terminal and green.
