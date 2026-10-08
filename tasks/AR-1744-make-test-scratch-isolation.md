---
{
  "branch": "repair/ar-1744-make-test-scratch-isolation",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-08T14:41:03+00:00",
  "depends_on": [],
  "id": "AR-1744",
  "next_action": "Reproduce the current-main make test failure and repair test scratch-root isolation.",
  "observed_branch": "repair/ar-1744-make-test-scratch-isolation",
  "observed_dirty": 0,
  "observed_head": "cbcfa025ca31e5a216076a3bc9d3bd3fb4d2f874",
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
  "summary": "Repair make test failure caused by runtime scratch fixtures inheriting the Cargo target directory.",
  "task_revision": 60,
  "title": "Repair make test scratch-root isolation",
  "updated_at": "2026-10-08T13:14:08+00:00",
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
