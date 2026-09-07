---
{
  "branch": "feature/gemini-generate-content-replay",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-07T18:58:09+00:00",
  "depends_on": [
    "AR-0502",
    "AR-0503",
    "AR-0517"
  ],
  "id": "AR-0518",
  "next_action": "Define and qualify the bounded Gemini GenerateContent strict-replay dialect from exact pinned capture evidence.",
  "observed_branch": "feature/gemini-generate-content-replay",
  "observed_dirty": 0,
  "observed_head": "ab5d6c91c99d48883ed58eb1df6803c2711ecbd3",
  "owner": "replay_20260906",
  "plan": "../plans/AR-0518.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Add strict replay support for Gemini GenerateContent SSE traffic.",
  "task_revision": 5,
  "title": "Gemini GenerateContent strict-replay dialect",
  "updated_at": "2026-09-07T15:59:52+00:00",
  "worktree_key": "agent-systems-benchmark-gemini-generate-content-replay"
}
---
## AR-0518

Add the bounded Gemini GenerateContent dialect required by pinned evidence: validated `POST /v1beta/models/{model}:streamGenerateContent?alt=sse`, exact JSON/tool/generation configuration, redaction-pointer parity, and strict SSE framing. Reject arbitrary models, paths, queries, unsupported fields, malformed payloads, marker injection, and outbound fallback.

Require schema/runtime parity, focused and adversarial tests, fuzz/mutation/formal/privacy gates, native x86_64/aarch64 checks, and a real credential-free Gemini replay before AR-0510 can complete.

- 2026-09-07T15:58:07+00:00: Promote Gemini shared dialect repair after isolated AR-0510 capture
  identified the missing GenerateContent route; serialize before AR-0510 integration.

- 2026-09-07T15:58:09+00:00: Claimed by replay_20260906.

- 2026-09-07T15:59:52+00:00: Recorded command exit 0; command argv SHA-256
  cc517b6ec5bba838c0ff1b0bda80b050419c6600b5efeb329096e40609d22719.
