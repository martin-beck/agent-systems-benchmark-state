---
{
  "branch": "feature/frontend-protocol-contract",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-0101",
    "AR-0801"
  ],
  "id": "AR-0840",
  "next_action": "Define version-negotiated frontend requests, events, capabilities, and fixtures.",
  "observed_branch": "feature/frontend-protocol-contract",
  "observed_dirty": 0,
  "observed_head": "d3e2dfa979d85b8b443a07f93e7dd7b9a226bc2f",
  "owner": "",
  "plan": "../plans/AR-0840.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "done",
  "summary": "Define the stable frontend control protocol contract.",
  "task_revision": 47,
  "title": "Define frontend protocol contract",
  "updated_at": "2026-09-08T06:52:11+00:00",
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

- 2026-09-07T23:45:05+00:00: Heartbeat by root-coordination-20260906.

- 2026-09-07T23:45:27+00:00: Heartbeat by root-coordination-20260906.

- 2026-09-08T01:06:58+00:00: Recorded command exit 0; command argv SHA-256
  f51a5b63a69b3d7978fb1c90ebf3a19981bf609e65d9972077d74d3a0e27ee4f.

- 2026-09-08T01:53:59+00:00: Recorded command exit 0; command argv SHA-256
  acb9e76f0ab803d47bc3bb755b59054859f060c84e60cbce9137696dd1019947.

- 2026-09-08T01:54:05+00:00: Recorded command exit 1; command argv SHA-256
  ef098df8fdc207db420949b2219bac09dc01860f9a9e50a9987e33851bb768aa.

- 2026-09-08T02:13:13+00:00: Recorded command exit 0; command argv SHA-256
  eaf2472e4b0ec29bac3303a6d46474c99be3c0ab077feca87b1c3650d4745e53.

- 2026-09-08T02:13:39+00:00: Recorded command exit 0; command argv SHA-256
  eaf2472e4b0ec29bac3303a6d46474c99be3c0ab077feca87b1c3650d4745e53.

- 2026-09-08T02:46:56+00:00: Heartbeat by root-coordination-20260906.

- 2026-09-08T05:50:22+00:00: 2026-09-08T07:06:00Z: Coordinator lease expired with no active process;
  preserve protocol-contract worktree and all artifacts. Release is lease recovery only; reclaim
  after fresh audit.

- 2026-09-08T05:51:08+00:00: Fresh coordinator reclaim after expired lease recovery; protocol
  worktree preserved.

- 2026-09-08T05:51:11+00:00: Claimed by root-coordination-20260906.

- 2026-09-08T05:52:15+00:00: Recorded command exit 0; command argv SHA-256
  e3824fc8c14c516969ce294171e3394f31b7e1ada9d7e029ca75818ed35cd340.

- 2026-09-08T06:04:49+00:00: Recorded command exit 101; command argv SHA-256
  1f1f392b8f627db10943f1071c5ae1e2f8004ab1b3b15f3026a5ac90bf625205.

- 2026-09-08T06:05:09+00:00: Recorded command exit 0; command argv SHA-256
  4afa16f078462457863052381156429515eaf344117aa30161e83134fc7572f2.

- 2026-09-08T06:37:21+00:00: Recorded command exit 127; command argv SHA-256
  3d5864cc866186ad62378e2ed331f8b141acae1008c182651cbda5fba782a7f0.

- 2026-09-08T06:37:48+00:00: Recorded command exit 101; command argv SHA-256
  c4309a1e71f7b31ff4115d40399496fe9f0c995d7a40d9aef6e795400eb2d1e7.

- 2026-09-08T06:38:05+00:00: Recorded command exit 0; command argv SHA-256
  0b16cabb2243c8e2a481915400db7124ec2647b25507030c790388c3c83b445f.

- 2026-09-08T06:52:11+00:00: Independent review complete: PR #54 merged as signed/DCO no-ff
  462bd04a349dfbea1797c8a358e390544d51471e, included in current main. Exact asb-control focused
  suite passed: 3 unit + 13 control + 5 endpoint + 4 schema-conformance tests; schemas
  regenerated/conformance fixtures and bounded deadline/privacy/idempotency/owner transport
  negatives pass. Current worktree clean and protocol paths are immutable.
