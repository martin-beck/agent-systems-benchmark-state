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
  "next_action": "Create the declared worktree with the corrected exact git worktree add invocation; then hold product mutation until active AR-0855 broad source-header fence is integrated/released.",
  "owner": "quality_20260906",
  "plan": "../plans/AR-0805.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Start validated runs and monitor current progress, health, metrics, failures, and cancellation from the TUI.",
  "task_revision": 5,
  "title": "Add terminal run control and status",
  "updated_at": "2026-09-08T16:23:47+00:00",
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
