---
{
  "branch": "feature/ar-1772-unified-step-progress-reporter",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-13T21:37:45+00:00",
  "depends_on": [
    "AR-1775"
  ],
  "id": "AR-1772",
  "next_action": "Implement the single human step reporter on the mandatory output router after its output, level, status, and quiet contracts are accepted.",
  "observed_branch": "feature/ar-1772-unified-step-progress-reporter",
  "observed_dirty": 0,
  "observed_head": "65ee830e6659ac5426757833d1030ae0c32f8ac5",
  "owner": "ar1772-progress-luna",
  "plan": "../plans/AR-1772-unified-step-progress-reporter.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "contract-test",
    "evidence_digest": "",
    "evidence_ref": "",
    "spec_ref": "specs/AR-1772.json",
    "spec_revision": 1,
    "status": "pending"
  },
  "spec_ref": "specs/AR-1772.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Provide the sole status/progress reporter for delayed, terminal-safe, ETA-bearing human step output.",
  "task_revision": 4,
  "title": "Unified human step-progress reporter",
  "updated_at": "2026-10-13T19:37:45+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1772-unified-step-progress-reporter"
}
---

Create one shared Rust status/progress reporter used for all ASB human status
updates. It begins each meaningful operation as a structured step with a stable
identifier, concise label, total work when known, completed work, rate/time
observations, and terminal outcome. The helper—not individual commands—decides
whether to produce no transient rendering for a step that completes within one
second, or to begin/update a progress bar once the one-second threshold is
crossed. It must update until the step finishes and then emit the final fixed-width
state line.

For known work totals, show completed/total and a rough remaining-time estimate.
For genuinely unknown totals, show an honest indeterminate progress bar/activity
state and elapsed time; never invent a percentage or ETA. Callers must report
meaningful substep/work-unit changes and any revised total so estimates can be
derived from real observations. The reporter owns adaptive refresh throttling,
clock injection for tests, terminal-width clipping, redraw/line cleanup, nested
or sequential step behavior, interruption/failure/cancellation finalization, and
safe writer errors.

Only human operational mode may instantiate it, and it must render exclusively
through the AR-1775 output router at the selected output level. JSON mode and
quiet mode must not instantiate a renderer or emit any reporter bytes.
Non-terminals receive stable,
append-only fixed-width lines without ANSI/control/redraw bytes; a terminal may
redraw the `[WAIT]` progress bar. No hand-written status or progress print is
allowed outside this helper.

- 2026-10-13T19:37:28+00:00: Dependency AR-1775 is complete; existing merged implementation and
  evidence are ready for reconciliation.

- 2026-10-13T19:37:45+00:00: Claimed by ar1772-progress-luna.
