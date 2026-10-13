---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [],
  "id": "AR-1861",
  "next_action": "Promote after AR-1841 and verify the immutable upstream AR-0034 repair source, then vendor it through the approved coordinator tool and qualify AR-1826 re-binding.",
  "owner": "",
  "plan": "../plans/AR-1861-coordinator-ar0034-repair-adoption.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Adopt the merged Coordinator AR-0034 partial-legacy worktree repair needed to unblock ASB AR-1826.",
  "task_revision": 1,
  "title": "Adopt Coordinator AR-0034 legacy-binding repair",
  "updated_at": "2026-10-13T00:00:00Z",
  "worktree_key": ""
}
---

Narrow downstream successor for the exact coordinator-owned seam recorded by
ASB AR-1826. AR-1841 remains historical context but is blocked on unrelated
v0.7.4 compatibility work; this task therefore has no unfinished ASB
dependency. It must consume the independently completed upstream AR-0034
repair at signed merge `3b200c9` (PR #1293 head `0bc30d4`) through the
approved vendor/provenance path. It must not patch vendored coordinator files
or mutate AR-1826 until the adopted repair is verified.

