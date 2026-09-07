---
{
  "branch": "feature/opendesk-strict-replay-http-compatibility",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-07T13:58:41+00:00",
  "depends_on": [
    "AR-0502",
    "AR-0503",
    "AR-0504",
    "AR-0302"
  ],
  "id": "AR-0516",
  "next_action": "Implement fail-closed OpenDesk HTTP compatibility for span_id, absent-stream SSE, and recorded model catalog probes.",
  "owner": "root",
  "plan": "../plans/AR-0516.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Add narrowly scoped strict-replay compatibility for pinned OpenDesk traffic.",
  "task_revision": 3,
  "title": "OpenDesk strict-replay HTTP compatibility",
  "updated_at": "2026-09-07T13:28:41+00:00",
  "worktree_key": "agent-systems-benchmark-opendesk-strict-replay-http-compatibility"
}
---
## AR-0516

Implement the shared, fail-closed replay compatibility required by the pinned OpenDesk 0.3.5 evidence: lowercase underscore-bearing header names including redacted `span_id`; absent `stream` paired only with an exact recorded SSE content type; and the two bounded credential-free model-catalog GET probes. Preserve strict ordering, accounting, network denial, and negative cases.

Acceptance requires schema/runtime parity, adversarial positives and negatives, exact socket-byte SSE replay, catalog ordering/accounting, privacy/Gitleaks/formal/full x86_64+aarch64 gates, and a real loopback OpenDesk rerun. Do not claim OpenDesk support until AR-0507 consumes this reviewed merge.

- 2026-09-07T13:28:39+00:00: Promote shared replay compatibility repair discovered by AR-0507
  evidence; serialize schema/service changes separately.

- 2026-09-07T13:28:41+00:00: Claimed by root.
