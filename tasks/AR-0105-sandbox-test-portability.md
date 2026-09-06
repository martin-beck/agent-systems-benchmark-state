---
{
  "branch": "fix/sandbox-test-portability",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-06T23:14:40+00:00",
  "depends_on": [
    "AR-0103"
  ],
  "id": "AR-0105",
  "next_action": "Promote after confirming AR-0103 remains done, then repair the isolated-target fixture before resuming blocked full-tree gates.",
  "observed_branch": "fix/sandbox-test-portability",
  "observed_dirty": 1,
  "observed_head": "9543a3297dd9d0ca93c802bb204b099ac1df569b",
  "owner": "contracts-20260906",
  "plan": "../plans/AR-0105.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Remove repository-target assumptions from sandbox lease tests so clean external Cargo targets work.",
  "task_revision": 8,
  "title": "Repair sandbox test target portability",
  "updated_at": "2026-09-06T21:16:36+00:00",
  "worktree_key": "agent-systems-benchmark-sandbox-test-portability"
}
---
## AR-0105

Remove repository-target assumptions from sandbox lease tests so clean external Cargo targets work.

This defect was discovered by AR-0204's exact-tree validation with a fresh external
`CARGO_TARGET_DIR`. The sandbox lease unit fixture derives a repository `target` path and
attempts to create a child without creating its missing parent, producing `ENOENT`. Do not
pre-create or retain a repository target directory to mask the failure.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-06T21:12:10+00:00: Promoted after confirming dependency AR-0103 is durably done; P0
  regression blocks clean external-target full-tree validation and must not be masked by precreating
  repository target directories.

- 2026-09-06T21:14:40+00:00: Claimed by contracts-20260906.

- 2026-09-06T21:14:51+00:00: Recorded command exit 0; command argv SHA-256
  bbce29c67a8524be6da229d8a31c52c3d6291ba6e461557ac0293df07a911720.

- 2026-09-06T21:15:10+00:00: Recorded command exit 101; command argv SHA-256
  9d971526f8ffc1039239ca1a987d496ad8ee068c325e8d745189812a4d433c02.

- 2026-09-06T21:16:36+00:00: Recorded command exit 0; command argv SHA-256
  d7a046c26df871a74ff3ea86b44762fdbb3a81d73dc5c95949cae8cf74d88f11.
