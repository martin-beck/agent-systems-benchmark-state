---
{
  "branch": "repair/ar-1750-ruleset-response-normalization",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-08T22:56:21+00:00",
  "depends_on": [
    "AR-1427",
    "AR-1431"
  ],
  "id": "AR-1750",
  "next_action": "Claim from exact canonical main and repair owned ruleset ID 24750310 with strict request/response normalization before any settings PATCH.",
  "owner": "codex-asb-ar1750-ruleset-normalization-20261008",
  "plan": "../plans/AR-1750-github-ruleset-response-normalization.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_ref": "specs/AR-1750.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Repair GitHub ruleset request/readback canonicalization and development-review admission after AR-1748 created owned ruleset 24750310 but stopped before repository-settings mutation.",
  "task_revision": 2,
  "title": "Canonicalize GitHub ruleset response and complete guarded admission",
  "updated_at": "2026-10-08T20:56:21+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1750-ruleset-response-normalization"
}
---

AR-1748 merged portable protected-main provenance and its bounded head-projection
repair with independent review and all exact-head and post-merge workflows green.
Its one guarded live creation returned ruleset ID 24750310, but intermediate
readback differed because GitHub added response fields. The tool stopped before
the settings PATCH with phase=ruleset-readback, prior-ruleset-effect=applied,
settings-effect=not-attempted, effect=ambiguous, ruleset-id=24750310, and
ownership=response-only.

Before the call the ruleset inventory was empty. Afterwards it contained only
active branch ruleset 24750310 named ASB protected main publication. Repository
ID 1359260742, owner/type, visibility, main head, and settings were unchanged:
merge commits enabled; squash/rebase enabled; auto-merge disabled; web signoff
disabled. The requested policy was preserved, but GitHub added exactly
require_extra_approval_for_unattributed_changes=true and required_reviewers=[]
to pull_request.parameters.

This task owns only the narrow repair and completion. Preserve ruleset ID
24750310, never discover mutation ownership by name alone, never delete the
ruleset, and never retry an ambiguous mutation blindly.

- 2026-10-08T20:56:21+00:00: Claimed by codex-asb-ar1750-ruleset-normalization-20261008.
