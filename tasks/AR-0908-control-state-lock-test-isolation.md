---
{
  "branch": "fix/control-state-lock-test-isolation",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-09T22:41:04+00:00",
  "depends_on": [
    "AR-0101",
    "AR-0102",
    "AR-0103",
    "AR-0875"
  ],
  "id": "AR-0908",
  "next_action": "Run remaining exact one-path and full gates, then prepare signed immutable candidate.",
  "observed_branch": "fix/control-state-lock-test-isolation",
  "observed_dirty": 1,
  "observed_head": "b6d04a8305ce6d49cc327e4e6d2d6fa42a88050b",
  "owner": "contracts_20260906",
  "plan": "../plans/AR-0908.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Harden asb-cli control-state lock test isolation and deterministic reopen coverage.",
  "task_revision": 25,
  "title": "Harden control-state lock test isolation",
  "updated_at": "2026-09-09T20:08:04+00:00",
  "worktree_key": "agent-systems-benchmark-control-state-lock-test-isolation"
}
---
## AR-0908

Repair the isolated `asb-cli` control-state ownership test boundary exposed by Repository Quality
run 34339927858. The observed failure occurred when reopening after dropping the original backend;
an unchanged focused test subsequently passed repeatedly, so preserve the incident as a
non-deterministic isolation signal rather than claiming a production lock defect without evidence.


- 2026-09-09T19:39:36+00:00: Dependencies AR-0101, AR-0102, AR-0103 and AR-0875 are durably done;
  focused embedded-test-only scope is disjoint from active product lanes.

- 2026-09-09T19:41:04+00:00: Claimed by contracts_20260906.

- 2026-09-09T19:41:27+00:00: Recorded command exit 0; command argv SHA-256
  5345cd4b5f66285dc80cddfe59c0a95475263f9ff88d25d2639fce3c300aa4b9.

- 2026-09-09T19:42:01+00:00: Recorded command exit 1; command argv SHA-256
  63c858d759cea8e2caca2e0c4088189d3f96da31efdb75cb6464ce4089512f2c.

- 2026-09-09T19:42:09+00:00: Recorded command exit 0; command argv SHA-256
  caa327f26dd36c9e407005cb01b02437839c9536e8fb16c21879afe7fb919e11.

- 2026-09-09T19:43:44+00:00: Recorded command exit 2; command argv SHA-256
  9cebae8c9699f439675941aafd58f8f653f68112d085f17a4667aac6160c1d36.

- 2026-09-09T19:45:28+00:00: Recorded command exit 1; command argv SHA-256
  57e589deb899e438076d3362e4988e6c1c14b89a24e412f4f10b6e8f489c5bc4.

- 2026-09-09T19:45:47+00:00: Recorded command exit 1; command argv SHA-256
  5e44b86fdc808a33319c6fe8aa5032fb7baff44dcbb71ec780cdbb39182deb93.

- 2026-09-09T19:46:03+00:00: Recorded command exit 0; command argv SHA-256
  17afb6ac79fa2a87a18e862caf84751f345025b2e5d1a2b30b669e887c88b9c7.

- 2026-09-09T19:46:44+00:00: Recorded command exit 101; command argv SHA-256
  0da34342d3204b6b2934633dff1edfe4f810ae0be87037f95a0702e3d14e6c37.

- 2026-09-09T19:47:41+00:00: Recorded command exit 0; command argv SHA-256
  17afb6ac79fa2a87a18e862caf84751f345025b2e5d1a2b30b669e887c88b9c7.

- 2026-09-09T19:48:01+00:00: Recorded command exit 0; command argv SHA-256
  f8cf86a4aa31d5c9a33125cfd658365f041d5a32bb5c094ce7a5c405cc3246f3.

- 2026-09-09T19:48:34+00:00: First substantive checkpoint: source audit located the observed failure
  at post-drop reopen. Existing recursive PID/sequence roots could reuse stale paths. Embedded tests
  now use canonical symlink-free external bases, atomic bounded create-new 0700 owner-bound leaves,
  device/inode-aware cleanup, and hostile parent-symlink/collision/wrong-owner/public-mode
  negatives. Focused control suite passes 14/14. Earlier exit 1 was an accidental invalid git
  subcommand with no product effect; the first compile exit 101 correctly exposed an unused test
  import and was resolved by adding the intended hostile test.

- 2026-09-09T19:58:54+00:00: Recorded command exit 0; command argv SHA-256
  7c12eef00d06fb1af4b8b5f4349d8e3729e511bd0814d0c19e9fe9a65922a5a1.

- 2026-09-09T19:59:51+00:00: Recorded command exit 101; command argv SHA-256
  47971602f2ef867a877c59579371b437f0b09dacaa5d2fadf2677d8b34e7f0f7.

- 2026-09-09T20:01:32+00:00: Coverage checkpoint without rerun: corrected stable cargo-llvm-cov
  invocation completed 31/31 asb-cli lib tests with 87.49% total line coverage and 82.59% control.rs
  line coverage. The prior --branch attempt failed only because stable Rust rejects nightly -Z
  coverage options. Handoff recording of the successful run was initially blocked by expired
  AR-0859; coordinator repaired that unrelated lease at bfb04689. Parallel focused stress was
  already recorded exit 0: 30 runs x 14 tests = 420 passes.

- 2026-09-09T20:02:30+00:00: Recorded command exit 101; command argv SHA-256
  660a0cb43587dc519e51750e271f74529f861bb7761047222c4441f451ab6591.

- 2026-09-09T20:03:47+00:00: Recorded command exit 0; command argv SHA-256
  e98b48f0ba9b12fe7c0739f8c6b62cee00827dc554a04bf586b8d7c93cc7ab27.

- 2026-09-09T20:05:11+00:00: Recorded command exit 0; command argv SHA-256
  30c399f30331e7fbebadc015bcfb6093dd8d9d4ed414b08707b89dd994d3d74c.

- 2026-09-09T20:06:59+00:00: Recorded command exit 0; command argv SHA-256
  ac43eebca735b7f57287c673c11e156eb9978e34da2ca7ecd5b5d42ed7882c24.

- 2026-09-09T20:07:42+00:00: Recorded command exit 1; command argv SHA-256
  1444a30fc6cece039ddc01e0a79e22f58e37cc5ef9c48063a02d066a9f272f7b.

- 2026-09-09T20:08:04+00:00: Recorded command exit 1; command argv SHA-256
  bb5717d4f2fa088fbccee362a286b93b4d560c4e295e3d80d7d6d922ae50c529.
