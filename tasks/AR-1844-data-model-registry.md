---
{"branch":"feature/ar-1844-data-model-registry","checkpoint_commit":"","claim_expires":"","depends_on":["AR-1842"],"id":"AR-1844","next_action":"Promote after AR-1842; inventory the authoritative ASB data model and define the generated field registry contract.","owner":"","plan":"../plans/AR-1844-data-model-registry.md","priority":"P0","schema_version":1,"spec_acceptance":{"evidence_class":"contract-test","evidence_digest":"","evidence_ref":"","spec_ref":"specs/AR-1844.json","spec_revision":1,"status":"pending"},"spec_ref":"specs/AR-1844.json","spec_revision":1,"status":"planned","summary":"Generate a complete secret-free registry of ASB configuration options and individual settings from the authoritative data model.","task_revision":1,"title":"Extract the ASB data-model registry","updated_at":"2026-10-13T00:00:00Z","worktree_key":"agent-systems-benchmark-ar-1844-data-model-registry"}
---

This AR establishes the authoritative machine-readable inventory used by the
remaining dataflow series. It must cover all configuration settings rather than
only the current wizard fields, while keeping API-key values and private paths
out of generated artifacts.
