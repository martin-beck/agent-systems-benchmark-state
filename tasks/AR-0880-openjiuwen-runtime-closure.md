---
{
  "branch": "fix/openjiuwen-runtime-closure",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-0857"
  ],
  "id": "AR-0880",
  "next_action": "Regenerate and verify the exact OpenJiuwen cli plus observability runtime closure, then prove imports and the console entry point before unblocking AR-0859.",
  "owner": "",
  "plan": "../plans/AR-0880.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "open",
  "summary": "Repair the incomplete pinned OpenJiuwen Python runtime closure required by live qualification.",
  "task_revision": 2,
  "title": "Repair OpenJiuwen runtime closure",
  "updated_at": "2026-09-09T07:14:48+00:00",
  "worktree_key": "agent-systems-benchmark-openjiuwen-runtime-closure"
}
---
## AR-0880

Repair the immutable OpenJiuwen `0.1.17.post1` runtime lock after AR-0859 proved that the
provenance-pinned console executable imports packages excluded by the original base-only lock.
The repair is a prerequisite for resuming AR-0859; it does not itself establish live support.

The formal dependency is AR-0857 only. AR-0859 supplied the immutable failure evidence but is not
a dependency, avoiding a completion cycle while AR-0859 remains blocked on this repair.


- 2026-09-09T07:14:48+00:00: AR-0857 is done; AR-0859 is blocked and released. Exact Python
  lock/provenance/import-test paths are disjoint from active lanes, no Cargo or schema fence is
  required, and the repair dependency graph is acyclic.
