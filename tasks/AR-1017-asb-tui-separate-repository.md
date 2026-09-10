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
  "next_action": "Publish reviewed signed head 0a726d4 unchanged as public martin-beck/asb-tui main; configure metadata, security, and required hosted plus trusted self-hosted exact-main checks; verify exact-head CI before release.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "contracts_20260906",
  "plan": "../plans/AR-1017.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Build asb-tui as an isolated optional repository and extension.",
  "task_revision": 222,
  "title": "Create the standalone asb-tui extension repository",
  "updated_at": "2026-09-10T12:25:07+00:00",
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

- 2026-09-10T11:33:06+00:00: Recorded command exit 0; command argv SHA-256
  b429917579e487e85889df0e08b6fe0567a481c8cb4d043bc9f61034277382fc.

- 2026-09-10T11:34:09+00:00: Recorded command exit 0; command argv SHA-256
  37c7c845aa1ec3f9a634625d924e83fa95fb2b2fffbaf0044ee35585a689da56.

- 2026-09-10T11:34:33+00:00: Recorded command exit 0; command argv SHA-256
  1046ee0ab78a4f71a02963e09d00df37a26aba2e4c23ada28133964065f2e4e1.

- 2026-09-10T11:35:04+00:00: Recorded command exit 0; command argv SHA-256
  9d339512fff96af5528ea6269babd342cb7fc4b939e9d96867f57e29dacd0d1a.

- 2026-09-10T11:35:26+00:00: Recorded command exit 0; command argv SHA-256
  69f6d482ffd51a1dc1b28c737c6c857a93f107dcf190b822d15cfdddb8ef3cd1.

- 2026-09-10T11:35:58+00:00: Trusted-main repair successor complete:
  963ccb0fd1062acac0a52ef64a76040c774cb350/tree ef9c1c966d60ccd05bfdb207eb4db4a28bb7d01b, exact
  parent c6749880a16082c9d3ab3fe892d3e6083540f1ce, clean exact six-path diff, no remote. SSH
  signature and exact DCO pass. The new persistent-runner workflow has only main push/manual
  triggers, repository/ref/event guards before checkout, SHA-pinned checkout without persisted
  credentials, exact checkout plus live origin/main equality, exact privacy-safe label, full
  Rust/supply/coverage/schema/provenance/shell/workflow/Gitleaks/privacy gates, and no PR or secrets
  context. Hostile executable tests reject PR, fork repository, feature ref, malformed SHA, stale
  checkout and stale remote main; hosted PR workflow remains ubuntu-24.04 only. All 17 Rust tests
  pass; coverage remains 92.57% lines/90.16% regions; fmt, Clippy, rustdoc, release, deny, audit,
  exact dependency authentication, 16+2 asb-core isolation, checksum-pinned
  ShellCheck/shfmt/actionlint/Zizmor zero findings, Gitleaks and privacy scans pass. Four transient
  LLVM profiles from the earlier pre-current-dir run were removed by exact path. The first final
  privacy run found only its own literal detector strings; equivalent split regexes removed the
  self-match and the rerun passed. A temporary state-recording blocker from expired AR-1010 was
  resolved at coordinator state 00526d2b before final evidence/commit.

- 2026-09-10T11:38:03+00:00: Recorded command exit 1; command argv SHA-256
  6eda4b42bc351469a94c5769a3ce440b7bc7595dd62b921a1b67c1a4dbd6fd68.

- 2026-09-10T11:38:40+00:00: Recorded command exit 0; command argv SHA-256
  98b7c6d70adecdc3f45bc8329ab3dfa6c3146fd439a085b71a6d42c84e35c2db.

- 2026-09-10T11:38:48+00:00: Recorded command exit 0; command argv SHA-256
  8d620784c11b0c0c2666d5a987f1662d162b98abc0113793f7fbf6328bfdef51.

- 2026-09-10T11:39:37+00:00: Independent causal review found deletion was not remediation: cargo
  llvm-cov instruments the env-cleared child in tests/isolation.rs; env_clear removes
  LLVM_PROFILE_FILE and no current_dir is set, so the child writes default_*.profraw into the
  checkout. Trusted-main would reproduce this, while git diff --exit-code ignores untracked files.
  Require a focused signed+DCO successor that runs the child in a unique safely cleaned temporary
  directory or equivalent, adds a regression proving coverage leaves the checkout clean, and updates
  hosted/trusted final gates to require both git diff --exit-code and an empty git status
  --porcelain. Publication remains prohibited pending fresh independent green gates.

- 2026-09-10T11:42:15+00:00: Recorded command exit 0; command argv SHA-256
  4eac93b62869bfa2f1156c7bdaeb0d58f8a868b4119a2e6f1556ebe27a4f231d.

- 2026-09-10T11:42:37+00:00: Recorded command exit 0; command argv SHA-256
  4929e76b0a02fc004fc6b9b599acf4292b9cae8f450c651b27d12c63c30525f0.

- 2026-09-10T11:43:12+00:00: Recorded command exit 0; command argv SHA-256
  57ff4070ca52a92c393d07f5a1e5520e120e2714be502ab8e5dd065c9cde35be.

- 2026-09-10T11:43:45+00:00: Recorded command exit 0; command argv SHA-256
  2dd05605d8d56c39643363ddef8304d6e837ff4442932e77deff750aedb89c36.

- 2026-09-10T11:44:10+00:00: Recorded command exit 0; command argv SHA-256
  644fec904ed2de5d25fe17ccbae937981d25a211656db884e625b3a14fa6d1ec.

- 2026-09-10T11:44:31+00:00: Recorded command exit 0; command argv SHA-256
  c30ecc6ebf963afb3ca8f99e38d9f222fdf3f2ff4430180fc4b00948390f2841.

- 2026-09-10T11:44:50+00:00: Recorded command exit 1; command argv SHA-256
  482bef3c4a5553f1925d612b72fc070baa66c354bf3dc9ba6a23bb2da15a34c3.

- 2026-09-10T11:45:07+00:00: Recorded command exit 1; command argv SHA-256
  5d0e18051fa3367493b6bdf148e912f451d96b296b3f70312dd746cb98f94b7e.

- 2026-09-10T11:45:53+00:00: Recorded command exit 0; command argv SHA-256
  e1b244e6d4f42f9d186ad6f315164a3f760bd64dc797bee02771dabb5e6c6787.

- 2026-09-10T11:49:19+00:00: Recorded command exit 1; command argv SHA-256
  51e480cbf906f624a0d394fe1595626af34906340e666cbebcc42bf4ac653e3a.

- 2026-09-10T11:49:40+00:00: Recorded command exit 0; command argv SHA-256
  28b09a88dd74eff5351af68835eb790ec46b0799326e1edbdfa9c4a661b7340a.

- 2026-09-10T11:49:47+00:00: Recorded command exit 0; command argv SHA-256
  e1f73c31b1a7cc6f96afee873e8ecbe7d1ee54bcc6a759c7d68c15698febb6b5.

- 2026-09-10T11:49:55+00:00: Recorded command exit 0; command argv SHA-256
  2a19edfe2d0f44c0b3c7ee2c8f889fb547190fdd96a880b82df1e1d6b43055af.

- 2026-09-10T11:50:26+00:00: Recorded command exit 0; command argv SHA-256
  b9e7dcc52dc7aa67624f2ae6a1fd28115e559381e90fca819f8afd7898758b12.

- 2026-09-10T11:50:35+00:00: Recorded command exit 0; command argv SHA-256
  d383a3269c425516e52adcf230163ef8327d95597b4bf5c434deb100df0dcefc.

- 2026-09-10T11:50:44+00:00: Recorded command exit 0; command argv SHA-256
  39d26f0ba498184d56f4e58da3de04aa67394cfec8ce488938d162f41a51ab1d.

- 2026-09-10T11:50:54+00:00: Recorded command exit 0; command argv SHA-256
  8a229d6c626f5db30286f63d1e3b0ff7732cd50e18d93c187baac0a8d9163247.

- 2026-09-10T11:51:04+00:00: Recorded command exit 0; command argv SHA-256
  dec3425192831f4fd806ee2baa21710d8ef0c1c2e39c8ac16bb69d5229e7d0cd.

- 2026-09-10T11:51:23+00:00: Recorded command exit 1; command argv SHA-256
  dae694fb96619917e87c8eacded9583c2e4451b75379e9f718b28f0ea530a483.

- 2026-09-10T11:52:01+00:00: Recorded command exit 1; command argv SHA-256
  a75f6f62625a5d624622b62fe63aa8ef86f9a0ff73abea4ba9077b7ea0b5a1ea.

- 2026-09-10T11:52:19+00:00: Recorded command exit 0; command argv SHA-256
  423ecbe614c1d9dfba38a3cd942e1585fbea2d792ed021c7d653a5010721cbef.

- 2026-09-10T11:52:42+00:00: Recorded command exit 0; command argv SHA-256
  3b1c3c4ab2cc2d4fe14404afc3b64ca69bbf5d4f408c795e65d89305c9a7c574.

- 2026-09-10T11:53:01+00:00: Recorded command exit 0; command argv SHA-256
  223a10daeff8ae515521f49e4d861903e599fc99b4e96b688c716cf5a000731c.

- 2026-09-10T11:53:54+00:00: Recorded command exit 0; command argv SHA-256
  03e9d0cd3eb2869603f0e3f4ec25f8ebe733e931bb35702f6ae88d0a58ad36bc.

- 2026-09-10T11:54:03+00:00: Recorded command exit 0; command argv SHA-256
  ffe308041cbb928231475710e3bf55a88e42b1b198a9429364955481505b7d8f.

- 2026-09-10T11:54:11+00:00: Recorded command exit 0; command argv SHA-256
  c2fadb5078d0fad24233957c868fa93af1899fdc600ca0aeab7c50900d1d1aa8.

- 2026-09-10T11:54:20+00:00: Recorded command exit 0; command argv SHA-256
  e0fe5fda3c099f3eca7843706a3d6498ae3a5dd2c35ece0bec085ec0c3c80847.

- 2026-09-10T11:54:29+00:00: Recorded command exit 0; command argv SHA-256
  432e4987b8d8eb14d2c9cf454953c26e77ea2796fed0f7f0ee7fa975ee1007d7.

- 2026-09-10T11:54:37+00:00: Recorded command exit 0; command argv SHA-256
  bb8f0af6547c2a913ee3e36544abc4b76c29911af9ef2ac94fb3bfca50b0715a.

- 2026-09-10T11:54:45+00:00: Recorded command exit 0; command argv SHA-256
  24e7012548dab89afb8437e998863baf21da1eb99e1fab8e930690d1a1f80f75.

- 2026-09-10T11:54:53+00:00: Recorded command exit 127; command argv SHA-256
  2364657c6a747456b8ecf50a8306493c153eda5326c0016b71b1c1d2b3a71048.

- 2026-09-10T11:55:14+00:00: Recorded command exit 0; command argv SHA-256
  78e037b1bcb9e0ca17b384c5f7203a2cfe345e63ac0b28d3d7881fa3ec951b93.

- 2026-09-10T11:55:21+00:00: Recorded command exit 0; command argv SHA-256
  cffd2573b675c715127bdd910a9ca3ff1b4dd1d6ec900a0f8884e13fee6caab4.

- 2026-09-10T11:56:02+00:00: Recorded command exit 1; command argv SHA-256
  4c177b8b9fbe2a7ffb769f7a36b6f496bf64f81fff0c015c7be87832e1f41187.

- 2026-09-10T11:57:10+00:00: Coverage repair successor 0a726d4ab3f939ab21811608e952b6fc1249c22c
  (tree db1d64341d060d3b6f86dd868a11ea45a0899692, parent 28911d936b7bc4d70869f053bdf6f48aff4b6b94)
  is SSH-signed and exact-DCO, clean three-path scope: tests/doctor.rs, tests/isolation.rs,
  tests/support/mod.rs. Prior clean coverage at 28911d9 failed after 18/18 tests and left one
  default profraw; cause was doctor.rs child inheriting checkout cwd after env_clear. Successor uses
  shared collision-safe 0700 RAII temp cwd for every direct asb-tui child and asserts no checkout
  profile and cleanup. Corrected clean-tree llvm-cov passed 18/18 with 92.57% line and 90.16% region
  coverage; afterward git status porcelain empty and zero default profraw. Full fmt, Clippy -D
  warnings, tests, rustdoc -D warnings, release, cargo-deny, cargo-audit, shell/workflow quality
  including Zizmor, Gitleaks, JSON/provenance/SBOM, ASB-core absence proof (16 tests plus 2
  doctests), diff/privacy/scope gates passed. One isolation invocation exited 127 solely from
  omitted Cargo PATH; corrected exact invocation passed. Ready for independent immutable review; no
  remote or publication.

- 2026-09-10T11:58:41+00:00: Recorded command exit 0; command argv SHA-256
  892ded1136e1abef92424cd46a901d56e1efb3439304b2e2fcb260a3e2673c7b.

- 2026-09-10T11:59:21+00:00: Independent causal review passed immutable
  0a726d4ab3f939ab21811608e952b6fc1249c22c/tree db1d64341d060d3b6f86dd868a11ea45a0899692, exact
  parent 28911d9. Pinned allowed-signers SSH verification and exact DCO pass; scope is only
  tests/doctor.rs, tests/isolation.rs, tests/support/mod.rs. Every asb-tui child now runs in a
  unique mode-0700 RAII directory, including both env-cleared launch sites. A fresh clean-tree
  tools/run-coverage-clean.sh run passed all 18 tests at 92.57% lines/90.16% regions and ended with
  zero default_*.profraw plus empty git status --porcelain. The prior 28911d9 post-coverage
  untracked artifact failure is preserved as the negative detection evidence. Full earlier Rust,
  supply-chain, workflow, shell, release-authentication, privacy, Gitleaks, provenance and ASB-core
  isolation gates remain green. No remote or publication exists; current instruction explicitly
  prohibits publication.

- 2026-09-10T12:00:54+00:00: Publication explicitly resumed after causal coverage repair and
  independent pre-publication gates passed at signed+DCO head
  0a726d4ab3f939ab21811608e952b6fc1249c22c/tree db1d64341d060d3b6f86dd868a11ea45a0899692. AR-1017 is
  publication-in-progress. Preserve signed history without rewrite; verify GitHub authentication and
  repository nonexistence before creation, then record public URL, settings, rules/protection, exact
  pushed SHA, workflow run IDs, conclusions, and local-runner evidence.

- 2026-09-10T12:01:22+00:00: Recorded command exit 0; command argv SHA-256
  fdfe7bf22cc2f1a12e38adece1d554144b4d0dfb426f287c7a071567fd5869c9.

- 2026-09-10T12:02:32+00:00: Recorded command exit 0; command argv SHA-256
  7aded333062aeeaf4953dc0dc73dfac72f5eb3e05a1b52a2d9f8c70dd9a6ed6c.

- 2026-09-10T12:02:43+00:00: Recorded command exit 0; command argv SHA-256
  373ee7ac10dc66eb54ad2dfed8db449e71ff09f691e6da3ac9d010fc338cf6ca.

- 2026-09-10T12:02:53+00:00: Recorded command exit 0; command argv SHA-256
  99235c34df668cd18b7fe7eea67be7e6e329a90495b002022525002cfe428976.

- 2026-09-10T12:03:07+00:00: Recorded command exit 128; command argv SHA-256
  503be62de1e55273bb83db37b348fea5c26157efbb3b21e93d468152476f7eb7.

- 2026-09-10T12:03:36+00:00: Recorded command exit 0; command argv SHA-256
  f2649b06a50ff97469dccf06540e2116628dabfcf4528c310855def424e19286.

- 2026-09-10T12:03:44+00:00: Recorded command exit 0; command argv SHA-256
  c3a482af2f1244a6b61a16ccae347f81759e084e97915398fc22a093fa42ce49.

- 2026-09-10T12:03:53+00:00: Recorded command exit 0; command argv SHA-256
  503be62de1e55273bb83db37b348fea5c26157efbb3b21e93d468152476f7eb7.

- 2026-09-10T12:04:49+00:00: Recorded command exit 0; command argv SHA-256
  66ee70abc707cedab7a1b2f27220b9bd06122a8fccda4abdaa86e7776be0c02c.

- 2026-09-10T12:04:57+00:00: Recorded command exit 0; command argv SHA-256
  58d28997fc6f0459073a384149e69ea93590ee5e8d9a78a95481a8d8ee4d54d4.

- 2026-09-10T12:05:05+00:00: Recorded command exit 0; command argv SHA-256
  333ac515755a83868c28d6780db6bd8e132fb44cb265706aa7ff64f984fe889d.

- 2026-09-10T12:05:14+00:00: Recorded command exit 0; command argv SHA-256
  2b6f8863083094723b4c16b4a4e9a9114ec7284f14e96ea72f6d55826d40f895.

- 2026-09-10T12:05:22+00:00: Recorded command exit 0; command argv SHA-256
  53eaf2a0881e933f76de2e48698cc4c302248cfd750ff7fbd54555a8cb13df9e.

- 2026-09-10T12:05:46+00:00: Recorded command exit 0; command argv SHA-256
  674949589be9810afb882fc356340b6547c524ec6df7bef13cf7ac19ef5aa3ba.

- 2026-09-10T12:05:57+00:00: Recorded command exit 0; command argv SHA-256
  83a61c8bea5849de694548b7aed6a1f9d445c2acbea20fd5054d9d69ff625ecc.

- 2026-09-10T12:06:09+00:00: Recorded command exit 0; command argv SHA-256
  67315c6d6f773e15a2e4d2d7b55156460250e7caf74d22b96d2013ab816a5ee9.

- 2026-09-10T12:07:04+00:00: Recorded command exit 0; command argv SHA-256
  b9e7dcc52dc7aa67624f2ae6a1fd28115e559381e90fca819f8afd7898758b12.

- 2026-09-10T12:07:14+00:00: Recorded command exit 0; command argv SHA-256
  16658ca53d61f64d870e5711ceac80792ae843f42a19eb373f7db2c9904c51d2.

- 2026-09-10T12:07:24+00:00: Recorded command exit 1; command argv SHA-256
  432e4987b8d8eb14d2c9cf454953c26e77ea2796fed0f7f0ee7fa975ee1007d7.

- 2026-09-10T12:08:02+00:00: Recorded command exit 0; command argv SHA-256
  432e4987b8d8eb14d2c9cf454953c26e77ea2796fed0f7f0ee7fa975ee1007d7.

- 2026-09-10T12:08:12+00:00: Recorded command exit 0; command argv SHA-256
  16658ca53d61f64d870e5711ceac80792ae843f42a19eb373f7db2c9904c51d2.

- 2026-09-10T12:08:21+00:00: Recorded command exit 0; command argv SHA-256
  4b76332be28b8a328412f5ac8f15a4f66d4ed876f1e3111e97e881324d40ca5b.

- 2026-09-10T12:08:42+00:00: Recorded command exit 0; command argv SHA-256
  0a5c1ad381942d3f6956f88a1cd783207b0b5a8ddde22a4f5f9806b3bbdface4.

- 2026-09-10T12:08:49+00:00: Recorded command exit 0; command argv SHA-256
  63d70b3bb79647c1da2a7f5fe27cdcf0360d5ad9c247e16d9d1710afbbc02e46.

- 2026-09-10T12:09:33+00:00: Recorded command exit 0; command argv SHA-256
  984fac3b70bf7d123af130e99a300a4d9a09e3fd45b9371c8c2b52f4f4e71367.

- 2026-09-10T12:09:46+00:00: Recorded command exit 0; command argv SHA-256
  7ef8ef2cb9d020747c12bcaa447c9832c48997da4229fb26cded0f498c898c32.

- 2026-09-10T12:09:55+00:00: Recorded command exit 0; command argv SHA-256
  8dddf68533c6608ba3037b11f020359ad27c2136a083e925ea4f31867da250ba.

- 2026-09-10T12:10:13+00:00: Recorded command exit 0; command argv SHA-256
  d19e2a874988e30f3b51c735779054d4c414ba65bc42e63bbc3df4aeef61989b.

- 2026-09-10T12:10:21+00:00: Recorded command exit 0; command argv SHA-256
  ff854fb3d7c4a8158488164f59b80e04998cc6d588d425fda47a314190ac78dd.

- 2026-09-10T12:10:31+00:00: Recorded command exit 0; command argv SHA-256
  d1590511f0a468ab484c37a33843a43fb4cc5208621b5744dcd99f38e8a6c02a.

- 2026-09-10T12:10:42+00:00: Recorded command exit 0; command argv SHA-256
  42c23259427566e127f7b39e5b6b0fa4d79b118415edb1285eb0fcec6ae0fa56.

- 2026-09-10T12:10:53+00:00: Recorded command exit 0; command argv SHA-256
  ba751a52187fbd62e489015f7da5cf8b109593e4bc19c6cfd1cd4429fc165ff6.

- 2026-09-10T12:11:01+00:00: Recorded command exit 0; command argv SHA-256
  cffd2573b675c715127bdd910a9ca3ff1b4dd1d6ec900a0f8884e13fee6caab4.

- 2026-09-10T12:11:18+00:00: Recorded command exit 1; command argv SHA-256
  401b11dc94ecec9fcc14b0a3fd13f96d2a740c7e058684c7a83936aee87c8f91.

- 2026-09-10T12:11:42+00:00: Recorded command exit 0; command argv SHA-256
  0762c2e9e88ded381cec99188f68223065c3de06e24401a16359e40d8358fc18.

- 2026-09-10T12:12:02+00:00: Recorded command exit 0; command argv SHA-256
  110084484f505487a5192719fd6774cf9dda8266ec7e4991e5068adf966dfc58.

- 2026-09-10T12:12:19+00:00: Recorded command exit 0; command argv SHA-256
  521d5479f561a96123b4c99f2025c832a76a8b4ba0b251909a8151465280b2e7.

- 2026-09-10T12:16:17+00:00: Recorded command exit 2; command argv SHA-256
  3e84c0ca229a9f0205bea57d9ffd6a0d45a75c9baf0cc28eb847af2c8ac6e55f.

- 2026-09-10T12:17:00+00:00: Recorded command exit 2; command argv SHA-256
  c169b093d61ce51536de5da59e947f8e5c7550829bed9dc7d693543fe21ebaa0.

- 2026-09-10T12:17:10+00:00: Recorded command exit 0; command argv SHA-256
  9fb327ae4a389d690beb5d35a638f44864c813be07c00c522e4330e01aae973b.

- 2026-09-10T12:17:21+00:00: Recorded command exit 0; command argv SHA-256
  88715fd009c31177e7c69d3e59c2e3f84d05b9da9c8f6452cd97d9a14aecd688.

- 2026-09-10T12:17:41+00:00: Recorded command exit 0; command argv SHA-256
  b28eb5defac71c8920b688bceaf1ddaf55e295be3fba8b0e9d0bc131689448f7.

- 2026-09-10T12:17:52+00:00: Recorded command exit 0; command argv SHA-256
  0762c43dab473c4ef3338b65d12bd5cf3c3a966f53bf49a85d094fe290ea3552.

- 2026-09-10T12:18:04+00:00: Recorded command exit 0; command argv SHA-256
  5d525659f351f939c0e1c543a197d2c119797b9530ee200b1906252991f9b37d.

- 2026-09-10T12:18:14+00:00: Recorded command exit 0; command argv SHA-256
  13035d664c27364e394d93a930e4831d8dc33307a51fd26e42252ab320be841e.

- 2026-09-10T12:18:23+00:00: Recorded command exit 0; command argv SHA-256
  38ac49a1b9fa9525833fc2fa663079f57eecd385c3b24d25514582601ef084f5.

- 2026-09-10T12:18:31+00:00: Recorded command exit 0; command argv SHA-256
  ea42a0af9d1da1b47880c795ccd8193445692d1e9b8f5e8aacc59d23b639c5ca.

- 2026-09-10T12:18:40+00:00: Recorded command exit 0; command argv SHA-256
  50f95f3978aec6500de8b40dee25864987b3cafed382426022a6d5cb264fbdbd.

- 2026-09-10T12:19:42+00:00: Recorded command exit 0; command argv SHA-256
  ad0f70bb89dfba2766fa55d74de758c899d3d20c81aef03a129d485ad325abe4.

- 2026-09-10T12:19:53+00:00: Recorded command exit 0; command argv SHA-256
  d686ba83e5bc7f33b487b629508f9f7023469d0b6a08663a9990450c53f64d45.

- 2026-09-10T12:20:14+00:00: Recorded command exit 1; command argv SHA-256
  40db98a36e652f13c51c48b3754c89c9e63fb82743d6f5d71f67ca35e4887ffc.

- 2026-09-10T12:20:30+00:00: Recorded command exit 0; command argv SHA-256
  a684ecf5a3917ad6dd4fa340c11acca99e92d72af061cc62d7c2fcfb5675568a.

- 2026-09-10T12:21:17+00:00: Recorded command exit 0; command argv SHA-256
  76ca5786d217c3da21de95460a4c5da59e63a5a14c0853f83cbdc010fc8de035.

- 2026-09-10T12:21:26+00:00: Recorded command exit 0; command argv SHA-256
  99ade3e6152d4c2b001225bd3c8d1926aba322c87253537e165ea951b651a488.

- 2026-09-10T12:21:36+00:00: Recorded command exit 0; command argv SHA-256
  cc63acba5f871584f084a0fd3dfb607665db55b4be5b2ba6265f7e9b218f5903.

- 2026-09-10T12:21:47+00:00: Recorded command exit 0; command argv SHA-256
  f97fe1b943f3af42645eb4605f6bc72c0c7650978ba536ff5c11f1dfc450e194.

- 2026-09-10T12:21:56+00:00: Recorded command exit 0; command argv SHA-256
  1b76f1862c877a52820edea6768c4949cfeb8389d162747c85759031ee8880ef.

- 2026-09-10T12:22:18+00:00: Recorded command exit 2; command argv SHA-256
  d1c8fab52298c87843abce6188d70060bb010ff6c540cd011317ffe4f3b9d66f.

- 2026-09-10T12:22:39+00:00: Recorded command exit 0; command argv SHA-256
  319265217d963449e554f2b4a770fb9b9bab6294ecd43d227c0ca6a6b0a6981c.

- 2026-09-10T12:22:48+00:00: Recorded command exit 0; command argv SHA-256
  6ffbf2f324cc22ad28eb63d898d42f4c5e461d30312080374554f07198306438.

- 2026-09-10T12:23:00+00:00: Recorded command exit 0; command argv SHA-256
  9effe816cc0a14ab84d63cce6382538df1ec16bb286043eae049e1448fa5c34d.

- 2026-09-10T12:23:10+00:00: Recorded command exit 1; command argv SHA-256
  e3595a84235d7cb8a10f73c6481a42b9dfec39725d0ec43832a92616b486c318.

- 2026-09-10T12:23:27+00:00: Recorded command exit 0; command argv SHA-256
  febeb799abf20c9082ce80560969f42ff72aa276f4f9af805ae3ddc503dd67ac.

- 2026-09-10T12:23:36+00:00: Recorded command exit 0; command argv SHA-256
  bea6c035f2c4c50040dc5b59a34658b5db53bb15c60ba245f207ef0ea0ae89ac.

- 2026-09-10T12:24:27+00:00: Recorded command exit 0; command argv SHA-256
  5a729de8a3d3dcaa9b91f1e7ee3581a4f4a259cb5358cb5f4d6e02e534cfa21c.

- 2026-09-10T12:24:56+00:00: Recorded command exit 0; command argv SHA-256
  a2e143f362a3c440d018487ece48e79dcfb9907891ea77f93f827a827a1e1f67.

- 2026-09-10T12:25:07+00:00: Recorded command exit 0; command argv SHA-256
  0fe0432e3c64909d9a7729d4fdde9d409148cf3e83b34a248fe0cea067c57826.
