---
{
  "branch": "repair/ar-1398-signed-protected-main-recovery",
  "checkpoint_commit": "b63394b167d453738364f4eca73af76838ef1937",
  "claim_expires": "2026-09-24T12:25:33+00:00",
  "depends_on": [
    "AR-1337"
  ],
  "id": "AR-1398",
  "next_action": "Watch all seven exact-main workflows for merge b63394b; after terminal success, record conclusions and release AR-1398 done.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "0000000000000000000000000000000000000000",
  "owner": "ar1398_signed_recovery_luna56",
  "plan": "../plans/AR-1398-signed-protected-main-recovery.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Restore signed+DCO protected-main evidence after an unsigned GitHub-generated repair merge.",
  "task_revision": 64,
  "title": "Signed protected-main recovery",
  "updated_at": "2026-09-24T10:25:56+00:00",
  "worktree_key": ""
}
---

# AR-1398

This is an integration/publication repair only. It must not change workload
semantics, OpenRouter behavior, native-evidence policy, or asb-tui. External
providers are never required for development evidence.

- 2026-09-24T09:58:18+00:00: Protected-main audit requires signed descendant recovery after PR #286
  merge 123ba915; preserve historical evidence and restore signed+DCO exact-main proof.

- 2026-09-24T10:00:09+00:00: Claimed by ar1398_signed_recovery_luna56.

- 2026-09-24T10:00:44+00:00: Recorded command exit 0; command argv SHA-256
  c725572ba4f53df0f5d848d1c6861633cd446ff51c3e8c3a06f5a000630c5f61.

- 2026-09-24T10:01:11+00:00: Recorded command exit 0; command argv SHA-256
  8fade593bd1ee9ba7c7ebfb3646c2d83591a375f5df4fc68f8f4ab22b6b730cb.

- 2026-09-24T10:01:39+00:00: Recorded command exit 1; command argv SHA-256
  afdc768d3b8a1656a6db8a2cf3e170572c704ef8520da22d8b1956304821b5c0.

- 2026-09-24T10:02:00+00:00: Recorded command exit 0; command argv SHA-256
  87cd4bb47c5cb6cbb3f94935be7cae7c1f98416231eb9de5ba30dfa616e9fda0.

- 2026-09-24T10:02:32+00:00: Recovery commit f5680de is SSH-signed+DCO, parent 123ba915, identical
  tree, zero files changed. Initial push attempt omitted fully qualified refs and was rejected
  without remote effect; corrected push succeeded to repair/ar-1398-signed-protected-main-recovery.
  Continue with PR review and exact-main qualification.

- 2026-09-24T10:03:09+00:00: Recorded command exit 0; command argv SHA-256
  e104568cf8d119cf1befccb214dd9155882c8513a5c249e8b44ee403a4d84634.

- 2026-09-24T10:03:44+00:00: Recorded command exit 0; command argv SHA-256
  95adf97c4cb200cb005384230ca6a459328da84887a3d23e47fa096791afe694.

- 2026-09-24T10:04:12+00:00: Heartbeat by ar1398_signed_recovery_luna56.

- 2026-09-24T10:04:22+00:00: Recorded command exit 8; command argv SHA-256
  6ee9976d1a5d4049c16287d0368110437d5838b542c5ededd08311da5aa58c3a.

- 2026-09-24T10:04:41+00:00: Recorded command exit 8; command argv SHA-256
  6ee9976d1a5d4049c16287d0368110437d5838b542c5ededd08311da5aa58c3a.

- 2026-09-24T10:05:02+00:00: Heartbeat by ar1398_signed_recovery_luna56.

- 2026-09-24T10:05:06+00:00: Recorded command exit 8; command argv SHA-256
  6ee9976d1a5d4049c16287d0368110437d5838b542c5ededd08311da5aa58c3a.

- 2026-09-24T10:05:25+00:00: Recorded command exit 8; command argv SHA-256
  6ee9976d1a5d4049c16287d0368110437d5838b542c5ededd08311da5aa58c3a.

- 2026-09-24T10:05:45+00:00: Recorded command exit 0; command argv SHA-256
  8e70d7296333048b35eed5250ee116b3901394b2133cdbd7e2c791bf3cc5d26b.

- 2026-09-24T10:06:09+00:00: PR #287 exact head f5680de is based directly on 123ba915 and has no
  file changes. Exact-head run IDs: 35984949129 emulated aarch64 pending; 35984949118 repository
  quality pending; 35984949114 Rust verification pending; 35984949065 formal assurance pending;
  35984949070 fault assurance success; 35984949047 AWQ shadow success; 35984949142 headers success;
  35984949137 platform success. No failures.

- 2026-09-24T10:06:20+00:00: Heartbeat by ar1398_signed_recovery_luna56.

- 2026-09-24T10:06:24+00:00: Recorded command exit 8; command argv SHA-256
  6ee9976d1a5d4049c16287d0368110437d5838b542c5ededd08311da5aa58c3a.

- 2026-09-24T10:06:43+00:00: Recorded command exit 0; command argv SHA-256
  4597209fd38723e1dd39681c4258a62eec74fd3ba636c5bbc14e9559efddd1fc.

- 2026-09-24T10:07:03+00:00: Recorded command exit 8; command argv SHA-256
  6ee9976d1a5d4049c16287d0368110437d5838b542c5ededd08311da5aa58c3a.

- 2026-09-24T10:07:27+00:00: Formal assurance run 35984949065 is now fully green: TLC/Alloy and
  Loom/state models passed. Remaining exact-head groups are emulated aarch64 35984949129, repository
  quality 35984949118, and Rust verification 35984949114; all other checks green.

- 2026-09-24T10:07:42+00:00: Heartbeat by ar1398_signed_recovery_luna56.

- 2026-09-24T10:07:45+00:00: Recorded command exit 8; command argv SHA-256
  6ee9976d1a5d4049c16287d0368110437d5838b542c5ededd08311da5aa58c3a.

- 2026-09-24T10:10:04+00:00: Recorded command exit 0; command argv SHA-256
  038a68313e304021cd516ea5d536b1cec3a618a993db00fefa71bb079fb1fd0a.

- 2026-09-24T10:10:27+00:00: Exact failure in repository quality run 35984949118: asb-metrics
  kernel::tests::bounded_tool_boundary_covers_success_denial_timeout_and_cleanup panicked at
  crates/asb-metrics/src/kernel.rs:646. Expected ProbeResult value Some(12500000), got unavailable
  ToolMismatch. 15 passed, 1 failed, 4 ignored; cargo llvm-cov exited 101. This is an existing
  fixture/test path, not recovery-commit content. No merge permitted.

- 2026-09-24T10:10:35+00:00: Recorded command exit 0; command argv SHA-256
  887e131b8d79411845a5ac004cca377e14e91df405f5756ee717eb797f09e7bb.

- 2026-09-24T10:10:55+00:00: Recorded command exit 1; command argv SHA-256
  665a4d2fad398c5eef451f667b9dbdd255326a76f88f706cd2c809f9134d0299.

- 2026-09-24T10:11:14+00:00: Recorded command exit 0; command argv SHA-256
  c3e0632183a1f025d901efafec5ba960247032171251b32902ae2dee400b0ced.

- 2026-09-24T10:11:39+00:00: Reran failed workflow 35984949118 through handoffctl using gh run rerun
  --failed. Same exact head f5680de, attempt 2 is currently in progress. No product changes made.

- 2026-09-24T10:11:47+00:00: Heartbeat by ar1398_signed_recovery_luna56.

- 2026-09-24T10:11:51+00:00: Recorded command exit 0; command argv SHA-256
  54a85e80e0b88f145960b050a249de69a505219a1c1cd18a4e47301eb7c5b266.

- 2026-09-24T10:12:10+00:00: Recorded command exit 8; command argv SHA-256
  6ee9976d1a5d4049c16287d0368110437d5838b542c5ededd08311da5aa58c3a.

- 2026-09-24T10:12:32+00:00: Recorded command exit 8; command argv SHA-256
  6ee9976d1a5d4049c16287d0368110437d5838b542c5ededd08311da5aa58c3a.

- 2026-09-24T10:12:51+00:00: Recorded command exit 0; command argv SHA-256
  54a85e80e0b88f145960b050a249de69a505219a1c1cd18a4e47301eb7c5b266.

- 2026-09-24T10:13:11+00:00: Heartbeat by ar1398_signed_recovery_luna56.

- 2026-09-24T10:13:15+00:00: Recorded command exit 8; command argv SHA-256
  6ee9976d1a5d4049c16287d0368110437d5838b542c5ededd08311da5aa58c3a.

- 2026-09-24T10:13:36+00:00: Recorded command exit 0; command argv SHA-256
  20ff7a6bbcaeec2fea4499ec1b84d9a97da6d80610b1c92a005b89f353ac4473.

- 2026-09-24T10:14:38+00:00: Heartbeat by ar1398_signed_recovery_luna56.

- 2026-09-24T10:14:46+00:00: Recorded command exit 8; command argv SHA-256
  6ee9976d1a5d4049c16287d0368110437d5838b542c5ededd08311da5aa58c3a.

- 2026-09-24T10:19:29+00:00: Recorded command exit 2; command argv SHA-256
  b914238e07f012b8983974f67200aa4c6619adcb80595382ef8e08c090e874de.

- 2026-09-24T10:19:51+00:00: Recorded command exit 1; command argv SHA-256
  bf1e8a01dbb63e7e1bd54d7b93679fd230be2aa451bbd3489256a907dcd416a6.

- 2026-09-24T10:20:13+00:00: Recorded command exit 0; command argv SHA-256
  c725572ba4f53df0f5d848d1c6861633cd446ff51c3e8c3a06f5a000630c5f61.

- 2026-09-24T10:20:42+00:00: Recorded command exit 0; command argv SHA-256
  bf1e8a01dbb63e7e1bd54d7b93679fd230be2aa451bbd3489256a907dcd416a6.

- 2026-09-24T10:21:07+00:00: Recorded command exit 0; command argv SHA-256
  8e70d7296333048b35eed5250ee116b3901394b2133cdbd7e2c791bf3cc5d26b.

- 2026-09-24T10:21:38+00:00: Final review passed: PR #287 head f5680de is SSH Good and DCO-signed,
  parent 123ba915, tree 5e10b6a1, zero changed files. Signed merge_pr.py ran from clean isolated
  worktree at approved base 123ba915 and published merge b63394b167d453738364f4eca73af76838ef1937
  with parents 123ba915 and f5680de, identical tree, Good SSH signature and matching DCO. Exact-main
  workflows dispatched: Huawei 35986670232 (success), emulated aarch64 35986670215, fault
  35986670237, repository quality 35986670309, hosted portability 35986670359, Rust 35986670370,
  formal 35986670435 (remaining six in progress). Historical unsigned merge 123ba915 preserved.

- 2026-09-24T10:21:51+00:00: Heartbeat by ar1398_signed_recovery_luna56.

- 2026-09-24T10:21:55+00:00: Recorded command exit 0; command argv SHA-256
  fbaf903bb42afac5a76db563ff8f8547411b2a4e9fe37d94e7c7eceaa6286098.

- 2026-09-24T10:22:15+00:00: Recorded command exit 0; command argv SHA-256
  fbaf903bb42afac5a76db563ff8f8547411b2a4e9fe37d94e7c7eceaa6286098.

- 2026-09-24T10:22:39+00:00: Heartbeat by ar1398_signed_recovery_luna56.

- 2026-09-24T10:22:43+00:00: Recorded command exit 0; command argv SHA-256
  fbaf903bb42afac5a76db563ff8f8547411b2a4e9fe37d94e7c7eceaa6286098.

- 2026-09-24T10:23:03+00:00: Recorded command exit 0; command argv SHA-256
  fbaf903bb42afac5a76db563ff8f8547411b2a4e9fe37d94e7c7eceaa6286098.

- 2026-09-24T10:23:22+00:00: Heartbeat by ar1398_signed_recovery_luna56.

- 2026-09-24T10:23:26+00:00: Recorded command exit 0; command argv SHA-256
  fbaf903bb42afac5a76db563ff8f8547411b2a4e9fe37d94e7c7eceaa6286098.

- 2026-09-24T10:23:48+00:00: Recorded command exit 0; command argv SHA-256
  fbaf903bb42afac5a76db563ff8f8547411b2a4e9fe37d94e7c7eceaa6286098.

- 2026-09-24T10:24:07+00:00: Heartbeat by ar1398_signed_recovery_luna56.

- 2026-09-24T10:24:11+00:00: Recorded command exit 0; command argv SHA-256
  fbaf903bb42afac5a76db563ff8f8547411b2a4e9fe37d94e7c7eceaa6286098.

- 2026-09-24T10:24:32+00:00: Recorded command exit 0; command argv SHA-256
  fbaf903bb42afac5a76db563ff8f8547411b2a4e9fe37d94e7c7eceaa6286098.

- 2026-09-24T10:24:52+00:00: Recorded command exit 0; command argv SHA-256
  57982755fe74d7a25f0a2108193fa80de6799adc0b3e21ca33ad5e565ac9b5a4.

- 2026-09-24T10:25:13+00:00: Recorded command exit 0; command argv SHA-256
  fbaf903bb42afac5a76db563ff8f8547411b2a4e9fe37d94e7c7eceaa6286098.

- 2026-09-24T10:25:33+00:00: Heartbeat by ar1398_signed_recovery_luna56.

- 2026-09-24T10:25:36+00:00: Recorded command exit 0; command argv SHA-256
  fbaf903bb42afac5a76db563ff8f8547411b2a4e9fe37d94e7c7eceaa6286098.

- 2026-09-24T10:25:56+00:00: Recorded command exit 0; command argv SHA-256
  fbaf903bb42afac5a76db563ff8f8547411b2a4e9fe37d94e7c7eceaa6286098.
