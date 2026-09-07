---
{
  "branch": "feature/reliability-fairness",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-07T05:27:20+00:00",
  "depends_on": [
    "AR-0203",
    "AR-0204",
    "AR-0401"
  ],
  "id": "AR-1004",
  "next_action": "Hold immutable c6c7d37 for independent review; publish only after approval and exact-main recheck.",
  "observed_branch": "feature/reliability-fairness",
  "observed_dirty": 3,
  "observed_head": "c6c7d37e27a33c3d5e4e0165a04585403260d317",
  "owner": "contracts-20260906",
  "plan": "../plans/AR-1004.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Report repeated-attempt reliability and prevent aggregate results from hiding starvation or hard strata.",
  "task_revision": 47,
  "title": "Measure reliability and mixed-workload fairness",
  "updated_at": "2026-09-07T03:58:49+00:00",
  "worktree_key": "agent-systems-benchmark-reliability-fairness"
}
---
## AR-1004

Report repeated-attempt reliability and prevent aggregate results from hiding starvation or hard strata.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-07T03:26:36+00:00: Dependencies AR-0203, AR-0204, and AR-0401 are durably done. Promote
  this P1 analysis task for contracts-20260906 after AR-0902 release; its asb-analysis
  reliability/report scope is independent of active frontend-control, mini-SWE, and native-platform
  paths.

- 2026-09-07T03:27:20+00:00: Claimed by contracts-20260906.

- 2026-09-07T03:27:46+00:00: Recorded command exit 0; command argv SHA-256
  95d17f4eb08fbda8ab0832bb2ee42c62d939545eff69c8cd25ce253283420c83.

- 2026-09-07T03:31:21+00:00: Recorded command exit 2; command argv SHA-256
  48458d4adcbc2714c4ae60f17ec39d916357031118af6e75d9a5cd826c73f20e.

- 2026-09-07T03:33:09+00:00: Recorded command exit 0; command argv SHA-256
  c519f43ba3b5d096908f69ee04349e26ec55bab7fa7aaf32c0d3e1689526bded.

- 2026-09-07T03:34:10+00:00: Recorded command exit 0; command argv SHA-256
  c519f43ba3b5d096908f69ee04349e26ec55bab7fa7aaf32c0d3e1689526bded.

- 2026-09-07T03:34:38+00:00: Recorded command exit 101; command argv SHA-256
  71855465d58a14c2a688a4b1274b5ab8828d5cbd3d8f4a99dcc72cbdec81fa4b.

- 2026-09-07T03:34:53+00:00: Recorded command exit 0; command argv SHA-256
  c519f43ba3b5d096908f69ee04349e26ec55bab7fa7aaf32c0d3e1689526bded.

- 2026-09-07T03:35:15+00:00: Recorded command exit 0; command argv SHA-256
  71855465d58a14c2a688a4b1274b5ab8828d5cbd3d8f4a99dcc72cbdec81fa4b.

- 2026-09-07T03:35:39+00:00: Recorded command exit 0; command argv SHA-256
  96267ae6178bc8a81d2bd589503ac621cc69c92687335eccb0c0a81916f6e5fd.

- 2026-09-07T03:36:37+00:00: Recorded command exit 0; command argv SHA-256
  33e9962ad00866c6616045365339c9f3bd27b0ebfeaba60a8acaf4f363e008db.

- 2026-09-07T03:36:54+00:00: Recorded command exit 0; command argv SHA-256
  2e8a9dc7938940a8cb62ccb50f0c8f51bb82a11b32d560fbab75da32f0e345c3.

- 2026-09-07T03:37:15+00:00: Implemented initial four-path asb-analysis-only boundary:
  constructor-validated workload/language/difficulty strata; complete k-wide trials with
  duplicate/gap rejection; non-forgeable first-attempt, empirical pass@k and empirical all-k pass^k
  rates; exact passed/failed/timed-out/cancelled/unstarted counts; stable per-class queue,
  starvation and SLO reports; explicit empirical-evidence limits. Hand-calculated mixed-strata,
  censoring, hard-class, extreme queue, malformed lifecycle/cardinality, accessor/error, and
  deterministic repeated-seed/input-permutation tests pass. Focused asb-analysis tests/clippy/doc
  compile-fail pass. Owned reliability.rs coverage is 100% lines/regions/functions; full
  asb-analysis is 99.15% lines. First patch wrapper invocation supplied heredoc to handoffctl rather
  than nested shell and failed before product mutation; corrected nested apply_patch. First compile
  then correctly failed missing integration-test crate docs; added the required public-boundary
  module docs and unchanged rerun passed.

- 2026-09-07T03:38:32+00:00: Recorded command exit 0; command argv SHA-256
  33e9962ad00866c6616045365339c9f3bd27b0ebfeaba60a8acaf4f363e008db.

- 2026-09-07T03:39:20+00:00: Recorded command exit 0; command argv SHA-256
  c519f43ba3b5d096908f69ee04349e26ec55bab7fa7aaf32c0d3e1689526bded.

- 2026-09-07T03:39:42+00:00: Recorded command exit 0; command argv SHA-256
  33e9962ad00866c6616045365339c9f3bd27b0ebfeaba60a8acaf4f363e008db.

- 2026-09-07T03:40:11+00:00: Recorded command exit 101; command argv SHA-256
  df61444569926f3b1f8e9d79988a4929a1632cc0876e926557aa8baaeae2925a.

- 2026-09-07T03:40:44+00:00: Recorded command exit 0; command argv SHA-256
  c519f43ba3b5d096908f69ee04349e26ec55bab7fa7aaf32c0d3e1689526bded.

- 2026-09-07T03:41:20+00:00: Recorded command exit 0; command argv SHA-256
  df61444569926f3b1f8e9d79988a4929a1632cc0876e926557aa8baaeae2925a.

- 2026-09-07T03:41:40+00:00: Recorded command exit 0; command argv SHA-256
  d3bbda69df3ceafea951d8fbdcf15f50c671a2c1c350d45c80477a09c76633c7.

- 2026-09-07T03:42:03+00:00: Recorded command exit 0; command argv SHA-256
  33e9962ad00866c6616045365339c9f3bd27b0ebfeaba60a8acaf4f363e008db.

- 2026-09-07T03:42:39+00:00: Recorded command exit 0; command argv SHA-256
  df61444569926f3b1f8e9d79988a4929a1632cc0876e926557aa8baaeae2925a.

- 2026-09-07T03:42:59+00:00: Recorded command exit 0; command argv SHA-256
  da94b863c52c03ce16a564728480120f4f87002a1c1238f341492c34839e0260.

- 2026-09-07T03:43:30+00:00: Recorded command exit 0; command argv SHA-256
  777d2010520dd994e7ed5c084772589aeaf46ca02e615b0add0e46feb3a10dbe.

- 2026-09-07T03:44:37+00:00: Recorded command exit 0; command argv SHA-256
  7c29c5cdadf347685c732e6ebf9d9338c072e1a8fb78e8e677aba8ce0659b0e7.

- 2026-09-07T03:49:32+00:00: Recorded command exit 2; command argv SHA-256
  c5166dcbde04dc0e74857de046d19fa87a8ebb3675313f6bc6699a7b1b9b7abf.

- 2026-09-07T03:50:28+00:00: Recorded command exit 0; command argv SHA-256
  30292fc0b5bbc77af9f660d586bff44928d2e2f26da50848d1e439f8590d7d7b.

- 2026-09-07T03:50:44+00:00: Recorded command exit 0; command argv SHA-256
  ddf42d7c27dd5ef1f70dc9a2e4e7203621b7f0ecfdd0c3c08728b2b08ecf8301.

- 2026-09-07T03:51:31+00:00: Completed the four-path asb-analysis reliability/fairness boundary and
  exact-tree self-audit. Exact empirical first-attempt, at-least-one pass@k, and all-k pass^k
  reports retain failed/timed-out/cancelled/not-started attempts; enforce complete k-wide
  epoch/class/trial cardinality; expose stable aggregate, class, and epoch queue/SLO/starvation
  evidence; and keep evidence outputs constructor-private. Seven integration tests include
  hand-calculated mixed strata, all 25 two-attempt outcome pairs, deterministic repeated seeds and
  input permutations, hard/degrading epoch visibility, malformed lifecycle/cardinality, threshold
  inclusion, and u64::MAX queue arithmetic. Full workspace fmt/clippy/tests/docs/release/formal,
  deny/audit/actionlint/zizmor/Gitleaks/failure fixtures/platform, and configured coverage passed;
  reliability.rs is 100% regions/functions/lines and asb-analysis 98.33% regions/99.28%
  functions/99.20% lines. The final quality wrapper encountered concurrent stale generated
  WORKTREES/private-host validation after all product gates passed; state was reconciled
  independently at fb4a9c8, snapshot/live doctor became green, and no product rerun was needed.
  Added pinned public provenance: tau-bench 59a200c (MIT, arXiv:2406.12045) and Inspect AI 0.3.258
  e72c73f (MIT), with no copied code/runtime dependency; focused fmt, 24 tests, 4 doctests including
  compile-fail, and clippy passed afterward using Rust/Cargo 1.93.0. Wrapper mistakes remain
  visible: an unset patch environment caused exit 2 before product mutation; durable effects were
  checked before applying once.

- 2026-09-07T03:52:03+00:00: Recorded command exit 0; command argv SHA-256
  79ccce9605d96a967da7319bf8ff3cf9212668563433ddda7fbc33fe333e35a8.

- 2026-09-07T03:52:39+00:00: Recorded command exit 0; command argv SHA-256
  a247798cc078537107028704e1b6579ebf974ff7d61d9d184f93ad326d7c0e97.

- 2026-09-07T03:52:53+00:00: Prepared clean unpublished immutable candidate
  c6c7d37e27a33c3d5e4e0165a04585403260d317, tree 9604b8e2e3dee2872ee0536c88864cf3efed638a, exactly
  one commit on public main 4a59593c0c55e0ad72656363473a404d8be1054b. The commit has a valid Martin
  Beck SSH signature and exactly one matching Signed-off-by trailer. Exact range contains only the
  four declared asb-analysis paths. DCO checker, repository policy, redacted exact-range Gitleaks,
  diff check, privacy keyword audit, and clean-tree check pass. No feature remote ref or PR exists.
  Candidate requires independent immutable review before publication.

- 2026-09-07T03:56:33+00:00: Recorded command exit 0; command argv SHA-256
  20eb12877bad56fc6d928b334de47ffe701ee810b22f628f234a9f1108ac6068.

- 2026-09-07T03:57:00+00:00: Recorded command exit 0; command argv SHA-256
  d1e0c128a7bb60080658d7cf31929af00184051a8cf5c84179dafed2bba46232.

- 2026-09-07T03:57:20+00:00: Recorded command exit 0; command argv SHA-256
  8f0f7901bf7f1530d4f68f1ff9ba5a476018e7b4f4e6264cf98cfea917ce4e17.

- 2026-09-07T03:58:13+00:00: Recorded command exit 0; command argv SHA-256
  3ea8662b590246c45c05727f054ba180b2d732b9e89a508f133a4f19afe529ac.

- 2026-09-07T03:58:30+00:00: Recorded command exit 0; command argv SHA-256
  10d2e678647a1dc6b84d577adf30564ec042c842e0eac9a2321e3c9d4458546a.

- 2026-09-07T03:58:49+00:00: Recorded command exit 0; command argv SHA-256
  38d11b7839406ea5bd7afe58d0c710765cd01b62fa2b4f9ae3ae22c837b334ca.
