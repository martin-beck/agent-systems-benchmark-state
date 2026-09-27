---
{
  "branch": "feature/ar-1374-cli-live-dispatch",
  "checkpoint_commit": "4ee5a4ed843c7dd7dda0b92dbe392f3787b4039f",
  "claim_expires": "2026-09-27T04:11:08+00:00",
  "depends_on": [
    "AR-1373",
    "AR-1339",
    "AR-1340",
    "AR-1328"
  ],
  "id": "AR-1374",
  "next_action": "Unblock after AR-1375 supplies the authenticated runtime control adapter and cross-crate bootstrap seam; then requalify run/sweep locally before any publication.",
  "observed_branch": "feature/ar-1374-cli-live-dispatch",
  "observed_dirty": 0,
  "observed_head": "363b21f81d5c5ab364c2e2a923bd82676feaf343",
  "owner": "ar1374-dispatch-requal-luna56",
  "plan": "../plans/AR-1374-cli-live-dispatch.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Consume authenticated runtime receipts in production asb run and sweep dispatch.",
  "task_revision": 31,
  "title": "Production live-provider dispatch",
  "updated_at": "2026-09-27T02:12:42+00:00",
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

- 2026-09-27T01:28:49+00:00: All declared dependencies AR-1373, AR-1339, AR-1340, and AR-1328 are
  done; AR-1363/1471 now provide authenticated control receipt binding. Resume runtime-owned
  dispatch audit.

- 2026-09-27T01:28:51+00:00: Claimed by ar1332_record_replay_luna56.

- 2026-09-27T01:29:23+00:00: Recorded command exit 0; command argv SHA-256
  ff6d1fa7a7185010f75fcfafe4bdc1bdd5b9804d8c2b3e7abdd8a1b96cd81c63.

- 2026-09-27T01:29:43+00:00: Recorded command exit 0; command argv SHA-256
  321c534968b9c456a64caf5e6d09b63780c507f97548057d2bfe31edcfd73ff4.

- 2026-09-27T01:30:02+00:00: Recorded command exit 0; command argv SHA-256
  b7c438686581cf292b6cd41497ceabb3af42dfed57e04dfd6cc89efed8e2d15b.

- 2026-09-27T01:30:23+00:00: Recorded command exit 0; command argv SHA-256
  b93382f245e081b8317a51c41d2ab4789445c7547649c1554bcc5fbeb3521d1d.

- 2026-09-27T01:30:45+00:00: Recorded command exit 0; command argv SHA-256
  d23f4a5f69552ee49d9a62b798284de57e12a57f0ad13eb5943cbcbb095c8d85.

- 2026-09-27T01:31:00+00:00: Recorded command exit 0; command argv SHA-256
  2888e5f4ddd794c45d079dbd0ab18f822d5749d4074df37eae09d1d02a4159c1.

- 2026-09-27T01:31:14+00:00: Recorded command exit 0; command argv SHA-256
  74779d60a3da240a3ab83f0b766939f0d1887f359a63f9ae071d9b85ea68080f.

- 2026-09-27T01:31:29+00:00: Recorded command exit 0; command argv SHA-256
  84e7a58c47c957aaf9495a62f6c3a36a99bf9f71e8a21271da8e4308ba76b074.

- 2026-09-27T01:31:49+00:00: Recorded command exit 0; command argv SHA-256
  ffd0d53afc589fa1d6dfac2c874868ba18f736ee28e2bbbd81b202dd9c3799f9.

- 2026-09-27T01:32:03+00:00: Recorded command exit 0; command argv SHA-256
  1ec03fda1f74c803bb5a7b097a8f588c73590e7033be466e85d2130fee8ac000.

- 2026-09-27T01:32:36+00:00: Bounded current-main audit at 4ee5a4ed: CLI exposes
  run_with_runtime_live_provider_source and runtime has LiveProviderRuntimeDispatchSource, but no
  authenticated control transport/chain source constructs it. Safe bridge-to-handle/bootstrap
  methods materialize_handle, LiveProviderBootstrapSpec::from_enrollment, and provisioner are
  pub(crate), and are marked dead_code pending the authenticated caller. Existing AR-1374 history
  already identifies this exact missing adapter; AR-1375 is the planned successor. No product
  changes made, no asb-tui/live-provider dependency introduced, and no authority fabricated. Release
  blocked with precise next action: implement AR-1375 adapter/cross-crate seam, then resume AR-1374.

- 2026-09-27T01:32:45+00:00: Blocked after bounded current-main audit at 4ee5a4ed: no authenticated
  control transport/chain source can construct the runtime-owned CLI dispatch source. Required
  runtime bridge/bootstrap constructors remain crate-private and dead_code pending the missing
  adapter. AR-1375 is planned for this exact cross-crate adapter. Next action: implement/promote
  AR-1375, then resume AR-1374 and qualify local/mock run and sweep.

- 2026-09-27T02:11:02+00:00: AR-1472 is complete at merge 363b21f with all seven exact-main
  workflows green and supplies the authenticated runtime adapter that resolved AR-1374 prior
  blocker. Reopen for current-main requalification audit; no live provider or asb-tui changes.

- 2026-09-27T02:11:08+00:00: Claimed by ar1374-dispatch-requal-luna56.

- 2026-09-27T02:11:17+00:00: Recorded command exit 0; command argv SHA-256
  321c534968b9c456a64caf5e6d09b63780c507f97548057d2bfe31edcfd73ff4.

- 2026-09-27T02:11:32+00:00: Recorded command exit 0; command argv SHA-256
  ff6d1fa7a7185010f75fcfafe4bdc1bdd5b9804d8c2b3e7abdd8a1b96cd81c63.

- 2026-09-27T02:11:47+00:00: Recorded command exit 0; command argv SHA-256
  49090c9b64f4e411e33838cd39168df2d7826370eab80d7a6859db7d35384f79.

- 2026-09-27T02:12:01+00:00: Recorded command exit 0; command argv SHA-256
  fdfca1f60c20086094286a809fe298138574266acadfb499b94d1f09ce35edef.

- 2026-09-27T02:12:16+00:00: Recorded command exit 0; command argv SHA-256
  d5cae6ce302d8ca5200c4e447362453e14f36935e3149fe0cdd926322eb8e984.

- 2026-09-27T02:12:31+00:00: Recorded command exit 0; command argv SHA-256
  7dfa8e4180973619ad63008ca55c1cdb60a77d1e72bc16077bde392345beacad.
