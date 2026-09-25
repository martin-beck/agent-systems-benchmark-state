---
{
  "branch": "feature/ar-1332-record-live-replay-offline",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1331"
  ],
  "id": "AR-1332",
  "next_action": "Add the record-live then replay-offline CLI workflow that seals cassettes from an opt-in live run and replays them strictly offline without provider fallback.",
  "owner": "",
  "plan": "../plans/AR-1332.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "planned",
  "summary": "Add the record-live then replay-offline end-to-end CLI workflow.",
  "task_revision": 1,
  "title": "Record-live to replay-offline workflow",
  "updated_at": "2026-09-22T13:39:37+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1332-record-live-replay-offline"
}
---

Live capture (AR-1330) and the runtime launch authority (AR-1331) exist in
isolation, but the user-visible workflow that connects them is missing: record a
real run under an explicit opt-in, seal the cassettes, then replay the exact
evidence strictly offline. This AR defines and documents that
`record-live -> replay-offline` workflow in the CLI: a bounded live record mode
that persists intent before provider contact and seals per-tuple cassettes, and
a replay mode that accepts only runtime-issued authority and never contacts a
provider. Replay results are recorded against the sealed cassette digests with
no fallback, and interrupted or duplicated records fail closed.

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
