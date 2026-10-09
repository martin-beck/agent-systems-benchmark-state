---
{
  "branch": "feature/ar-1761-tool-install-registry",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-09T17:41:04+00:00",
  "depends_on": [
    "AR-1759",
    "AR-1760"
  ],
  "id": "AR-1761",
  "next_action": "Implement `asb tool install` against the frozen schema and project layout.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "codex-asb-ar1761-tool-install-20261009",
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
  "status": "in_progress",
  "summary": "Install supported external ASB tools into a user/project-local root and persist validated records.",
  "task_revision": 6,
  "title": "ASB external-tool installer and registry",
  "updated_at": "2026-10-09T15:41:48+00:00",
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

- 2026-10-09T15:41:04+00:00: Claimed by codex-asb-ar1761-tool-install-20261009.

- 2026-10-09T15:41:15+00:00: Recorded command exit 0; command argv SHA-256
  8781f7f86432da71cf00304d47062d61aa5ed8ccbac43c32fffb341be9c007fd.

- 2026-10-09T15:41:35+00:00: Recorded command exit 0; command argv SHA-256
  c18ed43a4423686964d2b9e91943401cda7e5651ce092cd08b41811163bc1613.

- 2026-10-09T15:41:48+00:00: Recorded command exit 0; command argv SHA-256
  ec48e1d504dbb949df2606165a2406335cb4529dc7cbd9a666569760fe08df68.
