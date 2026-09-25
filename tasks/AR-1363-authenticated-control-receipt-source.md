---
{
  "branch": "feature/ar-1363-authenticated-control-receipt-source",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1362"
  ],
  "id": "AR-1363",
  "next_action": "Promote after AR-1362 is done, then implement the bounded authenticated control receipt source consumed by runtime-owned dispatch.",
  "observed_branch": "feature/ar-1363-authenticated-control-receipt-source",
  "observed_dirty": 0,
  "observed_head": "e9d4d3d1c6a4d67d0ce0e49fa8eaf696561fe45e",
  "owner": "",
  "plan": "../plans/AR-1363-authenticated-control-receipt-source.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "blocked",
  "summary": "Deliver authenticated runtime authority receipts through the versioned control boundary without exposing secrets or caller authority.",
  "task_revision": 5,
  "title": "Authenticated control receipt source",
  "updated_at": "2026-09-23T23:29:48+00:00",
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
