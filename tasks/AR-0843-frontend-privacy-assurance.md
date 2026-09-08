---
{
  "branch": "feature/frontend-privacy-assurance",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-08T11:21:28+00:00",
  "depends_on": [
    "AR-0840",
    "AR-0841"
  ],
  "id": "AR-0843",
  "next_action": "Replace path-based artifact metadata reads with component-wise no-follow directory-relative opens rooted at the configured result store; prove symlinked ancestor rejection and regular artifact success, then run focused privacy/fault tests.",
  "observed_branch": "feature/frontend-privacy-assurance",
  "observed_dirty": 1,
  "observed_head": "ba97a20f60f39b4c5ef601a7dade148276a631d6",
  "owner": "quality_20260906",
  "plan": "../plans/AR-0843.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Qualify frontend privacy, artifact access, and fault behavior.",
  "task_revision": 27,
  "title": "Assure frontend privacy and faults",
  "updated_at": "2026-09-08T08:45:20+00:00",
  "worktree_key": "agent-systems-benchmark-frontend-privacy-assurance"
}
---
## AR-0843

Separate public summaries from sensitive artifacts and enforce least-privilege access. Test malformed,
stale, duplicate, oversized, slow-client, disconnect, restart, authorization, compatibility, and
redaction failures; prove no credentials, prompts, transcripts, or private paths reach the default API.

- 2026-09-08T08:21:26+00:00: Promoted as the highest-priority dependency-ready safe leaf after
  AR-0842 release. AR-0840 and AR-0841 are done; the prior frontend lifecycle owner is idle; no
  branch, worktree, process, lease or active AR path overlap was found. AR-0837 was not promoted
  because required AR-0836 remains blocked.

- 2026-09-08T08:21:28+00:00: Claimed by quality_20260906.

- 2026-09-08T08:24:04+00:00: Recorded command exit 0; command argv SHA-256
  7fcc7feafce793ed694f89c1ed7932f34dc94e2903faf74975d0c5c554f2dcf9.

- 2026-09-08T08:24:37+00:00: Recorded command exit 0; command argv SHA-256
  a5946df944e123ef7a8fd7055e4af5e7601678b34d2212eb3ff654582c8805b6.

- 2026-09-08T08:26:05+00:00: Recorded command exit 0; command argv SHA-256
  b0455f0d0ab4ae18675447dcecda3aadb4f9e50dc617cd0d62dbbdf051523d9b.

- 2026-09-08T08:27:41+00:00: Recorded command exit 0; command argv SHA-256
  7c6ec2aa750ca2f19a393a93d47d022d53e309470b37ae84a4aff8d2884745af.

- 2026-09-08T08:28:03+00:00: Recorded command exit 0; command argv SHA-256
  22bae6d640a283a13ea67682daa3610a66fd16b7bdb4c5901a4f509342485fb9.

- 2026-09-08T08:28:48+00:00: Substantive checkpoint: assigned worktree is clean at
  ba97a20f60f39b4c5ef601a7dade148276a631d6. Required DEVELOPMENT/ARCHITECTURE/QUALITY docs plus
  complete AR/plan were read. Wrapped baseline command completed exit 0: cargo test -p asb-control
  --locked and cargo test -p asb-cli control::tests:: --locked. Wrapped source audit completed exit
  0 and confirmed default API exposes only bounded public summaries plus metadata-only sensitive
  artifact results. Concrete residual under test: RunnerBackend artifact_metadata hashes a
  digest-named regular file but does not visibly bind it to authoritative run evidence and checks
  only final-component symlink metadata; next action is adversarial forged/unbound and
  ancestor-symlink tests before the narrowest behavior repair. No product paths changed.

- 2026-09-08T08:29:12+00:00: Recorded command exit 0; command argv SHA-256
  06f9416cba02c50a91557cdafcddcb3711e5a48454c0e10bbc73a1e00a601d5c.

- 2026-09-08T08:32:49+00:00: Recorded command exit 1; command argv SHA-256
  3c8e85a83c5835d84fb596ff3c9b958e002d65acd897e06f4ae3de97fb6feeba.

- 2026-09-08T08:34:36+00:00: Classified 2026-09-08T08:32:49Z exit 1 as harness-only patch transport
  failure: apply_patch rejected argv because its first argument did not begin with the literal patch
  header. No product mutation occurred; AR-0843 worktree remains clean at
  ba97a20f60f39b4c5ef601a7dade148276a631d6. Corrective action is a distinct verified single-argument
  invocation, not repetition of the malformed argv.

- 2026-09-08T08:36:16+00:00: Recorded command exit 0; command argv SHA-256
  234b16f38540214b4b1c105c91d8101ed224bb9ce28d3912ec5cbdb441ebfb1a.

- 2026-09-08T08:36:45+00:00: Recorded command exit 0; command argv SHA-256
  d48b89eecb0b252ddaca7f6e506bd3b305e8ca11a30f155d6a364f8f7a3f21f3.

- 2026-09-08T08:37:11+00:00: Recorded command exit 1; command argv SHA-256
  09e005d85b96cc89ee5964df2bbceddee9ff36a3292f372e56de7382c64f0993.

- 2026-09-08T08:37:37+00:00: Recorded command exit 101; command argv SHA-256
  83c8dd43d821a391895fdd1a15124c609aa10fed05dc1ffefc4a20d2e854c793.

- 2026-09-08T08:38:10+00:00: Adversarial pre-repair evidence captured. The single test
  artifact_metadata_rejects_symlinked_artifact_ancestor executed under cargo test -p asb-cli
  --locked and failed as intended: backend returned metadata for a digest-correct 16-byte file
  reached through a symlinked artifacts directory, instead of Err(Rejected). This harness records
  before that were non-product: filter/argv mistakes (one zero-test exit 0 and one Cargo usage exit
  1); neither executed the oracle or mutated product behavior. Current dirty scope is one added test
  in crates/asb-cli/src/control.rs. Narrow repair is a result-root dirfd plus component-wise
  O_DIRECTORY/O_NOFOLLOW opens and final O_NOFOLLOW regular-file hashing; no artifact content will
  cross the control boundary.

- 2026-09-08T08:39:36+00:00: Recorded command exit 0; command argv SHA-256
  10afc112a6f0ce31d3ae8b05dbe6e8e7aa28a9d28207efa757a9916a7dbefd93.

- 2026-09-08T08:39:52+00:00: Recorded command exit 1; command argv SHA-256
  cdce6727d1264577d2ea2c17115792cdbfe203347757b18055ef0def7c50c79e.

- 2026-09-08T08:40:19+00:00: Recorded command exit 127; command argv SHA-256
  8f12d7b1d9666215239a492764d938e841316e6cb472a28871ff512922238aac.

- 2026-09-08T08:41:01+00:00: Recorded command exit 0; command argv SHA-256
  878886d70570a9910b0ca96a103cfedb54019c6165833c55b9fa5eab06e17db1.

- 2026-09-08T08:42:35+00:00: Recorded command exit 1; command argv SHA-256
  64f7aa5c81c6d63b5aeac412b5a96f9f9f7c221da0fa82e9fb2925e42373bdf8.

- 2026-09-08T08:43:30+00:00: Recorded command exit 0; command argv SHA-256
  7bc91623af295714f77cbf0f6552526652b3438e66882a1279972a8a945a0bc6.

- 2026-09-08T08:44:37+00:00: Recorded command exit 0; command argv SHA-256
  6c44983c36f140cf83135f11f0958f567b931cfeb0a514582403fa0405d37f3e.

- 2026-09-08T08:45:20+00:00: Recorded command exit 0; command argv SHA-256
  8435aef409a5d6472f00639295cbb150dcdd6fb887aef6255b4e5ee90c31e790.
