---
{
  "branch": "fix/sandbox-test-portability",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-0103"
  ],
  "id": "AR-0105",
  "next_action": "Promote after confirming AR-0103 remains done, then repair the isolated-target fixture before resuming blocked full-tree gates.",
  "owner": "",
  "plan": "../plans/AR-0105.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "open",
  "summary": "Remove repository-target assumptions from sandbox lease tests so clean external Cargo targets work.",
  "task_revision": 2,
  "title": "Repair sandbox test target portability",
  "updated_at": "2026-09-06T21:12:10+00:00",
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
