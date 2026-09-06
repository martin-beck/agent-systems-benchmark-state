---
{
  "branch": "feature/agent-opendesk",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-06T23:04:16+00:00",
  "depends_on": [
    "AR-0101",
    "AR-0102"
  ],
  "id": "AR-0302",
  "next_action": "Implement a fail-closed Linux x86_64 adapter around pinned OpenDesk 0.3.5 export JSON, with telemetry containment and explicit argv privacy limitation.",
  "observed_branch": "feature/agent-opendesk",
  "observed_dirty": 3,
  "observed_head": "b7e9078d53a4a4586beb68bf56233aba206112ac",
  "owner": "root-coordination-20260906",
  "plan": "../plans/AR-0302.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Support the bitclub OpenDesk CLI with its own dialect and compatibility record.",
  "task_revision": 84,
  "title": "Implement OpenDesk client adapter",
  "updated_at": "2026-09-06T22:06:27+00:00",
  "worktree_key": "agent-systems-benchmark-agent-opendesk"
}
---
## AR-0302

Support the bitclub OpenDesk CLI with its own dialect and compatibility record.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-06T21:04:14+00:00: Dependencies AR-0101 and AR-0102 are done; asb-agents OpenDesk paths
  are disjoint from active scheduler, workload, and comparability scopes, with shared Cargo/schema
  integration remaining fenced.

- 2026-09-06T21:04:16+00:00: Claimed by root-coordination-20260906.

- 2026-09-06T21:04:29+00:00: Recorded command exit 0; command argv SHA-256
  0a6027b61cddc0546b0532efbeddcb7565eb8d931f1209424da0fcd8631345f9.

- 2026-09-06T21:05:09+00:00: Recorded command exit 0; command argv SHA-256
  45a04b159fafc86dc241847890c46d71ce2c8222708b72811b3b597d758f341c.

- 2026-09-06T21:05:24+00:00: Recorded command exit 0; command argv SHA-256
  b09f2ac24df9f697e1d74da36a1eb7a431ba2bde6680e5110d7f3460b3fbe64f.

- 2026-09-06T21:05:36+00:00: Recorded command exit 0; command argv SHA-256
  f64d4bce4208152a4f8f7f9d04b22c6f642f11ad50c6ef47db9a5d890a84c203.

- 2026-09-06T21:07:03+00:00: Recorded command exit 0; command argv SHA-256
  6dfc69ac0f18d117307b24dd7cc9058363acd6dad44a746724e0c09440ee07ba.

- 2026-09-06T21:07:26+00:00: Recorded command exit 0; command argv SHA-256
  94e1a2f5f6f1714358deb32ae465f83cc1959443a8dd34bec1ac2fc6adaf1b02.

- 2026-09-06T21:07:51+00:00: Recorded command exit 0; command argv SHA-256
  a651e59e46fd06bdaebbcc9c4a5ebe52122f2979a5e1180ec2b67814641ad4db.

- 2026-09-06T21:08:06+00:00: Recorded command exit 0; command argv SHA-256
  7f96a72125f7f21894e9bc5308387e203c9c1ba412758a9be69a59f16d8f6906.

- 2026-09-06T21:08:24+00:00: Recorded command exit 0; command argv SHA-256
  38803e435d9641a6c4d6b411ee6252c77d74ab103bff5d97a9f06bb188ee0961.

- 2026-09-06T21:10:08+00:00: Recorded command exit 128; command argv SHA-256
  16afdabc3bc43036da2b9be5f15a07c3fb21ca6fe354a4d6c84b63c1900a26dc.

- 2026-09-06T21:10:28+00:00: Recorded command exit 1; command argv SHA-256
  16afdabc3bc43036da2b9be5f15a07c3fb21ca6fe354a4d6c84b63c1900a26dc.

- 2026-09-06T21:10:47+00:00: Recorded command exit 0; command argv SHA-256
  79423b37c6fc44767afbb6e2c6d89ca92a8f21e9aec9b166825194b1b67eadd5.

- 2026-09-06T21:10:58+00:00: Recorded command exit 0; command argv SHA-256
  b5ad7595a42b7e49f78c5bcd36d21339c062ae3c60c40d3508041762ee2d43fb.

- 2026-09-06T21:12:36+00:00: Recorded command exit 126; command argv SHA-256
  6a50e2d9912f1ebc279affc32e09602ca2472d7b60338e5ec9f4b94a8f4ec33e.

- 2026-09-06T21:13:29+00:00: Recorded command exit 128; command argv SHA-256
  55dfb8d588cc5e04d4cfa81d9429af59c5be7cbdd9e4e4c42d01158bab2a800a.

- 2026-09-06T21:13:54+00:00: Recorded command exit 0; command argv SHA-256
  55dfb8d588cc5e04d4cfa81d9429af59c5be7cbdd9e4e4c42d01158bab2a800a.

- 2026-09-06T21:19:45+00:00: Recorded command exit 0; command argv SHA-256
  e21ca9560ca72b879f56a8bba27a27bb031c80471f22d0e12772575faa9675cc.

- 2026-09-06T21:19:58+00:00: Recorded command exit 0; command argv SHA-256
  21ffbf46ab691b6d24adc1ebcb98afe5eecd0fd3fc9e62ac584c64b8b88e086a.

- 2026-09-06T21:20:11+00:00: Recorded command exit 128; command argv SHA-256
  737da72ab5c4c69bc80fc60712c2851194f66764b43edd7a39632aa7f5992375.

- 2026-09-06T21:20:30+00:00: Recorded command exit 0; command argv SHA-256
  f6e465a3285a5d3a12a6e03d0b0eb05628f38f01f8c3420dcc0d517adc8872e1.

- 2026-09-06T21:21:15+00:00: Recorded command exit 0; command argv SHA-256
  6e65010c168d77a340a96c0f92a9998a5ffe8629505215fc06770ba1d1dde25e.

- 2026-09-06T21:22:17+00:00: Recorded command exit 128; command argv SHA-256
  6490735cbec23327fe74e252f450654553fe5b39e4d5ad8c82c3890c9bbad8de.

- 2026-09-06T21:22:38+00:00: Recorded command exit 0; command argv SHA-256
  e8c8c98dd6b083040b7f08a3d25f2bee567b072433741f6464fa805229f43893.

- 2026-09-06T21:23:35+00:00: Recorded command exit 0; command argv SHA-256
  74e53fbac642acb23827cdc8022527437bfe6263ce29637e943a794c4f99ca2c.

- 2026-09-06T21:24:04+00:00: Recorded command exit 0; command argv SHA-256
  e889319fc59f920590ce0543cf0795cbee367950faadb9d500108a95dcfe73c3.

- 2026-09-06T21:24:16+00:00: Recorded command exit 0; command argv SHA-256
  c36372bc8aa72c9094efd6c6ab22494b03e8f6ee1040c2ba38e297d55bd0b3a4.

- 2026-09-06T21:26:50+00:00: Recorded command exit 0; command argv SHA-256
  abc8fdac0de568e6be19d2cc3cf720fc861a8b71002bc415d401e5a0735316c6.

- 2026-09-06T21:28:58+00:00: Recorded command exit 1; command argv SHA-256
  67e33c4fe36481dac259407017076702600d1dbff99743ab41781074d7b09702.

- 2026-09-06T21:29:30+00:00: Recorded command exit 1; command argv SHA-256
  519e801c79c274c478380acd8afead7fd1b36a4116e98ebed55aa773c4854176.

- 2026-09-06T21:29:46+00:00: Recorded command exit 0; command argv SHA-256
  9293ebfa9847fa7aa7475f6f0f561ece20b5301cc1dce575fc99dbd4905e7657.

- 2026-09-06T21:34:58+00:00: Recorded command exit 2; command argv SHA-256
  48458d4adcbc2714c4ae60f17ec39d916357031118af6e75d9a5cd826c73f20e.

- 2026-09-06T21:35:41+00:00: Recorded command exit 1; command argv SHA-256
  1324a3ef2051babfd4f86a7f96fc4ba077d6577422ce8c0f931710c75de60d83.

- 2026-09-06T21:35:59+00:00: Recorded command exit 0; command argv SHA-256
  d3cddd463cae084a639fa2c4dc99a82b5ecda4ccc4200d9aa4ffc1471ed361f8.

- 2026-09-06T21:36:18+00:00: Recorded command exit 0; command argv SHA-256
  eda65c6e9d990313374be2af16ac9825553cfc2ec540bcab819bc66210a30ce1.

- 2026-09-06T21:37:53+00:00: Recorded command exit 0; command argv SHA-256
  df5e600902657f86910bcb716a7fdfd171308684831ad3feabbbae2f31b5bc0d.

- 2026-09-06T21:39:09+00:00: Recorded command exit 0; command argv SHA-256
  daa573d0c6b8a515c8f509aa237446868acaa709731d3907aec8242270ffa0f6.

- 2026-09-06T21:39:14+00:00: Recorded command exit 0; command argv SHA-256
  55f885f47cdc8bf08b962b3056c70150bbb8efc900e88b181103f18e47bbd145.

- 2026-09-06T21:41:27+00:00: Recorded command exit 1; command argv SHA-256
  65423a2fe6ad7b8e760dd542617429f2ea362b3979a8005389a7494d6679e8d1.

- 2026-09-06T21:41:51+00:00: Recorded command exit 0; command argv SHA-256
  97cb7d28247960f0090e662f14d204ad35ac330ea7dd4f7b04eb07573a196371.

- 2026-09-06T21:42:18+00:00: Recorded command exit 0; command argv SHA-256
  ddf931f039374a91054ebaf7e8809d10f47ef11bc709b33f8bb48c7a1c2916e9.

- 2026-09-06T21:43:15+00:00: Pinned source tag v0.3.5 at f303069da72412dc90b3214d89da9c102282465f
  and npm artifact/executable digests; native loopback OpenAI-compatible smoke completed. Source
  inspection proves headless requires -c argv, stdout/export contain raw conversation, exit 0 alone
  is not success, and an unconditional heartbeat targets opendesk.matrix.openharmony.cn. Adapter
  must discard bounded raw output/export, parse benchmark task_success, isolate config, route all
  non-loopback traffic to a closed proxy, and claim only exercised Linux x86_64. Prompt argv
  visibility remains an explicit unsupported privacy boundary.

- 2026-09-06T21:44:59+00:00: Recorded command exit 0; command argv SHA-256
  31f662a8c0de0bdcef92075ddaf99fbd6a2befc75e47c3fccf36c521b0f46d24.

- 2026-09-06T21:46:46+00:00: Recorded command exit 0; command argv SHA-256
  9fc96a1c571eb76bc24066b70cc34a4a4032d4f12c0f4f0f453fa71cf77e5197.

- 2026-09-06T21:47:40+00:00: Recorded command exit 101; command argv SHA-256
  7008e12068a42a2947ec94d31b0ec3ed82641b58bf163610da21ec032def7303.

- 2026-09-06T21:48:08+00:00: Recorded command exit 0; command argv SHA-256
  3731222b89b5bcc0a1ae0bdca78217d25ac4e7a266b32e80af91050d83a25f1d.

- 2026-09-06T21:48:12+00:00: Recorded command exit 0; command argv SHA-256
  0e92d9045be60bbdabab0db39485cb0a5ad5a64db80a56f473b42bf57b9a3555.

- 2026-09-06T21:48:38+00:00: Recorded command exit 0; command argv SHA-256
  be3543159b1766792ffe490e98cdb71b55e1125a0e407b9a557bcf14fccd6439.

- 2026-09-06T21:49:52+00:00: Recorded command exit 0; command argv SHA-256
  81b3c663a7ac9038a3054efd611cf42261729b873e0aec6fcd4b0898e80f6384.

- 2026-09-06T21:50:02+00:00: Recorded command exit 101; command argv SHA-256
  fab41c00e2ebcdca27fa2a727f55580a61590324df4874e6dd14a85f9e9b22ae.

- 2026-09-06T21:50:20+00:00: Recorded command exit 0; command argv SHA-256
  b99e6a92e699e17d793ec5eeb3c4556e48b7351e1520e8a9a9135191d01874b2.

- 2026-09-06T21:50:31+00:00: Recorded command exit 101; command argv SHA-256
  fab41c00e2ebcdca27fa2a727f55580a61590324df4874e6dd14a85f9e9b22ae.

- 2026-09-06T21:50:57+00:00: Recorded command exit 0; command argv SHA-256
  5e87fae9129166f4e2c1650230bd51757091795bba7bee5b0ee6cb1d62566d47.

- 2026-09-06T21:51:02+00:00: Recorded command exit 0; command argv SHA-256
  fab41c00e2ebcdca27fa2a727f55580a61590324df4874e6dd14a85f9e9b22ae.

- 2026-09-06T21:51:59+00:00: Recorded command exit 3; command argv SHA-256
  f3555721d5da64da70e2de630282495ac34c9805bb2fed370bbe33f650277e0e.

- 2026-09-06T21:53:07+00:00: Recorded command exit 0; command argv SHA-256
  8e13e384aa832b697e9607df3a2c51c2289740eb410cf7ca625259550c709d0c.

- 2026-09-06T21:53:12+00:00: Recorded command exit 0; command argv SHA-256
  df0997a5a1f1604f83c6c9dddd1fdf781b7afdaa32c232374f1e98cae2db5b95.

- 2026-09-06T21:54:04+00:00: Recorded command exit 0; command argv SHA-256
  1dc663a95b158753628d4a5fbd11b7a9a337d2ee069b7c5a1dbcc78d10c5736e.

- 2026-09-06T21:54:09+00:00: Recorded command exit 0; command argv SHA-256
  7008e12068a42a2947ec94d31b0ec3ed82641b58bf163610da21ec032def7303.

- 2026-09-06T21:54:20+00:00: Recorded command exit 101; command argv SHA-256
  3baf8749f503eef5661517a73b0d2a11371ddd00662f8c4451acbb473662589d.

- 2026-09-06T21:54:56+00:00: Recorded command exit 0; command argv SHA-256
  7ea311bb2f74ebe5a6009b76d171c7f0b0ff310ea73dbe52449c7a27484b185a.

- 2026-09-06T21:55:01+00:00: Recorded command exit 101; command argv SHA-256
  3baf8749f503eef5661517a73b0d2a11371ddd00662f8c4451acbb473662589d.

- 2026-09-06T21:56:06+00:00: Recorded command exit 0; command argv SHA-256
  fa3062e37bc75cac7a715d9b88450089fc20cb0f2ebdf15eded7328c8dc02630.

- 2026-09-06T21:56:13+00:00: Recorded command exit 101; command argv SHA-256
  3baf8749f503eef5661517a73b0d2a11371ddd00662f8c4451acbb473662589d.

- 2026-09-06T21:57:13+00:00: Recorded command exit 0; command argv SHA-256
  111b9aa0c198d931a08662992160d387e32ba693400c37af30d8c259df619662.

- 2026-09-06T21:57:25+00:00: Recorded command exit 0; command argv SHA-256
  7008e12068a42a2947ec94d31b0ec3ed82641b58bf163610da21ec032def7303.

- 2026-09-06T21:58:12+00:00: Recorded command exit 101; command argv SHA-256
  3baf8749f503eef5661517a73b0d2a11371ddd00662f8c4451acbb473662589d.

- 2026-09-06T21:59:00+00:00: Recorded command exit 0; command argv SHA-256
  6971b32defabeac2083c1536727b218422ea8e1f0e85308f8e18a83a9a14d694.

- 2026-09-06T21:59:39+00:00: Recorded command exit 101; command argv SHA-256
  3baf8749f503eef5661517a73b0d2a11371ddd00662f8c4451acbb473662589d.

- 2026-09-06T22:00:28+00:00: Recorded command exit 0; command argv SHA-256
  5ca80a9c0a66cae09cc3942898ea5113d22eae166109fc5d192590c4def2a491.

- 2026-09-06T22:01:04+00:00: Recorded command exit 101; command argv SHA-256
  3baf8749f503eef5661517a73b0d2a11371ddd00662f8c4451acbb473662589d.

- 2026-09-06T22:01:34+00:00: Recorded command exit 0; command argv SHA-256
  1841c86b308bc5e802dfac9a6643e06c6c2c588d2ce62afb333d6083cc317c32.

- 2026-09-06T22:01:48+00:00: Recorded command exit 0; command argv SHA-256
  3baf8749f503eef5661517a73b0d2a11371ddd00662f8c4451acbb473662589d.

- 2026-09-06T22:02:44+00:00: Recorded command exit 1; command argv SHA-256
  b3eaf11a73f832c91dc198eed55c2e056832521463e43050da6a844e0da1479a.

- 2026-09-06T22:02:49+00:00: Recorded command exit 1; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-06T22:02:55+00:00: Recorded command exit 0; command argv SHA-256
  fab41c00e2ebcdca27fa2a727f55580a61590324df4874e6dd14a85f9e9b22ae.

- 2026-09-06T22:06:27+00:00: Recorded command exit 128; command argv SHA-256
  9d4ab0dc1cf63f0ca3dfa88be24c53525a179198a6131a456d7ae6df5d022cfd.
