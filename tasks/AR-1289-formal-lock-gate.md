---
{
  "branch": "fix/ar-1289-formal-lock-gate",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-17T05:17:44+00:00",
  "depends_on": [],
  "id": "AR-1289",
  "next_action": "Policy check 35177646319 failed only on pre-existing Gemini timing assertion; exact targeted test passed 3/3 locally. Failed hosted job rerun requested once; monitor rerun plus remaining required checks, merge only if all terminal-success.",
  "observed_branch": "fix/ar-1289-formal-lock-gate",
  "observed_dirty": 0,
  "observed_head": "53981d651645594a65aa7e69c9faa28e0770b6a6",
  "owner": "asb_ar1024_lifecycle_router",
  "plan": "../plans/AR-1289.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Repair the stale formal Cargo.lock required by hosted exact-head gates.",
  "task_revision": 39,
  "title": "Repair formal lock gate",
  "updated_at": "2026-09-17T03:27:33+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1289-formal-lock-gate"
}
---

## AR-1289

The required formal workflow currently fails before model tests because `formal/Cargo.lock` cannot
be used with `--locked`. Repair and verify this gate independently of feature ARs.

- 2026-09-17T03:12:39+00:00: Hosted exact-head formal job fails because formal/Cargo.lock is stale
  under --locked; repair independently of certificate feature.

- 2026-09-17T03:13:06+00:00: Claimed by asb_ar1024_lifecycle_router.

- 2026-09-17T03:13:22+00:00: Recorded command exit 0; command argv SHA-256
  5345cd4b5f66285dc80cddfe59c0a95475263f9ff88d25d2639fce3c300aa4b9.

- 2026-09-17T03:13:31+00:00: Recorded command exit 0; command argv SHA-256
  d0f0b52a0a5d46ebd4657c74ecbcbb904e0df02a72c4b192d4e9d74ecd6c4182.

- 2026-09-17T03:13:50+00:00: Heartbeat by asb_ar1024_lifecycle_router.

- 2026-09-17T03:14:06+00:00: Recorded command exit 101; command argv SHA-256
  7a92628b9c4db3b74a33f295f28b9b6f3786588dca51c09e12ba3282f2d2a9a2.

- 2026-09-17T03:14:24+00:00: Recorded command exit 0; command argv SHA-256
  fd4fe86de1f65ae1bf0c3c1dd2bf5e9211b2f05e99214a0f2b49ebabaae38d5b.

- 2026-09-17T03:14:45+00:00: Recorded command exit 0; command argv SHA-256
  9adc44b444f054489317aa8684e89eb22e667aea82b7d3fef5cd1953f30e30e3.

- 2026-09-17T03:14:55+00:00: Recorded command exit 1; command argv SHA-256
  833589edbbd6874476e9054b21cee2126187a6d470720f489715466b712a3948.

- 2026-09-17T03:15:14+00:00: Recorded command exit 0; command argv SHA-256
  7a92628b9c4db3b74a33f295f28b9b6f3786588dca51c09e12ba3282f2d2a9a2.

- 2026-09-17T03:15:40+00:00: Recorded command exit 0; command argv SHA-256
  b1030dbf9249e68f88a9d27bc718eafbb1f811430573c4a9f17d3483c0531df9.

- 2026-09-17T03:15:48+00:00: Recorded command exit 0; command argv SHA-256
  8b04d9f94f406362c0ec0821546b3ba121711de8bffa18560b3aa5d08d740899.

- 2026-09-17T03:16:11+00:00: Reproduced protected-main formal command: test suite runs but one
  bounded acquisition test intermittently fails with Os code 26 Text file busy; isolated rerun
  passes. cargo generate-lockfile on clean formal manifest produced the exact 40-line dependency
  checksum/version drift (cfg-if, syn, smallvec, synstructure, unicode-ident, yoke, zerofrom and
  related edges). Committed only formal/Cargo.lock as signed+DCO 53981d6. Post-repair cargo test
  --locked --manifest-path formal/Cargo.toml passes all formal suites; worktree clean.

- 2026-09-17T03:17:44+00:00: Heartbeat by asb_ar1024_lifecycle_router.

- 2026-09-17T03:17:48+00:00: Recorded command exit 0; command argv SHA-256
  d0a5e846cbf7e93e7e352a50e451c7f65309da71dd2355e1235faa7590287a38.

- 2026-09-17T03:18:01+00:00: Recorded command exit 0; command argv SHA-256
  d16b14aa60e6b53cb3b5278800b899c6f9ae40263627e889b039fdfa02d89456.

- 2026-09-17T03:18:22+00:00: Recorded command exit 0; command argv SHA-256
  f29e7ba2c9d9f11ea861bbabff757f5c1ebb8175ffd67e0964855c76398523ba.

- 2026-09-17T03:18:47+00:00: Published exact signed/DCO lock-only repair 53981d6 via branch
  fix/ar-1289-formal-lock-gate. PR #211:
  https://github.com/martin-beck/agent-systems-benchmark/pull/211, base 2fd90557, head
  53981d651645594a65aa7e69c9faa28e0770b6a6. Hosted checks started: formal 35177646338, Rust
  35177646365, repository quality 35177646319, fault 35177646341, AArch64 35177646317, hosted
  portability 35177646355, headers 35177646353 (headers and AWQ already SUCCESS; remaining checks
  IN_PROGRESS). Worktree clean.

- 2026-09-17T03:21:21+00:00: Recorded command exit 8; command argv SHA-256
  59ca2401805672391e4e7b342b7a52f01024b9e3280136bf92a85c6f1e5222dc.

- 2026-09-17T03:22:07+00:00: Recorded command exit 8; command argv SHA-256
  59ca2401805672391e4e7b342b7a52f01024b9e3280136bf92a85c6f1e5222dc.

- 2026-09-17T03:22:18+00:00: Recorded command exit 1; command argv SHA-256
  59ca2401805672391e4e7b342b7a52f01024b9e3280136bf92a85c6f1e5222dc.

- 2026-09-17T03:22:38+00:00: Recorded command exit 0; command argv SHA-256
  e6a2ce31e23ef87d7f78637217e4ce7c7568d723c9a039ee1ab16083a78c0408.

- 2026-09-17T03:23:07+00:00: Recorded command exit 0; command argv SHA-256
  698d93a862d1e85200b53f785a4b6cb50ecd8491d152917de86e1c8a891d6537.

- 2026-09-17T03:23:18+00:00: Recorded command exit 0; command argv SHA-256
  698d93a862d1e85200b53f785a4b6cb50ecd8491d152917de86e1c8a891d6537.

- 2026-09-17T03:23:35+00:00: Recorded command exit 0; command argv SHA-256
  698d93a862d1e85200b53f785a4b6cb50ecd8491d152917de86e1c8a891d6537.

- 2026-09-17T03:23:54+00:00: Recorded command exit 0; command argv SHA-256
  fecdbd7127c878562df77c452fc1e5086eb738a97698d06c1491030241f35951.

- 2026-09-17T03:24:17+00:00: Diagnosed hosted Repository quality failure: coverage test ran 172
  passed/1 ignored and failed gemini::tests::malformed_ready_marker_fails_fast_and_cleans_run_root
  at assertion started.elapsed() < 1s. The lock-only diff does not touch Gemini. Exact targeted
  cargo test on clean 53981d6 passed 3/3 consecutive runs (0.04s, 0.04s, 0.03s); classify as runner
  timing flake under coverage instrumentation. Requested one controlled rerun of failed workflow
  35177646319 via gh run rerun --failed; no product changes.

- 2026-09-17T03:24:24+00:00: Recorded command exit 8; command argv SHA-256
  59ca2401805672391e4e7b342b7a52f01024b9e3280136bf92a85c6f1e5222dc.

- 2026-09-17T03:25:09+00:00: Recorded command exit 8; command argv SHA-256
  59ca2401805672391e4e7b342b7a52f01024b9e3280136bf92a85c6f1e5222dc.

- 2026-09-17T03:25:18+00:00: Recorded command exit 8; command argv SHA-256
  59ca2401805672391e4e7b342b7a52f01024b9e3280136bf92a85c6f1e5222dc.

- 2026-09-17T03:26:04+00:00: Recorded command exit 8; command argv SHA-256
  59ca2401805672391e4e7b342b7a52f01024b9e3280136bf92a85c6f1e5222dc.

- 2026-09-17T03:26:14+00:00: Recorded command exit 8; command argv SHA-256
  59ca2401805672391e4e7b342b7a52f01024b9e3280136bf92a85c6f1e5222dc.

- 2026-09-17T03:26:27+00:00: Recorded command exit 0; command argv SHA-256
  75a306d0a0e4d07e4161808e5cd5a8e0cab1a971ca1892b917b07f6f57b8733f.

- 2026-09-17T03:27:16+00:00: Recorded command exit 0; command argv SHA-256
  8255d955fd18dc0494dac132d038c7568c9e65312f1410c6e92335cedd383124.

- 2026-09-17T03:27:33+00:00: Recorded command exit 8; command argv SHA-256
  59ca2401805672391e4e7b342b7a52f01024b9e3280136bf92a85c6f1e5222dc.
