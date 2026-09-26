---
{
  "branch": "feature/ar-1456-local-mock-multi-agent-campaign-successor",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1332",
    "AR-1433",
    "AR-1447"
  ],
  "id": "AR-1456",
  "next_action": "Promote after dependencies are verified; implement the credential-free local/mock multi-agent campaign successor and keep optional live integration separate.",
  "owner": "",
  "plan": "../plans/AR-1456.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "planned",
  "summary": "Decouple mandatory local/mock multi-agent campaign qualification from optional live-provider execution.",
  "task_revision": 1,
  "title": "Local/mock multi-agent campaign successor",
  "updated_at": "2026-09-26T19:40:20+02:00",
  "worktree_key": "agent-systems-benchmark-ar-1456-local-mock-multi-agent-campaign-successor"
}
---

AR-1456 is the ASB-only successor for the mandatory local/mock portion of
AR-1333. It must never require a provider key, external endpoint, live
`LiveProviderAttempt`, or AR-1329 production authority. AR-1329 remains the
optional production/live campaign integration boundary and is not a dependency
for local development, CI, or this AR's completion.

- 2026-09-26T19:40:20+02:00: Created after the dependency audit found that the
  completed ASB local campaign qualifications (AR-1437 and AR-1447) already
  prove the deterministic path while AR-1333 still incorrectly depends on the
  blocked optional live AR-1329.
