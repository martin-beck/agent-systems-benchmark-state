---
{
  "branch": "feature/ar-1760-project-init-workspace",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-09T17:04:33+00:00",
  "depends_on": [
    "AR-1759"
  ],
  "id": "AR-1760",
  "next_action": "Implement `asb project init` after AR-1759 is merged.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "codex-asb-ar1760-project-init-20261009",
  "plan": "../plans/AR-1760-project-init-workspace.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "contract-test",
    "evidence_digest": "",
    "evidence_ref": "",
    "spec_ref": "specs/AR-1760.json",
    "spec_revision": 1,
    "status": "pending"
  },
  "spec_ref": "specs/AR-1760.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Add an idempotent ASB project initializer containing config, results, and catalog areas.",
  "task_revision": 3,
  "title": "Initialize an ASB benchmark project workspace",
  "updated_at": "2026-10-09T15:04:33+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1760-project-init-workspace"
}
---

Implement `asb project init [PATH]` using the AR-1759 contract. It must create
the project configuration, results store, and catalog directory in a bounded
project layout, be safe and idempotent, refuse to overwrite unrelated files,
and recover cleanly from partial initialization. It must print the next simple
commands for a fresh user and support `--json` without leaking host secrets.

- 2026-10-09T15:04:30+00:00: AR-1759 schema is merged, accepted, released, and dependency-ready.

- 2026-10-09T15:04:33+00:00: Claimed by codex-asb-ar1760-project-init-20261009.
