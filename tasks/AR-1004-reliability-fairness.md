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
  "next_action": "Verify exact main 814397f with post-merge local gates and all fresh exact-main hosted CI; release only after green reconciliation.",
  "observed_branch": "feature/reliability-fairness",
  "observed_dirty": 0,
  "observed_head": "eb28ca7aeae59b2340af7856e40f0ea31b792e66",
  "owner": "contracts-20260906",
  "plan": "../plans/AR-1004.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Report repeated-attempt reliability and prevent aggregate results from hiding starvation or hard strata.",
  "task_revision": 65,
  "title": "Measure reliability and mixed-workload fairness",
  "updated_at": "2026-09-07T04:11:46+00:00",
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

- 2026-09-07T03:59:56+00:00: Recorded command exit 0; command argv SHA-256
  612d19a9282b6655b1fdc7b3dd34033dcf9d231fe6f218f9d348913750b35635.

- 2026-09-07T04:00:09+00:00: Recorded command exit 0; command argv SHA-256
  47088b5387269d02d18b00d78b68a055f891b6b0972a1c0860b24aa207be63b3.

- 2026-09-07T04:00:32+00:00: Recorded command exit 0; command argv SHA-256
  36b739feca05a8e6fca5e14dfe75edbd53fff61256c145079d113af61d24f0e8.

- 2026-09-07T04:01:03+00:00: Recorded command exit 0; command argv SHA-256
  4cef984f4b74b66ba6920a0e8e12e1dab5f813c2a0af09f9b5659d6bee8e3ba7.

- 2026-09-07T04:01:20+00:00: Recorded command exit 0; command argv SHA-256
  2ea26afc9c9ad2363b7a71f68173c972d0e0e4d6a37682b1eb114f306570c824.

- 2026-09-07T04:02:23+00:00: Recorded command exit 0; command argv SHA-256
  18d418e85733f65d57b6946f9d69a94897bfcbfed93be09c422189b54e8d5d75.

- 2026-09-07T04:02:38+00:00: Recorded command exit 0; command argv SHA-256
  aa815435c3a525e7ab20f7c935335987f54cbc8efe0a942ff38f1c0e294a0be0.

- 2026-09-07T04:02:55+00:00: Recorded command exit 0; command argv SHA-256
  6799f02f236333d088fa02cc630714fe84762ef80f4ded5f5e46df5a32347891.

- 2026-09-07T04:03:10+00:00: Recorded command exit 1; command argv SHA-256
  06941f1ac88a26f69dd73e9b9b89b4b33f7ba4616a24486108562a309afb1189.

- 2026-09-07T04:03:31+00:00: Recorded command exit 0; command argv SHA-256
  93ef2785f78e05d3a6af4b721933a8f9c2d284c2ed996c8493e4d5d147d05c33.

- 2026-09-07T04:03:49+00:00: Superseded blocked c6c7d37 with clean unpublished
  eb28ca7aeae59b2340af7856e40f0ea31b792e66, tree fb2c3f118a3a8e4f58f5eab4d87082311364950e, one
  signed+DCO commit on exact public main 4a59593c. Review blockers are closed: analyze_reliability
  now requires a bounded pre-execution PlannedAttempt roster with exact class/epoch/trial/index/seed
  equality, rejects duplicate slots even under different seeds, and fails a wholly omitted hard
  stratum or wrong seed; ReliabilityReport and every aggregate/class/epoch FairnessSummary expose
  the exact starvation threshold. Eight boundary tests cover those regressions plus prior formulas.
  Full workspace fmt/clippy/tests/docs/release/formal passed after repair; final workspace
  clippy/tests and focused doctests passed after dead-branch cleanup. New reliability module
  coverage returned to 100% regions/functions/lines; asb-analysis totals 98.38% regions, 99.30%
  functions, 99.23% lines. Exact DCO, repository policy, redacted Gitleaks, four-path scope, diff
  and clean-tree checks pass. A first final-validation wrapper asserted an incorrectly transcribed
  prospective full hash and exited 1 before any product mutation; fresh rev-parse established
  eb28ca7 and unchanged rerun passed.

- 2026-09-07T04:06:31+00:00: Recorded command exit 0; command argv SHA-256
  f869c988b47c2547360b31b45b490dff64197285c210daf33dfea3ff9caf71d8.

- 2026-09-07T04:07:00+00:00: Recorded command exit 0; command argv SHA-256
  64aa125edacaa73d3a8e8b27fed40ad10d382d092f365948506fc81360c7de94.

- 2026-09-07T04:07:17+00:00: Independent review approved immutable eb28ca7. Re-fetched exact refs,
  verified public main/base remains 4a59593c, feature ref was absent, tree clean,
  signature/DCO/privacy/policy/Gitleaks/four-path scope green, then pushed exact head with
  absent-ref lease and opened focused PR #30
  https://github.com/martin-beck/agent-systems-benchmark/pull/30. PR base/head are exactly
  4a59593c/eb28ca7 and mergeable. Exact-head hosted runs started: Fault assurance 34081912485,
  Formal assurance 34081912577, Repository quality 34081912503, Rust verification 34081912453. Await
  all exact-head jobs; do not merge before coordinator authorization.

- 2026-09-07T04:10:08+00:00: PR #30 exact immutable head eb28ca7/base 4a59593c remains mergeable and
  all ten exact-head jobs are green. Run 34081912485: retained faults x86_64/aarch64, bounded fuzz,
  mutation sentinels green. Run 34081912577: Kani and Loom/state models x86_64/aarch64 green. Run
  34081912503: policy/coverage/supply-chain green. Run 34081912453: Rust verification x86_64/aarch64
  green. Worktree remains clean; hold for coordinator-serialized integration.

- 2026-09-07T04:11:17+00:00: Recorded command exit 1; command argv SHA-256
  7b9a354a762217536de90f9be55aa2a450569f6a63f5b9ecfaee64c79dc8589c.

- 2026-09-07T04:11:46+00:00: Coordinator-authorized signed+DCO no-ff integration was created and
  exact-lease pushed. Durable main is 814397f8f74971589aa02b13da12485169db3e2e with exact parents
  4a59593c and eb28ca7; SSH signature and single matching DCO trailer are valid, primary tree clean,
  and origin/main matches. GitHub PR #30 is MERGED at the same 814397f identity. The integration
  wrapper exited 1 only because its immediate PR-state assertion raced GitHub convergence after the
  successful push; read-only reconciliation confirmed the PR transition seconds later. Do not repeat
  merge/fetch/push. Proceed with exact-main post-merge local and hosted verification.
