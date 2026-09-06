---
{
  "branch": "feature/sandbox-runtime",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-06T21:45:53+00:00",
  "depends_on": [
    "AR-0102"
  ],
  "id": "AR-0103",
  "next_action": "Await coordinator post-merge local verification; release AR-0103 only after explicit confirmation.",
  "observed_branch": "feature/sandbox-runtime",
  "observed_dirty": 0,
  "observed_head": "4b1cd544437faa102af6909243004f1d2c289430",
  "owner": "contracts-20260906",
  "plan": "../plans/AR-0103.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Isolate untrusted generated code and allocate cgroup/CPU/memory/PID budgets.",
  "task_revision": 289,
  "title": "Implement isolated execution and resource leases",
  "updated_at": "2026-09-06T19:53:42+00:00",
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

- 2026-09-06T18:35:23+00:00: Recorded command exit 0; command argv SHA-256
  14bffd5698f26a9926f1b89c6b32b8f42db1bb727be761561a161648ff3b2c7e.

- 2026-09-06T18:35:37+00:00: Recorded command exit 101; command argv SHA-256
  a30e057d48251b648cabd49f6d8b3d871ef51fa6ca25eb7d0f9233da4fff84c9.

- 2026-09-06T18:35:48+00:00: Recorded command exit 0; command argv SHA-256
  45deebec579cc41bb98004365434c9b0938b87bb5ddea6240ae286ac6f471fd6.

- 2026-09-06T18:36:22+00:00: Recorded command exit 0; command argv SHA-256
  a30e057d48251b648cabd49f6d8b3d871ef51fa6ca25eb7d0f9233da4fff84c9.

- 2026-09-06T18:36:41+00:00: Recorded command exit 0; command argv SHA-256
  bd463739e8f6a75b40567be1d27fa4d69c3ddc7d9200761e525c82ec03ad6dd5.

- 2026-09-06T18:37:43+00:00: Recorded command exit 0; command argv SHA-256
  745d6c4632305874a4c5b3a406044bbbbf2806a6386da6804439e905f2919d19.

- 2026-09-06T18:37:59+00:00: Recorded command exit 0; command argv SHA-256
  a2fc805ba16b0a6a4e0ae29afc868547f2c8e3725b307d8b6e877c084cf3d3d5.

- 2026-09-06T18:38:15+00:00: Recorded command exit 101; command argv SHA-256
  94e164a486450248e63b660dd2ae3c12cceaf3a2c4da21e168ed98454ff2d536.

- 2026-09-06T18:38:44+00:00: Recorded command exit 0; command argv SHA-256
  945ed6b3f8f08a0b66f342a7c5c153d027ba652566a99c157d57f8f2736cb2d5.

- 2026-09-06T18:38:55+00:00: Recorded command exit 0; command argv SHA-256
  0733ae7df401eb4487a17a1d2da8c1c77f2afc25a0935ffda433a207655ce2bd.

- 2026-09-06T18:39:27+00:00: Recorded command exit 101; command argv SHA-256
  28598b5536d990ee29b05027506c114bb081d47cf9273d4ac1cd0c19122c0e8c.

- 2026-09-06T18:39:52+00:00: Recorded command exit 0; command argv SHA-256
  654b69dac1313818924fccd7d883445f3a08ece2678ee2a12e690f9e3549af21.

- 2026-09-06T18:40:12+00:00: Recorded command exit 0; command argv SHA-256
  f4784457dcbad40dd6619d026cda572484a74b1441d021d732458c6a95e7e363.

- 2026-09-06T18:40:57+00:00: Recorded command exit 0; command argv SHA-256
  548eb1e25e4677a525dc1bebdae3c79c435986a30fc4319958a22fa923cd7ae5.

- 2026-09-06T18:41:13+00:00: Recorded command exit 0; command argv SHA-256
  bd463739e8f6a75b40567be1d27fa4d69c3ddc7d9200761e525c82ec03ad6dd5.

- 2026-09-06T18:41:26+00:00: Exact-tree parallel testing exposed an intermittent 30-second cleanup
  delay: systemctl stop entered deactivating/stop-sigterm and waited its long default timeout while
  the sandbox retained inherited pipes. A synchronous stop variant also timed out and once left a
  transient deactivating scope, which was reconciled and disappeared; no process or lease remained.
  Cleanup now verifies unit state, sends cgroup-wide SIGKILL, requests asynchronous collection, and
  polls exact state under a five-second hard bound. Fault tests cover already-inactive, kill/stop
  rejection, completion race, deactivating transition, unknown state, and deadline. Three repeated
  unit suites and three parallel real-native suites then passed in 3-5 seconds each with zero ASB
  scopes/processes/leases. Updated sandbox coverage: 95.46% regions, 98.74% lines, 100% functions;
  asb-runtime 95.43% regions and 98.81% lines.

- 2026-09-06T18:41:48+00:00: Recorded command exit 0; command argv SHA-256
  19d1e1bf18449b54f0e39a98ce15f2b05c67177862d7f502c7e635c9c7665e8a.

- 2026-09-06T18:42:01+00:00: Recorded command exit 0; command argv SHA-256
  741a1d0a356f98f026b3e60aa3d0f08a385c67b20cdf7fde44b24cb50db110dc.

- 2026-09-06T18:42:53+00:00: Recorded command exit 0; command argv SHA-256
  52b68ff606191f6e241f4d325893febff6752cdc298dbcf87d41c3c6f7849bc7.

- 2026-09-06T18:43:05+00:00: Recorded command exit 128; command argv SHA-256
  ca96534b7b25f263c0db2f9f3773016a17ae22c17f60355d10431568944b481b.

- 2026-09-06T18:43:26+00:00: Recorded command exit 0; command argv SHA-256
  321c534968b9c456a64caf5e6d09b63780c507f97548057d2bfe31edcfd73ff4.

- 2026-09-06T18:43:34+00:00: Recorded command exit 0; command argv SHA-256
  b7c438686581cf292b6cd41497ceabb3af42dfed57e04dfd6cc89efed8e2d15b.

- 2026-09-06T18:44:09+00:00: Recorded command exit 0; command argv SHA-256
  321c534968b9c456a64caf5e6d09b63780c507f97548057d2bfe31edcfd73ff4.

- 2026-09-06T18:44:16+00:00: Recorded command exit 0; command argv SHA-256
  e414cd2408857c8dfe9c5e1002d0cfab379645832848c20088f1d8f39c2e7f89.

- 2026-09-06T18:45:15+00:00: Recorded command exit 0; command argv SHA-256
  a45cd45f4fae36ba1e4443f8a91ffef7004f191661a661d835bddf5b31bc059e.

- 2026-09-06T18:45:32+00:00: Recorded command exit 0; command argv SHA-256
  225df1097e7a635be95216dfc336486919202a4221c4128306e6203fd6726298.

- 2026-09-06T18:45:49+00:00: Recorded command exit 0; command argv SHA-256
  517cb574cd20f2d084c6bff13b82c1dfe9f3b54e3e74bf78bde255aad6780a4d.

- 2026-09-06T18:46:22+00:00: Rebased once after serialized integrations onto exact signed product
  main c9e3653; range-diff is unchanged from reviewed local candidate, and new exact signed+DCO head
  is a2ebac54d8ea8d2337b1a73ac3ac4fccfbd4c581. Full exact-tree workspace build/test/doc/coverage,
  real native sandbox suite, dependency audit/deny, analyzers, Gitleaks, commit/repository policy
  and every failure fixture passed; tree clean with zero residual scopes/processes/leases. Published
  PR #10. Hosted exact-head runs 34052743817 and 34052743886 are in progress.

- 2026-09-06T18:47:36+00:00: PR #10 exact head a2ebac54 is merge-clean. Hosted Rust verification run
  34052743817 passed on Ubuntu x86_64 and aarch64, and repository-quality run 34052743886 passed
  policy, coverage and supply-chain checks. Local exact-tree and native evidence remain green and
  tree/residual audits remain clean.

- 2026-09-06T18:51:27+00:00: Recorded command exit 0; command argv SHA-256
  4759a9bda3b6bc3ef52d24855102cf46904dbcd28689d316cb6e7c7e613e0d1f.

- 2026-09-06T18:51:53+00:00: Recorded command exit 0; command argv SHA-256
  cf8fdc6b32549b4269ca30b7e46bd51c678bd3ef59fa34546db410674a698972.

- 2026-09-06T18:52:08+00:00: Recorded command exit 1; command argv SHA-256
  41aad9b7d26d29a12a2fa99654cc19770d0d5844a55cec08119eec7a24d44ee0.

- 2026-09-06T18:52:34+00:00: Recorded command exit 0; command argv SHA-256
  9255c68d844a54af18ca7140eb49fdcedc35951d895b0c3095de9bd2f773840c.

- 2026-09-06T18:52:42+00:00: Recorded command exit 0; command argv SHA-256
  fb1b0a4740e1a0c723fd7e6cc7e1ab0c491af1b1f6703a178a111d7e2ffa0906.

- 2026-09-06T18:53:22+00:00: Recorded command exit 0; command argv SHA-256
  208838086a88108339e7d1b60004877d52e4a448126b8b4bd8b5d022847f2f5f.

- 2026-09-06T18:54:23+00:00: Recorded command exit 2; command argv SHA-256
  69c680b09fe28d1973c616cbdbbff2460e8e22fef6c6adc532dd27746d4aebab.

- 2026-09-06T18:54:33+00:00: Recorded command exit 0; command argv SHA-256
  5e8759fd16f9544882e07ccfd7db810fb1538baa9266c59ccebad8b2278a8214.

- 2026-09-06T18:54:54+00:00: Recorded command exit 2; command argv SHA-256
  eb2704056888212298c01c4e2f33288c80fc77009625f5b35055cbf35719db8d.

- 2026-09-06T18:55:32+00:00: Recorded command exit 0; command argv SHA-256
  8c36207ea22fc281931e80189a4a9514d93eff94ae843e52f9e6f5e1c45fbd88.

- 2026-09-06T18:55:54+00:00: Recorded command exit 0; command argv SHA-256
  94811189b95efedf72384f45d5546c18a2221eaea4996c181e26b8376bb93d76.

- 2026-09-06T18:56:21+00:00: Recorded command exit 0; command argv SHA-256
  f8bbb53b89f434b9dd4bb9ef7b6e7957ac283b7258230224c77b9f75c534a875.

- 2026-09-06T18:56:34+00:00: Recorded command exit 0; command argv SHA-256
  7ac32a6ca82e734a1cd0e7ab6f60e6910ea73385cc92ce5db362fb7bfbcb0643.

- 2026-09-06T18:56:46+00:00: Recorded command exit 0; command argv SHA-256
  eabdd83df5e1e64d3598dec68d2a23ae232ecff89a5e78e7df7c556b8320fcfe.

- 2026-09-06T18:57:18+00:00: Recorded command exit 0; command argv SHA-256
  f261b5dde2907f04877c75bdb4e9c2a02c29d3542145cfaa68ff8fda313f6520.

- 2026-09-06T18:57:29+00:00: Recorded command exit 101; command argv SHA-256
  97a5356c1aa55e992681ade62abdec39396f159104cb841bee24a38897197129.

- 2026-09-06T18:57:42+00:00: Recorded command exit 0; command argv SHA-256
  8e0f70c4d230d80cc0c328370e2a49eabe8247d33bc1e1c0c6f2eca700f6a0ef.

- 2026-09-06T18:57:52+00:00: Recorded command exit 0; command argv SHA-256
  97a5356c1aa55e992681ade62abdec39396f159104cb841bee24a38897197129.

- 2026-09-06T18:58:04+00:00: Recorded command exit 101; command argv SHA-256
  8c66fa22d8b214f214b628c7e3022c3c1d10c10a46a02ee5f72f9e2c2f924423.

- 2026-09-06T18:58:30+00:00: Recorded command exit 0; command argv SHA-256
  79736493b4369f662c38ca9d6c9b7ae4e365079f65f39fd37ffc9b5473715a3d.

- 2026-09-06T18:58:44+00:00: Recorded command exit 0; command argv SHA-256
  8c66fa22d8b214f214b628c7e3022c3c1d10c10a46a02ee5f72f9e2c2f924423.

- 2026-09-06T18:59:28+00:00: Recorded command exit 1; command argv SHA-256
  d96db264810a53723c0e55c00b8950b74244251e76781912bbcf0198c1a311ab.

- 2026-09-06T18:59:50+00:00: Recorded command exit 0; command argv SHA-256
  4b4f331130d5c287bf4c77bfe3956d433d74f13d021486ae30761d2aa4a46d86.

- 2026-09-06T19:00:27+00:00: Recorded command exit 0; command argv SHA-256
  921279a4c7bfc16754759fda6c9d47a6ad1cee4b9d7872a2addac60b2def4b94.

- 2026-09-06T19:01:02+00:00: Recorded command exit 0; command argv SHA-256
  5183bc33d8d5df1a06ddb28380170f6f59543e9908abd3eab246237626c01618.

- 2026-09-06T19:01:17+00:00: Recorded command exit 0; command argv SHA-256
  a2fc805ba16b0a6a4e0ae29afc868547f2c8e3725b307d8b6e877c084cf3d3d5.

- 2026-09-06T19:01:25+00:00: Recorded command exit 101; command argv SHA-256
  ee5c17dd2f2ea23b4d8705d8a4e3be4d2bea4232f269ab8ef02c3a8e54b84d40.

- 2026-09-06T19:01:37+00:00: Recorded command exit 0; command argv SHA-256
  d0cce0218cbcaf08c14619d5c13a7b2e7550dacba65efacc0683bfe0c047d121.

- 2026-09-06T19:01:53+00:00: Recorded command exit 101; command argv SHA-256
  ee5c17dd2f2ea23b4d8705d8a4e3be4d2bea4232f269ab8ef02c3a8e54b84d40.

- 2026-09-06T19:02:06+00:00: Recorded command exit 0; command argv SHA-256
  f5834b7e5ce3253c898a3be6a533b4592fc0c5020c6a8e3079ff45fe2ada3102.

- 2026-09-06T19:02:16+00:00: Recorded command exit 101; command argv SHA-256
  ee5c17dd2f2ea23b4d8705d8a4e3be4d2bea4232f269ab8ef02c3a8e54b84d40.

- 2026-09-06T19:02:46+00:00: Recorded command exit 1; command argv SHA-256
  ba804bc12497e0f37c97af33728d0269b83feb8fa023c339eadb189413bd81a6.

- 2026-09-06T19:03:05+00:00: Recorded command exit 1; command argv SHA-256
  67a4810cac73eb987390e190a8273f6a3e2d4ecce3ae846cb8ce8695623d6ee5.

- 2026-09-06T19:03:22+00:00: Recorded command exit 0; command argv SHA-256
  a55c6637b263cc1966904938b254e35485b53cef85b3028fca49b2394535c2e3.

- 2026-09-06T19:03:38+00:00: Recorded command exit 0; command argv SHA-256
  ee5c17dd2f2ea23b4d8705d8a4e3be4d2bea4232f269ab8ef02c3a8e54b84d40.

- 2026-09-06T19:03:53+00:00: Recorded command exit 101; command argv SHA-256
  1de054fe32846da297c4e0d1d656d4f05ef746bd2f5db2fa7f2767ee4904e889.

- 2026-09-06T19:04:29+00:00: Recorded command exit 0; command argv SHA-256
  bfffaee58a4af3dc6cc0085ff4f2b730ba180a198f3ee497c28caba1937f037c.

- 2026-09-06T19:04:55+00:00: Recorded command exit 1; command argv SHA-256
  ff8278aa573c7a8feaaf1e04ab6ecd0d95bd7d14e46358c08e8ff48e8b754059.

- 2026-09-06T19:05:14+00:00: Recorded command exit 0; command argv SHA-256
  22bf0110de88d471e4b3535c795121e2ac8b580e4bd196cd25e67c6c6e3933c4.

- 2026-09-06T19:05:37+00:00: Recorded command exit 0; command argv SHA-256
  7691d29e30f82e73f38018b71a9f5c9279c2241e460e88bd5515fdb11950df36.

- 2026-09-06T19:05:47+00:00: Recorded command exit 0; command argv SHA-256
  1de054fe32846da297c4e0d1d656d4f05ef746bd2f5db2fa7f2767ee4904e889.

- 2026-09-06T19:06:07+00:00: Recorded command exit 0; command argv SHA-256
  a6f95538fa18d6a0c7056fc2920dc7db5aa386b07f26e670e0f8e0d05da857af.

- 2026-09-06T19:06:23+00:00: Recorded command exit 0; command argv SHA-256
  c62d4e8df036b75b6d9df8680320b6e44ad1d482bf042cfb0289f34f9fb3768f.

- 2026-09-06T19:06:41+00:00: Recorded command exit 1; command argv SHA-256
  79096114e549553ddb8a572c61b0f87e441a17a5f6b232e8f6225d8a07691709.

- 2026-09-06T19:06:57+00:00: Recorded command exit 0; command argv SHA-256
  a2fc805ba16b0a6a4e0ae29afc868547f2c8e3725b307d8b6e877c084cf3d3d5.

- 2026-09-06T19:07:20+00:00: Recorded command exit 0; command argv SHA-256
  afd7fbb1a9b405f581b834d63b77db3202a888f2423f9b9003a877ef5e866aa1.

- 2026-09-06T19:07:44+00:00: Recorded command exit 0; command argv SHA-256
  f56e5622715ccd2b7a52f45db17cf1facbd0740f832958b8e9366dc5895d2d63.

- 2026-09-06T19:08:44+00:00: Recorded command exit 0; command argv SHA-256
  a2fc805ba16b0a6a4e0ae29afc868547f2c8e3725b307d8b6e877c084cf3d3d5.

- 2026-09-06T19:09:19+00:00: Recorded command exit 0; command argv SHA-256
  fe6f885d798a9e1428b0a30b7406e6ee2a1861e373faaac422522e49015872bf.

- 2026-09-06T19:09:36+00:00: Recorded command exit 0; command argv SHA-256
  7a6a6f1e7deafb979dc0f8bc93504754686aeec8de024b8212676bff1d8c149d.

- 2026-09-06T19:09:48+00:00: Recorded command exit 0; command argv SHA-256
  e056cb3be56302ea866c6d82a809d00852b665ce6ca9dd5af125459bd52501d4.

- 2026-09-06T19:10:08+00:00: Recorded command exit 101; command argv SHA-256
  192d118f35668818f8a863b292f2996939f39ed775b572499b0562a61eb82069.

- 2026-09-06T19:10:40+00:00: Recorded command exit 2; command argv SHA-256
  48458d4adcbc2714c4ae60f17ec39d916357031118af6e75d9a5cd826c73f20e.

- 2026-09-06T19:10:53+00:00: Recorded command exit 0; command argv SHA-256
  27d769b70455db626ad3a9cd558ceff05faa5b4a83f3628ef4601671c04abd06.

- 2026-09-06T19:11:05+00:00: Recorded command exit 0; command argv SHA-256
  2b8c309ab58380dcefa705ace65dc2b97eaba2c273c3a1ff9047938e1dd3ee6e.

- 2026-09-06T19:11:34+00:00: Recorded command exit 92; command argv SHA-256
  9339ba719f083db80a32e8c5e418277f780ebb54f9474735f1be431908cc8c0a.

- 2026-09-06T19:12:06+00:00: Recorded command exit 101; command argv SHA-256
  7902bb70fe1dfbd5f1873f57eb3fd396e222a70d8352d43810f606ac0a5e4b85.

- 2026-09-06T19:12:37+00:00: Recorded command exit 0; command argv SHA-256
  765e56798b6675e4a6f860185382592d0b84645f97a0dbcb1c0b9cf00d91115e.

- 2026-09-06T19:12:58+00:00: Recorded command exit 0; command argv SHA-256
  7647983d4c166df34eedbde56b0ca439cfb7a5953a74affe00ec9c53a3bbe54c.

- 2026-09-06T19:13:27+00:00: Recorded command exit 93; command argv SHA-256
  53b6255b4b27bf285d58220b30de0c6509936daf704a8ebac2f63fb03d0b6297.

- 2026-09-06T19:13:43+00:00: Recorded command exit 0; command argv SHA-256
  e26cf188748889761963d770532bede20a9071ed40e7c34af93c87659c1e8523.

- 2026-09-06T19:14:23+00:00: Recorded command exit 0; command argv SHA-256
  7902bb70fe1dfbd5f1873f57eb3fd396e222a70d8352d43810f606ac0a5e4b85.

- 2026-09-06T19:14:40+00:00: Recorded command exit 0; command argv SHA-256
  a3e7e26db9609c1e8fbde2057bf156ba4a9ebaca12bb2c3256c454816e581f1b.

- 2026-09-06T19:15:19+00:00: Recorded command exit 0; command argv SHA-256
  ca054bc4b46224982c0c43e9b05410256090c78895fb951f25903bf97017f987.

- 2026-09-06T19:15:42+00:00: Recorded command exit 0; command argv SHA-256
  63be9581689ce7f5b9961b8ea9cf99a241b26a02ccb26576632aac806d9b4d3a.

- 2026-09-06T19:15:59+00:00: Recorded command exit 0; command argv SHA-256
  f31d4a10bb87d6993e4773ce3b96299f41b36201637e5a648dbb2a5ab21df07d.

- 2026-09-06T19:16:26+00:00: Recorded command exit 0; command argv SHA-256
  633db4ddee8fd97e2f48af5543d7084f31c64292e40e4feb084f7d578d5f0dce.

- 2026-09-06T19:16:42+00:00: Recorded command exit 101; command argv SHA-256
  b514df4057efc0edca0bb6e4dd0c7bbb9ff921a244feaddf215ed70c0bdc449b.

- 2026-09-06T19:16:54+00:00: Recorded command exit 0; command argv SHA-256
  2227ed8540cff63b3768094ad039880aab48dd319a652bed6b07d6f7371fd7f9.

- 2026-09-06T19:17:17+00:00: Recorded command exit 0; command argv SHA-256
  b514df4057efc0edca0bb6e4dd0c7bbb9ff921a244feaddf215ed70c0bdc449b.

- 2026-09-06T19:17:39+00:00: Recorded command exit 0; command argv SHA-256
  c979f4c289b7f0a1556af768819600a407f2562267672b212f5b609a47bb11e2.

- 2026-09-06T19:18:04+00:00: Recorded command exit 0; command argv SHA-256
  7471017bc3a57fd7f64244eb0970aad261054c602bcd032d632ddd399f524b2d.

- 2026-09-06T19:18:14+00:00: Recorded command exit 0; command argv SHA-256
  bb6089725e500f48abd6a6acb2b7139172f0f7914f26a0212c9e575d5a5c4c42.

- 2026-09-06T19:18:48+00:00: Recorded command exit 101; command argv SHA-256
  0f0480a44f628265997528f8d97054c497b9b7c505b076c54f5f43bad99be6d0.

- 2026-09-06T19:19:49+00:00: Independent review blockers repaired at signed+DCO 832e72c: internal
  kernel-random scope IDs; reserved nonce proven inside the exact cgroup before returning; live
  harmless pre-existing-scope collision proves unrelated scope is never stopped; unproven ownership
  and cleanup uncertainty conservatively retain leases; Drop retries cleanup after terminal leader;
  deterministic and real descendant tests prove retry and zero residuals. A short-process ownership
  race and timeout cancellation/reap gap were discovered and fixed. Three serialized full
  native/unit repetitions passed with zero residual scopes/helpers/leases. Coverage now sandbox.rs
  95.05% regions and 97.54% lines, workspace runtime coverage 95.15% regions and 97.89% lines. Full
  workspace gate then hit one intermittent ETXTBSY executing a fresh fake systemctl fixture; focused
  fixture test subsequently passed 20 repetitions. One focused diagnostic repetition command was
  mistakenly invoked without handoffctl; it changed no source or Git state, only the existing
  worktree target cache. Root Cargo files remain untouched.

- 2026-09-06T19:19:56+00:00: Heartbeat by contracts-20260906.

- 2026-09-06T19:20:56+00:00: Recorded command exit 0; command argv SHA-256
  0f0480a44f628265997528f8d97054c497b9b7c505b076c54f5f43bad99be6d0.

- 2026-09-06T19:21:16+00:00: Recorded command exit 0; command argv SHA-256
  457f007c86d4ee2a0334e98450e733a8b1c48d3a4f695080f47f295ec1789130.

- 2026-09-06T19:21:42+00:00: Repair head 832e72c pushed to PR #10 after complete exact-tree gates
  passed: formatting, workspace Clippy/tests/docs/release, Cargo Deny/Audit, coverage, actionlint,
  zizmor, Gitleaks, repository policy and all failure fixtures. Post-gate tree clean with zero ASB
  scopes, sandbox helpers or lease files. Hosted exact-head runs 34054628751 and 34054628754
  started. Product main advanced independently; branch was not rewritten.

- 2026-09-06T19:23:05+00:00: Recorded command exit 0; command argv SHA-256
  48d74de6bff5025062d89d34a3bb4d061e3d7abc15f3c0a14131e1272a73dd1a.

- 2026-09-06T19:23:19+00:00: Recorded command exit 0; command argv SHA-256
  7b84ebfe4e16aa743c40930b40362a710e8ecf0e4ec4d5f2d473d957a8948443.

- 2026-09-06T19:23:32+00:00: Recorded command exit 0; command argv SHA-256
  1796c4cb83421457af48e43c6d4d3c82dad736a2b74834c173e1d330d7e5d7b3.

- 2026-09-06T19:23:47+00:00: Recorded command exit 0; command argv SHA-256
  c4e283e07fb6d4b73bce5ba12d27b5302f78149cbaa633cd71a4d13d8b0b537d.

- 2026-09-06T19:24:06+00:00: Recorded command exit 101; command argv SHA-256
  0f0480a44f628265997528f8d97054c497b9b7c505b076c54f5f43bad99be6d0.

- 2026-09-06T19:24:35+00:00: Recorded command exit 0; command argv SHA-256
  5ebd61b12b9a1be00f62c37a8a3c2cf9713b9308a7924f8c171069663cb8f539.

- 2026-09-06T19:24:58+00:00: Recorded command exit 101; command argv SHA-256
  b05067a7f24cef8fbd1870e470964c209dc71764d57987de86683ec9cefdd681.

- 2026-09-06T19:25:28+00:00: Recorded command exit 0; command argv SHA-256
  013844d66b9b9cabb0161b1edc35234edcf79261991fcc30de5bfc567ce4f4ab.

- 2026-09-06T19:25:43+00:00: Recorded command exit 0; command argv SHA-256
  a9b0d394d2fb67dbea0c3418deed6fe7cd743fca9e8633354b69372e24241105.

- 2026-09-06T19:25:56+00:00: Recorded command exit 101; command argv SHA-256
  4420b71f42177a6c2a4d333707414c1400d60963efa5092c60810d2dd479e881.

- 2026-09-06T19:26:53+00:00: Recorded command exit 0; command argv SHA-256
  6a77a738d571fe5a40fce5f32c971861c0b06925d03a1eefd3a12b2f9d21c5ef.

- 2026-09-06T19:27:28+00:00: Recorded command exit 0; command argv SHA-256
  7f5d82bcf6c1827179fdff9c0dcc1db3e5af6d229537fd020e7cb5633bb5c5be.

- 2026-09-06T19:27:48+00:00: Recorded command exit 0; command argv SHA-256
  19d1e1bf18449b54f0e39a98ce15f2b05c67177862d7f502c7e635c9c7665e8a.

- 2026-09-06T19:27:57+00:00: Recorded command exit 0; command argv SHA-256
  9f48cbb8ccbc25374f8382949dd55e998f82d42f3737ddcdc7cbd0bd7345f58f.

- 2026-09-06T19:28:23+00:00: Recorded command exit 1; command argv SHA-256
  0f0480a44f628265997528f8d97054c497b9b7c505b076c54f5f43bad99be6d0.

- 2026-09-06T19:29:14+00:00: Recorded command exit 0; command argv SHA-256
  b4c5718b846a7850629aa06cafb8c9d94d714e99efcdb0cc853688c178975532.

- 2026-09-06T19:29:35+00:00: Recorded command exit 0; command argv SHA-256
  a70e7d4a535956b94b277aaf875f31169f8362fd1c1f159ed4c4be6c575e071b.

- 2026-09-06T19:30:32+00:00: Recorded command exit 0; command argv SHA-256
  75e3191e9490cbad0148964024a03de7da9069949fad7a2cf12d4e41247edade.

- 2026-09-06T19:30:43+00:00: Recorded command exit 0; command argv SHA-256
  19d1e1bf18449b54f0e39a98ce15f2b05c67177862d7f502c7e635c9c7665e8a.

- 2026-09-06T19:30:53+00:00: Recorded command exit 0; command argv SHA-256
  3f0217f2bdef72542d2e70daca011c92b911aff6985fa8fa1635e2e5159a3fc4.

- 2026-09-06T19:31:51+00:00: Recorded command exit 0; command argv SHA-256
  0f0480a44f628265997528f8d97054c497b9b7c505b076c54f5f43bad99be6d0.

- 2026-09-06T19:32:18+00:00: Recorded command exit 0; command argv SHA-256
  457f007c86d4ee2a0334e98450e733a8b1c48d3a4f695080f47f295ec1789130.

- 2026-09-06T19:32:51+00:00: Hosted runs for 832e72c failed because the real cleanup-retry test
  unconditionally pinned Bubblewrap on disposable runners where that native capability is absent.
  Focused signed+DCO e15e3a1 now gates only that native test on the exact toolchain. Local parallel
  tests also exposed intermittent ETXTBSY from concurrently executed generated fake scripts;
  signed+DCO 2987a9f and 7e764d8 atomically publish and serialize fake tools and preserve exact
  diagnostics. Ten parallel unit repetitions, three instrumented coverage repetitions, full
  exact-tree gates and native checks passed. Exact PR head 7e764d8 is published; runs 34055198296
  and 34055198399 are in progress. Remote main is 1621103; branch not rebased or merged.

- 2026-09-06T19:34:24+00:00: Recorded command exit 0; command argv SHA-256
  c753019cc3092abed903573f04c9697c90978405426e0acbb6a95c552d8cdb60.

- 2026-09-06T19:35:30+00:00: Recorded command exit 0; command argv SHA-256
  564802aa6c78190c29e2416ff6f9337112e9057ad57d2a70d4ced9f44d73f455.

- 2026-09-06T19:35:37+00:00: Heartbeat by contracts-20260906.

- 2026-09-06T19:36:03+00:00: Recorded command exit 0; command argv SHA-256
  19d1e1bf18449b54f0e39a98ce15f2b05c67177862d7f502c7e635c9c7665e8a.

- 2026-09-06T19:36:14+00:00: Recorded command exit 0; command argv SHA-256
  f49fbbd82f916fd1a6618d4bcf0fa3fbed2d8cf9f32e6027076ec9cd891e1afb.

- 2026-09-06T19:37:18+00:00: Recorded command exit 0; command argv SHA-256
  0f0480a44f628265997528f8d97054c497b9b7c505b076c54f5f43bad99be6d0.

- 2026-09-06T19:37:46+00:00: Recorded command exit 0; command argv SHA-256
  457f007c86d4ee2a0334e98450e733a8b1c48d3a4f695080f47f295ec1789130.

- 2026-09-06T19:38:04+00:00: Failed 7e764d8 policy run 34055198399 confirmed ETXTBSY arose only from
  direct execution of generated fake systemctl scripts under hosted coverage; both Rust jobs were
  green. Changed conclusion: serialization and atomic rename alone were insufficient on the hosted
  filesystem. Signed+DCO cf43bac uses a cfg(test)-only ToolPin interpreter path so fake scripts are
  read by immutable /bin/sh; production, integration and release pins remain direct. Five
  consecutive instrumented runtime runs and the complete exact-tree suite passed locally; sandbox.rs
  coverage is 95.15% regions and 97.55% lines. Clean tree, zero residual scopes/leases. Exact-head
  runs 34055485257 and 34055485275 started.

- 2026-09-06T19:39:35+00:00: Exact-head hosted CI is green for cf43bac: Rust x86_64 and aarch64 run
  34055485257 succeeded; policy, coverage and supply chain run 34055485275 succeeded. Local/remote
  feature head match, tree is clean, signatures and DCO verified, and product main remains 1621103.
  Await independent review.

- 2026-09-06T19:40:59+00:00: Recorded command exit 0; command argv SHA-256
  7b319a699773bac8fa1a39289cda54ce01f007a9053cfa3f532fe4cab74b8939.

- 2026-09-06T19:42:44+00:00: Recorded command exit 0; command argv SHA-256
  c95a6e5c04cd95c8aaa6e7ffe0f6028906732832e64146c1ed91cac9dd64c3c0.

- 2026-09-06T19:43:05+00:00: Recorded command exit 0; command argv SHA-256
  344f669c82c2b517cf9b6904d03ee035f98b028fb6e4828e4852e6ef4fddebd1.

- 2026-09-06T19:43:37+00:00: Coordinator-authorized single rebase onto exact product main
  162110386605a83f963758a07d83e77e2566528a produced signed+DCO head
  d8601c22982f634808826da01030e3c09733ee59. Range-diff shows all six commits exactly equal to the
  independently reviewed pre-rebase chain. Full exact-tree local gates passed: fmt, workspace
  Clippy/tests/docs/release, three real serialized sandbox native repetitions with zero ASB scopes
  and lease files after each, Cargo Deny/Audit, coverage, actionlint, zizmor, Gitleaks, repository
  policy and every failure fixture. Scope remains exactly four asb-runtime docs/source/test paths.
  Force-with-lease against exact cf43bac succeeded; local and remote feature heads now d8601c2.
  Await fresh hosted CI; no merge/release.

- 2026-09-06T19:44:50+00:00: Fresh exact-head hosted CI is fully green for rebased PR #10 at
  d8601c22982f634808826da01030e3c09733ee59 on exact base 162110386605a83f963758a07d83e77e2566528a:
  Rust verification run 34055764006 passed on disposable Ubuntu x86_64 and aarch64 jobs; repository
  quality run 34055764091 passed policy, signatures/DCO, secrets, supply-chain, coverage, negative
  fixtures, platform validation and clean-tree checks. PR remains OPEN and MERGEABLE; local/remote
  feature head exact and clean. Await coordinator approval; no merge/release.

- 2026-09-06T19:45:40+00:00: Recorded command exit 0; command argv SHA-256
  1e440ac9b38942af142121a48437e23c4c00a2a4702871a36fed5117b598a3ec.

- 2026-09-06T19:45:53+00:00: Heartbeat by contracts-20260906.

- 2026-09-06T19:46:02+00:00: Recorded command exit 1; command argv SHA-256
  62db78d364113bb91700c6fe4f74836c4fb831ff08c68da8956afb0bf8fa4e77.

- 2026-09-06T19:46:27+00:00: Recorded command exit 101; command argv SHA-256
  8ddb54febb35f3cf4263635937b10e96d260e228b20acc61b7d0d29b71d53ec3.

- 2026-09-06T19:46:39+00:00: Recorded command exit 0; command argv SHA-256
  c79a731ffe2f03e0237062cbf5c8fa21fb8b389171a16e3c0cd7e1436dab0a50.

- 2026-09-06T19:47:11+00:00: Recorded command exit 101; command argv SHA-256
  8ddb54febb35f3cf4263635937b10e96d260e228b20acc61b7d0d29b71d53ec3.

- 2026-09-06T19:47:29+00:00: PR #10 is MERGED with exact merge
  4d716973f483f0d6387798496302180a246140b6. Remote main resolves exactly to 4d71697; merge parents
  are exact prior main 1621103 and reviewed feature d8601c2, with Martin Beck author/committer and
  exact Signed-off-by trailer plus SSH signature payload (GitHub reports unknown_key as expected for
  the repository-local allowed-signers boundary). Exact-main hosted Rust run 34055890354 passed
  x86_64 and aarch64; repository quality run 34055890362 passed. Lease renewed. Await coordinator
  post-merge local checks; do not release yet.

- 2026-09-06T19:47:52+00:00: Recorded command exit 0; command argv SHA-256
  321c534968b9c456a64caf5e6d09b63780c507f97548057d2bfe31edcfd73ff4.

- 2026-09-06T19:48:05+00:00: Recorded command exit 0; command argv SHA-256
  06e029a4f2672f3276bd02eb28ca8fe92976bc52c4ad022cae0791e5abafed72.

- 2026-09-06T19:49:08+00:00: Recorded command exit 2; command argv SHA-256
  48458d4adcbc2714c4ae60f17ec39d916357031118af6e75d9a5cd826c73f20e.

- 2026-09-06T19:49:54+00:00: Recorded command exit 0; command argv SHA-256
  f50425f8c672c1713bb62c4f616952e7f4b5123b5970597bbd60382fc573739d.

- 2026-09-06T19:50:06+00:00: Recorded command exit 1; command argv SHA-256
  4a4200ba78a3f26b917ccd918aa764f757dd270f0bd45d242e8cc4a4f06ed177.

- 2026-09-06T19:50:25+00:00: Recorded command exit 0; command argv SHA-256
  30c35d074ebd225da053438dfdc954dd08fbae16484afe2aecea0044739b02de.

- 2026-09-06T19:51:04+00:00: Recorded command exit 0; command argv SHA-256
  e3804c51d24d39292c280d2ae46ec35024ead2acbe96ac86c58be68e6d125a05.

- 2026-09-06T19:52:27+00:00: Recorded command exit 1; command argv SHA-256
  9dd09a11372cde5585273563dc9c0f942de625231782e064fce50419ad9f81ff.

- 2026-09-06T19:52:53+00:00: Recorded command exit 0; command argv SHA-256
  2afd6e75dce873ef4833ef8b9d513063eae1ba6992028c976a0542db2565917b.

- 2026-09-06T19:53:06+00:00: Recorded command exit 1; command argv SHA-256
  fc396fa757f48f5b095d23a5f769bdb38642d0043827c62854911b63f166f7df.

- 2026-09-06T19:53:19+00:00: Recorded command exit 0; command argv SHA-256
  6dfc4edb916b78d1cad0915df03c4546202474560f8b7e3b9052c321a0021c13.
