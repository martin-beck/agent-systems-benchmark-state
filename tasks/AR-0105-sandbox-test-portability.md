---
{
  "branch": "fix/sandbox-test-portability",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-06T23:14:40+00:00",
  "depends_on": [
    "AR-0103"
  ],
  "id": "AR-0105",
  "next_action": "Resolve newly exposed sandbox_boundary.rs target_root ownership, then rerun full isolated-target gates without masking.",
  "observed_branch": "fix/sandbox-test-portability",
  "observed_dirty": 1,
  "observed_head": "2b28fee781afed113d2b468f8480f4eb71d01feb",
  "owner": "contracts-20260906",
  "plan": "../plans/AR-0105.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Remove repository-target assumptions from sandbox lease tests so clean external Cargo targets work.",
  "task_revision": 26,
  "title": "Repair sandbox test target portability",
  "updated_at": "2026-09-06T21:25:45+00:00",
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

- 2026-09-06T21:16:52+00:00: Recorded command exit 0; command argv SHA-256
  9cec9684a58511c4e54662b6a1b70f20cf58a8f71f19e46c562a37d8da6964ef.

- 2026-09-06T21:17:13+00:00: Recorded command exit 0; command argv SHA-256
  77a4167ec9ee7467eca742fcbb87aefbc12ecc58578734426b3bd77ea4ea4141.

- 2026-09-06T21:17:33+00:00: Recorded command exit 101; command argv SHA-256
  46414eb6feafa620f5d84b88b300599506be0f17f11a83e52ec1f661bc751196.

- 2026-09-06T21:17:51+00:00: Recorded command exit 0; command argv SHA-256
  6a2e050bfce0a55aa633ab06c09a432628f93c95e6bfb658c141d331a92520e0.

- 2026-09-06T21:18:08+00:00: Recorded command exit 101; command argv SHA-256
  2f185f7fedd7b24aea88ac1b6206522a66a2b5de11b7d1d8d3078d1ad175bf63.

- 2026-09-06T21:18:22+00:00: Recorded command exit 0; command argv SHA-256
  5d12c87c349772d104fdb43ead9913e4d346bbd337bd01fc621a007f18d1710d.

- 2026-09-06T21:19:01+00:00: Recorded command exit 1; command argv SHA-256
  7ba9030695cbd80ffbab797d62a9beccc5b61333b68c6ea5e7ab01525a5152ad.

- 2026-09-06T21:19:15+00:00: Recorded command exit 0; command argv SHA-256
  f71975b0e0b00a780fed3410ff70f306b8004ce22f8d1aecc438b8adc79fe8e9.

- 2026-09-06T21:19:27+00:00: Recorded command exit 0; command argv SHA-256
  2bfa70e56e0700f1936ea112c39e5f5d79584490104fd381369d35104ecc19ae.

- 2026-09-06T21:20:17+00:00: Recorded command exit 0; command argv SHA-256
  25207b320ad4204782e2db1b7cacc6fa99a74d8a745e25d61895e0601ee06505.

- 2026-09-06T21:21:10+00:00: Recorded command exit 101; command argv SHA-256
  579e494bde30fdd2a65a089c97b4bb11aaed8968fc1b6e507e156f52539ff4a9.

- 2026-09-06T21:21:27+00:00: Recorded command exit 0; command argv SHA-256
  25207b320ad4204782e2db1b7cacc6fa99a74d8a745e25d61895e0601ee06505.

- 2026-09-06T21:21:47+00:00: Original main 9543a32 failure reproduced at sandbox.rs:1329 with fresh
  external CARGO_TARGET_DIR and absent repository target. Signed+DCO fixture-only candidate 2b28fee
  changes only sandbox.rs tests: external-target/temp scratch base, PID plus atomic uniqueness, RAII
  fixture cleanup, and panic-path/no-repository-target regression. Original and negative tests pass
  on three distinct fresh targets with no residuals; one fresh full workspace run passed. A later
  fresh full run exposed a separate order-dependent ENOENT at tests/sandbox_boundary.rs:187 because
  target_root at line 44 still hardcodes repository target and the panic sentinel may execute before
  another test creates it. That path is outside current AR ownership; it was not edited or masked,
  and the empty residual target directory was removed. Clippy typo attempts and exact outcomes are
  retained in wrapper evidence.

- 2026-09-06T21:25:00+00:00: Recorded command exit 0; command argv SHA-256
  b6058f98fd23577b6803e77af4eb661df17e2c37e924329ba58040dfdc78180f.

- 2026-09-06T21:25:26+00:00: Recorded command exit 0; command argv SHA-256
  da3ced52682d53d4280c82d189cc02bdb13d285b39876cd6d29325f514cc0978.

- 2026-09-06T21:25:45+00:00: Recorded command exit 0; command argv SHA-256
  49e3ef9be34e75b475cee10027dfccec505a638f9ba801ab3311d2252174feb9.
