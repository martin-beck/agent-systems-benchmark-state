---
{
  "branch": "release/ar-1492-customer-bundle-signing-handoff",
  "checkpoint_commit": "1836d0f0bff012a9941085f61cac6fdc1cfead64",
  "claim_expires": "2026-09-27T18:13:26+00:00",
  "depends_on": [
    "AR-1461",
    "AR-1462",
    "AR-1491"
  ],
  "id": "AR-1492",
  "next_action": "Monitor PR #371 exact head 1836d0f; merge only after all required checks and independent review are green. Do not claim customer release without external signature.",
  "observed_branch": "release/ar-1492-customer-bundle-signing-handoff",
  "observed_dirty": 0,
  "observed_head": "050b298c99724f7265e8dec47c6e801b3fb53e85",
  "owner": "ar1332-record-replay-luna56",
  "plan": "../plans/AR-1492-customer-bundle-signing-handoff.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Stage a deterministic customer bundle and provide an explicit external signing handoff and verifier.",
  "task_revision": 23,
  "title": "Customer bundle signing handoff",
  "updated_at": "2026-09-27T16:21:57+00:00",
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
