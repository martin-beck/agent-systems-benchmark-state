---
{
  "branch": "feature/opendesk-strict-replay-http-compatibility",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-07T16:52:10+00:00",
  "depends_on": [
    "AR-0502",
    "AR-0503",
    "AR-0504",
    "AR-0302"
  ],
  "id": "AR-0516",
  "next_action": "Implement fail-closed OpenDesk HTTP compatibility for span_id, absent-stream SSE, and recorded model catalog probes.",
  "observed_branch": "feature/opendesk-strict-replay-http-compatibility",
  "observed_dirty": 8,
  "observed_head": "40cfa75ca195aaf13be1d5bc8025f96e5f4d3e7c",
  "owner": "quality_20260906",
  "plan": "../plans/AR-0516.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Add narrowly scoped strict-replay compatibility for pinned OpenDesk traffic.",
  "task_revision": 34,
  "title": "OpenDesk strict-replay HTTP compatibility",
  "updated_at": "2026-09-07T14:17:30+00:00",
  "worktree_key": "agent-systems-benchmark-opendesk-strict-replay-http-compatibility"
}
---
## AR-0516

Implement the shared, fail-closed replay compatibility required by the pinned OpenDesk 0.3.5 evidence: lowercase underscore-bearing header names including redacted `span_id`; absent `stream` paired only with an exact recorded SSE content type; and the two bounded credential-free model-catalog GET probes. Preserve strict ordering, accounting, network denial, and negative cases.

Acceptance requires schema/runtime parity, adversarial positives and negatives, exact socket-byte SSE replay, catalog ordering/accounting, privacy/Gitleaks/formal/full x86_64+aarch64 gates, and a real loopback OpenDesk rerun. Do not claim OpenDesk support until AR-0507 consumes this reviewed merge.

- 2026-09-07T13:28:39+00:00: Promote shared replay compatibility repair discovered by AR-0507
  evidence; serialize schema/service changes separately.

- 2026-09-07T13:28:41+00:00: Claimed by root.

- 2026-09-07T13:28:51+00:00: Coordinator created and promoted AR-0516; release claim because all
  four stable workers are occupied. Keep planned for next safe serialized slot.

- 2026-09-07T13:52:07+00:00: Promote shared OpenDesk replay compatibility repair now that AR-0508
  released and a worker slot is free.

- 2026-09-07T13:52:10+00:00: Claimed by quality_20260906.

- 2026-09-07T13:52:58+00:00: Recorded command exit 0; command argv SHA-256
  195449c186722fe0b769c793877c599856ce076ac8181bc5b9a600a9dd38eec9.

- 2026-09-07T13:57:32+00:00: Recorded command exit 0; command argv SHA-256
  279684299b6a4f7bcdab8980675f55ad1d66f160c4802953878e25e916c9a863.

- 2026-09-07T13:57:51+00:00: Recorded command exit 1; command argv SHA-256
  c0dc1f34cd998dc456d44afacdaf4a24fa3d03748cc7b6165330680a53aa5763.

- 2026-09-07T13:58:06+00:00: Recorded command exit 0; command argv SHA-256
  5e9694509038c5216d4f02627782683082ff47c5e43f8d8abe20b0d12b95136d.

- 2026-09-07T13:58:29+00:00: Recorded command exit 101; command argv SHA-256
  c0dc1f34cd998dc456d44afacdaf4a24fa3d03748cc7b6165330680a53aa5763.

- 2026-09-07T13:58:51+00:00: Recorded command exit 0; command argv SHA-256
  dcc921c7318383697a10e1813d189e6524409e5444bcc9d46758f055d898e29c.

- 2026-09-07T13:59:12+00:00: Recorded command exit 0; command argv SHA-256
  c0dc1f34cd998dc456d44afacdaf4a24fa3d03748cc7b6165330680a53aa5763.

- 2026-09-07T14:00:51+00:00: Recorded command exit 0; command argv SHA-256
  976dd9a59563747b46328642f09cb1e74330171f764d6372243d6e2954a46d48.

- 2026-09-07T14:01:39+00:00: Recorded command exit 0; command argv SHA-256
  f235d0c549fa7568ec631b95cd307a13cac5c1c2c840b65f5aebab4ac24038aa.

- 2026-09-07T14:03:11+00:00: Recorded command exit 0; command argv SHA-256
  3990fdc285c13d815a7d626fe9eb513bbe5ece51e1f05ee32386c689a5bbe9d3.

- 2026-09-07T14:04:34+00:00: Recorded command exit 0; command argv SHA-256
  9812bfdd87da0c5659ca3cb21ea1aac202ae06ea0731fda8ae798f116295ebcf.

- 2026-09-07T14:04:49+00:00: Recorded command exit 0; command argv SHA-256
  5e9694509038c5216d4f02627782683082ff47c5e43f8d8abe20b0d12b95136d.

- 2026-09-07T14:05:10+00:00: Recorded command exit 0; command argv SHA-256
  5d70464abfe059f7c62df8cf185695dc6220002156d4e96f96e0abd830dc3337.

- 2026-09-07T14:06:38+00:00: Recorded command exit 1; command argv SHA-256
  4566e388b2c03b58af4c8ef29f7481e6db2c0d0daa0533e3807959ffe6e361a0.

- 2026-09-07T14:09:40+00:00: Recorded command exit 1; command argv SHA-256
  2e086b8b83af13e1d3333985e8b55b5d4bfbb90b0d89cbe5701ad393a564251a.

- 2026-09-07T14:10:15+00:00: Recorded command exit 0; command argv SHA-256
  06b7d25b5d0e1a2982295c8fe174b9fb69c3acf2e3aa5d9ecb3ce76a4b556178.

- 2026-09-07T14:11:44+00:00: Recorded command exit 0; command argv SHA-256
  88628f26ff88e7aa804f9b9ce50a0bdc10d98afc409aebb001948462a67fc605.

- 2026-09-07T14:11:59+00:00: Recorded command exit 0; command argv SHA-256
  5e9694509038c5216d4f02627782683082ff47c5e43f8d8abe20b0d12b95136d.

- 2026-09-07T14:12:21+00:00: Recorded command exit 0; command argv SHA-256
  2cc15bff5200e61c764a35f5fcb34f0a9a6b254bc6a1a931134a6ee671965f99.

- 2026-09-07T14:15:33+00:00: Recorded command exit 0; command argv SHA-256
  225a2c6a21adde6c706bc7e47fdc1bb37f2061b7eac126fee7bb07ff7be368cd.

- 2026-09-07T14:15:50+00:00: Recorded command exit 0; command argv SHA-256
  e212dce3104c4f2cb341ae31eb17107d42390af64aa54db541b147bcf95ea2d1.

- 2026-09-07T14:16:38+00:00: Recorded command exit 0; command argv SHA-256
  d10af40211a957f6ed4b33d741cca9a6c2d394a6b3a715da9f87a9731e3a4ccd.

- 2026-09-07T14:17:14+00:00: Recorded command exit 0; command argv SHA-256
  cb83a5bafb221cfc0798f2e09567944bbb38dbe79f160c29dcdc3bd19d4cccbe.

- 2026-09-07T14:17:30+00:00: Recorded command exit 0; command argv SHA-256
  8a2a27f84a80a83ebe7d5372deb9a39931a0c541782ce6a0dacfafa58e2728df.
