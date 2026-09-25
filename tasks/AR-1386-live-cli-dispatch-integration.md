---
{
  "branch": "feature/ar-1386-live-cli-dispatch-integration",
  "checkpoint_commit": "25548846966e37646dded8d67ed8ee5123b8bc32",
  "claim_expires": "",
  "depends_on": [
    "AR-1385",
    "AR-1384",
    "AR-1380",
    "AR-1381",
    "AR-1378",
    "AR-1377"
  ],
  "id": "AR-1386",
  "next_action": "Refresh the declared isolated worktree from protected main, integrate the authenticated runtime live dispatch source into production asb run and sweep, and add local provider-mock plus fail-closed egress/teardown tests.",
  "observed_branch": "feature/ar-1386-live-cli-dispatch-integration",
  "observed_dirty": 0,
  "observed_head": "25548846966e37646dded8d67ed8ee5123b8bc32",
  "owner": "",
  "plan": "../plans/AR-1386-live-cli-dispatch-integration.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "blocked",
  "summary": "Integrate authenticated runtime live dispatch into production asb run and sweep.",
  "task_revision": 10,
  "title": "Production live CLI dispatch integration",
  "updated_at": "2026-09-24T06:34:59+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1386-live-cli-dispatch-integration"
}
---

This repair consumes the opaque authenticated dispatch source from AR-1385 in
the actual production CLI path. It must preserve runtime-owned authority and
fail-closed network, credential, namespace, launch-token, lease, and teardown
boundaries.


- 2026-09-24T06:31:38+00:00: AR-1385 done; next coordinator repair integrates authenticated dispatch
  into production run and sweep; dependencies verified

- 2026-09-24T06:32:29+00:00: Claimed by codex-asb-ar1329-repair-luna56.

- 2026-09-24T06:32:32+00:00: Heartbeat by codex-asb-ar1329-repair-luna56.

- 2026-09-24T06:32:48+00:00: Recorded command exit 0; command argv SHA-256
  321c534968b9c456a64caf5e6d09b63780c507f97548057d2bfe31edcfd73ff4.

- 2026-09-24T06:33:08+00:00: Recorded command exit 0; command argv SHA-256
  b7c438686581cf292b6cd41497ceabb3af42dfed57e04dfd6cc89efed8e2d15b.

- 2026-09-24T06:34:27+00:00: Recorded command exit 0; command argv SHA-256
  eee0bfe7b8074d9284501372a84dfcfb185292346be3ff70334878a6c5c469df.

- 2026-09-24T06:34:59+00:00: Post-AR-1385 production audit: normal asb run/sweep --live-provider
  dispatch passes no runtime source (entry -> dispatch(..., None, None)); the safe source consumer
  exists only as run_with_runtime_live_provider_source and requires an opaque runtime-issued
  LiveProviderRuntimeDispatchSource. No authenticated ControlClient/authority bootstrap source is
  available in the CLI process. Adding CLI/config endpoints, credentials, policy, roots, tools, or
  synthetic local authority would violate AR-1386. Focused live-gate test passes; no safe product
  diff made. Coordinator must create the next narrowly scoped runtime/control bootstrap-to-CLI
  bridge repair.

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
