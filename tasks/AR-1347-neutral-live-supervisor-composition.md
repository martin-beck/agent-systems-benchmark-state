---
{
  "branch": "feature/ar-1347-neutral-live-supervisor-composition",
  "checkpoint_commit": "625a250b527b51994be7653e24c3825512e5f449",
  "claim_expires": "2026-09-23T17:37:59+00:00",
  "depends_on": [
    "AR-1327",
    "AR-1328",
    "AR-1339",
    "AR-1340"
  ],
  "id": "AR-1347",
  "next_action": "Opaque CredentialInjection trait is implemented in asb-runtime and SandboxBackend exposes spawn_launch_with_credential without exposing bytes or changing NetworkPolicy::Deny. Add positive/negative injection tests and compose an asb-agents supervisor implementation; then wire runtime-owned live acquisition. AR-1329 remains fail-closed.",
  "observed_branch": "feature/ar-1347-neutral-live-supervisor-composition",
  "observed_dirty": 1,
  "observed_head": "625a250b527b51994be7653e24c3825512e5f449",
  "owner": "codex-asb-ar1329-live-cli-luna56",
  "plan": "../plans/AR-1347-neutral-live-supervisor-composition.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Add the dependency-safe opaque supervisor contract needed for live-provider acquisition.",
  "task_revision": 16,
  "title": "Neutral live-supervisor composition contract",
  "updated_at": "2026-09-23T15:43:15+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1347-neutral-live-supervisor-composition"
}
---

Created from the AR-1346 cross-crate audit. `ResolvedCredential` is private to
`asb-agents`, which already depends on `asb-runtime`; do not expose secret bytes
or introduce a cyclic dependency.

- 2026-09-23T15:37:56+00:00: Promote neutral cross-crate supervisor composition repair from AR-1346
  audit; dependencies complete and AR-1329 remains fail-closed.

- 2026-09-23T15:37:59+00:00: Claimed by codex-asb-ar1329-live-cli-luna56.

- 2026-09-23T15:39:17+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-23T15:39:48+00:00: Recorded command exit 0; command argv SHA-256
  a37d35e290b63ddfe8627f9bdb0474ef6d3f2654ade91f05cd9a55c3a713fceb.

- 2026-09-23T15:40:09+00:00: Recorded command exit 101; command argv SHA-256
  e8beebac0638d83321c84d952814966bbba80dc16ee7dd3d3ead10f3c2b72292.

- 2026-09-23T15:40:33+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-23T15:40:52+00:00: Recorded command exit 101; command argv SHA-256
  e8beebac0638d83321c84d952814966bbba80dc16ee7dd3d3ead10f3c2b72292.

- 2026-09-23T15:41:15+00:00: Recorded command exit 101; command argv SHA-256
  e8beebac0638d83321c84d952814966bbba80dc16ee7dd3d3ead10f3c2b72292.

- 2026-09-23T15:41:40+00:00: Recorded command exit 0; command argv SHA-256
  e8beebac0638d83321c84d952814966bbba80dc16ee7dd3d3ead10f3c2b72292.

- 2026-09-23T15:41:59+00:00: Recorded command exit 0; command argv SHA-256
  f71975b0e0b00a780fed3410ff70f306b8004ce22f8d1aecc438b8adc79fe8e9.

- 2026-09-23T15:42:37+00:00: AR-1347 worktree established from a336d674. Implemented signed+DCO
  commit 625a250: neutral CredentialInjection trait plus
  SandboxBackend::spawn_launch_with_credential, preserving existing spawn API. Initial clippy
  failures were repaired: too_many_arguments (allow on internal helper), needless_option_as_deref,
  unused_mut, and one test call missing the new None argument. Latest cargo clippy --locked -p
  asb-runtime --all-targets -- -D warnings passes; cargo check --locked --workspace and fmt check
  pass. Product still needs positive/negative injector tests and asb-agents composition; no AR-1329
  wiring.

- 2026-09-23T15:42:57+00:00: Recorded command exit 1; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-23T15:43:15+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.
