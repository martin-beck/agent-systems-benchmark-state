---
{
  "branch": "feature/frontend-control-api-repair",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-08T00:11:04+00:00",
  "depends_on": [
    "AR-0101",
    "AR-0104",
    "AR-0204",
    "AR-0801"
  ],
  "id": "AR-0847",
  "next_action": "Repair the AR-0803 frontend control candidate's five immutable-review findings, then qualify the repaired API and transfer the reviewed result back to AR-0803.",
  "observed_branch": "feature/frontend-control-api-repair",
  "observed_dirty": 20,
  "observed_head": "b7e7f5b8864343fe4079ee84bd7131456ad6f26c",
  "owner": "replay_20260906",
  "plan": "../plans/AR-0847.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Repair and independently qualify the blocked frontend control API candidate.",
  "task_revision": 44,
  "title": "Frontend control API repair",
  "updated_at": "2026-09-07T21:36:04+00:00",
  "worktree_key": "agent-systems-benchmark-frontend-control-api-repair"
}
---
## AR-0847

Repair the blocked AR-0803 candidate without mutating its dirty worktree in place. Wire the protocol into a real runner endpoint/client and lifecycle recovery path; enforce absolute operation deadlines; restrict negotiation to offered versions; validate the initial envelope through the common path; and enforce bounded privacy for backend responses/errors. Add focused positive and negative tests, formal/fault/privacy evidence, exact immutable review, exact-head CI, integration, and post-merge verification. On completion, reconcile AR-0803's umbrella status and unblock its child frontend ARs.

- 2026-09-07T21:11:02+00:00: Promote focused repair for AR-0803 immutable-review findings;
  dependencies are complete and isolated worktree is available.

- 2026-09-07T21:11:04+00:00: Claimed by replay_20260906.

- 2026-09-07T21:13:31+00:00: Recorded command exit 0; command argv SHA-256
  7c145cae25b02f870487e3a09450303496a9a72f7b01b10b754f5034e73197ad.

- 2026-09-07T21:14:04+00:00: Recorded command exit 0; command argv SHA-256
  658fb5a97909c6f127ef833e6ff3e20add5ec672faf7819331111bc4da915c77.

- 2026-09-07T21:14:45+00:00: Recorded command exit 1; command argv SHA-256
  2d548922f2047456a47a0eeb3dbf48554efec24c5cc9323c131afb3b9bda7f8f.

- 2026-09-07T21:15:37+00:00: Recorded command exit 2; command argv SHA-256
  48458d4adcbc2714c4ae60f17ec39d916357031118af6e75d9a5cd826c73f20e.

- 2026-09-07T21:16:09+00:00: Recorded command exit 1; command argv SHA-256
  5c188617dec83f9f1010f73ca05003594c52bbc2b2659b0a180c3cd28785aa9c.

- 2026-09-07T21:17:35+00:00: Recorded command exit 0; command argv SHA-256
  c5d51883a7ef7dc025b0e911117a4a085f969f1e14a9642431c6f86b5292b019.

- 2026-09-07T21:17:49+00:00: Recorded command exit 0; command argv SHA-256
  4fec215f1bf600ab04757b8ce8ac2d4440f4c52bed405bd31581924757e16c3d.

- 2026-09-07T21:17:55+00:00: Recorded command exit 0; command argv SHA-256
  3177e091f96c86bc611ad9642929a7d37b185a320c1633263cba1eba3e40d88d.

- 2026-09-07T21:18:14+00:00: Recorded command exit 0; command argv SHA-256
  86b687f725cee36dba2a311ad07d2521b7f63589c3487007deb354b8aa25fb18.

- 2026-09-07T21:19:01+00:00: Recorded command exit 127; command argv SHA-256
  3ae507d85a97643c36d8319289be5b2fb008391efbdea064d236728dede86fed.

- 2026-09-07T21:21:16+00:00: Recorded command exit 0; command argv SHA-256
  98716b8379a7a16e4f2ec8e2154d9b0f04e40aec3e50692c7f25495685796cea.

- 2026-09-07T21:22:02+00:00: Recorded command exit 0; command argv SHA-256
  7c245a83e20bdc3ddf80a1130350c6beea96868eb2e7b3e21d1d9c578f020705.

- 2026-09-07T21:22:35+00:00: Recorded command exit 101; command argv SHA-256
  111541959c64681c19c974d4807b5b75186e59c992c7af70c8c7f4bff10261e8.

- 2026-09-07T21:22:45+00:00: Recorded command exit 0; command argv SHA-256
  0c2715ed55ffbce1d3113a3fb02dc4f09c7bce7eb2af02f5a5049c1383250f59.

- 2026-09-07T21:23:03+00:00: Recorded command exit 101; command argv SHA-256
  111541959c64681c19c974d4807b5b75186e59c992c7af70c8c7f4bff10261e8.

- 2026-09-07T21:23:40+00:00: Recorded command exit 0; command argv SHA-256
  a4ae643830492890b6269bd5ac6ec3e61656dd5e798da8a0b4212a934a829510.

- 2026-09-07T21:24:34+00:00: Recorded command exit 0; command argv SHA-256
  3c8536d6edc3b59d7c2360fd114f9d64c1d6c776369eb365f7fb998a63ad7417.

- 2026-09-07T21:24:56+00:00: Recorded command exit 101; command argv SHA-256
  1320fabc3ae5ece3c6533a47b31bfa1d7389481c083691ac109bea7be8d183d2.

- 2026-09-07T21:25:15+00:00: Recorded command exit 0; command argv SHA-256
  641f43cc4497e53dc84db1c8064978e11478ff516aeb6ed615c55b76ae69ddff.

- 2026-09-07T21:25:32+00:00: Recorded command exit 0; command argv SHA-256
  111541959c64681c19c974d4807b5b75186e59c992c7af70c8c7f4bff10261e8.

- 2026-09-07T21:28:29+00:00: Recorded command exit 0; command argv SHA-256
  c6b4f365620212c8c6373d76bc6d72c1ef4e3f570db859fa984b3e6b5175de1f.

- 2026-09-07T21:29:24+00:00: Recorded command exit 0; command argv SHA-256
  72d2d2c20cd07fa16f653e1af52e28a4ee8af6fa036bd194fe434a81bfcecfb8.

- 2026-09-07T21:29:38+00:00: Recorded command exit 0; command argv SHA-256
  9cbdfcea7a08c5cc8d8a5508513cfdcd72ec7c8e52aee5f5b47581578c88ff99.

- 2026-09-07T21:29:56+00:00: Recorded command exit 0; command argv SHA-256
  111541959c64681c19c974d4807b5b75186e59c992c7af70c8c7f4bff10261e8.

- 2026-09-07T21:30:36+00:00: Recorded command exit 0; command argv SHA-256
  5dd7387544ffaf96fc6b948c4807e0026f882caff903180c74f653a41624ff18.

- 2026-09-07T21:31:35+00:00: Recorded command exit 1; command argv SHA-256
  4cd4471c1c4ba65ed1e82bdf59129ea4ef34ee6dd2836ed2f587cf4d8e8a59c6.

- 2026-09-07T21:32:34+00:00: Recorded command exit 0; command argv SHA-256
  1996ae1d17b5e8feb7c8cc0121aa51630df8ae656bfe5b02d920a80f74ff3998.

- 2026-09-07T21:32:55+00:00: Recorded command exit 0; command argv SHA-256
  9cbdfcea7a08c5cc8d8a5508513cfdcd72ec7c8e52aee5f5b47581578c88ff99.

- 2026-09-07T21:33:01+00:00: Recorded command exit 0; command argv SHA-256
  17a8ab923f871ad30f50441eb572890294874791247caf820b5d0e27c8b28ae0.

- 2026-09-07T21:33:27+00:00: Recorded command exit 101; command argv SHA-256
  efe7203abb65d5c98cf8850391b98af96324965358d6907dc7d5885e10974de7.

- 2026-09-07T21:33:48+00:00: Recorded command exit 0; command argv SHA-256
  2170d834cbae8627043a26aa9d3d86f5af2535cb43b6232f0b01928181c85785.

- 2026-09-07T21:34:04+00:00: Recorded command exit 101; command argv SHA-256
  efe7203abb65d5c98cf8850391b98af96324965358d6907dc7d5885e10974de7.

- 2026-09-07T21:34:28+00:00: Recorded command exit 0; command argv SHA-256
  ff7157414de0a4137b45e1aa25b4ae955bd992b623ea27e7876d39f9b45c346e.

- 2026-09-07T21:34:47+00:00: Recorded command exit 0; command argv SHA-256
  efe7203abb65d5c98cf8850391b98af96324965358d6907dc7d5885e10974de7.

- 2026-09-07T21:35:27+00:00: Recorded command exit 0; command argv SHA-256
  7b2e77a47b8401ec343055d9fca7f78780d5e0d10a269d7a7fb7210ab7b0af22.

- 2026-09-07T21:35:46+00:00: Recorded command exit 1; command argv SHA-256
  ccaeaeff1ddde5f211cfbde513936a31e28df7a42385fb4a8aea2819cf96928f.

- 2026-09-07T21:36:04+00:00: Recorded command exit 0; command argv SHA-256
  9cbdfcea7a08c5cc8d8a5508513cfdcd72ec7c8e52aee5f5b47581578c88ff99.
