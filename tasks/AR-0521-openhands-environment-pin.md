---
{
  "branch": "feature/replay-openhands-environment-pin",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-0309", "AR-0514"],
  "id": "AR-0521",
  "next_action": "Define an immutable, reproducible OpenHands environment bundle and verifier.",
  "observed_branch": "", "observed_dirty": 0, "observed_head": "", "owner": "",
  "plan": "../plans/AR-0521.md", "priority": "P0", "schema_version": 1,
  "status": "planned", "summary": "Repair OpenHands replay environment provenance and reproducibility.",
  "task_revision": 1, "title": "Reproduce and pin the OpenHands replay environment",
  "updated_at": "2026-09-08T08:52:00+00:00", "worktree_key": "agent-systems-benchmark-replay-openhands-environment-pin"
}
---
## AR-0521

Repair missing reproducible provenance for the approved OpenHands replay environment. Do not bypass the digest or use unverifiable proprietary artifacts.

Acceptance requires a content-addressed environment bundle, offline verifier, dependency and license evidence, reproducible rebuild instructions, and a negative altered-input test. Only then may AR-0514 be reclaimed.
