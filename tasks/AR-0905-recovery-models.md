---
{
  "branch": "feature/recovery-models",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-08T01:28:29+00:00",
  "depends_on": [
    "AR-0102",
    "AR-0104",
    "AR-0204",
    "AR-0503"
  ],
  "id": "AR-0905",
  "next_action": "Translate Agent Relay's TLA+/Alloy/executable-model pattern to ASB run and replay domains.",
  "observed_branch": "feature/recovery-models",
  "observed_dirty": 15,
  "observed_head": "9d17563f39c1eb51f17309578430a13a4d87b1f1",
  "owner": "replay_20260906",
  "plan": "../plans/AR-0905.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Apply bounded formal models to run lifecycle, leases, recovery, replay cursors and uncertain external effects.",
  "task_revision": 39,
  "title": "Model execution recovery and worker fencing",
  "updated_at": "2026-09-07T22:49:53+00:00",
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
