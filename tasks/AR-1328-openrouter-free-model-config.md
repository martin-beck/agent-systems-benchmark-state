---
{
  "branch": "feature/ar-1328-openrouter-free-model-config",
  "checkpoint_commit": "2aa39d98553e7d5c25a8cc85decb4a17e58242ba",
  "claim_expires": "2026-09-23T09:43:12+00:00",
  "depends_on": [
    "AR-1325",
    "AR-1326",
    "AR-1100"
  ],
  "id": "AR-1328",
  "next_action": "Monitor PR #254 exact-head CI; after merge verify post-merge checks and then close AR-1328 with durable evidence.",
  "observed_branch": "feature/ar-1328-openrouter-free-model-config",
  "observed_dirty": 0,
  "observed_head": "2c392a30e47da237e35f3b4e85b8342171fd55a6",
  "owner": "codex-asb-ar1328-20260923",
  "plan": "../plans/AR-1328.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Persist the per-user OpenRouter free-model configuration and credential-free key enrollment.",
  "task_revision": 34,
  "title": "OpenRouter free-model user configuration and key enrollment",
  "updated_at": "2026-09-23T07:43:57+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1328-openrouter-free-model-config"
}
---

The AR-1325/AR-1326 work makes the OpenRouter profile selectable through the
CLI catalog, but the selection and its credential still live only in process
memory or shell state: the AR-1100 `asb-config` crate owns the
credential-free `AuthEnrollment` and `CredentialReference` boundary, yet the CLI
has no `--use-config` wiring and no way to persist a pinned free-model OpenRouter
selection. This AR defines the durable per-user configuration that names the
exact free model, binds the credential reference digest to the
`OPENROUTER_API_KEY` environment channel, and loads it through the CLI without
ever writing a secret to disk. Unsupported, stale, or credential-bearing
configurations fail closed.

- 2026-09-23T07:30:47+00:00: Dependencies AR-1325 and AR-1326 are released; AR-1100 is done. Promote
  next OpenRouter user-configuration AR while AR-1327 post-merge verification continues.

- 2026-09-23T07:31:24+00:00: Claimed by codex-asb-ar1328-20260923.

- 2026-09-23T07:31:58+00:00: Recorded command exit 0; command argv SHA-256
  d7eb8d802ae6845423749ce62fb86178fe290e3c7376ab62af304a8b5f5ba983.

- 2026-09-23T07:35:02+00:00: Recorded command exit 101; command argv SHA-256
  31a05f46a65b4172cfcc5ef4e1ed2b4ddd54c042ac56eff6dc51f4205a4051b1.

- 2026-09-23T07:35:29+00:00: Recorded command exit 0; command argv SHA-256
  31a05f46a65b4172cfcc5ef4e1ed2b4ddd54c042ac56eff6dc51f4205a4051b1.

- 2026-09-23T07:35:43+00:00: Heartbeat by codex-asb-ar1328-20260923.

- 2026-09-23T07:36:59+00:00: Implemented credential-free OpenRouterFreeModelConfig enrollment and
  optional Configuration persistence with strict dated snapshot, environment locator digest,
  enrollment binding, tamper rejection, and round-trip tests. asb-config tests pass (16/16). CLI
  dependency and initial config dispatch are staged; CLI currently fails compile only because
  configure_openrouter is not yet defined and imports are temporarily unused while that
  implementation is completed.

- 2026-09-23T07:37:28+00:00: Recorded command exit 0; command argv SHA-256
  73d005d4c4983870f0c5405c6c97dffbf521d57825b14d75dae888988fbdcd03.

- 2026-09-23T07:37:53+00:00: Recorded command exit 101; command argv SHA-256
  7ff3c4ac9f6cba636658b049cbbe7eb339117982fe2d7125f73226a2f31e4c37.

- 2026-09-23T07:38:12+00:00: Recorded command exit 0; command argv SHA-256
  4acbbedcdf95da4d07c6d66a2d0ee0cad792e5208b7442787a35466c7da97290.

- 2026-09-23T07:38:29+00:00: Recorded command exit 0; command argv SHA-256
  65c6148bf907829069e536019d838d8e631fe06640051d1f5919aa7b1d29bfa9.

- 2026-09-23T07:38:47+00:00: Credential-free config command was exercised live in isolated XDG
  config: asb config openrouter persisted owner-private config with model snapshot, endpoint digest,
  env locator digest, and active generation; no API key material. provider-plan --use-config --agent
  codex passed with exact catalog digest and OpenRouter model. Remaining AR acceptance gap is
  --use-config wiring for plan/run/sweep (currently provider-plan only), then full locked gates/PR.

- 2026-09-23T07:39:26+00:00: Recorded command exit 1; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-23T07:39:40+00:00: Recorded command exit 101; command argv SHA-256
  73d005d4c4983870f0c5405c6c97dffbf521d57825b14d75dae888988fbdcd03.

- 2026-09-23T07:40:08+00:00: Heartbeat by codex-asb-ar1328-20260923.

- 2026-09-23T07:40:15+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-23T07:40:29+00:00: Recorded command exit 0; command argv SHA-256
  73d005d4c4983870f0c5405c6c97dffbf521d57825b14d75dae888988fbdcd03.

- 2026-09-23T07:41:38+00:00: Heartbeat by codex-asb-ar1328-20260923.

- 2026-09-23T07:41:59+00:00: Recorded command exit 0; command argv SHA-256
  3d4cc54827fa0ae5c402321266e4a8e9a84a69a17f7ff27b7a0f0c858d454784.

- 2026-09-23T07:42:13+00:00: Recorded command exit 0; command argv SHA-256
  31a05f46a65b4172cfcc5ef4e1ed2b4ddd54c042ac56eff6dc51f4205a4051b1.

- 2026-09-23T07:42:38+00:00: Recorded command exit 101; command argv SHA-256
  1024fc1e6cefa31b078f0b5d2ed85c7ea4586897b388bf1e308f62db58574461.

- 2026-09-23T07:42:59+00:00: Recorded command exit 0; command argv SHA-256
  1024fc1e6cefa31b078f0b5d2ed85c7ea4586897b388bf1e308f62db58574461.

- 2026-09-23T07:43:12+00:00: Heartbeat by codex-asb-ar1328-20260923.

- 2026-09-23T07:43:16+00:00: Recorded command exit 0; command argv SHA-256
  4ecddce6f52f0cd06bd20439afd80cdf1b56f2ecee19208f80d06182975be0a1.

- 2026-09-23T07:43:29+00:00: Recorded command exit 0; command argv SHA-256
  9a7d10d310c0482bfb5f5ef0dd112ea18645d6bf49884a05de2f4d79aa3367c4.

- 2026-09-23T07:43:57+00:00: Implemented and pushed signed+DCO commit 2aa39d9 and opened PR #254.
  Added credential-free OpenRouterFreeModelConfig persistence/enrollment, strict model
  snapshot/endpoint/credential binding, config command, provider-plan --use-config, and
  plan/run/sweep --use-config. Evidence: cargo fmt check; cargo test --locked --workspace passed;
  focused workflow transcript and asb-cli/asb-config tests passed; isolated XDG live
  config+provider-plan smoke passed without a key or network contact. Earlier cargo test invocation
  failed transiently with exit 101 while the workspace compile was still progressing; the same
  locked command completed successfully on rerun.
