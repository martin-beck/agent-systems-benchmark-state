---
{"branch":"feature/frontend-api-integration","checkpoint_commit":"","claim_expires":"","depends_on":["AR-0840","AR-0841","AR-0842","AR-0843"],"id":"AR-0844","next_action":"Integrate independently reviewed frontend API components and qualify standalone runner operation.","owner":"","plan":"../plans/AR-0844.md","priority":"P1","schema_version":1,"status":"planned","summary":"Integrate and qualify the frontend control API as an independent boundary.","task_revision":1,"title":"Integrate frontend control API","updated_at":"2026-09-07T00:00:00+00:00","worktree_key":"agent-systems-benchmark-frontend-api-integration"}
---
## AR-0844

Integrate the reviewed protocol, transport, lifecycle, and privacy components. Prove the runner
starts and completes without a frontend, frontend restart does not alter runs, reconnect loses no
status, no implicit network listener exists, and exact-head CI/post-merge recovery checks pass.
