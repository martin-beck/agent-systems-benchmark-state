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
  "next_action": "Read complete AR-0805 plan and product frontend/control contracts in the declared clean worktree; do not mutate crates/asb-tui until active AR-0855, which overlaps lib.rs/main.rs, is integrated or its fence is returned, then rebase onto exact main.",
  "observed_branch": "feature/tui-run-control",
  "observed_dirty": 1,
  "observed_head": "b2707c482876dcfb42c756c39165f6ecdb5c7c10",
  "owner": "quality_20260906",
  "plan": "../plans/AR-0805.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Start validated runs and monitor current progress, health, metrics, failures, and cancellation from the TUI.",
  "task_revision": 9,
  "title": "Add terminal run control and status",
  "updated_at": "2026-09-08T16:37:08+00:00",
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
