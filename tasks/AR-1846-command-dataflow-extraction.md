---
{"branch":"feature/ar-1846-command-dataflow-extraction","checkpoint_commit":"","claim_expires":"","depends_on":["AR-1845"],"id":"AR-1846","next_action":"Promote after AR-1845; extract the authoritative `asb` command tree and connect every option to lifecycle entities.","owner":"","plan":"../plans/AR-1846-command-dataflow-extraction.md","priority":"P0","schema_version":1,"spec_acceptance":{"evidence_class":"contract-test","evidence_digest":"","evidence_ref":"","spec_ref":"specs/AR-1846.json","spec_revision":1,"status":"pending"},"spec_ref":"specs/AR-1846.json","spec_revision":1,"status":"planned","summary":"Extract all ASB commands and options and their relations to configuration entities across the complete workflow.","task_revision":1,"title":"Extract ASB command and option dataflows","updated_at":"2026-10-13T00:00:00Z","worktree_key":"agent-systems-benchmark-ar-1846-command-dataflow-extraction"}
---

The output is an executable inventory of how commands assemble, validate,
modify, consume, and emit configuration and results. It must be generated from
the CLI implementation so new options cannot silently disappear from the map.
