---
{
  "branch": "release/ar-1492-customer-bundle-signing-handoff",
  "checkpoint_commit": "a2d9be3eb3c77331a7a3498fdec8e54fb74ae8d6",
  "claim_expires": "2026-09-27T18:40:23+00:00",
  "depends_on": [
    "AR-1461",
    "AR-1462",
    "AR-1491"
  ],
  "id": "AR-1492",
  "next_action": "Classify Repository Quality run 36333580327 failure; rerun only if approved after confirming timing-flake, while Rust 36333580319 and AArch64 36333580303 remain in progress.",
  "observed_branch": "release/ar-1492-customer-bundle-signing-handoff",
  "observed_dirty": 0,
  "observed_head": "050b298c99724f7265e8dec47c6e801b3fb53e85",
  "owner": "ar1332-record-replay-luna56",
  "plan": "../plans/AR-1492-customer-bundle-signing-handoff.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Stage a deterministic customer bundle and provide an explicit external signing handoff and verifier.",
  "task_revision": 59,
  "title": "Customer bundle signing handoff",
  "updated_at": "2026-09-27T16:40:23+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1492-customer-bundle-signing-handoff"
}
---

AR-1490 is blocked on missing external release package and signing authority.
This bounded successor prepares everything that can be produced autonomously,
without fabricating a signature or claiming customer acceptance.

- Stage the exact deterministic runtime bundle input tree, manifest, checksums,
  SBOM, provenance, and verifier invocation from the pinned source.
- Emit a concise external-signing handoff specifying the expected SSHSIG
  namespace, principal, allowed-signers input, and post-signature validation.
- Keep all outputs credential-free and bounded; do not retain private paths or
  secret material and do not contact a provider.

The resulting staging artifact is not a release and cannot satisfy AR-1490
until an authorized external signer supplies and independently validates the
detached signature.

- 2026-09-27T16:13:21+00:00: Dependencies complete; prepare deterministic customer bundle staging
  and explicit external signing handoff without fabricating release authority.

- 2026-09-27T16:13:23+00:00: Claimed by ar1332-record-replay-luna56.

- 2026-09-27T16:13:26+00:00: Heartbeat by ar1332-record-replay-luna56.

- 2026-09-27T16:13:35+00:00: Recorded command exit 0; command argv SHA-256
  1be3df8ac8a124a6199760f3e1a120392451859acb9b8a94d858d5fd026f1c18.

- 2026-09-27T16:13:57+00:00: Recorded command exit 2; command argv SHA-256
  f246114e63922b80b23a8b6c53b5df63c9e3ff55bb234723023a02aa6e259d82.

- 2026-09-27T16:15:51+00:00: Recorded command exit 0; command argv SHA-256
  e501325c2f00e14e73d45ed23a843b3da31b59f73801b77c791316dc6a8bd116.

- 2026-09-27T16:16:08+00:00: Recorded command exit 1; command argv SHA-256
  606808e88963abca5725c993a1e1dff7625a0cdcf0b18d08476614e429169a15.

- 2026-09-27T16:16:24+00:00: Recorded command exit 0; command argv SHA-256
  ffa872787fcfd00e0b71a33dd9da711daac8d333fdc83efb7d1df7c0efdeb58c.

- 2026-09-27T16:17:11+00:00: Recorded command exit 0; command argv SHA-256
  972fcda574e08779fba36c338d13a11d0f55846c66db9737d83a247c321fe1de.

- 2026-09-27T16:17:32+00:00: Implemented prepare_signing_handoff.py: deterministic helper/LICENSE
  staging, signed-profile manifest/SBOM metadata, bounded handoff JSON with SSHSIG
  namespace/principal/ssh-keygen digest/verifier command, and no detached signature fabrication.
  Added positive/negative Python tests. Focused gates green: Python bundle tests 5/5, offline
  verifier 22/22, clippy workspace all-targets, rustdoc workspace, repository policy,
  fmt/diff/clean. Product head 1836d0f0 is SSH-signed+DCO.

- 2026-09-27T16:19:11+00:00: Recorded command exit 0; command argv SHA-256
  2dc75c71065c01bd6ae8b26b0898f48c3c4a43881e4ff64ae8d8a66daa40913b.

- 2026-09-27T16:19:34+00:00: Full gates passed at 1836d0f: Python bundle tests 5/5, offline verifier
  22/22, workspace clippy all-targets, serial cargo test workspace all-targets (green), rustdoc
  workspace, release build, repository policy, fmt/diff/clean. prepare_signing_handoff stages
  signed-profile metadata but intentionally emits no detached signature; handoff records external
  SSHSIG requirements and verifier command. No customer-release claim.

- 2026-09-27T16:19:56+00:00: Recorded command exit 0; command argv SHA-256
  cf86b6fc7867072c3ef946b511b5bcf11a9af7b10d94f84dbe35ebfa76f7b1cb.

- 2026-09-27T16:20:21+00:00: Independent review passed: three-file release-tooling/docs/test diff;
  reuses existing deterministic builder primitives, refuses existing output/bad helpers, emits no
  signature or private path, and preserves signed verifier/customer-release gate. Published PR #371
  from exact SSH-signed+DCO head 1836d0f0bff012a9941085f61cac6fdc1cfead64.

- 2026-09-27T16:20:35+00:00: Recorded command exit 0; command argv SHA-256
  7ea0d13c9417ccae5efd80f809914c8b60a39553bd48f033de3896fce4750f4f.

- 2026-09-27T16:21:04+00:00: Recorded command exit 0; command argv SHA-256
  0d69e785961d4380ac458ee061c526456852c859814b873b20779605c2595940.

- 2026-09-27T16:21:31+00:00: Recorded command exit 0; command argv SHA-256
  569376868c7964eba4cbd4d73a86896a7e7664076d13fb11eaaadb794ed5c01d.

- 2026-09-27T16:21:57+00:00: Recorded command exit 0; command argv SHA-256
  b4e7d83f347295781a7a8fc5edb4e5c4ef944ad210da005f850eebb8ddac4a53.

- 2026-09-27T16:22:34+00:00: PR #371 initial head 1836d0f failed Platform evidence 36332843012 with
  source identity not immutable and Repository Quality 36332843017 because topic was based on stale
  b048fef instead of protected main 5f4e286. Repaired by fetching origin/main and creating signed
  non-squash merge commit 050b298, preserving the reviewed implementation tree; force-with-lease
  updated the branch. Re-run exact-head checks; no product semantics changed.

- 2026-09-27T16:22:53+00:00: Recorded command exit 0; command argv SHA-256
  7ea0d13c9417ccae5efd80f809914c8b60a39553bd48f033de3896fce4750f4f.

- 2026-09-27T16:23:54+00:00: Recorded command exit 0; command argv SHA-256
  b2a3f375b68618e2dfb0edaab69c2b4577afbac8afeba3e74b3334c555414237.

- 2026-09-27T16:24:45+00:00: Recorded command exit 0; command argv SHA-256
  b2a3f375b68618e2dfb0edaab69c2b4577afbac8afeba3e74b3334c555414237.

- 2026-09-27T16:25:03+00:00: Recorded command exit 0; command argv SHA-256
  b2a3f375b68618e2dfb0edaab69c2b4577afbac8afeba3e74b3334c555414237.

- 2026-09-27T16:25:44+00:00: Recorded command exit 0; command argv SHA-256
  b2a3f375b68618e2dfb0edaab69c2b4577afbac8afeba3e74b3334c555414237.

- 2026-09-27T16:26:00+00:00: Recorded command exit 0; command argv SHA-256
  b2a3f375b68618e2dfb0edaab69c2b4577afbac8afeba3e74b3334c555414237.

- 2026-09-27T16:26:40+00:00: Recorded command exit 0; command argv SHA-256
  b2a3f375b68618e2dfb0edaab69c2b4577afbac8afeba3e74b3334c555414237.

- 2026-09-27T16:27:01+00:00: Recorded command exit 0; command argv SHA-256
  b2a3f375b68618e2dfb0edaab69c2b4577afbac8afeba3e74b3334c555414237.

- 2026-09-27T16:27:37+00:00: Recorded command exit 0; command argv SHA-256
  b2a3f375b68618e2dfb0edaab69c2b4577afbac8afeba3e74b3334c555414237.

- 2026-09-27T16:27:57+00:00: Recorded command exit 0; command argv SHA-256
  b2a3f375b68618e2dfb0edaab69c2b4577afbac8afeba3e74b3334c555414237.

- 2026-09-27T16:28:48+00:00: Recorded command exit 0; command argv SHA-256
  b2a3f375b68618e2dfb0edaab69c2b4577afbac8afeba3e74b3334c555414237.

- 2026-09-27T16:29:05+00:00: Recorded command exit 0; command argv SHA-256
  b2a3f375b68618e2dfb0edaab69c2b4577afbac8afeba3e74b3334c555414237.

- 2026-09-27T16:29:47+00:00: Recorded command exit 0; command argv SHA-256
  b2a3f375b68618e2dfb0edaab69c2b4577afbac8afeba3e74b3334c555414237.

- 2026-09-27T16:30:05+00:00: Recorded command exit 0; command argv SHA-256
  b2a3f375b68618e2dfb0edaab69c2b4577afbac8afeba3e74b3334c555414237.

- 2026-09-27T16:30:23+00:00: Heartbeat by ar1332-record-replay-luna56.

- 2026-09-27T16:31:12+00:00: Recorded command exit 0; command argv SHA-256
  b2a3f375b68618e2dfb0edaab69c2b4577afbac8afeba3e74b3334c555414237.

- 2026-09-27T16:31:30+00:00: Recorded command exit 0; command argv SHA-256
  b2a3f375b68618e2dfb0edaab69c2b4577afbac8afeba3e74b3334c555414237.

- 2026-09-27T16:31:49+00:00: Recorded command exit 0; command argv SHA-256
  359e32b9c9409463ad91e16212ec517683c55fec9fcfd09d5ba1f51ce7ba2dc7.

- 2026-09-27T16:32:12+00:00: Recorded command exit 0; command argv SHA-256
  8a616e50dd73778f41c21c04bf2989cd68b252dc8916ac97341bd0bb77b82890.

- 2026-09-27T16:33:15+00:00: Recorded command exit 0; command argv SHA-256
  8a616e50dd73778f41c21c04bf2989cd68b252dc8916ac97341bd0bb77b82890.

- 2026-09-27T16:33:32+00:00: Recorded command exit 0; command argv SHA-256
  8a616e50dd73778f41c21c04bf2989cd68b252dc8916ac97341bd0bb77b82890.

- 2026-09-27T16:34:16+00:00: Recorded command exit 0; command argv SHA-256
  8a616e50dd73778f41c21c04bf2989cd68b252dc8916ac97341bd0bb77b82890.

- 2026-09-27T16:34:33+00:00: Recorded command exit 0; command argv SHA-256
  8a616e50dd73778f41c21c04bf2989cd68b252dc8916ac97341bd0bb77b82890.

- 2026-09-27T16:35:14+00:00: Recorded command exit 0; command argv SHA-256
  8a616e50dd73778f41c21c04bf2989cd68b252dc8916ac97341bd0bb77b82890.

- 2026-09-27T16:35:34+00:00: Recorded command exit 0; command argv SHA-256
  8a616e50dd73778f41c21c04bf2989cd68b252dc8916ac97341bd0bb77b82890.

- 2026-09-27T16:36:16+00:00: Recorded command exit 0; command argv SHA-256
  8a616e50dd73778f41c21c04bf2989cd68b252dc8916ac97341bd0bb77b82890.

- 2026-09-27T16:36:33+00:00: Recorded command exit 0; command argv SHA-256
  8a616e50dd73778f41c21c04bf2989cd68b252dc8916ac97341bd0bb77b82890.

- 2026-09-27T16:37:14+00:00: Recorded command exit 0; command argv SHA-256
  8a616e50dd73778f41c21c04bf2989cd68b252dc8916ac97341bd0bb77b82890.

- 2026-09-27T16:37:39+00:00: Recorded command exit 0; command argv SHA-256
  8a616e50dd73778f41c21c04bf2989cd68b252dc8916ac97341bd0bb77b82890.

- 2026-09-27T16:38:38+00:00: Recorded command exit 0; command argv SHA-256
  246e218d4f0eef61a33b81ef1db24c3247fb29746a4a807d151f834335d23ca6.

- 2026-09-27T16:39:02+00:00: Heartbeat by ar1332-record-replay-luna56.

- 2026-09-27T16:39:25+00:00: Post-merge Repository Quality 36333580327 failed only because existing
  control::tests::strict_replay_requires_a_cassette_path_and_expired_deadline_fails_closed exceeded
  its test wall-clock assertion (started.elapsed() < 750ms) under llvm-cov; 120 passed, 1 failed.
  This is an existing timing-sensitive test, not a bundle/signing assertion. Preserve immutable
  failure; classify with isolated serial reproduction before any retry. Rust and AArch64 remain
  active; other six workflows are terminal SUCCESS.

- 2026-09-27T16:39:35+00:00: Recorded command exit 0; command argv SHA-256
  df755fa4914630a24cb2c47b1572fa371c6450ce9026e803d07053879d61307d.

- 2026-09-27T16:39:56+00:00: Recorded command exit 0; command argv SHA-256
  8a616e50dd73778f41c21c04bf2989cd68b252dc8916ac97341bd0bb77b82890.

- 2026-09-27T16:40:23+00:00: Heartbeat by ar1332-record-replay-luna56.
