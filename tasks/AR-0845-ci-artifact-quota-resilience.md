---
{
  "branch": "feature/ci-artifact-quota-resilience",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-07T13:04:47+00:00",
  "depends_on": [
    "AR-0003",
    "AR-0831"
  ],
  "id": "AR-0845",
  "next_action": "Make optional CI evidence quota-aware while preserving required-check semantics and provenance.",
  "observed_branch": "feature/ci-artifact-quota-resilience",
  "observed_dirty": 0,
  "observed_head": "7d98653e7e7f219cced6abfb5c611d2614c72bd7",
  "owner": "quality-20260906",
  "plan": "../plans/AR-0845.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Prevent exhausted GitHub artifact quota from obscuring authoritative ASB results.",
  "task_revision": 53,
  "title": "Harden CI artifact quota behavior",
  "updated_at": "2026-09-07T12:06:24+00:00",
  "worktree_key": "agent-systems-benchmark-ci-artifact-quota-resilience"
}
---
## AR-0845

Make ASB CI distinguish required checks from optional artifact publication when GitHub artifact quota
is exhausted. Preserve test truth, provenance, privacy, and failure visibility; never turn a required
artifact or required check silently optional. Add quota detection, bounded diagnostics, fixtures, and
operator guidance.

- 2026-09-07T11:34:45+00:00: Dependencies AR-0003 and AR-0831 are durably done; declared
  branch/ref/worktree are absent. Promote only optional-artifact quota resilience; keep AR-0846
  planned behind AR-0845 and AR-0903.

- 2026-09-07T11:34:47+00:00: Claimed by quality-20260906.

- 2026-09-07T11:34:54+00:00: Recorded command exit 0; command argv SHA-256
  b99c4627ac0ef4cea44bffc0a740f529746ed2e6296605c5f4663fdbed9116b4.

- 2026-09-07T11:39:06+00:00: Recorded command exit 1; command argv SHA-256
  2e086b8b83af13e1d3333985e8b55b5d4bfbb90b0d89cbe5701ad393a564251a.

- 2026-09-07T11:40:03+00:00: Recorded command exit 0; command argv SHA-256
  3dd7f7357a238d20596efa9d08905c55d8f536d5f27602fd768b58d69baa9212.

- 2026-09-07T11:41:57+00:00: Recorded command exit 0; command argv SHA-256
  443a552c3b0583840ca023a5761944c2eafc18adbd03338912e07d38e35af0de.

- 2026-09-07T11:43:12+00:00: Recorded command exit 0; command argv SHA-256
  7d2c2b2f26c377193c0f695ff56acc8387d77576a3df4a471ea01d7382f8fd42.

- 2026-09-07T11:44:32+00:00: Recorded command exit 0; command argv SHA-256
  6196620d7b2953c1c3899ef214716b6193974134b95fb7fb62a4b1fff0c97897.

- 2026-09-07T11:44:51+00:00: Recorded command exit 1; command argv SHA-256
  c8210befebd8eed901558968d6ce662ba32685de477877544b6a9909983ec559.

- 2026-09-07T11:45:05+00:00: Recorded command exit 0; command argv SHA-256
  645026f8613b52cf0471fe6325316c638d8e58eb654fce8a0656db501d414868.

- 2026-09-07T11:45:24+00:00: Recorded command exit 1; command argv SHA-256
  77b24eae8ccedc66543f9f83a3a7f2913288793578f983a54d652c4c416a6882.

- 2026-09-07T11:45:39+00:00: Recorded command exit 0; command argv SHA-256
  4f1b17aa87534c6abf210db760cd56495905ed917e6a8359cdab35bd27fd9a8d.

- 2026-09-07T11:45:56+00:00: Recorded command exit 0; command argv SHA-256
  9f115ae7982ba6588aec3f10e684e3087aca2a7a422ab0ae16da06db165de166.

- 2026-09-07T11:46:47+00:00: Recorded command exit 0; command argv SHA-256
  fe49674361a69e15b429ca7d7e9758b73fcd5dca60c286b286af80c1769d2f6b.

- 2026-09-07T11:47:38+00:00: Recorded command exit 0; command argv SHA-256
  1985dd7ee61c2e53877735dd49fa79e0b0de93df05f495ce5aee07b714d460a3.

- 2026-09-07T11:47:57+00:00: Recorded command exit 1; command argv SHA-256
  6422f42a8413cdb5b3bb717856db09aeeb6ba62cc3802106b363b59c3e676ea7.

- 2026-09-07T11:48:35+00:00: Recorded command exit 0; command argv SHA-256
  0421b48219e835b879a47216ef66febdfeca76b1a2568b416dec43d864f33a91.

- 2026-09-07T11:48:56+00:00: Recorded command exit 2; command argv SHA-256
  217d0dc688b4b0bf5c37098851004af23e5994aa3b20b3e392454b0d6e93767e.

- 2026-09-07T11:49:50+00:00: Recorded command exit 0; command argv SHA-256
  c39460f595363ad3137b192c8b892fccd6a2cfb38858cc1cec29114cd91f766f.

- 2026-09-07T11:50:09+00:00: Recorded command exit 0; command argv SHA-256
  217d0dc688b4b0bf5c37098851004af23e5994aa3b20b3e392454b0d6e93767e.

- 2026-09-07T11:51:02+00:00: Recorded command exit 0; command argv SHA-256
  6ca3a0c4b82c4fa566fe1b2cb507efab403d2194a9d4feea4dc3c773634bdb38.

- 2026-09-07T11:51:35+00:00: Recorded command exit 0; command argv SHA-256
  b7203beb11c11a67db8ff1c68f160fd8b57f24ee7574fea45296bd0b4a943a5b.

- 2026-09-07T11:52:27+00:00: Recorded command exit 1; command argv SHA-256
  e44036cca6896f492f07cfb76b222986ad8f0a336c1fe0d64de787cce44e4a84.

- 2026-09-07T11:52:57+00:00: Recorded command exit 0; command argv SHA-256
  50d45c0c259cb19503bae506462360e12977639d3c0de440f1b000e4cda03ec5.

- 2026-09-07T11:53:31+00:00: Recorded command exit 1; command argv SHA-256
  e2b6651e2538d3a942ff988f15bc67a430a229a69e016d01c5e21dc025df352a.

- 2026-09-07T11:53:51+00:00: Recorded command exit 0; command argv SHA-256
  eb60d8b8e561210276ac63d2dd4e5c07c0dd59bf585b2d59e17c489b354a3470.

- 2026-09-07T11:54:44+00:00: Recorded command exit 0; command argv SHA-256
  e2b6651e2538d3a942ff988f15bc67a430a229a69e016d01c5e21dc025df352a.

- 2026-09-07T11:55:21+00:00: Recorded command exit 0; command argv SHA-256
  c54464ead392c38078404a51263ccf7b1e17d6b413f3a6ba65161acababbb868.

- 2026-09-07T11:56:30+00:00: Recorded command exit 0; command argv SHA-256
  4eddd3ddfcd5d8d6d626aa30f9890b0b071a9546a9b9e58b528a486b55a64e23.

- 2026-09-07T11:57:56+00:00: Recorded command exit 0; command argv SHA-256
  e5f4fa2644ea7c659f690a34c83d2a17799979910f3a64c4f968760a6a6e913a.

- 2026-09-07T11:59:33+00:00: Recorded command exit 1; command argv SHA-256
  0ca5dd615cface37ff95022c7408ac496df48d82c3f4d03e4d37b7542e140064.

- 2026-09-07T12:00:27+00:00: Recorded command exit 0; command argv SHA-256
  db26fb758b234791c3fa30b53525a339347bdd929f18f22745c0c770e24df15f.

- 2026-09-07T12:02:09+00:00: Recorded command exit 1; command argv SHA-256
  2e086b8b83af13e1d3333985e8b55b5d4bfbb90b0d89cbe5701ad393a564251a.

- 2026-09-07T12:02:50+00:00: Recorded command exit 0; command argv SHA-256
  bc62c49d0048283d28db4ee273965843616e94b5921c7f9f7d7461cd92e3422c.

- 2026-09-07T12:03:10+00:00: Recorded command exit 127; command argv SHA-256
  28a020345ae0a000a8617a8c485fd18f2eef53f059801341480ad04f2fe1d54e.

- 2026-09-07T12:03:43+00:00: Recorded command exit 1; command argv SHA-256
  c8d4f166c542b18dfcba0928eb0a291cfd8d265a890b24ce6880638528a6c715.

- 2026-09-07T12:03:56+00:00: Recorded command exit 0; command argv SHA-256
  324fe47fb69bd4b9a0141a205a4118b1263ff7fd8d79b13359376f183daddc17.

- 2026-09-07T12:04:13+00:00: Recorded command exit 127; command argv SHA-256
  c8d4f166c542b18dfcba0928eb0a291cfd8d265a890b24ce6880638528a6c715.

- 2026-09-07T12:04:29+00:00: Recorded command exit 0; command argv SHA-256
  e5af71e294c802e11556ad5d482d63bfb4d4f0ee92d0142f4b4f6a12fcff3f09.

- 2026-09-07T12:04:46+00:00: Recorded command exit 0; command argv SHA-256
  2d43b6f25d9147081b105af6ee60e3dba227a802779b84342e68808278f0ec0e.

- 2026-09-07T12:06:24+00:00: Recorded command exit 1; command argv SHA-256
  c6480ca3d66d63bf72bd3d0e2b05a772611c1ada417aa4350dbc5416ca7d35ae.
