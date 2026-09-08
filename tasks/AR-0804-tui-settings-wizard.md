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
  "next_action": "Monitor exact-main d51ee9c postmerge runs: Rust 34246605181, quality 34246605294, emulated-aarch64 34246605130, fault 34246605182, formal 34246605248. After all terminal success, run focused local verification and state doctor, then release with unsupported launch/transport/full-screen limits.",
  "observed_branch": "feature/tui-settings-wizard",
  "observed_dirty": 0,
  "observed_head": "8f7152c525daf0b8dd61961c780848ed7a8bf979",
  "owner": "quality_20260906",
  "plan": "../plans/AR-0804.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Guide users through agents, providers, workloads, resources, replay, metrics, and output settings.",
  "task_revision": 40,
  "title": "Build the terminal settings wizard",
  "updated_at": "2026-09-08T15:50:02+00:00",
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

- 2026-09-08T15:31:41+00:00: Recorded command exit 0; command argv SHA-256
  b4c6daa5728e14ec18a7baef847d931b25531c05065f1a362fc42b823364f8ff.

- 2026-09-08T15:32:12+00:00: Recorded command exit 2; command argv SHA-256
  96cd55f3832ee5842e4ad6fe82d4093abfb5e9c316b3c0d201d40c415ee78b4f.

- 2026-09-08T15:33:06+00:00: Recorded command exit 1; command argv SHA-256
  ff0dfafab5239f5ed76d39567223d165af0d72e3d9615eb3ef2b62454360b2af.

- 2026-09-08T15:34:05+00:00: Recorded command exit 0; command argv SHA-256
  241f42d88ed742f578ed3699a64a9cc73322de1ceef1ea5e53a6cd66c03ad445.

- 2026-09-08T15:34:44+00:00: Recorded command exit 0; command argv SHA-256
  9440b74a46ba9bee53c205c77d0a1133b996a026a9cb5fd6523225dc89a6438d.

- 2026-09-08T15:35:03+00:00: Recorded command exit 0; command argv SHA-256
  2f8cebe472ac67a0af5137a62505a2e6f1f54a143c3ccc85a46818d9e0a98713.

- 2026-09-08T15:35:24+00:00: Recorded command exit 0; command argv SHA-256
  95a72bbf54c7eef99805c0d1cd5e042012d042fed6dbe73fa74b3ac05f852eaf.

- 2026-09-08T15:35:58+00:00: Signed+DCO clean candidate 8f7152c525daf0b8dd61961c780848ed7a8bf979,
  tree 0a17f5e127b2c1766a24ea927b5a4d4b15e13111, exact parent 76497db, six-path scope (root
  Cargo.toml/Cargo.lock plus new asb-tui Cargo.toml/README/lib/main). Full locked workspace tests,
  workspace all-target clippy -D warnings, rustdoc -D warnings, release build, fmt and diff-check
  passed. Focused adversarial suite 5/5 passed: closed/oversize import, unadvertised/stale replay,
  duplicate metrics/catalog, non-ASCII/oversize search, snapshot digest non-emission,
  navigation/back/reset, validation/create separation. Repository policy, failure-path suite,
  contract consistency 4/4, cargo-deny and targeted Gitleaks for every changed path are green;
  added-line privacy scan found no credential-value patterns. Whole-tree Gitleaks exit 1 was
  classified as unrelated historical/build scope after changed-path scans passed. Earlier exits were
  formatting-only and missing required --bin-dir harness argument, both corrected. No Launch API
  exists; terminal rendering/transport/run control remain unsupported follow-ups.

- 2026-09-08T15:37:00+00:00: Recorded command exit 0; command argv SHA-256
  d54772afd62a043b148785c21fb86184849454ead8c62a8eb09c4c33c0a41a69.

- 2026-09-08T15:37:36+00:00: Published independently approved six-path candidate as PR #83 with
  exact head 8f7152c525daf0b8dd61961c780848ed7a8bf979 and base
  76497db8f22c43762f0b5bcbc7f2549c1d17281d. GitHub reports OPEN/MERGEABLE; AWQ run 34245893935
  already succeeded and all five required workflows are active. Preserve limitations: no Launch API,
  transport wiring, or full-screen terminal rendering claim.

- 2026-09-08T15:43:37+00:00: Recorded command exit 0; command argv SHA-256
  52e3c6c6ea3012e5b61ab57a813a60c9a3d653a9abefbdabbdd1504b2162e67b.

- 2026-09-08T15:44:26+00:00: Authorized signed+DCO no-ff merge completed as
  d51ee9c9ab8889f6b9837a89772f59ea6f37d3a3 with parents exact 76497db and reviewed 8f7152c.
  Signature/show-check pass; push used exact main force-with-lease. PR #83 reports MERGED and local
  main/origin/main are clean and equal d51ee9c. Fresh five-workflow exact-main matrix is active;
  hold release.

- 2026-09-08T15:50:02+00:00: Recorded command exit 0; command argv SHA-256
  75704dee64f1e4c9098c5869decdade51510717f4bc51af7cc5446c20dd3f9cb.
