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
  "task_revision": 10,
  "title": "Initialize an ASB benchmark project workspace",
  "updated_at": "2026-10-09T15:07:52+00:00",
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

- 2026-10-09T15:04:43+00:00: Recorded command exit 0; command argv SHA-256
  03d9fe5791f2da017ecf4f0e815462d8fa0df4b590d3db050e5855f3ee6c8b46.

- 2026-10-09T15:04:57+00:00: Recorded command exit 0; command argv SHA-256
  0c9e7e234ecef0ada5ab70152a1b18bee6c8d9e247b80e39b1612a4e2d0a6275.

- 2026-10-09T15:05:04+00:00: Recorded command exit 0; command argv SHA-256
  064e8b6760e2a8b9269baa1776da1b65ee7d2ae0a00f570726f71394792f2b54.

- 2026-10-09T15:06:59+00:00: Recorded command exit 0; command argv SHA-256
  3cf13a5edc254b85c4d447ce67a1ffdea4e2bf581375435f08beb65055741b39.

- 2026-10-09T15:07:10+00:00: Recorded command exit 1; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-09T15:07:21+00:00: Recorded command exit 0; command argv SHA-256
  6f25c271a70927d75fec926d61ffa949ce0ab9d62261aa338a7702469464fc50.

- 2026-10-09T15:07:52+00:00: Recorded command exit 0; command argv SHA-256
  294e7c15e0bfdd7f1b3311b2e9e0aab99a2eb2f22deb9b899e5b2f988bf9825b.
