---
{
  "branch": "feature/recovery-models",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-0102",
    "AR-0104",
    "AR-0204",
    "AR-0503"
  ],
  "id": "AR-0905",
  "next_action": "Monitor PR #57 exact head a288bb3485aa2a65ffa79626c3352c6522791138; investigate failures and merge only after every required exact-head check is green and coordinator authorizes.",
  "observed_branch": "feature/recovery-models",
  "observed_dirty": 0,
  "observed_head": "a288bb3485aa2a65ffa79626c3352c6522791138",
  "owner": "",
  "plan": "../plans/AR-0905.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "done",
  "summary": "Apply bounded formal models to run lifecycle, leases, recovery, replay cursors and uncertain external effects.",
  "task_revision": 84,
  "title": "Model execution recovery and worker fencing",
  "updated_at": "2026-09-07T23:23:10+00:00",
  "worktree_key": "agent-systems-benchmark-recovery-models"
}
---
## AR-0905

Apply bounded formal models to run lifecycle, leases, recovery, replay cursors and uncertain external effects.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-07T22:14:48+00:00: Dependencies AR-0102, AR-0104, AR-0204 and AR-0503 are durably done.
  Selected highest-priority ready compatible task after excluding native-capacity work overlapping
  active AR-0707, AR-0832 with its plan-level blocked AR-0703 dependency, and schema/contract work
  overlapping active AR-0840. Declared recovery-model branch/worktree and remote ref are absent;
  docs/formal verifier/trace scope is disjoint from active AR-0505 replay integration.

- 2026-09-07T22:14:58+00:00: Claimed by replay_20260906.

- 2026-09-07T22:16:20+00:00: Recorded command exit 0; command argv SHA-256
  0c45238c27b38f287d8c104a676b9c8d75deee6985f9f757151d54374b7753fb.

- 2026-09-07T22:17:45+00:00: Recorded command exit 1; command argv SHA-256
  22ff8758a1a185c5a55cf2cf09eaba75a48facd2ca96d86d1fb9607238352604.

- 2026-09-07T22:28:29+00:00: Heartbeat by replay_20260906.

- 2026-09-07T22:33:03+00:00: Recorded command exit 0; command argv SHA-256
  4b9c02191e39deea93bb2bf1b82d95036ccf7daeee565282b629333974ee25fd.

- 2026-09-07T22:33:19+00:00: Recorded command exit 1; command argv SHA-256
  2d87808075546993b1cc1c99353d31ba54d8f047470b6e5c7b77675d1c69865d.

- 2026-09-07T22:33:45+00:00: Recorded command exit 0; command argv SHA-256
  6718a69bf07d2c94d1287058f944ce52ffd6bab99b274d192fb44333a602cb94.

- 2026-09-07T22:34:00+00:00: Recorded command exit 1; command argv SHA-256
  fdd723cd72b3e9e36d0f77f562e48081211f9e1f5f8ee21fc3d1a9bdfeb67a70.

- 2026-09-07T22:34:25+00:00: Recorded command exit 0; command argv SHA-256
  86198b4ef5451b9cd2ef025f4b81ba6b11b7b5be56fa5abdb28c5cf15682b8ed.

- 2026-09-07T22:36:58+00:00: Recorded command exit 0; command argv SHA-256
  07c18edde70669271083dcd799b1adce4ece1b5c484c1c04b18dc8815f1a8be2.

- 2026-09-07T22:37:15+00:00: Recorded command exit 127; command argv SHA-256
  bde7505bbc26adb2958b2eaba2fe1af76aa5c2a461692c232cf4fee835cf6600.

- 2026-09-07T22:37:49+00:00: Recorded command exit 1; command argv SHA-256
  7590ef708eb857596045c7f1b0a403913a4800abb2c8c7e71a2b63f932e1560e.

- 2026-09-07T22:38:14+00:00: Recorded command exit 101; command argv SHA-256
  9356923345b92900ca1a028eb4df0422472f2b69d5b75fa7fb0fb7ec86a34f62.

- 2026-09-07T22:38:39+00:00: Recorded command exit 0; command argv SHA-256
  871319aa978de0b82d2250293a5c508aba9a24c228c1058e63f085988b1c279b.

- 2026-09-07T22:38:52+00:00: Recorded command exit 0; command argv SHA-256
  9356923345b92900ca1a028eb4df0422472f2b69d5b75fa7fb0fb7ec86a34f62.

- 2026-09-07T22:40:00+00:00: Recorded command exit 0; command argv SHA-256
  7a260acac0c7686e54693b2199c9bd56f9e167e66bca178f6a0b30a67bd74f85.

- 2026-09-07T22:40:24+00:00: Recorded command exit 101; command argv SHA-256
  bd5533b551cdca66819f301809acdc23fe96c5e8633f1cfdb0af905cbf6d7c61.

- 2026-09-07T22:41:02+00:00: Recorded command exit 0; command argv SHA-256
  a9eb0b43e610ed7ddd383bb4da0603573cdd52bba7067bd6c1da76071aaf5fb3.

- 2026-09-07T22:41:19+00:00: Recorded command exit 0; command argv SHA-256
  86cf9d2915a52c866ae7c92cf03742dbaffca2632e182aa84cd8acb663209f20.

- 2026-09-07T22:43:08+00:00: Recorded command exit 0; command argv SHA-256
  74dafcbf0682c361d753bafc49d43467195755e92b46f997df41af657094c866.

- 2026-09-07T22:43:32+00:00: Recorded command exit 0; command argv SHA-256
  3f71f50923cfec1cd7cb1cf4ba3cf8d36cf729c314dd82e48cfcbb9586bc6697.

- 2026-09-07T22:44:21+00:00: Recorded command exit 0; command argv SHA-256
  5bb210d195c2ab3ab8e3b54d0bcb4d5cbab303a9219e3ae8f958a873832519cf.

- 2026-09-07T22:46:39+00:00: Recorded command exit 1; command argv SHA-256
  0a4dd922c029912278385a6db01f039a69d107f85448e9835d97a498520d853b.

- 2026-09-07T22:47:48+00:00: Recorded command exit 1; command argv SHA-256
  e2d50981f2ceeb9f102fec155016c0cf2aab6b6317ceeb968234bb96f93fdba5.

- 2026-09-07T22:48:26+00:00: Recorded command exit 0; command argv SHA-256
  e87cc84c7e98c2915203c76dd705f61b902b1239fd678d9aa3c3635f24d37695.

- 2026-09-07T22:49:09+00:00: Recorded command exit 0; command argv SHA-256
  e038332751a9281779cc3fac28a18699bcfaec8807ed50362854ec253b09bb75.

- 2026-09-07T22:49:53+00:00: Recorded command exit 0; command argv SHA-256
  c8ff74d56efe02a631de3500137dee4108405227f461e45856ac7054c35ae906.

- 2026-09-07T22:50:40+00:00: Recorded command exit 0; command argv SHA-256
  808c2196102d7c6c3e54490eafb836e8334e83261bcc6980cd7bbdef3e66d1aa.

- 2026-09-07T22:51:08+00:00: Recorded command exit 101; command argv SHA-256
  2840ea82fd2c8aa4892ec58598ab323f6a03ea3f33e2f440c3aacfbb79e246df.

- 2026-09-07T22:51:40+00:00: Recorded command exit 0; command argv SHA-256
  f0cc084224a550079a3f2a6815c4c182634d087abbecb72bdf86e3fc671c6084.

- 2026-09-07T22:52:27+00:00: Recorded command exit 0; command argv SHA-256
  a89709bd75393c8a323eea904a80b8f734f6beae35769b628d346e18b1c3e4ff.

- 2026-09-07T22:52:46+00:00: Recorded command exit 0; command argv SHA-256
  1ddc827f3fc7bf5a490e466f79dcb620bd1f20f91a1e8f44b80dbe8da6e1d307.

- 2026-09-07T22:53:24+00:00: Recorded command exit 0; command argv SHA-256
  044ecb625a098d69b66f7c5423ba603e88f9e464ccf4b6da98ffe0282da320e5.

- 2026-09-07T22:54:22+00:00: Recorded command exit 0; command argv SHA-256
  049eb7beb35c8041cd2adb9d59764ba9ab54d173097a140e34934e71aa117cab.

- 2026-09-07T22:54:47+00:00: Recorded command exit 0; command argv SHA-256
  f8610e2592547eade748b7a390155a206faeca38d311d1ac18ac9fe2ef756bbf.

- 2026-09-07T22:55:56+00:00: Recorded command exit 0; command argv SHA-256
  5b32cedaaaef7b648b396af13d4e1d5e8c4669321ff448750756c36c6debfc83.

- 2026-09-07T22:56:19+00:00: Recorded command exit 0; command argv SHA-256
  11e145ed21929598ddfed2fad190ac7906ddacd42fc7fb453420c0d6cd40f530.

- 2026-09-07T22:57:18+00:00: Recorded command exit 0; command argv SHA-256
  b9b7167fdf9666b71e4761b77c6b80ba4f931bc3abf5d6a06362ee561574ef45.

- 2026-09-07T22:57:48+00:00: Recorded command exit 1; command argv SHA-256
  6288ab4209016c669505f7e11aea37a81657c04b662fde6f093c840029b9e323.

- 2026-09-07T22:58:30+00:00: Recorded command exit 1; command argv SHA-256
  da3857c1bea20ccf6e25110fcb3fbb777ca2fd45bc6b994cf944d9748647ac8e.

- 2026-09-07T22:58:50+00:00: Recorded command exit 1; command argv SHA-256
  3671d198576798fbae9a125ee5eea6a53c22de2c9b548f784425460f1bcef08c.

- 2026-09-07T22:59:51+00:00: Recorded command exit 0; command argv SHA-256
  ceaf9690dd16618c0bce89eef639bbbdca7dd0c664cacf89bcbaa9ce5480a607.

- 2026-09-07T23:00:23+00:00: Recorded command exit 1; command argv SHA-256
  55822da2d5ad67344ec272a098de7759894b50aba07b32ae3764959105d9ac15.

- 2026-09-07T23:01:09+00:00: Recorded command exit 0; command argv SHA-256
  179804a32ecebd0d291aa21cedd5342a8d4a5c78a841bb0b211b7c7e7bb9f9ce.

- 2026-09-07T23:01:44+00:00: Recorded command exit 1; command argv SHA-256
  8625e91eddfa7ef31ca8a4274bf6ae14b0863072ea47fa0d70463853ba0b35e5.

- 2026-09-07T23:02:05+00:00: Recorded command exit 0; command argv SHA-256
  26d18f12280270e319db937db16d74181dd8569feb7fdb3180c67d5b798219fd.

- 2026-09-07T23:03:00+00:00: Heartbeat by replay_20260906.

- 2026-09-07T23:03:23+00:00: Recorded command exit 0; command argv SHA-256
  8bf561ad4da403a8fad06938ffe0bd3a83719c38a92a52f8b3e47bd693f8837b.

- 2026-09-07T23:04:16+00:00: Recorded command exit 0; command argv SHA-256
  3bc6094d788d245ebb92787b8c512da1b8b7cd48887b0d6513a0ded033249905.

- 2026-09-07T23:04:37+00:00: Recorded command exit 0; command argv SHA-256
  8f6d792fac0ed0e040c3f8a8e3b278b41e6c44fd87d1c23e66d51a17966c725f.

- 2026-09-07T23:05:35+00:00: Recorded command exit 0; command argv SHA-256
  b542fec45e8d75aadd0747d53dab8176b84a34fb85576213fa30bf3776010cfc.

- 2026-09-07T23:05:58+00:00: Recorded command exit 0; command argv SHA-256
  8fc7aadce740c3eebd282dbec9cc43e109da5b049360b29b92ebb5aec2e59583.

- 2026-09-07T23:06:48+00:00: Recorded command exit 0; command argv SHA-256
  7e32854b60f33a333c4fc2c9e75ad31d884d85263133c287a63571abb7a5b84a.

- 2026-09-07T23:07:07+00:00: Recorded command exit 0; command argv SHA-256
  0c5074a0ae62105bd5d106ac264ea6dccab3bb5c35f402825e7374f5b9a983c3.

- 2026-09-07T23:07:42+00:00: Recorded command exit 1; command argv SHA-256
  864dc346440417a76d69043243c13d80f01ec7f0565d025bb77023cdf670fb55.

- 2026-09-07T23:08:25+00:00: Recorded command exit 0; command argv SHA-256
  3303d946dae393d598616ab5a796b9e2d075d4562cce33c6a3f91824001f29ea.

- 2026-09-07T23:08:45+00:00: Recorded command exit 1; command argv SHA-256
  2426693612504a91c19320572041b5ef4ded5335fee4ca94ca8ed7f36dfbd85c.

- 2026-09-07T23:09:23+00:00: Recorded command exit 0; command argv SHA-256
  25b46b7575cc3c916ca5274ce4046c6f918052a40220467bdebfe69bd30eaee5.

- 2026-09-07T23:09:44+00:00: Recorded command exit 0; command argv SHA-256
  54471d2a93defebd9a2bce5727f6050da834d2548dbef705bd47a3e86833e57c.

- 2026-09-07T23:10:06+00:00: Recorded command exit 0; command argv SHA-256
  ba79ce345e02c10ff571cba07591d945ea8ab86e2b08bf43ccb93cbd173b4caa.

- 2026-09-07T23:10:36+00:00: Recorded command exit 0; command argv SHA-256
  4933efb928cde21ed7d1131564ff379018d7501794259ae431e8dfe03703d5c7.

- 2026-09-07T23:11:16+00:00: Candidate a288bb3485aa2a65ffa79626c3352c6522791138, tree
  dd66c8248986b1d17245e7a4f898db307be5abd7, exact parent 72dd78f72dd74d20654232923dfe2fcff7771dff.
  TLC 1.8.0 checked 3,709 distinct states at depth 17; Alloy 6.2.0 produced one SAT witness and six
  UNSAT assertions; deliberate stale-state TLC and all six weakened Alloy assertions produced
  counterexamples. Rust formal suite, production AtomicStore traces, full workspace
  fmt/Clippy/tests/docs/release, Kani 6/6 plus negative, repository policy, actionlint, cargo-deny,
  Gitleaks, signature and DCO passed. Focused recovery coverage is 97.75% lines, 97.18% regions,
  100% functions; unstable nightly branch instrumentation is 87.5% and is not claimed as 95%.
  Investigated and repaired initial wrong archive filename, Alloy temp/output collision, production
  transition setup, incomplete Kani environment, absent Gitleaks config invocation, and TLC
  source-tree trace residue; final runner is canonical-path, size/hash bounded, mutation-sensitive,
  and leaves the source tree unchanged. Finite safety proof excludes liveness, timing, native
  support, and real crash/filesystem guarantees.

- 2026-09-07T23:12:39+00:00: Recorded command exit 0; command argv SHA-256
  7c7ac5f1a45f8b9ec75d6a0cb2c1e583f7e10281f8684e331e6f091dbf36cfec.

- 2026-09-07T23:13:10+00:00: Published immutable reviewed head
  a288bb3485aa2a65ffa79626c3352c6522791138 with exact absent-ref lease and opened focused PR #57
  against base 72dd78f72dd74d20654232923dfe2fcff7771dff. Initial exact-head runs: formal
  34169250678, quality 34169250636, Rust x86_64/aarch64 34169250637, fault 34169250641,
  emulated-aarch64 34169250633; all were in progress at first query. PR head/base identities and
  mergeability were exact.

- 2026-09-07T23:17:54+00:00: Recorded command exit 0; command argv SHA-256
  bb5713b8423bb3868f9fc5cbf333a9f6dfcbf0ab88e5cfc3362732241405ec37.

- 2026-09-07T23:19:11+00:00: Recorded command exit 0; command argv SHA-256
  1fee7ce3a833ffa5e3a153d5d64da8dfb73737812a349ea0a83154871818ca25.

- 2026-09-07T23:19:47+00:00: Recorded command exit 0; command argv SHA-256
  9c928c3547f8a5a5f6a37996985dc5905999a331ba922862e18dcab78849145f.

- 2026-09-07T23:23:10+00:00: Released after independently reviewed PR #57 exact head
  a288bb3485aa2a65ffa79626c3352c6522791138 merged by signed+DCO no-ff commit
  20ac1e507e678aff463ec5f6c7b37cfcd67a5ad0 with exact parents
  72dd78f72dd74d20654232923dfe2fcff7771dff and a288bb3485aa2a65ffa79626c3352c6522791138. Exact-main
  hosted runs all succeeded: formal 34169558987, quality 34169558969, Rust x86_64/aarch64
  34169558933, fault 34169558934, emulated-aarch64 34169558929. Complete exact-main local postmerge
  fmt, Clippy, workspace tests, docs, release build, repository policy, actionlint, cargo-deny,
  Gitleaks, TLC/Alloy positive and mutation checks, Kani 6/6 and deliberate negative passed; product
  main and feature worktrees were clean and refs synchronized; live doctor passed. Finite evidence
  retains the documented liveness, timing, native, filesystem and 87.5% nightly branch-coverage
  limitations.
