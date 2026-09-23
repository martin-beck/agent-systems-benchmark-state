---
{
  "branch": "feature/ar-1324-auth-helper-control-contract",
  "checkpoint_commit": "5abd8c7c2d2a6a38e2d9be9340f0eb5e16f8807a",
  "claim_expires": "2026-09-23T07:45:07+00:00",
  "depends_on": [],
  "id": "AR-1324",
  "next_action": "Monitor authoritative pull_request checks for PR #248 at 5abd8c7; merge only after all required checks pass, then perform ASB\u2194asb-tui first-user/live-provider wizard acceptance.",
  "owner": "codex",
  "plan": "../plans/AR-1324.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Own the ASB control and runner backend for safe credential-helper invocation.",
  "task_revision": 24,
  "title": "Authenticated credential-helper control contract",
  "updated_at": "2026-09-23T05:59:29+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1324-auth-helper-control-contract"
}
---

AR-1323 owns the asb-tui user journey, but the runner must own helper
discovery, executable identity, timeout/cancellation, generation fencing and
secret resolution. This AR adds the versioned ASB control schema and backend
integration using the existing sealed helper implementation. The frontend must
never receive a raw credential or execute an arbitrary path.

- 2026-09-21T03:27:36+00:00: AR-1322 exact-main post-merge gates are green; open the runner-owned
  helper contract slice.

- 2026-09-21T03:27:39+00:00: Claimed by codex-ar1324.

- 2026-09-21T03:31:23+00:00: Heartbeat by codex-ar1324.

- 2026-09-21T03:42:07+00:00: Implemented signed/DCO runner-owned v1.10 auth_helper_invoke control
  operation; validates helper profile, uses no-follow allowlisted executable and sealed
  CredentialBackend, persists only typed AuthStatus receipt. Focused protocol test and clippy pass.

- 2026-09-21T03:43:34+00:00: Full workspace tests pass when isolated scratch roots use a private
  non-overlapping temporary base; the prior default run failed only because the worktree under /tmp
  overlaps the repository safety guard. The focused descendant-cancellation test passes with the
  safe temporary base. ASB control/auth tests and clippy pass.

- 2026-09-21T03:47:44+00:00: Hardened idempotency: helper resolution now occurs inside the durable
  mutation closure, after replay detection, so retries do not invoke the helper twice. Signed/DCO
  commit 2953465; cargo check passes.

- 2026-09-21T03:58:07+00:00: Regenerated all checked-in control schemas after adding
  auth_helper_invoke; schema conformance now passes. Signed/DCO commit 7165884 includes runner
  operation, idempotency hardening, docs, tests, and generated schema updates.

- 2026-09-21T03:59:57+00:00: ASB schema conformance and all focused control/auth tests pass. Full
  workspace sweep is blocked by reproducible pre-existing asb-metrics test
  missing_malformed_and_unsafe_configuration_fail_closed (kernel.rs line 733); no auth/catalog code
  path is implicated. Keep this defect separate and fix before release qualification.

- 2026-09-21T04:07:28+00:00: Fixed two independent quality issues exposed by the isolated full
  sweep: metrics negative test now targets fixed public /tmp instead of TMPDIR; parallel
  mini-SWE/OpenHands test scratch roots now include atomic sequence identities. Focused metrics and
  full asb-agents suites pass; signed/DCO commits 71b5b63 and ba140f8.

- 2026-09-21T04:11:37+00:00: Full TMPDIR-isolated cargo test --locked --workspace passes after
  fixing two test-only assumptions: metrics and runtime transport now use fixed public /tmp negative
  boundaries; parallel mini-swe/OpenHands scratch roots use atomic nonces. cargo fmt --all --
  --check passes; cargo clippy --locked --workspace --all-targets -D warnings completed without
  reported diagnostics. Production validation and security boundaries unchanged.

- 2026-09-21T04:12:48+00:00: Opened PR #248 from exact checkpoint
  ba32bc524355420e0658f68cbd76a5c19f30c3c7. Hosted checks are running; local locked workspace, fmt,
  and clippy gates are green.

- 2026-09-21T04:23:31+00:00: Hosted Repository quality failed only because coverage hit a Unix
  socket path-length fixture under hosted target paths. Reproduced locally; shortened the test-only
  sandbox fixture label, preserving runtime behavior. Focused test passes; TMPDIR-isolated coverage
  sweep reaches passing reports (workspace 93.45% lines, critical asb-replay 96.47% lines). Pushed
  signed fix as 5c13a1d.

- 2026-09-21T04:34:39+00:00: Hosted coverage remained below floor at 89.87% despite socket fixture
  correction. Added a testable registration seam and comprehensive helper success/rejection coverage
  without unsafe environment mutation. Local isolated coverage now passes workspace 90.43% lines and
  critical package floors; focused helper test passes. Signed commit bab01b7 pushed to PR #248.

- 2026-09-21T04:36:32+00:00: Hosted Rust gate found two clippy needless-borrow errors in helper
  registration seam. Corrected them; focused helper test and package clippy pass locally. Signed fix
  4c32f13 pushed to PR #248.

- 2026-09-21T04:42:09+00:00: Hosted coverage reached 89.96%, narrowly under the 90% floor. Added
  focused tests for empty provider/locator, missing executable, digest mismatch, and helper
  rejection branches. Package clippy and focused test pass locally; signed 6439b82 pushed.

- 2026-09-21T04:50:08+00:00: Prior hosted runs were stale for over an hour and were cancelled;
  policy had failed at 89.97% coverage. Added helper registration/deadline/error branch coverage in
  signed commit ed61f86. Manually triggered all required workflows on exact PR head
  ed61f865c99d139facb813e7344699595dc7155e because pull_request checks did not auto-start after the
  push.

- 2026-09-21T04:53:49+00:00: The prior manually triggered run set again stalled in
  Rust/policy/aarch64; stale runs were cancelled. A fresh complete workflow set is now running on
  the same exact head ed61f865c99d139facb813e7344699595dc7155e. No merge was attempted against stale
  or cancelled evidence.

- 2026-09-21T04:55:24+00:00: Manual workflow_dispatch policy failure was correctly rejected because
  it scans unrelated historical merge commit 909078c without DCO. Closed/reopened PR #248 to
  regenerate authoritative pull_request-context checks on exact head ed61f865; fresh pull_request
  runs are now executing.

- 2026-09-22T13:47:03+00:00: Recovered expired claim formerly owned by codex-ar1324. Claim expired
  at 2026-09-21T05:31:23Z and no owner process exists; released to open as prerequisite for adding
  the AR-1328..1336 benchmark integration series.

- 2026-09-23T05:45:07+00:00: Claimed by codex.

- 2026-09-23T05:45:24+00:00: Added malformed-helper and missing-reference rejection coverage; local
  cargo test and clippy pass; hosted-equivalent workspace coverage is 90.46% lines, above the 90%
  floor. Pushed b5f6553 to PR #248; awaiting fresh pull_request-context checks.

- 2026-09-23T05:51:11+00:00: Fresh CI exposed a restart-test race: backend lock release can lag
  worker teardown. Added bounded retry in restart-focused tests for production and recording
  backends, preserving immediate exclusivity semantics. Full asb-cli lib suite passes locally
  (90/90); pushed 0116bf1.

- 2026-09-23T05:59:29+00:00: Hosted coverage remained 89.98% despite local margin, so added explicit
  tests for all helper environment binding paths through a safe injectable value seam. Targeted test
  and clippy pass; pushed 5abd8c7. Awaiting fresh PR checks.
