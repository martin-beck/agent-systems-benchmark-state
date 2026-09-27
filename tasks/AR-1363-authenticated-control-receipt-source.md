---
{
  "branch": "feature/ar-1363-authenticated-control-receipt-source",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-27T01:55:30+00:00",
  "depends_on": [
    "AR-1362"
  ],
  "id": "AR-1363",
  "next_action": "Promote after AR-1362 is done, then implement the bounded authenticated control receipt source consumed by runtime-owned dispatch.",
  "observed_branch": "feature/ar-1363-authenticated-control-receipt-source",
  "observed_dirty": 0,
  "observed_head": "cb9bce4dd99194ba44f65655d7f7e2e21fc8b408",
  "owner": "ar1332_record_replay_luna56",
  "plan": "../plans/AR-1363-authenticated-control-receipt-source.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Deliver authenticated runtime authority receipts through the versioned control boundary without exposing secrets or caller authority.",
  "task_revision": 13,
  "title": "Authenticated control receipt source",
  "updated_at": "2026-09-27T00:57:26+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1363-authenticated-control-receipt-source"
}
---

Successor for blocked AR-1361, explicitly depending on completed AR-1362.
Do not touch asb-tui, reopen stale dependencies, or synthesize authority in CLI.

- 2026-09-24T00:00:00+00:00: Created after AR-1362 delivered the durable
  digest-only runtime authority enrollment contract and all post-merge gates.

- 2026-09-23T23:28:50+00:00: Promote receipt source after AR-1362 completed durable authority
  enrollment and all post-merge gates.

- 2026-09-23T23:28:52+00:00: Claimed by codex-asb-runtime-attested-enrollment-luna56.

- 2026-09-23T23:29:30+00:00: Recorded command exit 0; command argv SHA-256
  277a1936169e354dbe4c6881de500884f7d6e3cf1bd44c494d3e2099e18ee3e0.

- 2026-09-23T23:29:48+00:00: Blocked after exact protected-main audit at e9d4d3d1: ControlBackend
  AuthRecord still contains only provider/endpoint/credential digests, generation, and status. No
  authenticated certificate chain or runtime-owned authority issuer is available to issue
  RuntimeEnrollmentReceiptV1; synthesizing chain or target/tool/lease/relay authority would violate
  fail-closed policy. Create a successor for authenticated certificate-chain
  enrollment/materialization, then resume AR-1363 and downstream AR-1360.

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

- 2026-09-27T00:55:24+00:00: AR-1471 now provides authenticated control-to-runtime chain binding;
  resume downstream receipt-source integration without caller authority.

- 2026-09-27T00:55:30+00:00: Claimed by ar1332_record_replay_luna56.

- 2026-09-27T00:56:02+00:00: Recorded command exit 0; command argv SHA-256
  ff6d1fa7a7185010f75fcfafe4bdc1bdd5b9804d8c2b3e7abdd8a1b96cd81c63.

- 2026-09-27T00:56:21+00:00: Recorded command exit 0; command argv SHA-256
  321c534968b9c456a64caf5e6d09b63780c507f97548057d2bfe31edcfd73ff4.

- 2026-09-27T00:56:40+00:00: Recorded command exit 0; command argv SHA-256
  d5cae6ce302d8ca5200c4e447362453e14f36935e3149fe0cdd926322eb8e984.

- 2026-09-27T00:56:55+00:00: Recorded command exit 0; command argv SHA-256
  6ed643dd35118b3bc9a612aa209a8cdcd22d115d0c1c932de68957f3c4782365.

- 2026-09-27T00:57:14+00:00: Recorded command exit 0; command argv SHA-256
  b7c438686581cf292b6cd41497ceabb3af42dfed57e04dfd6cc89efed8e2d15b.
