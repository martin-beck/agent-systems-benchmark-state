---
{
  "branch": "feature/ar1850-development-tui-interactive-lifetime",
  "checkpoint_commit": "2b42c8c1d24495d1155484b0b3d76bd7f7d0c11d",
  "claim_expires": "2026-10-13T16:00:53+00:00",
  "depends_on": [],
  "id": "AR-1850",
  "next_action": "Rerun only failed Policy/coverage workflow 38410495133 through handoffctl; keep PR unmerged until rerun, pending emulated-aarch64, and all required checks are terminal green.",
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
  "task_revision": 18,
  "title": "Repair development ASB TUI interactive lifetime",
  "updated_at": "2026-10-13T14:19:46+00:00",
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

- 2026-10-13T14:06:45+00:00: Published PR #631
  https://github.com/martin-beck/agent-systems-benchmark/pull/631 from exact signed product head
  671f898b6a859655952a009b9a4468e685d74013 against current main. Push and PR creation completed
  through handoffctl run; state reconciled.

- 2026-10-13T14:08:47+00:00: Independent exact-head review approved PR #631 at
  671f898b6a859655952a009b9a4468e685d74013 with no findings; focused 5/5 passed and
  cleanup/admission/PTY contracts preserved. Hosted checks remain in progress; merge stays gated.

- 2026-10-13T14:09:36+00:00: Recorded command exit 0; command argv SHA-256
  138d2c1840ff852c43dd72d516eb85dd14b58e25b0417148f52fa00fcc8ceff4.

- 2026-10-13T14:09:53+00:00: PR #631 initial credential-free run 38410493915 failed only in
  unrelated concurrent source_checkout fixtures: acquisition collision returned Unavailable and
  poisoned exact-fixture lock; 457 passed/2 failed. Exact TUI inherited-fd/PTY check passed (run
  38410494755). Reran failed workflow unchanged; rerun job is 115342870094.

- 2026-10-13T14:11:47+00:00: Recorded command exit 0; command argv SHA-256
  7d12739e865d55632d6cb72a839447b58e350416d790072224ab5786826269fb.

- 2026-10-13T14:12:03+00:00: Emulated aarch64 run 38410493750 failed in unrelated
  goose::tests::diagnostic_and_symlink_fail_closed: 220 passed, 1 failed; expected unwrap_err but
  received typed failed outcome exit 127. No AR-1850/TUI path involved. Reran unchanged portability
  workflow; rerun is active.

- 2026-10-13T14:12:21+00:00: Required checks now show unrelated repeated failures: credential-free
  initial run 38410493915 had source_checkout collision/poison failures; policy/coverage 38410495133
  independently failed exact_fixture_checkout_is_returned_and_cleanup_is_explicit (458 passed, 1
  failed, Unavailable); emulated aarch64 38410493750 failed unrelated goose
  diagnostic_and_symlink_fail_closed (220 passed, 1 failed). Exact TUI PTY run 38410494755 passed
  and independent review approved. Do not alter AR-1850 product scope or merge; focused repair ARs
  are required for repeated non-TUI failures.

- 2026-10-13T14:13:19+00:00: Coordinator confirms Policy/coverage failure is reproducible on
  source_checkout exact_fixture Unavailable; focused AR-1856 repair worker is investigating.
  Credential-free rerun 115342870094 passes; Exact TUI PTY 38410494755 passes; PR #631 remains
  unmerged.

- 2026-10-13T14:19:46+00:00: AR-1856 diagnostic reconciled: no deterministic product defect found.
  Exact source_checkout fixture passed under 24-way concurrency, full suite, and local llvm-cov;
  hosted failure was transient Unavailable under RUST_TEST_THREADS=1. PR #631 exact head remains
  671f898b6a859655952a009b9a4468e685d74013.
