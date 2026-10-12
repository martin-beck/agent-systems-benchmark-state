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
  "next_action": "Integrate every development-supported installed workload bundle into selection and prove full run/sweep/report/compare consumes its exact recorded identity.",
  "observed_branch": "feature/ar-1783-installed-workload-selection-and-execution",
  "observed_dirty": 0,
  "observed_head": "4dfb7a3038c2e95b76c10844fedde87281b35361",
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
  "summary": "Select every development external workload and prove ASB uses its exact project-local identity end to end.",
  "task_revision": 47,
  "title": "Installed workload selection and execution",
  "updated_at": "2026-10-12T00:13:41+00:00",
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
