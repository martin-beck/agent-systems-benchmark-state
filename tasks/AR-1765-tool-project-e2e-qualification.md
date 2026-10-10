---
{
  "branch": "feature/ar-1765-tool-project-e2e-qualification",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-10T13:40:55+00:00",
  "depends_on": [
    "AR-1760",
    "AR-1761",
    "AR-1762",
    "AR-1763",
    "AR-1764"
  ],
  "id": "AR-1765",
  "next_action": "Run the fresh-user end-to-end qualification after AR-1764 is merged.",
  "observed_branch": "feature/ar-1765-tool-project-e2e-qualification",
  "observed_dirty": 0,
  "observed_head": "fd61b856570bf1d57e9dba4f8bee1da99b77189e",
  "owner": "ar1765-tool-project-e2e-terra",
  "plan": "../plans/AR-1765-tool-project-e2e-qualification.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "contract-test",
    "evidence_digest": "",
    "evidence_ref": "",
    "spec_ref": "specs/AR-1765.json",
    "spec_revision": 1,
    "status": "pending"
  },
  "spec_ref": "specs/AR-1765.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Qualify the complete fresh-user flow from project init through tool install/discovery/catalog selection and benchmark results.",
  "task_revision": 4,
  "title": "End-to-end qualification of ASB tool projects",
  "updated_at": "2026-10-10T11:41:33+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1765-tool-project-e2e-qualification"
}
---

Build a disposable-machine qualification that starts with a fresh ASB install,
runs `asb project init`, installs at least one fixture of every tool kind,
discovers system and project tools, generates/selects catalogs, executes a
small benchmark, and verifies results and machine-readable config remain in
the project. Cover clean-machine detection, repeatability, partial failures,
unsafe paths, missing credentials/signatures in development mode, human output,
and `--json`. Record a short fresh-user help/tutorial path and exact CI evidence.

- 2026-10-10T11:40:42+00:00: AR-1764 merged at fd61b856570bf1d57e9dba4f8bee1da99b77189e; all
  exact-main post-merge workflows terminal-success and receipt recorded. Start fresh-user end-to-end
  qualification.

- 2026-10-10T11:40:55+00:00: Claimed by ar1765-tool-project-e2e-terra.
