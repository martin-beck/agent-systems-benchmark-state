---
{
  "branch": "feature/ar-1780-installed-tool-workload-execution-qualification",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1764", "AR-1779", "AR-1783"],
  "id": "AR-1780",
  "next_action": "Qualify every development external workload, after installation and selection, through actual run, sweep, report, and comparison flows.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1780-installed-tool-workload-execution-qualification.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {"evidence_class": "environmental", "evidence_digest": "", "evidence_ref": "", "spec_ref": "specs/AR-1780.json", "spec_revision": 2, "status": "pending"},
  "spec_ref": "specs/AR-1780.json",
  "spec_revision": 2,
  "status": "planned",
  "summary": "End-to-end qualify default-installed supported tools and workload bundles through actual ASB execution.",
  "task_revision": 2,
  "title": "Installed tool and workload execution qualification",
  "updated_at": "2026-10-10T09:49:36+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1780-installed-tool-workload-execution-qualification"
}
---

Qualify the whole intended user journey: initialize a disposable project, run
`asb tool install <supported-id>` for selected agents/harnesses/benchmarks and
`asb workload install <supported-id>` for workload bundles, select compatible generated catalogs, execute a bounded local
or development provider benchmark, then inspect/report/compare results. Prove
that execution used the installed project-local binary/workload identity rather
than an ambient substitute. Exercise compatible reuse, official prebuilt,
source-build fallback, project-local dependency closure, update/repair/remove,
offline-after-install, and failure recovery.

This is execution qualification, not merely installer testing. It must retain
identity/provenance in run evidence, reject stale/revoked/mismatched installed
records before launch, keep credentials private, and distinguish unsupported
source/build/install failure from a benchmark failure. The qualification matrix
must cover every AR-1781 development workload ID—including SWE-mini—using a
controlled local/development backend where needed. Production authorization or
hosted qualification absence is not a blocker for this development evidence.
