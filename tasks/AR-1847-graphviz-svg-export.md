---
{"branch":"feature/ar-1847-graphviz-svg-export","checkpoint_commit":"","claim_expires":"","depends_on":["AR-1846"],"id":"AR-1847","next_action":"Promote after AR-1846; implement the extraction command and deterministic DOT/SVG graph artifacts with privacy checks.","owner":"","plan":"../plans/AR-1847-graphviz-svg-export.md","priority":"P0","schema_version":1,"spec_acceptance":{"evidence_class":"contract-test","evidence_digest":"","evidence_ref":"","spec_ref":"specs/AR-1847.json","spec_revision":1,"status":"pending"},"spec_ref":"specs/AR-1847.json","spec_revision":1,"status":"planned","summary":"Write the ASB configuration/dataflow graph as Graphviz DOT and a developer-screen-readable SVG.","task_revision":1,"title":"Export ASB configuration dataflows to Graphviz and SVG","updated_at":"2026-10-13T00:00:00Z","worktree_key":"agent-systems-benchmark-ar-1847-graphviz-svg-export"}
---

This AR turns the extracted registries into a durable developer artifact. DOT is
the source of truth; SVG is a local rendering that preserves all relations and
never includes secrets or private machine details.
