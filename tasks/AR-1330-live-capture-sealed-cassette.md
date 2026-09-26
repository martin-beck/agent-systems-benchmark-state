---
{
  "branch": "feature/ar-1330-live-capture-sealed-cassette",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-26T22:11:10+00:00",
  "depends_on": [
    "AR-0502",
    "AR-0503",
    "AR-1329"
  ],
  "id": "AR-1330",
  "next_action": "Invoke the existing StrictReplayService::capture_authenticated_connection boundary from the live run path and seal the sanitized, redacted provider exchange as a content-addressed cassette.",
  "owner": "coordinator-ar1330-capture",
  "plan": "../plans/AR-1330.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Capture and seal a real authenticated provider exchange as a content-addressed cassette.",
  "task_revision": 3,
  "title": "Live provider capture into a sealed cassette",
  "updated_at": "2026-09-26T20:11:10+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1330-live-capture-sealed-cassette"
}
---

The AR-0502/AR-0503 replay cassette and strict-replay contracts are complete,
and `StrictReplayService::capture_authenticated_connection` exists as a
runtime-owned seam, but no live run invokes it. This AR wires the AR-1329 live
execution path into that seam so every real provider exchange is captured,
sanitized and redacted by the existing `Redactor`, sealed as a
content-addressed `CassetteContents`, and recorded with its digest and
redaction/verification result. Credentials, prompts, responses and raw capture
data never enter durable state or public control responses, and interrupted
captures reconcile without repeating uncertain paid work.

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

- 2026-09-26T20:11:07+00:00: Dependencies are done; implement capture through the existing
  runtime-owned seam using deterministic local/mock qualification, with external provider access
  optional.

- 2026-09-26T20:11:10+00:00: Claimed by coordinator-ar1330-capture.
