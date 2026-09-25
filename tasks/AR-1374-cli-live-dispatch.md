---
{
  "branch": "feature/ar-1374-cli-live-dispatch",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1373",
    "AR-1339",
    "AR-1340",
    "AR-1328"
  ],
  "id": "AR-1374",
  "next_action": "Await dependency completion, then audit and implement runtime-owned asb run/sweep dispatch using the authenticated receipt source.",
  "observed_branch": "feature/ar-1374-cli-live-dispatch",
  "observed_dirty": 0,
  "observed_head": "265b936d995148f8e40e36664cf68bf12affc20d",
  "owner": "",
  "plan": "../plans/AR-1374-cli-live-dispatch.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "blocked",
  "summary": "Consume authenticated runtime receipts in production asb run and sweep dispatch.",
  "task_revision": 7,
  "title": "Production live-provider dispatch",
  "updated_at": "2026-09-24T02:35:32+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1374-cli-live-dispatch"
}
---

Successor to the completed authenticated receipt source AR-1373. This task
must not claim end-to-end OpenRouter readiness until real runtime/provider
execution and teardown are verified.

- 2026-09-24T02:35:00+00:00: Created as the dependency-valid successor for
  AR-1329 production run/sweep dispatch.

- 2026-09-24T02:33:21+00:00: Dependencies AR-1373, AR-1339, AR-1340, and AR-1328 verified done;
  promote production dispatch successor.

- 2026-09-24T02:33:24+00:00: Claimed by codex-asb-runtime-receipt-source-luna56.

- 2026-09-24T02:34:44+00:00: Heartbeat by codex-asb-runtime-receipt-source-luna56.

- 2026-09-24T02:34:47+00:00: Recorded command exit 0; command argv SHA-256
  383490be2620f3fb3c83962ffeae4899d14503b59efacb41425befcd94b7ac7c.

- 2026-09-24T02:35:32+00:00: Audit complete: CLI run/sweep accepts only an opaque
  LiveProviderAttemptFactory, and asb-runtime validates receipts only after an externally supplied
  response/chain. No authenticated control transport/chain source connects AR-1373 RuntimeReceipt to
  the CLI factory. No safe production implementation exists in this AR without synthesizing
  authority; AR-1375 created for the missing runtime-owned adapter.

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
