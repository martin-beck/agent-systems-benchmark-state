---
{
  "branch": "feature/ar-1328-openrouter-free-model-config",
  "checkpoint_commit": "4fc4dbbe0af22756994904cdd186f99caa34c805",
  "claim_expires": "2026-09-23T10:17:40+00:00",
  "depends_on": [
    "AR-1325",
    "AR-1326",
    "AR-1100"
  ],
  "id": "AR-1328",
  "next_action": "Monitor PR #254 exact head 4fc4dbb hosted checks after Windows-safe symlink test repair; merge only after every required check and independent review are green.",
  "observed_branch": "feature/ar-1328-openrouter-free-model-config",
  "observed_dirty": 1,
  "observed_head": "4fc4dbbe0af22756994904cdd186f99caa34c805",
  "owner": "codex-asb-ar1328-20260923",
  "plan": "../plans/AR-1328.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Persist the per-user OpenRouter free-model configuration and credential-free key enrollment.",
  "task_revision": 115,
  "title": "OpenRouter free-model user configuration and key enrollment",
  "updated_at": "2026-09-23T08:18:29+00:00",
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

- 2026-09-23T07:44:02+00:00: Recorded command exit 0; command argv SHA-256
  39129b49e499c43e82be4a8f242e7d349182433a2abf400b3a9b1361019c8649.

- 2026-09-23T07:44:43+00:00: Recorded command exit 101; command argv SHA-256
  534f8613e1c316db8f0f46dd989e44e14a8ca74304a94791b4e4a1c59b2fbb1d.

- 2026-09-23T07:44:56+00:00: Heartbeat by codex-asb-ar1328-20260923.

- 2026-09-23T07:45:07+00:00: Recorded command exit 0; command argv SHA-256
  ef19043205064ea87bec66574bfe246191c9311bc8c404cd8e347d08fbdc44f0.

- 2026-09-23T07:45:26+00:00: Recorded command exit 0; command argv SHA-256
  4a4ff35f6232ccc0515ee27b9d01ddf6b58afae04bb15b4c9da6491feca7a617.

- 2026-09-23T07:45:39+00:00: Recorded command exit 0; command argv SHA-256
  4f57a11aa2bf274c43f195a4ed92cb47353997648897f1204b3e52caa033dfda.

- 2026-09-23T07:45:53+00:00: Recorded command exit 0; command argv SHA-256
  39129b49e499c43e82be4a8f242e7d349182433a2abf400b3a9b1361019c8649.

- 2026-09-23T07:46:20+00:00: Replacement worker audit complete: existing implementation commit
  2aa39d9 was reviewed; clippy repair 2c392a3 and provenance repair ec92cf8 are signed/DCO and
  pushed. Focused config/CLI/workflow tests pass; PR #254 exact head is ec92cf8.

- 2026-09-23T07:47:18+00:00: Recorded command exit 101; command argv SHA-256
  534f8613e1c316db8f0f46dd989e44e14a8ca74304a94791b4e4a1c59b2fbb1d.

- 2026-09-23T07:48:06+00:00: Recorded command exit 0; command argv SHA-256
  7b80382008cb01e3ea6fa6e88054b624464f9801b40ed57f947b01892a686ae8.

- 2026-09-23T07:49:12+00:00: Heartbeat by codex-asb-ar1328-20260923.

- 2026-09-23T07:49:37+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-23T07:49:50+00:00: Recorded command exit 0; command argv SHA-256
  31a05f46a65b4172cfcc5ef4e1ed2b4ddd54c042ac56eff6dc51f4205a4051b1.

- 2026-09-23T07:50:03+00:00: Recorded command exit 0; command argv SHA-256
  36526a6e9ff3db476eb511221f8972449d92d2caa68260e3e97de3b8a6725047.

- 2026-09-23T07:50:17+00:00: Recorded command exit 1; command argv SHA-256
  2164a265a9f2dc772aac4d3ce0e17c284ec4a139db706bf463a4d744ce00d78e.

- 2026-09-23T07:50:30+00:00: Heartbeat by codex-asb-ar1328-20260923.

- 2026-09-23T07:50:33+00:00: Recorded command exit 0; command argv SHA-256
  39129b49e499c43e82be4a8f242e7d349182433a2abf400b3a9b1361019c8649.

- 2026-09-23T07:50:46+00:00: Fixed hosted Rust/rustdoc failure: unresolved intra-doc link to
  credential_environment in asb-config. Replaced with explicit OPENROUTER_API_KEY channel text.
  Signed+DCO commit 7dd39bc pushed to PR #254. Local evidence: cargo fmt check, RUSTDOCFLAGS=-D
  warnings cargo doc --locked --workspace --no-deps, and locked asb-cli/asb-config tests all pass.
  Hosted rerun is active at exact head 7dd39bc; mergeState currently UNSTABLE while checks run.

- 2026-09-23T07:51:28+00:00: Heartbeat by codex-asb-ar1328-20260923.

- 2026-09-23T07:51:36+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-23T07:51:52+00:00: Recorded command exit 0; command argv SHA-256
  31a05f46a65b4172cfcc5ef4e1ed2b4ddd54c042ac56eff6dc51f4205a4051b1.

- 2026-09-23T07:52:13+00:00: Recorded command exit 0; command argv SHA-256
  1024fc1e6cefa31b078f0b5d2ed85c7ea4586897b388bf1e308f62db58574461.

- 2026-09-23T07:52:32+00:00: Recorded command exit 0; command argv SHA-256
  125aef7109cef83022b093c81a022e0f826cecdd5d92d2f55decb629e0742ce1.

- 2026-09-23T07:52:54+00:00: Heartbeat by codex-asb-ar1328-20260923.

- 2026-09-23T07:53:02+00:00: Recorded command exit 0; command argv SHA-256
  aa75a47abb51c989607a90cde0d8370262f138508299c06ab69b5d163bb590db.

- 2026-09-23T07:53:52+00:00: Recorded command exit 0; command argv SHA-256
  aa75a47abb51c989607a90cde0d8370262f138508299c06ab69b5d163bb590db.

- 2026-09-23T07:54:31+00:00: Heartbeat by codex-asb-ar1328-20260923.

- 2026-09-23T07:54:38+00:00: Recorded command exit 0; command argv SHA-256
  aa75a47abb51c989607a90cde0d8370262f138508299c06ab69b5d163bb590db.

- 2026-09-23T07:55:31+00:00: Recorded command exit 0; command argv SHA-256
  aa75a47abb51c989607a90cde0d8370262f138508299c06ab69b5d163bb590db.

- 2026-09-23T07:55:46+00:00: Recorded command exit 0; command argv SHA-256
  aa75a47abb51c989607a90cde0d8370262f138508299c06ab69b5d163bb590db.

- 2026-09-23T07:56:07+00:00: Recorded command exit 0; command argv SHA-256
  ff803c6cdf8d1d7b697e05f3c4f478d60c6821825b7e49c8d453c098735eb7f5.

- 2026-09-23T07:57:16+00:00: Recorded command exit 0; command argv SHA-256
  d340bb67d5f3d9a9b2334b1e88494e1dc0f57288706b4c72748a215dd693017e.

- 2026-09-23T07:58:51+00:00: Recorded command exit 101; command argv SHA-256
  6541657f00bf5668f46bdeb18363d9bbfec1d5ccd3a72f3118538e087c5731d7.

- 2026-09-23T08:00:42+00:00: Recorded command exit 0; command argv SHA-256
  6541657f00bf5668f46bdeb18363d9bbfec1d5ccd3a72f3118538e087c5731d7.

- 2026-09-23T08:01:33+00:00: Recorded command exit 101; command argv SHA-256
  d340bb67d5f3d9a9b2334b1e88494e1dc0f57288706b4c72748a215dd693017e.

- 2026-09-23T08:03:23+00:00: Recorded command exit 1; command argv SHA-256
  b472e049a034b1e0694a8a7b5a51336302c20f4417d089abfea2589ac9b1e217.

- 2026-09-23T08:04:09+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-23T08:04:22+00:00: Recorded command exit 0; command argv SHA-256
  31a05f46a65b4172cfcc5ef4e1ed2b4ddd54c042ac56eff6dc51f4205a4051b1.

- 2026-09-23T08:04:36+00:00: Recorded command exit 0; command argv SHA-256
  6541657f00bf5668f46bdeb18363d9bbfec1d5ccd3a72f3118538e087c5731d7.

- 2026-09-23T08:04:54+00:00: Recorded command exit 0; command argv SHA-256
  36526a6e9ff3db476eb511221f8972449d92d2caa68260e3e97de3b8a6725047.

- 2026-09-23T08:05:07+00:00: Recorded command exit 1; command argv SHA-256
  79f6b894f3cd5bc3262fdfe9ae9ba65b54adccd1cc071b678d6ae2bc1f4da437.

- 2026-09-23T08:05:56+00:00: Heartbeat by codex-asb-ar1328-20260923.

- 2026-09-23T08:06:16+00:00: Coverage repair: signed+DCO commit 0f77c87 added persisted-config
  positive/negative CLI tests; signed+DCO commit fc04eba added 11 OpenRouter identity/enrollment
  rejection cases and refreshed the provenance digest. Focused asb-config 17/17 and asb-cli config
  tests 2/2 pass. Initial hosted coverage failure was workspace 87.94% below the unchanged 90%
  floor; a local full llvm-cov rerun was invalidated by a concurrent cargo target binary race, so
  hosted exact-head coverage is authoritative.

- 2026-09-23T08:06:27+00:00: Recorded command exit 0; command argv SHA-256
  aa75a47abb51c989607a90cde0d8370262f138508299c06ab69b5d163bb590db.

- 2026-09-23T08:07:17+00:00: Recorded command exit 0; command argv SHA-256
  aa75a47abb51c989607a90cde0d8370262f138508299c06ab69b5d163bb590db.

- 2026-09-23T08:07:35+00:00: Heartbeat by codex-asb-ar1328-20260923.

- 2026-09-23T08:07:57+00:00: Heartbeat by codex-asb-ar1328-20260923.

- 2026-09-23T08:08:25+00:00: Recorded command exit 0; command argv SHA-256
  aa75a47abb51c989607a90cde0d8370262f138508299c06ab69b5d163bb590db.

- 2026-09-23T08:09:14+00:00: Recorded command exit 0; command argv SHA-256
  aa75a47abb51c989607a90cde0d8370262f138508299c06ab69b5d163bb590db.

- 2026-09-23T08:10:03+00:00: Recorded command exit 0; command argv SHA-256
  aa75a47abb51c989607a90cde0d8370262f138508299c06ab69b5d163bb590db.

- 2026-09-23T08:10:21+00:00: Heartbeat by codex-asb-ar1328-20260923.

- 2026-09-23T08:11:05+00:00: Recorded command exit 8; command argv SHA-256
  a8c05c63b8cf962ed7bb36a3b5144cd9db88894fb72c16f100ff04cbd4e9c35d.

- 2026-09-23T08:11:24+00:00: Recorded command exit 0; command argv SHA-256
  9fc0a2187517fc425d55024344df15268554f985b0bc78b3734023d7b9d6b335.

- 2026-09-23T08:11:47+00:00: Recorded command exit 0; command argv SHA-256
  17f68b9dff62ed0333edd220a6807aa8a1c75d53e1ec59281645255d684aaeeb.

- 2026-09-23T08:12:32+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-23T08:12:46+00:00: Recorded command exit 0; command argv SHA-256
  31a05f46a65b4172cfcc5ef4e1ed2b4ddd54c042ac56eff6dc51f4205a4051b1.

- 2026-09-23T08:12:59+00:00: Recorded command exit 0; command argv SHA-256
  36526a6e9ff3db476eb511221f8972449d92d2caa68260e3e97de3b8a6725047.

- 2026-09-23T08:13:12+00:00: Recorded command exit 0; command argv SHA-256
  172471c007341687352ec8f7095457939dd0e724ca8c3a18cf053a9268b3f3c9.

- 2026-09-23T08:13:30+00:00: Recorded command exit 0; command argv SHA-256
  39129b49e499c43e82be4a8f242e7d349182433a2abf400b3a9b1361019c8649.

- 2026-09-23T08:14:01+00:00: Heartbeat by codex-asb-ar1328-20260923.

- 2026-09-23T08:14:14+00:00: Independent review found 184f8e9 imported std::os::unix::fs::symlink in
  an unconditionally compiled test. Added signed+DCO 4fc4dbb with #[cfg(unix)] around that fixture;
  cargo fmt and asb-config 22/22 tests pass. Exact PR head is now 4fc4dbb; hosted checks restarted.

- 2026-09-23T08:14:25+00:00: Recorded command exit 0; command argv SHA-256
  aa75a47abb51c989607a90cde0d8370262f138508299c06ab69b5d163bb590db.

- 2026-09-23T08:15:18+00:00: Recorded command exit 0; command argv SHA-256
  aa75a47abb51c989607a90cde0d8370262f138508299c06ab69b5d163bb590db.

- 2026-09-23T08:15:36+00:00: Heartbeat by codex-asb-ar1328-20260923.

- 2026-09-23T08:16:21+00:00: Recorded command exit 0; command argv SHA-256
  aa75a47abb51c989607a90cde0d8370262f138508299c06ab69b5d163bb590db.

- 2026-09-23T08:17:22+00:00: Recorded command exit 0; command argv SHA-256
  aa75a47abb51c989607a90cde0d8370262f138508299c06ab69b5d163bb590db.

- 2026-09-23T08:17:40+00:00: Heartbeat by codex-asb-ar1328-20260923.

- 2026-09-23T08:18:29+00:00: Recorded command exit 0; command argv SHA-256
  aa75a47abb51c989607a90cde0d8370262f138508299c06ab69b5d163bb590db.
