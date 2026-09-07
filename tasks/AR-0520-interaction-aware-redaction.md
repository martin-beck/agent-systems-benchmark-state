---
{
  "branch": "feature/interaction-aware-redaction",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-07T23:07:49+00:00",
  "depends_on": [
    "AR-0502",
    "AR-0503",
    "AR-0517"
  ],
  "id": "AR-0520",
  "next_action": "Make request-body redaction selectors interaction/method-aware so GET catalog entries can remain selector-free while POST bodies remain private and replayable.",
  "observed_branch": "feature/interaction-aware-redaction",
  "observed_dirty": 0,
  "observed_head": "1963364e75eec8cfcde0cfd0eaca672df12a2968",
  "owner": "quality_20260906",
  "plan": "../plans/AR-0520.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Support per-interaction request redaction policies for mixed catalog and private requests.",
  "task_revision": 4,
  "title": "Interaction-aware request redaction",
  "updated_at": "2026-09-07T20:09:39+00:00",
  "worktree_key": "agent-systems-benchmark-interaction-aware-redaction"
}
---
## AR-0520

Repair the cassette-global request-body redaction limitation exposed by Goose: catalog GET interactions must have null selectors while private POST message bodies retain bounded selectors and remain strictly replayable. Add interaction/method-aware policy representation, schema/roundtrip/strict-match support, missing-selector and marker-injection negatives, and full privacy/formal/platform gates.

- 2026-09-07T20:07:46+00:00: Promote interaction-aware redaction repair after confirmed Goose mixed
  GET/POST privacy blocker; serialize shared replay changes.

- 2026-09-07T20:07:49+00:00: Claimed by quality_20260906.
