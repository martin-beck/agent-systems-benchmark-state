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
  "task_revision": 14,
  "title": "Preserve coverage sinks in sanitized CLI child tests",
  "updated_at": "2026-09-10T23:08:10+00:00",
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

- 2026-09-10T23:04:32+00:00: Recorded command exit 0; command argv SHA-256
  256423c8900d6dfa34df9cd63ce7a37fb83bfb6a1ff21374798ee71f3ab21c4d.

- 2026-09-10T23:05:55+00:00: Recorded command exit 1; command argv SHA-256
  b98fa5f31a3776574cfc43aede3198a94d130dcc4f49ded27ed7d0efea649b83.

- 2026-09-10T23:06:35+00:00: Recorded command exit 0; command argv SHA-256
  94a980f40fcbfe6659cf967b318dc33fad47361d16ec87dfa0c880d859eb111a.

- 2026-09-10T23:06:54+00:00: Recorded command exit 0; command argv SHA-256
  256423c8900d6dfa34df9cd63ce7a37fb83bfb6a1ff21374798ee71f3ab21c4d.

- 2026-09-10T23:07:20+00:00: Recorded command exit 0; command argv SHA-256
  e05bd290238ddb252923c16c6ed0a31803232940b7311848859f6f386763703a.

- 2026-09-10T23:08:10+00:00: Recorded command exit 0; command argv SHA-256
  d6b9ab339d7d3c0ad428bd006af6b4ccef78a0452b921c313218a605c6caf3b3.
