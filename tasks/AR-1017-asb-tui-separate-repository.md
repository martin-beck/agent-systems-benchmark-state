---
{
  "branch": "feature/asb-tui-separate-repository",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-10T13:30:26+00:00",
  "depends_on": [
    "AR-0803",
    "AR-0804",
    "AR-0805",
    "AR-0806",
    "AR-0851"
  ],
  "id": "AR-1017",
  "next_action": "Implement and independently gate the assurance tests and public-repository baseline; publish only the reviewed immutable signed head, then verify visibility, settings, protections, and exact-head CI.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "contracts_20260906",
  "plan": "../plans/AR-1017.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Build asb-tui as an isolated optional repository and extension.",
  "task_revision": 43,
  "title": "Create the standalone asb-tui extension repository",
  "updated_at": "2026-09-10T10:42:24+00:00",
  "worktree_key": "agent-systems-benchmark-asb-tui-separate-repository"
}
---
Create a separate public asb-tui repository containing the optional terminal frontend only. Consume
the latest immutable releases of `martin-beck/agent-workflow-coordinator` and
`martin-beck/agent-workflow-quality`, recording exact tags/commits, artifact digests, signatures,
licenses, and compatibility in a lock manifest. Define a versioned, capability-negotiated CLI/JSON
protocol to the installed ASB program; do not share Cargo
workspace manifests, provider code, benchmark execution, or private coordination history.

Acceptance criteria: isolated repository and worktree, latest-release discovery that rejects mutable
or unsigned inputs, pinned coordinator/quality/Ratatui/Crossterm inputs, explicit
unverified-extension classification, protocol compatibility matrix, sanitized SBOM/license/provenance
metadata, and tests proving the main benchmark runs independently when the TUI is absent.

- 2026-09-10T08:55:59+00:00: Promote standalone asb-tui extension boundary after dependency
  preflight.

- 2026-09-10T08:57:32+00:00: Claimed by contracts_20260906.

- 2026-09-10T08:58:06+00:00: Recorded command exit 0; command argv SHA-256
  42a502c9a2ee9cf5bea7b8a16c82cd4845a0f513fde9cfb55f13095b40b120a4.

- 2026-09-10T08:58:20+00:00: Recorded command exit 0; command argv SHA-256
  b0ed9dcaecd924d95cf0a33d420a9fe950657c7e20599add0036d47e052af603.

- 2026-09-10T08:58:39+00:00: Recorded command exit 0; command argv SHA-256
  92dd972edd1a176a56751859e55d72e93598cd4098694b248effb76fa55a9631.

- 2026-09-10T08:58:53+00:00: Recorded command exit 0; command argv SHA-256
  b93e4b1ba3ebf72928cac6689e8562cc6c1e940c8a1759dc1b3e981716383910.

- 2026-09-10T08:59:24+00:00: Recorded command exit 0; command argv SHA-256
  039b3d941d87ac86cad296adfafbdc9796ba83101c5caaf4931819d9a8882cd1.

- 2026-09-10T08:59:39+00:00: Recorded command exit 0; command argv SHA-256
  32a88ae86cc5fbf7432fbe927dceb0991be96a2d887d97236eb13974b5a4f2ce.

- 2026-09-10T09:00:15+00:00: Recorded command exit 0; command argv SHA-256
  8263cda2fb83351a7edb6515297ece9ab9662d798e47289ddc1c507d64c188d2.

- 2026-09-10T09:00:30+00:00: Recorded command exit 0; command argv SHA-256
  ef982609348a8ad8faf8e30be27203612be964d8c882149e3c277bc3badf634d.

- 2026-09-10T09:00:44+00:00: Recorded command exit 0; command argv SHA-256
  40749e3991b223ead911d8e01cf832c92e28f2051609c742edf99f60e891754f.

- 2026-09-10T09:01:01+00:00: Recorded command exit 0; command argv SHA-256
  b660253513b6f1a7d329e6db0e7ee94ff4d6f90e47787e902b4a905fdfbd67f9.

- 2026-09-10T09:01:17+00:00: Recorded command exit 0; command argv SHA-256
  df08122c9f0ffc13e535e5b90e79ec634cbeb03bd8229cc98ab78a02678a01c8.

- 2026-09-10T09:01:33+00:00: Recorded command exit 0; command argv SHA-256
  09b5ebfd4677044848b7f66313a4fc3049cead1179f01044fa2f84f4e1c8a61e.

- 2026-09-10T09:01:49+00:00: Recorded command exit 0; command argv SHA-256
  bcd330af3d24dd224d6bc8afc73e1dd9e2e849a9b3054cf9e7bf44e80a3f8d2f.

- 2026-09-10T09:02:02+00:00: Recorded command exit 0; command argv SHA-256
  0d0e6a324b1df14543667b5d7cbcfe87e720cba4492e30367e40378558461177.

- 2026-09-10T09:02:22+00:00: Recorded command exit 0; command argv SHA-256
  12b49793e1aea457d66ae255f5fb905f39de3448c982ff569206380867b9c386.

- 2026-09-10T09:03:55+00:00: Recorded command exit 0; command argv SHA-256
  af44f955b3bb5ea94a585a4edb54fb4f496e8134f5b166b115d291c267f22083.

- 2026-09-10T09:04:21+00:00: Recorded command exit 0; command argv SHA-256
  f268d9008f582b67afa8d9632b4a0268a4826e525c5a3aac343cf9cb80370703.

- 2026-09-10T09:04:38+00:00: Recorded command exit 0; command argv SHA-256
  27688ce00f9f335cc2ec71e2b5ac933b49fa96256bc77f49ca3b24ffae4c1ca8.

- 2026-09-10T09:04:54+00:00: Recorded command exit 0; command argv SHA-256
  724a3a45f1b13e5fc518f8f430c9c32aeb167e469bb0f970bf5d88aa205d66a8.

- 2026-09-10T09:05:32+00:00: Immutable dependency discovery passed without mutable/vendor
  substitution. Latest coordinator release is v0.3.5 (published 2026-09-08), annotated tag object
  9e862e9e7af328e489b6e2fe958e5df1ddd702c1 -> commit 510817b93feb80dde13e5a6c61d657954fae2346/tree
  41d08ed42333cb47b07c2c401a9167b56c7cfb81; tag verifies with independently pinned ASB ED25519 key,
  source is dependency-free Python >=3.12 under MIT, LICENSE sha256 91863eae..., and fetched GitHub
  archive sha256 a51e58ed... is byte-tree-equal to the exact tag checkout. Coordinator publishes no
  separate assets/SBOM, so the lock must state source-archive-only provenance and may not imply
  binary/SBOM attestation. Latest AWQ release is v0.23.0 (published 2026-09-10), annotated tag
  object 79c699258111cc3ae4585d46c6ce4999784001b3 -> commit
  8a9f056b7fc7926b9465a0f7a09225d4da1c572a/tree ca77db478f0737142690d37683d826710cd953b0; tag and
  detached awq-release manifest signature verify with the same independent key. Manifest 05bbb0d4
  binds wheel 9d480cab, provenance a2ba5f30, SBOM 840e85a1, sdist 69b1c9c4; structural/source
  verification passes. AWQ is dependency-free Python >=3.12 MIT, LICENSE sha256 20647d25.... Both
  releases are acceptable with the explicit coordinator provenance limitation.

- 2026-09-10T09:05:42+00:00: Recorded command exit 1; command argv SHA-256
  274f9b56c94523cd52878e961dcc6ed51292b1d2f8dbccda8f40b542ada1b749.

- 2026-09-10T09:06:20+00:00: Recorded command exit 0; command argv SHA-256
  842c6b9775aa127c6d8dbec81788bc222b7e1f2ee452998be16382ab7b1196d5.

- 2026-09-10T09:06:36+00:00: Recorded command exit 0; command argv SHA-256
  7c3ee82bff650d0b22e81ef58084888c70c7e400a2afbe0c652320d98451506e.

- 2026-09-10T09:07:17+00:00: Recorded command exit 0; command argv SHA-256
  e798dbe413f79ee1119b2b7510424acc1fcb40125658db899ab8ef1cfc85cefb.

- 2026-09-10T09:13:11+00:00: Recorded command exit 0; command argv SHA-256
  d06d8588b3b9db3a8bc5a4e94829e379eb8cdf9711e03a691036e27c1f0ffb6b.

- 2026-09-10T09:13:28+00:00: Recorded command exit 0; command argv SHA-256
  652a7b522f9a73664208c7244d628dd6a070130fb82e54a0c26fe2b27e617c74.

- 2026-09-10T09:13:46+00:00: Recorded command exit 0; command argv SHA-256
  9790ca5e68bb3103a718dddce7c32be359f82fd78a17b9929531724d920a000f.

- 2026-09-10T09:14:40+00:00: Recorded command exit 0; command argv SHA-256
  9790ca5e68bb3103a718dddce7c32be359f82fd78a17b9929531724d920a000f.

- 2026-09-10T09:14:56+00:00: Recorded command exit 0; command argv SHA-256
  6f92160db9aa76ac8099bd40b740c8ecbb7db38d4afc5ebdbccc1bfffaa731cc.

- 2026-09-10T09:15:14+00:00: Recorded command exit 0; command argv SHA-256
  652a7b522f9a73664208c7244d628dd6a070130fb82e54a0c26fe2b27e617c74.

- 2026-09-10T09:15:31+00:00: Recorded command exit 0; command argv SHA-256
  473c4970766160bcdfdf7d92300e1228abe54fb8eb6c50f2fb3e026b52997144.

- 2026-09-10T09:15:46+00:00: Recorded command exit 128; command argv SHA-256
  9b58144c5731a9998bcb74550df96045f7f59e81342d08b6779e54a89e2ce67b.

- 2026-09-10T09:16:21+00:00: Recorded command exit 0; command argv SHA-256
  8f93f3d7bb9137620c4211d371e239cb50408b9ea59285b1fd90565d139a725e.

- 2026-09-10T09:16:36+00:00: Recorded command exit 0; command argv SHA-256
  4665c7e4710433e0a6ac72ee8d8faa0c2986888e77b4730ed41a233f995803b4.

- 2026-09-10T09:17:36+00:00: Standalone local repository boundary created at
  /srv/data/projects/agent-systems-benchmark-asb-tui-separate-repository on declared branch. Root
  candidate 42d540d96709e13bdf3796a2e45dd195c042d898/tree d4f34270f099402d9f76197a085cbe7b64449fd2
  is clean, SSH-signed by the independently pinned key, and has exact DCO. Eight paths establish an
  independent dependency-free Rust 1.93 crate, MIT license, explicit unverified-extension doctor
  JSON/exit 3, closed v1 capability schema, and immutable tooling lock for coordinator v0.3.5 plus
  AWQ v0.23.0. Rendering remains explicitly unavailable pending AR-1010; no Ratatui/Crossterm or ASB
  product dependency is claimed. Focused 3/3 tests, fmt and Clippy -D warnings pass. Initial cargo
  command failed only because handoffctl has no ambient cargo PATH; corrected commands use the exact
  1.93 toolchain. Initial commit signing attempted GPG due the new repository lacking local config;
  no commit was created, and the corrected command-scoped SSH signing produced 42d540d. No remote
  repository exists or was created.

- 2026-09-10T10:30:26+00:00: Heartbeat by contracts_20260906.

- 2026-09-10T10:31:15+00:00: Recorded command exit 0; command argv SHA-256
  8755eb8279d8421bcbb3e9b11dcfdbf54e16bf20ec4bdcc632723360c5eeef9b.

- 2026-09-10T10:38:56+00:00: Scope expanded by explicit authorization: after closed-schema
  negatives, ASB-core absence/isolation proof, authenticated immutable release-discovery tests, and
  all pre-publication gates pass, create the public martin-beck/asb-tui repository. Before
  publication require MIT licensing; exact Huawei Technologies Co., Ltd. 2026 copyright and SPDX
  headers on first-party sources; README, CONTRIBUTING.md, SECURITY.md; sanitized content and
  history; repository metadata; immutable pinned Actions; quality, privacy, and Gitleaks checks;
  applicable branch protections; and privacy-safe self-hosted CI labels/workflows that disclose no
  development-host identifiers or credentials. After publication verify public visibility, exact
  pushed signed+DCO head, settings/protections, and exact-head CI. Status-only worker output is not
  a substantive checkpoint.

- 2026-09-10T10:42:08+00:00: Recorded command exit 0; command argv SHA-256
  c373f0ced4a0f58d1f8f9efc56bdaec78cf7c91f6119b0da42ba61ef939d3efb.

- 2026-09-10T10:42:24+00:00: Recorded command exit 2; command argv SHA-256
  48458d4adcbc2714c4ae60f17ec39d916357031118af6e75d9a5cd826c73f20e.
