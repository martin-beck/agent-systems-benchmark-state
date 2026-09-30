---
{
  "branch": "feature/ar-1367-ar1329-production-dispatch-integration",
  "checkpoint_commit": "0c6dc52e1f4aa5854f73081711dbd9a5bc1a5d7c",
  "claim_expires": "",
  "depends_on": [
    "AR-1366",
    "AR-1340",
    "AR-1339",
    "AR-1328"
  ],
  "id": "AR-1367",
  "next_action": "Development qualification complete on exact protected main with deterministic local/mock and strict-replay runtime authority. Deployment-owned live-provider materialization remains optional future hardening; no development action remains.",
  "observed_branch": "feature/ar-1367-ar1329-production-dispatch-integration",
  "observed_dirty": 0,
  "observed_head": "bf89a45ddd71af96e6d4b6954320e199e147f83e",
  "owner": "",
  "plan": "../plans/AR-1367-ar1329-production-dispatch-integration.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Development asb run/sweep dispatch is qualified with local/mock and strict replay; deployment-owned live-provider materialization is optional future hardening.",
  "task_revision": 30,
  "title": "AR-1329 production dispatch integration",
  "updated_at": "2026-09-29T22:58:12+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1367-ar1329-production-dispatch-integration"
}
---

Successor for the blocked AR-1329 execution path. For development, qualify the
existing ordinary run/sweep bridge with deterministic local/mock and strict
replay, without touching asb-tui or exposing authority through CLI/config
input. This does not claim live-provider readiness.

- 2026-09-30T06:45:00+00:00: Development path is satisfied by the exact-main AR-1390/1374
  dispatch qualification receipts. No deployment-owned authenticated source or external provider
  is required; live-provider materialization remains optional future hardening.

- 2026-09-24T00:44:01+00:00: Promote fresh AR-1329 successor after runtime-owned receipt consumer
  AR-1366 completed; preserve fail-closed live execution.

- 2026-09-24T00:44:03+00:00: Claimed by codex-asb-runtime-attested-enrollment-luna56.

- 2026-09-24T00:44:25+00:00: Heartbeat by codex-asb-runtime-attested-enrollment-luna56.

- 2026-09-24T00:44:27+00:00: Recorded command exit 0; command argv SHA-256
  0f4a57e84077aa2aca93b43c7a5076f72dc40bc5f95460fbb317d7cc68fa264b.

- 2026-09-24T00:46:04+00:00: Blocked truthfully after fresh production dispatch audit: CLI run/sweep
  only accepts an injected LiveProviderAttemptFactory, and ordinary CLI has no authenticated
  ControlClient receipt operation or runtime-owned enrollment source. Existing AR-1366 consumer is
  only an in-process response validator; it cannot materialize authority. No safe product mutation
  was made. Successor AR-1368 created to add the missing authenticated ControlClient receipt source;
  AR-1329 remains fail-closed.

- 2026-09-24T05:39:05+00:00: AR-1384 is terminal done; resume this previously blocked AR-1329
  successor for runtime-owned production dispatch integration.

- 2026-09-24T05:39:13+00:00: Claimed by codex-asb-ar1329-repair-luna56.

- 2026-09-24T05:39:46+00:00: Recorded command exit 0; command argv SHA-256
  a1159e9df3670d549d04524532629f5477ceb7deec9b45e47e8c009506ecb2c8.

- 2026-09-24T05:40:01+00:00: Recorded command exit 0; command argv SHA-256
  321c534968b9c456a64caf5e6d09b63780c507f97548057d2bfe31edcfd73ff4.

- 2026-09-24T05:40:39+00:00: Recorded command exit 0; command argv SHA-256
  b7c438686581cf292b6cd41497ceabb3af42dfed57e04dfd6cc89efed8e2d15b.

- 2026-09-24T05:41:16+00:00: Recorded command exit 0; command argv SHA-256
  eee0bfe7b8074d9284501372a84dfcfb185292346be3ff70334878a6c5c469df.

- 2026-09-24T05:41:51+00:00: Heartbeat by codex-asb-ar1329-repair-luna56.

- 2026-09-24T05:42:25+00:00: Post-AR-1384 audit remains blocked: asb-cli normal run/sweep has no
  runtime-owned enrollment/source. LiveProviderRuntimeAuthorityProfile::materialize_handle is
  crate-private and requires config, policy, allowlist, relay root, tool pins;
  LiveProviderRuntimeService::acquire_from_enrollment still requires an externally constructed
  LiveProviderEnrollment. Supplying these through CLI or synthesizing them violates authority
  boundaries. Focused CLI live-gate test passes; no safe product diff. Coordinator must create a
  narrowly scoped runtime-owned source/CLI bridge successor.

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

- 2026-09-29T22:24:51+00:00: Dependencies are complete; re-audit the protected-main production
  dispatch seam against canonical AR-1523 without requiring live provider reachability for
  development.

- 2026-09-29T22:24:53+00:00: Claimed by coordinator-ar1367-production-dispatch-20260930.

- 2026-09-29T22:25:11+00:00: Recorded command exit 0; command argv SHA-256
  fc3a21ba950e863d0e622614c1e221ea1ffa0f289610c02afcd4229a95fb1b05.

- 2026-09-29T22:25:28+00:00: Recorded command exit 0; command argv SHA-256
  d1c8186c6c83e370a511410072acacb20cb44ca600da6d9a56b39214a6e9f7fd.

- 2026-09-29T22:29:51+00:00: Heartbeat by coordinator-ar1367-production-dispatch-20260930.

- 2026-09-29T22:30:00+00:00: Recorded command exit 0; command argv SHA-256
  1f77f0a8a53061fcd85f9fe998aefee958ccee86048f742e3840d8ca5d8b8fa5.

- 2026-09-29T22:51:09+00:00: Heartbeat by coordinator-ar1367-production-dispatch-20260930.

- 2026-09-29T22:51:42+00:00: Exact protected-main audit at bf89a45ddd71af96e6d4b6954320e199e147f83e:
  PlanAuthoritySource in crates/asb-cli/src/control.rs rejects ExecutionMode::Live; ordinary CLI has
  no authenticated runtime/control enrollment source. Runtime acquire_from_record/materialization
  remains crate-private and requires a platform-owned source. Existing local/mock and strict-replay
  paths remain intact. No product mutation; route the production bridge to canonical AR-1523.

- 2026-09-29T22:57:53+00:00: Reopen only to correct durable next action after the exact
  production-dispatch audit; live authority source remains unavailable.

- 2026-09-29T22:57:56+00:00: Claimed by coordinator-ar1367-metadata-20260930.

- 2026-09-29T22:58:09+00:00: Corrected durable next action after exact production-dispatch audit; no
  product mutation.

- 2026-09-29T22:58:12+00:00: Durable next action corrected. Exact protected-main audit remains
  valid: PlanAuthoritySource rejects live mode and no authenticated platform-owned authority source
  exists; AR-1523 owns the blocker.
