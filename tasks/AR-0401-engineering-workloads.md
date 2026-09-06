---
{
  "branch": "feature/engineering-workloads",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-06T23:31:26+00:00",
  "depends_on": [
    "AR-0101",
    "AR-0103"
  ],
  "id": "AR-0401",
  "next_action": "Repair scratch-root boundary, rerun exact full gates, and submit a signed successor to superseded 3bef7cf for independent review.",
  "observed_branch": "feature/engineering-workloads",
  "observed_dirty": 0,
  "observed_head": "6f808671a232bc9d1afb5c39591049ee50f99c21",
  "owner": "replay-20260906",
  "plan": "../plans/AR-0401.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Deliver bug fix, feature addition, refactoring, test generation, dependency migration, build repair and repository navigation fixtures via extension API.",
  "task_revision": 102,
  "title": "Implement original engineering workloads",
  "updated_at": "2026-09-06T22:10:59+00:00",
  "worktree_key": "agent-systems-benchmark-engineering-workloads"
}
---
## AR-0401

Deliver bug fix, feature addition, refactoring, test generation, dependency migration, build repair and repository navigation fixtures via extension API.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-06T20:38:47+00:00: Promoted after independently verifying all dependencies done; paths are
  disjoint from active AR-0204, AR-0301, and AR-1001, with Cargo/schema integration
  coordinator-fenced.

- 2026-09-06T20:38:57+00:00: Claimed by replay-20260906.

- 2026-09-06T20:39:30+00:00: Recorded command exit 0; command argv SHA-256
  47dad3c04f6979bfb2506154fe679f032429b43cb480062fbaca11acd2c9212a.

- 2026-09-06T20:47:54+00:00: Recorded command exit 128; command argv SHA-256
  0224ceb56d898f25b3e9c9dd853c9fe8d335b8ed7b138c35e801de9ffa857108.

- 2026-09-06T20:48:07+00:00: Recorded command exit 0; command argv SHA-256
  0d8febe67373096d7ff80f56d0b3ab72cff90492070b2d43889f9b00999f1c69.

- 2026-09-06T20:48:15+00:00: Recorded command exit 0; command argv SHA-256
  7f9de8ab07395f814b92ef50bc9c2acffd0a0e0a4bd3547460772318b449d862.

- 2026-09-06T20:48:32+00:00: Recorded command exit 127; command argv SHA-256
  f1a936cdd93ba194c6116308ca6dfd260243b65ca04c78743f74a8429c7b0efa.

- 2026-09-06T20:48:45+00:00: Recorded command exit 101; command argv SHA-256
  abd4b78730f578bba60096109929eacd5532d9635c19a4bcf10af5b9a3d07e5c.

- 2026-09-06T20:49:06+00:00: Recorded command exit 0; command argv SHA-256
  961cc019f427724c8cfe473960df4931a328ac5e5a7e1fb54b1223dd6de482be.

- 2026-09-06T20:49:38+00:00: Recorded command exit 101; command argv SHA-256
  5db8fb77cc132d200b839ec10a4b72d603f45c8b42b8ccd89677bdfdf1a14b11.

- 2026-09-06T20:50:07+00:00: Recorded command exit 128; command argv SHA-256
  4c69ad4ca5026978130c169d0a917e90e10b0fa8eaf1811e2aa0b71bc93f73bb.

- 2026-09-06T20:50:16+00:00: Recorded command exit 0; command argv SHA-256
  8fb02a5dcea683257c6c418304fe657e12621e678aaaee7dd24165469cfac400.

- 2026-09-06T20:51:22+00:00: Recorded command exit 128; command argv SHA-256
  7d72277fe2cb5f326f604b3bc0002473faf5c28b7ea8f53fdf108b167d7c8dea.

- 2026-09-06T20:51:36+00:00: Recorded command exit 1; command argv SHA-256
  2b889aede04852b23fcf32f3fbbe10116542ecec150e82777ba883954b333471.

- 2026-09-06T20:52:34+00:00: Recorded command exit 0; command argv SHA-256
  f8b958da08ab6b51b1b260df9647e6360083a83f1ad02a754619c11c032099a2.

- 2026-09-06T20:53:00+00:00: Recorded command exit 101; command argv SHA-256
  7fabfdc64007a0a20e328e8fac1aa24c0edba679becc2e11f10b32ffb67933d1.

- 2026-09-06T20:53:31+00:00: Recorded command exit 1; command argv SHA-256
  415a31ba1c3d2108b6517366adf59e56573eff2f86f3a4324394f0060e529044.

- 2026-09-06T20:53:56+00:00: Recorded command exit 0; command argv SHA-256
  d5fce88081a24f6385284171e4e6ae6ac4d7dc24caa8c19c8b869c47072c18a1.

- 2026-09-06T20:54:10+00:00: Recorded command exit 101; command argv SHA-256
  7fabfdc64007a0a20e328e8fac1aa24c0edba679becc2e11f10b32ffb67933d1.

- 2026-09-06T20:54:45+00:00: Recorded command exit 0; command argv SHA-256
  daff02cdae3cd62d83631d2dca382ee0420f608fc8f9ffb4f4569c8e8e54b99c.

- 2026-09-06T20:54:56+00:00: Recorded command exit 101; command argv SHA-256
  7fabfdc64007a0a20e328e8fac1aa24c0edba679becc2e11f10b32ffb67933d1.

- 2026-09-06T20:55:09+00:00: Recorded command exit 0; command argv SHA-256
  c0e65f6243585d4c2725bf139e4237bafe8b03ebb62cf1fbdb87e02903e6e99c.

- 2026-09-06T20:55:23+00:00: Recorded command exit 101; command argv SHA-256
  7fabfdc64007a0a20e328e8fac1aa24c0edba679becc2e11f10b32ffb67933d1.

- 2026-09-06T20:55:35+00:00: Recorded command exit 0; command argv SHA-256
  06c45520049572772a9f1eee78a462e816c0f6aa01a6f39548bdef33664cf888.

- 2026-09-06T20:55:45+00:00: Recorded command exit 101; command argv SHA-256
  7fabfdc64007a0a20e328e8fac1aa24c0edba679becc2e11f10b32ffb67933d1.

- 2026-09-06T20:56:42+00:00: Recorded command exit 1; command argv SHA-256
  975172d37d4b5eb6ef31d80a0b318b0d80a8cd4b89507fa65b3acf5ed86e4814.

- 2026-09-06T20:56:57+00:00: Recorded command exit 0; command argv SHA-256
  975172d37d4b5eb6ef31d80a0b318b0d80a8cd4b89507fa65b3acf5ed86e4814.

- 2026-09-06T20:57:08+00:00: Recorded command exit 0; command argv SHA-256
  7fabfdc64007a0a20e328e8fac1aa24c0edba679becc2e11f10b32ffb67933d1.

- 2026-09-06T20:59:26+00:00: Recorded command exit 1; command argv SHA-256
  356205a6e5b8167c44b2220a873d232bf8903065f1677b2da9f6420fec071eaf.

- 2026-09-06T20:59:59+00:00: Recorded command exit 128; command argv SHA-256
  597bb24d2ce1df8ff9c13729618464416090db22290fb908640ce96e509a55e9.

- 2026-09-06T21:00:11+00:00: Recorded command exit 0; command argv SHA-256
  9ad94ae56883f8ee704a7c913279a6e05729837e2a519d9fb57bcb13529676d8.

- 2026-09-06T21:00:25+00:00: Recorded command exit 0; command argv SHA-256
  d2ba4ccd9fcf613baa1e890437891f5674e8feb601bfdfa162cceda5c5695cbe.

- 2026-09-06T21:00:40+00:00: Recorded command exit 101; command argv SHA-256
  310b520603ac3525a1dfaad15d85b21836b3913974361e2e75088dca9ac7662c.

- 2026-09-06T21:01:12+00:00: Recorded command exit 128; command argv SHA-256
  ee0cc76466a2e4f455fc8fc2b8935e120d463c4b12465890b5422cf6b656b446.

- 2026-09-06T21:01:23+00:00: Recorded command exit 0; command argv SHA-256
  aee532170bd3077d670a62627d11818c182a95d65ede8c0ac02c495279f6301c.

- 2026-09-06T21:01:39+00:00: Recorded command exit 0; command argv SHA-256
  0d79fc735c22203f38d2daf8b7819853a2c2ad15742faf226f166f967e0ef10d.

- 2026-09-06T21:01:59+00:00: AR-0401 now has crate-local asb-workloads implementation and seven
  original offline fixture sets: bug fix, feature addition, refactoring, test generation, dependency
  migration, build repair, and repository navigation. Each has a strict v1 WorkloadManifest,
  deterministic SHA-256 content pin and exact fixture byte count, public prompt, passing reference
  patch, failing counterexample, protected semantic grader, and clean prepare/reset/evaluate/cleanup
  lifecycle. Bounds cover 32 files, 1 MiB aggregate, 256 KiB per file, strict absolute normalized
  roots, nonempty destination preservation, symlink/nonregular/non-UTF8 rejection, content-free
  failure names, retryable cleanup ownership, and zero network destinations. Root
  Cargo.toml/Cargo.lock/schemas remain untouched; compilation uses disposable
  /srv/data/projects/.asb-local/ar0401-mirror with only asb-protocol/asb-workloads. Isolated 6 unit
  + 2 public API tests, Clippy warnings denied, fmt, and rustdoc warnings denied pass. Material
  failures preserved: initial git patches required --recount due stale generated hunk counts; first
  build lacked Cargo PATH; direct crate build correctly hit workspace fence; compile exposed unused
  import/Debug/mut/test map errors; reference tests exposed overescaped CR, newline and Makefile tab
  fixture patches plus a feature-grader spelling mismatch; hardening test insertion initially nested
  a test. All were repaired and rerun green; no root integration claim is made.

- 2026-09-06T21:02:01+00:00: Heartbeat by replay-20260906.

- 2026-09-06T21:02:26+00:00: Recorded command exit 0; command argv SHA-256
  6ba45e738cb6a13be535effb07b1f5988a386b12f3a55fb8f0e96c5d734ca420.

- 2026-09-06T21:04:23+00:00: Recorded command exit 127; command argv SHA-256
  222107db27d374ab5114fad3c8642e3882477d4eed0c7e3a970e11fe17a19663.

- 2026-09-06T21:04:54+00:00: Recorded command exit 1; command argv SHA-256
  9909e5db821f60ecb04a1b8502a1d833125f727bdab4f4714a872c907d7d0517.

- 2026-09-06T21:05:19+00:00: Recorded command exit 0; command argv SHA-256
  3a6c4620bb3a4856dfaf6892e50346551bceb7c4b5b968d3915f2c0cc2197761.

- 2026-09-06T21:07:20+00:00: Recorded command exit 0; command argv SHA-256
  249fd2093c4033bc86d92015f028aedfd9ec47fbd0f371db95da4d4c86462523.

- 2026-09-06T21:07:37+00:00: Recorded command exit 0; command argv SHA-256
  0f77749a4e7fee49f65e0ae11dcf47a1c7213b5ac697798c499510e8b962cb81.

- 2026-09-06T21:08:22+00:00: Recorded command exit 0; command argv SHA-256
  a937402c6535a5acf0fe69d738c63b76ea704fdf33b754711fd4e934412c8364.

- 2026-09-06T21:09:03+00:00: Recorded command exit 0; command argv SHA-256
  a937402c6535a5acf0fe69d738c63b76ea704fdf33b754711fd4e934412c8364.

- 2026-09-06T21:09:38+00:00: Coverage hardening completed in the isolated
  /srv/data/projects/.asb-local/ar0401-mirror: cargo llvm-cov all-targets reports 95.13% regions
  (1251/1315), 99.19% lines (739/745), and 100% functions (66/66) for asb-workloads. Added
  adversarial coverage for every manifest field constraint, empty/duplicate/unsafe/oversized
  definitions, malformed and over-count test vectors, all content-free error displays,
  root/workspace/file symlink boundaries, absent parent, and direct oversized reads. The earlier two
  evidence commands failed only because cargo PATH was absent and cargo-llvm-cov does not accept
  --target-dir; both failures are durably recorded and the corrected CARGO_TARGET_DIR invocation
  passed. Root Cargo.toml/Cargo.lock and schemas remain untouched.

- 2026-09-06T21:09:51+00:00: Recorded command exit 1; command argv SHA-256
  e2f7df5065ca24b436412a5cdab756e79eae3e1df41e62e0c6f6be34569ce135.

- 2026-09-06T21:10:03+00:00: Recorded command exit 0; command argv SHA-256
  1879c4dcaee310e566962f34fc55bd8439cc1cf3a033de5f5e8194d708358110.

- 2026-09-06T21:10:22+00:00: Recorded command exit 4; command argv SHA-256
  e2f7df5065ca24b436412a5cdab756e79eae3e1df41e62e0c6f6be34569ce135.

- 2026-09-06T21:10:42+00:00: Recorded command exit 0; command argv SHA-256
  7756a50c46be5ee7ef92ae7a32448f5f46491e27762b1fa5fe780dd5ede58057.

- 2026-09-06T21:11:13+00:00: Recorded command exit 0; command argv SHA-256
  4fe4f886b2e3f0aacbd0e582892ae816509236a7e01beb06f2103031c361abb6.

- 2026-09-06T21:13:01+00:00: Recorded command exit 0; command argv SHA-256
  d5cc8c4fe14dadf5ba904c24d53413cab186975ea08927dcff99769679b1230c.

- 2026-09-06T21:14:19+00:00: Recorded command exit 0; command argv SHA-256
  aea275b8dfc363ee30d64e0caa9e2598c2bc89656441acba3943c43820b4294e.

- 2026-09-06T21:14:38+00:00: Recorded command exit 0; command argv SHA-256
  509d2dc7cf41692acac3d67f6e36a1e7e9fb68695550354c50c1ae7595220dec.

- 2026-09-06T21:14:57+00:00: Final path audit closed ancestor-symlink resolution: prepare now
  requires the existing parent canonical path to equal its lexical absolute path and rejects
  non-directory/symlink parents; a linked-ancestor negative proves fail-closed behavior. README now
  precisely says existing destinations, lexically unnormalized roots, and observed symlink
  ancestors/objects. Affected fmt, Clippy -D warnings, 9 unit plus 2 public lifecycle tests, privacy
  scan and Gitleaks pass. Updated coverage is 95.03% regions (1280/1347), 99.21% lines (752/758),
  100% functions. Locked isolated release build, full tests, rustdoc, cargo audit and
  repository-configured cargo-deny pass. Remaining boundary: product is still crate-only/untracked
  on base 68f313f; root workspace/lock/schema remain untouched pending coordinator fence transfer
  and current-main rebase.

- 2026-09-06T21:36:56+00:00: Recorded command exit 0; command argv SHA-256
  485a75b8814f5b07dca5e1bbc4c5cff1836cf99c98809882b25d99ab4fb6f648.

- 2026-09-06T21:39:02+00:00: Recorded command exit 0; command argv SHA-256
  2cecaaa4c79ccbad35e740d00ba7d0e9b9bb4e63c4b51c46e1a8e57f03c38e06.

- 2026-09-06T21:39:47+00:00: Recorded command exit 0; command argv SHA-256
  84b70ee03f70d4131a909688c760d3028e85dba263b7c764cff614e45a0e662c.

- 2026-09-06T21:40:50+00:00: Recorded command exit 0; command argv SHA-256
  3f863e9c7095b6d0d90a4a6a44f06205f9509404c86a8e5965be89865f4ed59a.

- 2026-09-06T21:41:08+00:00: Recorded command exit 1; command argv SHA-256
  858ec36703ebd62232d31197a2d185dcf90bda5ee8800da52d2dabec6bd277a6.

- 2026-09-06T21:41:23+00:00: Recorded command exit 1; command argv SHA-256
  aca151054677a1d5ebd8fbdd5c493bf22ccf340d9d7b2f81a57681868c6fb399.

- 2026-09-06T21:41:56+00:00: Recorded command exit 0; command argv SHA-256
  537b282f0c9ad8c149986e625a7d27c251dff1b91a50c0f543be7373948424c8.

- 2026-09-06T21:42:07+00:00: Recorded command exit 2; command argv SHA-256
  de55507cb93cd50fb828b274f114562a4b271272871efcc9aafeaac455569393.

- 2026-09-06T21:43:22+00:00: Recorded command exit 101; command argv SHA-256
  21afa6f09120d8c315fc28f878c0182c0e0d4f917eec2bfc1f9ea54839c46795.

- 2026-09-06T21:44:16+00:00: Recorded command exit 0; command argv SHA-256
  69e5f5edc01b78b1d6fed4ce6d5b9efcd3223f94d462fe727f3a78eefbaf5640.

- 2026-09-06T21:44:34+00:00: Recorded command exit 0; command argv SHA-256
  4d91e6392bb639debbe694ff8977f99548df811b81d6bf38281954f8fc339c2d.

- 2026-09-06T21:45:02+00:00: Recorded command exit 0; command argv SHA-256
  728947a65cc0b82ad21d5382020944fe585ad9fea22b4d1cdde613c786449f14.

- 2026-09-06T21:46:48+00:00: Recorded command exit 0; command argv SHA-256
  66911dc5348a2aa59076c4da19f17c8324092a22b7506979975c9f4491f4697a.

- 2026-09-06T21:47:09+00:00: Signed+DCO AR-0401 candidate 3bef7cfada4c419daefa2744cb043a75b314541d,
  tree 4bf07e662264befb7b2d21530d1d45e179e00a89, is one commit on exact signed main b7e9078. Scope
  is 34 paths: Cargo workspace member, one additive asb-workloads lock entry, and the new
  crate/fixtures only; worktree is clean. Full committed-tree gates pass: fmt, locked workspace
  Clippy warnings denied, all workspace tests, rustdoc warnings denied, locked release build,
  cargo-deny/audit, repository coverage, formal Loom/state/production traces, platform
  manifests/negatives, actionlint, zizmor, introduced-history Gitleaks, repository
  signature/DCO/SPDX/link/scope policy, and all controlled failure fixtures. Coverage reports
  workspace 93.77% regions/97.01% lines and asb-workloads 95.03% regions/99.21% lines/100%
  functions. Four zero-context patch fixtures were normalized after git diff --check detected
  required unified-diff context whitespace; first focused rerun correctly failed until test
  application added explicit --unidiff-zero, then reference/counterexample and all full gates reran
  green. Two test_failure_paths attempts failed only from incorrect analyzer bin directory then
  missing Cargo PATH; corrected pinned PATH/bin invocation passed every negative. Native aarch64
  remains unclaimed until hosted exact-head CI.

- 2026-09-06T22:01:26+00:00: Heartbeat by replay-20260906.

- 2026-09-06T22:01:54+00:00: Recorded command exit 0; command argv SHA-256
  e14af162307de7cfce6e79ec03a878f7ea635bf2219e88a0f1d6503f69eb18b0.

- 2026-09-06T22:02:59+00:00: Recorded command exit 128; command argv SHA-256
  9f25b4a3dc1315764a801516638b7f85d050f0cc5789ece8cc3e66a46da89a4d.

- 2026-09-06T22:03:21+00:00: Recorded command exit 128; command argv SHA-256
  9f25b4a3dc1315764a801516638b7f85d050f0cc5789ece8cc3e66a46da89a4d.

- 2026-09-06T22:03:48+00:00: Recorded command exit 0; command argv SHA-256
  b7b9aec211c28f58ca9155225378d1b548a7ee7e922067aa5e37b3f61922b99d.

- 2026-09-06T22:04:05+00:00: Recorded command exit 0; command argv SHA-256
  3805bc843c4c3e9690443fa119fed8b0f0c2f6ac9fe88663ab6a0a632fb7a9a9.

- 2026-09-06T22:04:15+00:00: Recorded command exit 0; command argv SHA-256
  428f533a711f3769c2438c7a5e1d19e66b644fff32bfe8310bf8659f66ad3fc1.

- 2026-09-06T22:04:46+00:00: Recorded command exit 0; command argv SHA-256
  e26b55cfd93661a30c37cc6dbab5f9afbdb924d9c11c3bee41229267c20fee44.

- 2026-09-06T22:05:11+00:00: Coordinator review found six failed reference-patch attempts leaked
  under /tmp because workload tests used std::env::temp_dir. Read-only audit verified all six exact
  mode-700 directories were generated AR-0401 fixture roots with valid public workload owner markers
  and no live workload process. Removed only those exact generated directories; removal is
  nonrecoverable but they contained reproducible public test material. Repair now routes test
  attempts through absolute ASB_TEST_SCRATCH when configured, otherwise an absolute CARGO_TARGET_DIR
  subdirectory, while retaining an OS-temp fallback for portable external CI; relative configured
  paths fail closed. All controlled commands set TMPDIR and ASB_TEST_SCRATCH under
  /srv/data/projects/.asb-local. Focused 9 unit and 2 public API tests pass, no attempt residue
  remains in configured scratch or /tmp, and a wrapped negative proved relative ASB_TEST_SCRATCH
  rejection without creating the relative directory. Two initial patch-check commands failed because
  the hand-written unified diff final hunk count was stale; git apply --recount applied the reviewed
  patch content.

- 2026-09-06T22:05:26+00:00: Recorded command exit 0; command argv SHA-256
  e290faef7d12d2fdee27b86a7aab3ce85801b0be1a08944cdb9e5bb926f13bf3.

- 2026-09-06T22:05:32+00:00: Recorded command exit 0; command argv SHA-256
  c9e06dac82b5a0e6855b31ef550284c3b779f5ded3ff31c1bf28237c2632723a.

- 2026-09-06T22:06:01+00:00: Recorded command exit 1; command argv SHA-256
  e4fb0a6ff23f8f1999d2b9b84236be12e594a29a1df37aea2529845b3e8cd76d.

- 2026-09-06T22:06:47+00:00: Recorded command exit 0; command argv SHA-256
  ea1e4945b46f81632255784d929276b6a4567cc3dc160357f4faace8a3e86aa1.

- 2026-09-06T22:07:33+00:00: Recorded command exit 0; command argv SHA-256
  4334fc740a2a0fc0e0094bfc90a43f352e5a9d906b62a8822aea825ee073231e.

- 2026-09-06T22:08:28+00:00: Recorded command exit 0; command argv SHA-256
  5b9ac9f86af5a6b4a237e85e9b13c7c230a8a2ad70996e5f045ce949efd0ec17.

- 2026-09-06T22:08:34+00:00: Recorded command exit 0; command argv SHA-256
  7b21c88f74795a2bdea1a2b863c360f60dab54151a0555b2df8e400519cdfa01.

- 2026-09-06T22:08:48+00:00: Recorded command exit 0; command argv SHA-256
  ed183408be4521c9be7f94484b6e7a42f2422f388bd906ea9fd07f7e7f3ec79d.

- 2026-09-06T22:08:54+00:00: Recorded command exit 0; command argv SHA-256
  f55b7c899706e845114d5bc3a137d081ab8b6cc6ee48860f4ce4c8abdd59913f.

- 2026-09-06T22:09:46+00:00: Recorded command exit 0; command argv SHA-256
  62e710045074a53d6215938f2cae41d54fc31ab43b30eeb1ca4ad9bbce703ac3.

- 2026-09-06T22:10:32+00:00: Recorded command exit 0; command argv SHA-256
  4211b26c7ccdc6cfef661b2ebc23c70491308db6aa55c2d5171493069a1ca719.

- 2026-09-06T22:10:59+00:00: Recorded command exit 101; command argv SHA-256
  3c82630bd308a91fe878d4ac8419c133673490ba1d7a2392ee59b2e6d33d02bb.
