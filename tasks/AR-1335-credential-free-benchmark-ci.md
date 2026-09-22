---
{
  "branch": "feature/ar-1335-credential-free-benchmark-ci",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1333",
    "AR-1334"
  ],
  "id": "AR-1335",
  "next_action": "Add the required credential-free CI stage that exercises the complete benchmark path with loopback and synthetic doubles, no secrets, no egress and no network, keeping the 90% coverage floor.",
  "owner": "",
  "plan": "../plans/AR-1335.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "planned",
  "summary": "Add the required credential-free CI stage for the complete benchmark path.",
  "task_revision": 1,
  "title": "Credential-free CI stage for the benchmark path",
  "updated_at": "2026-09-22T13:39:37+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1335-credential-free-benchmark-ci"
}
---

The benchmark path introduced by AR-1329 through AR-1334 must not degrade the
project's guarantee that CI runs without credentials, egress or network. This
AR adds a required CI stage that exercises the complete benchmark path end to
end against loopback and synthetic doubles: provider selection, live-mode
planning, execution with the deterministic double, capture, sealing, and strict
offline replay, plus the hostile negative cases. No secret, paid call, or
provider egress is permitted in any automated run; the unchanged 90% coverage
floor and all other native, formal, platform and privacy gates remain green.
