---
{
  "branch": "feature/ar-1450-runtime-owned-local-replay-acquisition",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1448"
  ],
  "id": "AR-1450",
  "next_action": "Blocked: a public factory accepting SandboxLaunchInput, ResourceLease and SandboxBackend would violate runtime ownership. Promote a reviewed runtime-owned provisioning design; no product change was published.",
  "observed_branch": "feature/ar-1450-runtime-owned-local-replay-acquisition",
  "observed_dirty": 0,
  "observed_head": "e4d2c821d160256df4e00df4f165aa69a54d69e6",
  "owner": "",
  "plan": "../plans/AR-1450.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "blocked",
  "summary": "Keep local replay authority acquisition inside the runtime boundary.",
  "task_revision": 8,
  "title": "Runtime-owned local replay acquisition factory",
  "updated_at": "2026-09-25T17:01:55+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1450-runtime-owned-local-replay-acquisition"
}
---
AR-1449 proved that the ordinary CLI cannot safely call AR-1448 because authority issuance still requires caller-built sandbox, lease, backend and relay objects. This task moves only their acquisition into asb-runtime.

Requirements:
- accept only a validated cassette digest; reject malformed, stale, copied and mismatched identities before side effects;
- provision bounded private replay relay, benchmark lease and NetworkPolicy::Deny launch input in runtime;
- perform backend attestation and return opaque one-shot authority;
- guarantee cancellation, teardown, no secret or provider network access, and no alternate egress;
- add positive and hostile offline tests; no live provider or native host requirement;
- expose a narrow API that asb-cli can consume without constructing authority.

- 2026-09-25T16:59:00+00:00: Claimed by ar1450-replay-luna56.

- 2026-09-25T17:00:26+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-25T17:00:49+00:00: Recorded command exit 0; command argv SHA-256
  65bd39b6e995daa8de012e38f77d7d34e17aaa7f48f7d1538e37af30d16d3784.

- 2026-09-25T17:01:05+00:00: Recorded command exit 0; command argv SHA-256
  24503ef668e612b07a646bfcdc91f2dce6cd0768756ff9bc94993a66bbbfcdb6.

- 2026-09-25T17:01:55+00:00: Independent audit stopped before publication: a public factory
  constructor accepting SandboxLaunchInput, ResourceLease and SandboxBackend would preserve the
  AR-1449 boundary violation. Current AR-1448 primitives lack a runtime-owned provisioning
  entrypoint; no product change published.
