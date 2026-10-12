---
{
  "branch": "feature/ar-1772-unified-step-progress-reporter",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-12T07:29:39+00:00",
  "depends_on": [
    "AR-1775"
  ],
  "id": "AR-1772",
  "next_action": "Blocked on dedicated Cargo tool-discovery fixture isolation successor; reporter focused/diagnostic tests are green, but exact full asb-cli gate has two ambient Cargo probe failures. Do not accept or waive until full gate is green.",
  "observed_branch": "feature/ar-1772-unified-step-progress-reporter",
  "observed_dirty": 1,
  "observed_head": "763c0f4f60fede50ad63a7b9398aa468ca2d4e61",
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
  "task_revision": 63,
  "title": "Unified human step-progress reporter",
  "updated_at": "2026-10-12T05:31:56+00:00",
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

- 2026-10-12T02:14:38+00:00: Recorded command exit 101; command argv SHA-256
  3d738ecca808106a6d3f40dce9f253b89aba9faf5e73d05d854aa53b1e26c857.

- 2026-10-12T02:14:56+00:00: Recorded command exit 0; command argv SHA-256
  3d738ecca808106a6d3f40dce9f253b89aba9faf5e73d05d854aa53b1e26c857.

- 2026-10-12T02:15:05+00:00: Recorded command exit 0; command argv SHA-256
  c6125931e3473b8532ffca127825e8bafe99f79b2462df17b6705a521836c317.

- 2026-10-12T02:15:13+00:00: Recorded command exit 0; command argv SHA-256
  5536295cad907b40de7760309c9964d5980c36afae4fdb3e1e03245d7a38b279.

- 2026-10-12T02:15:29+00:00: Gate diagnosis and repair: full asb-cli failed
  diagnostic_contract::ordinary_cli_producers_are_mechanically_closed because router edits shifted
  line-based reviewed call-site identities; restoring router block and moving module declaration
  into human.rs preserved identities. The next focused gate passed. A transient compile failure also
  reported dead_code for unreferenced reporter; module-level allow is intentional until universal
  instrumentation AR-1773 consumes the API.

- 2026-10-12T02:15:56+00:00: Recorded command exit 101; command argv SHA-256
  c9266e05291502ffd361fe1821edf1e07e255bcbf030cad9d5973101fe63d04d.

- 2026-10-12T02:16:06+00:00: Exact full-gate failure: cargo test -p asb-cli,
  tool_discovery::tests::path_discovery_is_deterministic_and_bounded, expected tool version
  null/reason version_probe_unavailable but observed cargo 1.0 and reason null. Reporter tests and
  diagnostic_contract::ordinary_cli_producers_are_mechanically_closed pass. This is unrelated to
  AR-1772 and reflects ambient cargo probe output.

- 2026-10-12T02:17:38+00:00: Successor ownership audit: AR-1762-tool-discovery is the existing
  completed owner for tool discovery, but no open successor owns the ambient Cargo-version fixture
  regression. Do not waive full gate; preserve exact failure in this task and request successor
  coordination.

- 2026-10-12T02:17:43+00:00: Blocked truthfully: focused AR-1772 reporter and diagnostic-contract
  tests pass, but required full cargo test remains red at
  tool_discovery::tests::path_discovery_is_deterministic_and_bounded due ambient cargo version probe
  (expected version_probe_unavailable/null, observed cargo 1.0). Existing AR-1762 is completed
  owner; no dedicated successor currently owns this fixture-isolation repair. Do not waive or accept
  AR-1772 until full exact-head gate is green.

- 2026-10-12T05:27:59+00:00: AR-1803 is complete and merged; re-evaluate AR-1772 against current
  protected main exact head and rerun full/focused gates.

- 2026-10-12T05:28:02+00:00: Claimed by ar1772-progress-reporter-luna56.

- 2026-10-12T05:28:05+00:00: Recorded command exit 0; command argv SHA-256
  e622e28f965e41715b2f87ca046805025c71bba7ec1496e488ac94f520ddc0d2.

- 2026-10-12T05:28:12+00:00: Recorded command exit 0; command argv SHA-256
  86ec781ec60a4aaa596634d6c4a49e9491478af966b136bd9281479ca311cbf0.

- 2026-10-12T05:28:18+00:00: Recorded command exit 0; command argv SHA-256
  6ef69f6569cb5a05d13507ce4e86a1fad34da7e86d1a382f6c79632b1e174026.

- 2026-10-12T05:28:24+00:00: Recorded command exit 0; command argv SHA-256
  677bc2cc171a9e8240e46431420cfe8278966da1b5382f1994d91b907d4eac52.

- 2026-10-12T05:28:32+00:00: Recorded command exit 0; command argv SHA-256
  ec38355c2f4209d2cf8ae21a14252fbe1bb7cc56d6165f2f0b73a6bf93892136.

- 2026-10-12T05:28:43+00:00: Recorded command exit 0; command argv SHA-256
  9c0ead30623ef81aa0835e457454e8e696fb35b2b34a4e8341cdfa28caaad624.

- 2026-10-12T05:29:07+00:00: Recorded command exit 101; command argv SHA-256
  efcca2fcdc32708cf3d10e499b46d7e57b0561edfd7d1fa792c8d22f4f2a624b.

- 2026-10-12T05:29:15+00:00: Fresh exact-candidate full gate diagnosis: cargo test --locked -p
  asb-cli --lib on AR-1772 head f9ad19ff ran 432 tests: 430 passed, 2 failed, 0 ignored. Failures
  are tool_discovery::tests::path_discovery_is_deterministic_and_bounded and
  tool_discovery::tests::version_probe_reaps_background_processes_without_pipe_hang. Both expected
  Cargo fixture version null with reason version_probe_unavailable but observed ambient Cargo
  version cargo 1.0 and reason null. Reporter step_progress 3/3 and diagnostic_contract
  ordinary_cli_producers 1/1 pass. This is unrelated AR-1772 product behavior; preserve full-gate
  blocker and do not waive.

- 2026-10-12T05:29:19+00:00: Released blocked with exact full-gate evidence: AR-1772 reporter and
  diagnostic focused tests pass, but full asb-cli has two deterministic Cargo probe fixture failures
  (ambient cargo 1.0 observed instead of null/version_probe_unavailable), 430/432 passed. AR-1803 is
  complete but does not repair these distinct probe fixtures. No product PR/merge or gate waiver.

- 2026-10-12T05:29:39+00:00: Reopen stale AR-1772 candidate after AR-1803 completion; rebase
  reporter diff onto current protected main and rerun exact gates.

- 2026-10-12T05:29:39+00:00: Claimed by ar1772-progress-reporter-luna56.

- 2026-10-12T05:29:45+00:00: Recorded command exit 0; command argv SHA-256
  12b28c8c7005c506d4f6b256c5a85659b053ff57cc0ad5ef9dee6bd614fc7beb.

- 2026-10-12T05:29:50+00:00: Recorded command exit 0; command argv SHA-256
  e6c5f96874fd41490529863beb26b8cbb17b2cd3c03808778b81a0e2fea552c1.

- 2026-10-12T05:30:06+00:00: Recorded command exit 0; command argv SHA-256
  677bc2cc171a9e8240e46431420cfe8278966da1b5382f1994d91b907d4eac52.

- 2026-10-12T05:30:22+00:00: Recorded command exit 0; command argv SHA-256
  9c0ead30623ef81aa0835e457454e8e696fb35b2b34a4e8341cdfa28caaad624.

- 2026-10-12T05:30:50+00:00: Recorded command exit 0; command argv SHA-256
  efcca2fcdc32708cf3d10e499b46d7e57b0561edfd7d1fa792c8d22f4f2a624b.

- 2026-10-12T05:31:27+00:00: Recorded command exit 2; command argv SHA-256
  48ab3ffc6bb04a557a3ff33f5191b2dd0b0cb7683332ef5da9b8203462913847.

- 2026-10-12T05:31:39+00:00: Recorded command exit 1; command argv SHA-256
  69fcc4e3eae6355972ea471d1dcfdac3bff0491a658f349c950765f374102fef.

- 2026-10-12T05:31:45+00:00: Recorded command exit 0; command argv SHA-256
  c6973b6b7f808b25109354c3f0de92d81bfc13cd6570221c618ac58d1ea1d381.

- 2026-10-12T05:31:56+00:00: Recorded command exit 101; command argv SHA-256
  658a9a9a691bb510ec742ef28b0ace514a78ca5eb9bbee364cedaa1d96324dc0.
