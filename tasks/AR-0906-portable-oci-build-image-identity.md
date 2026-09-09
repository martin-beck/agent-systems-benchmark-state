---
{
  "branch": "fix/formal-oci-image-identity",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-09T17:36:00+00:00",
  "depends_on": [
    "AR-0003",
    "AR-0878",
    "AR-0901",
    "AR-0902"
  ],
  "id": "AR-0906",
  "next_action": "Hold PR #121 unchanged; AR-0877 must repair hosted curl exit-63 acquisition cap, then rerun exact-head CI.",
  "observed_branch": "fix/formal-oci-image-identity",
  "observed_dirty": 0,
  "observed_head": "156f7e011867956cb3bfaf5f511d65340f1b840e",
  "owner": "quality_20260906",
  "plan": "../plans/AR-0906.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Make deterministic formal source builds verify OCI image identity portably across Docker engines.",
  "task_revision": 36,
  "title": "Verify formal OCI build identity portably",
  "updated_at": "2026-09-09T16:10:22+00:00",
  "worktree_key": "agent-systems-benchmark-formal-oci-image-identity"
}
---
## AR-0906

Repair the Docker image identity boundary exposed by hosted formal CI without weakening the exact
AR-0878 source-build provenance. Verify the immutable repository digest and platform independently
instead of assuming an engine's local configuration ID equals the registry manifest digest.

- 2026-09-09T14:35:26+00:00: Dependencies AR-0003, AR-0878, AR-0901 and AR-0902 are done; the
  six-path OCI verifier fence is disjoint from active AR-0877 and AR-0704 work.

- 2026-09-09T14:36:00+00:00: Claimed by quality_20260906.

- 2026-09-09T14:36:27+00:00: Recorded command exit 0; command argv SHA-256
  cdcd326ab164f572ec8097b3acfae0b1487ac6fcd2490f76eaff129bd3f80646.

- 2026-09-09T14:41:12+00:00: Recorded command exit 2; command argv SHA-256
  9bdfb50edf62a5f583f5dfd9b9303eeb8aec5fd1bd4898891922e71db68dbb56.

- 2026-09-09T14:46:45+00:00: Recorded command exit 0; command argv SHA-256
  fd8cc47177c54ff0956e5de741ed1304bc7769bf6b41750ec8cc10f168717371.

- 2026-09-09T14:47:28+00:00: Recorded command exit 0; command argv SHA-256
  79ee00f5fb02a02c5f835f3fcb6d14de21cd6dc98153635aa06a22527555d128.

- 2026-09-09T14:47:54+00:00: Initial AR-0906 verifier checkpoint on exact product base b6d04a8.
  Dirty scope is exactly six owned paths: build.sh, new bounded verifier, positive/mutation
  fixtures, focused Rust test and public design note. Verifier distinguishes OCI config ID from
  repository digest; it requires a closed <=16384-byte JSON projection, exactly one pinned
  name-at-digest, linux/amd64, and redacts all failures. Focused test passes 3/3: two positive
  config-ID representations and all 20 unique declared mutations fail closed, plus static effect
  ordering. Real local Docker projection for the pinned digest passes. No AR-0877 PR path or AR-0704
  path changed.

- 2026-09-09T14:49:21+00:00: Recorded command exit 0; command argv SHA-256
  646877526d47d96c73301b82fcda376bc137edcdbe9113af9036ccdcfe794461.

- 2026-09-09T14:50:09+00:00: Bounded OCI verifier implemented in exact six-path AR-0906 scope on
  base b6d04a8. build.sh now projects config ID, repository digests, OS and architecture as bounded
  JSON; the closed verifier requires the sole exact name-at-digest and linux/amd64 while treating
  config ID as a separate well-formed value. Focused tests pass 3/3: matching and distinct config
  IDs both bind the exact repository digest; all 20 unique mutation fixtures fail with one redacted
  diagnostic; static ordering requires verification before any docker run effect. Bash syntax,
  ShellCheck and focused clippy pass. Real local Docker projection passes, and a full deterministic
  source build reproduced exact output SHA-256 8c200a88, 4512486 bytes. No AR-0877 or AR-0704 path
  changed.

- 2026-09-09T14:51:59+00:00: Recorded command exit 0; command argv SHA-256
  1049836bb4cc2ab94a0f499c32b8b6b6256ab85dd6f07c048aa123212693bc79.

- 2026-09-09T14:55:28+00:00: Recorded command exit 0; command argv SHA-256
  2ee76e3c9b3dec5d2d25a2209cb87dfea538cad2ae81e6610a7706a5c91d9b6d.

- 2026-09-09T14:56:00+00:00: Recorded command exit 0; command argv SHA-256
  586d40b6c5a0fcd828e5db0ec6df7f641e2dd0ce0fb64b81dbd1d5b7daf5493f.

- 2026-09-09T14:56:42+00:00: Recorded command exit 0; command argv SHA-256
  4c8a3187ad6a46478025a98d14a141b8c8894208f678ddea26e54dc05d1e2557.

- 2026-09-09T14:57:11+00:00: Recorded command exit 0; command argv SHA-256
  0ec0266aeecd98477938cf2c92460d6785b4a7d7fcc96c82f338fd4e7c4e8155.

- 2026-09-09T14:57:55+00:00: Signed immutable candidate 90caa78574f70a67646c2d6fc30d8744e955c250
  (tree ad17ba1a4a0a77aac0754abc52c1e5bd68dd2be2, parent b6d04a8305ce6d49cc327e4e6d2d6fa42a88050b)
  is clean and exactly six owned paths. SSH signature and DCO pass. Focused 3/3 plus 20 hostile
  mutations, real Docker projection, deterministic source build SHA-256 8c200a88/4512486 bytes, full
  formal/root fmt-clippy-workspace-doc-release, policy, headers, actionlint, zizmor, cargo
  deny/audit, coverage, failure paths, ShellCheck, exact-path Gitleaks, diff and privacy scans all
  pass. No AR-0877 PR or AR-0704 paths touched; unpublished pending independent review.

- 2026-09-09T15:05:20+00:00: Recorded command exit 0; command argv SHA-256
  95eb851390c78171ccf9dd5836368b399d3adc942350758d51c678bff8875355.

- 2026-09-09T15:05:47+00:00: Recorded command exit 127; command argv SHA-256
  0b641e5fe566f9a38290856d8168f6efdfe86f4fe7f740cddf104f4d94d655fc.

- 2026-09-09T15:06:35+00:00: Recorded command exit 0; command argv SHA-256
  7daab76bc1a5c160bafda31ae1abb69f14436bebfd4efc17e2379c7b5d5723cb.

- 2026-09-09T15:08:17+00:00: Recorded command exit 0; command argv SHA-256
  c0361c6c24eaf627f43c8757b93f70aeb2a765eacea38bc9ad5b44c6a93244c6.

- 2026-09-09T15:10:10+00:00: Recorded command exit 0; command argv SHA-256
  851f7b54431520599d6f075494be0cbf4ad5ca4f44c95298861f9d76c08c3b46.

- 2026-09-09T15:10:30+00:00: Recorded command exit 0; command argv SHA-256
  037648e4b9bdbf3fd97ed0ca322d25570b49e395f1271006de7f8b83529b2940.

- 2026-09-09T15:10:57+00:00: Recorded command exit 0; command argv SHA-256
  62470d7979da2a3d85dfb1a33eeb4d4fdfb77b0d71e39dae8499a3c78c2a3320.

- 2026-09-09T15:11:29+00:00: Review-block repair complete in replacement signed candidate
  156f7e011867956cb3bfaf5f511d65340f1b840e (tree 740616c7ec9806a4ec6f429aad7d7e90036a7987, exact
  parent b6d04a8305ce6d49cc327e4e6d2d6fa42a88050b). build.sh now direct-pipes inspect JSON to the
  16385-byte verifier under pipefail, suppresses raw inspect stderr, and emits bounded generic
  classification. Fake-Docker integration tests prove invalid/oversized/private-stderr projections
  exit 65 without a run marker and prove valid input reaches the exact offline license-check argv;
  focused suite 5/5. Full formal/workspace fmt, clippy, tests, docs, release, deterministic build
  SHA-256 8c200a88/4512486 bytes, actionlint, zizmor, policy, headers, deny, audit, coverage,
  failure paths, ShellCheck, Gitleaks and privacy pass. Earlier exit 127 was operator-only: unquoted
  RUSTDOCFLAGS split warnings into a command; corrected invocation passed. Clean exact six-path
  scope, SSH signature and DCO pass; unpublished.

- 2026-09-09T15:16:55+00:00: Approved candidate published unchanged as PR #121: exact base
  b6d04a8305ce6d49cc327e4e6d2d6fa42a88050b, head 156f7e011867956cb3bfaf5f511d65340f1b840e.
  Exact-head formal run 34368956147 job 102524900910 failed before AR-0906 execution:
  formal/run_temporal_models.sh curl exited 63 Maximum file size exceeded during TLA artifact
  acquisition. This is AR-0877-owned formal acquisition scope; AR-0877 is currently blocked and
  unowned at 55fdd686/PR #120, so coordinator must resume/claim it or create a successor to adjust
  the verified source-build/cache acquisition size boundary. PR #121 can rerun unchanged after that
  repair. Publication wrapper exit 1 was only the now-recovered unrelated AR-0704 expired-lease
  reconciliation. No merge attempted.

- 2026-09-09T16:05:20+00:00: Recorded command exit 0; command argv SHA-256
  3f8320328266c2fa6a97dc7825e7e3e97708b69f62997c976b62ae5f70557bbc.

- 2026-09-09T16:06:56+00:00: Recorded command exit 0; command argv SHA-256
  aa118061a4a8771d4e03c5300271cada99903a04987d0432d4b731a484c93fc7.

- 2026-09-09T16:09:03+00:00: Recorded command exit 1; command argv SHA-256
  9db1355ff9d6612743abe4978ddd8a766a58d56577182b104f7948f125c42687.

- 2026-09-09T16:09:33+00:00: Recorded command exit 0; command argv SHA-256
  a9f0120b5ae7881f434fc8113cf3faf3fe40ccb1b7da5e94bc58a92c780fd48b.

- 2026-09-09T16:09:50+00:00: Recorded command exit 0; command argv SHA-256
  f6c2f09ce7cc30e298094fbf60cee031a175a214c466a350515546d7a469972a.

- 2026-09-09T16:10:22+00:00: Recorded command exit 0; command argv SHA-256
  399f5268625320f6cf0d735167c220708e5d9e0e43e30091ae15bc76c4772c84.
