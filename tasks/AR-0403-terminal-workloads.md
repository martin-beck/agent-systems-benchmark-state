---
{
  "branch": "feature/terminal-workloads",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-08T15:37:57+00:00",
  "depends_on": [
    "AR-0401"
  ],
  "id": "AR-0403",
  "next_action": "Add a provenance-only Terminal-Bench v4 adapter record and fail-closed negatives; do not qualify or execute until selected Harbor package bytes, OCI image digest, reset behavior, and native oracle evidence are available.",
  "observed_branch": "feature/terminal-workloads",
  "observed_dirty": 0,
  "observed_head": "e0da4efd375080c774cff91a8eef694d93e14132",
  "owner": "replay_20260906",
  "plan": "../plans/AR-0403.md",
  "priority": "P2",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Import terminal tasks through an adapter to the published harness or task format.",
  "task_revision": 27,
  "title": "Integrate Terminal-Bench workloads",
  "updated_at": "2026-09-08T14:00:55+00:00",
  "worktree_key": "agent-systems-benchmark-terminal-workloads"
}
---
## AR-0403

Import terminal tasks through an adapter to the published harness or task format.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-08T13:37:54+00:00: Dependency AR-0401 is durably done; paths are disjoint from active
  AR-0314 and AR-0855. Promote for contract assessment.

- 2026-09-08T13:37:57+00:00: Claimed by replay_20260906.

- 2026-09-08T13:38:56+00:00: Recorded command exit 0; command argv SHA-256
  bc0b1cbda14b1f9e8ed2b04d75aa98d36461147a776680ec41ef650830c8736d.

- 2026-09-08T13:40:43+00:00: Recorded command exit 0; command argv SHA-256
  0ad4c664c6156bf8720766f7796539654c69d14e0bd5b5f05fbb3fbc9dddb5f7.

- 2026-09-08T13:47:28+00:00: Recorded command exit 0; command argv SHA-256
  cbda25a19c0f65fc1cfa43f3caeeb406009c7c2c62a872b9f0cf2aef3318aec0.

- 2026-09-08T13:48:28+00:00: Compatibility spike: pinned Terminal-Bench v4.0.0 at verified commit
  452bf305c6daa62fc59061d22133a7cbc7c1572e (archive SHA-256
  390ee198a0f02fcdf140ac21420e106ce98f26d5f028b3d16b73e2d5137ff392) and Harbor v0.22.0 at peeled
  commit 4407eb5227a2ff4f0d3f16b2eb48849382fdf276 (archive SHA-256
  04ec6b077d610896d75ed85b6b5ff88a9a241da6d528419acca66d2307329a21); both LICENSE files are
  Apache-2.0 SHA-256 c71d239df91726fc519c6eb72d318ec65820627232b2f796219e87dcf35d0ab4. v4 dataset
  manifest SHA-256 ecd296ba053840bd4c0068e8f84e8a6fa829d184d0fd9852becdc19f4c895fcf contains 66
  content-addressed task refs and labels itself terminal-bench-3. Source audit: every verifier mode
  is separate, no task declares network policy (Harbor default is public), and only 8/66 source
  Dockerfiles pin a base image digest. Recomputed Harbor package hashes for sampled source trees did
  not equal dataset package digests, so tag checkout bytes cannot substitute for acquired package
  bytes. Native oracle/reset evidence is unavailable because this worker cannot access the Docker
  socket; no support claim made.

- 2026-09-08T13:51:02+00:00: Recorded command exit 1; command argv SHA-256
  c82935fac7709f957bda6f12e1fc666d2f1ba2cc05cef745daf3897f445cc06c.

- 2026-09-08T13:53:48+00:00: Recorded command exit 128; command argv SHA-256
  7bdc502fe5aaa3163855d10f58125d7caae602741fb6f5117534ae091e212abe.

- 2026-09-08T13:54:35+00:00: Recorded command exit 0; command argv SHA-256
  78477c70d3e2c64e783699173f5f936efaf6d582d9aafd92d5a0130a27883c6b.

- 2026-09-08T13:54:56+00:00: Recorded command exit 1; command argv SHA-256
  8bdaea23f8d1fa90c50b7f413d8cad1aa86a6374d9bb802e1a9b1970da15311f.

- 2026-09-08T13:55:33+00:00: Recorded command exit 0; command argv SHA-256
  fa8d55f7c4d0cf59d1caefe2327911a4f5f44d387dea4098db035bddfbc39d5e.

- 2026-09-08T13:56:20+00:00: Recorded command exit 0; command argv SHA-256
  ab36d804841394be8801dede80bf7d0285434a6b6b1a720996f986a45504b54c.

- 2026-09-08T13:57:13+00:00: Recorded command exit 0; command argv SHA-256
  f31328010946b4943494990cf96dcab243664f41cf99dcdfc8a80c9f5c0fcb62.

- 2026-09-08T13:57:41+00:00: Recorded command exit 0; command argv SHA-256
  bc35586f2be2a5ed6fec27ffeda8ef9298f7c2348c29f950052baafb5b11a401.

- 2026-09-08T13:58:11+00:00: Recorded command exit 1; command argv SHA-256
  ce058406ae13362fca4f6b9bfdaf741076464472e3df928eda647f571822607f.

- 2026-09-08T13:58:35+00:00: Recorded command exit 0; command argv SHA-256
  24ac9b665ddfc02cdb23a34a9a02df89f83e1a09bed7f6864f6801dc701e0abd.

- 2026-09-08T13:58:57+00:00: Recorded command exit 0; command argv SHA-256
  ef32af15430f6c8130dceb795926b6bd4f805bf33b1b9a7bfa8d05e28cb6757e.

- 2026-09-08T13:59:52+00:00: Recorded command exit 0; command argv SHA-256
  91be65fcac6d132d60257440da8fc667625f504d4afcddf60293283b290c20eb.

- 2026-09-08T14:00:23+00:00: Recorded command exit 0; command argv SHA-256
  fd5be908a7e19b92ee220abbbc548558b7ba308846b0fe348012a25533657ce2.

- 2026-09-08T14:00:55+00:00: Recorded command exit 0; command argv SHA-256
  461737c8f8df917e34527895d7b95becab88852dbf4ae5c68bf721452e72be07.
