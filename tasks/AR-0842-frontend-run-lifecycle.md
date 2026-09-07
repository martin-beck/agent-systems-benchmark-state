---
{"branch":"feature/frontend-run-lifecycle","checkpoint_commit":"","claim_expires":"","depends_on":["AR-0840","AR-0841","AR-0801"],"id":"AR-0842","next_action":"Implement idempotent launch, cancellation, status reconnect, history, and recovery semantics.","owner":"","plan":"../plans/AR-0842.md","priority":"P1","schema_version":1,"status":"planned","summary":"Define and implement frontend-independent run lifecycle semantics.","task_revision":1,"title":"Implement frontend run lifecycle","updated_at":"2026-09-07T00:00:00+00:00","worktree_key":"agent-systems-benchmark-frontend-run-lifecycle"}
---
## AR-0842

Keep journals authoritative so frontend disconnect, duplicate request, retry, crash, or restart
cannot duplicate or corrupt a run. Implement reconnect cursors, idempotency, cancellation, paging,
and bounded backpressure with recovery tests.
