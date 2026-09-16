---
{
  "branch": "feature/ar-1265-runtime-owned-replay-entrypoint",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-17T00:25:16+00:00",
  "depends_on": [
    "AR-1237",
    "AR-1238",
    "AR-1239"
  ],
  "id": "AR-1265",
  "next_action": "Commit runtime-owned launch bundle after dead-code fix; then add executable replay dispatch and lifecycle tests.",
  "observed_branch": "feature/ar-1265-runtime-owned-replay-entrypoint",
  "observed_dirty": 2,
  "observed_head": "301b9e1e8c1a522bd4ac53ddb0600b12928d90e8",
  "owner": "asb_ar1024_lifecycle_router",
  "plan": "../plans/AR-1265.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Provide a real runtime-owned strict-replay CLI entrypoint.",
  "task_revision": 28,
  "title": "Runtime-owned strict-replay CLI entrypoint",
  "updated_at": "2026-09-16T22:27:32+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1265-runtime-replay-entrypoint"
}
---
## AR-1265

Implement the runtime-owned strict-replay entrypoint and supervised lifecycle contract. AR-1262's
unmerged implementation is not an input; preserve its review as the reason this separate AR exists.

- 2026-09-16T22:19:31+00:00: Dependencies AR-1237, AR-1238, and AR-1239 are done; AR-1262 review
  proves a separate runtime-owned entrypoint is required.

- 2026-09-16T22:19:45+00:00: Claimed by asb_ar1024_lifecycle_router.

- 2026-09-16T22:20:30+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T22:20:41+00:00: Recorded command exit 101; command argv SHA-256
  63ab3884ab9bcc90b152b670679db1838641a24ef89b5882b21150218acfda2d.

- 2026-09-16T22:21:09+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T22:21:19+00:00: Recorded command exit 0; command argv SHA-256
  63ab3884ab9bcc90b152b670679db1838641a24ef89b5882b21150218acfda2d.

- 2026-09-16T22:21:27+00:00: Recorded command exit 0; command argv SHA-256
  1fd26a558e8ddc9805f77c8e5bd0be22c3406605621b83c467722874ebf64fa1.

- 2026-09-16T22:21:36+00:00: Recorded command exit 0; command argv SHA-256
  69f7e3331e88a1cba83d2b08317550cd841ad28b2f6c710e70fd6edb6a577b87.

- 2026-09-16T22:21:55+00:00: Signed c679467 adds fresh runtime replay_entrypoint module from current
  main: RuntimeReplayAttestation has private readiness/digest fields, constructors are
  runtime-internal, ReplayLaunchAuthority is one-shot and consumes authenticated handoff exactly
  once. Focused authority test passes 1/1; cargo fmt passes. Initial test failure was dead-code
  warnings on runtime-internal constructors/fields, fixed with narrow annotations. Product tree
  clean.

- 2026-09-16T22:22:34+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T22:22:57+00:00: Recorded command exit 101; command argv SHA-256
  4d794e29b61dffc224f97f0280c573e3ed07695dad1bba348b4bd20627fb7998.

- 2026-09-16T22:24:30+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T22:24:48+00:00: Recorded command exit 0; command argv SHA-256
  4d794e29b61dffc224f97f0280c573e3ed07695dad1bba348b4bd20627fb7998.

- 2026-09-16T22:25:16+00:00: Heartbeat by asb_ar1024_lifecycle_router.

- 2026-09-16T22:25:18+00:00: Recorded command exit 0; command argv SHA-256
  b531c9b318472575743e64f2bad65d82351e4a903664641db806c5c64f5f4a0c.

- 2026-09-16T22:25:27+00:00: Recorded command exit 0; command argv SHA-256
  535a44864a98ef7dfbac9336ff0e27f327c62b7d350e5f943b81b509d01c036f.

- 2026-09-16T22:26:17+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T22:26:28+00:00: Recorded command exit 101; command argv SHA-256
  4d794e29b61dffc224f97f0280c573e3ed07695dad1bba348b4bd20627fb7998.

- 2026-09-16T22:26:54+00:00: Focused cargo test initially failed at runtime replay_entrypoint.rs:
  issue_launch was unused under -D warnings (exit 101). This is a compile hygiene failure from the
  new runtime seam, not a product behavior failure; added a narrow dead_code allowance because the
  runtime-only issuer is intentionally consumed by a later CLI entrypoint integration. Rerun focused
  tests now.

- 2026-09-16T22:27:08+00:00: Recorded command exit 0; command argv SHA-256
  4d794e29b61dffc224f97f0280c573e3ed07695dad1bba348b4bd20627fb7998.

- 2026-09-16T22:27:23+00:00: Recorded command exit 0; command argv SHA-256
  8b7b738045a7ea62115c620784d7f6ca349907f65245bd6f96e8d64024c81823.

- 2026-09-16T22:27:32+00:00: Recorded command exit 0; command argv SHA-256
  25ed64071a1368ccee047775a536c3f41b1cb5b917c9c1699654066dbb35133a.
