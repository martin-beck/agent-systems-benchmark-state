---
{
  "branch": "feature/ar-1392-control-authority-materializer",
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
  "id": "AR-1392",
  "next_action": "Claim the pre-bound isolated worktree, implement the control-owned private authority resolver required by AR-1391, and publish a signed PR.",
  "observed_branch": "feature/ar-1392-control-authority-materializer",
  "observed_dirty": 0,
  "observed_head": "10bffbf015bd7ca78d8c0d18f04cf0190195e933",
  "owner": "",
  "plan": "../plans/AR-1392-control-authority-materializer.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "blocked",
  "summary": "Resolve private live authority from authenticated control enrollment without caller injection.",
  "task_revision": 4,
  "title": "Control-owned private authority materializer",
  "updated_at": "2026-09-24T07:46:33+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1392-control-authority-materializer"
}
---

This successor owns the control-side authority gap found by AR-1391. It must
not touch asb-tui, expose secrets, synthesize authority, or require external
provider connectivity in development or CI.

- 2026-09-24T07:45:20+00:00: Runtime authority dependencies verified; AR-1391 audit identifies
  missing private control authority materialization.

- 2026-09-24T07:46:08+00:00: Claimed by codex-asb-ar1329-repair-luna56.

- 2026-09-24T07:46:33+00:00: Protected-main audit confirms deeper missing primitive remains: control
  catalog RuntimeAuthorityRecord stores only digest metadata (credential reference, tool/lease/relay
  digests, target/generation), with no protected local authority resolver or durable private
  roots/tools/policy/allowlist/namespace/launch-token/teardown issuer. Runtime APIs require
  caller-supplied private inputs and CLI cannot access crate-private bootstrap APIs. No safe
  control-owned materializer can be implemented without inventing authority or accepting caller
  injection. Worktree clean at 10bffbf015bd7ca78d8c0d18f04cf0190195e933; no PR published.

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
