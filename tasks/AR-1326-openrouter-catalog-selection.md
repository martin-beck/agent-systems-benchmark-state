---
{
  "branch": "feature/ar-1326-openrouter-catalog-selection",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-23T09:01:58+00:00",
  "depends_on": [
    "AR-0313",
    "AR-1325"
  ],
  "id": "AR-1326",
  "next_action": "PR #250 merged at 8692729a58d16e5c9d5387d5d68a7daa54d6443a. Post-merge hosted workflows: Fault assurance and hosted portability passed; Rust verification failed once on timing assertion gemini::tests::malformed_ready_marker_fails_fast_and_cleans_run_root (elapsed >= 1s), while Repository quality, Formal assurance, and Emulated AArch64 remain in progress. Keep AR in progress and create/assign a repair AR or approved rerun; do not release done until all post-merge evidence is green.",
  "observed_branch": "feature/ar-1326-openrouter-catalog-selection",
  "observed_dirty": 0,
  "observed_head": "64a3a002018a542cba9a6e5844589c89417700a5",
  "owner": "codex-asb-ar1326-20260923",
  "plan": "../plans/AR-1326.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Advertise the OpenRouter profile in the CLI provider catalog and accept it in provider-plan selection.",
  "task_revision": 43,
  "title": "Select OpenRouter through the CLI provider catalog",
  "updated_at": "2026-09-23T07:02:40+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1326-openrouter-catalog-selection"
}
---

The closed `asb provider-catalog` output only advertises `openai` as selectable
and `provider-plan` rejects any other profile, so the AR-1325 OpenRouter profile
cannot be selected end to end. This AR extends the CLI catalog identity and the
selection path: `provider_catalog`, `provider_catalog_digest`, `provider_plan`
and `validate_provider_selection` gain the `openrouter` profile with its pinned
model, the selection manifest carries the OpenRouter provider profile, and the
plan/experiment binding accepts the OpenRouter model identity without weakening
the fail-closed content-address checks.

- 2026-09-23T06:44:36+00:00: Promoted after AR-1325 provider profile and protected-main repair are
  complete and post-merge workflows are green.

- 2026-09-23T06:46:14+00:00: Claimed by codex-asb-ar1326-20260923.

- 2026-09-23T06:46:33+00:00: Recorded command exit 0; command argv SHA-256
  f5b0c15f4770053bcb33932b08720ba3b39fe8acb9332383209242201b949ea5.

- 2026-09-23T06:46:54+00:00: Recorded command exit 0; command argv SHA-256
  bc76c7aa1aebfeb93c2f7fc4fc94489109031e9692c06579982d7d99fc83dc8e.

- 2026-09-23T06:47:23+00:00: Recorded command exit 1; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-23T06:47:41+00:00: Recorded command exit 0; command argv SHA-256
  e8d9b4361efdcfbea0c74c2bdefa047fc8f06de115fb4ddb5e30e4f4c63a1f83.

- 2026-09-23T06:48:16+00:00: Recorded command exit 101; command argv SHA-256
  f345d38a5139bb1ee1454021b3751f227b6cbd8c228dca91c369de1a7ea068bb.

- 2026-09-23T06:48:29+00:00: Recorded command exit 0; command argv SHA-256
  08699230908ee4610f64584954e71c4032ddcffaa2ad1f603212b64fa9247216.

- 2026-09-23T06:49:02+00:00: Recorded command exit 0; command argv SHA-256
  8b672149a1a5b2a344a29aaace585428903caf2cb761ce40532261c44bf3daa0.

- 2026-09-23T06:49:18+00:00: Recorded command exit 0; command argv SHA-256
  8c9818d6dab822480d8fa4cf7ab7c5b2e567a79fd9404c2cc717a99bf9165a94.

- 2026-09-23T06:50:32+00:00: Heartbeat by codex-asb-ar1326-20260923.

- 2026-09-23T06:50:52+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-23T06:51:20+00:00: Recorded command exit 101; command argv SHA-256
  534f8613e1c316db8f0f46dd989e44e14a8ca74304a94791b4e4a1c59b2fbb1d.

- 2026-09-23T06:51:41+00:00: Recorded command exit 0; command argv SHA-256
  fd5732ac3e8e10c52f19501fb44dfd37ae6a65e7b1927439a83a826245ac0423.

- 2026-09-23T06:52:14+00:00: Heartbeat by codex-asb-ar1326-20260923.

- 2026-09-23T06:52:24+00:00: Recorded command exit 0; command argv SHA-256
  1024fc1e6cefa31b078f0b5d2ed85c7ea4586897b388bf1e308f62db58574461.

- 2026-09-23T06:52:39+00:00: Recorded command exit 101; command argv SHA-256
  22fc19d872be75a975891ff0abd53f1c305974a409b50c49c5df5d842d033e81.

- 2026-09-23T06:52:51+00:00: Recorded command exit 0; command argv SHA-256
  21dedc4c397aec52824556459b566d4c78dd18b5e5b27ef668d0a4193bd42895.

- 2026-09-23T06:53:18+00:00: Replacement worker audit: implementation head is clean, signed+DCO;
  local focused gates pass. Full parallel workspace and CLI runs had infrastructure concurrency
  failures (mini_swe ExecutableFileBusy x3; control state root already owned), reproduced tests
  passed with --test-threads=1. Hosted required checks remain in progress.

- 2026-09-23T06:53:36+00:00: Heartbeat by codex-asb-ar1326-20260923.

- 2026-09-23T06:54:40+00:00: Heartbeat by codex-asb-ar1326-20260923.

- 2026-09-23T06:55:39+00:00: Heartbeat by codex-asb-ar1326-20260923.

- 2026-09-23T06:55:42+00:00: Recorded command exit 0; command argv SHA-256
  26a6ac86d00f2d8d134dfaf911d536f85b56f7839588790ec314c978682edf66.

- 2026-09-23T06:56:30+00:00: Recorded command exit 0; command argv SHA-256
  7b80382008cb01e3ea6fa6e88054b624464f9801b40ed57f947b01892a686ae8.

- 2026-09-23T06:56:52+00:00: Serial full locked workspace test completed successfully: all
  applicable tests and doctests passed; only documented environment-dependent tests were ignored. PR
  #250 hosted AArch64 emulation, Rust checks, and policy/supply-chain still running.

- 2026-09-23T06:57:01+00:00: Heartbeat by codex-asb-ar1326-20260923.

- 2026-09-23T06:57:31+00:00: Heartbeat by codex-asb-ar1326-20260923.

- 2026-09-23T06:57:54+00:00: Recorded command exit 1; command argv SHA-256
  056bdd1dc09150649ac976e2f57ef7edb1196c17626037dd91e41566fd18f9eb.

- 2026-09-23T06:58:21+00:00: Recorded command exit 0; command argv SHA-256
  470db9a27a5b9ffbd58dfcd670a0b7322a599f10a8a4f8c40bc31d4d2627c0eb.

- 2026-09-23T06:58:35+00:00: Heartbeat by codex-asb-ar1326-20260923.

- 2026-09-23T06:58:44+00:00: Recorded command exit 0; command argv SHA-256
  056bdd1dc09150649ac976e2f57ef7edb1196c17626037dd91e41566fd18f9eb.

- 2026-09-23T06:59:45+00:00: Heartbeat by codex-asb-ar1326-20260923.

- 2026-09-23T07:00:33+00:00: Heartbeat by codex-asb-ar1326-20260923.

- 2026-09-23T07:01:34+00:00: Recorded command exit 0; command argv SHA-256
  05f37e86cfcc833d061bb9ad7ca0e27ec8426b7c252f5f4a8d579c598977de18.

- 2026-09-23T07:01:58+00:00: Heartbeat by codex-asb-ar1326-20260923.

- 2026-09-23T07:02:13+00:00: Post-merge transition recorded. Rust failure is an existing
  timing-flake candidate, not an OpenRouter-specific failure; exact test passes locally serially.
  Merge is complete but AR acceptance remains pending repair/rerun and remaining workflows.

- 2026-09-23T07:02:18+00:00: Recorded command exit 1; command argv SHA-256
  e443b09ae650958d9f0bdcb3fb298485b41ea5c90d3dad46ada881ae3623f52e.

- 2026-09-23T07:02:40+00:00: Recorded command exit 0; command argv SHA-256
  c314f9156ca8a131aa5bdc960bd2c85fd620f5fda403529dbc64d9143f4dadcf.
