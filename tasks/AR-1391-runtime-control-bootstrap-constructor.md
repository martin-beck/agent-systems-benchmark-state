---
{
  "branch": "feature/ar-1391-runtime-control-bootstrap-constructor",
  "checkpoint_commit": "10bffbf015bd7ca78d8c0d18f04cf0190195e933",
  "claim_expires": "2026-09-27T04:42:28+00:00",
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
  "id": "AR-1391",
  "next_action": "Claim the pre-bound isolated worktree, implement the runtime/control-owned authenticated bootstrap constructor, and publish a signed PR.",
  "observed_branch": "feature/ar-1391-runtime-control-bootstrap-constructor",
  "observed_dirty": 0,
  "observed_head": "10bffbf015bd7ca78d8c0d18f04cf0190195e933",
  "owner": "ar1332_record_replay_luna56",
  "plan": "../plans/AR-1391-runtime-control-bootstrap-constructor.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Materialize authenticated runtime live authority into an opaque source without caller injection.",
  "task_revision": 9,
  "title": "Runtime control bootstrap constructor",
  "updated_at": "2026-09-27T02:43:20+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1391-runtime-control-bootstrap-constructor"
}
---

This narrow successor owns the missing authority source identified by the
AR-1390 audit. It must not touch asb-tui, synthesize authority, or require an
external provider connection for development or CI.

- 2026-09-24T07:42:41+00:00: Runtime authority dependencies verified; AR-1390 audit identified this
  exact missing authenticated constructor.

- 2026-09-24T07:43:46+00:00: Claimed by codex-asb-ar1329-repair-luna56.

- 2026-09-24T07:44:12+00:00: Protected-main audit confirms no production runtime/control-owned
  bootstrap constructor exists. asb-cli RuntimeAuthorityRecord and RuntimeReceipt expose only
  authenticated digest metadata; no resolver supplies private lease/relay roots, egress
  policy/allowlist, pinned tools, namespace identity, credential capability, or teardown authority.
  Existing LiveProviderRuntimeBootstrapSpec::from_enrollment and materialize_handle are
  crate-private and require caller-supplied private inputs; existing CLI source bridge accepts
  externally injected opaque source. Implementing a facade would violate acceptance and fabricate
  authority. Worktree remains clean at checkpoint 10bffbf015bd7ca78d8c0d18f04cf0190195e933; no PR
  published.

## Current development and CI qualification boundary

The mandatory development and CI qualification path for this AR is a deterministic
local provider/LLM mock (LiteLLM-compatible where practical), including hostile
negative tests and offline replay where applicable. External/live OpenRouter orchanged=110

other provider reachability is optional supplementary evidence only; it is never a
completion, dependency-readiness, or CI gate. Production egress policy, credential
non-disclosure, runtime-owned authority, namespace/relay attestation, cancellation
and teardown, and fail-closed denial of unapproved external traffic remain required
contracts. Existing live-provider dependency edges describe production integration
ordering only and must not be used to block local qualification or to claim external
reachability.

- 2026-09-27T02:42:23+00:00: Dependencies AR-1388, AR-1385, AR-1373, AR-1366, AR-1341, AR-1342,
  AR-1339, and AR-1340 are durably done. Resume this narrow successor for the runtime/control-owned
  authenticated bootstrap constructor identified by AR-1387; no CLI authority exposure, live
  provider, or asb-tui.

- 2026-09-27T02:42:28+00:00: Claimed by ar1332_record_replay_luna56.

- 2026-09-27T02:42:44+00:00: Recorded command exit 0; command argv SHA-256
  ff6d1fa7a7185010f75fcfafe4bdc1bdd5b9804d8c2b3e7abdd8a1b96cd81c63.

- 2026-09-27T02:43:05+00:00: Recorded command exit 0; command argv SHA-256
  9c86c49433e8910ce448b09860062c402216cfc3a7a8bab60a0474bcb3073a8e.

- 2026-09-27T02:43:20+00:00: Recorded command exit 0; command argv SHA-256
  97149e1fed9062e061094f8d0a0d921c8b355d8216f566ba7202ede70be3c2aa.
