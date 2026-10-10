---
{
  "branch": "feature/ar-1782-verified-asb-workload-installation",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1781"],
  "id": "AR-1782",
  "next_action": "Implement asb workload install/list/status/select/repair/update/remove for every development-supported official external workload bundle.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1782-verified-asb-workload-installation.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {"evidence_class": "contract-test", "evidence_digest": "", "evidence_ref": "", "spec_ref": "specs/AR-1782.json", "spec_revision": 2, "status": "pending"},
  "spec_ref": "specs/AR-1782.json",
  "spec_revision": 2,
  "status": "planned",
  "summary": "Implement dedicated verified remote external workload installation and lifecycle through asb workload.",
  "task_revision": 2,
  "title": "Verified asb workload installation",
  "updated_at": "2026-10-10T09:49:36+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1782-verified-asb-workload-installation"
}
---

Add `asb workload install <supported-id> [--project PATH]` and `list`, `status`,
`select`, `repair`, `update`, and `remove` lifecycle commands. Install resolves only the
AR-1781 catalog, downloads the official primary-source workload release into a
project-local workload root, verifies immutable identity/proof/license/size and
archive boundaries, performs only declared bounded preparation, validates the
adapter-ready structure, and atomically records a workload receipt.

The command must support all AR-1781 development workload IDs, including
SWE-mini, not merely list them. It must preserve a good prior workload on failed update,
never execute downloaded installer scripts, require root, or mutate global package
manager state. Read-only operations are network-free. Download, integrity,
license, preparation, storage, incompatibility, stale/revoked, and offline cases
must remain separate actionable outcomes. Development operation must not be
blocked by production authorization or hosted-release verification requirements;
the pinned primary-source identity, declared constraints, and bounded preparation
remain mandatory.
