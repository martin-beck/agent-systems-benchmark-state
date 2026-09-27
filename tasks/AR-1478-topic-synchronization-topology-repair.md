---
{
  "schema_version": 1,
  "id": "AR-1478",
  "title": "Repair topic synchronization topology",
  "status": "planned",
  "priority": "P0",
  "summary": "Repair protected-main topic synchronization topology after AR-1477 merge policy failure.",
  "next_action": "Promote after validating completed dependencies, inspect exact merge ancestry, and apply only the smallest policy-compliant topology repair.",
  "task_revision": 1,
  "updated_at": "2026-09-27T05:33:00+00:00",
  "owner": "",
  "claim_expires": "",
  "worktree_key": "agent-systems-benchmark-ar-1478-topic-synchronization-topology-repair",
  "branch": "feature/ar-1478-topic-synchronization-topology-repair",
  "checkpoint_commit": "",
  "plan": "../plans/AR-1478-topic-synchronization-topology-repair.md",
  "depends_on": ["AR-1475", "AR-1476", "AR-1379"]
}
---

Successor created from AR-1477’s exact protected-main post-merge policy
failure. It must preserve the reviewed product tree and repair only ancestry
or synchronization topology permitted by the policy.

- 2026-09-27T05:33:00+00:00: Created after Repository Quality workflow
  `36297383090` rejected merge `67fa0d1a` because the topic synchronization
  merge was not at the tip.
