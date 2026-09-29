---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1304"
  ],
  "id": "AR-1517",
  "next_action": "Classify evidence and select AR-1309's capacity/model contract.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1517-ar1309-capacity-decision-unblock.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "done",
  "summary": "Select a reviewed AR-1309 capacity/model contract after runner failure.",
  "task_revision": 4,
  "title": "AR-1309 capacity decision",
  "updated_at": "2026-09-29T19:06:42+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1517-ar1309-capacity-decision-unblock"
}
---

This is a decision and contract AR, not permission to widen existing formal
limits. It preserves the distinction between provider-free development tests,
formal qualification, and first-customer production readiness.

- 2026-09-29T19:05:20+00:00: Completed AR-1304 dependency verified; promote independent
  capacity/model decision successor using terminal AR-1307/1308 evidence.

- 2026-09-29T19:06:02+00:00: Claimed by coordinator-ar1517-capacity-decision-20260929.

- 2026-09-29T19:06:42+00:00: Capacity decision recorded; implementation belongs to a separate
  successor AR and does not widen AR-1307.

- Decision detail: retain AR-1307's 3G/3G/2-worker/8G/7200s contract. The successor uses a
  separately provisioned disposable VM with 8G memory and 8G guest swap, the same model and
  inputs, a distinct profile/attestation, and the same bounded 7200s execution limit.
