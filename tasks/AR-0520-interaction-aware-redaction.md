---
{"branch":"feature/interaction-aware-redaction","checkpoint_commit":"","claim_expires":"","depends_on":["AR-0502","AR-0503","AR-0517"],"id":"AR-0520","next_action":"Make request-body redaction selectors interaction/method-aware so GET catalog entries can remain selector-free while POST bodies remain private and replayable.","owner":"","plan":"../plans/AR-0520.md","priority":"P0","schema_version":1,"status":"planned","summary":"Support per-interaction request redaction policies for mixed catalog and private requests.","task_revision":1,"title":"Interaction-aware request redaction","updated_at":"2026-09-07T00:00:00+00:00","worktree_key":"agent-systems-benchmark-interaction-aware-redaction"}
---
## AR-0520

Repair the cassette-global request-body redaction limitation exposed by Goose: catalog GET interactions must have null selectors while private POST message bodies retain bounded selectors and remain strictly replayable. Add interaction/method-aware policy representation, schema/roundtrip/strict-match support, missing-selector and marker-injection negatives, and full privacy/formal/platform gates.
