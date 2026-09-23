---
{
  "branch": "feature/ar-1338-guided-asb-command-wrapper",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1328", "AR-1329", "AR-1332", "AR-1333"],
  "id": "AR-1338",
  "next_action": "Promote after AR-1328, AR-1329, AR-1332 and AR-1333 are done; implement the catalog-driven asb easy wrapper, generated private files, documentation and offline hostile tests.",
  "owner": "",
  "plan": "../plans/AR-1338.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "planned",
  "summary": "Add a catalog-driven friendly wrapper for setup, selection and benchmark workflows.",
  "task_revision": 1,
  "title": "Guided ASB command wrapper",
  "updated_at": "2026-09-23T00:00:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1338-guided-asb-command-wrapper"
}
---

Add a friendly `asb easy` command or equivalent in-tree wrapper that guides a
user through supported setup, provider/model selection, multi-agent plans and
benchmark/report workflows. It must derive all digests and generated files from
the authoritative ASB catalog and config contracts, preserve secret isolation,
and delegate execution to the normal ASB commands. It must not become a second
provider registry or bypass the runtime's fail-closed validation.
