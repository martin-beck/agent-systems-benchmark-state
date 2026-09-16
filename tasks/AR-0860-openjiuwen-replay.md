---
{
  "branch": "feature/openjiuwen-replay",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-0859"
  ],
  "id": "AR-0860",
  "next_action": "Seal the sanitized live capture and prove strict offline replay, causal parity, malformed-record rejection, and zero external network.",
  "owner": "",
  "plan": "../plans/AR-0860.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "open",
  "summary": "Qualify strict OpenJiuwen replay.",
  "task_revision": 2,
  "title": "Qualify strict OpenJiuwen replay",
  "updated_at": "2026-09-16T08:20:45+00:00",
  "worktree_key": "agent-systems-benchmark-openjiuwen-replay"
}
---
## AR-0860

Seal the sanitized live capture and prove strict offline replay, causal parity, malformed-record rejection, and zero external network.

This phase cannot claim support from mocks, parser fixtures, source inspection, compilation, or mutable artifacts. If its executable evidence is unavailable, leave this child blocked with exact provenance evidence while the sibling agent series proceeds.

- 2026-09-16T08:20:45+00:00: Dependency AR-0859 is complete; begin strict OpenJiuwen replay
  qualification.
