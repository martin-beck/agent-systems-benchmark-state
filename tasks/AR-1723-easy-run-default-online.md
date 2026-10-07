---
{"id":"AR-1723","title":"Make the easy run default to online provider execution","priority":"P0","depends_on":["AR-1711","AR-1715"],"plan":"../plans/AR-1723-easy-run-default-online.md","summary":"Make the shortest user-facing run use the configured live provider by default while keeping local mock explicit and development authentication warning-only.","status":"planned","next_action":"Promote after the live runner and provider qualification dependencies are current; implement and qualify the default-online easy run.","owner":"","claim_expires":"","checkpoint_commit":"","worktree_key":"","branch":"","schema_version":1,"spec_ref":"specs/AR-1723.json","spec_revision":1,"task_revision":1,"updated_at":"2026-10-07T12:00:00+00:00"}
---

The development prototype must make live provider execution the obvious
default. Missing development credentials are warnings until live execution is
requested; live failures never silently select mock or replay.
