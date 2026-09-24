---
{"branch":"","checkpoint_commit":"","claim_expires":"","depends_on":["AR-1427"],"id":"AR-1431","next_action":"Promote after AR-1427 is done; reproduce the AR-1216 post-merge merge-tree failure and repair stale-base protected-main requalification before releasing AR-1216.","owner":"","plan":"../plans/AR-1431-protected-main-stale-base-repair.md","priority":"P0","schema_version":1,"status":"planned","summary":"Prevent stale-base sequential merges from passing review but failing protected-main merge-tree policy.","task_revision":1,"title":"Protected-main stale-base merge requalification repair","updated_at":"2026-09-24T00:00:00+00:00","worktree_key":""}
---

Failure evidence is immutable: AR-1216 post-merge Repository Quality run
`36066329347` rejected merge `e82e2e6` because the protected target advanced from
review base `d9eb6c2` to `8d1889b` before publication.  This AR must preserve
that incident and must not waive the policy.
