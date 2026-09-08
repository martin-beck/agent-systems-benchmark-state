---
{
  "branch": "feature/benchmark-validity",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-08T03:10:34+00:00",
  "depends_on": [
    "AR-0401",
    "AR-0701",
    "AR-1001"
  ],
  "id": "AR-1007",
  "next_action": "Implement registry schema and validation for built-in and imported workloads.",
  "observed_branch": "feature/benchmark-validity",
  "observed_dirty": 0,
  "observed_head": "60a6c730457b4c40f9a025751c1e317d9fe9429d",
  "owner": "replay_20260906",
  "plan": "../plans/AR-1007.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Track dataset provenance, contamination risk, grader validity and native portability per workload revision.",
  "task_revision": 61,
  "title": "Maintain benchmark validity and portability registry",
  "updated_at": "2026-09-08T00:16:10+00:00",
  "worktree_key": "agent-systems-benchmark-benchmark-validity"
}
---
## AR-1007

Track dataset provenance, contamination risk, grader validity and native portability per workload revision.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-07T23:27:08+00:00: Dependencies AR-0401, AR-0701, and AR-1001 are durably done. Selected
  highest-priority dependency-ready leaf; workload registry/provenance scope is disjoint from active
  AR-0505 replay integration, AR-0840 frontend protocol, and AR-0848 native capacity. Declared
  branch, worktree, and remote ref are absent.

- 2026-09-07T23:27:10+00:00: Claimed by replay_20260906.

- 2026-09-07T23:27:52+00:00: Recorded command exit 0; command argv SHA-256
  f8e83446a4a364c5e265648164c1fcc18c0b30e0b72c156dcc3049075b0574af.

- 2026-09-07T23:28:47+00:00: Recorded command exit 0; command argv SHA-256
  b3e29f2cbb6733a2838ea852d7ac6731d92ff49a5716b40ba590735d6a73ebae.

- 2026-09-07T23:37:36+00:00: Changed conclusion: the initial isolated source patch was applied by
  the workspace edit tool before the handoffctl wrapper instead of through the required wrapper.
  Exact affected paths are crates/asb-workloads/Cargo.toml, src/lib.rs, src/validity.rs, and
  examples/generate_validity_schema.rs; no build, Git, publication, network, or external effect
  occurred. Preserve and audit these effects; all subsequent product/build/test/Git mutations use
  handoffctl run.

- 2026-09-07T23:39:58+00:00: Recorded command exit 0; command argv SHA-256
  5f1114104d3919f72ee746fc7bea36de9b7fd8369650f9ab250d692d5ebc4bd2.

- 2026-09-07T23:40:12+00:00: Recorded command exit 127; command argv SHA-256
  19732f767eebd6a6e1839f95999f2ca1f0db3789500883e5d8dae5d8be4e8cfc.

- 2026-09-07T23:40:57+00:00: Recorded command exit 0; command argv SHA-256
  d80be3a7a0c3d33c85bb5705bf448503c1341ebce6352bdb0c8e8ac3800764b4.

- 2026-09-07T23:41:29+00:00: Recorded command exit 101; command argv SHA-256
  f4c9f5870426327d3cb87263d8d31031f4dd658fbc9a8139bcc19f8d99fe0442.

- 2026-09-07T23:42:06+00:00: Recorded command exit 127; command argv SHA-256
  6fe3949d12e3b9ec837ab915faef353028d6f5d7391008dd465408f598253f7e.

- 2026-09-07T23:42:31+00:00: Recorded command exit 0; command argv SHA-256
  f4c9f5870426327d3cb87263d8d31031f4dd658fbc9a8139bcc19f8d99fe0442.

- 2026-09-07T23:42:50+00:00: Recorded command exit 0; command argv SHA-256
  3f800d425626b4733bd1a0681ce9dac8a5f4c48c91a84772aacfb4ef9a456d03.

- 2026-09-07T23:46:17+00:00: Recorded command exit 1; command argv SHA-256
  fecb6f93f03d87486ca8587d580e2a564d4e50043f3a24d13e0a9c48f5611217.

- 2026-09-07T23:47:11+00:00: Recorded command exit 0; command argv SHA-256
  fecb6f93f03d87486ca8587d580e2a564d4e50043f3a24d13e0a9c48f5611217.

- 2026-09-07T23:47:27+00:00: Recorded command exit 0; command argv SHA-256
  7cf2d4dcf2763fa05550ff20a6b1247b640007f0842fcee82d7082ef26a7c52c.

- 2026-09-07T23:49:27+00:00: Recorded command exit 0; command argv SHA-256
  adec60fa4c2c5e8468afdff1918ce1c3cef4836c2fca2377edd41fe3b50d4727.

- 2026-09-07T23:50:28+00:00: Recorded command exit 101; command argv SHA-256
  3a0309a11529adc02cc5f9c9743b7ebe1304c55b3667c3e8f6c83877afc34323.

- 2026-09-07T23:51:23+00:00: Recorded command exit 0; command argv SHA-256
  7f16d13ad59c7a38f47cd3420d9501e88b39ad3c9684fe75cdc0377c43d404f6.

- 2026-09-07T23:51:40+00:00: Recorded command exit 0; command argv SHA-256
  b6458ab5191472659188869904da55bdd66d72965f503e014af2e317a0b2f9ac.

- 2026-09-07T23:54:05+00:00: Recorded command exit 101; command argv SHA-256
  9422ee223cb1d10bd2be7b11df23e7b431e5724e90f62752ba8bebdb14a5c289.

- 2026-09-07T23:54:28+00:00: Recorded command exit 127; command argv SHA-256
  91e6133eb4778fbb372ebcc0940071e2a7890dd88c73d630458980e95e1f8650.

- 2026-09-07T23:55:02+00:00: Recorded command exit 0; command argv SHA-256
  e21bfd27bdf4c8453ea7387b0a26ac691c304655cacd4434ba60e0b791b83f23.

- 2026-09-07T23:55:09+00:00: Recorded command exit 0; command argv SHA-256
  43b4cc5dd4bad88ac8eb1d3bdcadd6bdc82e961e027c63cc63a0ba55316a7901.

- 2026-09-07T23:55:26+00:00: Recorded command exit 0; command argv SHA-256
  2e495258b12bcb53006c66bab155e719b94a3f700afb38534f0a343503c116b2.

- 2026-09-07T23:55:43+00:00: Recorded command exit 0; command argv SHA-256
  60b09b6c88e3e8883e3dd463b44399774844035adc6ba30e9206706af25fb35b.

- 2026-09-07T23:56:50+00:00: Recorded command exit 0; command argv SHA-256
  08c49338c09e1d1f6f3cd46cb4088d0d214a6b4988d259ebb885aebad80bebca.

- 2026-09-07T23:56:59+00:00: Recorded command exit 0; command argv SHA-256
  2d7f774a5558ccfa61dedb67b3b9abd1f838c627734dbd316613fe92f34fca0b.

- 2026-09-07T23:57:31+00:00: Recorded command exit 0; command argv SHA-256
  52927f5ba99245527d0994717a4ade82b788bfec418c40d6a75a5b62473c9ecc.

- 2026-09-07T23:58:20+00:00: Recorded command exit 101; command argv SHA-256
  45084b60505f66acd984fc7d69140a5092a5e64bfbdb9597ab42c9bb8f0c7624.

- 2026-09-07T23:59:30+00:00: Recorded command exit 0; command argv SHA-256
  528d833c61b5e37a93b564f724bbd916942e443722570da195e1dec92d99883d.

- 2026-09-07T23:59:38+00:00: Recorded command exit 0; command argv SHA-256
  aa2e013097c5c96fb9e7bde8d3de5dc9fd4db2245a72257c5c15619b92c49004.

- 2026-09-08T00:01:23+00:00: Recorded command exit 0; command argv SHA-256
  3404391ede05eee37f1660dea1239b83afbfb99215633e52c7e2d99ccccc1922.

- 2026-09-08T00:02:28+00:00: Recorded command exit 1; command argv SHA-256
  5e3fd74d2ecbcbe08b1e8493fdb1dae3c6fccfa641afd444b8c36aa0ce227487.

- 2026-09-08T00:03:01+00:00: Recorded command exit 1; command argv SHA-256
  c835b54d14c5ae3ecc200ae98c3fa6f285f15b9068a52ff1820f50d2e0dc8482.

- 2026-09-08T00:04:13+00:00: Recorded command exit 0; command argv SHA-256
  653cda38def6e4d33155f3068a49db6871d86b908c27ff8041731d8f438feb3c.

- 2026-09-08T00:04:30+00:00: Recorded command exit 1; command argv SHA-256
  3204804d88a416a0bb4d503ab0c734149cd038cff50f8bd683c85019a0360eb5.

- 2026-09-08T00:04:51+00:00: Recorded command exit 0; command argv SHA-256
  990a389263b676a726d929853345940cf0cad9456ee6e27df9be58762c244851.

- 2026-09-08T00:05:32+00:00: Recorded command exit 0; command argv SHA-256
  ecde36e4ef54be679b837b5a3d84ded0eda1e87d33a33078a458fec5b7f99198.

- 2026-09-08T00:06:29+00:00: Recorded command exit 0; command argv SHA-256
  3204804d88a416a0bb4d503ab0c734149cd038cff50f8bd683c85019a0360eb5.

- 2026-09-08T00:06:51+00:00: Recorded command exit 0; command argv SHA-256
  2ccc80d25ef2c82344c535d3e5d45e80abdd24fc48db488863b78f13ecceab46.

- 2026-09-08T00:07:08+00:00: Recorded command exit 0; command argv SHA-256
  fc09503af9c004d9e4ef2f2511a98f9560c4c60f6e3f1c36222e8946f6483a63.

- 2026-09-08T00:07:40+00:00: Recorded command exit 0; command argv SHA-256
  95be89c99e01650f8f58cc334fdd76ad88e01266c9dfd5f595e1049c215d5ae0.

- 2026-09-08T00:08:43+00:00: Recorded command exit 0; command argv SHA-256
  c24fffe98acd5beea6f07c6d1c0aefb5f54d14e6a072e2924baa6e2fb0728bb3.

- 2026-09-08T00:10:34+00:00: Heartbeat by replay_20260906.

- 2026-09-08T00:11:20+00:00: Recorded command exit 1; command argv SHA-256
  85127a86717c8ca3c732c3fa54f12d8a1b94abe876081caca9d41c6cff5e4ab5.

- 2026-09-08T00:11:48+00:00: Final precommit actionlint, zizmor, and directory-mode Gitleaks
  completed green. The combined failure-fixture invocation then stopped after its
  workflow/DCO/privacy negatives because the subprocess environment could not resolve Cargo;
  repository policy did not execute in that invocation. This is an environment-path failure, not a
  product failure. Next action: rerun only the uncompleted failure-fixture and repository-policy
  gates with the pinned Rust toolchain path.

- 2026-09-08T00:12:30+00:00: Recorded command exit 0; command argv SHA-256
  d7627741bb1bf2dc8b979c5212f61df7b4d19242d9fa832df0fe1f9751170d5c.

- 2026-09-08T00:12:50+00:00: Recorded command exit 0; command argv SHA-256
  321c534968b9c456a64caf5e6d09b63780c507f97548057d2bfe31edcfd73ff4.

- 2026-09-08T00:14:11+00:00: Provenance correction: an initial direct Kani setup probe created only
  a disposable tool cache on the configured development volume and failed before proof execution
  because its toolchain was unavailable on PATH. It changed no product, coordination, repository, or
  external state; subsequent cache repair and all Kani proof mutations ran through the AR wrapper.
  The corrected Kani run proved all six harnesses and the deliberate false assertion failed closed.

- 2026-09-08T00:14:20+00:00: Recorded command exit 0; command argv SHA-256
  047e9ddb68fd8b60fbeaf12b3125a0d1e50e3291c52b264e2800be40163292c9.

- 2026-09-08T00:14:47+00:00: Recorded command exit 0; command argv SHA-256
  0f092180a92f096d60d2459469dfea56d6bbf910bedb566ccfed101aeb2451e0.

- 2026-09-08T00:15:08+00:00: Immutable review candidate 60a6c730457b4c40f9a025751c1e317d9fe9429d,
  tree 1a5f7481c34209affa7b19f19acda42df1ec5f17, exact parent/origin main
  20ac1e507e678aff463ec5f6c7b37cfcd67a5ad0. Ten-path focused registry/Cargo/docs scope; worktree
  clean. SSH signature is valid for Martin Beck and the exact DCO trailer is present. Exact-tree
  repository policy, range Gitleaks, diff check, Cargo locked/offline metadata and scope audit pass.
  Focused 22 tests, full workspace fmt/clippy/tests/docs/release, formal workspace, Kani six
  harnesses plus false-assertion negative, TLC/Alloy witnesses and mutants, failure fixtures,
  cargo-deny and cargo-audit pass. Validity module coverage is 97.35 percent lines and 100 percent
  functions; explicit nightly branch instrumentation measured 79.33 percent for the module and 82.30
  percent for the crate, so no 95 percent branch claim is made. Registry intentionally claims no
  native workload, holdout/contamination-resistance, or host-performance qualification. Next action:
  immutable independent review before publication.

- 2026-09-08T00:16:10+00:00: Recorded command exit 0; command argv SHA-256
  214f96074e0e40ecb0a6db4b6e2038e5e78adf70193a72defafd4169ec364a9d.
