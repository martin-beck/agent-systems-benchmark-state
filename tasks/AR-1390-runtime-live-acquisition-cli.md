---
{
  "branch": "feature/ar-1390-runtime-live-acquisition-cli",
  "checkpoint_commit": "10bffbf015bd7ca78d8c0d18f04cf0190195e933",
  "claim_expires": "",
  "depends_on": [
    "AR-1388",
    "AR-1385",
    "AR-1373",
    "AR-1366",
    "AR-1341",
    "AR-1342",
    "AR-1339",
    "AR-1340"
  ],
  "id": "AR-1390",
  "next_action": "Claim the pre-bound isolated worktree, implement the runtime-owned live acquisition and normal CLI run/sweep bridge, and publish a signed PR.",
  "observed_branch": "feature/ar-1390-runtime-live-acquisition-cli",
  "observed_dirty": 0,
  "observed_head": "10bffbf015bd7ca78d8c0d18f04cf0190195e933",
  "owner": "",
  "plan": "../plans/AR-1390-runtime-live-acquisition-cli.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "blocked",
  "summary": "Compose runtime-owned live provider acquisition and wire it into normal ASB run and sweep.",
  "task_revision": 11,
  "title": "Runtime live acquisition and CLI bridge",
  "updated_at": "2026-09-24T07:42:38+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1390-runtime-live-acquisition-cli"
}
---

This AR is the narrowly scoped production successor required to unblock
AR-1329. It must not touch asb-tui, accept synthetic authority, or make an
external provider connection a development or CI requirement.

- 2026-09-24T07:36:40+00:00: All runtime authority, receipt, egress, namespace, and relay
  dependencies verified done; promote production-owned live acquisition/CLI bridge successor for
  AR-1329.

- 2026-09-24T07:37:45+00:00: Claimed by codex-asb-ar1329-repair-luna56.

- 2026-09-24T07:39:29+00:00: Recorded command exit 1; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-24T07:39:48+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-24T07:40:16+00:00: Recorded command exit 0; command argv SHA-256
  b424a9b48859c95f2c076c63eb8af7f081718e87da9bcd44a60969f81404e3fb.

- 2026-09-24T07:40:46+00:00: Recorded command exit 0; command argv SHA-256
  c92caf7f39494d198847900edc43cf7c243b341a47fb86efeccb7360fffc79cd.

- 2026-09-24T07:41:33+00:00: Blocked after protected-main audit: normal asb run/sweep still has no
  runtime/control-owned constructor that obtains an authenticated receipt/chain, resolves private
  bootstrap policy/allowlist/lease/relay/tool authority, mints LiveProviderRuntimeHandle, and passes
  the opaque source into the normal CLI entrypoint. Existing
  LiveProviderRuntimeDispatchSource::from_handle and CLI source bridge require an externally
  injected opaque handle/source; adding a handle-to-source facade would not satisfy acceptance and
  would falsely claim AR-1329 unblocked. Worktree reverted clean at checkpoint
  10bffbf015bd7ca78d8c0d18f04cf0190195e933. Focused existing gates pass; no commit or PR published.

## Current development and CI qualification boundary

The mandatory development and CI qualification path for this AR is a deterministic
local provider/LLM mock (LiteLLM-compatible where practical), including hostile
negative tests and offline replay where applicable. External/live OpenRouter or
other provider reachability is optional supplementary evidence only; it is never a
completion, dependency-readiness, or CI gate. Production egress policy, credential
non-disclosure, runtime-owned authority, namespace/relay attestation, cancellation
and teardown, and fail-closed denial of unapproved external traffic remain required
contracts. Existing live-provider dependency edges describe production integration
ordering only and must not be used to block local qualification or to claim external
reachability.
