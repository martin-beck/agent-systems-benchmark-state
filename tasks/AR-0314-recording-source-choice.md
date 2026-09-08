---
{
  "branch": "feature/provider-recording-choice",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-08T17:38:25+00:00",
  "depends_on": [
    "AR-0104",
    "AR-0310",
    "AR-0313",
    "AR-0503",
    "AR-0504",
    "AR-0318"
  ],
  "id": "AR-0314",
  "next_action": "Independent immutable review of rebased signed candidate e8fed7e and exact-tree evidence; if approved, publish/update focused PR and require exact-head CI before integration/release.",
  "observed_branch": "feature/provider-recording-choice",
  "observed_dirty": 0,
  "observed_head": "e8fed7e572b6bf9d14d76f15b91b7cb208e2d48b",
  "owner": "quality_20260906",
  "plan": "../plans/AR-0314.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Offer matching prior recordings or an actual provider connection without silently choosing either.",
  "task_revision": 41,
  "title": "Choose matching replay or live provider execution",
  "updated_at": "2026-09-08T14:42:52+00:00",
  "worktree_key": "agent-systems-benchmark-provider-recording-choice"
}
---
## AR-0314

Offer matching prior recordings or an actual provider connection without silently choosing either.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-08T13:37:26+00:00: Dependency audit: AR-0104, AR-0310, AR-0503, AR-0504, and AR-0313 are
  durably done; AR-0803 is done. Promote as highest-priority compatible provider/replay leaf.

- 2026-09-08T13:37:29+00:00: Claimed by quality_20260906.

- 2026-09-08T13:38:40+00:00: Recorded command exit 0; command argv SHA-256
  c2a25f84ed443b9770bf82f9936459b9a8b8dc5e072d4c915fbb2fd7643af8d2.

- 2026-09-08T13:39:07+00:00: Recorded command exit 0; command argv SHA-256
  d60eb14ae9128e35a0b23dbc6d74e92e0a232a68a2318aed870d56226eb6f4be.

- 2026-09-08T00:00:00+00:00: Independent provider/TUI audit found no implementation for resolving
  credential references, verifying their digest, or injecting them at a bounded process boundary.
  Added dependency AR-0318; recording catalog work may proceed, but live credential preflight remains
  fenced until AR-0318 proves the fail-closed resolver and privacy boundary.

- 2026-09-08T13:39:27+00:00: Recorded command exit 0; command argv SHA-256
  a12133e023147b1cbdb6246af3266c39f570839f1079a40b8d37d93d1dfdc0a5.

- 2026-09-08T13:42:28+00:00: Recorded command exit 101; command argv SHA-256
  c73a16ca22deceac2bf5e7129b39a604808a95cd3c2917f4524e0ec324f9bbf1.

- 2026-09-08T13:43:53+00:00: Paused checkpoint on exact base
  9feeba6524357df38e3ad118d4c3740306d3ec8e. Dirty paths: crates/asb-replay/src/lib.rs plus untracked
  crates/asb-replay/src/selection.rs. Delta authenticates cassette roots, indexes explicit
  profile-digest+agent compatibility metadata, offers deterministic recording identities, and
  requires explicit replay or live choice with no fallback. No live connection or credential
  resolver mutation. Focused cargo test exited 101 at compile time because the new test fixture
  incorrectly supplied nonexistent PolicyVersion.name; product code did not run. Preserve unchanged
  until dependency update.

- 2026-09-08T13:45:01+00:00: Paused safely: replay/catalog skeleton remains in declared worktree;
  live provider path is fenced on new AR-0318. Release lane so credential boundary can be
  implemented.

- 2026-09-08T14:04:53+00:00: Claimed by quality_20260906.

- 2026-09-08T14:06:33+00:00: Recorded command exit 101; command argv SHA-256
  6dab8e4e0daf4974e48901fca9cc72f1bf8ff91dd686f51563d8bab821fa6621.

- 2026-09-08T14:06:41+00:00: No durable progress after repeated follow-ups; preserve the dirty
  replay/catalog skeleton and exact fixture blocker. Release lane so the worker can implement ready
  AR-0319; AR-0314 may be reclaimed only after fixture repair is explicitly resumed.

- 2026-09-08T14:08:52+00:00: Claimed by quality_20260906.

- 2026-09-08T14:10:07+00:00: Recorded command exit 0; command argv SHA-256
  6dab8e4e0daf4974e48901fca9cc72f1bf8ff91dd686f51563d8bab821fa6621.

- 2026-09-08T14:10:26+00:00: Repeated resumed exit-101 with no diagnosis or fixture repair; preserve
  dirty replay/catalog worktree and exact blocker. Release inactive claim; reclaim only when the
  worker can execute the configured focused repair.

- 2026-09-08T14:10:44+00:00: Claimed by quality_20260906.

- 2026-09-08T14:11:17+00:00: Recorded command exit 0; command argv SHA-256
  8a803dfb909dc49c7612fd844c26acb22183a1ad25b95968a1c216df5195aab8.

- 2026-09-08T14:11:34+00:00: Recorded command exit 1; command argv SHA-256
  88269d845a2046ad64b2c694950c00b7ab16306d67dc00a68bce73eff1a10503.

- 2026-09-08T14:11:56+00:00: Recorded command exit 0; command argv SHA-256
  2a4eb6c36536e5d4e6ac0992765200db3691f7f949ecbad0242c5c1314247498.

- 2026-09-08T14:12:17+00:00: Recorded command exit 0; command argv SHA-256
  b48cc76e7ac9d219bd6861d0b04197eab850ef2118bd50b8dd9aff8abde90752.

- 2026-09-08T14:12:31+00:00: Recorded command exit 0; command argv SHA-256
  2b20d5d109f4e99d2b8b709894f603031aeb40a1bbeec481fd55a460de6e1e0b.

- 2026-09-08T14:12:55+00:00: Signed checkpoint 1d0e521 has clean two-path scope and green wrapped
  focused selection tests. It implements deterministic compatible recording offers and explicit
  replay/live source choice; live preflight remains to be independently verified against AR-0318
  environment credentials.

- 2026-09-08T14:14:11+00:00: Coordinator independently ran cargo test --locked -p asb-replay on
  signed 1d0e521: 91 tests passed across unit, cassette, fault, migration, pacing, redaction,
  schema, strict-replay, and Gemini suites. Replay/source-choice behavior is validated; live
  preflight remains open.

- 2026-09-08T14:15:56+00:00: Live-preflight integration audit on AR-0314 candidate 1d0e521:
  origin/main remains 9feeba652 and does not contain AR-0318 source commit e9a0e523 (merge-base
  --is-ancestor exit 1); AR-0314 branch likewise has no crates/asb-agents/src/credential.rs.
  Therefore no AR-0318 environment resolver is available on the exact candidate tree, and claiming a
  live preflight would be false. The independently reported asb-replay 91/91 suite remains green.
  Exact blocker is missing product integration of the released dependency, not credential lookup or
  provider behavior.

- 2026-09-08T14:16:57+00:00: Exact blocker proven: AR-0318 resolver commit is not integrated into
  product main or AR-0314 candidate. Preserve clean AR-0314 checkpoint; unblock only after AR-0320
  product integration, then rebase and run synthetic environment preflight.

- 2026-09-08T14:38:22+00:00: AR-0320 is released and integrated on product main at 33f30cb; all
  AR-0314 dependencies are done. Resume for synthetic environment-credential live preflight;
  FD/helper remain AR-0319.

- 2026-09-08T14:38:25+00:00: Claimed by quality_20260906.

- 2026-09-08T14:39:03+00:00: Recorded command exit 0; command argv SHA-256
  0c94026d9284715e03150d90095b28985dfe5b4abfda01cab97c907552ba993d.

- 2026-09-08T14:39:57+00:00: Recorded command exit 0; command argv SHA-256
  80ac37f620247324501966a720dcb8e3ac3a575c429172af7ff1cbc71c96097e.

- 2026-09-08T14:40:14+00:00: Recorded command exit 0; command argv SHA-256
  6dab8e4e0daf4974e48901fca9cc72f1bf8ff91dd686f51563d8bab821fa6621.

- 2026-09-08T14:40:30+00:00: Recorded command exit 0; command argv SHA-256
  8a803dfb909dc49c7612fd844c26acb22183a1ad25b95968a1c216df5195aab8.

- 2026-09-08T14:40:48+00:00: Recorded command exit 0; command argv SHA-256
  c317b7c24375fb096a27f342a5aea63d10a04794ef494f405b6613ae6a03e57a.

- 2026-09-08T14:41:27+00:00: Recorded command exit 0; command argv SHA-256
  75b9166da42e3d26765d8da9ac5616a0f7c9e543f86874f4e974cf21485c9115.

- 2026-09-08T14:41:48+00:00: Recorded command exit 0; command argv SHA-256
  e7203f64cfdd6c3f1176bfc9d5de4a05334173ce00588d5a8b8b7b3f5cbf7a82.

- 2026-09-08T14:42:03+00:00: Recorded command exit 0; command argv SHA-256
  9fd74b467579068b070ad3aa26ba36ff5a812841a7deb24dfcbf6bb6d20f6577.

- 2026-09-08T14:42:18+00:00: Recorded command exit 0; command argv SHA-256
  a84711d4adba925bc749e7a734d54c56aa9b592ebe204fa9d99b417bc18a4df2.

- 2026-09-08T14:42:52+00:00: AR-0314 controlled rebase complete: old 1d0e521 -> signed
  e8fed7e572b6bf9d14d76f15b91b7cb208e2d48b on exact main 33f30cb; range-diff is = and worktree
  clean. Exact-tree synthetic Environment credential preflight test passed 1/1: non-secret reference
  digest is verified, resolved synthetic credential is injected into an otherwise empty bounded
  child environment, output contains only `isolated`, and no credential bytes are emitted. FD/helper
  remain unsupported. Selection focused tests passed 4/4; explicit live/replay choice, unavailable
  live, mismatched recording/profile/agent, forged/duplicate cassette, malformed/bounded inputs all
  fail closed. Full locked workspace test, fmt, workspace all-target clippy -D warnings, repository
  policy exact range, DCO exact range, and Gitleaks one-commit 13.34KB/no-leaks are green.
  Candidate: tree 4ef17ad010f067e6d87409727cbb098bfb8328a3, parent
  33f30cb7d88aa8d3c323895154c8237d1763c6b8, exact two-path replay scope.
