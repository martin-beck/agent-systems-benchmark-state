---
{
  "branch": "codex/ar1849-formal-admission-env-repair",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-13T13:11:59+00:00",
  "depends_on": [],
  "id": "AR-1849",
  "next_action": "Retain workflow-only private TLC admission environment; rebase onto exact v0.7.4 adoption and rerun focused/full gates, review, and CI.",
  "owner": "ar1849-formal-admission-env-luna",
  "plan": "../plans/AR-1849-formal-admission-env-repair.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "mechanical",
    "evidence_digest": "",
    "evidence_ref": "",
    "spec_ref": "specs/AR-1849.json",
    "spec_revision": 1,
    "status": "pending"
  },
  "spec_ref": "specs/AR-1849.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Repair workflow-wide private TLC admission environment for formal CI.",
  "task_revision": 45,
  "title": "Formal admission environment repair",
  "updated_at": "2026-10-13T12:47:00+00:00",
  "worktree_key": "agent-systems-benchmark-state-ar-1849-formal-admission-env"
}
---

The hosted formal workflow scopes `TLC_ADMISSION_QUEUE` and
`TLC_ADMISSION_LOCK` only to the model invocation. The subsequent full
unittest step therefore falls back to the root-owned `/tmp` lock and fails
before the runner tests can execute. Make the approved private paths job-wide,
retain absolute-path and privacy boundaries, and add regression coverage.

- 2026-10-13T11:10:00+00:00: Created as a narrowly scoped successor repair after PR #142 formal CI rejected AR-1841 on the unscoped admission lock.

- 2026-10-13T11:11:41+00:00: Promoted focused successor repair for workflow-wide private TLC
  admission environment.

- 2026-10-13T11:11:59+00:00: Claimed by ar1849-formal-admission-env-luna.

- 2026-10-13T11:12:20+00:00: Recorded command exit 0; command argv SHA-256
  fa8b5b71edf3200d321ee3c09e348eccd55c38732142f7ba47f3a35c7d1b1356.

- 2026-10-13T11:12:32+00:00: Recorded command exit 0; command argv SHA-256
  a1495074bb03d8e7f52befdddceaf088d909f30877e7f3c901be291e8314d521.

- 2026-10-13T11:12:49+00:00: Recorded command exit 127; command argv SHA-256
  fbd60e32e15e10812bc508cbaa142cec210bc6b019622b18d3023b35023c3838.

- 2026-10-13T11:12:59+00:00: Recorded command exit 0; command argv SHA-256
  6b147123626330988a8154de925126794a292f986b18ec02906eaa39b20cc660.

- 2026-10-13T11:13:09+00:00: Recorded command exit 0; command argv SHA-256
  78a6479d88a2a57c0b01a35b4597670b02fdb184f7498e01671813926c8c3e63.

- 2026-10-13T11:13:17+00:00: Recorded command exit 0; command argv SHA-256
  e06dacc6d4d452e01e4a1628cb8b9cf94ac3a308720137c69aa4346a24cd44a3.

- 2026-10-13T11:13:28+00:00: Recorded command exit 0; command argv SHA-256
  96229c636436dd2e86187fe0170fe0291c65a70a2efc90011b9c48d94056791b.

- 2026-10-13T11:13:43+00:00: Recorded command exit 0; command argv SHA-256
  4a6d09b8b6f98a1face652131d09748c968ee736ea7e2dc64525ec24ca85dec3.

- 2026-10-13T11:14:37+00:00: Recorded command exit 0; command argv SHA-256
  6b147123626330988a8154de925126794a292f986b18ec02906eaa39b20cc660.

- 2026-10-13T11:14:44+00:00: Recorded command exit 0; command argv SHA-256
  08b1cd003159b33cbfcecbf52498ab2604d646126132bf932a6f23b64e8f78b1.

- 2026-10-13T11:14:52+00:00: Recorded command exit 0; command argv SHA-256
  078e0d5e8191aa23fbdff0e0000fd643a4a17b4a5c415ac9cb5a6fe280559a06.

- 2026-10-13T11:15:01+00:00: Recorded command exit 0; command argv SHA-256
  5eab89acc6dc4a906fc44c69a3acfbd88b416ab75ccb4dc588fee318a4311a4c.

- 2026-10-13T11:15:42+00:00: Recorded command exit 0; command argv SHA-256
  6b147123626330988a8154de925126794a292f986b18ec02906eaa39b20cc660.

- 2026-10-13T11:15:49+00:00: Recorded command exit 0; command argv SHA-256
  08b1cd003159b33cbfcecbf52498ab2604d646126132bf932a6f23b64e8f78b1.

- 2026-10-13T11:15:57+00:00: Recorded command exit 0; command argv SHA-256
  5af91fe685a3f0a1704756ec8887b7badfcf5e1b94698dbd22649366ce71eb78.

- 2026-10-13T11:16:07+00:00: Recorded command exit 0; command argv SHA-256
  5eab89acc6dc4a906fc44c69a3acfbd88b416ab75ccb4dc588fee318a4311a4c.

- 2026-10-13T11:16:45+00:00: Recorded command exit 0; command argv SHA-256
  e69c2e902c5ef9f746141f76705ef7e0a3dfbf966fe57f16f9d7bfd927afc8dc.

- 2026-10-13T11:25:06+00:00: Recorded command exit 0; command argv SHA-256
  3d101ee1a18f150afda28158255072095465d5ebe132c24c46ee02abbcccaedb.

- 2026-10-13T11:25:15+00:00: Recorded command exit 0; command argv SHA-256
  3f2b347d5aa7a5c5c76c24f7addb5d681ddbf3137b55a7f608e72dc97999e67e.

- 2026-10-13T11:25:23+00:00: Recorded command exit 0; command argv SHA-256
  4be42e12ccdc2f185a668b17c8103af4857455c7861709035c197c9b6f9b8903.

- 2026-10-13T11:26:10+00:00: Recorded command exit 1; command argv SHA-256
  cd63bedf5974650d94441521a9d93843c77a3886b6b85dc0ea9b0bb646d89468.

- 2026-10-13T11:26:23+00:00: Recorded command exit 0; command argv SHA-256
  6ad7dfbc0a41824b52784bbf7c8d9d45b1476101d9d62f3bc80a3fea7decba53.

- 2026-10-13T11:26:31+00:00: Recorded command exit 0; command argv SHA-256
  1eb6b46badbdb84e195440b84c5e2766866e35e2b011860a6f1bab746bb2b9d8.

- 2026-10-13T11:26:38+00:00: Recorded command exit 0; command argv SHA-256
  cd63bedf5974650d94441521a9d93843c77a3886b6b85dc0ea9b0bb646d89468.

- 2026-10-13T11:26:54+00:00: Recorded command exit 0; command argv SHA-256
  65700f26bbb2957c7be386de810dfaacac427a80404fb062df4b8c39d885e6cd.

- 2026-10-13T11:32:11+00:00: Recorded command exit 1; command argv SHA-256
  55029e58f4e767809d6aae0895600c78dbf8d638c4fda21fb39c23050027ebeb.

- 2026-10-13T11:34:49+00:00: Recorded command exit 1; command argv SHA-256
  55029e58f4e767809d6aae0895600c78dbf8d638c4fda21fb39c23050027ebeb.

- 2026-10-13T11:35:48+00:00: Recorded command exit 0; command argv SHA-256
  1753e561f4a9eea3011799f543d7ed1fb274f6f9c6d214c885fe3247e4396b73.

- 2026-10-13T11:36:06+00:00: Recorded command exit 0; command argv SHA-256
  6ad7dfbc0a41824b52784bbf7c8d9d45b1476101d9d62f3bc80a3fea7decba53.

- 2026-10-13T11:36:24+00:00: Recorded command exit 0; command argv SHA-256
  80fecbfff01bd8dd9d2c5682836a456086ca1147c8c2ea606763df90e3ff80ab.

- 2026-10-13T11:36:26+00:00: Recorded command exit 0; command argv SHA-256
  82acbf175fd267f4f6074bde643f4332bf7b5fa343127240fcd8d3038160e2b2.

- 2026-10-13T11:36:34+00:00: Recorded command exit 0; command argv SHA-256
  6ad7dfbc0a41824b52784bbf7c8d9d45b1476101d9d62f3bc80a3fea7decba53.

- 2026-10-13T11:36:42+00:00: Recorded command exit 1; command argv SHA-256
  82acbf175fd267f4f6074bde643f4332bf7b5fa343127240fcd8d3038160e2b2.

- 2026-10-13T11:36:53+00:00: Recorded command exit 128; command argv SHA-256
  648530583690fc84057a27f250208efc8cbb79c13b8e288cc72dba68ab0324eb.

- 2026-10-13T11:37:05+00:00: Recorded command exit 0; command argv SHA-256
  99f4656875599a1086f0499220e6f74c47a388942e530b029a387af8ba3bc2c0.

- 2026-10-13T12:04:28+00:00: Dependency blocker recorded: AR-0029 tag v0.7.3 metadata/runtime
  mismatch prevents immutable vendor sync. Do not weaken vendor verification or alter vendored
  files.

- 2026-10-13T12:04:59+00:00: Recorded command exit 0; command argv SHA-256
  fa8b5b71edf3200d321ee3c09e348eccd55c38732142f7ba47f3a35c7d1b1356.

- 2026-10-13T12:41:52+00:00: Dependency retargeted to corrected Coordinator v0.7.4 release at
  2ea256d0; preserve immutable vendor boundary.

- 2026-10-13T12:45:09+00:00: Recorded command exit 1; command argv SHA-256
  cf56dfc1f49967d16a9299afcad06728c9e30837c00559964ce2ebc58065ccc7.

- 2026-10-13T12:46:12+00:00: Recorded command exit 0; command argv SHA-256
  8ac9a4b628a007ec2fff82b024c102bf6572498af3f438314240edeae4e2c646.

- 2026-10-13T12:46:28+00:00: Recorded command exit 0; command argv SHA-256
  6a075973886059416de4aa06021dbf0a54102baa243ece8060a361c48fe167e0.

- 2026-10-13T12:47:00+00:00: Recorded command exit 1; command argv SHA-256
  6cf0ee5ce970121954a9f21d17ead3c1de635a542bd3675274eb690c4319b861.
