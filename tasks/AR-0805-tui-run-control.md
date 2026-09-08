---
{
  "branch": "feature/tui-run-control",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-08T19:22:57+00:00",
  "depends_on": [
    "AR-0104",
    "AR-0204",
    "AR-0803",
    "AR-0804"
  ],
  "id": "AR-0805",
  "next_action": "Request independent review of the exact one-file lifecycle slice before any signed checkpoint. Keep AR in progress: scheduler capacity, deadlines, leases, provider source, metrics, warnings, evidence availability, terminal resize, and native frontend resource/separation evidence require an owned follow-up boundary and are not claimed. Preserve AR-0855 header lines on any rebase.",
  "observed_branch": "feature/tui-run-control",
  "observed_dirty": 0,
  "observed_head": "f9d4afe9902367fe0c09a517b210e8ce33f21d0e",
  "owner": "quality_20260906",
  "plan": "../plans/AR-0805.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Start validated runs and monitor current progress, health, metrics, failures, and cancellation from the TUI.",
  "task_revision": 40,
  "title": "Add terminal run control and status",
  "updated_at": "2026-09-08T17:06:26+00:00",
  "worktree_key": "agent-systems-benchmark-tui-run-control"
}
---
## AR-0805

Start validated runs and monitor current progress, health, metrics, failures, and cancellation from the TUI.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-08T16:22:44+00:00: Fresh post-AR-0315 audit: AR-0805 is the highest-priority
  dependency-ready unclaimed task after AR-0319 was concurrently claimed by replay_20260906.
  Dependencies AR-0104, AR-0204, AR-0803, and AR-0804 are all durably done. Promote for
  quality_20260906; product mutation must wait for or rebase after active broad AR-0855
  source-header fence, which overlaps asb-tui source.

- 2026-09-08T16:22:57+00:00: Claimed by quality_20260906.

- 2026-09-08T16:23:19+00:00: Recorded command exit 129; command argv SHA-256
  6fbe289a70903596c35c58cb3776d1e022f9eaa51e506a69b65d3c420dd6437b.

- 2026-09-08T16:23:47+00:00: Initial worktree-create command exit 129 is operator-only: an
  unintended trailing argument made git worktree add receive too many positional arguments and print
  usage. No branch or worktree was created and no product path changed. Corrective action is a
  single exact retry after durable classification.

- 2026-09-08T16:24:03+00:00: Recorded command exit 0; command argv SHA-256
  5b93a7b16ff13cbd2e349403c14ce7e7a9174946197bcdaa139476839f7c4300.

- 2026-09-08T16:24:28+00:00: Post-release handoff complete. AR-0319 became unavailable in a
  concurrent signed claim by replay_20260906, so the next highest-priority dependency-ready task
  selected was AR-0805. Promotion 95b587e4 and claim d448ae77 are durable. Declared worktree
  /srv/data/projects/agent-systems-benchmark-tui-run-control now exists on branch
  feature/tui-run-control, clean at exact product main b2707c482876dcfb42c756c39165f6ecdb5c7c10.
  Active AR-0855 candidate touches crates/asb-tui/src/lib.rs and main.rs, so shared path mutation is
  fenced pending its integration/release.

- 2026-09-08T16:38:01+00:00: Recorded command exit 2; command argv SHA-256
  48458d4adcbc2714c4ae60f17ec39d916357031118af6e75d9a5cd826c73f20e.

- 2026-09-08T16:39:14+00:00: Recorded command exit 0; command argv SHA-256
  5bf0b7b04c83b7df7bc62cba06fa5d9838d810e3d53661feba9eac720a1a515b.

- 2026-09-08T16:39:46+00:00: Recorded command exit 101; command argv SHA-256
  3caed8f2c97a1dd7146849884c2a7da81c53b7be4c84dbc3db9ff3ed69a58e3f.

- 2026-09-08T16:40:12+00:00: First AR-0805 focused compile failed before tests with two local import
  defects introduced by the new run-control slice: MutationParams was accidentally removed although
  the existing wizard still uses it; AttemptId and RunId are test-only and therefore unused in the
  non-test library build. This is a source compile failure, not environment or harness. Corrective
  scope is import-only: restore MutationParams at module scope and move AttemptId/RunId into the
  test module.

- 2026-09-08T16:40:32+00:00: Recorded command exit 0; command argv SHA-256
  61c42c9a70f10e57aabc5a3c2e240492450fbc505076e7f32298ad23f46936a0.

- 2026-09-08T16:40:52+00:00: Recorded command exit 0; command argv SHA-256
  3caed8f2c97a1dd7146849884c2a7da81c53b7be4c84dbc3db9ff3ed69a58e3f.

- 2026-09-08T16:41:22+00:00: AR-0805 first implementation slice is working on exact base
  b2707c482876dcfb42c756c39165f6ecdb5c7c10 with one dirty path, crates/asb-tui/src/lib.rs (367
  insertions, 1 deletion). Added explicit-confirmation at-most-once launch, durable run/attempt
  identity binding, bounded reconnect calls, non-regressing status, contiguous exact-run event
  projection, causally fenced cancellation, and acknowledgement-vs-terminal separation. Focused
  cargo test --locked -p asb-tui passes 8/8; focused all-target clippy -D warnings, fmt, and
  diff-check pass. The prior exit 101 was repaired by restoring MutationParams and moving test-only
  IDs under cfg(test). AR-0855 is now blocked/unowned, so its active path fence is returned; future
  rebase must preserve the required header delta.

- 2026-09-08T16:42:45+00:00: Recorded command exit 1; command argv SHA-256
  27dfaf8283c89553da77b2f951150438d336134c52a62106346d10292ccdaf06.

- 2026-09-08T16:43:23+00:00: The next-slice apply_patch exited 1 because its expected pre-format
  context did not match rustfmt-expanded accept_events lines. This is a patch-harness/context
  failure; apply_patch made no product changes. Current one-file implementation and all prior 8/8
  focused evidence remain preserved. Exact current context was inspected before the corrected patch.

- 2026-09-08T16:44:14+00:00: Recorded command exit 0; command argv SHA-256
  d556ef5b8c968bfcd3cb1a95ec29fe648ab625fccc3a266d7d670a6b7e2da9ee.

- 2026-09-08T16:44:36+00:00: Recorded command exit 0; command argv SHA-256
  3caed8f2c97a1dd7146849884c2a7da81c53b7be4c84dbc3db9ff3ed69a58e3f.

- 2026-09-08T16:45:11+00:00: Recorded command exit 0; command argv SHA-256
  2bb73eb49d3816608c7376e2904614ddd53ad9502c636054d600744f860c0dfe.

- 2026-09-08T16:45:23+00:00: Recorded command exit 0; command argv SHA-256
  b919e5874d6da6a93161371f9ff174e571194bf786441952a004667a1ed99166.

- 2026-09-08T16:46:10+00:00: Completed the requested bounded AR-0805 slice in
  crates/asb-tui/src/lib.rs only (486 insertions, 1 deletion) on base
  b2707c482876dcfb42c756c39165f6ecdb5c7ló? Wait must no typo hash. Need exact. Stop call due
  generated weird? We must ensure note no typo. Redo safely shorter.

- 2026-09-08T16:46:33+00:00: Correction to the immediately preceding malformed operator note: exact
  base is b2707c482876dcfb42c756c39165f6ecdb5c7c10. The one-file asb-tui slice now covers bounded
  page cardinality, contiguous cursors, restart reconstruction without relaunch, terminal
  event/status convergence, duplicate launch/cancel rejection, stale and cross-attempt rejection,
  and cancellation acknowledgement races. Focused asb-tui tests pass 10/10; focused clippy with
  warnings denied, fmt, and diff-check pass. No protocol/schema paths changed.

- 2026-09-08T16:47:53+00:00: Recorded command exit 0; command argv SHA-256
  00383a816118bc9ee1eaf4852084f6dd208ae4811e4898c4bb2f4b1beb707bc3.

- 2026-09-08T16:50:19+00:00: Exact-tree core gate batch completed successfully on base
  b2707c482876dcfb42c756c39165f6ecdb5c7c10 with only crates/asb-tui/src/lib.rs dirty: cargo fmt
  --all -- --check, cargo clippy --locked --workspace --all-targets -- -D warnings, cargo test
  --locked --workspace, RUSTDOCFLAGS=-D warnings cargo doc --locked --workspace --no-deps, cargo
  build --locked --workspace --release, and git diff --check all exited 0. Focused asb-tui remains
  10/10 green. The bounded lifecycle slice proves page cardinality, contiguous cursor progression,
  reconnect without relaunch, terminal convergence, and cancellation races. Dashboard
  capacity/deadline/lease/provider/metrics/warnings/evidence fields remain unavailable from current
  public control protocol and are not claimed.

- 2026-09-08T16:52:06+00:00: Recorded command exit 0; command argv SHA-256
  8233b5d077fac82e2fd2ca3407d7e4bb326b3f10cd5f19f621534f672eab5bc5.

- 2026-09-08T16:52:43+00:00: Recorded command exit 0; command argv SHA-256
  3bd2246f55e55e32e8e68a51f689e76a0807a3f4f210f8e80f45c01f4c297a11.

- 2026-09-08T16:53:48+00:00: Recorded command exit 0; command argv SHA-256
  2fb716cc8bbfaf4528274187a0b12bafbc503a1be56806029142a618135cb11f.

- 2026-09-08T16:55:32+00:00: Recorded command exit 1; command argv SHA-256
  4fe5e6df52eee69f9abda47b6896be6dcde0d41f363cfac5b974b99168d876d4.

- 2026-09-08T16:56:10+00:00: Recorded command exit 0; command argv SHA-256
  58fdc62df80c18b89ef97b1f3c1a4ae47d0a10315b29ceb8cfd94c5b7a4ddeb4.

- 2026-09-08T16:56:37+00:00: Recorded command exit 101; command argv SHA-256
  0bae271a114ea2af73b478100724a29660bbea86c35e03cf2f1c955c0a3e3579.

- 2026-09-08T16:56:54+00:00: Recorded command exit 0; command argv SHA-256
  e63761b08022247dabe796c9854834d37b2c22b2d2703c9669470dce50d08c35.

- 2026-09-08T16:57:05+00:00: Recorded command exit 0; command argv SHA-256
  0bae271a114ea2af73b478100724a29660bbea86c35e03cf2f1c955c0a3e3579.

- 2026-09-08T16:57:45+00:00: Recorded command exit 0; command argv SHA-256
  f608fda4edb1fbecd1e1ac5da1ffb864d0ff510016bb125baa79d98906929372.

- 2026-09-08T16:58:22+00:00: AR-0805 bounded lifecycle slice is ready for review as one dirty path,
  crates/asb-tui/src/lib.rs (551 insertions, 1 deletion), exact base
  b2707c482876dcfb42c756c39165f6ecdb5c7c10. A final adversarial audit found and repaired
  status-state regression and reconciliation handling: higher-revision lifecycle regressions now
  fail closed; needs_reconciliation is displayed as a non-cancellable authoritative terminal
  projection. The first focused rerun exposed a source compile defect because PartialEq is not
  const-callable; removing only the unnecessary const qualifier repaired it. Final focused test is
  11/11 green, focused clippy/fmt/diff clean. Exact post-repair workspace fmt, all-target clippy -D
  warnings, workspace tests, rustdoc -D warnings, contract consistency and tests, coverage floors,
  failure fixtures, artifact outcome, platform manifests plus 23 tests, actionlint, zizmor, cargo
  deny, cargo audit, Gitleaks file scan, added-line privacy scan, and one-path scope/diff checks all
  pass. No schema, control protocol, Cargo, main.rs, or AR-0855 header path changed.

- 2026-09-08T17:05:45+00:00: Recorded command exit 0; command argv SHA-256
  321c534968b9c456a64caf5e6d09b63780c507f97548057d2bfe31edcfd73ff4.

- 2026-09-08T17:06:14+00:00: Recorded command exit 0; command argv SHA-256
  9fe06d548cfdfaf5d66d30ca41930792632412646ce581ac20bf2dc81083328c.

- 2026-09-08T17:06:26+00:00: Recorded command exit 0; command argv SHA-256
  7de8d3ab9059b7ab7bb3812306a48029a239687bf3dd0e9e446a3d1527ec28bf.
