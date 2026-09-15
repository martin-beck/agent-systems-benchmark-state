---
{
  "branch": "feature/ar-1230-authenticated-provider-request-seam",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-15T20:49:15+00:00",
  "depends_on": [
    "AR-0319",
    "AR-0320",
    "AR-1100"
  ],
  "id": "AR-1230",
  "next_action": "Promote after architecture review; specify and test the fail-closed authenticated provider-request seam, then unblock AR-1228.",
  "observed_branch": "feature/ar-1230-authenticated-provider-request-seam",
  "observed_dirty": 3,
  "observed_head": "2117a40e2e27602c39aebee87581cf652628a534",
  "owner": "asb_ar1230_auth_request_seam",
  "plan": "../plans/AR-1230.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Define the approved bounded provider authentication request and secret-injection seam.",
  "task_revision": 21,
  "title": "Authenticated provider-request seam and secret injection contract",
  "updated_at": "2026-09-15T18:50:33+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1230-authenticated-provider-request-seam"
}
---

Create the architecture contract required to turn qualified credential sources into authenticated
provider probes without exposing secret values to argv, ordinary environment, config, control
frames, logs, evidence or public state. This prerequisite owns the narrow seam and its security
proofs; AR-1228 owns concrete bounded provider transport and AR-1229 owns durable application
integration.

- 2026-09-15T18:40:00+00:00: Created after independent review found that the opaque credential
  resolver cannot safely support HTTP authentication without an approved provider-request seam.

- 2026-09-15T18:43:01+00:00: Dependencies AR-0319, AR-0320 and AR-1100 verified complete; promote
  authenticated provider-request seam prerequisite.

- 2026-09-15T18:43:15+00:00: Claimed by asb_ar1230_auth_request_seam.

- 2026-09-15T18:43:29+00:00: Recorded command exit 0; command argv SHA-256
  e95aa81c9bca865107c5e1bb46effcb4a6f91d4a8e4c8c04b85dccbe373d0147.

- 2026-09-15T18:43:39+00:00: Heartbeat by asb_ar1230_auth_request_seam.

- 2026-09-15T18:47:16+00:00: Heartbeat by asb_ar1230_auth_request_seam.

- 2026-09-15T18:47:19+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-15T18:47:39+00:00: Recorded command exit 0; command argv SHA-256
  c1e7039f75f0d249f1099a8ed9798935c71634c00dc669755dba2f34373ab2dd.

- 2026-09-15T18:47:53+00:00: Recorded command exit 101; command argv SHA-256
  4340dcbf253e5e20fd7f5355131da4428901f1f912a4e0ac816826265343c6b5.

- 2026-09-15T18:48:10+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-15T18:48:21+00:00: Recorded command exit 0; command argv SHA-256
  c1e7039f75f0d249f1099a8ed9798935c71634c00dc669755dba2f34373ab2dd.

- 2026-09-15T18:48:31+00:00: Recorded command exit 0; command argv SHA-256
  4340dcbf253e5e20fd7f5355131da4428901f1f912a4e0ac816826265343c6b5.

- 2026-09-15T18:49:15+00:00: Heartbeat by asb_ar1230_auth_request_seam.

- 2026-09-15T18:49:19+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-15T18:49:29+00:00: Recorded command exit 101; command argv SHA-256
  c1e7039f75f0d249f1099a8ed9798935c71634c00dc669755dba2f34373ab2dd.

- 2026-09-15T18:50:05+00:00: Recorded command exit 0; command argv SHA-256
  c1e7039f75f0d249f1099a8ed9798935c71634c00dc669755dba2f34373ab2dd.

- 2026-09-15T18:50:15+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-15T18:50:23+00:00: Recorded command exit 0; command argv SHA-256
  c1e7039f75f0d249f1099a8ed9798935c71634c00dc669755dba2f34373ab2dd.

- 2026-09-15T18:50:33+00:00: Recorded command exit 0; command argv SHA-256
  4340dcbf253e5e20fd7f5355131da4428901f1f912a4e0ac816826265343c6b5.
