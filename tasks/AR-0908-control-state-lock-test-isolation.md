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
  "next_action": "Hold successor 8b0f9fd for fresh independent immutable review; publish only after approval.",
  "observed_branch": "fix/control-state-lock-test-isolation",
  "observed_dirty": 0,
  "observed_head": "8b0f9fd07d5dfbedd83376c1380ab225dfba1213",
  "owner": "contracts_20260906",
  "plan": "../plans/AR-0908.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Harden asb-cli control-state lock test isolation and deterministic reopen coverage.",
  "task_revision": 40,
  "title": "Harden control-state lock test isolation",
  "updated_at": "2026-09-09T20:27:14+00:00",
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

- 2026-09-09T20:09:17+00:00: Recorded command exit 0; command argv SHA-256
  fbe9860580ae2c293d9279c7203a211a5f98ee9147133a1eb8886dc7ccecda81.

- 2026-09-09T20:10:10+00:00: Recorded command exit 0; command argv SHA-256
  e22cf53d7f62b7d7682d13b2cc9df8b500e36207fed15521589cb74dab2040e0.

- 2026-09-09T20:10:37+00:00: Recorded command exit 0; command argv SHA-256
  e1c9b197831a90273213545ab2fe1f95a07c00fa799dda354a29674d78b28cbb.

- 2026-09-09T20:11:07+00:00: Immutable candidate f7a08f98743643c1fa855a19ebe3a1f3211c5f05, tree
  a9484d622d8d487ccb1ef85fdc52b671dd4d2c77, exact parent b6d04a8305ce6d49cc327e4e6d2d6fa42a88050b.
  Scope is exactly crates/asb-cli/src/control.rs within cfg(test); production locking is unchanged.
  Atomic unique 0700 external roots validate absolute canonical non-symlink base,
  ownership/mode/repository disjointness, bound collisions, and retain an open directory identity so
  substituted cleanup paths are not removed. Hostile test covers relative/file/symlinked bases,
  stale collision preservation, leaf symlink preservation, wrong owner, public mode, and path
  substitution. Focused 14/14; parallel stress 30x14=420; exact coverage gate green (workspace and
  critical floors), with 31/31 asb-cli library tests and 87.49% lines in the earlier focused
  coverage context. Full locked workspace fmt, all-target clippy -D warnings, tests, rustdoc, and
  release build green; contracts/schema, failure-path/artifact, deny/audit, exact-range repository
  policy, signature/DCO, Gitleaks, diff/privacy/scope/clean checks green. One new hostile test
  initially exposed inode reuse in dev/inode-only cleanup; repaired by retaining an open directory
  handle and focused suite then passed. Earlier policy exit scanned full history because base was
  omitted; earlier contract exit used symbolic rather than exact baseline; corrected exact-range
  invocations passed.

- 2026-09-09T20:18:50+00:00: Recorded command exit 0; command argv SHA-256
  742ecacbec9a75e4066ef65c6919d03997e80131eb4ef0925a69dab15d800168.

- 2026-09-09T20:19:50+00:00: Recorded command exit 0; command argv SHA-256
  206d63eb4809b936e7874d445e9aeb46f208ea70ebb4fbf8e7839ea05abd4368.

- 2026-09-09T20:20:58+00:00: Recorded command exit 0; command argv SHA-256
  ac43eebca735b7f57287c673c11e156eb9978e34da2ca7ecd5b5d42ed7882c24.

- 2026-09-09T20:22:52+00:00: Recorded command exit 0; command argv SHA-256
  0f71ae5783b2fb724c90138a440d92c80fa172a5cc949ef863dadb7ded710ef2.

- 2026-09-09T20:23:35+00:00: Recorded command exit 0; command argv SHA-256
  c5a5d17fa1cad4473d544af54fabc10e2e7c0d32c1ae8f8f4af89ecc6628cd2d.

- 2026-09-09T20:24:04+00:00: Recorded command exit 0; command argv SHA-256
  26cafe5973eebd904304fd6a6d09e626e29f0c102a53abc3121bba052da94571.

- 2026-09-09T20:24:32+00:00: Independent-review repair successor
  8b0f9fd07d5dfbedd83376c1380ab225dfba1213, tree 178f6fe26c1a3f6689367a33a017bd12b6af7018, parent
  f7a08f98743643c1fa855a19ebe3a1f3211c5f05; aggregate exact base
  b6d04a8305ce6d49cc327e4e6d2d6fa42a88050b and one-path cfg(test) scope. Repository overlap now
  binds the canonical workspace root, not the crate directory. Bases are opened
  O_DIRECTORY|O_NOFOLLOW and accepted only as current-UID non-group/world-writable or owner/root
  sticky directories. Root creation uses retained base fd through /proc/self/fd; cleanup walks
  retained directory fds with no-follow opens and only removes an empty root after rechecking it
  against the held identity. Synchronized hooks prove an ancestor swap to the workspace still
  creates under the retained original base, and a replacement between cleanup validation and
  deletion remains intact. Hostile policy negatives cover workspace sibling, unsafe 0777 base and
  accepted sticky boundary. Repaired focused 14/14 and Clippy pass; 30x14 parallel stress passes;
  exact workspace/critical coverage passes; full locked workspace fmt, Clippy, tests, rustdoc,
  release, contract/schema, failure/artifact, deny/audit pass. Both commits SSH-signed+DCO;
  aggregate exact-range policy/Gitleaks/diff/privacy/scope and clean tree pass.

- 2026-09-09T20:27:14+00:00: Recorded command exit 0; command argv SHA-256
  3dd4b53be6f2c03bc99d28c4064f2427fadccc60eecf5462e2696404e769df78.
