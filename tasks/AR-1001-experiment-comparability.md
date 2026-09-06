---
{
  "branch": "feature/experiment-comparability",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-06T22:08:22+00:00",
  "depends_on": [
    "AR-0101",
    "AR-0203"
  ],
  "id": "AR-1001",
  "next_action": "Rebase once after AR-0301 integration, take transferred Cargo/schema fence, wire modules, generate checked-in schema and matched/confounded fixtures, then run full gates.",
  "observed_branch": "feature/experiment-comparability",
  "observed_dirty": 15,
  "observed_head": "9543a3297dd9d0ca93c802bb204b099ac1df569b",
  "owner": "quality-20260906",
  "plan": "../plans/AR-1001.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Make every comparison content-addressed and explicit about agent, model, workload and platform confounders.",
  "task_revision": 60,
  "title": "Define experiment identity and comparability",
  "updated_at": "2026-09-06T20:49:54+00:00",
  "worktree_key": "agent-systems-benchmark-experiment-comparability"
}
---
## AR-1001

Make every comparison content-addressed and explicit about agent, model, workload and platform confounders.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-06T20:05:38+00:00: Claimed by quality-20260906.

- 2026-09-06T20:05:51+00:00: Recorded command exit 0; command argv SHA-256
  a87e6936612e0fe8006c110e65eb3032b43e306fe9daefeff2ae697b86690107.

- 2026-09-06T20:08:22+00:00: Heartbeat by quality-20260906.

- 2026-09-06T20:10:50+00:00: Recorded command exit 2; command argv SHA-256
  48458d4adcbc2714c4ae60f17ec39d916357031118af6e75d9a5cd826c73f20e.

- 2026-09-06T20:13:22+00:00: Recorded command exit 0; command argv SHA-256
  655a9b3e54d71c46d82ae8f5dc856d108816b96812b584054c1dc06c69c4f1c9.

- 2026-09-06T20:14:56+00:00: Recorded command exit 0; command argv SHA-256
  cd04871ebcbd721769286eeb65a26c1b026a799daa53696c99c538153d1d1098.

- 2026-09-06T20:15:24+00:00: Recorded command exit 0; command argv SHA-256
  710cb76ba0832d99e05dd0b97943369f3d8f0f5a58dc8795ac70e9b642f8dee7.

- 2026-09-06T20:15:43+00:00: Recorded command exit 0; command argv SHA-256
  9eb4a59131362f6308fcdd1af3a2ac9d3abf39328231207e85800dcce0547fb1.

- 2026-09-06T20:16:22+00:00: Recorded command exit 0; command argv SHA-256
  acb729de8c0dfef7a151e8decb21568cad5ab92fd2388c5dd975e1657c6430e1.

- 2026-09-06T20:16:37+00:00: Recorded command exit 0; command argv SHA-256
  e6a5c2e233ca93dde81b2e072b434e7f3dd229bfbd1ffaaa44ce0ac60d16c5ce.

- 2026-09-06T20:17:15+00:00: Recorded command exit 0; command argv SHA-256
  ff885f4e69f07b31f539454648b53438e81b6f6290c6b94237f715e86100fca2.

- 2026-09-06T20:18:40+00:00: Recorded command exit 0; command argv SHA-256
  5a334fc9961543439c95cad314f1e481d6c08e3b563fcbe95cf5f6cc3348171a.

- 2026-09-06T20:19:04+00:00: Implemented isolated source modules only: typed credential-free v1
  experiment identity, deterministic SHA-256 content address excluding its own digest, strict
  field/replay/bounds validation, and fail-closed comparison that reports deterministic confounder
  dimensions without raw values. Added protocol negative unit coverage. Did not touch Cargo.toml,
  Cargo.lock, generated schemas, fixtures, or registries while root AR-0301 holds the shared fence.
  First wrapped apply_patch attempt failed exit 2 because run stdin is DEVNULL; no product mutation.
  One later wrapped patch waited safely behind AR-0504 long coverage state lock, then applied after
  serialization.

- 2026-09-06T20:20:03+00:00: Recorded command exit 0; command argv SHA-256
  57975b9d36bf1e516aef1d2e97dca8486d066bc49c3bab18003b80f851da928a.

- 2026-09-06T20:20:47+00:00: Recorded command exit 1; command argv SHA-256
  b790f511afc61f9b1f73609956a900a0b4f4db06a4cecca4d4b28d2d8dd8295d.

- 2026-09-06T20:20:56+00:00: Recorded command exit 0; command argv SHA-256
  acae82902d4c8e17584017569d4c40fc10205ffd8eb2b80c4f71355c170258c8.

- 2026-09-06T20:21:23+00:00: Recorded command exit 0; command argv SHA-256
  133b32255181471858ea96a1689aef776e0d7bb604a303063023e10717c962a3.

- 2026-09-06T20:21:37+00:00: Recorded command exit 0; command argv SHA-256
  a44a605fefc46e11829b7c9c541f3674157660af29c7bbdfb457a1583a65d93a.

- 2026-09-06T20:28:24+00:00: Recorded command exit 0; command argv SHA-256
  282fed576370daee5fa029a6e337ec6c01e112c0f3abdc71817b969dabcc190f.

- 2026-09-06T20:28:36+00:00: Recorded command exit 101; command argv SHA-256
  7e71e334f663fe949b5f7f96b352083d2725feed830d96fe2aa60dab62fc0c72.

- 2026-09-06T20:28:53+00:00: Recorded command exit 0; command argv SHA-256
  c699bef32e8ee0f5d80d919f57575fd3f4ba225b5006d3b698c490b723264d81.

- 2026-09-06T20:29:06+00:00: Recorded command exit 0; command argv SHA-256
  f058a9534a68b79de52dfdd00be504c56f4f9bfec3c04f02f7be76392dfe9752.

- 2026-09-06T20:29:27+00:00: Recorded command exit 101; command argv SHA-256
  ae336d5fde85b0aa4a12ce1fb225d3048d74c005e8d938f9386278d737c5b067.

- 2026-09-06T20:29:38+00:00: Recorded command exit 0; command argv SHA-256
  dd1a1b00e66979dc8b85358045fcbca90a3cef29baf659f6d2abfced47271dd6.

- 2026-09-06T20:31:01+00:00: Recorded command exit 0; command argv SHA-256
  4ad4757370b8c8873a962e5cbec6c945010f0c4b881e7e6b9a2a6c64bcdbbe58.

- 2026-09-06T20:31:16+00:00: Recorded command exit 101; command argv SHA-256
  dcbb54da441fcf13f3619e31cd6de81b28451b5ca96099206f5b46670b68e483.

- 2026-09-06T20:31:31+00:00: Recorded command exit 0; command argv SHA-256
  a79793d3b81d246307c7bef1d6a0d4982089675fb54d45fae8cbdc2f961e2402.

- 2026-09-06T20:31:42+00:00: Recorded command exit 0; command argv SHA-256
  dd1a1b00e66979dc8b85358045fcbca90a3cef29baf659f6d2abfced47271dd6.

- 2026-09-06T20:31:55+00:00: Recorded command exit 0; command argv SHA-256
  54e3ef9b279a5aa2d51d94d9f3d3dbb1e7f0d12ef8f641eece9eca218d301a26.

- 2026-09-06T20:32:18+00:00: Recorded command exit 0; command argv SHA-256
  f834554712607d9ed768641824377da4d7ef9d9b27d08b2841436b6873f1445a.

- 2026-09-06T20:32:32+00:00: Recorded command exit 0; command argv SHA-256
  94afea8492cdb1d16385be104f6055d1107061e72f729253c897c91e85e3495b.

- 2026-09-06T20:32:45+00:00: Recorded command exit 0; command argv SHA-256
  dd1a1b00e66979dc8b85358045fcbca90a3cef29baf659f6d2abfced47271dd6.

- 2026-09-06T20:33:16+00:00: Recorded command exit 0; command argv SHA-256
  3599f2477dbaef5ee30d5a9ec2076e8214a559e38788e766d39ecc844b60f124.

- 2026-09-06T20:33:31+00:00: Recorded command exit 101; command argv SHA-256
  7a9b3b7231e69c4b452728ca212937e8ccd53c1cc4ad5ff3bbc234748def1eb3.

- 2026-09-06T20:33:45+00:00: Recorded command exit 0; command argv SHA-256
  c64a5762105f56388f4e3393b1e141d75f0108039db1cc63d64347059b1d17f6.

- 2026-09-06T20:34:05+00:00: Recorded command exit 0; command argv SHA-256
  4bbec9c65a5324d6962b5000e83a5cabaf228f71abf544b79202d711f925258a.

- 2026-09-06T20:34:25+00:00: Recorded command exit 0; command argv SHA-256
  dd1a1b00e66979dc8b85358045fcbca90a3cef29baf659f6d2abfced47271dd6.

- 2026-09-06T20:37:24+00:00: Isolated source validation uses scratch manifests under
  /srv/data/projects/.asb-local/ar1001-source-check that point to, rather than copy, owned product
  source. Pinned Rust 1.93 offline all-target tests pass 7/7 and clippy -D warnings passes. Stable
  llvm-cov reports comparison 100% and protocol 98.61% source-line coverage (99.22% combined; 96.68%
  combined regions). Branch instrumentation was attempted and failed before tests because
  cargo-llvm-cov requires nightly for --branch; no branch-coverage claim. A newly added
  replay-negative initially expected Replay+missing-cassette while leaving mode Live, failed
  correctly, was diagnosed/fixed, and all tests reran green.

- 2026-09-06T20:45:56+00:00: Recorded command exit 1; command argv SHA-256
  9e5def586634a7c667869234dea4a855b206fcaadb733c84b1ae068e6c16e4db.

- 2026-09-06T20:46:18+00:00: Recorded command exit 0; command argv SHA-256
  f091112720cc2a1f71c0d4c2c8c0a1912cb07accdfd4e50e2fdbf8ac271232ad.

- 2026-09-06T20:47:01+00:00: Recorded command exit 0; command argv SHA-256
  012f51100fc161d9a1a4df1b98c71947bc8ec18c32b54bb17e73cf1c556c2dc1.

- 2026-09-06T20:47:23+00:00: Recorded command exit 0; command argv SHA-256
  85fee6aeb3accf257d2fa9fd2138e00c99b5d7ac5c4690ff6cc8748eeef4a3b4.

- 2026-09-06T20:47:46+00:00: Recorded command exit 0; command argv SHA-256
  14858fcef02d2bfbe74419b77c98235d5f28328aa070b032005fe2918c96446d.

- 2026-09-06T20:48:23+00:00: Recorded command exit 0; command argv SHA-256
  de6f117708fcab43074a277fd262f12cb78beefd05a32a6ed8714d4a3276a6ff.

- 2026-09-06T20:48:39+00:00: Recorded command exit 0; command argv SHA-256
  ad7f2be03ac46d166a9a8919bd3c9b86eee6b1a6af3c85a6aa4bdf750d707107.

- 2026-09-06T20:48:52+00:00: Recorded command exit 0; command argv SHA-256
  2d324c5cf1b91ca95a5eaafd1ecb64c3ce78aecc41b74ea5016d0b6527a1427b.

- 2026-09-06T20:49:19+00:00: Recorded command exit 0; command argv SHA-256
  493f9a26dfd468fdb8df35c923b93e71e7fdd4c6338ff033abad0fc2b50004d8.

- 2026-09-06T20:49:54+00:00: Recorded command exit 0; command argv SHA-256
  551e5edc6b2954b6bee6225ba11e0688b57dc94c7c76d513a580c2cac7ff39f4.
