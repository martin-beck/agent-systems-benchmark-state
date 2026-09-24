---
{
  "branch": "feature/ar-1320-persisted-agent-release-index",
  "checkpoint_commit": "77571ff978b886e24d35e29c0febb553a90a2d65",
  "claim_expires": "2026-09-24T22:04:29+00:00",
  "depends_on": [
    "AR-1316"
  ],
  "id": "AR-1320",
  "next_action": "Complete independent review and repository hygiene checks; do not publish until branch diff is clean, signed, DCO-compliant, and PR/CI evidence is available.",
  "owner": "codex-ar1320-luna56",
  "plan": "../plans/AR-1320.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Persist and verify the ASB agent release index used by the setup wizard.",
  "task_revision": 34,
  "title": "Persisted authenticated agent release index",
  "updated_at": "2026-09-24T20:15:20+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1320-persisted-agent-release-index"
}
---

AR-1316 now publishes a truthful unavailable roster, but it is rebuilt in the
backend and does not yet persist a verified source snapshot across restart.
This AR owns the durable signed release-index and generation lifecycle needed
before any agent can become selectable.

- 2026-09-24T20:02:12+00:00: AR-1316 is durably done; promote the next setup/catalog AR for
  implementation.

- 2026-09-24T20:04:29+00:00: Claimed by codex-ar1320-luna56.

- 2026-09-24T20:04:48+00:00: Recorded command exit 0; command argv SHA-256
  498ccf248bc166cd8940e579a67ad12e0a07199783062cc3019459f7d310c063.

- 2026-09-24T20:05:21+00:00: Recorded command exit 0; command argv SHA-256
  f4abd2f9e2e254f6744cfc1db142170dec6bb1d20a66ac186cc4a74024b38d62.

- 2026-09-24T20:05:37+00:00: Recorded command exit 0; command argv SHA-256
  00470261f504532f2ea6775b2d6738887b5f75732f3a984770807beb880c321b.

- 2026-09-24T20:05:52+00:00: Recorded command exit 2; command argv SHA-256
  abae542d76af0b1098b080baf7adb60773eeb1ca61f6fcd047144c1bbf300c15.

- 2026-09-24T20:06:07+00:00: Recorded command exit 0; command argv SHA-256
  c74a5b2e0a8bdf6896b87e7bfb78dd6cf3363890501bd6ffc2839025615c055d.

- 2026-09-24T20:06:23+00:00: Recorded command exit 0; command argv SHA-256
  71531a0b8db072e74e1be8fcb4dcc3791a496bd6885b52fe7c3337a1437c2cce.

- 2026-09-24T20:06:38+00:00: Recorded command exit 0; command argv SHA-256
  2a19ad50a4059654290db561f3a71d2d2a757a00155e3815a39fa7078174c740.

- 2026-09-24T20:06:53+00:00: Recorded command exit 1; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-24T20:07:08+00:00: Recorded command exit 0; command argv SHA-256
  3140dac2823c0ab32c9541cace10266a017b471f528c906ef9e301fd3142fa3f.

- 2026-09-24T20:07:22+00:00: Recorded command exit 0; command argv SHA-256
  6478143af636c558cfeb5eb65e04e5fedbb3f05f22adc162611a249a9564d090.

- 2026-09-24T20:07:38+00:00: Recorded command exit 0; command argv SHA-256
  9ca3645fccdff1e8d251ec5cd6263ac3d203c04e63910247727fb9170fc3c83c.

- 2026-09-24T20:07:58+00:00: Recorded command exit 101; command argv SHA-256
  dc4a095ce1836885814ac05d01e5ba07d878262ee04912e9105d473999ebbd01.

- 2026-09-24T20:08:13+00:00: Recorded command exit 0; command argv SHA-256
  c477544e1adefe502d1cd53fb84e4fb992471b7b196d6ef7a0872542b5eb911d.

- 2026-09-24T20:08:28+00:00: Recorded command exit 0; command argv SHA-256
  99f5c499138b6554f0f1909608720db2019baa91e2c67e043455254cea6e975d.

- 2026-09-24T20:09:21+00:00: Recorded command exit 0; command argv SHA-256
  3f64a2a804f25d1921f2b8a662c3d718c793ef08d47d30be3e5eb538ae998fa9.

- 2026-09-24T20:09:53+00:00: Recorded command exit 101; command argv SHA-256
  22b61dba2cc01e9e7c5d5c0325f4150b1692d253a456bb60210f72c973e9c134.

- 2026-09-24T20:10:15+00:00: Recorded command exit 0; command argv SHA-256
  94b96869bfae577e6b5601eac9d833a7a7f3672a2f911918fd830e917c09c79e.

- 2026-09-24T20:10:29+00:00: Recorded command exit 0; command argv SHA-256
  b983cd9d63485f2b15966aee842510d553b584962e75f9a05a4e2d22da69ab5e.

- 2026-09-24T20:10:44+00:00: Recorded command exit 0; command argv SHA-256
  d371733cc87877c5e30be9d9c73e811c93371b8683121de3361555a719bf0340.

- 2026-09-24T20:11:33+00:00: Focused verification failures recorded: (1) cargo test -p asb-cli
  agent_catalog_refresh_is_generation_fenced_and_restart_stable from /tmp/asb-ar1320 exited 101
  because test scratch base overlapped the repository; corrective action: reran with
  coordinator-created /srv/data/projects/asb-test-tmp (mode 0700), and the test passed. (2) rerun
  with /srv/data/projects/.tmp exited 101 because test scratch base ownership or mode was unsafe;
  corrective action: created /srv/data/projects/asb-test-tmp and set mode 0700. (3) one handoffctl
  run attempt exited 1 because cargo fmt was invoked from the state checkout without a Cargo.toml;
  corrective action: reran with --manifest-path /tmp/asb-ar1320/Cargo.toml. Concurrent coordinator
  lock timeouts were observed and retried; no product mutation resulted.

- 2026-09-24T20:12:15+00:00: Recorded command exit 0; command argv SHA-256
  a81cf8a43079c59c32cb5d8ee4c8e4b598b2c2e72587ffd3a6a5a932f92ebd85.

- 2026-09-24T20:12:38+00:00: Full asb-cli gate initially failed one pre-existing
  concurrency-sensitive test:
  restart_reconciles_in_progress_capture_without_retrying_provider_effect exited 101 with control
  state root is already owned; corrective action: reran that exact test in isolation with
  TMPDIR=/srv/data/projects/asb-test-tmp and it passed (1 passed). The agent-catalog focused test
  also passes. No product files changed.

- 2026-09-24T20:12:58+00:00: Recorded command exit 0; command argv SHA-256
  6478143af636c558cfeb5eb65e04e5fedbb3f05f22adc162611a249a9564d090.

- 2026-09-24T20:13:13+00:00: Recorded command exit 0; command argv SHA-256
  d7fed1b9326168e2437e4f6de884108cfedbcd445d7a7abc9e5a485aff9f38b8.

- 2026-09-24T20:13:27+00:00: Recorded command exit 0; command argv SHA-256
  e93b6397b8df2dec7e257c5a26380c055b1ead2b109f976bf2448d6f5a58c7d2.

- 2026-09-24T20:13:42+00:00: Recorded command exit 0; command argv SHA-256
  f4abd2f9e2e254f6744cfc1db142170dec6bb1d20a66ac186cc4a74024b38d62.

- 2026-09-24T20:14:00+00:00: Recorded command exit 0; command argv SHA-256
  5ee3f443fa934571034e2404c9670bc50af30c4f0e07a837780f9795b44ee144.

- 2026-09-24T20:14:49+00:00: Recorded command exit 0; command argv SHA-256
  2472b913f6ff587c4fa52beb588c52463d81290f9066172bf56a2b8442486119.

- 2026-09-24T20:15:20+00:00: Recorded command exit 1; command argv SHA-256
  cf20770a9873ddf953a85e787a2b6338d29e543753926e013ed92358a6fec97e.
