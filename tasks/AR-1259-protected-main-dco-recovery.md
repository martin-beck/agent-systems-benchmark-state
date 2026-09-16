---
{
  "branch": "repair/pr202-protected-main-dco",
  "checkpoint_commit": "14b604fec262575496f8838db1456679b1b14bbf",
  "claim_expires": "",
  "depends_on": ["AR-0813"],
  "id": "AR-1259",
  "next_action": "Promote and claim; create signed protected-main recovery preserving PR202 tree and parents, then run exact-main policy and all post-merge gates.",
  "observed_branch": "repair/pr202-protected-main-dco",
  "observed_dirty": 0,
  "observed_head": "14b604fec262575496f8838db1456679b1b14bbf",
  "owner": "",
  "plan": "../plans/AR-1259.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Recover a signed protected-main DCO boundary after the unsigned PR202 web merge.",
  "task_revision": 1,
  "title": "Protected-main DCO recovery for PR202",
  "updated_at": "2026-09-16T16:40:00+00:00",
  "worktree_key": "agent-systems-benchmark-protected-main-dco-1259"
}
---

## AR-1259

Create a signed, forward-only protected-main recovery for the unsigned PR202 merge.

- 2026-09-16T16:40:00+00:00: Created as successor to AR-0813. PR202 merge
  `14b604fec262575496f8838db1456679b1b14bbf` has parents `a0befc0ff247a42b8d796af161b58b1011de8377`
  and `b7d9e142d684f1fa65fc3f52258ec46585194950`, but no Signed-off-by trailer. Preserve
  source tree and require signed recovery plus exact-main policy/post-merge evidence.
