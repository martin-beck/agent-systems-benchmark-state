---
{
  "branch": "feature/ar-1324-auth-helper-control-contract",
  "checkpoint_commit": "3a1e9c49c728fca014031c0d9fb186bf854f329d",
  "claim_expires": "2026-09-21T05:31:23+00:00",
  "depends_on": [],
  "id": "AR-1324",
  "next_action": "Run hosted ASB quality gates on ba140f8, then integrate exact ASB/TUI heads and perform live first-user wizard acceptance.",
  "owner": "codex-ar1324",
  "plan": "../plans/AR-1324.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Own the ASB control and runner backend for safe credential-helper invocation.",
  "task_revision": 10,
  "title": "Authenticated credential-helper control contract",
  "updated_at": "2026-09-21T04:07:28+00:00",
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
