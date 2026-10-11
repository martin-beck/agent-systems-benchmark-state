---
{
  "branch": "feature/ar-1778-pinned-source-build-and-project-dependencies",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1776"
  ],
  "id": "AR-1778",
  "next_action": "Accept AR-1778 with exact-main postmerge evidence at d64ac90a; then release done after durable acceptance.",
  "observed_branch": "feature/ar-1778-pinned-source-build-and-project-dependencies",
  "observed_dirty": 0,
  "observed_head": "1c11b88d2790447c6d277342c8233fdf245ba391",
  "owner": "",
  "plan": "../plans/AR-1778-pinned-source-build-and-project-dependencies.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "mechanical",
    "evidence_digest": "sha256:b1515b297f4836576e897f53f1d8cc224353dc1f632593d415034623fb6df507",
    "evidence_ref": "https://github.com/martin-beck/agent-systems-benchmark/pull/568",
    "spec_ref": "specs/AR-1778.json",
    "spec_revision": 1,
    "status": "pass"
  },
  "spec_ref": "specs/AR-1778.json",
  "spec_revision": 1,
  "status": "done",
  "summary": "Build supported tools from verified pinned source and materialize missing dependencies in a project-owned prefix.",
  "task_revision": 38,
  "title": "Pinned source builds and project dependencies",
  "updated_at": "2026-10-11T08:55:50+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1778-pinned-source-build-and-project-dependencies"
}
---

When no compatible verified prebuilt artifact exists, `asb tool install` must
build the supported tool from the acquisition catalog's exact source revision.
Materialize every missing declared build/runtime dependency into a bounded,
project-owned prefix using its own pinned source/artifact recipe, rather than
requiring a user to preinstall it, invoking `sudo`, or mutating global package
manager state. Reuse a system dependency only after validating its catalog
identity and compatibility; record every reuse/build dependency in the receipt.

Builds run in a bounded isolated staging environment with a declared compiler/
toolchain, environment, network phase, resource/time limits, no inherited
credentials, and no arbitrary project shell hooks. Verify source identity before
build, verify declared outputs/entrypoint afterward, collect only safe bounded
diagnostics, atomically publish the final tool and dependency closure, and clean
only transaction-owned staging data. Missing compiler/platform support, failed
dependency build, build-script policy rejection, output mismatch, and resource
limit are distinct actionable outcomes.

- 2026-10-11T08:14:46+00:00: Dependency AR-1776 is complete; opening AR-1778 for implementation per
  coordinated plan.

- 2026-10-11T08:14:52+00:00: Claimed by codex-ar1778-luna56.

- 2026-10-11T08:20:30+00:00: Heartbeat by codex-ar1778-luna56.

- 2026-10-11T08:22:18+00:00: Recorded command exit 0; command argv SHA-256
  e00ddc47d1f97e96e8d5b5d1cb147d84ae24445b5e6e936757809f0ee0e5821c.

- 2026-10-11T08:23:01+00:00: Heartbeat by codex-ar1778-luna56.

- 2026-10-11T08:23:08+00:00: Recorded command exit 0; command argv SHA-256
  a24d8ddac1475fd88c905a457454eb908ea48d17dfe65c58ea9213a04ce7b8fc.

- 2026-10-11T08:24:20+00:00: Recorded command exit 0; command argv SHA-256
  780a79fcab6a88f44c65a1c800ec215251ab9b9960f708c32ff0ee8c8063d4c4.

- 2026-10-11T08:25:11+00:00: Recorded command exit 0; command argv SHA-256
  87fc6c1bf8da5627b98b9cb295981c49991e3c8c9c0061f1714286a1ef004711.

- 2026-10-11T08:25:55+00:00: Heartbeat by codex-ar1778-luna56.

- 2026-10-11T08:26:00+00:00: Recorded command exit 0; command argv SHA-256
  01f18e24d6f2b404308afdf4e1de75f8744a5a0452f0d14b86477d57b6ce3bf3.

- 2026-10-11T08:28:39+00:00: Recorded command exit 0; command argv SHA-256
  ed516f6f0da731f7f0c8670680dc0151dbd38c6637e417bb47b211eb4c8699ca.

- 2026-10-11T08:29:28+00:00: Recorded command exit 0; command argv SHA-256
  b7c438686581cf292b6cd41497ceabb3af42dfed57e04dfd6cc89efed8e2d15b.

- 2026-10-11T08:31:52+00:00: Recorded command exit 0; command argv SHA-256
  780a79fcab6a88f44c65a1c800ec215251ab9b9960f708c32ff0ee8c8063d4c4.

- 2026-10-11T08:32:38+00:00: Recorded command exit 0; command argv SHA-256
  77a9202bfab57536964bbe8deb47c01ab14d71e7e39961bcb06ca6e1d31a264f.

- 2026-10-11T08:33:06+00:00: Recorded command exit 0; command argv SHA-256
  ff2282a95ca1c6c17ceac3ebe66584e5898db9c0b814b01f29105f3fc1b053a7.

- 2026-10-11T08:35:04+00:00: Heartbeat by codex-ar1778-luna56.

- 2026-10-11T08:35:24+00:00: Observed exact product head 30d397f3 after rebase onto protected main
  4245b4a1; full asb-cli suite 348 passed, focused source-builder/catalog tests and clippy passed.
  PR #568 required checks remain in progress; separate technical review and protected merge are
  pending.

- 2026-10-11T08:37:00+00:00: Recorded command exit 0; command argv SHA-256
  780a79fcab6a88f44c65a1c800ec215251ab9b9960f708c32ff0ee8c8063d4c4.

- 2026-10-11T08:37:44+00:00: Recorded command exit 0; command argv SHA-256
  203382bcbbcd33861c67b4daba675aa8b99ed72c3ad932e6996a5827ef403500.

- 2026-10-11T08:38:36+00:00: Recorded command exit 0; command argv SHA-256
  a5e91d8a6e356ba88fd4835c765ebd2411c75eacaa60f98e203295ec257bd3a5.

- 2026-10-11T08:39:00+00:00: Recorded command exit 0; command argv SHA-256
  ce7d45fffe378f17b6453e4e851b9576b579444d490ac31ccb139f845c58245e.

- 2026-10-11T08:39:21+00:00: Recorded command exit 0; command argv SHA-256
  ff2282a95ca1c6c17ceac3ebe66584e5898db9c0b814b01f29105f3fc1b053a7.

- 2026-10-11T08:40:07+00:00: Heartbeat by codex-ar1778-luna56.

- 2026-10-11T08:46:12+00:00: Heartbeat by codex-ar1778-luna56.

- 2026-10-11T08:46:34+00:00: Independent exact-diff review completed on 1c11b88d: source entrypoint
  traversal fenced, offline package recipes constrained, provenance digest refreshed and workflow
  transcript 3/3 green. No merge until remaining required CI and review decision pass.

- 2026-10-11T08:51:00+00:00: Recorded command exit 1; command argv SHA-256
  56da2adb7697ad56a60a96e6e420d11687503f3fec9cb37f457a98eefb1b9795.

- 2026-10-11T08:51:44+00:00: Recorded command exit 1; command argv SHA-256
  0e5aa838f4f744e0652aa46f0a58ed12fa17f544bc9d10f3d26d5928536c1de6.

- 2026-10-11T08:52:39+00:00: Recorded command exit 0; command argv SHA-256
  350f94e9e0ba1970ca86b4e6dad1d1796ad9d7d72c916aca3a2faf80de780190.

- 2026-10-11T08:55:03+00:00: Protected merge complete: PR #568 merged as
  d64ac90ad96a0941ddf6acb2d60ffe7b2ab5f948 with reviewed tree
  3d60069e79c6bf725de3dac489acc27cdf320fc2. Exact-main worktree clean; asb-cli lib 235/235 passed,
  source-builder 3/3 passed, workflow transcript 3/3 passed; merge commit SSH signature verified.

- 2026-10-11T08:55:27+00:00: Accepted exact-main postmerge evidence at
  d64ac90ad96a0941ddf6acb2d60ffe7b2ab5f948: clean worktree, signed merge, 235/235 asb-cli library
  tests, 3/3 source-builder tests, and 3/3 workflow-transcript tests.

- 2026-10-11T08:55:50+00:00: AR-1778 complete: PR #568 merged as
  d64ac90ad96a0941ddf6acb2d60ffe7b2ab5f948; exact-main postmerge clean, signed, and tests passed.
  Acceptance evidence recorded.
