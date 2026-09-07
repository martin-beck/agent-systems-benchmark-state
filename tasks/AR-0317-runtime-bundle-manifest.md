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
  "observed_dirty": 3,
  "observed_head": "b1669203308db5a75fee1e78a45c6fc8e71f17ce",
  "owner": "contracts-20260906",
  "plan": "../plans/AR-0317.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Define common signed runtime bundle manifests and offline verification.",
  "task_revision": 39,
  "title": "Define runtime bundle manifest and verifier",
  "updated_at": "2026-09-07T11:07:03+00:00",
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
