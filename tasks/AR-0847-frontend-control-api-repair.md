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
  "task_revision": 15,
  "title": "Frontend control API repair",
  "updated_at": "2026-09-07T21:18:12+00:00",
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
