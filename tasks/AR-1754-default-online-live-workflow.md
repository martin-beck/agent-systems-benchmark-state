---
{"id":"AR-1754","title":"Make online execution the default across ASB workflows","priority":"P0","depends_on":["AR-1699","AR-1700","AR-1723","AR-1724"],"plan":"../plans/AR-1754-default-online-live-workflow.md","summary":"Make configured online/live provider execution the default for canonical run, sweep, easy, recording/campaign, and TUI handoff paths while keeping local mock and strict replay explicit alternatives.","status":"planned","next_action":"Promote after AR-1723 and AR-1724 are current; inventory every run/sweep/easy/record/campaign/TUI entry point, implement default-online routing with explicit --local-mock and offline replay alternatives, then qualify positive and negative paths.","owner":"","claim_expires":"","checkpoint_commit":"","worktree_key":"","branch":"","schema_version":1,"spec_ref":"specs/AR-1754.json","spec_revision":1,"task_revision":1,"updated_at":"2026-10-09T09:00:00+00:00"}
---

The user-facing ASB workflow currently requires explicit online/live flags in
several places and makes `asb easy run|sweep` local-mock-only. Define one
consistent development contract: configured online provider execution is the
default, while `--local-mock` is an explicit credential-free alternative and
strict offline replay remains explicit. A live failure must remain a typed
failure; it must never silently fall back to mock or replay.

Cover canonical `run`, `sweep`, `benchmark-live`, `record-live`, recording
campaigns, `asb easy` commands, and the ASB/TUI handoff/configuration contract.
Do not modify the separate asb-tui repository in this AR; publish any required
cross-repository contract and dependency notes in the state plan. Preserve
credential-reference-only configuration, bounded progress, network/cost
warnings, provider/model/agent/workload identity, and all existing fail-closed
production authority checks.
