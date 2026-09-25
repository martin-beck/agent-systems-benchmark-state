---
{
  "branch": "feature/ar-1331-runtime-replay-launch-authority",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-25T17:47:57+00:00",
  "depends_on": [
    "AR-1443",
    "AR-1446"
  ],
  "id": "AR-1331",
  "next_action": "Promote and claim the ASB-local runtime replay authority repair. Provide runtime-owned ReplayLaunchAuthority for strict offline cassette replay, prove the CLI cannot fabricate one, and keep optional live capture AR-1330 separate.",
  "observed_branch": "feature/ar-1331-runtime-replay-launch-authority",
  "observed_dirty": 0,
  "observed_head": "2872a31f2ee90ac5df1a47203b2a618b1829cfec",
  "owner": "coordinator-ar1331",
  "plan": "../plans/AR-1331.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Deliver the runtime-owned strict-replay launch authority required by the replay CLI contract.",
  "task_revision": 6,
  "title": "Runtime-owned strict-replay launch authority",
  "updated_at": "2026-09-25T15:49:30+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1331-runtime-replay-launch-authority"
}
---

The replay CLI contract requires a `ReplayLaunchAuthority` that can only be
issued by the runtime, but no code path constructs one, so `asb replay` can
never run. This AR delivers the runtime-owned launch authority: a constructor-
or lifecycle-owned value that binds a live run context to the sealed cassettes
produced by AR-1330, is injected through the supervised context the CLI already
requires, and cannot be fabricated by a caller-supplied manifest or CLI flag.
Replay remains strict, offline-only, and without any fallback to a live
provider.

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

- 2026-09-25T15:47:55+00:00: ASB-local dependencies AR-1443 and AR-1446 are done; promote
  runtime-owned strict replay authority. Optional live capture AR-1330 remains separate.

- 2026-09-25T15:47:57+00:00: Claimed by coordinator-ar1331.

- 2026-09-25T15:48:16+00:00: Recorded command exit 0; command argv SHA-256
  019774536693c0853a036a3a6fafb2fb59bf34f301bd785dea167af8c4561e75.

- 2026-09-25T15:49:30+00:00: Recorded command exit 0; command argv SHA-256
  70f00fbfb55e500b653e236cbd5112375a0e7b0e67e03b689e99160a0664371f.
