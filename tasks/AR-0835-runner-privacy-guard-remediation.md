---
{
  "branch": "fix/runner-canary-privacy-guards",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-07T10:48:09+00:00",
  "depends_on": [
    "AR-0830",
    "AR-0831"
  ],
  "id": "AR-0835",
  "next_action": "Remove or narrow runner identity leakage in canary output and enforce repository/main-ref guards for every persistent-runner workflow.",
  "observed_branch": "fix/runner-canary-privacy-guards",
  "observed_dirty": 0,
  "observed_head": "a4782cdc467d38996473168cc5d2ccedfae75a25",
  "owner": "contracts-20260906",
  "plan": "../plans/AR-0835.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Remediate runner privacy leakage and protected-workflow guard gaps found during independent audit.",
  "task_revision": 4,
  "title": "Remediate runner privacy and workflow guards",
  "updated_at": "2026-09-07T07:49:30+00:00",
  "worktree_key": "agent-systems-benchmark-runner-privacy-guard-remediation"
}
---
## AR-0835

Remediate the independent audit finding that GitHub runner logs expose runner and machine identity,
and that the original canary lacks the repository/main-ref guard required by the routing contract.

Acceptance criteria:

- Remove or formally narrow public output claims; prove sanitized logs do not expose private identity.
- Add repository and protected-main guard to every persistent-runner workflow, including canary.
- Add negative fixtures for alternate refs, forks, identity leakage, and widened permissions.
- Re-run privacy, policy, actionlint/zizmor, exact-head CI, and post-merge audit checks.
- Update documentation to state evidence limits accurately.

- 2026-09-07T07:48:07+00:00: AR-0830 and AR-0831 are durably done; persistent-runner workflow
  privacy and guard remediation paths are dependency-ready and no active AR owns them.

- 2026-09-07T07:48:09+00:00: Claimed by contracts-20260906.
