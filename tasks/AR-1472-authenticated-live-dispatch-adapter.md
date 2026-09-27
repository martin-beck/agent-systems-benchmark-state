---
{
  "branch": "feature/ar-1472-authenticated-live-dispatch-adapter",
  "checkpoint_commit": "5f785dab598f24c2221272cf53b9366a10625413",
  "claim_expires": "2026-09-27T03:34:43+00:00",
  "depends_on": [
    "AR-1373",
    "AR-1363"
  ],
  "id": "AR-1472",
  "next_action": "Run full workspace gates, then independent review and publish exact signed head through handoffctl.",
  "observed_branch": "feature/ar-1472-authenticated-live-dispatch-adapter",
  "observed_dirty": 0,
  "observed_head": "5f785dab598f24c2221272cf53b9366a10625413",
  "owner": "ar1332_record_replay_luna56",
  "plan": "../plans/AR-1472-authenticated-live-dispatch-adapter.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Connect authenticated control receipts to runtime-owned CLI live dispatch without a dependency cycle.",
  "task_revision": 31,
  "title": "Authenticated live-dispatch adapter",
  "updated_at": "2026-09-27T01:46:15+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1472-authenticated-live-dispatch-adapter"
}
---

Successor for the circular AR-1374/AR-1375 dependency. It must not touch
asb-tui, require a live provider, expose credentials, or fabricate runtime
authority. Mandatory qualification is deterministic local/mock or replay.

- 2026-09-27T01:33:00+00:00: Created after AR-1374 current-main audit found
  AR-1375 circularly depended on the blocked dispatch AR. Depends only on
  completed authenticated receipt-source ARs.

- 2026-09-27T01:34:40+00:00: Circular AR-1374/AR-1375 dependency repaired; dependencies AR-1373 and
  AR-1363 are done. Implement the narrow authenticated adapter successor.

- 2026-09-27T01:34:43+00:00: Claimed by ar1332_record_replay_luna56.

- 2026-09-27T01:35:44+00:00: Recorded command exit 0; command argv SHA-256
  59bb9a1153647e6dc218582c1538eb832e176b1bda204242704cd5898afc7806.

- 2026-09-27T01:36:10+00:00: Recorded command exit 0; command argv SHA-256
  4d290c6dc120e554fc209ce1c9ac890ba28e0f2fd1b3089834e5d1f1ca90e071.

- 2026-09-27T01:36:29+00:00: Recorded command exit 0; command argv SHA-256
  9d6fcabeb7e5b962740288c314bdd7c232554d15e2929a4a65685d842b2991bd.

- 2026-09-27T01:36:44+00:00: Recorded command exit 0; command argv SHA-256
  cfccf54cf2fb0224d961b5f78dcf8433c105cff235fa6076fcee6d9f495f6cce.

- 2026-09-27T01:37:09+00:00: Recorded command exit 0; command argv SHA-256
  5120e9e96db00c2696ca438a3e8260234064fb107703eae831f030c08a5fe917.

- 2026-09-27T01:37:23+00:00: Recorded command exit 0; command argv SHA-256
  8bb052aed29d30070d07099e89f2c4bdf14a6a8cceabb002d7f120616d92b76b.

- 2026-09-27T01:37:54+00:00: Recorded command exit 0; command argv SHA-256
  0cc2d5251c4585ad1aee95035f632213a41375969c9aee2ee196d74ede2df6a3.

- 2026-09-27T01:38:17+00:00: Recorded command exit 0; command argv SHA-256
  eafe6afd1bc1686435d1a0fcab125c3ea981194bd47463341bdecb16b00311da.

- 2026-09-27T01:38:56+00:00: Recorded command exit 0; command argv SHA-256
  f324a49c78e3cd321a41af71e88ec8f1bbcee64a37251219b6edd022f9e0c78f.

- 2026-09-27T01:39:17+00:00: Recorded command exit 1; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-27T01:39:36+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-27T01:39:56+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-27T01:40:41+00:00: Recorded command exit 0; command argv SHA-256
  5c65734e6538cf9e4793a7b2544e7ef4effba6047efc156c8474d0017efc7be6.

- 2026-09-27T01:40:56+00:00: Recorded command exit 0; command argv SHA-256
  7c730eec3ea71bd24ffc5a9255bf7f542481bf601dba6c72bed6e00f6c2fab3c.

- 2026-09-27T01:41:16+00:00: Recorded command exit 0; command argv SHA-256
  0c3a5150207f73fcd896f8d69bcd72b4bab205cdeca8aa41f1a41b6ef0ed74a8.

- 2026-09-27T01:41:37+00:00: Current main 4ee5a4ed isolated worktree. Implemented narrow runtime
  adapter: LiveProviderRuntimeDispatchSource::from_enrollment consumes only opaque
  LiveProviderEnrollment and delegates to existing validated from_handle path; enrollment failures
  map to InvalidConfiguration before scheduler exposure. Added deterministic positive one-shot
  opaque-enrollment test and unavailable-enrollment negative test. No asb-tui/live-provider changes.
  Focused runtime/CLI tests pass (133 passed, 1 ignored), fmt/diff clean, signed+DCO commit 5f785dab
  verified.

- 2026-09-27T01:42:19+00:00: Recorded command exit 0; command argv SHA-256
  534f8613e1c316db8f0f46dd989e44e14a8ca74304a94791b4e4a1c59b2fbb1d.

- 2026-09-27T01:42:35+00:00: Recorded command exit 0; command argv SHA-256
  1024fc1e6cefa31b078f0b5d2ed85c7ea4586897b388bf1e308f62db58574461.

- 2026-09-27T01:43:02+00:00: Recorded command exit 0; command argv SHA-256
  83eea80a9d087ff8892cb2661bf0e6f7ab62f8c8288f14697126e2ebaafdf975.

- 2026-09-27T01:43:50+00:00: Recorded command exit 0; command argv SHA-256
  b49a90ee600c1023cee9ee9f9e8a4f9a06c53eef8c48d3932d88e482126c7c01.

- 2026-09-27T01:44:40+00:00: Recorded command exit 0; command argv SHA-256
  d04aa803a9fcb854b247572f9b417fd1935a57ca978bb887d2e7c188e99db043.

- 2026-09-27T01:44:55+00:00: Recorded command exit 1; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-27T01:45:26+00:00: Recorded command exit 0; command argv SHA-256
  d04aa803a9fcb854b247572f9b417fd1935a57ca978bb887d2e7c188e99db043.

- 2026-09-27T01:45:45+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-27T01:46:15+00:00: Recorded command exit 0; command argv SHA-256
  5c65734e6538cf9e4793a7b2544e7ef4effba6047efc156c8474d0017efc7be6.
