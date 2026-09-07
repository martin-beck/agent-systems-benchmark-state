---
{"branch":"feature/gemini-generate-content-replay","checkpoint_commit":"","claim_expires":"","depends_on":["AR-0502","AR-0503","AR-0517"],"id":"AR-0518","next_action":"Define and qualify the bounded Gemini GenerateContent strict-replay dialect from exact pinned capture evidence.","owner":"","plan":"../plans/AR-0518.md","priority":"P0","schema_version":1,"status":"planned","summary":"Add strict replay support for Gemini GenerateContent SSE traffic.","task_revision":1,"title":"Gemini GenerateContent strict-replay dialect","updated_at":"2026-09-07T00:00:00+00:00","worktree_key":"agent-systems-benchmark-gemini-generate-content-replay"}
---
## AR-0518

Add the bounded Gemini GenerateContent dialect required by pinned evidence: validated `POST /v1beta/models/{model}:streamGenerateContent?alt=sse`, exact JSON/tool/generation configuration, redaction-pointer parity, and strict SSE framing. Reject arbitrary models, paths, queries, unsupported fields, malformed payloads, marker injection, and outbound fallback.

Require schema/runtime parity, focused and adversarial tests, fuzz/mutation/formal/privacy gates, native x86_64/aarch64 checks, and a real credential-free Gemini replay before AR-0510 can complete.
