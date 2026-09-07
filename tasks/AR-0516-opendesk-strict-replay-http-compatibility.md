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
  "observed_dirty": 6,
  "observed_head": "40cfa75ca195aaf13be1d5bc8025f96e5f4d3e7c",
  "owner": "quality_20260906",
  "plan": "../plans/AR-0516.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Add narrowly scoped strict-replay compatibility for pinned OpenDesk traffic.",
  "task_revision": 13,
  "title": "OpenDesk strict-replay HTTP compatibility",
  "updated_at": "2026-09-07T13:58:29+00:00",
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
