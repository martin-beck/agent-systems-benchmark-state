---
{
  "branch": "feature/frontend-privacy-assurance",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-08T11:21:28+00:00",
  "depends_on": [
    "AR-0840",
    "AR-0841"
  ],
  "id": "AR-0843",
  "next_action": "Enforce public-summary and sensitive-artifact boundaries with privacy and fault tests.",
  "owner": "quality_20260906",
  "plan": "../plans/AR-0843.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Qualify frontend privacy, artifact access, and fault behavior.",
  "task_revision": 3,
  "title": "Assure frontend privacy and faults",
  "updated_at": "2026-09-08T08:21:28+00:00",
  "worktree_key": "agent-systems-benchmark-frontend-privacy-assurance"
}
---
## AR-0843

Separate public summaries from sensitive artifacts and enforce least-privilege access. Test malformed,
stale, duplicate, oversized, slow-client, disconnect, restart, authorization, compatibility, and
redaction failures; prove no credentials, prompts, transcripts, or private paths reach the default API.

- 2026-09-08T08:21:26+00:00: Promoted as the highest-priority dependency-ready safe leaf after
  AR-0842 release. AR-0840 and AR-0841 are done; the prior frontend lifecycle owner is idle; no
  branch, worktree, process, lease or active AR path overlap was found. AR-0837 was not promoted
  because required AR-0836 remains blocked.

- 2026-09-08T08:21:28+00:00: Claimed by quality_20260906.
