---
{
  "branch": "feature/frontend-protocol-contract",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-07T23:44:45+00:00",
  "depends_on": [
    "AR-0101",
    "AR-0801"
  ],
  "id": "AR-0840",
  "next_action": "Define version-negotiated frontend requests, events, capabilities, and fixtures.",
  "owner": "root-coordination-20260906",
  "plan": "../plans/AR-0840.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Define the stable frontend control protocol contract.",
  "task_revision": 28,
  "title": "Define frontend protocol contract",
  "updated_at": "2026-09-07T22:37:44+00:00",
  "worktree_key": "agent-systems-benchmark-frontend-protocol-contract"
}
---
## AR-0840

Define version-negotiated requests/events for capabilities, settings validation, plan creation,
launch, status, cancellation, history, repeat, and analysis. Provide canonical schemas, fixtures,
compatibility rules, bounded errors, and generated consistency checks.

- 2026-09-07T08:41:59+00:00: Begin canonical frontend protocol contract after verified AR-0101 and
  AR-0801 dependencies.

- 2026-09-07T08:42:02+00:00: Claimed by root-coordination-20260906.

- 2026-09-07T08:48:50+00:00: Recorded command exit 0; command argv SHA-256
  c7558c2803cd97faa708393f9f861ae3bd64b639014b985249708a87bc339e64.

- 2026-09-07T09:01:43+00:00: Recorded command exit 0; command argv SHA-256
  588284cf0fbf0a297e09c58d61c2e7ef62cac2813f0bb4d7a8791cd549cff8df.

- 2026-09-07T10:33:18+00:00: Recorded command exit 0; command argv SHA-256
  465f460bcc9a4a9739e3ec473aaca37f5f57a3c7316687c2b87ba1cb23e07579.

- 2026-09-07T11:21:15+00:00: Recorded command exit 0; command argv SHA-256
  9c209dd0b91376590e82598f8e7bca56261846e6ed4eaec86caf013f2cf8ddff.

- 2026-09-07T11:33:42+00:00: Recorded command exit 0; command argv SHA-256
  60edcf472ff2fc350fc24e5cc86906a715b605eeb06397dc49548aa361846d8e.

- 2026-09-07T11:37:14+00:00: Recorded command exit 0; command argv SHA-256
  1fdf16006094ff0093e6a94f7b3d5e866df9318048f54d9b47a0cb23dfa06286.

- 2026-09-07T11:42:44+00:00: Heartbeat by root-coordination-20260906.

- 2026-09-07T11:54:37+00:00: Recorded command exit 0; command argv SHA-256
  a783ec17481aba0a32e82322cbe5bd233ce58463bff3bedea4695557d684297a.

- 2026-09-07T13:28:30+00:00: Recorded command exit 0; command argv SHA-256
  c894e4428bed393ef5997e6e8239c1bdf9d0c3f79a6747d5b488f8242add780f.

- 2026-09-07T13:28:36+00:00: Recorded command exit 1; command argv SHA-256
  203f4ba927e2fa3a003c77c72805d1a7a49a69a873aa97b7fc7fdfc9f4b3a36a.

- 2026-09-07T13:51:53+00:00: Recorded command exit 0; command argv SHA-256
  0a438cd42816f4b94f9c0b202dfcbeb804af66963ffd0e7a185afc82938d4f8f.

- 2026-09-07T13:52:00+00:00: Recorded command exit 1; command argv SHA-256
  497c891a107cc2fe60d591450cf484ced560d5634250dbd5ad163f5426b76597.

- 2026-09-07T14:43:09+00:00: Heartbeat by root-coordination-20260906.

- 2026-09-07T15:53:40+00:00: Recorded command exit 0; command argv SHA-256
  6e4b7642313346b0b67f7d47eb521ca4ef218a971019ef8ae9a2bbacbbde8efd.

- 2026-09-07T15:53:46+00:00: Recorded command exit 1; command argv SHA-256
  beb4b760f8e57f4293c1de0a7b16986bd4425408ba5ef3cdea69a6410a48de6d.

- 2026-09-07T17:23:22+00:00: Recorded command exit 0; command argv SHA-256
  d165e39ac94c310d66c2a6e09c06ac80f9171ec523e3790c6fc6e0b5e7ecbfbe.

- 2026-09-07T17:23:30+00:00: Recorded command exit 1; command argv SHA-256
  e49ece748a7b06c61a1c65c591ba0e2eaa2bed63d71e64a74bc09cd64c141c1e.

- 2026-09-07T17:43:34+00:00: Heartbeat by root-coordination-20260906.

- 2026-09-07T19:00:25+00:00: Recorded command exit 0; command argv SHA-256
  c1a4e78493ca22d7ac33824c02f54a6d223d8f07407f4c7fd2b15478675aadcc.

- 2026-09-07T19:00:31+00:00: Recorded command exit 1; command argv SHA-256
  ce2b5042f8216175ccfb79c4aa04e0a720a02c696ab5cc267e57649388e7eb92.

- 2026-09-07T20:44:45+00:00: Heartbeat by root-coordination-20260906.

- 2026-09-07T21:10:51+00:00: Recorded command exit 0; command argv SHA-256
  8a930f9c284f1cb665aaf46046094372cbc4372c32bc5fdd6e094f8e3167520c.

- 2026-09-07T21:10:57+00:00: Recorded command exit 1; command argv SHA-256
  3bdd1788a518fa934174d0d0bca8e7fa9320780caa4767f0fe4a03d45ed6fdf3.

- 2026-09-07T21:27:57+00:00: Recorded command exit 0; command argv SHA-256
  eaf2472e4b0ec29bac3303a6d46474c99be3c0ab077feca87b1c3650d4745e53.

- 2026-09-07T22:37:44+00:00: Recorded command exit 0; command argv SHA-256
  eaf2472e4b0ec29bac3303a6d46474c99be3c0ab077feca87b1c3650d4745e53.
