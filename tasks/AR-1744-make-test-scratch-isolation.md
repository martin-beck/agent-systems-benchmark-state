---
{
  "branch": "repair/ar-1744-make-test-scratch-isolation",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-08T14:41:03+00:00",
  "depends_on": [],
  "id": "AR-1744",
  "next_action": "Wait for PR #511 jobs 37788419498, 37788419514, and 37788419573 to finish; merge only after all required checks are green, then verify exact main.",
  "observed_branch": "repair/ar-1744-make-test-scratch-isolation",
  "observed_dirty": 1,
  "observed_head": "42b6453922c8b38fdab03e2b1aa2d396c0cf288e",
  "owner": "codex-ar1744-make-test",
  "plan": "../plans/AR-1744-make-test-scratch-isolation.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "contract-test",
    "evidence_digest": "",
    "evidence_ref": "",
    "spec_ref": "specs/AR-1744.json",
    "spec_revision": 1,
    "status": "pending"
  },
  "spec_ref": "specs/AR-1744.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Repair now also prevents plan-create tests from reading the operator terminal; focused test passes and PR #511 awaits three long-running CI jobs.",
  "task_revision": 99,
  "title": "Repair make test scratch-root isolation",
  "updated_at": "2026-10-08T14:04:28+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1744-make-test-scratch-isolation"
}
---

The current protected ASB main fails under `make test` because the Makefile
exports `CARGO_TARGET_DIR` into the test process while runtime scratch fixtures
derive their temporary roots from that variable. The resulting fixtures can be
created inside the repository Cargo target tree, violating the test contract
that scratch roots are external and private. The failure must be reproduced on
the exact main head, repaired without weakening path validation, and covered by
focused and full gates.

The repair must preserve the pinned toolchain, locked dependency/test path,
private bounded fixtures, cleanup guarantees, and all existing positive and
negative path checks. Add regression coverage for the Make invocation and the
named validated-linker environment test, update documentation only if needed,
and record exact PR, signature/DCO, CI, merge, and post-merge evidence.

- 2026-10-08T12:40:57+00:00: Dependencies verified; reproduce and repair current-main make test
  scratch isolation.

- 2026-10-08T12:41:03+00:00: Claimed by codex-ar1744-make-test.

- 2026-10-08T12:41:35+00:00: Recorded command exit 0; command argv SHA-256
  a014a10eb5dd4fa65cb2e51a89d085d13ae41eb5538833a58867e76d5d4ba18a.

- 2026-10-08T12:42:22+00:00: Recorded command exit 0; command argv SHA-256
  03006edd7c26ab149381fd8e64ec9685ed4567ae0f5d554c6aff520c8a67c503.

- 2026-10-08T12:43:09+00:00: Recorded command exit 0; command argv SHA-256
  ba6497e0660a2089fe8bb13f171c609310126866b1c97fc4fc731b7f2f5ffad4.

- 2026-10-08T12:43:41+00:00: Recorded command exit 0; command argv SHA-256
  7c730eec3ea71bd24ffc5a9255bf7f542481bf601dba6c72bed6e00f6c2fab3c.

- 2026-10-08T12:44:52+00:00: Recorded command exit 0; command argv SHA-256
  f71975b0e0b00a780fed3410ff70f306b8004ce22f8d1aecc438b8adc79fe8e9.

- 2026-10-08T12:45:22+00:00: Recorded command exit 0; command argv SHA-256
  d0f198b9a45d38114b538f0cff6b253a9963ac66566cf5946a99d7c709f8a3b3.

- 2026-10-08T12:46:47+00:00: Recorded command exit 2; command argv SHA-256
  3fc122cf075789d0bc02db7fd32de1be63709d388a5a8cb44f03ddbc0ae0dfb6.

- 2026-10-08T12:47:44+00:00: Recorded command exit 0; command argv SHA-256
  65bd39b6e995daa8de012e38f77d7d34e17aaa7f48f7d1538e37af30d16d3784.

- 2026-10-08T12:48:19+00:00: Recorded command exit 0; command argv SHA-256
  9a5585c26ae7ddbd2a1aa9e21b2c4b1a5d8a599f6e1b256c90d74782e7485a56.

- 2026-10-08T12:49:25+00:00: Recorded command exit 2; command argv SHA-256
  3fc122cf075789d0bc02db7fd32de1be63709d388a5a8cb44f03ddbc0ae0dfb6.

- 2026-10-08T12:50:23+00:00: Recorded command exit 0; command argv SHA-256
  79da272f7e4e7a786ca90e5ea99a1b051339fd1ac5cd8d61b67c8ebfbc695ad8.

- 2026-10-08T12:51:25+00:00: Recorded command exit 0; command argv SHA-256
  65bd39b6e995daa8de012e38f77d7d34e17aaa7f48f7d1538e37af30d16d3784.

- 2026-10-08T12:51:49+00:00: Recorded command exit 0; command argv SHA-256
  bc586414bde2565f55afc62585428f4cf76392ef9881a202e1b65e0f44409086.

- 2026-10-08T12:52:44+00:00: Recorded command exit 2; command argv SHA-256
  3fc122cf075789d0bc02db7fd32de1be63709d388a5a8cb44f03ddbc0ae0dfb6.

- 2026-10-08T12:53:26+00:00: Recorded command exit 0; command argv SHA-256
  79da272f7e4e7a786ca90e5ea99a1b051339fd1ac5cd8d61b67c8ebfbc695ad8.

- 2026-10-08T12:53:59+00:00: Recorded command exit 0; command argv SHA-256
  6120de36aaf3f41dd6cadb792c3fccfa2bc059e1af956c26b16aabbc0ee7bbd5.

- 2026-10-08T12:54:18+00:00: Recorded command exit 0; command argv SHA-256
  5aae83ac29c3f85de109ea29b48150a117904c8515ed8d5db74856ca02fc57c5.

- 2026-10-08T12:54:45+00:00: Recorded command exit 101; command argv SHA-256
  eda2cde3c975586ebd7e8518ce2393266fd48dbab02504429dac576245463534.

- 2026-10-08T12:55:30+00:00: Recorded command exit 0; command argv SHA-256
  79da272f7e4e7a786ca90e5ea99a1b051339fd1ac5cd8d61b67c8ebfbc695ad8.

- 2026-10-08T12:56:12+00:00: Recorded command exit 0; command argv SHA-256
  6120de36aaf3f41dd6cadb792c3fccfa2bc059e1af956c26b16aabbc0ee7bbd5.

- 2026-10-08T12:56:32+00:00: Recorded command exit 0; command argv SHA-256
  5e50e81fbb5690ff4db2861e06286f7b7dcf0553a556418719d833645165ccb4.

- 2026-10-08T12:57:00+00:00: Recorded command exit 0; command argv SHA-256
  eda2cde3c975586ebd7e8518ce2393266fd48dbab02504429dac576245463534.

- 2026-10-08T12:57:48+00:00: Recorded command exit 0; command argv SHA-256
  357a822a3bd5a5d87334198a3442d1d4928d1e30cc97d958472a952da89e3b5e.

- 2026-10-08T12:58:31+00:00: Recorded command exit 0; command argv SHA-256
  c4eabbd5df5c4e407a36e72104c180ac2908dbc1b4c4ca35b403ab1a6ae63d16.

- 2026-10-08T12:59:40+00:00: Recorded command exit 2; command argv SHA-256
  3fc122cf075789d0bc02db7fd32de1be63709d388a5a8cb44f03ddbc0ae0dfb6.

- 2026-10-08T13:00:47+00:00: Recorded command exit 0; command argv SHA-256
  79da272f7e4e7a786ca90e5ea99a1b051339fd1ac5cd8d61b67c8ebfbc695ad8.

- 2026-10-08T13:01:31+00:00: Recorded command exit 0; command argv SHA-256
  e0e814b48e1909b50ccabd4bb0699237298e6f32cf543810dd57274837794bd9.

- 2026-10-08T13:02:05+00:00: Recorded command exit 0; command argv SHA-256
  152bd0dab4e85ef6fe7ba3846fe6c3b765f0c26563da409c9923453e36cbf97d.

- 2026-10-08T13:03:29+00:00: Recorded command exit 2; command argv SHA-256
  3fc122cf075789d0bc02db7fd32de1be63709d388a5a8cb44f03ddbc0ae0dfb6.

- 2026-10-08T13:04:11+00:00: Recorded command exit 0; command argv SHA-256
  edf02434f25ea8c42479eb830253a273d3b3fdca4bbb2d91b2f1adffb3c1c3aa.

- 2026-10-08T13:05:23+00:00: Recorded command exit 2; command argv SHA-256
  3fc122cf075789d0bc02db7fd32de1be63709d388a5a8cb44f03ddbc0ae0dfb6.

- 2026-10-08T13:05:47+00:00: Recorded command exit 0; command argv SHA-256
  77f531c8550024b3fb6d94c965fd8d69f33b2fbd016f3688e26ba7cff0360060.

- 2026-10-08T13:07:06+00:00: Recorded command exit 2; command argv SHA-256
  3fc122cf075789d0bc02db7fd32de1be63709d388a5a8cb44f03ddbc0ae0dfb6.

- 2026-10-08T13:08:00+00:00: Recorded command exit 101; command argv SHA-256
  b6cc4cfcbdad37ecbeb90e4fa51d2ba1a3e39ba415767d77881c565bf0336098.

- 2026-10-08T13:09:03+00:00: Recorded command exit 101; command argv SHA-256
  195f3d9c2e7d9ae032177ae159d0a6785a5a268e53a84f1a43322eb9dc7b3f9f.

- 2026-10-08T13:09:32+00:00: Recorded command exit 0; command argv SHA-256
  79da272f7e4e7a786ca90e5ea99a1b051339fd1ac5cd8d61b67c8ebfbc695ad8.

- 2026-10-08T13:10:12+00:00: Recorded command exit 0; command argv SHA-256
  f88069dc41c1a5ec2f9bc39df2f03464b45f89f9d51c0abf09ee5aa8da4765a3.

- 2026-10-08T13:10:40+00:00: Recorded command exit 0; command argv SHA-256
  b02bd07a02c1781f91a2a91693f95f965f1a0030967f539eb19c3ea844f6d3c3.

- 2026-10-08T13:11:27+00:00: Recorded command exit 2; command argv SHA-256
  3fc122cf075789d0bc02db7fd32de1be63709d388a5a8cb44f03ddbc0ae0dfb6.

- 2026-10-08T13:11:49+00:00: Recorded command exit 0; command argv SHA-256
  7ffdd0e9859ac8fd73aec1dae2f614afad667dac82bead85368d718c9496697d.

- 2026-10-08T13:13:21+00:00: Recorded command exit 0; command argv SHA-256
  8c71ac629a497e7a7239bf2c40da3752354b57f3847d0a6ad6c9e332b6c5a95f.

- 2026-10-08T13:14:08+00:00: Recorded command exit 101; command argv SHA-256
  36493c4fb20e2236f456686dbf53cf3d5b4119699e8785b57bc169abad2cf78e.

- 2026-10-08T13:15:46+00:00: Recorded command exit 1; command argv SHA-256
  0cb92d2830b71d23dd5394183f04eb60eee0fd4aabe090fbc8e5ef70fb9a8ea6.

- 2026-10-08T13:17:13+00:00: Recorded command exit 0; command argv SHA-256
  498be40a39ada4cd36b28eeb4019b51a08000f15ef8b71888991a0cf70f71067.

- 2026-10-08T13:19:51+00:00: Recorded command exit 0; command argv SHA-256
  0cb92d2830b71d23dd5394183f04eb60eee0fd4aabe090fbc8e5ef70fb9a8ea6.

- 2026-10-08T13:30:10+00:00: Recorded command exit 0; command argv SHA-256
  ed4753b5920a4b18b66f8b4ab26918e1d588633e35fef08f12279e1dbcd54329.

- 2026-10-08T13:30:41+00:00: Recorded command exit 1; command argv SHA-256
  b4d536ccc1f1b3b4db3f5f122c5e4827377257db96ee78386e35c55156c8ffdd.

- 2026-10-08T13:31:08+00:00: Recorded command exit 1; command argv SHA-256
  b4d536ccc1f1b3b4db3f5f122c5e4827377257db96ee78386e35c55156c8ffdd.

- 2026-10-08T13:31:33+00:00: Recorded command exit 0; command argv SHA-256
  b4d536ccc1f1b3b4db3f5f122c5e4827377257db96ee78386e35c55156c8ffdd.

- 2026-10-08T13:31:55+00:00: Recorded command exit 1; command argv SHA-256
  b4d536ccc1f1b3b4db3f5f122c5e4827377257db96ee78386e35c55156c8ffdd.

- 2026-10-08T13:32:22+00:00: Recorded command exit 1; command argv SHA-256
  b4d536ccc1f1b3b4db3f5f122c5e4827377257db96ee78386e35c55156c8ffdd.

- 2026-10-08T13:32:54+00:00: Recorded command exit 1; command argv SHA-256
  b4d536ccc1f1b3b4db3f5f122c5e4827377257db96ee78386e35c55156c8ffdd.

- 2026-10-08T13:33:22+00:00: Recorded command exit 1; command argv SHA-256
  b4d536ccc1f1b3b4db3f5f122c5e4827377257db96ee78386e35c55156c8ffdd.

- 2026-10-08T13:33:50+00:00: Recorded command exit 1; command argv SHA-256
  b4d536ccc1f1b3b4db3f5f122c5e4827377257db96ee78386e35c55156c8ffdd.

- 2026-10-08T13:34:18+00:00: Recorded command exit 1; command argv SHA-256
  b4d536ccc1f1b3b4db3f5f122c5e4827377257db96ee78386e35c55156c8ffdd.

- 2026-10-08T13:34:35+00:00: Recorded command exit 0; command argv SHA-256
  36493c4fb20e2236f456686dbf53cf3d5b4119699e8785b57bc169abad2cf78e.

- 2026-10-08T13:35:10+00:00: Focused named test passes (1/1) under handoffctl. Full env
  RUST_TEST_THREADS=1 make test passed. PR #511 head cbcfa025ca31e5a216076a3bc9d3bd3fb4d2f874 has
  every required check green except emulated-aarch64 job 113337465103; stale queued attempt was
  cancelled and rerun once, but runner assignment is still pending. No merge attempted.

- 2026-10-08T13:38:04+00:00: Recorded command exit 0; command argv SHA-256
  3fc122cf075789d0bc02db7fd32de1be63709d388a5a8cb44f03ddbc0ae0dfb6.

- 2026-10-08T13:38:44+00:00: Recorded command exit 129; command argv SHA-256
  89acba3111d0be4d622dc0b8ed90242ff67b0e43aef52840a274689e6d088e2a.

- 2026-10-08T13:39:19+00:00: Recorded command exit 0; command argv SHA-256
  2d565b0d9649934932c722cc971c74e243922b01ebd24fd224c76861f0e6b8a7.

- 2026-10-08T13:39:53+00:00: Recorded command exit 0; command argv SHA-256
  ddc84cd45863ba7a3818bfe15427b182beba40ee17d9a26f2dda465291922ff0.

- 2026-10-08T13:40:32+00:00: Recorded command exit 0; command argv SHA-256
  85d7931526bf76ea7e6d175da89de2854609a3f285d6023ddda347f87b4b3f02.

- 2026-10-08T13:44:18+00:00: Added RUST_TEST_THREADS ?= 1 to Makefile with documented override and
  passed plain make test through handoffctl. PR head is 0d057ade6f450ded6255aa1500b0023a0969ecbd.
  Fast checks are green; remaining required jobs are in progress without failures.

- 2026-10-08T13:51:05+00:00: Recorded command exit 0; command argv SHA-256
  60784069cad657573cf381fda6969a0403149c741eede8d8378e03cd00027a09.

- 2026-10-08T13:52:21+00:00: Recorded command exit 0; command argv SHA-256
  79da272f7e4e7a786ca90e5ea99a1b051339fd1ac5cd8d61b67c8ebfbc695ad8.

- 2026-10-08T13:52:57+00:00: Recorded command exit 0; command argv SHA-256
  e7856fdbe5b7ccde26c626200fae10a3624e91633260bda551b24ee85bd3ee1b.

- 2026-10-08T13:53:29+00:00: Recorded command exit 0; command argv SHA-256
  3ac90ee4cb903aa496ac880a1708f9545b3f7056d40866dfb0b0cb7cb3ba8c4f.

- 2026-10-08T13:54:06+00:00: Recorded command exit 0; command argv SHA-256
  79da272f7e4e7a786ca90e5ea99a1b051339fd1ac5cd8d61b67c8ebfbc695ad8.

- 2026-10-08T13:54:38+00:00: Recorded command exit 0; command argv SHA-256
  3ac90ee4cb903aa496ac880a1708f9545b3f7056d40866dfb0b0cb7cb3ba8c4f.

- 2026-10-08T13:55:05+00:00: Recorded command exit 0; command argv SHA-256
  e274074a17e0682b5edf79b5caca577a41520ed9ca8daf9342f0433b678582a1.

- 2026-10-08T13:56:09+00:00: Recorded command exit 0; command argv SHA-256
  bc894b528fa93cd1c91c7d0023bfcd64046b50c889c8b57d5ded65f9f3797f8b.

- 2026-10-08T13:56:43+00:00: Recorded command exit 0; command argv SHA-256
  85d7931526bf76ea7e6d175da89de2854609a3f285d6023ddda347f87b4b3f02.

- 2026-10-08T14:00:28+00:00: Root cause confirmed: create_plan used io::stdin().is_terminal()
  despite the test harness passing no stdin, then blocked read_line on the terminal. Fix commit
  42b6453922c8b38fdab03e2b1aa2d396c0cf288e passes the exact test immediately, uses injected stdin,
  and bounds interactive selection to 64 bytes. PR #511 fast checks are green; three hosted jobs
  remain pending with no failure.

- 2026-10-08T14:03:29+00:00: Recorded command exit 0; command argv SHA-256
  9101955416b0fa537273d09b73dd8f87f10eb9f0d755f697fc109c68bd64e4e8.

- 2026-10-08T14:03:55+00:00: Recorded command exit 0; command argv SHA-256
  a5e91d8a6e356ba88fd4835c765ebd2411c75eacaa60f98e203295ec257bd3a5.

- 2026-10-08T14:04:28+00:00: Recorded command exit 0; command argv SHA-256
  ce7d45fffe378f17b6453e4e851b9576b579444d490ac31ccb139f845c58245e.
