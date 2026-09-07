---
{"branch":"feature/frontend-privacy-assurance","checkpoint_commit":"","claim_expires":"","depends_on":["AR-0840","AR-0841"],"id":"AR-0843","next_action":"Enforce public-summary and sensitive-artifact boundaries with privacy and fault tests.","owner":"","plan":"../plans/AR-0843.md","priority":"P1","schema_version":1,"status":"planned","summary":"Qualify frontend privacy, artifact access, and fault behavior.","task_revision":1,"title":"Assure frontend privacy and faults","updated_at":"2026-09-07T00:00:00+00:00","worktree_key":"agent-systems-benchmark-frontend-privacy-assurance"}
---
## AR-0843

Separate public summaries from sensitive artifacts and enforce least-privilege access. Test malformed,
stale, duplicate, oversized, slow-client, disconnect, restart, authorization, compatibility, and
redaction failures; prove no credentials, prompts, transcripts, or private paths reach the default API.
