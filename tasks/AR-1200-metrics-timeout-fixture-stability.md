---
{
  "branch": "repair/metrics-timeout-flake",
  "checkpoint_commit": "0a7f6a192af9b6a538c7547dfff9e65842d59049",
  "claim_expires": "2026-09-15T11:29:16+00:00",
  "depends_on": [],
  "id": "AR-1200",
  "next_action": "Review and merge the isolated test-fixture stabilization after exact-head CI passes; do not modify production timeout policy.",
  "owner": "root-ar1200-metrics",
  "plan": "../plans/AR-1200.md",
  "priority": "P2",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Remove hosted timing flakiness from the bounded kernel diagnostic rejection test.",
  "task_revision": 5,
  "title": "Kernel diagnostic rejection fixture stability",
  "updated_at": "2026-09-15T10:04:13+00:00",
  "worktree_key": "agent-systems-benchmark-metrics-timeout-flake"
}
---

The bounded kernel diagnostic test launched the complete instrumented test binary for its
rejection case while enforcing a 100 ms deadline. Hosted CI intermittently observed
`TimedOut` instead of the expected `ProbeRejected`, because process startup and scheduler
load consumed the test deadline before the panic fixture ran. This AR keeps the production
deadline unchanged and uses a tiny pinned rejection fixture script instead. The actual
failure classification, output bounds, staging verification, and cleanup remain exercised.


- 2026-09-15T09:29:16+00:00: Claimed by root-ar1200-metrics.

- 2026-09-15T09:31:27+00:00: Separate PR #175 published from signed branch
  repair/metrics-timeout-flake at exact head 0a7f6a192af9b6a538c7547dfff9e65842d59049. The candidate
  keeps production timeout behavior unchanged and replaces only the flaky test-binary rejection
  subprocess with a pinned fixture. Pre-fix focused test passed 30 local repetitions but failed
  hosted PR #174 run 34951783425 with TimedOut instead of ProbeRejected; fixed candidate passed 30
  focused repetitions, full asb-metrics unit tests (16 passed, 4 ignored), fmt, clippy -D warnings,
  and diff check. Await exact-head PR #175 CI and independent review; do not merge PR #174 here.

- 2026-09-15T10:02:09+00:00: PR #175 merged at immutable main SHA
  ef82484fa78dd31c0d7b5ad48e2dc51a93ec1339. Post-merge runs: 34955354481 success, 34955354446
  completed success, 34955354399 success; 34955354479 Rust verification, 34955354482 Formal
  assurance, and 34955354389 Emulated aarch64 remain in progress. Repository quality 34955354581
  failed with protected-main merge-tree mismatch (range
  d354a5127c8d065de64432fb443200612df10f6d..ef82484fa78dd31c0d7b5ad48e2dc51a93ec1339); keep
  in_progress and investigate before release.

- 2026-09-15T10:04:13+00:00: Post-merge watch terminal: 34955354389 Emulated aarch64 success; all
  assurance runs for merge SHA ef82484fa78dd31c0d7b5ad48e2dc51a93ec1339 are terminal and successful
  except Repository quality 34955354581 failure. Failure is the protected-main merge-tree mismatch
  caused by merging stale-base PR #175 after #174 (range
  d354a5127c8d065de64432fb443200612df10f6d..ef82484fa78dd31c0d7b5ad48e2dc51a93ec1339). Do not
  release until policy failure is remediated or explicitly adjudicated.
