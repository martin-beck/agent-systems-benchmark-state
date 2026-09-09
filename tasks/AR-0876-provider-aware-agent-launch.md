---
{
  "branch": "feature/provider-aware-agent-launch",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-0102",
    "AR-0103",
    "AR-0313",
    "AR-0316",
    "AR-0317",
    "AR-0318",
    "AR-0319",
    "AR-0320",
    "AR-0869"
  ],
  "id": "AR-0876",
  "next_action": "Create signed+DCO follow-up parented bc071fd, force-with-lease origin/main 32562e8, rerun exact-main postmerge workflows.",
  "observed_branch": "feature/provider-aware-agent-launch",
  "observed_dirty": 0,
  "observed_head": "7c9daf795b02d1692e87a6be4d0087c163050ad3",
  "owner": "",
  "plan": "../plans/AR-0876.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "done",
  "summary": "Apply validated provider selections at the authoritative agent launch boundary and reject conflicting runtime configuration.",
  "task_revision": 99,
  "title": "Wire provider-aware agent launches",
  "updated_at": "2026-09-09T01:27:19+00:00",
  "worktree_key": "agent-systems-benchmark-provider-aware-agent-launch"
}
---
## AR-0876

Close the AR-0869 execution-wiring gap by making its content-addressed provider selection an
authoritative input to the actual adapter process launch, rather than provenance-only metadata.

Implementation has not started. Read the linked plan before claiming.


- 2026-09-09T00:30:52+00:00: AR-0871 is merged and fully verified; AR-0876 is the highest-priority
  dependency-ready leaf that closes provider-selection execution wiring.

- 2026-09-09T00:30:55+00:00: Claimed by replay_20260909.

- 2026-09-09T00:31:20+00:00: Recorded command exit 0; command argv SHA-256
  d7c226a60b6735868b5a8965666285114b01921a4fd641a6c89c52f51e831b01.

- 2026-09-09T00:33:44+00:00: Heartbeat by replay_20260909.

- 2026-09-09T00:37:29+00:00: Recorded command exit 0; command argv SHA-256
  9fe73088536dc5e06523f8e18e23dd6be47e78a90426e7b579b7067624f73c84.

- 2026-09-09T00:37:46+00:00: Heartbeat by replay_20260909.

- 2026-09-09T00:38:02+00:00: Recorded command exit 0; command argv SHA-256
  56b228d10c091c83b96d7316d8d47def00bf0962640ede14a4b12cbb2094f07f.

- 2026-09-09T00:38:59+00:00: Heartbeat by replay_20260909.

- 2026-09-09T00:39:03+00:00: Recorded command exit 0; command argv SHA-256
  a7d6b628d30e583db6df7759a836c6fde7df539f25510ea41031a87c62fe9ea0.

- 2026-09-09T00:40:41+00:00: Heartbeat by replay_20260909.

- 2026-09-09T00:40:51+00:00: Recorded command exit 0; command argv SHA-256
  f62c661b82a90472684d6ad074a742ebece91dafce7de4f468389a35a12ac00b.

- 2026-09-09T00:41:19+00:00: Heartbeat by replay_20260909.

- 2026-09-09T00:41:24+00:00: Recorded command exit 0; command argv SHA-256
  9214ef896a6b61c45637dc024149c7d08b8f222d0b658b5cd340010f5271d46a.

- 2026-09-09T00:42:32+00:00: Heartbeat by replay_20260909.

- 2026-09-09T00:42:37+00:00: Recorded command exit 101; command argv SHA-256
  814fca455e3ba22c34d5389553e345fb9ddf1e645afd2ebd791e4b78984d0786.

- 2026-09-09T00:43:16+00:00: Recorded command exit 0; command argv SHA-256
  5bf699b95b8c514d6effac6dbc2be6013575611b144a06c747536d187e583ef8.

- 2026-09-09T00:43:23+00:00: Recorded command exit 101; command argv SHA-256
  ec488f391ae4bc2f24b23f2a1f1edc93bd38ca7c416f7fa93c8ded4fb0b7ca60.

- 2026-09-09T00:43:34+00:00: Heartbeat by replay_20260909.

- 2026-09-09T00:43:38+00:00: Recorded command exit 0; command argv SHA-256
  8ac918ff2f721c0cbeb365213414bd96fba625d2259fb4d9d8040feb612e7236.

- 2026-09-09T00:43:58+00:00: Heartbeat by replay_20260909.

- 2026-09-09T00:44:02+00:00: Recorded command exit 0; command argv SHA-256
  bd15653064fc694558b26c2bcc2b4aede6fcf3bac6b4cded456c569f99accbd3.

- 2026-09-09T00:44:33+00:00: Heartbeat by replay_20260909.

- 2026-09-09T00:45:17+00:00: Recorded command exit 0; command argv SHA-256
  ebeec6162a51506bd6dae4a57dddb77a32cb3af1cf8f7e05befee8e3bd28f719.

- 2026-09-09T00:45:56+00:00: Heartbeat by replay_20260909.

- 2026-09-09T00:45:58+00:00: Recorded command exit 0; command argv SHA-256
  49a18c8f11b1a2d093b69d5b1e4413552ae0bc922f7b5983069d52d3b10cc6f3.

- 2026-09-09T00:46:06+00:00: Recorded command exit 0; command argv SHA-256
  6b917aabd1bdb436194b4426d4acce75ab6bd08ae9bc8d8a618e6352a31a137d.

- 2026-09-09T00:46:34+00:00: Implemented signed commit 45999650: added constructor-controlled
  ProviderLaunchV1 binding, canonical launch digest, projection/tamper/privacy tests, CLI pre-spawn
  binding and non-secret launch environment, durable manifest/report identity, fixtures, and
  documentation. Focused CLI/agent tests and workspace test plus clippy passed; next action is
  independent review, exact-head CI, and repair if required.

- 2026-09-09T00:46:53+00:00: Recorded command exit 0; command argv SHA-256
  918a3be8115380b3ca5df46a6140376f49a2659d83c88d0b4c3bbab81f17a755.

- 2026-09-09T00:47:16+00:00: Recorded command exit 0; command argv SHA-256
  b13c42f7cc043c64aa511f89f8dee2c4748dd23a13704d69da805358d3a7d534.

- 2026-09-09T00:47:24+00:00: Recorded command exit 0; command argv SHA-256
  9816f39cfe20bd6dc6df5d7df1682e3c76a4b0de8d77974baa8b05e818b71a75.

- 2026-09-09T00:47:34+00:00: Recorded command exit 0; command argv SHA-256
  88fa7186fe7a47cafde98549e48d32802236eca529608fb488e4f267317dfd85.

- 2026-09-09T00:47:42+00:00: Recorded command exit 0; command argv SHA-256
  3a315ff4db2e103070338c4e7ce7277e12596177f16a02b6688a77fbbf793067.

- 2026-09-09T00:48:06+00:00: Immutable PR #93 opened at signed+DCO head 45999650 on exact main
  dca243ab. Exact-head required CI is running; current completed checks: AWQ and Huawei header
  validation passed. No feature work proceeds until all required gates are terminal green.

- 2026-09-09T00:50:17+00:00: Heartbeat by replay_20260909.

- 2026-09-09T00:50:32+00:00: Recorded command exit 0; command argv SHA-256
  5ec35fcaad5a6c6bd145073a63b94b564ee0ad178a80ee7fd24a540996f2470e.

- 2026-09-09T00:50:51+00:00: Recorded command exit 0; command argv SHA-256
  16c083d3c272b073619797084e784192f83c0e45f3f7fa6f372a2ac715f9666d.

- 2026-09-09T00:51:33+00:00: Recorded command exit 0; command argv SHA-256
  1e4d8d434e76f20af551249372d861428f1f2beeef34b02d32877135a7c91c0d.

- 2026-09-09T00:51:40+00:00: Recorded command exit 0; command argv SHA-256
  40b754580b11c57d1b5938e58489cb520de17417151a2ee5e38d62f1a98d8858.

- 2026-09-09T00:51:52+00:00: Recorded command exit 0; command argv SHA-256
  f2dad8c5e2ba3038e703841a610082e1c4b3888488207889e5e917cd68aa5a1d.

- 2026-09-09T00:52:22+00:00: CI failure on original head 45999650 was diagnosed from job logs:
  formal TLC asset 551007111 returned HTTP 404. Root cause was an upstream release asset
  replacement, not launch code. Repaired same branch with signed+DCO commit 251d676, pinning
  official asset 551658253, size 4489044, digest 0d1f3b48..., updated formal metadata/tests/docs;
  local formal test and temporal runner passed. PR #93 now reruns at exact head 251d676.

- 2026-09-09T00:53:57+00:00: Heartbeat by replay_20260909.

- 2026-09-09T00:58:56+00:00: Heartbeat by replay_20260909.

- 2026-09-09T00:59:02+00:00: Recorded command exit 101; command argv SHA-256
  0599275c8aa0355961fe7672b2edd2406cd449ca785541744d20a7ffe1e54cc8.

- 2026-09-09T00:59:17+00:00: Recorded command exit 101; command argv SHA-256
  30b0fb6ce39f801f3066326fc4b417f989203b6965cc79103552a72259a009de.

- 2026-09-09T00:59:59+00:00: Heartbeat by replay_20260909.

- 2026-09-09T01:00:03+00:00: Recorded command exit 101; command argv SHA-256
  3ba65d349e4be4e7e666d162a8746fef1dc195b989c1ce6e116cb5aa1bbe4ed3.

- 2026-09-09T01:00:26+00:00: Recorded command exit 101; command argv SHA-256
  ec488f391ae4bc2f24b23f2a1f1edc93bd38ca7c416f7fa93c8ded4fb0b7ca60.

- 2026-09-09T01:00:59+00:00: Heartbeat by replay_20260909.

- 2026-09-09T01:01:05+00:00: Recorded command exit 0; command argv SHA-256
  c7a379ede77c800db4360ff7fc9a701a56ba2dafee97b3f7d847e1b992b2a934.

- 2026-09-09T01:01:28+00:00: Recorded command exit 0; command argv SHA-256
  acadaeae01a342919e31ab32252a06812b3153c476670b8f325de0e8881d4337.

- 2026-09-09T01:01:36+00:00: Recorded command exit 0; command argv SHA-256
  e0a5015e29a6dcbef94551bbeebb53faf9feeb7abbc7da40fd88c97f111319b4.

- 2026-09-09T01:01:54+00:00: Recorded command exit 0; command argv SHA-256
  f2dad8c5e2ba3038e703841a610082e1c4b3888488207889e5e917cd68aa5a1d.

- 2026-09-09T01:02:08+00:00: Heartbeat by replay_20260909.

- 2026-09-09T01:02:38+00:00: Recorded command exit 0; command argv SHA-256
  ebeec6162a51506bd6dae4a57dddb77a32cb3af1cf8f7e05befee8e3bd28f719.

- 2026-09-09T01:03:52+00:00: Heartbeat by replay_20260909.

- 2026-09-09T01:03:56+00:00: Recorded command exit 63; command argv SHA-256
  1383d6b4232a45b0b2107e5b657945439622f83e47b8a6021fbcf4eff7591605.

- 2026-09-09T01:04:34+00:00: Recorded command exit 63; command argv SHA-256
  16c083d3c272b073619797084e784192f83c0e45f3f7fa6f372a2ac715f9666d.

- 2026-09-09T01:05:30+00:00: Heartbeat by replay_20260909.

- 2026-09-09T01:05:36+00:00: Recorded command exit 0; command argv SHA-256
  16c083d3c272b073619797084e784192f83c0e45f3f7fa6f372a2ac715f9666d.

- 2026-09-09T01:06:12+00:00: Recorded command exit 0; command argv SHA-256
  1e4d8d434e76f20af551249372d861428f1f2beeef34b02d32877135a7c91c0d.

- 2026-09-09T01:06:21+00:00: Recorded command exit 0; command argv SHA-256
  8adc2c81bfdf7324491897ae8ed6c479b15d89c879f9c7b4ac12c2ee54ce7e1a.

- 2026-09-09T01:06:32+00:00: Recorded command exit 0; command argv SHA-256
  f2dad8c5e2ba3038e703841a610082e1c4b3888488207889e5e917cd68aa5a1d.

- 2026-09-09T01:06:53+00:00: Final review found the adapter projection was being synthesized by the
  CLI. Tightened it in signed commit 26af8e6 to derive from OpenAiProfile::translate, with private
  projection fields/getters and exact per-adapter model/API mode; focused tests passed. A second
  formal CI retry showed GitHub replaced the TLC asset again; signed commit 7c9daf7 pins the current
  release URL bytes (asset 551679598, 4489230 bytes, digest 13885c09...). Local temporal runner
  passes. PR #93 now reruns at 7c9daf7.

- 2026-09-09T01:09:39+00:00: Heartbeat by replay_20260909.

- 2026-09-09T01:12:44+00:00: Recorded command exit 0; command argv SHA-256
  70bd7b23cb8e1254deb8a25efa6c8e4e8b5b8b03f74f2b659da46a6f2dc72380.

- 2026-09-09T01:12:53+00:00: Recorded command exit 0; command argv SHA-256
  2ed9ed195c0971bd0b30f6089a8954c118efab71ce133511107173551966e0e9.

- 2026-09-09T01:13:06+00:00: Recorded command exit 0; command argv SHA-256
  869f4fe8ee37b442566fc225cad27f94cc1c35052ac8bd5144bf13cfedf230cc.

- 2026-09-09T01:14:16+00:00: Post-merge exact-main policy workflow failed on merge commit 716a8f1:
  repository_policy.py reported no matching Signed-off-by trailer. All PR #93 exact-head checks were
  green; this is an integration-boundary defect. Release is preempted. Repair must replace only the
  merge boundary with a signed+DCO no-ff merge using guarded force-with-lease, then rerun exact-main
  postmerge workflows.

- 2026-09-09T01:14:36+00:00: Recorded command exit 0; command argv SHA-256
  35f4e4d75f439e6903cd23f824c29060a52792a5be80c9fe177331b361c99ba3.

- 2026-09-09T01:14:44+00:00: Recorded command exit 0; command argv SHA-256
  4370da346bc8314b159e94c1ee24bb530f605c1ca679776865fc33ecc70b936a.

- 2026-09-09T01:15:01+00:00: Recorded command exit 0; command argv SHA-256
  3f91514dfc45a3183ef671ac265d82db7e19cc4e07f4aec5dc3203999150f530.

- 2026-09-09T01:15:29+00:00: Heartbeat by replay_20260909.

- 2026-09-09T01:16:15+00:00: Recorded command exit 0; command argv SHA-256
  ac61978be9ce6a6cbcab8cb2ddfa1912f1e51e545bae44b1f73502ffc9392a71.

- 2026-09-09T01:17:14+00:00: Post-merge repository-quality retry on signed replacement bc071fd
  failed before policy evaluation because workflow RANGE_BASE remained old unreachable merge
  716a8f1: invalid revision range. The working tree and formal/Rust postmerge gates are otherwise
  green/in progress. Preserve both histories and add a signed bridge merge with first parent bc071fd
  so the configured base remains reachable; then rerun exact-main workflows.

- 2026-09-09T01:17:33+00:00: Recorded command exit 0; command argv SHA-256
  b3fca686654d9ccd6062eacf0fc666e6abcb469ce5d79e7f08b13063231d5d1a.

- 2026-09-09T01:17:51+00:00: Recorded command exit 0; command argv SHA-256
  9e0700745adbe8ee2147f1c1c4363345891a6f28ca8101bff8281a3c0a749ce3.

- 2026-09-09T01:18:42+00:00: Policy retry on bridge 32562e8 still rejected obsolete 716a8f1 because
  rev-list follows the bridge second parent. Repairing by dropping that second-parent reference:
  final main will be a signed+DCO normal follow-up parented to valid signed merge bc071fd, with no
  bad commit in the changed range.

- 2026-09-09T01:18:59+00:00: Recorded command exit 0; command argv SHA-256
  90fe3615c89020060455ac02f26a41f888fc7c61a49b36057b77b12ccfeacf9e.

- 2026-09-09T01:19:07+00:00: Recorded command exit 0; command argv SHA-256
  f49492fa5dac983ebf3738fed0161b22b1a3c355bc0dad36ee69bc0575eb182c.

- 2026-09-09T01:19:20+00:00: Recorded command exit 0; command argv SHA-256
  2d4d15d43fda7d7e2fcf29e2f35a97e98856bafd592f858fabc087464c7ea412.

- 2026-09-09T01:20:36+00:00: Recorded command exit 0; command argv SHA-256
  59ea39c5251954f266b911a3e440e76f4d88773f38867540a1be6df2f047523c.

- 2026-09-09T01:20:45+00:00: Recorded command exit 0; command argv SHA-256
  616a928327393c6641c8c7ccd99931aee881d490534707ec6a6951ba79f6a2bc.

- 2026-09-09T01:20:57+00:00: Recorded command exit 0; command argv SHA-256
  f78711fcb170f9a90faaa3197f67d22beda67d3c4d135ee5ef0e113496d21ff5.

- 2026-09-09T01:24:25+00:00: Heartbeat by replay_20260909.

- 2026-09-09T01:27:19+00:00: AR-0876 complete and released. Product feature commits 4599965,
  251d676, 26af8e6, 7c9daf7 merged through signed no-ff boundary bc071fd, followed by signed
  reachable postmerge boundary f2028d7. PR #93 exact-head 7c9daf7 and final exact-main tip f2028d7
  required checks are all green: Rust x86_64/aarch64, emulated aarch64, formal TLC/Alloy/Kani/Loom,
  faults/fuzz/mutation, repository quality, Huawei headers, and AWQ. Local workspace tests/clippy
  and postmerge local tests passed. All temporary integration worktrees were clean.
