---
{
  "branch": "feature/statistical-analysis",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-06T20:04:07+00:00",
  "depends_on": [
    "AR-0101"
  ],
  "id": "AR-0203",
  "next_action": "Create and push reviewed signed+DCO no-ff merge of exact head 3bcfd85; verify PR merge identity, then run exact-main local and hosted post-merge checks.",
  "observed_branch": "feature/statistical-analysis",
  "observed_dirty": 0,
  "observed_head": "3bcfd85dedd3b0c944d8c3100c031203d5888b10",
  "owner": "root-coordination-20260906",
  "plan": "../plans/AR-0203.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Compute latency distributions, quality/throughput intervals and evidence-aware SLO results.",
  "task_revision": 107,
  "title": "Implement statistical and SLO assessment",
  "updated_at": "2026-09-06T18:44:51+00:00",
  "worktree_key": "agent-systems-benchmark-statistical-analysis"
}
---
## AR-0203

Compute latency distributions, quality/throughput intervals and evidence-aware SLO results.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-06T17:21:38+00:00: Coordinator promoted the sole dependency-ready planned AR after
  verifying AR-0101 done, its declared branch/worktree absent, and its asb-analysis paths
  non-overlapping. Root Cargo.toml/Cargo.lock integration remains serialized behind AR-0102.

- 2026-09-06T17:22:14+00:00: Claimed by root-coordination-20260906.

- 2026-09-06T17:22:36+00:00: Recorded command exit 0; command argv SHA-256
  4935ea99a9b7233cabb2a603d8f8637a008cbc6ad21a887437c805f5a404c85e.

- 2026-09-06T17:29:07+00:00: Recorded command exit 0; command argv SHA-256
  91d21f688db0a437440f3416c11e40e2242c2ad0e24e08788e865b8714faf691.

- 2026-09-06T17:29:19+00:00: Recorded command exit 1; command argv SHA-256
  68737d5c487a7bdb7cbf9675ca4297eee8cb9b90680499e4cb112c7a7a67e6d9.

- 2026-09-06T17:29:31+00:00: Recorded command exit 0; command argv SHA-256
  e35b6774643aa4f9fe4f3b881cbdf4822c811d3956449ed046c3dafb84d0d7e8.

- 2026-09-06T17:29:36+00:00: Recorded command exit 101; command argv SHA-256
  68737d5c487a7bdb7cbf9675ca4297eee8cb9b90680499e4cb112c7a7a67e6d9.

- 2026-09-06T17:30:21+00:00: Recorded command exit 0; command argv SHA-256
  f9ec108c892c80e40ecd976ef50d84627e6b9f294145ab07947e4e215039da44.

- 2026-09-06T17:30:27+00:00: Recorded command exit 0; command argv SHA-256
  4e3a91c4c554e556d7a8412003796aaa50a535104c5e84f4f4fa6d94246d83d1.

- 2026-09-06T17:31:24+00:00: Recorded command exit 0; command argv SHA-256
  251a1e7308d7ecd405fb25546ebb818b62dd7e3644b44369a8ef52e03b6e12f6.

- 2026-09-06T17:31:39+00:00: Recorded command exit 0; command argv SHA-256
  adaa559124f55fe7326405d10bd0a03b6eebd4fe6617f4c096a8a861e2656886.

- 2026-09-06T17:34:49+00:00: Recorded command exit 0; command argv SHA-256
  c2edfebdf6058f22faa4a8e1f84527e9e1488b0a6ce2010c532a85b21f7deaec.

- 2026-09-06T17:35:01+00:00: Recorded command exit 0; command argv SHA-256
  adaa559124f55fe7326405d10bd0a03b6eebd4fe6617f4c096a8a861e2656886.

- 2026-09-06T17:36:20+00:00: Recorded command exit 0; command argv SHA-256
  ce4ee76fb430c305c8cec3745c8d80d4ee3ea93d6b5c98dddbff57190f41f6fd.

- 2026-09-06T17:36:24+00:00: Recorded command exit 0; command argv SHA-256
  adaa559124f55fe7326405d10bd0a03b6eebd4fe6617f4c096a8a861e2656886.

- 2026-09-06T17:38:22+00:00: Recorded command exit 0; command argv SHA-256
  8954f83abd153e3bbbaf85a14daa99082c38b1ea950e75350d13a82b2302e711.

- 2026-09-06T17:38:41+00:00: Recorded command exit 0; command argv SHA-256
  adaa559124f55fe7326405d10bd0a03b6eebd4fe6617f4c096a8a861e2656886.

- 2026-09-06T17:45:08+00:00: Recorded command exit 1; command argv SHA-256
  bcbdb9a8f9200b269cab87f3be5023ac2c27d9bf4406cb32c4814caa68616a42.

- 2026-09-06T17:45:31+00:00: Recorded command exit 1; command argv SHA-256
  d67989f52fe095ab065af594b62e12c050693f4b13e758a698bf63c2d0a74bf4.

- 2026-09-06T17:46:49+00:00: Recorded command exit 0; command argv SHA-256
  d67989f52fe095ab065af594b62e12c050693f4b13e758a698bf63c2d0a74bf4.

- 2026-09-06T17:47:37+00:00: A focused validation invocation failed before spawning rustfmt because
  the coordinator environment did not expose rustfmt on PATH; no product mutation or test execution
  occurred. Verified pinned rustfmt and rustc under /srv/data/projects/.asb-local/cargo/bin and will
  use those exact paths.

- 2026-09-06T17:47:52+00:00: Recorded command exit 1; command argv SHA-256
  11a2c4fa5a47a900c52f26b524f81ea591cd599d3a636fab85d19a45191ab902.

- 2026-09-06T17:48:11+00:00: Recorded command exit 1; command argv SHA-256
  0b860f9182d7d45b202272f04983523bf28507c1aa480c88c571b9349c60b622.

- 2026-09-06T17:48:26+00:00: Recorded command exit 0; command argv SHA-256
  034527bb71c5d238cef9515aea4cecd3cd0b9f86cb4550054c64f2ee6a4ad81b.

- 2026-09-06T17:48:33+00:00: Recorded command exit 0; command argv SHA-256
  0b860f9182d7d45b202272f04983523bf28507c1aa480c88c571b9349c60b622.

- 2026-09-06T17:48:39+00:00: Recorded command exit 1; command argv SHA-256
  5f61964c0ff8b49d0e1e81ec4ec3fe6fe3d746fe671d936be44ed00d1667ccfc.

- 2026-09-06T17:48:56+00:00: Recorded command exit 0; command argv SHA-256
  360b8be73d332d775b3757e8d47bb7f1ca055418b93911af67a2f731eb1eb542.

- 2026-09-06T17:49:01+00:00: Recorded command exit 0; command argv SHA-256
  5f61964c0ff8b49d0e1e81ec4ec3fe6fe3d746fe671d936be44ed00d1667ccfc.

- 2026-09-06T17:49:05+00:00: Recorded command exit 101; command argv SHA-256
  20993c253f90297033c52c392ada3c6ac9449f59364d4f8587efbdb601af40ad.

- 2026-09-06T17:49:23+00:00: Recorded command exit 0; command argv SHA-256
  a00de494e3902200c50e57c8609f9e102137601a9b52da7ea22442ab9b312c14.

- 2026-09-06T17:49:27+00:00: Recorded command exit 0; command argv SHA-256
  0b860f9182d7d45b202272f04983523bf28507c1aa480c88c571b9349c60b622.

- 2026-09-06T17:49:31+00:00: Recorded command exit 0; command argv SHA-256
  5f61964c0ff8b49d0e1e81ec4ec3fe6fe3d746fe671d936be44ed00d1667ccfc.

- 2026-09-06T17:49:35+00:00: Recorded command exit 0; command argv SHA-256
  20993c253f90297033c52c392ada3c6ac9449f59364d4f8587efbdb601af40ad.

- 2026-09-06T17:49:47+00:00: Recorded command exit 1; command argv SHA-256
  8c5385b486cf6d1047a4bdf72c6542ae22645b40a33e4d2950a3bb14b52f0b0a.

- 2026-09-06T17:49:57+00:00: Recorded command exit 0; command argv SHA-256
  a876469b481443dbd541b1c37bf1a51bb62d95ab341b04ca6aeca05c8895b4e6.

- 2026-09-06T17:50:09+00:00: Recorded command exit 1; command argv SHA-256
  6bc26afc7bc6878bda9556b7d8e36532ed23ebafd9771338f289e0b7fa882d74.

- 2026-09-06T17:50:39+00:00: Recorded command exit 0; command argv SHA-256
  c0744dd3a0b40032534b89288f4f7227489188759cae237eac5f990a723e2338.

- 2026-09-06T17:50:52+00:00: Recorded command exit 0; command argv SHA-256
  97c7ba256c1fbe8d3f16fb577d06ad5ecf8c25c04e6323593f8fe69b6b494799.

- 2026-09-06T17:51:18+00:00: Recorded command exit 1; command argv SHA-256
  e5c327fb91fc2ddbbd53d3dd78b9f95ff8635ceca1cfb6a1a94bfd8c830712da.

- 2026-09-06T17:51:30+00:00: Recorded command exit 0; command argv SHA-256
  e5298be373f6b2ed9c44cbb30be8bf79fec823f2d80a6b771ac2b35eed9febdb.

- 2026-09-06T17:52:05+00:00: Recorded command exit 0; command argv SHA-256
  f3b5af1294e62a3db2effec3619ada28e0ce7bd8899c4a0542aec549358e8137.

- 2026-09-06T17:52:10+00:00: Recorded command exit 0; command argv SHA-256
  034527bb71c5d238cef9515aea4cecd3cd0b9f86cb4550054c64f2ee6a4ad81b.

- 2026-09-06T17:52:23+00:00: Recorded command exit 0; command argv SHA-256
  5f61964c0ff8b49d0e1e81ec4ec3fe6fe3d746fe671d936be44ed00d1667ccfc.

- 2026-09-06T17:52:35+00:00: Recorded command exit 0; command argv SHA-256
  20993c253f90297033c52c392ada3c6ac9449f59364d4f8587efbdb601af40ad.

- 2026-09-06T17:52:40+00:00: Recorded command exit 0; command argv SHA-256
  e5c327fb91fc2ddbbd53d3dd78b9f95ff8635ceca1cfb6a1a94bfd8c830712da.

- 2026-09-06T17:54:08+00:00: Independent review fixed three conservative-analysis defects: missing
  successful latency now prevents both latency pass and fail; unequal throughput-window durations
  are rejected; df>30 retains the wider t(30) critical value. Added negative/property tests and
  quantile-order evidence checks. Standalone rustfmt and 13 Rust tests pass. Checked-in vector
  d24ab8119 was independently validated against pinned scipy 1.16.1 and numpy 2.5.3 using
  project-local script d9e2348a; this caught and corrected rounded t-critical fixture drift. Failed
  commands for absent PATH tool shims, missing build directory, pre-fix formatting/test, and absent
  SciPy/mpmath were preserved by handoffctl before successful repairs.

- 2026-09-06T17:54:32+00:00: Recorded command exit 0; command argv SHA-256
  92fe63e78de73d1089bd56370ebfff2deba787d083b012b0c9df7ff29af0d8f4.

- 2026-09-06T17:54:41+00:00: Recorded command exit 1; command argv SHA-256
  875c27e2c4a616ec7169bf5ff1d70f56cee0024b797c65e6782da5596f6531bd.

- 2026-09-06T17:54:57+00:00: Recorded command exit 0; command argv SHA-256
  a58deaf6f045ff3e0c9968ca17bf00543336de8dce81b6c2df734053017db76a.

- 2026-09-06T17:55:03+00:00: Recorded command exit 0; command argv SHA-256
  607ab1820675009da18a9ac8b5404f5f11d331e5fb9351e8e102aab000516c1e.

- 2026-09-06T17:55:32+00:00: Recorded command exit 0; command argv SHA-256
  f8e2c2a14a851419daadca9e9a66376fcc70991458d02884b161da55b37dd220.

- 2026-09-06T17:55:44+00:00: Recorded command exit 0; command argv SHA-256
  016ffa1cfcd6b1550a3547237c017e8e48116343b1b621c194a0bdc31fe07b40.

- 2026-09-06T17:55:57+00:00: Recorded command exit 0; command argv SHA-256
  a654e6a5b5cd94c19f5748bc950da94ec369c08550b27b614a5faf6ece405ede.

- 2026-09-06T17:58:13+00:00: Recorded command exit 0; command argv SHA-256
  acc95d5275a0a8f7b0845852a1fc545f4d5fec53e692d57d1e3ce0272e3123f7.

- 2026-09-06T18:04:07+00:00: Heartbeat by root-coordination-20260906.

- 2026-09-06T18:16:06+00:00: Crate-only candidate is clean signed+DCO commit
  a47cce4e92c4141406ef4a94323045b6645db600 rebased directly on exact product main e6a81e8. Diff
  check, standalone rustfmt and 13 tests pass; scoped Gitleaks found no leaks and privacy-pattern
  search found no matches. Root Cargo.toml/Cargo.lock remain untouched while AR-0502 owns the fence.
  No PR or support claim yet.

- 2026-09-06T18:24:08+00:00: Recorded command exit 0; command argv SHA-256
  2cb591c4c09b5403d18df30de0aa9d63ebbebc8e7651760594cfc641693d034e.

- 2026-09-06T18:24:30+00:00: Recorded command exit 127; command argv SHA-256
  42f2b711c089862e8e49e599ecb7a0274e69f465681231dc1e90bab2877f14f8.

- 2026-09-06T18:24:58+00:00: Recorded command exit 0; command argv SHA-256
  dc2d4e90e2e56b358eb3e3c0271f33b042eea544c36394092e932bfa0e7a85c5.

- 2026-09-06T18:25:41+00:00: Recorded command exit 128; command argv SHA-256
  a8c20011839f7e27decdf238c4ee09bf055b1275268ceeaae5b0e2048e5e701b.

- 2026-09-06T18:26:12+00:00: Recorded command exit 128; command argv SHA-256
  a8c20011839f7e27decdf238c4ee09bf055b1275268ceeaae5b0e2048e5e701b.

- 2026-09-06T18:26:45+00:00: Recorded command exit 0; command argv SHA-256
  0df157a351b38baad95cacbf603460ebe6f314484b7ac49ca03b9653c1654b0c.

- 2026-09-06T18:27:14+00:00: Recorded command exit 0; command argv SHA-256
  a2d3a4de415c2ad017c87309c94f3cbabda59f5bf248c7b791b396ea756302df.

- 2026-09-06T18:27:44+00:00: Recorded command exit 101; command argv SHA-256
  a9f08b04568de2292f5c9358ab28fd95dab64d4677d5a6834e78f5843c5a70a5.

- 2026-09-06T18:28:14+00:00: Recorded command exit 0; command argv SHA-256
  2e92c70ce524b51d3e6563b1f95601c019f2c36e15b3a98f63cfde468ecf9f17.

- 2026-09-06T18:28:49+00:00: Recorded command exit 0; command argv SHA-256
  a9f08b04568de2292f5c9358ab28fd95dab64d4677d5a6834e78f5843c5a70a5.

- 2026-09-06T18:29:33+00:00: Recorded command exit 0; command argv SHA-256
  62b120d208be5df9a41dbc0c3a25ba6f90737511cc81d26509f6f17bc995bccc.

- 2026-09-06T18:30:24+00:00: Recorded command exit 0; command argv SHA-256
  e5c327fb91fc2ddbbd53d3dd78b9f95ff8635ceca1cfb6a1a94bfd8c830712da.

- 2026-09-06T18:31:00+00:00: AR-0502 fence transfer verified and candidate rebased from e6a81e8 onto
  exact signed main 265d811; new candidate 4d9643c has only asb-analysis plus serialized
  Cargo.toml/Cargo.lock integration. First full Clippy run failed on an over-precise t-critical
  literal; focused signed+DCO repair 4d9643c removed only the non-representable trailing zero, then
  fmt, Clippy -D warnings, 108 workspace tests, rustdoc -D warnings and release build passed.
  cargo-deny/audit, actionlint, zizmor, Gitleaks, repository policy and every real failure fixture
  passed. Coverage: asb-analysis 98.31% lines/96.59% regions and workspace 97.04% lines/92.97%
  regions. Independent pinned SciPy 1.16.1 and NumPy 2.5.3 revalidated all reference vectors;
  validator SHA-256 d9e2348a976d69026154a6b05af134c345d8d4b0e7f708662b6511860c9a9910 and fixture
  SHA-256 d24ab81191879e88a37913cf2100e6a60961a4fd393e211e1e14bf679ff8dffe. Review confirmed type-7,
  Wilson, DKW, equal-duration Student-t and conservative Pass/Fail/Inconclusive bounds, explicit
  failures/timeouts/cancellations and missing-evidence behavior. Limits remain 95% intervals, iid
  throughput windows, floating point, no autocorrelation/sequential correction/bootstrap; those are
  documented and unsupported.

- 2026-09-06T18:31:19+00:00: Recorded command exit 0; command argv SHA-256
  7cebacf9126c9f8ae398f34ec125c74044adbbc804c7beb65764f4eaf6d70def.

- 2026-09-06T18:31:36+00:00: Recorded command exit 0; command argv SHA-256
  d505b0d6700d8706edea12847cadac0f3c6ba750f915f407bd7bcdab49fe8210.

- 2026-09-06T18:32:29+00:00: Recorded command exit 1; command argv SHA-256
  2e80a105128f849969e0015bb6c39a4cc27d89ffb6440d0b82abd57e56176d18.

- 2026-09-06T18:34:24+00:00: Recorded command exit 0; command argv SHA-256
  b02602630a27833f7fe669f34ab34e126fae5c3a24c5ea6e7122cf0df97ef3da.

- 2026-09-06T18:36:12+00:00: Recorded command exit 1; command argv SHA-256
  7b7986604b357eb6d52a0e2db17932ac850c272b6dfc81fb1316a4325c3c9eb7.

- 2026-09-06T18:36:48+00:00: Recorded command exit 0; command argv SHA-256
  cbb415cb494e76267918dbcca308473cfe369c3dbab03f58c56dae234f0e3525.

- 2026-09-06T18:37:54+00:00: Recorded command exit 0; command argv SHA-256
  96d4635f9c70fbd24a7a5afe54b82766f85e5f9739b178973a7b9cddb3c96b6a.

- 2026-09-06T18:38:13+00:00: Recorded command exit 101; command argv SHA-256
  02d9fcb7e4b2c6c5d70872f778a695a9fb8ee9aec444d48c3209ce0c2a263271.

- 2026-09-06T18:38:38+00:00: Recorded command exit 0; command argv SHA-256
  a3531c8f36358b8588b8d95061164963b8fa3acd306c81774ea2f31accef601b.

- 2026-09-06T18:38:59+00:00: Recorded command exit 0; command argv SHA-256
  02d9fcb7e4b2c6c5d70872f778a695a9fb8ee9aec444d48c3209ce0c2a263271.

- 2026-09-06T18:39:19+00:00: Recorded command exit 0; command argv SHA-256
  1dd73195d2c26a8985bd54af9b06b9e421eeb45d8df447629fac132ad69fdd7c.

- 2026-09-06T18:39:45+00:00: Recorded command exit 0; command argv SHA-256
  f6cf52d98ac43d04b0fc84f21118aff9853b7d87394b6dafa36b2ee7e8b01cca.

- 2026-09-06T18:40:19+00:00: Recorded command exit 0; command argv SHA-256
  7961f4b1f9685544760905444f40bac27cb7a872dd58ae27aa738ecb0f8ad09e.

- 2026-09-06T18:40:46+00:00: Recorded command exit 0; command argv SHA-256
  d5e1d5d35a3e06e64621aba7acebb55f22d392db84aeaad690e5b9d51c0ae956.

- 2026-09-06T18:41:23+00:00: Recorded command exit 0; command argv SHA-256
  456258b34efc50c9b6a64313472eb972abe0ba7924550046298cd41065d0e74c.

- 2026-09-06T18:41:35+00:00: Recorded command exit 0; command argv SHA-256
  b62d0f83ae74db68440c0e9cf6ddec88e767d63ac08a51e3c8d92ec621145b81.

- 2026-09-06T18:41:55+00:00: Independent immutable review blocked old PR head 4d9643c because public
  evidence fields permitted forged well-shaped intervals and DKW lacked independent reference
  vectors. Repaired at signed+DCO head 3bcfd85: AttemptAnalysis and EstimateInterval are
  constructor-controlled with read-only accessors; two downstream compile-fail doctests prove forged
  Wilson/DKW/Student-t evidence cannot be constructed; pinned committed SciPy 1.16.1/NumPy 2.5.3
  validator reproduces original vectors plus DKW n=100 unbounded-upper and n=1000 finite-upper
  vectors. Initial new DKW fixture failed because separators were literal backslash-t; corrected to
  real TSV delimiters before acceptance. Exact final full gates pass: 14 analysis
  unit/model/negative tests plus 2 compile-fail doctests, 109 workspace unit/integration tests,
  fmt/Clippy/rustdoc/release, deny/audit, actionlint/zizmor/Gitleaks/policy/all failure fixtures.
  Final coverage asb-analysis 98.45% lines/97.00% regions, workspace 97.09% lines/93.12% regions.
  Await new immutable-head review and hosted CI.

- 2026-09-06T18:42:10+00:00: Recorded command exit 0; command argv SHA-256
  f601b07dfc1392f6b3fc434ba55dc32d00449c144205fb20a810fcb309044a5e.

- 2026-09-06T18:43:32+00:00: Independent worker re-review APPROVED immutable PR #9 head
  3bcfd85dedd3b0c944d8c3100c031203d5888b10 after confirming both prior evidence-boundary blockers
  closed, independently checking DKW epsilon/type-7 values and boundary direction, and verifying
  focused privacy-safe delta, SSH signature and exact DCO. Exact-head hosted quality run 34052528401
  and Rust x86_64/aarch64 run 34052528404 are green with matching head SHA. Nonblocking hardening
  only: Rust fixture test does not consume the quantile column, while the committed independent
  validator does and the fixed current value is 0.95.

- 2026-09-06T18:43:45+00:00: Recorded command exit 0; command argv SHA-256
  cd75eda6d1b71544ce0586745e2b2418677c4e1bbe159a6dfc5c466dc9d9b8df.

- 2026-09-06T18:44:51+00:00: Recorded command exit 0; command argv SHA-256
  53ad45efa30948d2a3fe82e450901792095cdb2753d978df6c993a9b8d93af15.
