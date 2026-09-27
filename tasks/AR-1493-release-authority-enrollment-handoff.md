---
{
  "branch": "release/ar-1493-release-authority-enrollment-handoff",
  "checkpoint_commit": "e1be259c9abb2a901998d3ca9b82521edd3fa2f8",
  "claim_expires": "2026-09-27T19:14:02+00:00",
  "depends_on": [
    "AR-1461",
    "AR-1462",
    "AR-1491",
    "AR-1492"
  ],
  "id": "AR-1493",
  "next_action": "Monitor eight exact-main post-merge workflows for e1be259c; release AR-1493 done only after all terminal SUCCESS.",
  "observed_branch": "release/ar-1493-release-authority-enrollment-handoff",
  "observed_dirty": 0,
  "observed_head": "9d2b22a80cfe9c6d9a01daec1e257fd93b99d37d",
  "owner": "ar1332-record-replay-luna56",
  "plan": "../plans/AR-1493-release-authority-enrollment-handoff.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Define and validate the external release-authority enrollment and signed-bundle verification handoff.",
  "task_revision": 54,
  "title": "Release-authority enrollment handoff",
  "updated_at": "2026-09-27T17:14:13+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1493-release-authority-enrollment-handoff"
}
---

AR-1490 is blocked because the authorized external signed customer package and
release authority are absent. AR-1493 makes the safe operator handoff exact
without fabricating authority or turning the AR-1491 non-production fixture
into release evidence.

- Required public handoff identities: SSHSIG namespace
  `asb-runtime-bundle-v1`, externally supplied principal, allowed-signers
  contract, trusted `ssh-keygen` path and SHA-256.
- Required verification: detached signature over exact `manifest.json` bytes,
  exact target identity, complete inventory/SBOM/provenance/checksum validation,
  and bounded offline verifier invocation.
- Forbidden substitutions: generated keys, placeholder principals, unsigned
  release claims, live providers, network access, credentials, private paths,
  or raw signature material in state.

The next action after promotion is to audit the existing AR-1492 output and add
only deterministic repository-side checks/docs. If the external authority
inputs remain absent, release AR-1493 blocked with those exact missing inputs
and preserve AR-1490 as the customer-release blocker.

- 2026-09-27T16:52:40+00:00: Dependencies AR-1461, AR-1462, AR-1491, and AR-1492 are complete.
  Promote the repository-side release-authority enrollment/verification handoff while preserving
  AR-1490 external signed-package blocker.

- 2026-09-27T16:52:46+00:00: Claimed by ar1332-record-replay-luna56.

- 2026-09-27T16:52:55+00:00: Heartbeat by ar1332-record-replay-luna56.

- 2026-09-27T16:53:13+00:00: Recorded command exit 0; command argv SHA-256
  cc7868e69d843cc7770dfabaea600e67a6d6e3ed3f397db89d2e989706c70f92.

- 2026-09-27T16:53:34+00:00: Recorded command exit 0; command argv SHA-256
  1d6d631a0dc3693d000855b26dbacde946226abb99b1ec88a6b65d920b3e274b.

- 2026-09-27T16:53:57+00:00: Recorded command exit 0; command argv SHA-256
  321c534968b9c456a64caf5e6d09b63780c507f97548057d2bfe31edcfd73ff4.

- 2026-09-27T16:54:19+00:00: Recorded command exit 0; command argv SHA-256
  adb7ea61df9925f792fc5c72b34d0fb7d5129ed8ecca5730349508fb442315dc.

- 2026-09-27T16:55:40+00:00: Recorded command exit 0; command argv SHA-256
  f111cb30c3f89153f572c45c09d6df2119cceae3e86837a437188a493d4c8d1a.

- 2026-09-27T16:56:07+00:00: Recorded command exit 0; command argv SHA-256
  d1f37769545bdad3dfa6428b31f9ea765d0d1851289aa32b9b4d1fb58748677a.

- 2026-09-27T16:56:28+00:00: Recorded command exit 2; command argv SHA-256
  5f3f0a4fce99c33a59a16051e720790377262db7783b390ec3ed6fc67f270a95.

- 2026-09-27T16:56:48+00:00: Recorded command exit 0; command argv SHA-256
  7c730eec3ea71bd24ffc5a9255bf7f542481bf601dba6c72bed6e00f6c2fab3c.

- 2026-09-27T16:57:19+00:00: Recorded command exit 0; command argv SHA-256
  49905f60922bc8cff7be115f3e60db8b22b6355f5ad2faf337905fb47da9392a.

- 2026-09-27T16:57:41+00:00: Recorded command exit 0; command argv SHA-256
  f111cb30c3f89153f572c45c09d6df2119cceae3e86837a437188a493d4c8d1a.

- 2026-09-27T16:58:17+00:00: Recorded command exit 0; command argv SHA-256
  1323675f398c5359b24d39bcb41463d389e4d3f5f0251a918ee3f577300acab1.

- 2026-09-27T16:58:39+00:00: Recorded command exit 0; command argv SHA-256
  392420e7a4ff6bcfb3efd61977a3faaf0f2cd3dcced6d949c8cccc5550b6781d.

- 2026-09-27T16:59:17+00:00: Implemented narrow repository-side release-authority handoff validation
  and docs. validate_authority_inputs now fail-closes malformed principal and
  non-lowercase/non-64-char ssh-keygen digest without deciding trusted identity. Added positive and
  negative tests; Python bundle tests 7/7 pass, asb-bundle offline verifier 22/22 pass, repository
  policy passes, diff check passes. Independent diff review: exactly docs/RUNTIME_BUNDLES.md,
  tools/bundle/prepare_signing_handoff.py, and its test file; no asb-tui/provider changes.
  Signed+DCO commit 6f5dfd5c3292fd177a8f627c661e68ef30c40c65 verified SSH signature. One concurrent
  cargo invocation recorded LOCK_TIMEOUT and was rerun successfully; invalid check_source_headers
  path was a command/setup error (file absent), not product failure.

- 2026-09-27T16:59:27+00:00: Recorded command exit 0; command argv SHA-256
  579ef7db444bc7988a1f404a41609d04b7d18de014db18bae75b6c79862893c3.

- 2026-09-27T16:59:52+00:00: Recorded command exit 0; command argv SHA-256
  6daaf30e44aa3ce6c5d4418a43d5daf6bd2f9a339087430d658652bd62cdb1dc.

- 2026-09-27T17:00:19+00:00: Published exact SSH-signed/DCO head
  6f5dfd5c3292fd177a8f627c661e68ef30c40c65 as PR #372:
  https://github.com/martin-beck/agent-systems-benchmark/pull/372. Scope is three ASB files only; no
  asb-tui/provider changes. External authority remains operator-supplied and AR-1490 remains blocked
  until signed customer package inputs exist.

- 2026-09-27T17:00:27+00:00: Recorded command exit 0; command argv SHA-256
  fe22b8af89dfe26a754f8f06d2ff037bc789613211a39608e3fe97ea4eac3578.

- 2026-09-27T17:00:50+00:00: Recorded command exit 0; command argv SHA-256
  16aa608ab61d58686bd3d8d2b00f0ca212a416b16b601c4747d90fa9a2e8e3dd.

- 2026-09-27T17:01:24+00:00: Recorded command exit 0; command argv SHA-256
  e6ae98b22ae471658d6cedc211e1d091b56fad8a18ae170f21dba6e1ec78bae1.

- 2026-09-27T17:01:51+00:00: Recorded command exit 0; command argv SHA-256
  a80d3e6c9375f79d90f80e477f5b38541068960f70f244d87a0a4853c8d25cd1.

- 2026-09-27T17:02:28+00:00: Repository Quality run 36335270389 failed because synchronization merge
  ba222bbbdad190fd9e66ad2ee9e62fc1969722c lacked a matching Signed-off-by trailer. This was a
  publication-history defect, not product behavior. Safely rebased the single implementation commit
  onto current protected main a2d9be3, amended/recreated signed+DCO head
  9d2b22a80cfe9c6d9a01daec1e257fd93b99d37d, and force-with-lease updated PR #372. Prior failure
  preserved; all product diff remains the same three ASB files.

- 2026-09-27T17:02:36+00:00: Recorded command exit 0; command argv SHA-256
  fe22b8af89dfe26a754f8f06d2ff037bc789613211a39608e3fe97ea4eac3578.

- 2026-09-27T17:03:00+00:00: Recorded command exit 0; command argv SHA-256
  1e0cdedfa4e644b0209bca0064770f5f4fc10dac81816c82d4e3db1b4e8b2468.

- 2026-09-27T17:03:28+00:00: PR #372 exact signed head 9d2b22a80cfe9c6d9a01daec1e257fd93b99d37d is
  OPEN/UNSTABLE while CI runs. AWQ shadow and Huawei headers are SUCCESS; credential-free, AArch64,
  fault, formal, hosted, Repository Quality, and Rust are IN_PROGRESS; Kani is now IN_PROGRESS. No
  new failure after DCO-history repair.

- 2026-09-27T17:03:35+00:00: Heartbeat by ar1332-record-replay-luna56.

- 2026-09-27T17:03:42+00:00: Recorded command exit 0; command argv SHA-256
  1e0cdedfa4e644b0209bca0064770f5f4fc10dac81816c82d4e3db1b4e8b2468.

- 2026-09-27T17:04:05+00:00: Recorded command exit 0; command argv SHA-256
  1e0cdedfa4e644b0209bca0064770f5f4fc10dac81816c82d4e3db1b4e8b2468.

- 2026-09-27T17:04:25+00:00: Recorded command exit 0; command argv SHA-256
  1e0cdedfa4e644b0209bca0064770f5f4fc10dac81816c82d4e3db1b4e8b2468.

- 2026-09-27T17:04:47+00:00: Recorded command exit 0; command argv SHA-256
  1e0cdedfa4e644b0209bca0064770f5f4fc10dac81816c82d4e3db1b4e8b2468.

- 2026-09-27T17:05:09+00:00: Heartbeat by ar1332-record-replay-luna56.

- 2026-09-27T17:08:14+00:00: Recorded command exit 0; command argv SHA-256
  4ac888abf2dcaad69ba99d6c8d40dcd52cf578d1d8aef6af6374f4057dd64b4f.

- 2026-09-27T17:08:35+00:00: Recorded command exit 0; command argv SHA-256
  1e0cdedfa4e644b0209bca0064770f5f4fc10dac81816c82d4e3db1b4e8b2468.

- 2026-09-27T17:10:18+00:00: Recorded command exit 0; command argv SHA-256
  0cff9779ecf445c0cf541a53d99d195040a4e8d199ef05e33a8a76363a00781e.

- 2026-09-27T17:10:37+00:00: Recorded command exit 0; command argv SHA-256
  7ebc05781d0a1ec6b95afaf25fdb5e26fbf9536cfc74fc3352097c630e9351f9.

- 2026-09-27T17:11:00+00:00: Recorded command exit 0; command argv SHA-256
  fe22b8af89dfe26a754f8f06d2ff037bc789613211a39608e3fe97ea4eac3578.

- 2026-09-27T17:11:22+00:00: Recorded command exit 0; command argv SHA-256
  6820c1c8140eaa4d61496265a8fc4074c630c4b6bfa3536cedb337c31dcf3482.

- 2026-09-27T17:11:47+00:00: Recorded command exit 0; command argv SHA-256
  456a09bc3668d8fc9704c04c42e4063d12dff7895c8b188cc1cf79833a475733.

- 2026-09-27T17:12:09+00:00: Recorded command exit 0; command argv SHA-256
  dd92ec7ea8b88456df90f26fb70fa2f6ed36991f749f3810e11e706398700b83.

- 2026-09-27T17:12:32+00:00: Recorded command exit 0; command argv SHA-256
  65c48537df954c87b1d88d29f6fc784ec1946325f89a10c698d249fe7fdf9686.

- 2026-09-27T17:13:01+00:00: PR #372 merged normally at 2026-09-27T17:11:45Z. Reviewed topic head
  9d2b22a80cfe9c6d9a01daec1e257fd93b99d37d; merge SHA e1be259c9abb2a901998d3ca9b82521edd3fa2f8.
  Post-merge runs launched on exact merge: Rust 36336026563, Repository Quality 36336026573, AArch64
  36336026554, Formal 36336026579, credential-free 36336026586, hosted 36336026588, fault
  36336026566 are IN_PROGRESS; Huawei 36336026608 SUCCESS.

- 2026-09-27T17:13:10+00:00: Heartbeat by ar1332-record-replay-luna56.

- 2026-09-27T17:13:19+00:00: Recorded command exit 0; command argv SHA-256
  65c48537df954c87b1d88d29f6fc784ec1946325f89a10c698d249fe7fdf9686.

- 2026-09-27T17:13:41+00:00: Recorded command exit 0; command argv SHA-256
  65c48537df954c87b1d88d29f6fc784ec1946325f89a10c698d249fe7fdf9686.

- 2026-09-27T17:14:02+00:00: Heartbeat by ar1332-record-replay-luna56.

- 2026-09-27T17:14:13+00:00: Recorded command exit 0; command argv SHA-256
  65c48537df954c87b1d88d29f6fc784ec1946325f89a10c698d249fe7fdf9686.
