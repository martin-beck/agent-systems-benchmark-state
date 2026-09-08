---
{
  "branch": "feature/tui-settings-wizard",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-08T18:20:28+00:00",
  "depends_on": [
    "AR-0313",
    "AR-0314",
    "AR-0803"
  ],
  "id": "AR-0804",
  "next_action": "Run full locked workspace, docs, repository policy/privacy/Gitleaks and bounded adversarial import/render gates; then exact scope audit and signed candidate if green.",
  "observed_branch": "feature/tui-settings-wizard",
  "observed_dirty": 3,
  "observed_head": "76497db8f22c43762f0b5bcbc7f2549c1d17281d",
  "owner": "quality_20260906",
  "plan": "../plans/AR-0804.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Guide users through agents, providers, workloads, resources, replay, metrics, and output settings.",
  "task_revision": 26,
  "title": "Build the terminal settings wizard",
  "updated_at": "2026-09-08T15:30:35+00:00",
  "worktree_key": "agent-systems-benchmark-tui-settings-wizard"
}
---
## AR-0804

Guide users through agents, providers, workloads, resources, replay, metrics, and output settings.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-08T15:10:03+00:00: Coordinator verified AR-0313, AR-0314, and AR-0803 are durably done;
  promote TUI settings wizard for next safe worker slot.

- 2026-09-08T15:14:52+00:00: Claimed by quality_20260906.

- 2026-09-08T15:15:51+00:00: Recorded command exit 0; command argv SHA-256
  ae8fb19894ace7028ed539e8025f93162b05b3be4e83eed8a3aa7056e24aa5ec.

- 2026-09-08T15:16:36+00:00: Initial exact-main audit at 76497db is complete in clean declared
  worktree. AR-0803 exposes typed negotiate/capabilities/validate_settings/create_plan calls but no
  TUI crate exists. The narrow first slice is a dependency-light pure wizard model: negotiated
  choices only, explicit replay/live source, bounded repetitions/concurrency/budgets/paths,
  backtracking/reset/import/export/dry-run/final review, with launch impossible from wizard state.
  Adding the required standalone executable changes root Cargo.toml and Cargo.lock, so
  implementation is paused at the serialized workspace fence rather than mutating shared manifests
  implicitly.

- 2026-09-08T15:18:01+00:00: Coordinator recovery after repeated no-process/no-worktree checks
  despite explicit Cargo fence authorization; no product mutation observed. Reopen for reassignment.

- 2026-09-08T15:18:04+00:00: Claimed by contracts_20260906.

- 2026-09-08T15:20:05+00:00: Coordinator recovery after repeated no-process/no-checkpoint checks
  despite explicit Cargo-fence authorization; worktree remained clean at 76497db and no product
  mutation occurred.

- 2026-09-08T15:20:28+00:00: Claimed by quality_20260906.

- 2026-09-08T15:21:03+00:00: Recorded command exit 0; command argv SHA-256
  ea21a405d49dac283d4547860028a0ad623c49c6e520573d3c61aef4f0fed2c4.

- 2026-09-08T15:23:08+00:00: Recorded command exit 0; command argv SHA-256
  0d43dcff2c7b06b4164032960b3d5d06ba4881ff7a79f7ecce450dda269469df.

- 2026-09-08T15:23:36+00:00: Recorded command exit 101; command argv SHA-256
  0bdcdff341ca745d16c8424ff217af8df295f460b614e49399c46b4fe1b7bdbe.

- 2026-09-08T15:23:55+00:00: Recorded command exit 0; command argv SHA-256
  32795194b3a73c437a3551367986b26e469e7addaf3efd21f20e93aecdd2f2f7.

- 2026-09-08T15:24:15+00:00: Recorded command exit 0; command argv SHA-256
  26f655f2e0d5a89504c1b0c40046eb5bc9496af2cbbd93070e8399f3a79aa684.

- 2026-09-08T15:24:43+00:00: Authorized Cargo fence implementation checkpoint on exact base 76497db:
  dirty scope is root Cargo.toml/Cargo.lock plus new
  crates/asb-tui/{Cargo.toml,README.md,src/lib.rs,src/main.rs}. The standalone crate has a pure
  capability-driven wizard model; only runner-advertised
  agents/providers/workloads/platforms/metrics/recordings are accepted, live/replay is explicit,
  credential values are unrepresentable, JSON import is closed/bounded, back/reset are lossless,
  dry-run maps only to ValidateSettings, and exact confirmation maps only to CreatePlan (no Launch
  API). Initial test failed only for missing binary crate docs and was fixed. Final focused
  evidence: fmt check green, 3/3 model tests green, clippy all-targets -D warnings green. Cargo.lock
  changed only by registering local asb-tui dependencies already pinned in the workspace.

- 2026-09-08T15:26:04+00:00: Recorded command exit 1; command argv SHA-256
  c5cd10474a470e32ba5355df34efc4f3cff6f507dc26d675b51556f6cf3b693f.

- 2026-09-08T15:27:18+00:00: Recorded command exit 0; command argv SHA-256
  16c7c9b07df8bd511b3f939074c400bbb604eb2e8f2793c0fae1351f3c8ac8a8.

- 2026-09-08T15:27:57+00:00: Recorded command exit 0; command argv SHA-256
  70b93aaeec894f4ddf4f7f2a532bc0857e840c9e2d04fa179750e1cb913de146.

- 2026-09-08T15:28:23+00:00: Second AR-0804 checkpoint on exact base 76497db: capability-driven
  model now includes deterministic seven-step keyboard navigation, help toggle, bounded ASCII
  selector search, width-bounded plain accessibility rendering, lossless back/reset/import, and
  stable text snapshot coverage. Rendered source reports only live/matching-replay classification
  and never emits cassette or credential digests. Launch remains unrepresentable; only
  ValidateSettings and explicitly confirmed CreatePlan can be produced. Focused cargo test is 4/4
  green, fmt check, package all-target clippy -D warnings, and diff-check are green. Dirty scope
  remains root Cargo.toml/Cargo.lock plus four new asb-tui paths.

- 2026-09-08T15:29:15+00:00: Recorded command exit 1; command argv SHA-256
  acbdc32aa8aa3efea70b6c6093703e69060ddf467c3ebe57f497b1009e71c8ca.

- 2026-09-08T15:29:55+00:00: Recorded command exit 0; command argv SHA-256
  cd243d3420b4c213a7011a573ecd50a68e91cb6d5d446a32ed4d2536023d1758.

- 2026-09-08T15:30:16+00:00: Recorded command exit 1; command argv SHA-256
  664c798b9ba0ef8fcd9cc079f71003ec0764338bdf1ff69942615d3bc912af25.

- 2026-09-08T15:30:35+00:00: Recorded command exit 0; command argv SHA-256
  f625a0bcbf9759fd51e3662845f1cdc0270bf53df57a22c946bbe99b7ed4ddca.
