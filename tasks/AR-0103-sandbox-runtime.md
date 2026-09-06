---
{
  "branch": "feature/sandbox-runtime",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-06T20:22:42+00:00",
  "depends_on": [
    "AR-0102"
  ],
  "id": "AR-0103",
  "next_action": "Run exact-tree full quality/privacy/supply-chain gates, create focused signed DCO commit and PR, then await immutable-head review and CI; root Cargo/lock remain fenced.",
  "observed_branch": "feature/sandbox-runtime",
  "observed_dirty": 1,
  "observed_head": "f4f1875b7e48f7a6636d9bf8ef0caabe0d15ff98",
  "owner": "contracts-20260906",
  "plan": "../plans/AR-0103.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Isolate untrusted generated code and allocate cgroup/CPU/memory/PID budgets.",
  "task_revision": 100,
  "title": "Implement isolated execution and resource leases",
  "updated_at": "2026-09-06T18:35:08+00:00",
  "worktree_key": "agent-systems-benchmark-sandbox-runtime"
}
---
## AR-0103

Isolate untrusted generated code and allocate cgroup/CPU/memory/PID budgets.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-06T17:44:13+00:00: Claimed by contracts-20260906.

- 2026-09-06T17:44:30+00:00: Recorded command exit 0; command argv SHA-256
  f5db5950ed3ebac6fe52d904adc7fa04c8635a51a93dcdb8a5d853a5095dabf8.

- 2026-09-06T17:45:41+00:00: Recorded command exit 0; command argv SHA-256
  54e2df778337ab245f4101716dc1ded6767e6c307e0ca87e616ece75bdca17a2.

- 2026-09-06T17:46:21+00:00: Recorded command exit 1; command argv SHA-256
  1bb9e1171df9c2bff2b89e43f7e63eb1fe501f03f003662952c3f581e4e0ac5b.

- 2026-09-06T17:46:58+00:00: Reconciled signed promotion repair d763c7f and fresh state, then
  claimed AR-0103 in its declared feature/sandbox-runtime worktree at exact integrated main e6a81e8.
  The earlier f166248 promotion effect is preserved and its generated-view repair is durable. Native
  probe found bubblewrap 0.9.0 and a working systemd 255 user scope with cgroup v2 controllers,
  while direct current-session cgroup writes and plain unshare user/network are unavailable. A real
  disposable MemoryMax/TasksMax/CPUQuota user scope succeeded. Design will therefore fail closed
  around exact executable/version probes, bubblewrap namespaces with network denial and minimal
  mounts, systemd user-scope resource properties, explicit CPU reservation leases disjoint from CI
  resources, bounded inputs, and documented cgroup/daemonization/platform limits. No root Cargo/lock
  mutation.

- 2026-09-06T17:48:05+00:00: Recorded command exit 1; command argv SHA-256
  db87c36f5743872c9f740f2105268de6e24fec38fa74e935a559fae7d506dbb7.

- 2026-09-06T17:48:22+00:00: Recorded command exit 0; command argv SHA-256
  41ecf8bd73d31df144c9c2b44abcf9d80e802e020e6f2bcea2ac4522765368af.

- 2026-09-06T17:52:56+00:00: Recorded command exit 0; command argv SHA-256
  f08e25c5942d67126891fb0ad368829f711225a34fc131e9c2d23b31544226b7.

- 2026-09-06T17:53:18+00:00: Recorded command exit 0; command argv SHA-256
  55330e4811159a70ea1f1fa36f542979bdc13a976674bccd6daadc497b13e922.

- 2026-09-06T17:54:51+00:00: Recorded command exit 0; command argv SHA-256
  f7688bab73070b01c61efff2a6a36e072f969058eaa52f7e898a45d5c2cdf1f2.

- 2026-09-06T17:55:08+00:00: Recorded command exit 101; command argv SHA-256
  55330e4811159a70ea1f1fa36f542979bdc13a976674bccd6daadc497b13e922.

- 2026-09-06T17:55:24+00:00: Recorded command exit 0; command argv SHA-256
  772bd5425180ceb77c624e02d6b34195aa84bbf2cdfad9956b705148186d324d.

- 2026-09-06T17:55:37+00:00: Recorded command exit 0; command argv SHA-256
  8bf3fb31fedd4b3e4bc70bef5f0f1459f25c3da4bfea60ad9e5e554fd97bd1a6.

- 2026-09-06T17:55:59+00:00: Recorded command exit 101; command argv SHA-256
  aa3ea198239b622282057090afa407ff0f6e5a461ce9c64566c4a49f2e433c59.

- 2026-09-06T17:56:20+00:00: Recorded command exit 0; command argv SHA-256
  b8fc6fdf20d89464d9e88015b4166013689114a3b4b6278ea9ebc96d4e9cfe06.

- 2026-09-06T17:57:08+00:00: Recorded command exit 101; command argv SHA-256
  8f56e04f8b968e399900e6993b1115ae07f0e705af87a57e617d6a8ae2d4f158.

- 2026-09-06T17:57:56+00:00: Recorded command exit 0; command argv SHA-256
  05fff524a446fa054e46432a604e39b5562e3d9caa20403fe0552bbf7d3f6fe3.

- 2026-09-06T17:58:46+00:00: Recorded command exit 101; command argv SHA-256
  8f56e04f8b968e399900e6993b1115ae07f0e705af87a57e617d6a8ae2d4f158.

- 2026-09-06T17:59:05+00:00: Recorded command exit 0; command argv SHA-256
  065d69c0be8182c89f3c8ba477fc6ff4caefd16506265b81a5b0ee89ce5541b6.

- 2026-09-06T17:59:34+00:00: Recorded command exit 0; command argv SHA-256
  50a5145852c17985d004ea12305492591c351e8a0cf8f2752b070238c2c88391.

- 2026-09-06T18:00:06+00:00: Recorded command exit 101; command argv SHA-256
  0d984d3039fcfb0ea504bade5f67ff323c8e5fd03046d1223d27fb3d9f2a6b8e.

- 2026-09-06T18:00:31+00:00: Recorded command exit 0; command argv SHA-256
  af4c29a9b0125f247bb3d8734be175a89fea9149b304cd25339e58d8cc1b13dd.

- 2026-09-06T18:01:12+00:00: Recorded command exit 101; command argv SHA-256
  0d984d3039fcfb0ea504bade5f67ff323c8e5fd03046d1223d27fb3d9f2a6b8e.

- 2026-09-06T18:01:32+00:00: Recorded command exit 0; command argv SHA-256
  126842f56f6950e06c63320a761dea95b9118d512b21d4698f3bff5546cc17c8.

- 2026-09-06T18:01:52+00:00: Recorded command exit 0; command argv SHA-256
  fcb1d3d5fb458ac764d581b5b62b433da6371b16e6513aa1ff611030f854b2b9.

- 2026-09-06T18:02:13+00:00: Recorded command exit 101; command argv SHA-256
  0d984d3039fcfb0ea504bade5f67ff323c8e5fd03046d1223d27fb3d9f2a6b8e.

- 2026-09-06T18:02:29+00:00: Recorded command exit 0; command argv SHA-256
  ad60485817f575b1b3071bc84bd599dec1ef84962240a76b38ef479e92a912bb.

- 2026-09-06T18:02:59+00:00: Recorded command exit 0; command argv SHA-256
  33f9422d40cb4e25b4f75efb28bbec829416348d5998d61f26d4f986c31f270b.

- 2026-09-06T18:04:00+00:00: Recorded command exit 0; command argv SHA-256
  3eb9b0b5243dcc1d006776981a6ca170d708ef56c4c547404cb066bed91ec592.

- 2026-09-06T18:04:20+00:00: Recorded command exit 1; command argv SHA-256
  1dbcb43d61363990321ebc98b97e902be6483d20e089078cb70041d31bca6b96.

- 2026-09-06T18:04:52+00:00: Recorded command exit 0; command argv SHA-256
  b67bf78cc20844bebdf470ff9bb3905ff841946a5ac35cfb1f0d62eaefb8eb90.

- 2026-09-06T18:05:43+00:00: Recorded command exit 0; command argv SHA-256
  426580733078b62c070e80955a8b17ef886d428fcdfdb70351e6961b909ba259.

- 2026-09-06T18:06:20+00:00: Recorded command exit 1; command argv SHA-256
  af8e558441c612f592e71f0c56da8334c91394cceeeacd277c76a2ab7a62495e.

- 2026-09-06T18:06:42+00:00: Recorded command exit 0; command argv SHA-256
  1c14a1a32ba8514d3a96ca91fa8feab0eab4b634edbd6d65f5b0b41b4db431d2.

- 2026-09-06T18:07:10+00:00: Recorded command exit 101; command argv SHA-256
  a441bc124b0d140968a92fc7e791ee95fff085e28fcd27819ad5af13d1e4b5a9.

- 2026-09-06T18:08:08+00:00: Recorded command exit 0; command argv SHA-256
  ff36a52aaa1ad2e1258e089cfa0f76b4ab8ddf2cb90fa5dc845bb804477f84db.

- 2026-09-06T18:08:37+00:00: Recorded command exit 0; command argv SHA-256
  a218d98ab86fb942f22aa1a6de1d98d233037901162558460fde429344ff2ae0.

- 2026-09-06T18:09:14+00:00: Recorded command exit 1; command argv SHA-256
  8be137625e06e3f2390a4795ecd432c4ded32f9214b235ca6e9262ce3f3531da.

- 2026-09-06T18:09:48+00:00: Recorded command exit 0; command argv SHA-256
  b9eb73817f6a49836355f035991a31ccfc574354b044f0141a37a6ded1a81678.

- 2026-09-06T18:10:00+00:00: Recorded command exit 101; command argv SHA-256
  a80adb16ddcba3907ac3cb6ff598fc6ab0751be0f86cb8e4399db37131c763c8.

- 2026-09-06T18:10:27+00:00: Recorded command exit 0; command argv SHA-256
  0c1742630140a7df8172d89b3e9bc53e3153e38f7235c065c0c33442047e31a8.

- 2026-09-06T18:10:46+00:00: Recorded command exit 101; command argv SHA-256
  08a89404c58f84658090053fc1eef2bb99d7aa9af8672a6358729bfd5b493e7b.

- 2026-09-06T18:11:24+00:00: Recorded command exit 1; command argv SHA-256
  0fd7dcb279363a8f74b18d2a866a06130b4050cb30423fb783dae4559ac997d1.

- 2026-09-06T18:12:02+00:00: Recorded command exit 1; command argv SHA-256
  77fbfb3f8003925da2795df4db7393c6765c700d26ca7b1c0af9a486a3372f03.

- 2026-09-06T18:12:44+00:00: Recorded command exit 0; command argv SHA-256
  c3a875fe1fb50e6329c2cbc41b4a839b78be74021b3683f92de7e68ea7767066.

- 2026-09-06T18:13:06+00:00: Recorded command exit 0; command argv SHA-256
  a80adb16ddcba3907ac3cb6ff598fc6ab0751be0f86cb8e4399db37131c763c8.

- 2026-09-06T18:14:18+00:00: Recorded command exit 0; command argv SHA-256
  473b0c29ecb6c476181868ab6f5c9dabe0ef07b74d8e3c6e21ef8db6bb5b53bc.

- 2026-09-06T18:14:35+00:00: Recorded command exit 0; command argv SHA-256
  ad7a5cdea87a82ea9f84c7173865e92e1610ebd77a6411a7540a9379b41685cb.

- 2026-09-06T18:14:54+00:00: Recorded command exit 101; command argv SHA-256
  70a855102ebe934d4bf662e96ade9e9ea56a45475dfb2d08214509be9f89616b.

- 2026-09-06T18:15:14+00:00: Recorded command exit 0; command argv SHA-256
  78644c0f75658a395747bdfb805158ed079eb5b6ece42b6704b243f7ae77d9d4.

- 2026-09-06T18:15:55+00:00: Recorded command exit 0; command argv SHA-256
  f7754ad55a3bb0a00a5fa0c591c682a2a5db48a6816d7ff771367015727bec65.

- 2026-09-06T18:18:28+00:00: Recorded command exit 2; command argv SHA-256
  48458d4adcbc2714c4ae60f17ec39d916357031118af6e75d9a5cd826c73f20e.

- 2026-09-06T18:18:45+00:00: Recorded command exit 0; command argv SHA-256
  7fe24a37a4fff4dda1385cc605bddd45b0764b45f525ff66e08933d595560585.

- 2026-09-06T18:19:09+00:00: Recorded command exit 0; command argv SHA-256
  ae95c3777b9ca9735e4612d1493a413626e46daf39a7bf3deb0402c46cdbcd9e.

- 2026-09-06T18:19:34+00:00: Recorded command exit 0; command argv SHA-256
  c99f10ae0ea8b2471b5b8300d4a172ea08cae4cb655aa7e2a800b92993a827c2.

- 2026-09-06T18:19:47+00:00: Recorded command exit 0; command argv SHA-256
  7811855b541ae94b5e74b56d1967090309f0d053216927ca95eb701b59e5389a.

- 2026-09-06T18:19:59+00:00: Recorded command exit 0; command argv SHA-256
  a2fc805ba16b0a6a4e0ae29afc868547f2c8e3725b307d8b6e877c084cf3d3d5.

- 2026-09-06T18:20:04+00:00: Recorded command exit 0; command argv SHA-256
  871918e8f302d26cb0c61dc16fb60bc7e879aff3b92bb6264f0d4e29dbe59381.

- 2026-09-06T18:20:30+00:00: Recorded command exit 0; command argv SHA-256
  bd463739e8f6a75b40567be1d27fa4d69c3ddc7d9200761e525c82ec03ad6dd5.

- 2026-09-06T18:20:54+00:00: Recorded command exit 0; command argv SHA-256
  77472a8bfd7488bf4c0f5a4e765687e0411ca2a7bd020eb668a1bef2add5becb.

- 2026-09-06T18:21:05+00:00: Recorded command exit 0; command argv SHA-256
  a2fc805ba16b0a6a4e0ae29afc868547f2c8e3725b307d8b6e877c084cf3d3d5.

- 2026-09-06T18:21:21+00:00: Recorded command exit 0; command argv SHA-256
  bd463739e8f6a75b40567be1d27fa4d69c3ddc7d9200761e525c82ec03ad6dd5.

- 2026-09-06T18:21:47+00:00: Recorded command exit 0; command argv SHA-256
  a3a17022ff4b5078bb8c880adbc0a63096742b443b6c52188792b6ae0ff8b2f3.

- 2026-09-06T18:22:11+00:00: Recorded command exit 0; command argv SHA-256
  a2fc805ba16b0a6a4e0ae29afc868547f2c8e3725b307d8b6e877c084cf3d3d5.

- 2026-09-06T18:22:40+00:00: Recorded command exit 0; command argv SHA-256
  0d3cb833525ac74d73edb4d3d67e3f6485f28ea6102d91d04de6a092c828c982.

- 2026-09-06T18:22:42+00:00: Heartbeat by contracts-20260906.

- 2026-09-06T18:23:30+00:00: Implemented rootless exact-version-pinned Bubblewrap plus delegated
  systemd cgroup scope and taskset CPU enforcement, fail-closed shared benchmark/CI CPU leases,
  bounded configuration, cancellation/wait/drop cleanup, and real native negative tests. Changed
  conclusions preserved: MemoryMax alone permitted swap so MemorySwapMax=0 is required; systemd
  AllowedCPUs can be accepted but ineffective without delegated cpuset so taskset plus procfs
  verification is required. Ubuntu 24.04.4 x86_64, Linux 7.0.0-28, bubblewrap 0.9.0, systemd
  255.4-1ubuntu8.17, taskset 2.39.3 native suite passed three serial repetitions; every repetition
  proved no remaining ASB scope, sandbox helper process or CPU lease. Coverage is sandbox.rs 95.31%
  regions, 98.66% lines, 100% functions and asb-runtime 95.31% regions, 98.75% lines. Limits:
  Linux/cgroup-v2/user-systemd/userns only; no VM or kernel boundary; exact untested platform
  combinations remain unsupported; formal lease/cancellation proofs remain AR-0901/AR-0905.

- 2026-09-06T18:23:40+00:00: Recorded command exit 0; command argv SHA-256
  1927b2dfe6ce8273c46cacd8182ed398312092532c2f5dc1361c68a7f1c1a41a.

- 2026-09-06T18:24:35+00:00: Recorded command exit 0; command argv SHA-256
  7bb44165adf99f7a8fa0a87faeb8b7cc5f3c944471c3aae80eb48114b4913678.

- 2026-09-06T18:25:06+00:00: Recorded command exit 0; command argv SHA-256
  6b39fe97393ad90334aaf4a892941edd7330d52d80c93761ce0ca7efd61d8db3.

- 2026-09-06T18:25:45+00:00: Recorded command exit 0; command argv SHA-256
  7471017bc3a57fd7f64244eb0970aad261054c602bcd032d632ddd399f524b2d.

- 2026-09-06T18:25:51+00:00: Recorded command exit 0; command argv SHA-256
  ac686db03befa061261a3d10b68a71af2d35ec542a33a86f2cc87d765c6f12e3.

- 2026-09-06T18:27:37+00:00: Recorded command exit 0; command argv SHA-256
  4b098205e5dfa4336a5e14db060a2776e5fb2af394c1f282d241a715a269fa23.

- 2026-09-06T18:28:12+00:00: Recorded command exit 0; command argv SHA-256
  f4e502317f0214a17bc29495c5b14522775782fa2148ffcdf03488c4dc03ddfe.

- 2026-09-06T18:28:26+00:00: Recorded command exit 1; command argv SHA-256
  ade02afecd9ca95a406b9c94803061fa7465d2d06bb84626e4f7317370a473c7.

- 2026-09-06T18:28:47+00:00: Recorded command exit 0; command argv SHA-256
  a2fc805ba16b0a6a4e0ae29afc868547f2c8e3725b307d8b6e877c084cf3d3d5.

- 2026-09-06T18:29:30+00:00: Recorded command exit 101; command argv SHA-256
  afdca5488502d21af7b721249722816f0e86db09e3d484049e8e0480ae3a63bd.

- 2026-09-06T18:30:16+00:00: Recorded command exit 0; command argv SHA-256
  1dde2e9d7eaa577930cd8cf7cb82423b234f0a7b9795b750c474ec1691d296e9.

- 2026-09-06T18:30:29+00:00: Recorded command exit 0; command argv SHA-256
  3833c9511032c7b80f172c5cf214c3e2a2cac66f1ec3853e177476bcec327a05.

- 2026-09-06T18:30:55+00:00: Recorded command exit 0; command argv SHA-256
  a2fc805ba16b0a6a4e0ae29afc868547f2c8e3725b307d8b6e877c084cf3d3d5.

- 2026-09-06T18:31:30+00:00: Recorded command exit 1; command argv SHA-256
  a3deb0bee38b04375dd6da29ca527ce18bf7a37946b8cbf60e7204acaf16f004.

- 2026-09-06T18:31:54+00:00: Recorded command exit 0; command argv SHA-256
  074408b118d2a1cd829d07b854cedfdb0b76550debbfa07221c13d417f0dd1ab.

- 2026-09-06T18:32:36+00:00: Recorded command exit 1; command argv SHA-256
  bb339b2f7f991dcea6cea1b93ebb5528e866f52f99cb2a577fb0ac7aabce7755.

- 2026-09-06T18:33:03+00:00: Recorded command exit 0; command argv SHA-256
  98d890e913ab82c339313783ac1a23cc485939244447ba0a07cb970c032f6ec9.

- 2026-09-06T18:33:33+00:00: Recorded command exit 101; command argv SHA-256
  0ef73b6b3b7323569996183c83362235537048314a632ce19e13cd4543053169.

- 2026-09-06T18:33:55+00:00: Recorded command exit 1; command argv SHA-256
  ddcbd4488c981a582b02e173c3c4d114d9b69224cde0eabf7ba4af440a64e5dd.

- 2026-09-06T18:34:00+00:00: Recorded command exit 5; command argv SHA-256
  dca568f5a2525a3c681afdc8e969b26766c6ce1e0899a5fb9f3a02b1d70b8f84.

- 2026-09-06T18:34:36+00:00: Recorded command exit 0; command argv SHA-256
  d636693d2c037dedac0a9bce5bd9fd9e5d3457e63a4a11bd94ee89f74f4e418a.

- 2026-09-06T18:34:52+00:00: Recorded command exit 0; command argv SHA-256
  a2fc805ba16b0a6a4e0ae29afc868547f2c8e3725b307d8b6e877c084cf3d3d5.

- 2026-09-06T18:34:58+00:00: Recorded command exit 101; command argv SHA-256
  f2d618f4fe8a0c4676060d0615310a8809d64879de7da58847425f81c620d632.

- 2026-09-06T18:35:08+00:00: Recorded command exit 0; command argv SHA-256
  fca90edf8818373d75a6c1b609c2ad7d7dac19578895e0870b932afb459cc636.
