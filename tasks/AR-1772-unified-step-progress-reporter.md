---
{
  "branch": "feature/ar-1772-unified-step-progress-reporter",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-12T06:03:38+00:00",
  "depends_on": [
    "AR-1775"
  ],
  "id": "AR-1772",
  "next_action": "Obtain independent review of exact commit, run required full checks, then publish reviewed PR and post-merge acceptance.",
  "observed_branch": "feature/ar-1772-unified-step-progress-reporter",
  "observed_dirty": 3,
  "observed_head": "10e336655e39ce9eff0b30770348e72c92aa4e98",
  "owner": "ar1772-progress-reporter-luna56",
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
  "task_revision": 29,
  "title": "Unified human step-progress reporter",
  "updated_at": "2026-10-12T02:14:26+00:00",
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

- 2026-10-12T02:02:51+00:00: dependencies verified: AR-1775 is done

- 2026-10-12T02:02:54+00:00: Claimed by ar1772-progress-reporter-luna56.

- 2026-10-12T02:03:11+00:00: Heartbeat by ar1772-progress-reporter-luna56.

- 2026-10-12T02:03:38+00:00: Heartbeat by ar1772-progress-reporter-luna56.

- 2026-10-12T02:03:51+00:00: Recorded command exit 0; command argv SHA-256
  8a1e0e32146a9f14f4ddc4d415c1b397d127f83535b5e7638bf88536bfc46ecd.

- 2026-10-12T02:05:47+00:00: Checkpoint: isolated AR-1772 worktree contains initial step_progress
  module and public module wiring; no commit yet.

- 2026-10-12T02:06:12+00:00: Recorded command exit 101; command argv SHA-256
  30750a6ed153fa6ade122ac0af3ea5d7f30be20442f77a0117ba6d9ab6365c54.

- 2026-10-12T02:06:35+00:00: Recorded command exit 101; command argv SHA-256
  30750a6ed153fa6ade122ac0af3ea5d7f30be20442f77a0117ba6d9ab6365c54.

- 2026-10-12T02:06:57+00:00: Recorded command exit 101; command argv SHA-256
  30750a6ed153fa6ade122ac0af3ea5d7f30be20442f77a0117ba6d9ab6365c54.

- 2026-10-12T02:07:20+00:00: Recorded command exit 101; command argv SHA-256
  30750a6ed153fa6ade122ac0af3ea5d7f30be20442f77a0117ba6d9ab6365c54.

- 2026-10-12T02:07:43+00:00: Recorded command exit 101; command argv SHA-256
  30750a6ed153fa6ade122ac0af3ea5d7f30be20442f77a0117ba6d9ab6365c54.

- 2026-10-12T02:07:59+00:00: Recorded command exit 0; command argv SHA-256
  30750a6ed153fa6ade122ac0af3ea5d7f30be20442f77a0117ba6d9ab6365c54.

- 2026-10-12T02:08:45+00:00: Recorded command exit 101; command argv SHA-256
  30750a6ed153fa6ade122ac0af3ea5d7f30be20442f77a0117ba6d9ab6365c54.

- 2026-10-12T02:09:52+00:00: Focused test initially passed reporter unit tests; router integration
  compile failed because reporter took stdout/stderr by value. Reborrow fix applied. Prior exact
  compiler diagnostics: E0382 borrow of moved stderr/stdout at lib.rs:271/280; recommended &mut *
  reborrow. One post-reconcile run was also blocked by generated handoffctl.pyc >200 KiB.

- 2026-10-12T02:10:31+00:00: Recorded command exit 0; command argv SHA-256
  30750a6ed153fa6ade122ac0af3ea5d7f30be20442f77a0117ba6d9ab6365c54.

- 2026-10-12T02:10:45+00:00: Recorded command exit 0; command argv SHA-256
  37217a301668b8e1be10c93b48d12ce87b342acc597598876357a95ddaec65f0.

- 2026-10-12T02:10:57+00:00: Recorded command exit 0; command argv SHA-256
  7a66eb479f3d92a2841b13cd4eab1c8fb2d2db58ee4a0a601e07d1f97fbba3f6.

- 2026-10-12T02:11:16+00:00: Checkpoint commit 10e336655e39ce9eff0b30770348e72c92aa4e98: signed
  AR-1772 reporter module, router-owned human construction, deterministic clock tests. Focused cargo
  test -p asb-cli step_progress passes 3 tests.

- 2026-10-12T02:12:00+00:00: Recorded command exit 101; command argv SHA-256
  c9266e05291502ffd361fe1821edf1e07e255bcbf030cad9d5973101fe63d04d.

- 2026-10-12T02:12:13+00:00: Recorded command exit 101; command argv SHA-256
  ae0eb1c5339849c8562e98ca6a6505059c0e0331b2e1448570c8cf5d9291ed2a.

- 2026-10-12T02:13:04+00:00: Recorded command exit 101; command argv SHA-256
  3d738ecca808106a6d3f40dce9f253b89aba9faf5e73d05d854aa53b1e26c857.

- 2026-10-12T02:13:56+00:00: Recorded command exit 1; command argv SHA-256
  a088365c0a939590e0b2c2e372a031e445df67db9e1e8a8d471e2386b89a596f.

- 2026-10-12T02:14:24+00:00: Recorded command exit 0; command argv SHA-256
  5070341b6dac73aac957b91317d18f9c4680ec4b8cd613ff63d7908cc0a55fd1.
