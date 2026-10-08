---
{
  "branch": "repair/ar-1747-coordinator-unblock-vendor",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-08T18:17:08+00:00",
  "depends_on": [],
  "id": "AR-1747",
  "next_action": "Promote and claim; synchronize the reviewed upstream Coordinator development identity that adds provenance-checked unblock, then qualify the complete ASB state vendor closure and blocked-task transition fixtures.",
  "owner": "codex-asb-ar1747-vendor-20261008",
  "plan": "../plans/AR-1747-coordinator-unblock-vendor-adoption.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_ref": "specs/AR-1747.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Adopt the official Coordinator development unblock capability in ASB state so AR-1722 can be reopened through a supported provenance-checked transition.",
  "task_revision": 24,
  "title": "Adopt Coordinator unblock support for AR-1722",
  "updated_at": "2026-10-08T17:06:01+00:00",
  "worktree_key": "agent-systems-benchmark-state-ar-1747-coordinator-unblock-vendor"
}
---

ASB state currently vendors Coordinator v0.3.57, whose `resume` command accepts
only a valid pause snapshot. AR-1722 is externally blocked and has no pause
snapshot, so it cannot be reopened safely with the installed command set.
Upstream development commit `e863b57edc7f7a21b2aff2c7b45ce226e12637d2`
(tree `eee603591b917eeca244425559d7c67bb88a7268`) contains the independently
reviewed provenance-checked `unblock` transition and its complete formal vendor
closure. This AR owns exact adoption and downstream qualification; it must not
fabricate a pause, edit AR-1722 directly, or change ASB product runtime code.

- 2026-10-08T16:15:59+00:00: Official upstream Coordinator e863b57 already contains the reviewed
  unblock repair; exact downstream development vendor adoption is dependency-ready and path-isolated
  from AR-1746.

- 2026-10-08T16:17:08+00:00: Claimed by codex-asb-ar1747-vendor-20261008.

- 2026-10-08T16:17:14+00:00: Recorded command exit 0; command argv SHA-256
  321c534968b9c456a64caf5e6d09b63780c507f97548057d2bfe31edcfd73ff4.

- 2026-10-08T16:18:22+00:00: Recorded command exit 0; command argv SHA-256
  9811681c1d756cb583e733f64feb3306dcb60dbccc1ce655f0e9d174df4d13ed.

- 2026-10-08T16:21:42+00:00: Recorded command exit 0; command argv SHA-256
  b441e12f5aaf7da29555cd380addd8e739f421fa238e5f229ef76c7ec0483513.

- 2026-10-08T16:22:17+00:00: Recorded command exit 0; command argv SHA-256
  ad0356d5ddf070012b883621bffe60f5e38f37a5bce5bed0322d506e33f34d89.

- 2026-10-08T16:23:25+00:00: Recorded command exit 0; command argv SHA-256
  fec63797cd58c7d66faaded7b85b6950838c1e070fb864fbab0c3b6e26eb5d6e.

- 2026-10-08T16:23:57+00:00: Recorded command exit 0; command argv SHA-256
  098032cc6f966bf4b8de6774d1870b51a66c7d8c6a1b2a8609d014022ba43e7a.

- 2026-10-08T16:35:48+00:00: Recorded command exit 128; command argv SHA-256
  6277e66c506fd007d5f2d98119f1c3fcdf03a71967b5e474185bc558f9e4904b.

- 2026-10-08T16:50:04+00:00: Recorded command exit 0; command argv SHA-256
  22fda1bfad2e346d78ef52139e226051d0eb6ebc6d4e886f541c2931d15a5f25.

- 2026-10-08T16:52:14+00:00: Recorded command exit 0; command argv SHA-256
  6532337c5032d4d6925093fcca4bb25098786bfa5cac379ac14f4d2d912001e3.

- 2026-10-08T16:52:54+00:00: Recorded command exit 0; command argv SHA-256
  bb030e778d0dc783c28c64ed2a3d987f49f40be7e4e90d634f07375906e90b8d.

- 2026-10-08T16:53:52+00:00: Recorded command exit 1; command argv SHA-256
  aa08aa0e2f461edd4def4f67bf43f92beed69c6f88fa7f938a9affe7ef7d5383.

- 2026-10-08T16:54:43+00:00: Recorded command exit 0; command argv SHA-256
  4d694de3d5c5cb03473609f5080b6b19f2e5cac76c146232e5d2358af5d549ec.

- 2026-10-08T16:55:42+00:00: Recorded command exit 0; command argv SHA-256
  868955f5bd58e126d21cf06b99add85fa86c75f27dd1ac40faf673390a3d6447.

- 2026-10-08T16:58:20+00:00: Recorded command exit 0; command argv SHA-256
  22ecbe864b22a97a4740d8a859136ca4ab32582a66d3123d0c1e028bd6d66997.

- 2026-10-08T17:00:40+00:00: Recorded command exit 0; command argv SHA-256
  5a0a3751d7ced533e05b8a0199fff80a5920087030d9e331783505bda89f5608.

- 2026-10-08T17:01:22+00:00: Recorded command exit 1; command argv SHA-256
  ab759baf719b33b54c5d06898d9dcb5dc961a23c970bfe70e26d96cc1a9a3582.

- 2026-10-08T17:01:57+00:00: Recorded command exit 0; command argv SHA-256
  3ed3b32bae108beb803eaea5afe6d2b91cd668649824b806cf5b8de101fd0c97.

- 2026-10-08T17:02:39+00:00: Recorded command exit 0; command argv SHA-256
  ab759baf719b33b54c5d06898d9dcb5dc961a23c970bfe70e26d96cc1a9a3582.

- 2026-10-08T17:03:40+00:00: Recorded command exit 0; command argv SHA-256
  bcd1150a25744623c397ded77f605884f4669faf0781a4b6600b797c9ef398c5.

- 2026-10-08T17:04:45+00:00: Recorded command exit 1; command argv SHA-256
  adffbcd111f31ff33ee09890e4a9de21728520d004614850b9340f549e32dea0.

- 2026-10-08T17:06:01+00:00: Recorded command exit 0; command argv SHA-256
  9ac4208ac56854862843c4f9342e789f6153818c95c0986ffc66f638ed99dce4.
