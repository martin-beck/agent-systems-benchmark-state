---
{
  "branch": "feature/ar-1783-installed-workload-selection-and-execution",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1763",
    "AR-1764",
    "AR-1782"
  ],
  "id": "AR-1783",
  "next_action": "Wait for all ca494d50 protected-main post-merge workflows terminal green, record exact-main receipts, then accept and release AR-1783",
  "observed_branch": "feature/ar-1783-installed-workload-selection-and-execution",
  "observed_dirty": 0,
  "observed_head": "aca3f79b3256729543e93cc321ce3a85daa78051",
  "owner": "",
  "plan": "../plans/AR-1783-installed-workload-selection-and-execution.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "hosted",
    "evidence_digest": "sha256:f2d6c53370f84bcc31cb3fe9cbd6565f81f038c8e47375ec01ad5735dc174e19",
    "evidence_ref": "protected-main:ca494d506135c4a3263bea21621dcc97d817614c",
    "spec_ref": "specs/AR-1783.json",
    "spec_revision": 2,
    "status": "pass"
  },
  "spec_ref": "specs/AR-1783.json",
  "spec_revision": 2,
  "status": "done",
  "summary": "PR #596 locally integrated as signed/DCO protected-main merge ca494d50; exact remote main now points to it and post-merge workflows are running",
  "task_revision": 274,
  "title": "Installed workload selection and execution",
  "updated_at": "2026-10-12T01:59:18+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1783-installed-workload-selection-and-execution"
}
---

Make generated project catalogs and run/sweep consume the dedicated `asb workload`
records. Selection validates the installed workload's exact catalog revision,
identity, digest, license/terms compatibility, preparation state, adapter
version, and resource/platform requirements. Execution binds this identity into
the plan/run/record/report/compare evidence and rejects ambient, stale, revoked,
missing, incompatible, or manually substituted workload directories before a run
starts. Cover every AR-1781 workload ID—including SWE-mini—through a fresh
project's install, selection, bounded run and sweep, report, and comparison
journey. Development runs may use a controlled local/development backend where
needed; lack of production authorization or hosted qualification must not block
the suite from this end-to-end path.

- 2026-10-12T00:00:59+00:00: Dependencies are now complete; open AR-1783 for implementation.

- 2026-10-12T00:00:59+00:00: Claimed by ar1783_workload_selection_luna56.

- 2026-10-12T00:01:58+00:00: Recorded command exit 0; command argv SHA-256
  ff6d1fa7a7185010f75fcfafe4bdc1bdd5b9804d8c2b3e7abdd8a1b96cd81c63.

- 2026-10-12T00:04:04+00:00: Recorded command exit 0; command argv SHA-256
  665c8e3f3b5ce28b9d9834c286a1da3f3e4189b3cfd5796fc061ff512c2e5c79.

- 2026-10-12T00:04:13+00:00: Recorded command exit 1; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-10-12T00:04:20+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-12T00:04:48+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-12T00:04:54+00:00: Recorded command exit 0; command argv SHA-256
  665c8e3f3b5ce28b9d9834c286a1da3f3e4189b3cfd5796fc061ff512c2e5c79.

- 2026-10-12T00:05:30+00:00: Recorded command exit 0; command argv SHA-256
  7176a4996c16f289722a1ef4fdd225749fc51f58c34b0fcfb9c0f5689d2ab4a6.

- 2026-10-12T00:05:51+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-12T00:06:16+00:00: Recorded command exit 101; command argv SHA-256
  665c8e3f3b5ce28b9d9834c286a1da3f3e4189b3cfd5796fc061ff512c2e5c79.

- 2026-10-12T00:06:29+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-12T00:06:35+00:00: Recorded command exit 0; command argv SHA-256
  665c8e3f3b5ce28b9d9834c286a1da3f3e4189b3cfd5796fc061ff512c2e5c79.

- 2026-10-12T00:07:03+00:00: Recorded command exit 0; command argv SHA-256
  a1f8aedb7512b2eee19aac363063c66eb8c928cc3ddea4e50326dc00d77d230f.

- 2026-10-12T00:07:06+00:00: Recorded command exit 0; command argv SHA-256
  bb06a585a3c5274ee01d31c6141787822697874b6d86e64cee19e848885fea39.

- 2026-10-12T00:07:47+00:00: Recorded command exit 0; command argv SHA-256
  653ce9b81a4efbec43e5a667e890163176daab33a0f0336a5ce142c465f3afda.

- 2026-10-12T00:08:26+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-10-12T00:08:38+00:00: Recorded command exit 0; command argv SHA-256
  1024fc1e6cefa31b078f0b5d2ed85c7ea4586897b388bf1e308f62db58574461.

- 2026-10-12T00:09:29+00:00: Recorded command exit 0; command argv SHA-256
  fcd17480931a7c27121bea1a4b4cdf0263b22a8542f304a02b7fe3a5e06895df.

- 2026-10-12T00:09:40+00:00: Recorded command exit 0; command argv SHA-256
  2b1df63588adb427fc39c1cbbd05c1a633463dbf8b7315eee8dd189e47a45e1b.

- 2026-10-12T00:09:54+00:00: Recorded command exit 8; command argv SHA-256
  727ddf13cb9240da38da2754474c98f8fc0df5748ca22dce8b74ff3a03d4452b.

- 2026-10-12T00:10:03+00:00: Recorded command exit 8; command argv SHA-256
  727ddf13cb9240da38da2754474c98f8fc0df5748ca22dce8b74ff3a03d4452b.

- 2026-10-12T00:10:13+00:00: Recorded command exit 101; command argv SHA-256
  7b80382008cb01e3ea6fa6e88054b624464f9801b40ed57f947b01892a686ae8.

- 2026-10-12T00:10:43+00:00: Recorded command exit 8; command argv SHA-256
  727ddf13cb9240da38da2754474c98f8fc0df5748ca22dce8b74ff3a03d4452b.

- 2026-10-12T00:10:46+00:00: Recorded command exit 8; command argv SHA-256
  727ddf13cb9240da38da2754474c98f8fc0df5748ca22dce8b74ff3a03d4452b.

- 2026-10-12T00:11:28+00:00: Recorded command exit 8; command argv SHA-256
  727ddf13cb9240da38da2754474c98f8fc0df5748ca22dce8b74ff3a03d4452b.

- 2026-10-12T00:11:47+00:00: Recorded command exit 8; command argv SHA-256
  727ddf13cb9240da38da2754474c98f8fc0df5748ca22dce8b74ff3a03d4452b.

- 2026-10-12T00:11:50+00:00: Heartbeat by ar1783_workload_selection_luna56.

- 2026-10-12T00:11:56+00:00: Recorded command exit 8; command argv SHA-256
  727ddf13cb9240da38da2754474c98f8fc0df5748ca22dce8b74ff3a03d4452b.

- 2026-10-12T00:12:06+00:00: Recorded command exit 8; command argv SHA-256
  727ddf13cb9240da38da2754474c98f8fc0df5748ca22dce8b74ff3a03d4452b.

- 2026-10-12T00:12:15+00:00: Recorded command exit 0; command argv SHA-256
  a6b302213484dc6c49c3315a92e0115cf8b6e3452fb0d01b474027fe22086f16.

- 2026-10-12T00:12:25+00:00: Recorded command exit 1; command argv SHA-256
  727ddf13cb9240da38da2754474c98f8fc0df5748ca22dce8b74ff3a03d4452b.

- 2026-10-12T00:12:35+00:00: Recorded command exit 0; command argv SHA-256
  37bcfb4e5c77f7e275cb23e43251125e97fcbc29b2b687ff808872042d4e94f1.

- 2026-10-12T00:12:58+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-12T00:13:01+00:00: Recorded command exit 1; command argv SHA-256
  4fc90f37103bf41e22aac5d0234b31141b401ada4c8b6dc8d6a0181cf9502ad2.

- 2026-10-12T00:13:12+00:00: Recorded command exit 0; command argv SHA-256
  665c8e3f3b5ce28b9d9834c286a1da3f3e4189b3cfd5796fc061ff512c2e5c79.

- 2026-10-12T00:13:21+00:00: Recorded command exit 0; command argv SHA-256
  0ca500d01969eddb76c78415cf9bb0d0161afa9dee001b1e1e5192b0e2bac82f.

- 2026-10-12T00:13:24+00:00: Recorded command exit 0; command argv SHA-256
  eaa19eab230d4489499409e7f015c3f0d864d010f12353a338ea3db1c6043820.

- 2026-10-12T00:13:33+00:00: Recorded command exit 0; command argv SHA-256
  5910c431d6b0fd2583dc33666727341191a9a761fbeb1537cdf9dfb86e673820.

- 2026-10-12T00:13:41+00:00: Recorded command exit 8; command argv SHA-256
  727ddf13cb9240da38da2754474c98f8fc0df5748ca22dce8b74ff3a03d4452b.

- 2026-10-12T00:14:09+00:00: Recorded command exit 8; command argv SHA-256
  727ddf13cb9240da38da2754474c98f8fc0df5748ca22dce8b74ff3a03d4452b.

- 2026-10-12T00:14:45+00:00: Recorded command exit 8; command argv SHA-256
  727ddf13cb9240da38da2754474c98f8fc0df5748ca22dce8b74ff3a03d4452b.

- 2026-10-12T00:15:18+00:00: Recorded command exit 8; command argv SHA-256
  727ddf13cb9240da38da2754474c98f8fc0df5748ca22dce8b74ff3a03d4452b.

- 2026-10-12T00:15:51+00:00: Recorded command exit 1; command argv SHA-256
  727ddf13cb9240da38da2754474c98f8fc0df5748ca22dce8b74ff3a03d4452b.

- 2026-10-12T00:16:01+00:00: Recorded command exit 0; command argv SHA-256
  aece175ae2e0f0631d4c1d5b36a4d777b8684da1661fa392b93ab4aac43b1001.

- 2026-10-12T00:16:29+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-12T00:16:36+00:00: Recorded command exit 0; command argv SHA-256
  665c8e3f3b5ce28b9d9834c286a1da3f3e4189b3cfd5796fc061ff512c2e5c79.

- 2026-10-12T00:16:41+00:00: Recorded command exit 0; command argv SHA-256
  a183d478a215b7aba5213fb1eef17e3e522776f4e8649154168c5e9235dda14a.

- 2026-10-12T00:16:50+00:00: Recorded command exit 0; command argv SHA-256
  0ca500d01969eddb76c78415cf9bb0d0161afa9dee001b1e1e5192b0e2bac82f.

- 2026-10-12T00:16:53+00:00: Recorded command exit 0; command argv SHA-256
  280f3a4d19ed00df3c24c283babc70f706e4e9a5f4104e1d16a10baaed64e052.

- 2026-10-12T00:16:59+00:00: Recorded command exit 0; command argv SHA-256
  5910c431d6b0fd2583dc33666727341191a9a761fbeb1537cdf9dfb86e673820.

- 2026-10-12T00:17:12+00:00: Recorded exact hosted failure and corrective commits 4dfb7a30,
  6ec4d6b1; focused regression rerun passes. Await exact-head CI green.

- 2026-10-12T00:17:18+00:00: Recorded command exit 8; command argv SHA-256
  727ddf13cb9240da38da2754474c98f8fc0df5748ca22dce8b74ff3a03d4452b.

- 2026-10-12T00:17:27+00:00: Recorded command exit 0; command argv SHA-256
  89ed04764830401a00b566c8a116320eaaccfcefbab6ca8943d868b219ac46ae.

- 2026-10-12T00:18:00+00:00: Recorded command exit 8; command argv SHA-256
  727ddf13cb9240da38da2754474c98f8fc0df5748ca22dce8b74ff3a03d4452b.

- 2026-10-12T00:18:33+00:00: Recorded command exit 8; command argv SHA-256
  727ddf13cb9240da38da2754474c98f8fc0df5748ca22dce8b74ff3a03d4452b.

- 2026-10-12T00:19:11+00:00: Recorded command exit 8; command argv SHA-256
  727ddf13cb9240da38da2754474c98f8fc0df5748ca22dce8b74ff3a03d4452b.

- 2026-10-12T00:19:27+00:00: Durable diagnosis for repeated exit 8: argv hash 727d... was not a
  product/CI failure; stderr identified oversized generated handoffctl.pyc. Subsequent commands use
  python3 -B and supported handoffctl state operations.

- 2026-10-12T00:19:33+00:00: Recorded command exit 8; command argv SHA-256
  727ddf13cb9240da38da2754474c98f8fc0df5748ca22dce8b74ff3a03d4452b.

- 2026-10-12T00:20:11+00:00: Recorded command exit 8; command argv SHA-256
  727ddf13cb9240da38da2754474c98f8fc0df5748ca22dce8b74ff3a03d4452b.

- 2026-10-12T00:20:14+00:00: Recorded command exit 8; command argv SHA-256
  727ddf13cb9240da38da2754474c98f8fc0df5748ca22dce8b74ff3a03d4452b.

- 2026-10-12T00:20:52+00:00: Recorded command exit 8; command argv SHA-256
  727ddf13cb9240da38da2754474c98f8fc0df5748ca22dce8b74ff3a03d4452b.

- 2026-10-12T00:20:56+00:00: Recorded command exit 8; command argv SHA-256
  727ddf13cb9240da38da2754474c98f8fc0df5748ca22dce8b74ff3a03d4452b.

- 2026-10-12T00:21:39+00:00: Recorded command exit 8; command argv SHA-256
  727ddf13cb9240da38da2754474c98f8fc0df5748ca22dce8b74ff3a03d4452b.

- 2026-10-12T00:21:39+00:00: Recorded command exit 8; command argv SHA-256
  727ddf13cb9240da38da2754474c98f8fc0df5748ca22dce8b74ff3a03d4452b.

- 2026-10-12T00:21:53+00:00: Exit 8 diagnosis at 00:20: gh pr checks returns exit 8 while required
  checks remain pending; stderr has no product failure. Current pending jobs are Emulated aarch64,
  Policy/coverage/supply chain, and Rust checks. Prior post-reconcile bytecode guard was separately
  recorded for argv 727d... .

- 2026-10-12T00:21:58+00:00: Recorded command exit 0; command argv SHA-256
  9ab20cc6c2b2c2a7159effe0afe4c2fadd47bdbf39b5ca740d93b7e80dbfd093.

- 2026-10-12T00:22:34+00:00: Recorded command exit 0; command argv SHA-256
  d28b2a8146b38abd5bbbbf2a1a8c8c67b518b767f5d83057e74d98abd66ac040.

- 2026-10-12T00:30:20+00:00: Recorded command exit 1; command argv SHA-256
  727ddf13cb9240da38da2754474c98f8fc0df5748ca22dce8b74ff3a03d4452b.

- 2026-10-12T00:30:25+00:00: Recorded command exit 0; command argv SHA-256
  b5e720dde32dcdf96ec75add0d9c0f1af114dbd0180b1f5bcc3eabd517bdf23a.

- 2026-10-12T00:30:36+00:00: Recorded command exit 0; command argv SHA-256
  c6c57a857003191644a333a37826326c4fc687bab4f8b9e5945a6d7631ea0585.

- 2026-10-12T00:30:42+00:00: Recorded command exit 0; command argv SHA-256
  cf09db9aa851c8ae31d35d15609e9290e491e1157901cc446a26ab3b42c7a2f0.

- 2026-10-12T00:30:51+00:00: Recorded command exit 0; command argv SHA-256
  c6c57a857003191644a333a37826326c4fc687bab4f8b9e5945a6d7631ea0585.

- 2026-10-12T00:35:06+00:00: Recorded command exit 1; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-10-12T00:35:12+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-12T00:35:23+00:00: Recorded command exit 101; command argv SHA-256
  a86bea17953c018685e58730f2b2fe7473eddab992651407c38ba7bdd28e01dc.

- 2026-10-12T00:35:44+00:00: Recorded command exit 0; command argv SHA-256
  a86bea17953c018685e58730f2b2fe7473eddab992651407c38ba7bdd28e01dc.

- 2026-10-12T00:35:54+00:00: Recorded command exit 0; command argv SHA-256
  665c8e3f3b5ce28b9d9834c286a1da3f3e4189b3cfd5796fc061ff512c2e5c79.

- 2026-10-12T00:36:03+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-10-12T00:36:16+00:00: Recorded command exit 0; command argv SHA-256
  83c44d23be69a7c6f4e3f8e3242d300b5a18d33226d9c7e4292659c6f8c07ed1.

- 2026-10-12T00:37:54+00:00: Recorded command exit 101; command argv SHA-256
  b8d5820028fe4789a64739b2fb6ea5e4523dbe05c2e5fdc7d462c465f26f0075.

- 2026-10-12T00:38:22+00:00: Recorded command exit 0; command argv SHA-256
  d6a4561800f8e79160f1f30891a3f07ef4351a4749925c2eb7c421e26b160fb0.

- 2026-10-12T00:38:26+00:00: Recorded command exit 0; command argv SHA-256
  628f05372b8ece1a0e9f4f1203db1b3b9c3ac0a79d1f239b9f55e2d349d3ef1f.

- 2026-10-12T00:38:33+00:00: Recorded command exit 0; command argv SHA-256
  32d00e7bea48deb591900624d4de1f837dadd9a3cd5c55c2ee1561f8660d7fe2.

- 2026-10-12T00:38:58+00:00: Concrete hosted failure repaired: PR #587 Rust run 38187409948/job
  114612678937 and Policy run 38187409894/job 114612676006 failed at
  crates/asb-cli/tests/diagnostic_contract.rs:554, ordinary_cli_producers_are_mechanically_closed,
  with every quarantined legacy producer needs a reviewed call-site identity; missing lib.rs
  identities began at lines 9104/9110/9138 and continued through the shifted legacy producers. The
  repeated exit 8 was gh pr checks pending status (and earlier generated handoffctl.pyc
  oversized-state guard), not a product test; no unchanged retry was used. Repair preserves strict
  matching: validation is bound through ProjectExecution::bind_plan, and AR-1783 adds exact reviewed
  identities for new/shifted project_run producers in diagnostic_legacy_catalog_compact.rs. Signed
  DCO product commit f4fe84a0 pushed to PR #587. Local evidence on exact tree: diagnostic_contract
  9/9 passed; project_run tests 3/3 passed; cargo fmt check passed; workspace clippy -D warnings
  passed; locked offline workspace tests completed without failure. Await hosted exact-head
  checks/review; PR remains open and AR remains in_progress.

- 2026-10-12T00:39:01+00:00: Recorded command exit 0; command argv SHA-256
  0f0120a9a80647761b7023e1aec09161f189badcb9a7de98b9ba33922d55f476.

- 2026-10-12T00:39:53+00:00: Recorded command exit 0; command argv SHA-256
  0f0120a9a80647761b7023e1aec09161f189badcb9a7de98b9ba33922d55f476.

- 2026-10-12T00:40:03+00:00: Recorded command exit 0; command argv SHA-256
  0f0120a9a80647761b7023e1aec09161f189badcb9a7de98b9ba33922d55f476.

- 2026-10-12T00:40:11+00:00: Recorded command exit 0; command argv SHA-256
  de9ade51a140deb8cf4423c49c95a94e4d05a1737777d1d766f9715f833fdf01.

- 2026-10-12T00:41:17+00:00: Recorded command exit 0; command argv SHA-256
  0f0120a9a80647761b7023e1aec09161f189badcb9a7de98b9ba33922d55f476.

- 2026-10-12T00:41:21+00:00: Recorded command exit 0; command argv SHA-256
  0f0120a9a80647761b7023e1aec09161f189badcb9a7de98b9ba33922d55f476.

- 2026-10-12T00:42:30+00:00: Recorded command exit 0; command argv SHA-256
  0f0120a9a80647761b7023e1aec09161f189badcb9a7de98b9ba33922d55f476.

- 2026-10-12T00:43:17+00:00: Heartbeat by ar1783_workload_selection_luna56.

- 2026-10-12T00:43:42+00:00: Recorded command exit 0; command argv SHA-256
  0f0120a9a80647761b7023e1aec09161f189badcb9a7de98b9ba33922d55f476.

- 2026-10-12T00:44:36+00:00: Recorded command exit 0; command argv SHA-256
  95c14b9abf735939b9e9324b41bf3e083d79848364d781f329a36049529e8387.

- 2026-10-12T00:44:42+00:00: Recorded command exit 0; command argv SHA-256
  a5e91d8a6e356ba88fd4835c765ebd2411c75eacaa60f98e203295ec257bd3a5.

- 2026-10-12T00:44:45+00:00: Recorded command exit 0; command argv SHA-256
  ba023e76fd42b3c6b5bf76d17e6c7e17983743eeab8e33fc02237242b77d8db4.

- 2026-10-12T00:44:52+00:00: Recorded command exit 0; command argv SHA-256
  32d00e7bea48deb591900624d4de1f837dadd9a3cd5c55c2ee1561f8660d7fe2.

- 2026-10-12T00:45:44+00:00: Follow-up hosted failure repaired without weakening gates: Rust
  workflow_transcript.rs:330 provenance_binds_the_exact_cli_and_public_fixture_sources reported
  crates/asb-cli/src/lib.rs expected cli_source_sha256
  9d31c6c777920a4effe956f031ca4775b4dff957b75fd5b846bf35d7c04ab61e but exact candidate computed
  c2501ffb436f5affb77c43341da235729c26a0c4eeb22d2724cd9ce203f96d27 after the reviewed AR-1783 source
  change. Updated docs/examples/asb-cli-workflow-v1.provenance.json to the computed exact source
  digest. Focused workflow_transcript test 3/3 passed. Signed DCO product commit e644f9b0 pushed to
  PR #587. The prior strict identity failure remains repaired with exact catalog entries; all local
  focused/full gates previously green. PR remains open pending hosted checks and independent
  exact-head review.

- 2026-10-12T00:45:46+00:00: Recorded command exit 0; command argv SHA-256
  0f0120a9a80647761b7023e1aec09161f189badcb9a7de98b9ba33922d55f476.

- 2026-10-12T00:46:56+00:00: Recorded command exit 0; command argv SHA-256
  0f0120a9a80647761b7023e1aec09161f189badcb9a7de98b9ba33922d55f476.

- 2026-10-12T00:47:34+00:00: Heartbeat by ar1783_workload_selection_luna56.

- 2026-10-12T00:47:36+00:00: Recorded command exit 0; command argv SHA-256
  0f0120a9a80647761b7023e1aec09161f189badcb9a7de98b9ba33922d55f476.

- 2026-10-12T00:48:16+00:00: Recorded command exit 0; command argv SHA-256
  0f0120a9a80647761b7023e1aec09161f189badcb9a7de98b9ba33922d55f476.

- 2026-10-12T00:48:29+00:00: Recorded command exit 0; command argv SHA-256
  0f0120a9a80647761b7023e1aec09161f189badcb9a7de98b9ba33922d55f476.

- 2026-10-12T00:49:06+00:00: Heartbeat by ar1783_workload_selection_luna56.

- 2026-10-12T00:49:07+00:00: Recorded command exit 0; command argv SHA-256
  0f0120a9a80647761b7023e1aec09161f189badcb9a7de98b9ba33922d55f476.

- 2026-10-12T00:49:14+00:00: Recorded command exit 0; command argv SHA-256
  6d4447c3a2ff59739c1940ca442dfe465d3971c5aa334916a1dc4d9a5033eba3.

- 2026-10-12T00:49:20+00:00: Recorded command exit 0; command argv SHA-256
  77bcc1e4809748d85585bb42d5c4457685a600b7d2c6e56705316844fc61e1b6.

- 2026-10-12T00:49:58+00:00: Recorded command exit 0; command argv SHA-256
  0f0120a9a80647761b7023e1aec09161f189badcb9a7de98b9ba33922d55f476.

- 2026-10-12T00:50:05+00:00: Recorded command exit 1; command argv SHA-256
  b8b87980497870a88b168bc1aaab94ba583ff0fd2de5d866ef27fb07c455488c.

- 2026-10-12T00:51:45+00:00: Heartbeat by ar1783_workload_selection_luna56.

- 2026-10-12T00:51:47+00:00: Recorded command exit 0; command argv SHA-256
  0f0120a9a80647761b7023e1aec09161f189badcb9a7de98b9ba33922d55f476.

- 2026-10-12T00:51:54+00:00: Recorded command exit 0; command argv SHA-256
  77bcc1e4809748d85585bb42d5c4457685a600b7d2c6e56705316844fc61e1b6.

- 2026-10-12T00:52:32+00:00: Recorded command exit 0; command argv SHA-256
  0f0120a9a80647761b7023e1aec09161f189badcb9a7de98b9ba33922d55f476.

- 2026-10-12T00:53:10+00:00: Heartbeat by ar1783_workload_selection_luna56.

- 2026-10-12T00:53:12+00:00: Recorded command exit 0; command argv SHA-256
  77bcc1e4809748d85585bb42d5c4457685a600b7d2c6e56705316844fc61e1b6.

- 2026-10-12T00:53:49+00:00: Recorded command exit 0; command argv SHA-256
  0f0120a9a80647761b7023e1aec09161f189badcb9a7de98b9ba33922d55f476.

- 2026-10-12T00:54:27+00:00: Recorded command exit 0; command argv SHA-256
  0f0120a9a80647761b7023e1aec09161f189badcb9a7de98b9ba33922d55f476.

- 2026-10-12T00:55:05+00:00: Recorded command exit 0; command argv SHA-256
  6d4447c3a2ff59739c1940ca442dfe465d3971c5aa334916a1dc4d9a5033eba3.

- 2026-10-12T00:55:41+00:00: Heartbeat by ar1783_workload_selection_luna56.

- 2026-10-12T00:55:42+00:00: Recorded command exit 0; command argv SHA-256
  0f0120a9a80647761b7023e1aec09161f189badcb9a7de98b9ba33922d55f476.

- 2026-10-12T00:56:22+00:00: Recorded command exit 0; command argv SHA-256
  0f0120a9a80647761b7023e1aec09161f189badcb9a7de98b9ba33922d55f476.

- 2026-10-12T00:57:00+00:00: Recorded command exit 0; command argv SHA-256
  6d4447c3a2ff59739c1940ca442dfe465d3971c5aa334916a1dc4d9a5033eba3.

- 2026-10-12T00:57:26+00:00: Terminal hosted evidence: PR #587 exact head
  e644f9b02c5b3f7d46b051691accc249fa8a3585. Rust checks succeeded at 00:55:20Z after Tests, Goose,
  documentation, workload parity, and release build; Policy/coverage/supply-chain succeeded at
  00:56:41Z after coverage floors, controlled-defect, diagnostic completeness, platform manifests,
  clean-tree, and optional evidence steps. Emulated AArch64 succeeded at 00:53:35Z; all other
  required checks (formal, faults, platform, credential-free, TUI, provenance, headers, AWQ)
  succeeded. PR remains OPEN with no reviews/reviewDecision; independent exact-head review is the
  only current gate before merge. Prior failures and repairs remain recorded: strict diagnostic
  identity catalog repair and exact lib.rs provenance digest update in signed DCO commits f4fe84a0
  and e644f9b0.

- 2026-10-12T00:57:30+00:00: Recorded command exit 0; command argv SHA-256
  3d2fd6b255cc6177652d59680e0f30480812fbb4a8ba725b4bed4de686d6f350.

- 2026-10-12T00:58:06+00:00: Recorded command exit 0; command argv SHA-256
  0f0120a9a80647761b7023e1aec09161f189badcb9a7de98b9ba33922d55f476.

- 2026-10-12T00:59:04+00:00: Independent exact-head review approved PR #587 at
  e644f9b02c5b3f7d46b051691accc249fa8a3585 (tree c2ebca881ea7c31946d20ea18e0cf676b851b22e), base
  0a2039c448d4ab0ed3c9065c35cf90a77b94db6a. Read complete AR/task plan/spec and ASB
  development/architecture/quality docs. Reviewed four-file diff: project execution now validates
  selected external workload identity, platform/status/kind/digest, confined prepared tree, bounded
  verified receipt with revision/license/preparation/evaluator fields; standalone and legacy
  non-external fixtures remain explicitly exempt. Focused project_run 3/3, diagnostic_contract 9/9,
  workflow_transcript 3/3 pass; diff check clean. All five candidate commits SSH-signed by Martin
  Beck with matching DCO. Live PR checks all SUCCESS at exact head, PR open with no prior review. No
  privacy or gate-weakening finding. Approved for merge; do not merge in this review.

- 2026-10-12T00:59:20+00:00: Recorded command exit 1; command argv SHA-256
  89610f06868db0673e1ec1f3e8ee17634b2ce33b76e3bfd5935fece52d43db95.

- 2026-10-12T01:01:11+00:00: Recorded command exit 0; command argv SHA-256
  313241b346f0a07550543d5fe0f53c4c1a99430c1220dda42da81698908036d6.

- 2026-10-12T01:01:23+00:00: Recorded command exit 0; command argv SHA-256
  51cb5d43c543441da462d50d82dad6985b7fbd44e8ebe4650fd180cdcfe58f9f.

- 2026-10-12T01:01:29+00:00: Recorded command exit 0; command argv SHA-256
  1a51d8e44248df9b22b84b9f0a24ce6abc80ad70d73b321cc7698fe7556304ae.

- 2026-10-12T01:01:33+00:00: Recorded command exit 0; command argv SHA-256
  f5a589cdf7ff0b0c4aa322d6e6d65fbb05fd91306ad84af64030c0948de4ef59.

- 2026-10-12T01:01:41+00:00: Recorded command exit 0; command argv SHA-256
  321c534968b9c456a64caf5e6d09b63780c507f97548057d2bfe31edcfd73ff4.

- 2026-10-12T01:01:44+00:00: Recorded command exit 0; command argv SHA-256
  1ffb2638236f4da5d219207f1c9a0dc671216577ba02a0f8c7d6c73ff15b9ab7.

- 2026-10-12T01:01:51+00:00: Recorded command exit 0; command argv SHA-256
  c4eeb48a663282b5fa263132a3906d1d66b4a91715af637e272cad7465412a83.

- 2026-10-12T01:02:30+00:00: Heartbeat by ar1783_workload_selection_luna56.

- 2026-10-12T01:02:31+00:00: Recorded command exit 0; command argv SHA-256
  65a28ba3ae5d7b7849c0e37a61b553dd0e51becadfe7470071409a65024ea638.

- 2026-10-12T01:02:37+00:00: Recorded command exit 0; command argv SHA-256
  3a2b7bf7226995b77da118ac63a88635e36c9eac496f65a7905116db3608e0ee.

- 2026-10-12T01:02:44+00:00: Recorded command exit 0; command argv SHA-256
  33cd178a3a21f5e5a972ee32c041f1e40d71211b204c2a69bd4cef6fedd2a3f4.

- 2026-10-12T01:02:52+00:00: Recorded command exit 0; command argv SHA-256
  ac4d47e85ccb3fc32ecd53496e018da6bbd75d88213fae3e3b9db21fd4355164.

- 2026-10-12T01:02:55+00:00: Recorded command exit 0; command argv SHA-256
  789194c3de396e69228b64d22185390efbacf8c71ca52e73818b7ab7d4490f5a.

- 2026-10-12T01:03:04+00:00: Recorded command exit 0; command argv SHA-256
  75c2ce3316ec9899bc387d7c3b8b989b7c3748a001474f3315f1dc553646cd48.

- 2026-10-12T01:03:09+00:00: Recorded command exit 0; command argv SHA-256
  02061e0c5223bcff613f57b8e63a859f41edacee2e283bb323ff71179031518d.

- 2026-10-12T01:03:17+00:00: Recorded command exit 0; command argv SHA-256
  4f38b54799c71f365511ded9c011c46fef3f7f7e857b2f555cbfb299dd277cc7.

- 2026-10-12T01:03:22+00:00: Recorded command exit 0; command argv SHA-256
  8463e3cb5d1b2b1181c5b01b33fd09a29988ae204d0f68cec7cda97a32d57a48.

- 2026-10-12T01:04:09+00:00: Recorded command exit 0; command argv SHA-256
  e1e2443ed26dba6ae97dfdb982585dcdb062bea06c089a62622c38e5c1ac7c99.

- 2026-10-12T01:04:15+00:00: Recorded command exit 0; command argv SHA-256
  32d00e7bea48deb591900624d4de1f837dadd9a3cd5c55c2ee1561f8660d7fe2.

- 2026-10-12T01:04:23+00:00: Recorded command exit 0; command argv SHA-256
  d283c4dde8ee6702e88e8981fcdcd6e469452a2ff4f1e7985b68e4fcb0b25ca7.

- 2026-10-12T01:04:30+00:00: Recorded command exit 0; command argv SHA-256
  7ea7484350c00dc0a789d2587badd747cc5d6c61381a3948867184be72b14833.

- 2026-10-12T01:04:36+00:00: Recorded command exit 0; command argv SHA-256
  7ec9ee931e1922514ed002b0b54d72e4e53adfb19910ca428634c89d6e218eb3.

- 2026-10-12T01:04:40+00:00: Recorded command exit 1; command argv SHA-256
  42a2bf20f026e3b7074737ad4975e82c2c6c58c8d662597866dc9398a624d784.

- 2026-10-12T01:04:46+00:00: Recorded command exit 1; command argv SHA-256
  2b8b6a2ad67d1409f16849372c2d0fc623d3218660ceed42aa0da77acddd694d.

- 2026-10-12T01:04:52+00:00: Recorded command exit 0; command argv SHA-256
  a1239bc389d925ac45572156f31122e56f5315002dfe57b5fa16611a7d636df3.

- 2026-10-12T01:04:58+00:00: Recorded command exit 1; command argv SHA-256
  75a4b69749702c85590ea8d205fb7c5ad1e7d6b7669299cf5d8b7db8a4806ba1.

- 2026-10-12T01:05:18+00:00: Recorded command exit 0; command argv SHA-256
  68cc83978078c8799733513834dcbf67eab0f6f4264b1bfed655cc74a0857fb1.

- 2026-10-12T01:06:08+00:00: Recorded command exit 0; command argv SHA-256
  03a01f8cb90b5a5baa2f770b58dc604b5085b5ccae539b2cd4678133f7d369a8.

- 2026-10-12T01:06:15+00:00: Recorded command exit 0; command argv SHA-256
  b6a7c16f6fac04887a7890169acf6e61a18106c3a58ea044578c11d5b917cf81.

- 2026-10-12T01:06:26+00:00: Concrete post-merge failure: Repository quality run 38190265292 and
  Portable protected-main provenance run 38190265359 both rejected merge
  5201a0369193be5e093396d76bfa4b1c9b55e9db with: protected-main merge committer is not the local
  integration identity / portable provenance: protected-main merge committer is not the local
  integration identity. Portable job 114621305936 step 3 used
  PUSH_BASE=0a2039c448d4ab0ed3c9065c35cf90a77b94db6a and EVENT_HEAD=5201a036. Historical merge is
  preserved; do not accept/release until a local integration forward repair is green.

- 2026-10-12T01:06:30+00:00: Recorded command exit 0; command argv SHA-256
  24235539c147b40dccb7fd28bde957e6c1294be08d3c5c70b226609c33cc6226.

- 2026-10-12T01:06:37+00:00: Recorded command exit 0; command argv SHA-256
  32d00e7bea48deb591900624d4de1f837dadd9a3cd5c55c2ee1561f8660d7fe2.

- 2026-10-12T01:06:42+00:00: Recorded command exit 0; command argv SHA-256
  d15f729ec5302f1da7f831f387e287d93fd2548b50807dd8d1a029bcab37a1c7.

- 2026-10-12T01:06:51+00:00: Recorded command exit 1; command argv SHA-256
  ad83af4e1489871d6e54a4465f8a719bfe7cb036fc7d248879af19fb3b11ddaa.

- 2026-10-12T01:06:57+00:00: Recorded command exit 0; command argv SHA-256
  d015415b8cdeb947438154b5a42b5dfd3279a1f0242a4b7d08e0dad2ec1c701d.

- 2026-10-12T01:07:04+00:00: Recorded command exit 0; command argv SHA-256
  1c370d6074b72b12c0e0b562e318d930b3628a08d86c31227c66578bebec7737.

- 2026-10-12T01:07:10+00:00: Recorded command exit 1; command argv SHA-256
  5b8d25558a601707d8c775e0a95fe67f71900a0937fdc0b9d57e281b5f044eb7.

- 2026-10-12T01:07:17+00:00: Recorded command exit 0; command argv SHA-256
  5dbd0381ad4a0575c49b4e35fb64a3ad90402ecd052830c49ec497206e276ad1.

- 2026-10-12T01:07:24+00:00: Recorded command exit 0; command argv SHA-256
  766cc2c08caf509c90057f9eb75762610ae02ce31e56f5096db3012fb3d4ac8a.

- 2026-10-12T01:07:35+00:00: Recorded command exit 0; command argv SHA-256
  1aafe4d850b0706d576c6c631a9a01d736ef1c6283a082186cdc9cd22a929c1f.

- 2026-10-12T01:08:11+00:00: Recorded command exit 8; command argv SHA-256
  f283115d81ec675d674538bdc0103e155035d86d225e19704bb85d3842b0189b.

- 2026-10-12T01:08:13+00:00: Recorded command exit 8; command argv SHA-256
  f283115d81ec675d674538bdc0103e155035d86d225e19704bb85d3842b0189b.

- 2026-10-12T01:08:52+00:00: Recorded command exit 8; command argv SHA-256
  f283115d81ec675d674538bdc0103e155035d86d225e19704bb85d3842b0189b.

- 2026-10-12T01:09:00+00:00: Recorded command exit 0; command argv SHA-256
  6ac50d8a9f33e53bd30003377cb8771b1d02c0e272f5a4658aff225662e847af.

- 2026-10-12T01:09:13+00:00: Repair evidence: historical web merge 5201a036 remains preserved; PR
  #596 topic head 506de984 has parents ad64a90f and 5201a036, exact unchanged tree, signed+DCO local
  identity, and local repository_policy all checks passed. First synchronization cdf8b131 was
  rejected for missing Signed-off-by; amended -S -s and force-with-lease pushed. Hosted run
  38190636658 Portable protected-main provenance is already green; remaining required runs are in
  progress/queued.

- 2026-10-12T01:09:20+00:00: Recorded command exit 8; command argv SHA-256
  f283115d81ec675d674538bdc0103e155035d86d225e19704bb85d3842b0189b.

- 2026-10-12T01:09:36+00:00: Recorded command exit 8; command argv SHA-256
  f283115d81ec675d674538bdc0103e155035d86d225e19704bb85d3842b0189b.

- 2026-10-12T01:10:14+00:00: Recorded command exit 8; command argv SHA-256
  f283115d81ec675d674538bdc0103e155035d86d225e19704bb85d3842b0189b.

- 2026-10-12T01:10:16+00:00: Recorded command exit 8; command argv SHA-256
  f283115d81ec675d674538bdc0103e155035d86d225e19704bb85d3842b0189b.

- 2026-10-12T01:10:48+00:00: Recorded command exit 8; command argv SHA-256
  f283115d81ec675d674538bdc0103e155035d86d225e19704bb85d3842b0189b.

- 2026-10-12T01:11:19+00:00: Recorded command exit 8; command argv SHA-256
  f283115d81ec675d674538bdc0103e155035d86d225e19704bb85d3842b0189b.

- 2026-10-12T01:11:50+00:00: Recorded command exit 8; command argv SHA-256
  f283115d81ec675d674538bdc0103e155035d86d225e19704bb85d3842b0189b.

- 2026-10-12T01:11:57+00:00: Recorded command exit 0; command argv SHA-256
  41d9070e3779b92ead741a0279f3dbc40060d44806e145eacd08ec06e0e3bbd2.

- 2026-10-12T01:12:33+00:00: Recorded command exit 8; command argv SHA-256
  f283115d81ec675d674538bdc0103e155035d86d225e19704bb85d3842b0189b.

- 2026-10-12T01:12:35+00:00: Recorded command exit 8; command argv SHA-256
  f283115d81ec675d674538bdc0103e155035d86d225e19704bb85d3842b0189b.

- 2026-10-12T01:12:42+00:00: Recorded command exit 0; command argv SHA-256
  9a1fee751489e25009af80310de0d5b87ff7a7c3aa470c3b47a1f6bc1d5be8a1.

- 2026-10-12T01:13:17+00:00: Recorded command exit 8; command argv SHA-256
  f283115d81ec675d674538bdc0103e155035d86d225e19704bb85d3842b0189b.

- 2026-10-12T01:13:27+00:00: Heartbeat by ar1783_workload_selection_luna56.

- 2026-10-12T01:13:29+00:00: Recorded command exit 8; command argv SHA-256
  f283115d81ec675d674538bdc0103e155035d86d225e19704bb85d3842b0189b.

- 2026-10-12T01:14:00+00:00: Recorded command exit 8; command argv SHA-256
  f283115d81ec675d674538bdc0103e155035d86d225e19704bb85d3842b0189b.

- 2026-10-12T01:14:31+00:00: Recorded command exit 8; command argv SHA-256
  f283115d81ec675d674538bdc0103e155035d86d225e19704bb85d3842b0189b.

- 2026-10-12T01:14:48+00:00: Recorded command exit 0; command argv SHA-256
  41d9070e3779b92ead741a0279f3dbc40060d44806e145eacd08ec06e0e3bbd2.

- 2026-10-12T01:15:16+00:00: Recorded command exit 8; command argv SHA-256
  f283115d81ec675d674538bdc0103e155035d86d225e19704bb85d3842b0189b.

- 2026-10-12T01:15:47+00:00: Recorded command exit 8; command argv SHA-256
  f283115d81ec675d674538bdc0103e155035d86d225e19704bb85d3842b0189b.

- 2026-10-12T01:18:46+00:00: Recorded command exit 0; command argv SHA-256
  e0c7299eb470de7f38a1695f2b20320b95d8e4e8fee04fa5d78cbfeeaceb4b14.

- 2026-10-12T01:18:59+00:00: Hosted terminal evidence at exact head 506de984: PR #596 all listed
  checks pass, including Rust run 38190636507, Policy/coverage/supply-chain run 38190636526, AArch64
  38190636523, Formal 38190636521, Fault 38190636513, platform 38190636493, credential-free
  38190636477, TUI 38190636488, provenance 38190636658, headers 38190636491, and AWQ 38190636560.
  Exact base/tree verified: base 5201a036; topic tree and base tree
  c2ebca881ea7c31946d20ea18e0cf676b851b22e. PR remains open pending durable independent review.

- 2026-10-12T01:29:51+00:00: Heartbeat by ar1783_workload_selection_luna56.

- 2026-10-12T01:30:13+00:00: Recorded command exit 0; command argv SHA-256
  321c534968b9c456a64caf5e6d09b63780c507f97548057d2bfe31edcfd73ff4.

- 2026-10-12T01:30:16+00:00: Recorded command exit 0; command argv SHA-256
  cee2c29c5404892732d39e00825cdb549369e73ac4faa368868ac143f8b8eb64.

- 2026-10-12T01:30:19+00:00: Recorded command exit 0; command argv SHA-256
  c629e6bf0074745125aa9354164294681819bb3261a8e62380765c681e2f39e0.

- 2026-10-12T01:30:25+00:00: Recorded command exit 0; command argv SHA-256
  f283115d81ec675d674538bdc0103e155035d86d225e19704bb85d3842b0189b.

- 2026-10-12T01:30:32+00:00: Recorded command exit 0; command argv SHA-256
  56acd7514594a327da0c6d86bd75ea9bda08106ad88398e1014f1773de4abfcf.

- 2026-10-12T01:30:33+00:00: Recorded command exit 0; command argv SHA-256
  43eff77a126de093d58e18b90140115a58011d0c551685a25fce1dccce0ce392.

- 2026-10-12T01:30:37+00:00: Recorded command exit 0; command argv SHA-256
  9d3ccbe91e5025fa2777ef2030ee380691a7941fbc5bff44f235b31efcbc8b4c.

- 2026-10-12T01:30:38+00:00: Recorded command exit 0; command argv SHA-256
  6e4e65a1005e3f1e22aa997f16556e4d2b11fa632e438cbfaa7e5e0981a2a8a1.

- 2026-10-12T01:30:44+00:00: Recorded command exit 0; command argv SHA-256
  a71ae50e44ec6a7253169357dd11596528e539d33c38ebfed2b5dc7ea2542e26.

- 2026-10-12T01:30:48+00:00: Recorded command exit 0; command argv SHA-256
  1c370d6074b72b12c0e0b562e318d930b3628a08d86c31227c66578bebec7737.

- 2026-10-12T01:30:55+00:00: Recorded command exit 1; command argv SHA-256
  81343860ae2e1711fde7434bb7ce6bc42da51c2d1650b6cab3c87c7156d707c3.

- 2026-10-12T01:31:02+00:00: Recorded command exit 1; command argv SHA-256
  c39a7a9a107fbaa9eba4960d2e2e03de0be28c1d4b94f7da92bc8903eb4d1b00.

- 2026-10-12T01:31:03+00:00: Recorded command exit 1; command argv SHA-256
  a7c13d719060f2141b26f90e8ada2846f2773a72200efc4a219c0358917e5ed8.

- 2026-10-12T01:31:10+00:00: INDEPENDENT TECHNICAL REVIEW APPROVED: PR #596 exact head
  506de984af222659b3b48824cef7d34b15118862, approved base 5201a0369193be5e093396d76bfa4b1c9b55e9db,
  exact reviewed tree c2ebca881ea7c31946d20ea18e0cf676b851b22e. Reviewed the installed-workload
  selection/execution acceptance against the AR-1783 plan/spec: project-bound workload catalog
  identity/digest/revision/license/terms/preparation/adapter/platform validation,
  run/sweep/report/compare binding, stale/revoked/missing/manual-substitution rejection, bounded
  privacy-safe outputs, and no ambient directory fallback. Both commits in the reviewed range are
  SSH-signed (principal martin.beck2@gmx.de) and carry matching Signed-off-by DCO trailers; no
  credentials/private host data or gate weakening found. All required hosted checks for PR #596 are
  terminal SUCCESS, including policy/coverage/supply chain, Rust, aarch64, provenance,
  credential-free, privacy/TUI, fuzz, formal, mutation, and retained-fault gates. Approved for
  merge; do not merge in this review.

- 2026-10-12T01:31:10+00:00: Recorded command exit 0; command argv SHA-256
  67d7fa7c9799f03cf41691ab44ee42ba9b531659112ab6b66afeac3ca20d5976.

- 2026-10-12T01:31:26+00:00: Recorded command exit 0; command argv SHA-256
  8be66604c6491f47a5bb38130ba2134dce57a1d6535e94c6ee078f7f003db42d.

- 2026-10-12T01:31:37+00:00: Recorded command exit 0; command argv SHA-256
  1c370d6074b72b12c0e0b562e318d930b3628a08d86c31227c66578bebec7737.

- 2026-10-12T01:31:42+00:00: Recorded command exit 0; command argv SHA-256
  61a5ea6ddf08a3e2a7086ea9cd731e1d5bb07769bc5efa205ec7e8229d81fa09.

- 2026-10-12T01:32:11+00:00: Protected main advanced from 5201a036 to 98327152 via PR #597 while
  AR-1783 review was pending. Stale 506de984 approval is intentionally not reused. Repair topic now
  has signed+DCO add5690b (parents 506de984,98327152) and signed+DCO db9b1fb8 alignment, exact tree
  852f5b4ff6fa5f21a7120298e167e5a97487aa7a matching current main; local repository policy all checks
  passed. The first attempted sync ae71fb35 lacked Signed-off-by and was discarded; replacement
  db9b1fb8 passes policy.

- 2026-10-12T01:32:21+00:00: Recorded command exit 0; command argv SHA-256
  118a4754dd6c557f81b8470bb292bd635bd68d77b06d2ef7b41a1795c9e4d2a8.

- 2026-10-12T01:32:27+00:00: Recorded command exit 0; command argv SHA-256
  1c370d6074b72b12c0e0b562e318d930b3628a08d86c31227c66578bebec7737.

- 2026-10-12T01:32:34+00:00: Recorded command exit 0; command argv SHA-256
  66199c99ae3f3e8f18d242cc1a010adcdd21f332a209c21c351b7bed9ec90fa2.

- 2026-10-12T01:33:19+00:00: Recorded command exit 0; command argv SHA-256
  75f683fb0bb3ac099e9bf2f9389ecd4b3558f3d34d1a38aef88e234fc5ba251e.

- 2026-10-12T01:33:25+00:00: Recorded command exit 0; command argv SHA-256
  4d3bb2234b3d22652f3d57d75e91a2f40a42047b4a4cce6ca5230a2059300435.

- 2026-10-12T01:33:29+00:00: Recorded command exit 0; command argv SHA-256
  1c370d6074b72b12c0e0b562e318d930b3628a08d86c31227c66578bebec7737.

- 2026-10-12T01:33:35+00:00: Recorded command exit 0; command argv SHA-256
  d5b51d3ce4fa910e9c44aa6fd4fe2d1aee2efb6ca7ea64db1f4aa611d016cc59.

- 2026-10-12T01:34:23+00:00: Topology diagnosis: portable provenance rejected add5690b because any
  pull-request synchronization merge must be topic tip; removing alignment left add5690b as an
  invalid historical topic merge. Final repair head aca3f79b3256729543e93cc321ce3a85daa78051 is a
  single signed+DCO commit parented directly on current protected main
  98327152f2e92308b5bcf5b21cfe0c9f285cf950, tree 852f5b4ff6fa5f21a7120298e167e5a97487aa7a. Local
  repository policy passes; hosted Portable protected-main provenance run 38192353961 is green.
  Fresh exact-head review is required; prior 506de984 approval is invalidated.

- 2026-10-12T01:38:41+00:00: Heartbeat by ar1783_workload_selection_luna56.

- 2026-10-12T01:39:47+00:00: Recorded command exit 8; command argv SHA-256
  f283115d81ec675d674538bdc0103e155035d86d225e19704bb85d3842b0189b.

- 2026-10-12T01:40:26+00:00: Recorded command exit 8; command argv SHA-256
  f283115d81ec675d674538bdc0103e155035d86d225e19704bb85d3842b0189b.

- 2026-10-12T01:40:32+00:00: Recorded command exit 0; command argv SHA-256
  adc1ad366b4a2e0ae3329a8d7481cc097324fd73e9db001038d112a3dbf835d5.

- 2026-10-12T01:41:10+00:00: Recorded command exit 8; command argv SHA-256
  f283115d81ec675d674538bdc0103e155035d86d225e19704bb85d3842b0189b.

- 2026-10-12T01:41:47+00:00: Recorded command exit 8; command argv SHA-256
  f283115d81ec675d674538bdc0103e155035d86d225e19704bb85d3842b0189b.

- 2026-10-12T01:41:54+00:00: Recorded command exit 0; command argv SHA-256
  543a23f479b2dc68bee33ad81b77baa784522582f7f8608d6712360dedac57ef.

- 2026-10-12T01:42:34+00:00: Recorded command exit 8; command argv SHA-256
  f283115d81ec675d674538bdc0103e155035d86d225e19704bb85d3842b0189b.

- 2026-10-12T01:43:11+00:00: Recorded command exit 8; command argv SHA-256
  f283115d81ec675d674538bdc0103e155035d86d225e19704bb85d3842b0189b.

- 2026-10-12T01:43:49+00:00: Recorded command exit 8; command argv SHA-256
  f283115d81ec675d674538bdc0103e155035d86d225e19704bb85d3842b0189b.

- 2026-10-12T01:44:27+00:00: Recorded command exit 8; command argv SHA-256
  f283115d81ec675d674538bdc0103e155035d86d225e19704bb85d3842b0189b.

- 2026-10-12T01:45:05+00:00: Recorded command exit 8; command argv SHA-256
  f283115d81ec675d674538bdc0103e155035d86d225e19704bb85d3842b0189b.

- 2026-10-12T01:45:11+00:00: Recorded command exit 0; command argv SHA-256
  dc3a7c018ad5d3c62e946154e819ab868d1e941d883d3525435edd3ba19b9fe9.

- 2026-10-12T01:45:49+00:00: Recorded command exit 0; command argv SHA-256
  f283115d81ec675d674538bdc0103e155035d86d225e19704bb85d3842b0189b.

- 2026-10-12T01:45:51+00:00: Recorded command exit 0; command argv SHA-256
  5725d50980ebacf7d188110bf11bc9b53f19b62d3db60a89b0c92138e03a2730.

- 2026-10-12T01:45:59+00:00: Recorded command exit 1; command argv SHA-256
  9fab929adb3cd5c76dac9f228fadedba5b8c834dfbda5b863bee8e7fd3084505.

- 2026-10-12T01:46:06+00:00: Recorded command exit 1; command argv SHA-256
  353d303b655aecd02b9b31092a6d781df851605cf3b2337e171f0ddeee7aaf17.

- 2026-10-12T01:46:12+00:00: FRESH INDEPENDENT TECHNICAL REVIEW APPROVED: PR #596 exact head
  aca3f79b3256729543e93cc321ce3a85daa78051, exact reviewed base
  98327152f2e92308b5bcf5b21cfe0c9f285cf950, exact reviewed tree
  852f5b4ff6fa5f21a7120298e167e5a97487aa7a. Prior 506de984 approval is stale and not reused.
  Reviewed the current installed-workload selection/execution acceptance against AR-1783 plan/spec:
  project-bound catalog identity/revision/digest/license/terms/preparation/adapter/platform
  validation; every workload including SWE-mini; install/select/bounded run/sweep/report/compare
  evidence binding; stale/revoked/missing/incompatible/manual-substitution rejection; bounded
  privacy-safe output and no ambient directory fallback. Current range is signed with certified SSH
  identity and matching Signed-off-by DCO trailers; no credentials, private host data, or gate
  weakening found. All current required hosted checks are terminal SUCCESS at aca3f79, including
  policy/coverage/supply chain, Rust, emulated aarch64, provenance, credential-free, privacy/TUI,
  fuzz, formal, mutation, and retained-fault gates. Approved for merge; do not merge in this review.

- 2026-10-12T01:46:13+00:00: Recorded command exit 0; command argv SHA-256
  e58541a04ee60bf2b323a5f01a61abdf34360ce8dde236c9f8c61a58790722fb.

- 2026-10-12T01:46:17+00:00: Recorded command exit 1; command argv SHA-256
  5c73187eef8b5d4721b28ebe9759e45de0ac45b9687fc6679ef478eba2aa6282.

- 2026-10-12T01:46:26+00:00: Recorded command exit 0; command argv SHA-256
  cf7636d43a51c6626f20eb542b220961dc2da4a80582bf5a8cffe6571ba33358.

- 2026-10-12T01:46:37+00:00: Recorded command exit 0; command argv SHA-256
  06e3268785b6879ef98ca15c28d464109b48c8861ac00e711706c6ef9d6ed133.

- 2026-10-12T01:46:43+00:00: Recorded command exit 0; command argv SHA-256
  321c534968b9c456a64caf5e6d09b63780c507f97548057d2bfe31edcfd73ff4.

- 2026-10-12T01:47:01+00:00: Integration receipt: tools/integration/merge_pr.py ran in clean
  detached base worktree, expected base 98327152f2e92308b5bcf5b21cfe0c9f285cf950, reviewed head
  aca3f79b3256729543e93cc321ce3a85daa78051, expected tree 852f5b4ff6fa5f21a7120298e167e5a97487aa7a;
  published merge ca494d506135c4a3263bea21621dcc97d817614c. Verified merge parents exactly
  base/topic, SSH signature GMartin Beck, DCO trailer, tree 852f5b4f, and origin/main exact
  ca494d50. Post-merge runs 38193200385/393/407/410/422/427/434/435/452/588 are in progress except
  provenance and headers green.

- 2026-10-12T01:55:03+00:00: Heartbeat by ar1783_workload_selection_luna56.

- 2026-10-12T01:59:15+00:00: Accepted against exact protected-main merge
  ca494d506135c4a3263bea21621dcc97d817614c. Exact parents 98327152f2e92308b5bcf5b21cfe0c9f285cf950
  and aca3f79b3256729543e93cc321ce3a85daa78051, tree 852f5b4ff6fa5f21a7120298e167e5a97487aa7a,
  SSH/DCO verified. All ten post-merge required workflows terminal SUCCESS: 38193200385,
  38193200393, 38193200407, 38193200410, 38193200422, 38193200427, 38193200434, 38193200435,
  38193200452, 38193200588. Receipt digest is
  sha256:f2d6c53370f84bcc31cb3fe9cbd6565f81f038c8e47375ec01ad5735dc174e19.

- 2026-10-12T01:59:18+00:00: Released AR-1783 done after signed protected-main merge
  ca494d506135c4a3263bea21621dcc97d817614c, exact tree/parents/signature/DCO verification, and all
  ten terminal-green post-merge workflows. Historical failed web merge 5201a036 and repair
  diagnostics remain durable.
