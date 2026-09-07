---
{"branch":"feature/ci-artifact-quota-resilience","checkpoint_commit":"","claim_expires":"","depends_on":["AR-0003","AR-0831"],"id":"AR-0845","next_action":"Make optional CI evidence quota-aware while preserving required-check semantics and provenance.","owner":"","plan":"../plans/AR-0845.md","priority":"P1","schema_version":1,"status":"planned","summary":"Prevent exhausted GitHub artifact quota from obscuring authoritative ASB results.","task_revision":1,"title":"Harden CI artifact quota behavior","updated_at":"2026-09-07T00:00:00+00:00","worktree_key":"agent-systems-benchmark-ci-artifact-quota-resilience"}
---
## AR-0845

Make ASB CI distinguish required checks from optional artifact publication when GitHub artifact quota
is exhausted. Preserve test truth, provenance, privacy, and failure visibility; never turn a required
artifact or required check silently optional. Add quota detection, bounded diagnostics, fixtures, and
operator guidance.
