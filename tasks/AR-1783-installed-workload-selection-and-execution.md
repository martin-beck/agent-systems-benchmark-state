---
{
  "branch": "feature/ar-1783-installed-workload-selection-and-execution",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-12T02:11:50+00:00",
  "depends_on": [
    "AR-1763",
    "AR-1764",
    "AR-1782"
  ],
  "id": "AR-1783",
  "next_action": "Poll PR #587 checks only after meaningful head change; require Policy/coverage/supply-chain and Rust verification green, independent exact-head review, then merge and post-merge verify before accept/release.",
  "observed_branch": "feature/ar-1783-installed-workload-selection-and-execution",
  "observed_dirty": 0,
  "observed_head": "f4fe84a0936a26df85f8e4f98b913c924f779c46",
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
  "summary": "Repair reviewed CLI identity catalog and requalify signed PR head f4fe84a0",
  "task_revision": 103,
  "title": "Installed workload selection and execution",
  "updated_at": "2026-10-12T00:41:21+00:00",
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
