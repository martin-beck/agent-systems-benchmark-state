---
{
  "branch": "feature/runtime-bundle-manifest",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-07T13:35:27+00:00",
  "depends_on": [
    "AR-0101",
    "AR-0102",
    "AR-0701"
  ],
  "id": "AR-0317",
  "next_action": "Define signed runtime-bundle manifests and an offline verifier for content, architecture, libc, license, and SBOM identity.",
  "observed_branch": "feature/runtime-bundle-manifest",
  "observed_dirty": 0,
  "observed_head": "3d0bc9ccf1c5d4c524cf7689e8d598897bf9c700",
  "owner": "contracts-20260906",
  "plan": "../plans/AR-0317.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Define common signed runtime bundle manifests and offline verification.",
  "task_revision": 88,
  "title": "Define runtime bundle manifest and verifier",
  "updated_at": "2026-09-07T11:34:17+00:00",
  "worktree_key": "agent-systems-benchmark-runtime-bundle-manifest"
}
---
## AR-0317

Define the common signed, content-addressed runtime-bundle manifest and offline verifier used by
per-agent bundle leaves. Cover complete transitive contents, architecture/libc, SPDX/CycloneDX
parity, license evidence, tamper detection, and offline operation.

- 2026-09-07T10:35:24+00:00: Dependencies AR-0101, AR-0102, and AR-0701 are done; promote the common
  signed runtime-bundle manifest and offline verifier with shared Cargo/schema/release integration
  serialized by the coordinator.

- 2026-09-07T10:35:27+00:00: Claimed by contracts-20260906.

- 2026-09-07T10:35:50+00:00: Recorded command exit 0; command argv SHA-256
  65768c45e18cb2d475428c52888be464156e9a0c6569f8921105f7698ff2a908.

- 2026-09-07T10:42:29+00:00: Recorded command exit 2; command argv SHA-256
  48458d4adcbc2714c4ae60f17ec39d916357031118af6e75d9a5cd826c73f20e.

- 2026-09-07T10:42:55+00:00: Recorded command exit 0; command argv SHA-256
  d3a810e79e1f213d7c5c8b568610b782881f1290b3191cf75ea15df2523294fb.

- 2026-09-07T10:50:43+00:00: Recorded command exit 0; command argv SHA-256
  456e72718c999b656ffec4c7724280b5dec8caea2635ac2bfc66db7e37a963fb.

- 2026-09-07T10:51:02+00:00: Recorded command exit 101; command argv SHA-256
  baae7d3914b31e76b8fc6409da8f89945ccc53bf7f6bf940550c302ac842d3db.

- 2026-09-07T10:51:26+00:00: Recorded command exit 101; command argv SHA-256
  6603f941053cb1999d19f7fe12705889fcb17f41b038c97f36f432c49e8c7cb1.

- 2026-09-07T10:51:41+00:00: Recorded command exit 0; command argv SHA-256
  600577937bcd46d71017ac3514fb52b1e26ab30d8342b91786d4f417c800a88c.

- 2026-09-07T10:53:50+00:00: Recorded command exit 0; command argv SHA-256
  75980b332195231ea2165502ab78d8bbb7772bcb084e51b818601bf9724b9740.

- 2026-09-07T10:54:07+00:00: Recorded command exit 1; command argv SHA-256
  3ad544cd7f6f1cd1779c7e13a604d4783003c3b39c253412edca0075645979d1.

- 2026-09-07T10:54:23+00:00: Recorded command exit 0; command argv SHA-256
  6723aed7c3a8b80d90afe191d670bcf8bc0b07bf71d4c80470daa0a2a76fa4c9.

- 2026-09-07T10:54:42+00:00: Recorded command exit 101; command argv SHA-256
  1dca12695547dc22175ee8589da389c4b5bfcb6f015c84bd389696f3df76a7ba.

- 2026-09-07T10:55:08+00:00: Recorded command exit 0; command argv SHA-256
  4401f5214028ab571a9dc329fec9cd37ba2b310f03a6d858b394376dbd1b7eef.

- 2026-09-07T10:55:29+00:00: Recorded command exit 0; command argv SHA-256
  64f7b847369cc416251851942d5ebbc60ec9636e1b8b6a60cfe23cb47b470521.

- 2026-09-07T10:55:53+00:00: Recorded command exit 101; command argv SHA-256
  89d4b2a89d80cd6c6f3e192369212e030731939409beed50241f1c1bfa28802b.

- 2026-09-07T10:56:07+00:00: Recorded command exit 0; command argv SHA-256
  450247491273b63aa56c7be2d8d3a2ac5bb2f33b1e1209e086fa9aaa9fe0fec2.

- 2026-09-07T10:56:30+00:00: Recorded command exit 0; command argv SHA-256
  89d4b2a89d80cd6c6f3e192369212e030731939409beed50241f1c1bfa28802b.

- 2026-09-07T10:57:46+00:00: Recorded command exit 0; command argv SHA-256
  b9dd83d9c6cdf15bc206348494a1ab1bb44ca01be1d4dd7441a79decef1ba8ff.

- 2026-09-07T10:58:05+00:00: Recorded command exit 0; command argv SHA-256
  aa2f63f31227faef0d410799b5ca67ffe2988f1d3be666d0053cb00aadaac38a.

- 2026-09-07T10:58:54+00:00: Recorded command exit 0; command argv SHA-256
  b5fbd7bded73bd63a1f932ea4ca7f6aafdbb0c1407c010e59acb1202b48c05f8.

- 2026-09-07T10:59:19+00:00: Recorded command exit 0; command argv SHA-256
  97ae70309e1bab4afc61e3d2b5c18f119a434a3600f4ba6176d9413a0ce24462.

- 2026-09-07T11:00:56+00:00: Recorded command exit 0; command argv SHA-256
  d0042505200326e5134996187f876b4a13c10dfedfebd24863ecffe30ec92f13.

- 2026-09-07T11:01:13+00:00: Recorded command exit 0; command argv SHA-256
  ddb551d7d48c346317eb0ec00b11ea43d4bcc182cb65e575b83a4ac3d58b5b75.

- 2026-09-07T11:01:41+00:00: Recorded command exit 0; command argv SHA-256
  18903184e40e5268b34290eff9471399f5ec421307315d60bf184af58f3c7fa4.

- 2026-09-07T11:02:07+00:00: Recorded command exit 0; command argv SHA-256
  239dfb0241e8cc38788d0dec0b54ff767bc9769933d6339d3801fdb03b04e801.

- 2026-09-07T11:02:30+00:00: Recorded command exit 0; command argv SHA-256
  e945f86d717144dd0c16ab5be09d1b86d7fdfbc433936742f3dd63399afaed8f.

- 2026-09-07T11:04:18+00:00: Recorded command exit 0; command argv SHA-256
  30a8398253170515690896ef84c97052d45603e1e34e36da6e8fef7a2979b5c8.

- 2026-09-07T11:04:32+00:00: Recorded command exit 0; command argv SHA-256
  8215707d5a877a68152afbb9fd64c568f910999e46681a26b4697409dcbd9578.

- 2026-09-07T11:04:48+00:00: Recorded command exit 101; command argv SHA-256
  e1b5834ae159881b8eb7ccba69c08eb3503dd4b0b6a2d5ab17cec1ea841e6361.

- 2026-09-07T11:05:08+00:00: Recorded command exit 0; command argv SHA-256
  3316ad5a65fbc68c4e228df0dd7c7adf6fe7c44d087f11d0210b491dfbf6e850.

- 2026-09-07T11:05:25+00:00: Recorded command exit 0; command argv SHA-256
  296380711112c244723455c7827db59e55047d785a9c8bf4f809f9e667ad51c4.

- 2026-09-07T11:05:45+00:00: Recorded command exit 0; command argv SHA-256
  232c07097dd462b1edc7eecb89a8a772660d361e64841bbf5c1ef752f0cbc5a4.

- 2026-09-07T11:07:03+00:00: Recorded command exit 0; command argv SHA-256
  63db1f3f036af83ee45eb1824b0b8d6e094ff620a755e1951335a1bf2f8da3f5.

- 2026-09-07T11:07:22+00:00: Recorded command exit 101; command argv SHA-256
  38fdb90e680894c0c059b0d4785af4c8e65733e0bc87f2989f220853fd14a082.

- 2026-09-07T11:08:00+00:00: Recorded command exit 0; command argv SHA-256
  00d0fb2c8e16d4aa40c565f21457deb1a0d7847c465023bec9f5bed6031c180e.

- 2026-09-07T11:08:17+00:00: Recorded command exit 101; command argv SHA-256
  e1b5834ae159881b8eb7ccba69c08eb3503dd4b0b6a2d5ab17cec1ea841e6361.

- 2026-09-07T11:08:31+00:00: Recorded command exit 0; command argv SHA-256
  5d1d9f1cfce609e883a1cab2e5bc2ac3ce40ae805b8a151e019294206f86a01d.

- 2026-09-07T11:08:48+00:00: Recorded command exit 0; command argv SHA-256
  b0bf88bc1336d35e83900d136b503fffe3b7057bcb5c3fdc51d20c0de26ea25b.

- 2026-09-07T11:09:09+00:00: Recorded command exit 0; command argv SHA-256
  8a70ac0d483527db9f3bcc0690f7252f995db29b5fea3325a3e836cd97abdfcc.

- 2026-09-07T11:10:03+00:00: Recorded command exit 0; command argv SHA-256
  3538a4486dda6f2f3f4cf4a4e8ccb17dfbde0a6cddadd6863ee9033ba8aa9355.

- 2026-09-07T11:10:52+00:00: Recorded command exit 1; command argv SHA-256
  e4492fa4cb73d838c69b6068755b1d56683e404029312848449d99ce3be11738.

- 2026-09-07T11:11:06+00:00: Recorded command exit 0; command argv SHA-256
  27ecdaafcac54406e05b48fd0f72bf68e9067989978330e2c501b125ce63f95d.

- 2026-09-07T11:11:59+00:00: Recorded command exit 0; command argv SHA-256
  e4492fa4cb73d838c69b6068755b1d56683e404029312848449d99ce3be11738.

- 2026-09-07T11:12:59+00:00: Recorded command exit 0; command argv SHA-256
  6adc8264f54b9db75926514bae12547e16b6a65fde4a9717a5d4b69ee82a8cca.

- 2026-09-07T11:13:27+00:00: Recorded command exit 1; command argv SHA-256
  543dae042c545f916b697b1b25c67a9beef5a3eda77d148f379c06ac144c9010.

- 2026-09-07T11:13:56+00:00: Recorded command exit 101; command argv SHA-256
  654bf09b27a1f84f07fad46b7b529dc2fed368b81cf30adec4c3fd28320704ac.

- 2026-09-07T11:14:17+00:00: Recorded command exit 1; command argv SHA-256
  ef8d9468c3aab2845f1ec53deaa8835aea06c9507406ba60b3993824189864df.

- 2026-09-07T11:15:01+00:00: Recorded command exit 1; command argv SHA-256
  bac632df08b8a33193ae7a6f31c8cc43c06d17a7725b803886b9ac01d15fe52a.

- 2026-09-07T11:16:07+00:00: Recorded command exit 0; command argv SHA-256
  2d2955e83d483821f210e2c5ebc17eff84061c942e7047dd068319109a49142b.

- 2026-09-07T11:17:09+00:00: Recorded command exit 0; command argv SHA-256
  fd936d58ad77fcc3fcfb375edb05a80130f3b2277bb49233e4943fd538eba1ec.

- 2026-09-07T11:17:30+00:00: Recorded command exit 1; command argv SHA-256
  e0a749a8b118dd1939f3a7a0aeb8e0673ff637a19e97cf1ac7c4b90323518f38.

- 2026-09-07T11:17:46+00:00: Recorded command exit 0; command argv SHA-256
  16459a54235f1e57ed5ac4ca476381c057c58bf4bddb721f5954491cf6fcdd3b.

- 2026-09-07T11:18:44+00:00: Recorded command exit 1; command argv SHA-256
  abda0d799688c01f1fce86e661002914a3cebf267b8dad9c36eb0528e9a99e69.

- 2026-09-07T11:19:01+00:00: Recorded command exit 0; command argv SHA-256
  309b783b696ce3e856a56ff5b7cc1e8a0ec52f641c6152fcea9b07d0672984e7.

- 2026-09-07T11:20:00+00:00: Recorded command exit 1; command argv SHA-256
  53802a7e875306aa9cd9d13d2c2c0ac3e17d748f335496c67c50b9ffc3416a7f.

- 2026-09-07T11:20:53+00:00: Recorded command exit 0; command argv SHA-256
  f67c587ab0a67cc3e0d53bf8bba329f88fb0cf5f3df97f37fa72e1d394feb8e4.

- 2026-09-07T11:21:27+00:00: Recorded command exit 0; command argv SHA-256
  b4bb3a0104092099c2354d592b3af6bf852c5962cd40749fb6e0989826209b87.

- 2026-09-07T11:21:46+00:00: Recorded command exit 101; command argv SHA-256
  a5297a73832ac0370235df06482986c16e3b7e916fd86340a07c0a89b242449f.

- 2026-09-07T11:22:05+00:00: Recorded command exit 0; command argv SHA-256
  a99fc6a4a43edce0ea2f2df1a761d6e97f482317c8ce34d22ab132c2b6e0c9b5.

- 2026-09-07T11:22:31+00:00: Recorded command exit 0; command argv SHA-256
  b0bf88bc1336d35e83900d136b503fffe3b7057bcb5c3fdc51d20c0de26ea25b.

- 2026-09-07T11:22:50+00:00: Recorded command exit 0; command argv SHA-256
  bf1a4da273a42fea4828a0b1f5818205d09d0855ee0da403b055712ec885db43.

- 2026-09-07T11:23:16+00:00: Recorded command exit 0; command argv SHA-256
  2e9e530ebdea6cf082a1a2410358eea892f2cc3878ebd03ff0e30a08a35fd1ed.

- 2026-09-07T11:24:53+00:00: Recorded command exit 1; command argv SHA-256
  dd06bdfc2e3e3ccaccca124524f5a103ac0f6c6120d27293ad0c36fa4eca0af6.

- 2026-09-07T11:28:14+00:00: Recorded command exit 2; command argv SHA-256
  ba5ffb984bdef177ca924b7f84f7855f3bf89dc275652c1129820e312862bd1b.

- 2026-09-07T11:29:00+00:00: Recorded command exit 2; command argv SHA-256
  48458d4adcbc2714c4ae60f17ec39d916357031118af6e75d9a5cd826c73f20e.

- 2026-09-07T11:29:39+00:00: Recorded command exit 0; command argv SHA-256
  05947787a0a88d3fb66763a0a031ad13971242b3bca4ff721bf8c44268a7ff99.

- 2026-09-07T11:30:37+00:00: Recorded command exit 0; command argv SHA-256
  74629f5c8fcf15f96f4e29dc3d493f63b378b917256c03df04f8758e6e29b1c3.

- 2026-09-07T11:30:55+00:00: Recorded command exit 1; command argv SHA-256
  8b9962c3ab5a7231f27baa8a7478e9e55cc6a8c1a36ad55c6830a21bf3ac94aa.

- 2026-09-07T11:31:17+00:00: Recorded command exit 0; command argv SHA-256
  0b8967e04b7dd083b2d6119efd41697244f8411b9c6b05cba6d074c606a9d5a7.

- 2026-09-07T11:31:45+00:00: Recorded command exit 0; command argv SHA-256
  4216711666955b32a0a64d65904636346d68aa6b9a735fa794710562aa37417d.

- 2026-09-07T11:32:00+00:00: Recorded command exit 0; command argv SHA-256
  321c534968b9c456a64caf5e6d09b63780c507f97548057d2bfe31edcfd73ff4.

- 2026-09-07T11:33:49+00:00: Recorded command exit 1; command argv SHA-256
  b0492190f0913182a668f90184e6b12b444612879a223d2dd40c321ba6ac2c66.

- 2026-09-07T11:34:17+00:00: Recorded command exit 1; command argv SHA-256
  85bb2bd72ad5b914846d98366c248a362d6b68a0eefc46ca0f028d91477b0b87.
