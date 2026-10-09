---
{
  "branch": "feature/ar-1761-tool-install-registry",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1759",
    "AR-1760"
  ],
  "id": "AR-1761",
  "next_action": "Implement `asb tool install` against the frozen schema and project layout.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1761-tool-install-registry.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "contract-test",
    "evidence_digest": "",
    "evidence_ref": "",
    "spec_ref": "specs/AR-1761.json",
    "spec_revision": 1,
    "status": "pending"
  },
  "spec_ref": "specs/AR-1761.json",
  "spec_revision": 1,
  "status": "open",
  "summary": "Install supported external ASB tools into a user/project-local root and persist validated records.",
  "task_revision": 2,
  "title": "ASB external-tool installer and registry",
  "updated_at": "2026-10-09T15:40:58+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1761-tool-install-registry"
}
---

Add a clear `asb tool install <id> --kind agent|harness|benchmark|workload|support`
command (with source/version/project and `--json` options) backed by an
extensible, bounded installer registry. It must support the external tools ASB
actually uses, install without root into a user/project-local location, record
the executable/root/source/version/platform/digest/capabilities in the project
config, and give an explicit unsupported-tool diagnostic rather than executing
arbitrary shell. Add status/list/remove or repair behavior only where needed
for idempotence; never store API keys or tokens.

- 2026-10-09T15:40:58+00:00: dependencies AR-1759 and AR-1760 verified accepted/released;
  implementation ready
