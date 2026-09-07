---
{"branch":"feature/artifact-retention-cleanup","checkpoint_commit":"","claim_expires":"","depends_on":["AR-0845","AR-0903"],"id":"AR-0846","next_action":"Implement dry-run inventory and explicitly authorized bounded cleanup for linked GitHub artifacts.","owner":"","plan":"../plans/AR-0846.md","priority":"P1","schema_version":1,"status":"planned","summary":"Manage ASB GitHub artifact retention and cleanup without deleting required evidence.","task_revision":1,"title":"Add linked artifact retention and cleanup","updated_at":"2026-09-07T00:00:00+00:00","worktree_key":"agent-systems-benchmark-artifact-retention-cleanup"}
---
## AR-0846

Inventory and safely clean old GitHub Actions artifacts using linkage to commits/PRs/releases,
artifact role, age, size, retention class, and quota state. Default to dry-run; require explicit
bounded authorization for deletion, preserve required/release/provenance artifacts, record checksums
and deletion decisions, and test pagination, races, API failure, cancellation, and partial cleanup.
