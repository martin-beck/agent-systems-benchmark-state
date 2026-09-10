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
  "next_action": "Add a focused signed+DCO successor that runs full exact-main validation on the trusted self-hosted label for main push/manual only, while keeping all pull-request code exclusively GitHub-hosted; independently rerun all pre-publication gates before publication.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "contracts_20260906",
  "plan": "../plans/AR-1017.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Build asb-tui as an isolated optional repository and extension.",
  "task_revision": 107,
  "title": "Create the standalone asb-tui extension repository",
  "updated_at": "2026-09-10T11:30:45+00:00",
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

- 2026-09-10T10:47:17+00:00: Recorded command exit 0; command argv SHA-256
  57f44865a545036537e68510e6b56163749076d9cba0627f3769c3153a7706f2.

- 2026-09-10T10:47:35+00:00: Recorded command exit 0; command argv SHA-256
  e2a0f82bbc8a86c448adc7892f988f47b606f82b36fba19ebd45e366503b51d6.

- 2026-09-10T10:47:59+00:00: Recorded command exit 0; command argv SHA-256
  ee6aa53f05e959f3b35420333c4ea2f5432f587c59d5554f8e35dc481471ec25.

- 2026-09-10T10:48:18+00:00: Recorded command exit 0; command argv SHA-256
  dfbc2b644a67db8cfe6501f9bb74fe959fa4556910e04099e62c05c35657720a.

- 2026-09-10T10:48:38+00:00: Recorded command exit 0; command argv SHA-256
  a61ca78878bf5483b743a768321e3002efe547c261e37189cd5751a75a034db8.

- 2026-09-10T10:48:52+00:00: Recorded command exit 0; command argv SHA-256
  1af4d43d1274d3f92fda55e8cd1f584b95fbd1b0e772ace2c9dc2a0b87eac7b0.

- 2026-09-10T10:49:13+00:00: Recorded command exit 0; command argv SHA-256
  1a087504adde71a7c3ddb124209c15c387e8e44907d836a81b1f2de828bbcbfa.

- 2026-09-10T10:49:30+00:00: Recorded command exit 0; command argv SHA-256
  c31488fc3090b17f0c5f32379216c0c185d9603f934a80f5d99ff3071336505a.

- 2026-09-10T10:50:47+00:00: Recorded command exit 0; command argv SHA-256
  d41f11eead408cbcb241803687f6f4787656291ef4a28433c342870b96b1fc0e.

- 2026-09-10T10:51:04+00:00: Recorded command exit 1; command argv SHA-256
  ea1d8ad64c33ffd63df723dadad892e2bdb2fc2394b95ffb83004cceb54dc4ed.

- 2026-09-10T10:51:23+00:00: Recorded command exit 0; command argv SHA-256
  dfbc2b644a67db8cfe6501f9bb74fe959fa4556910e04099e62c05c35657720a.

- 2026-09-10T10:51:42+00:00: Recorded command exit 0; command argv SHA-256
  c4e4e5627c6c130a293c87108668ea8ac4a6948118fa44936b7749adfab21ae8.

- 2026-09-10T10:52:52+00:00: Recorded command exit 1; command argv SHA-256
  5d446b2fe028197a0fdd713590a686e364b37f60e1c069012b27ba6eb910a3b7.

- 2026-09-10T10:53:32+00:00: Recorded command exit 0; command argv SHA-256
  cd03d1a06b8194dd14fdfebd1ef98dd9dca4f567367b5844ec6404343875e18e.

- 2026-09-10T10:54:18+00:00: Recorded command exit 0; command argv SHA-256
  a3f42afd7289e7d7e25207e34d1b079aa13ac92f48b695ee3948a0d7da972f4e.

- 2026-09-10T10:56:19+00:00: Recorded command exit 0; command argv SHA-256
  dfbc2b644a67db8cfe6501f9bb74fe959fa4556910e04099e62c05c35657720a.

- 2026-09-10T10:56:38+00:00: Recorded command exit 0; command argv SHA-256
  a61ca78878bf5483b743a768321e3002efe547c261e37189cd5751a75a034db8.

- 2026-09-10T10:57:06+00:00: Recorded command exit 4; command argv SHA-256
  0aefcad993ba807408fb2bc1c832498df5cd125b9650a7a1a54fb3b14a65e681.

- 2026-09-10T10:57:44+00:00: Recorded command exit 0; command argv SHA-256
  23f6ef7d4e78c8a6f6bb7005b8f5e228200f160d78f40f08a3a03777564f94a5.

- 2026-09-10T11:00:42+00:00: Recorded command exit 127; command argv SHA-256
  122ad4c41893b9f909248e56abecb4146a64574c717e820a8612e68a8a39c808.

- 2026-09-10T11:01:03+00:00: Recorded command exit 0; command argv SHA-256
  8e234fc8d5598419c3ca804e9f43198a7f3284926f017193931224b0cd3d2278.

- 2026-09-10T11:01:48+00:00: Substantive implementation checkpoint: standalone crate now has strict
  serde deny_unknown_fields capability parsing with
  wrong/missing/unknown/duplicate/trailing/type/version negatives; 12 Rust tests pass. Authenticated
  release verification binds the pinned signer fingerprint, detached lock signature, signed
  annotated tag objects, commits and trees; unsigned, substituted-signer, mutable-tag and
  tampered-identity cases fail closed, and the exact coordinator v0.3.5/AWQ v0.23.0 local tag check
  passes. Executable isolation proof confirms asb-core dependency tree excludes standalone asb-tui
  and 16 unit plus 2 doctests pass. SPDX inventory is Cargo.lock-closed; MIT/security/contribution
  docs, pinned checkout Action, hosted quality/Gitleaks and checkout-free manual exact-label runner
  canary are prepared. One combined gate exited after tests because sanitized PATH omitted
  actionlint; absolute pinned actionlint rerun passed. cargo-deny initially rejected all licenses
  because deny.toml was absent; explicit narrow OSI license/source policy fixed it and cargo-deny
  plus cargo-audit now pass. An accidental wrapped env-only diagnostic had no product effect.

- 2026-09-10T11:02:34+00:00: Recorded command exit 127; command argv SHA-256
  1ed6d37086174c69529c38933227dbf1abcae6a4c00a0fdbce7296e735b97af3.

- 2026-09-10T11:02:52+00:00: Recorded command exit 0; command argv SHA-256
  35ea15799f89420f2d5c7571a50b3aa4820794898494467bb090a7197c2210e1.

- 2026-09-10T11:03:18+00:00: Recorded command exit 0; command argv SHA-256
  8c2bf6349d59901e05d3fdc0e27e974b610cdd5fb54a1f12e5bfa75b498598cd.

- 2026-09-10T11:04:13+00:00: Recorded command exit 13; command argv SHA-256
  71dc7f60ed179b6bc1641d7781ff20e2eb9b65a72db6d124f6bec2cd1cfc5049.

- 2026-09-10T11:04:49+00:00: Recorded command exit 0; command argv SHA-256
  151ea45e04f1a994f6545ce7d950aa79e09b96316113c1c5aeb8d992549fc8ec.

- 2026-09-10T11:05:12+00:00: Recorded command exit 0; command argv SHA-256
  5bbefabcdf77dac86279738f5765c30e5570a93983ed4b7c7c49c2552e7f35cb.

- 2026-09-10T11:06:24+00:00: Recorded command exit 0; command argv SHA-256
  91bf341ef98a21cba440f52a7a12988a70b2f460786bcbc969c4520f696fc6a6.

- 2026-09-10T11:06:49+00:00: Recorded command exit 1; command argv SHA-256
  3494c0222f4e0ae200c1cdad1464e497dced0f44d40792360fb76cb6abab6b30.

- 2026-09-10T11:10:03+00:00: Recorded command exit 0; command argv SHA-256
  c5e7179b85ffc0b84b855800e65ba038e2965d34aeccc6cc28f01624ef252458.

- 2026-09-10T11:10:23+00:00: Recorded command exit 0; command argv SHA-256
  3494c0222f4e0ae200c1cdad1464e497dced0f44d40792360fb76cb6abab6b30.

- 2026-09-10T11:11:13+00:00: Recorded command exit 0; command argv SHA-256
  3d6d9c88226ed15796f18e808f4a00b4411f31642b8e97bff2ff5aec08b6c171.

- 2026-09-10T11:11:34+00:00: Recorded command exit 1; command argv SHA-256
  a179671011fb70e06989b3a6b0f5bcb9c265b80c336427c9bfad02a66c99aae6.

- 2026-09-10T11:11:53+00:00: Recorded command exit 0; command argv SHA-256
  5062447c046627472f22aae89b4f3c88cb5a83ca8508ced20a70170f84c74d31.

- 2026-09-10T11:12:11+00:00: Recorded command exit 0; command argv SHA-256
  e85dfa81077329aabd172b5a6f68a96ddee964e03b881533720e578ae374d7c0.

- 2026-09-10T11:12:58+00:00: Recorded command exit 0; command argv SHA-256
  7001619f3b3a0e7ef99663832c02e07ec9084aada1131d65ce0c2dc1ed7da09e.

- 2026-09-10T11:13:16+00:00: Recorded command exit 126; command argv SHA-256
  76fffc88a1c618b120942727e0015c47d27d73c76dac8101ad842fc11b0b97b3.

- 2026-09-10T11:13:56+00:00: Recorded command exit 2; command argv SHA-256
  091246442a7f9f977bc7adbaceb73731df6e409857a1897a8e54f893ff1d26db.

- 2026-09-10T11:14:13+00:00: Recorded command exit 0; command argv SHA-256
  ebcd3c8460c4acd53d1e6dec8883e111bc67934a4f13ef975693865bfc4d83b1.

- 2026-09-10T11:14:34+00:00: Recorded command exit 0; command argv SHA-256
  dd8ddfbf3f4e0c784336d794961569396360216b4a768a6055b5f237b4da9b62.

- 2026-09-10T11:14:51+00:00: Recorded command exit 0; command argv SHA-256
  7156c8831ba2b17213319cf468aa52e34a27b822d17a93fe6261a0a0717850de.

- 2026-09-10T11:15:20+00:00: Recorded command exit 0; command argv SHA-256
  854cc2326a9cd5a0c9b83e1b65ac21d808b5daedf05ea101131c5d29fda9d868.

- 2026-09-10T11:16:04+00:00: Recorded command exit 0; command argv SHA-256
  8dfe5171173c6327b60bae499fee4f035f05bc9bd5ca92878c10a4bd9f2d79eb.

- 2026-09-10T11:17:00+00:00: Recorded command exit 0; command argv SHA-256
  df102f1c6167dc9c9a097139aa2c0efad78d7c7b3b8a4ca7927f6c97b0945fd0.

- 2026-09-10T11:17:58+00:00: Recorded command exit 0; command argv SHA-256
  3247c392b6b898abd8110dd6fe7810dadc917b44cc1fa7fc51ca589e607ae38a.

- 2026-09-10T11:18:28+00:00: Recorded command exit 0; command argv SHA-256
  4c634a31ef997054921e4bc9d0a932254ce9efc127831579796359b407420464.

- 2026-09-10T11:18:59+00:00: Recorded command exit 1; command argv SHA-256
  4946d58ff6ca0275ad9e95f4b2bc729dab3a122d8a939cba3cc406321cfa6135.

- 2026-09-10T11:19:27+00:00: Recorded command exit 1; command argv SHA-256
  26b50e0c40ded0053690f2579f5922d11cd1b7380c84c9f4c728b40ca4009339.

- 2026-09-10T11:19:35+00:00: Recorded command exit 0; command argv SHA-256
  f7d36ea27005d6c4bf392bbb043711488c3240cb8bfc430d6062d33691a82a9c.

- 2026-09-10T11:20:07+00:00: Pre-publication candidate complete:
  c6749880a16082c9d3ab3fe892d3e6083540f1ce, tree 56351344df5b934aea43751b8fa8a0fadc1c84c6, exact
  parent/root 42d540d96709e13bdf3796a2e45dd195c042d898, 23-path focused successor, clean tree and no
  remote. Both commits verify with the pinned ED25519 signer and exact DCO. Final Rust gate: 14
  tests plus doctests pass, fmt, Clippy -D warnings, rustdoc -D warnings, release build, cargo
  package, cargo-deny, cargo-audit green. Coverage is 92.57% lines (90.16% regions), above the 90%
  floor. Exact upstream tag/signature probe passes; hostile
  unsigned/substituted-signer/mutable/tampered cases fail closed. ASB isolation executes 16 asb-core
  tests plus 2 doctests and proves no standalone dependency. Actionlint and Zizmor (zero findings),
  digest-pinned ShellCheck/shfmt, Gitleaks, schema/JSON, privacy and diff checks pass. Earlier
  final-identity wrapper exit 1 was only a faulty tail-last-line DCO assertion against the commit
  message trailing blank; corrected exact-line grep, signatures, parent/tree/scope and clean-state
  check passed. No remote, GitHub repository, push, PR, or publication was created.

- 2026-09-10T11:21:43+00:00: Independent review found a required runner-policy gap in c674988: the
  self-hosted development-runner workflow is checkout-free canary only, while complete quality
  validation runs only on GitHub-hosted Ubuntu. Before publication add a trusted
  main-push/workflow_dispatch self-hosted job using privacy-safe label
  asb-development-v1-x86_64-ubuntu2404. It must check out and validate exactly github.sha/current
  main, fail closed on repository/ref/event/architecture mismatch, use immutable pinned Actions,
  persist no credentials, expose no host identifiers or credentials, and never run pull_request or
  other untrusted fork code. Preserve the GitHub-hosted pull_request quality path. After push,
  require and verify exact-head hosted quality and trusted local-runner validation in branch
  protection before release.

- 2026-09-10T11:25:18+00:00: Recorded command exit 0; command argv SHA-256
  f2030b8ca5f4292176817c2bd3af851115a9fc1513bd18b7790c4f5b45795dcc.

- 2026-09-10T11:25:38+00:00: Recorded command exit 0; command argv SHA-256
  1640f577b04404ec9fa21dd08e456aaab60704dfabfeec3ce85f85e7011fcd29.

- 2026-09-10T11:25:54+00:00: Recorded command exit 0; command argv SHA-256
  4fb834fc6743056e4a38e2000c722f701a77bf7022e870d028b9ed11750a0e7f.

- 2026-09-10T11:26:10+00:00: Recorded command exit 0; command argv SHA-256
  7156c8831ba2b17213319cf468aa52e34a27b822d17a93fe6261a0a0717850de.

- 2026-09-10T11:27:10+00:00: Recorded command exit 0; command argv SHA-256
  91bf341ef98a21cba440f52a7a12988a70b2f460786bcbc969c4520f696fc6a6.

- 2026-09-10T11:27:36+00:00: Recorded command exit 0; command argv SHA-256
  3494c0222f4e0ae200c1cdad1464e497dced0f44d40792360fb76cb6abab6b30.

- 2026-09-10T11:27:59+00:00: Recorded command exit 0; command argv SHA-256
  b5d22a565bf0774b551cae017a549047ac9221751b116086f849a8390df79550.

- 2026-09-10T11:29:05+00:00: Recorded command exit 0; command argv SHA-256
  f75ea21c76b72694079b09cdbde7f6e029f0f9ead945fc0e85ce660fae54d31d.

- 2026-09-10T11:29:27+00:00: Recorded command exit 0; command argv SHA-256
  3b69fe51f3256e4860f68082862246d0f7ab7bc67e24752d9e1ab7841f8f23fc.

- 2026-09-10T11:29:55+00:00: Recorded command exit 0; command argv SHA-256
  57ff4070ca52a92c393d07f5a1e5520e120e2714be502ab8e5dd065c9cde35be.

- 2026-09-10T11:30:15+00:00: Recorded command exit 0; command argv SHA-256
  3494c0222f4e0ae200c1cdad1464e497dced0f44d40792360fb76cb6abab6b30.

- 2026-09-10T11:30:45+00:00: Recorded command exit 1; command argv SHA-256
  016c63b74fc191199c0ba46a368c86685a697e28a2a1d990949c0bfc8372567e.
