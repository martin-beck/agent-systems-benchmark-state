---
{
  "branch": "feature/ar-1783-installed-workload-selection-and-execution",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1763", "AR-1764", "AR-1782"],
  "id": "AR-1783",
  "next_action": "Integrate every development-supported installed workload bundle into selection and prove full run/sweep/report/compare consumes its exact recorded identity.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1783-installed-workload-selection-and-execution.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {"evidence_class": "environmental", "evidence_digest": "", "evidence_ref": "", "spec_ref": "specs/AR-1783.json", "spec_revision": 2, "status": "pending"},
  "spec_ref": "specs/AR-1783.json",
  "spec_revision": 2,
  "status": "planned",
  "summary": "Select every development external workload and prove ASB uses its exact project-local identity end to end.",
  "task_revision": 2,
  "title": "Installed workload selection and execution",
  "updated_at": "2026-10-10T09:49:36+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1783-installed-workload-selection-and-execution"
}
---

Make generated project catalogs and run/sweep consume the dedicated `asb workload`
records. Selection validates the installed workload's exact catalog revision,
identity, digest, license/terms compatibility, preparation state, adapter
version, and resource/platform requirements. Execution binds this identity into
the plan/run/record/report/compare evidence and rejects ambient, stale, revoked,
missing, incompatible, or manually substituted workload directories before a run
starts. Cover every AR-1781 workload ID—including SWE-mini—through a fresh
project's install, selection, bounded run and sweep, report, and comparison
journey. Development runs may use a controlled local/development backend where
needed; lack of production authorization or hosted qualification must not block
the suite from this end-to-end path.
