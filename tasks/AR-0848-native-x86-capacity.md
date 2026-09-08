---
{
  "branch": "feature/native-x86-capacity",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-0701",
    "AR-0103",
    "AR-0201",
    "AR-0401"
  ],
  "id": "AR-0848",
  "next_action": "Await fresh independent immutable review of rebased signed head 45604cd323c5de0ab9c7eaf0b6a39d90f4d43002 on exact product main f42645dd05f17eca5635ca2e82057b703a03a1c3; only then update PR #58 by exact force-with-lease and require fresh exact-head CI.",
  "observed_branch": "feature/native-x86-capacity",
  "observed_dirty": 0,
  "observed_head": "45604cd323c5de0ab9c7eaf0b6a39d90f4d43002",
  "owner": "",
  "plan": "../plans/AR-0848.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "done",
  "summary": "Qualify authorized disposable native x86_64 capacity on a development host.",
  "task_revision": 89,
  "title": "Qualify native x86 capacity",
  "updated_at": "2026-09-08T01:52:11+00:00",
  "worktree_key": "agent-systems-benchmark-native-x86-capacity"
}
---
## AR-0848

Qualify the explicitly authorized development-host native x86_64 cell for ASB workloads. Record
host/distribution/kernel identity, disposable isolation and cleanup, runner provenance,
privacy-safe evidence, and bounded cost/availability. This AR is x86_64-only and must not
claim native aarch64 support; native aarch64 remains future work requiring separate capacity.

- 2026-09-07T23:11:04+00:00: Dependencies AR-0701, AR-0103, AR-0201 and AR-0401 are durably done.
  User explicitly authorized existing development-host native x86_64 capacity while deferring native
  aarch64. Declared branch/worktree are absent; native capacity evidence scope is disjoint from
  active replay conformance, frontend protocol, and recovery-model work.

- 2026-09-07T23:11:06+00:00: Claimed by quality_20260906.

- 2026-09-07T23:12:08+00:00: Recorded command exit 0; command argv SHA-256
  9889eb589d2dd928e231a4723c2bf37164066fcf7d45793c8ad8a8e3c731a626.

- 2026-09-07T23:14:43+00:00: Recorded command exit 0; command argv SHA-256
  089d20c2461efe9d909622f5fca75b2cd39e26d629f2fe4bf8d6bed41d180db5.

- 2026-09-07T23:17:15+00:00: Sanitized native audit observed bare-metal x86_64 Ubuntu 24.04 with
  kernel 7.0.0-28-generic, cgroup v2, CPU/memory/I/O PSI, user systemd, AppArmor registration,
  bubblewrap/systemd-run/taskset, 32 online CPUs, 125 GiB memory and sufficient second-drive
  storage. Source is clean exact 72dd78f/tree 6766ab7. Persistent trusted-runner dispatch remains
  outside this AR because its three-principal container boundary is separately blocked; AR-0848 will
  use a local expiring lease and disposable root and will publish no host identity, credentials, raw
  logs, or performance claim.

- 2026-09-07T23:18:03+00:00: Recorded command exit 0; command argv SHA-256
  0dce05c69bca61592080b15cbf2b6b201b5f9115a295ccb98ee7fdcf8022f24b.

- 2026-09-07T23:18:43+00:00: Recorded command exit 0; command argv SHA-256
  6fd85c2ca89db316367eb6a1637a0fe2ede80b097c8dcd74657babbab64ea03f.

- 2026-09-07T23:26:35+00:00: Recorded command exit 0; command argv SHA-256
  99f3bfc12bd5762f877a7881c32265d78073a2571c89518646e77419d2e3cf88.

- 2026-09-07T23:26:52+00:00: Recorded command exit 1; command argv SHA-256
  fedd184e4c804f81ed004c6b3a4732f64e6791a58b4ea35e10256fdf6e91c9ec.

- 2026-09-07T23:27:04+00:00: Recorded command exit 0; command argv SHA-256
  86a1be19555d3b6d1e4ce72830d22b5c13761a80a32c5e2d854ecfc5036cf7c8.

- 2026-09-07T23:27:18+00:00: Recorded command exit 1; command argv SHA-256
  fedd184e4c804f81ed004c6b3a4732f64e6791a58b4ea35e10256fdf6e91c9ec.

- 2026-09-07T23:27:45+00:00: Recorded command exit 0; command argv SHA-256
  171e9cec64106fb1d0dce322cabdf3c3ec6c5829ea1ab2dd5195142e99d4cb5b.

- 2026-09-07T23:27:58+00:00: Recorded command exit 1; command argv SHA-256
  fedd184e4c804f81ed004c6b3a4732f64e6791a58b4ea35e10256fdf6e91c9ec.

- 2026-09-07T23:28:10+00:00: Recorded command exit 1; command argv SHA-256
  a02a0831e722417d3d723cc6ba332e204ddf019b300e6370395527dd5ddd7923.

- 2026-09-07T23:28:21+00:00: Recorded command exit 1; command argv SHA-256
  7f83269efbf7ac82423d93820495c03aa299ae5982921c0849ffe3b01a3ac887.

- 2026-09-07T23:28:36+00:00: Recorded command exit 0; command argv SHA-256
  43bb285505d1fe82808dc99c1a3dcef1ddb19adacacfd3756ec1b335f1430733.

- 2026-09-07T23:28:52+00:00: Recorded command exit 1; command argv SHA-256
  75a10970d346b359d5e7cd404a28ca32d37bb47107f5299807c3441f3423bc53.

- 2026-09-07T23:29:11+00:00: Recorded command exit 0; command argv SHA-256
  487a550ccd445037a87ed1799d27a99392fbbf8ae444cda1b8a74d6bb51ac92a.

- 2026-09-07T23:29:31+00:00: Recorded command exit 0; command argv SHA-256
  75a10970d346b359d5e7cd404a28ca32d37bb47107f5299807c3441f3423bc53.

- 2026-09-07T23:30:51+00:00: Recorded command exit 0; command argv SHA-256
  a22f3d06d4125c5b9c7c3000c22c33953ccf7cb959494f43969cf8920136e87e.

- 2026-09-07T23:32:40+00:00: Recorded command exit 0; command argv SHA-256
  5ef70c4669539674becbc8db2d072824472317ee8e7b07b65bee4b281f95d92d.

- 2026-09-07T23:32:55+00:00: Recorded command exit 0; command argv SHA-256
  bd56fdef821d985a135d6a425eb1158fac95863f6944f4fac3288e58b462e94b.

- 2026-09-07T23:33:32+00:00: Recorded command exit 0; command argv SHA-256
  251a47e3a0c819b209eb49b46d05cdbdd852457be315869a51d6fc0049089344.

- 2026-09-07T23:34:17+00:00: Recorded command exit 0; command argv SHA-256
  34ca6e7161f9a902f60edcee6c6fc175dec6674d02d7fff81512f99c8aba8ed8.

- 2026-09-07T23:36:20+00:00: Recorded command exit 1; command argv SHA-256
  a67b6bfc0e3880903153072a7fd08a3c4bedc8db75f832df1fc18de6e1481a7a.

- 2026-09-07T23:37:18+00:00: Recorded command exit 0; command argv SHA-256
  fb139aee50cf5cdbdc97e30cbd24ca0d3c04c6320a7cd2556b66807718dabc73.

- 2026-09-07T23:37:34+00:00: Recorded command exit 0; command argv SHA-256
  bd56fdef821d985a135d6a425eb1158fac95863f6944f4fac3288e58b462e94b.

- 2026-09-07T23:37:54+00:00: Recorded command exit 0; command argv SHA-256
  c8712625d1f4206d28282e27f2251e33052fd01cc7a7861ec0179be71d7e57d1.

- 2026-09-07T23:38:08+00:00: Recorded command exit 0; command argv SHA-256
  9f7db6836462c4d8156f7a403483650c589fbfb5265833598462ead6f52a538e.

- 2026-09-07T23:40:07+00:00: Recorded command exit 1; command argv SHA-256
  078ee78ef7742a2c5ff5087c198dbc563af02ce6654ba62af9b0fd8ece95c157.

- 2026-09-07T23:40:51+00:00: Recorded command exit 1; command argv SHA-256
  df6247fe2e7b5dc10607d183db423b15b360dc742fa10c32d70ee722801cd6c1.

- 2026-09-07T23:41:27+00:00: Recorded command exit 0; command argv SHA-256
  edc6f0ebea97747fa3dfa8396bf4249c20d89195ed2fe17b826e61a0d45f46a7.

- 2026-09-07T23:41:48+00:00: Recorded command exit 0; command argv SHA-256
  f594dd2229ff59168cc936dc41318605c8acb1613457e84105b632abf97d250e.

- 2026-09-07T23:42:12+00:00: Recorded command exit 0; command argv SHA-256
  14a7bb65793d3d24a807972eadacc4bcb27f2cbcf2e2048e23cfb32d8bdce96f.

- 2026-09-07T23:42:37+00:00: Recorded command exit 0; command argv SHA-256
  3e0612fa6b760ba66823a9fdecd216dff1db848ac9497633f9f9cf16728681a2.

- 2026-09-07T23:43:15+00:00: Recorded command exit 0; command argv SHA-256
  5516170a3e9b98d5cc853b0c546e0e4b17feb090c90da86fa7800c4b2efa8bd8.

- 2026-09-07T23:43:30+00:00: Recorded command exit 0; command argv SHA-256
  bd56fdef821d985a135d6a425eb1158fac95863f6944f4fac3288e58b462e94b.

- 2026-09-07T23:43:48+00:00: Recorded command exit 1; command argv SHA-256
  01f05ef2157c1c7f04d6a3af4797f49ebf9c12eb78b1104dfe2e4ca25fdbe743.

- 2026-09-07T23:44:07+00:00: Recorded command exit 1; command argv SHA-256
  1fbe8926204b94ed028b52d11cdbb82a3b05f906279228255f5dcf08942c7908.

- 2026-09-07T23:45:40+00:00: Recorded command exit 1; command argv SHA-256
  bd56fdef821d985a135d6a425eb1158fac95863f6944f4fac3288e58b462e94b.

- 2026-09-07T23:46:06+00:00: Recorded command exit 0; command argv SHA-256
  8174ad9da784f01ae1bebdd28e8fab42edf3906e2fc18b2fa2990c0e511799d8.

- 2026-09-07T23:48:25+00:00: Recorded command exit 0; command argv SHA-256
  6e1d5fa80d8068b418d224fae2208826f6aaa0eec170829bc69d86e6331bbb77.

- 2026-09-07T23:48:59+00:00: Recorded command exit 0; command argv SHA-256
  59a457be3bd486882eb9bbce728682443d9347d230c79d2aa3d0460aa0bebf68.

- 2026-09-07T23:50:31+00:00: Recorded command exit 0; command argv SHA-256
  8c45c4411f4131dcddc239cbff3bfe4a4bed8f807b1496114acdddc1429e2443.

- 2026-09-07T23:50:59+00:00: Recorded command exit 0; command argv SHA-256
  38baae9f20f64c0c912de291cb90d5c986c33806342cd07cf2d556d6f465ab6a.

- 2026-09-07T23:51:15+00:00: Recorded command exit 0; command argv SHA-256
  c0870f2b7e5670ff9666c441e957bfd35b12405db9897692868cc92c8a131da4.

- 2026-09-07T23:51:33+00:00: Recorded command exit 0; command argv SHA-256
  59d820d0dcf5bb167b1893d1e304464c661bf3f62508a92b01d25dae98c3a907.

- 2026-09-07T23:52:09+00:00: Recorded command exit 1; command argv SHA-256
  5971010d640a05aa2c2eaf7e36c159898c932a832ad2519c8632b055173777c0.

- 2026-09-07T23:53:00+00:00: Recorded command exit 0; command argv SHA-256
  91024aafcfaf088deb82657ca2b15d155be88e8c213d2125331ae20ce25907f2.

- 2026-09-07T23:53:33+00:00: Recorded command exit 0; command argv SHA-256
  d438e5529aab2148d9e3fdb1b2bfa94b2e14a7ec0e0be264f5f708a4c6bf7cf2.

- 2026-09-07T23:53:59+00:00: Recorded command exit 0; command argv SHA-256
  273c31e89ca0db7b4dff0358f239c35c05e759d33dc8cbf419973fa70f3c0d88.

- 2026-09-07T23:56:08+00:00: Recorded command exit 0; command argv SHA-256
  e95a0cd09f32a47d357714582ba9906d18d4ce538949f9b6e28de6f1c404d6f7.

- 2026-09-07T23:56:25+00:00: Recorded command exit 0; command argv SHA-256
  c0870f2b7e5670ff9666c441e957bfd35b12405db9897692868cc92c8a131da4.

- 2026-09-07T23:56:40+00:00: Recorded command exit 0; command argv SHA-256
  03617af692f27e78126bf0f24568b05e75f8aabfb1ada34441331bac7f12a0a9.

- 2026-09-07T23:57:33+00:00: Recorded command exit 0; command argv SHA-256
  07a90110ae835a1afc5461db548b1fda423ea25ef978143761285b839b7b4d72.

- 2026-09-07T23:58:33+00:00: Recorded command exit 0; command argv SHA-256
  533741b83455be3216be27927f7b15f88b5e8d5d21942892a60a06685055ed6a.

- 2026-09-07T23:58:51+00:00: Recorded command exit 0; command argv SHA-256
  5dfc99bc80f00d819bba75627d01808202716ffdc3c0597dbadab06f29f34197.

- 2026-09-07T23:59:24+00:00: Recorded command exit 0; command argv SHA-256
  b86491ff1c6debe2a8d238bb774db6796b53a04a13ac8c709a088fe4f09c9807.

- 2026-09-08T00:00:58+00:00: Recorded command exit 0; command argv SHA-256
  b68ea59f1d66b0fcc72f156ba95c80293d278a02a243a4a412e9ce060071865a.

- 2026-09-08T00:02:22+00:00: Recorded command exit 0; command argv SHA-256
  0c0dfb029e4eb413a188c5131a14a8a93b9fa35c60ee1ea0322d3baf105579fa.

- 2026-09-08T00:03:26+00:00: Recorded command exit 0; command argv SHA-256
  89ebfc7fc95fea241b17e1b5c189e471d9316e4f17d99af266750f622c0b0d10.

- 2026-09-08T00:04:02+00:00: Recorded command exit 0; command argv SHA-256
  054089e9a86ced68de005e2fb1c22f78b95c3456606bee042968e48bff58d3b7.

- 2026-09-08T00:04:24+00:00: Recorded command exit 0; command argv SHA-256
  c3ab8d694c81d20361e7b14c63f5814062e68b4876b85dbda1bbb2dc5540bf77.

- 2026-09-08T00:04:45+00:00: Recorded command exit 0; command argv SHA-256
  7fd79834a2103daebb0b683b22de06a5908c16e2cc016ba801a9f4c35e164e49.

- 2026-09-08T00:05:05+00:00: Recorded command exit 0; command argv SHA-256
  c79337f00f0c6631de39c46fc655d7d187958b53d530408b9c2a5fccec8750c3.

- 2026-09-08T00:06:24+00:00: Immutable candidate 5d2cd78a924b2e2cb76e0bf48e01dca3e9249e74 (tree
  f70871120d9fd45f60eb43b80286904c0b05a546) contains three SSH-signed DCO commits on exact base
  72dd78f. Initial real qualification failed closed at sandbox relative-path test because the
  primary source was read-only; isolated diagnostics proved metrics/process green and sandbox EROFS.
  Signed repair 4658d0e materialized the exact commit/tree into the private bounded cell without
  weakening the host boundary. The changed run passed metrics/process/sandbox/workloads, collected
  all transient units and removed the cell before emitting schema-valid sanitized evidence. Focused
  11/11, all platform 23/23, full fmt/clippy/workspace tests/docs/release, repository policy,
  actionlint, zizmor, Gitleaks, deny/audit, controlled failure fixtures, aggregate/critical
  coverage, Kani 6/6 and deliberate counterexample all pass. Python changed-module branch coverage
  is measured 56% and is not a configured critical floor; native positive behavior is additionally
  exercised by the real four-check evidence. No aarch64, performance, public-PR runner, AppArmor
  enforcement, SLA, or zero-cost claim.

- 2026-09-08T00:07:27+00:00: Recorded command exit 0; command argv SHA-256
  4e173bfaf0b49f7ba1869e9f58c5c3107f20fc0ae4b77e0283c7f199828f42e7.

- 2026-09-08T00:07:49+00:00: Recorded command exit 0; command argv SHA-256
  0ff6c0dcb241e58076ea6b7cdb3a0bbd685e0cf5ba26a86e6eca902b5ac75460.

- 2026-09-08T01:17:55+00:00: Recorded command exit 0; command argv SHA-256
  a8383e8eba044293421edc32d069b507c1762e202db34f4ade71a85b82f93645.

- 2026-09-08T01:19:23+00:00: Recorded command exit 0; command argv SHA-256
  61a540ff8dff87e068648c251a64e520d20574193c5c0dd587628e1df12bbe65.

- 2026-09-08T01:21:00+00:00: Recorded command exit 0; command argv SHA-256
  238c5547d539ba0b8ed576b0623f4e1bd28dd65e8b010ec58d79e66d2e57c019.

- 2026-09-08T01:21:33+00:00: Recorded command exit 0; command argv SHA-256
  f3dc97c9fb502dbf961e094bbd151be191a66a63df5c65f5ab2db9240e539628.

- 2026-09-08T01:22:01+00:00: Controlled rebase preserved the three-commit AR-0848 series exactly:
  range-diff old 72dd78f..5d2cd78 versus f42645d..45604cd is equal for all commits. New head
  45604cd323c5de0ab9c7eaf0b6a39d90f4d43002, tree ebec01b4677174d20853574068d3265b8254e664, clean
  six-path scope; all rewritten commits are SSH-signed and DCO-valid. Exact rebased-tree focused
  Ruff/platform 23/23, full fmt/clippy/workspace tests/docs/release, repository policy, actionlint,
  zizmor, Gitleaks, deny/audit, failure fixtures, aggregate/critical coverage, Kani 6/6 and
  deliberate counterexample are green. Prior PR #58 stale head 5d2cd78 had all hosted checks green
  but remains unmerged and must be replaced only after fresh review.

- 2026-09-08T01:32:18+00:00: Recorded command exit 0; command argv SHA-256
  eef9cea2a000a118f0a74457c5bc81de507ba489cec4131ddf9411e07e895f7f.

- 2026-09-08T01:43:18+00:00: Recorded command exit 0; command argv SHA-256
  c86ee7e1e8079cdaaa7c04b4324ed7807f312930fe191cc511c7eeae3aa27e99.

- 2026-09-08T01:44:45+00:00: Recorded command exit 0; command argv SHA-256
  a7126208df51724f043a7488c1dc0d5770881344bdad79854305d1cba1acff50.

- 2026-09-08T01:45:11+00:00: Recorded command exit 0; command argv SHA-256
  cc8397959e61195897f082ea5a1e1f583544fab82fb537972153fac5f8f2466e.

- 2026-09-08T01:52:11+00:00: Released after independently reviewed PR #58 exact head
  45604cd323c5de0ab9c7eaf0b6a39d90f4d43002 was integrated by signed+DCO no-ff merge
  678ba7c8593a52beb8f3279ddd452245294131e7 with feature-identical tree
  ebec01b4677174d20853574068d3265b8254e664. Exact-main local focused/platform/repository policy and
  full fmt/clippy/workspace tests/docs/release passed from a clean primary tree. Hosted exact-main
  runs all completed success: quality 34177692194, Rust x86_64/aarch64 34177692208, formal
  34177692199, fault assurance 34177692197, and emulated aarch64 34177692187. Product main is clean
  and synchronized. State 43 tests, schema validation, generated STATUS check, snapshot and live
  doctor pass. A mistaken nonexistent tools/validate_state.py invocation failed without mutation;
  documented tests/validate_schema.py then passed. Proven support is one existing bare-metal Ubuntu
  24.04.4 x86_64 native-functional cell only; native aarch64, performance baseline, public-PR runner
  eligibility, AppArmor enforcement, availability SLA and zero operational cost remain unsupported.
