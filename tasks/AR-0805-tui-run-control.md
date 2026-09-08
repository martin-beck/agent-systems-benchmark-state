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
  "next_action": "Apply the same bounded reconnect/page/cancellation extension using smaller exact post-fmt context hunks, then rerun focused tests.",
  "observed_branch": "feature/tui-run-control",
  "observed_dirty": 1,
  "observed_head": "b2707c482876dcfb42c756c39165f6ecdb5c7c10",
  "owner": "quality_20260906",
  "plan": "../plans/AR-0805.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Start validated runs and monitor current progress, health, metrics, failures, and cancellation from the TUI.",
  "task_revision": 22,
  "title": "Add terminal run control and status",
  "updated_at": "2026-09-08T16:45:23+00:00",
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
