---
{
  "branch": "coord/agents-openjiuwen-workbuddy",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-0862",
    "AR-0868"
  ],
  "id": "AR-0856",
  "next_action": "Keep planned while both child series run independently; complete only after AR-0862 and AR-0868 are durably done with executable live/replay qualification.",
  "owner": "",
  "plan": "../plans/AR-0856.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "planned",
  "summary": "Coordinate independently qualified OpenJiuwen and WorkBuddy support without merging their provenance or evidence boundaries.",
  "task_revision": 3,
  "title": "Coordinate OpenJiuwen and WorkBuddy agent support",
  "updated_at": "2026-09-08T18:55:00+00:00",
  "worktree_key": "agent-systems-benchmark-agents-openjiuwen-workbuddy"
}
---
## AR-0856

Umbrella only: OpenJiuwen phases are AR-0857 through AR-0862 and WorkBuddy phases are AR-0863
through AR-0868. The two series proceed independently, but this AR remains planned and cannot be
released until both final qualification children are durably done. A blocked phase stays an exact
dependency blocker; it is never converted into an unsupported label merely to close the umbrella.
