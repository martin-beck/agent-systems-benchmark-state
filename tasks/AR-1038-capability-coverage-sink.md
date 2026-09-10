---
{
  "branch": "test/capability-coverage-sink",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-11T00:59:58+00:00",
  "depends_on": [
    "AR-1023"
  ],
  "id": "AR-1038",
  "next_action": "Preserve the validated external LLVM coverage sink across capability test env_clear without inheriting other ambient state.",
  "observed_branch": "test/capability-coverage-sink",
  "observed_dirty": 1,
  "observed_head": "58d0da27736d6c22ca7c43f76ade497165b29919",
  "owner": "codex-ar1038-coverage-20260911",
  "plan": "../plans/AR-1038.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Prevent sanitized capability child tests from writing default profraw files into the source checkout.",
  "task_revision": 8,
  "title": "Preserve coverage sinks in sanitized CLI child tests",
  "updated_at": "2026-09-10T23:04:12+00:00",
  "worktree_key": "agent-systems-benchmark-capability-coverage-sink"
}
---
## AR-1038

Fix the six `default_*.profraw` files discovered during AR-1013 full coverage without weakening
`env_clear()`. This is an ASB test-harness repair only and owns no standalone TUI or production UI.

- 2026-09-10T22:59:55+00:00: AR-1023 is complete; focused capability test-harness repair is
  dependency-ready.

- 2026-09-10T22:59:58+00:00: Claimed by codex-ar1038-coverage-20260911.

- 2026-09-10T23:01:26+00:00: Recorded command exit 0; command argv SHA-256
  ff96f1201b06672675efd403b806dc7c27fdaac28f0179b14754fde91d4abfb8.

- 2026-09-10T23:03:23+00:00: Recorded command exit 2; command argv SHA-256
  48458d4adcbc2714c4ae60f17ec39d916357031118af6e75d9a5cd826c73f20e.

- 2026-09-10T23:04:06+00:00: Recorded command exit 0; command argv SHA-256
  190f52074d594af56f94d8dee69d460ecc0ba6f773d6d0afeead797fd7ed872d.
