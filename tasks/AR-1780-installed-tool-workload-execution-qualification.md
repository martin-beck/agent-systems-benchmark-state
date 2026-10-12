---
{
  "branch": "feature/ar-1780-installed-tool-workload-execution-qualification",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-12T04:10:14+00:00",
  "depends_on": [
    "AR-1764",
    "AR-1779",
    "AR-1783"
  ],
  "id": "AR-1780",
  "next_action": "Qualify every development external workload, after installation and selection, through actual run, sweep, report, and comparison flows.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "ar1780_workload_qualification_luna56",
  "plan": "../plans/AR-1780-installed-tool-workload-execution-qualification.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "environmental",
    "evidence_digest": "",
    "evidence_ref": "",
    "spec_ref": "specs/AR-1780.json",
    "spec_revision": 2,
    "status": "pending"
  },
  "spec_ref": "specs/AR-1780.json",
  "spec_revision": 2,
  "status": "in_progress",
  "summary": "End-to-end qualify default-installed supported tools and workload bundles through actual ASB execution.",
  "task_revision": 10,
  "title": "Installed tool and workload execution qualification",
  "updated_at": "2026-10-12T02:10:26+00:00",
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

- 2026-10-12T02:09:08+00:00: dependencies verified: AR-1764, AR-1779, AR-1783 done

- 2026-10-12T02:09:10+00:00: Claimed by ar1780_workload_qualification_luna56.

- 2026-10-12T02:09:14+00:00: Recorded command exit 0; command argv SHA-256
  ff6d1fa7a7185010f75fcfafe4bdc1bdd5b9804d8c2b3e7abdd8a1b96cd81c63.

- 2026-10-12T02:09:31+00:00: Recorded command exit 0; command argv SHA-256
  b04e51d6a8a1cd1d991d96d1b0eeb7f5236f1056ccb95c8f404b26c181dc4797.

- 2026-10-12T02:09:51+00:00: Recorded command exit 0; command argv SHA-256
  df20f88ac79aa7d7ff50d4907276129073f71abdbef6b040ce20b910da05a70b.

- 2026-10-12T02:10:14+00:00: Heartbeat by ar1780_workload_qualification_luna56.

- 2026-10-12T02:10:22+00:00: Recorded command exit 128; command argv SHA-256
  32f2329f17ebfe2e32ec6439a8a438277cb4161fd6f1bdfc3b98e2bac6aa7c84.

- 2026-10-12T02:10:26+00:00: Recorded command exit 128; command argv SHA-256
  fa166ffff8a4b3c539413e2445ca8a6e1daf05c016e8f4af49647768507709ce.
