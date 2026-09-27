---
{
  "branch": "feature/ar-1391-runtime-control-bootstrap-constructor",
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
  "id": "AR-1391",
  "next_action": "Claim the pre-bound isolated worktree, implement the runtime/control-owned authenticated bootstrap constructor, and publish a signed PR.",
  "observed_branch": "feature/ar-1391-runtime-control-bootstrap-constructor",
  "observed_dirty": 0,
  "observed_head": "10bffbf015bd7ca78d8c0d18f04cf0190195e933",
  "owner": "",
  "plan": "../plans/AR-1391-runtime-control-bootstrap-constructor.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "blocked",
  "summary": "Materialize authenticated runtime live authority into an opaque source without caller injection.",
  "task_revision": 17,
  "title": "Runtime control bootstrap constructor",
  "updated_at": "2026-09-27T03:19:28+00:00",
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

- 2026-09-27T02:43:35+00:00: Recorded command exit 0; command argv SHA-256
  90d4d1fa26d86e71088cdeec2884e6f897ae597a058c5f04622551a8cf66e888.

- 2026-09-27T02:44:27+00:00: Bounded current-main audit complete: declared worktree is clean at
  10bffbf and protected origin/main is 363b21f. Current main contains authenticated
  receipt/profile/bootstrap internals, but no runtime/control-owned production constructor transfers
  a chain-bound opaque dispatch source to normal CLI run/sweep.
  LiveProviderRuntimeAuthorityProfile::materialize_handle remains crate-private and requires
  concrete policy/allowlist, lease/relay roots, pinned tools, credential capability, namespace and
  teardown authority; CLI only exposes injected-source helpers. Adding CLI/config/env inputs or
  synthetic local authority would violate fail-closed contracts. No product edits, no asb-tui, no
  live provider. Next action: after AR-1379 integration PR #344 is merged, re-audit current main and
  implement the narrow constructor only if runtime-owned inputs are available; otherwise create the
  next precise control/runtime source successor.

- 2026-09-27T03:16:59+00:00: AR-1379 merge 1e2c5911 is reported complete; resume for a fresh
  protected-main audit of runtime-owned bootstrap constructor availability before implementation.

- 2026-09-27T03:17:52+00:00: Claimed by ar1332_record_replay_luna56.

- 2026-09-27T03:18:10+00:00: Recorded command exit 0; command argv SHA-256
  db10c2b810ca2a05a2807fc1e3f072719794d3ac7ccc14bb48853c9d8e22e508.

- 2026-09-27T03:18:25+00:00: Recorded command exit 0; command argv SHA-256
  ff6d1fa7a7185010f75fcfafe4bdc1bdd5b9804d8c2b3e7abdd8a1b96cd81c63.

- 2026-09-27T03:18:53+00:00: Recorded command exit 0; command argv SHA-256
  8b2ab5e036f3d871625ce0fad918b320e4250fe3e6f3989f8fe9ff888f148056.

- 2026-09-27T03:19:28+00:00: Fresh audit after protected-main merge
  1e2c59119820bc073ea4c6736782f5041a395a28: current CLI still dispatches normal run/sweep with no
  runtime/control source; only run_with_runtime_live_provider_source accepts an externally injected
  opaque source. asb-runtime still exposes only crate-private
  LiveProviderRuntimeAuthorityProfile::materialize_handle requiring policy/allowlist, lease/relay
  roots, tool pins, credential capability, namespace and teardown inputs; RuntimeAuthorityRecord
  remains digest metadata without a resolver for those private inputs. AR-1379 merge did not supply
  the missing runtime-owned bootstrap constructor. No product/asb-tui/live-provider edits. Next
  action: create/promote a new narrow runtime/control enrollment-source successor defining the owner
  of concrete bootstrap inputs and opaque transfer, then re-audit normal run/sweep; do not weaken
  authority gates.
