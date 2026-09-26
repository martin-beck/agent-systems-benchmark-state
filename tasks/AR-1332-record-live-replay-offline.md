---
{
  "branch": "feature/ar-1332-record-live-replay-offline",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-26T18:49:06+00:00",
  "depends_on": [
    "AR-1331"
  ],
  "id": "AR-1332",
  "next_action": "Add the record-live then replay-offline CLI workflow that seals cassettes from an opt-in live run and replays them strictly offline without provider fallback.",
  "observed_branch": "feature/ar-1332-record-live-replay-offline",
  "observed_dirty": 0,
  "observed_head": "28730b61572f463e9cf1e6b5f1cf20fd198ef7e8",
  "owner": "ar1332-record-replay-luna56",
  "plan": "../plans/AR-1332.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Add the record-live then replay-offline end-to-end CLI workflow.",
  "task_revision": 9,
  "title": "Record-live to replay-offline workflow",
  "updated_at": "2026-09-26T16:49:06+00:00",
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

- 2026-09-26T16:46:13+00:00: AR-1331 is durably done; promote the ASB-only record-live to
  replay-offline workflow. Qualification must use local/mock or strict replay; external provider
  access remains optional.

- 2026-09-26T16:47:28+00:00: Claimed by ar1332-record-replay-luna56.

- 2026-09-26T16:48:03+00:00: Recorded command exit 0; command argv SHA-256
  86373cbbaffb66da63f9e5e10e308b45d7f25c83c016f6830b3db0bab7042f89.

- 2026-09-26T16:48:23+00:00: Recorded command exit 0; command argv SHA-256
  ff6d1fa7a7185010f75fcfafe4bdc1bdd5b9804d8c2b3e7abdd8a1b96cd81c63.

- 2026-09-26T16:48:37+00:00: Recorded command exit 0; command argv SHA-256
  b04e51d6a8a1cd1d991d96d1b0eeb7f5236f1056ccb95c8f404b26c181dc4797.

- 2026-09-26T16:48:52+00:00: Heartbeat by ar1332-record-replay-luna56.

- 2026-09-26T16:49:06+00:00: Heartbeat by ar1332-record-replay-luna56.
