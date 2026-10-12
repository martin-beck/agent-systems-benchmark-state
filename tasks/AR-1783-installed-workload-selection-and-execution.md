---
{
  "branch": "feature/ar-1783-installed-workload-selection-and-execution",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-12T02:14:51+00:00",
  "depends_on": [
    "AR-1763",
    "AR-1764",
    "AR-1782"
  ],
  "id": "AR-1783",
  "next_action": "Record independent exact-head review of 506de984, then run tools/integration/merge_pr.py against base 5201a036/tree c2ebca881ea7c31946d20ea18e0cf676b851b22e, verify green protected main, accept and release",
  "observed_branch": "feature/ar-1783-installed-workload-selection-and-execution",
  "observed_dirty": 0,
  "observed_head": "ae71fb35fbf1325eb34366ea4a3ccfad5e23d8e7",
  "owner": "ar1783_workload_selection_luna56",
  "plan": "../plans/AR-1783-installed-workload-selection-and-execution.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "environmental",
    "evidence_digest": "",
    "evidence_ref": "",
    "spec_ref": "specs/AR-1783.json",
    "spec_revision": 2,
    "status": "pending"
  },
  "spec_ref": "specs/AR-1783.json",
  "spec_revision": 2,
  "status": "in_progress",
  "summary": "Repair PR #596 exact head 506de984 has all hosted required checks green; independent review remains required before local integration",
  "task_revision": 218,
  "title": "Installed workload selection and execution",
  "updated_at": "2026-10-12T01:30:19+00:00",
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
