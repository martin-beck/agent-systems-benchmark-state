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
  "observed_dirty": 5,
  "observed_head": "a4782cdc467d38996473168cc5d2ccedfae75a25",
  "owner": "contracts-20260906",
  "plan": "../plans/AR-0835.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Remediate runner privacy leakage and protected-workflow guard gaps found during independent audit.",
  "task_revision": 26,
  "title": "Remediate runner privacy and workflow guards",
  "updated_at": "2026-09-07T08:03:14+00:00",
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

- 2026-09-07T07:49:32+00:00: Recorded command exit 0; command argv SHA-256
  dd22db57eacab65928b3e7fba885f8d91a2a45e9db16a71b008db23c69a0962b.

- 2026-09-07T07:51:48+00:00: Recorded command exit 128; command argv SHA-256
  133380a7a42dd767b6ac5cd0870d90c66a98dcd8c10fb187ec92624a0f99ccc7.

- 2026-09-07T07:54:33+00:00: Recorded command exit 0; command argv SHA-256
  133380a7a42dd767b6ac5cd0870d90c66a98dcd8c10fb187ec92624a0f99ccc7.

- 2026-09-07T07:54:49+00:00: Recorded command exit 1; command argv SHA-256
  a9af29dc82426b9d529a7e6788d8c9328d2a10a8edeb16e71aacf870371b2d3f.

- 2026-09-07T07:56:22+00:00: Recorded command exit 0; command argv SHA-256
  3a3e0fde30d0ffe5571623eb4eff801c4cf5de5a52988fdce788067de0d4fcda.

- 2026-09-07T07:56:28+00:00: Recorded command exit 0; command argv SHA-256
  df2f0be0ea8b505d097c4ff86af5c623435ac9fe1cd6c133ae421f32a92c2ffa.

- 2026-09-07T07:56:33+00:00: Recorded command exit 0; command argv SHA-256
  0aa1e1322ccc6658ee8b50536e7e8a5bb6a401f587df34dbc69758d0e64c75be.

- 2026-09-07T07:56:49+00:00: Recorded command exit 1; command argv SHA-256
  9b354e01a396325a99a73932b27fff689515115c8a7e2afb7003329b4adfe167.

- 2026-09-07T07:57:14+00:00: Recorded command exit 0; command argv SHA-256
  3a3e0fde30d0ffe5571623eb4eff801c4cf5de5a52988fdce788067de0d4fcda.

- 2026-09-07T07:57:46+00:00: Recorded command exit 0; command argv SHA-256
  9b354e01a396325a99a73932b27fff689515115c8a7e2afb7003329b4adfe167.

- 2026-09-07T07:59:12+00:00: Recorded command exit 0; command argv SHA-256
  621fdfdc1f6252394cc2d79f3de8abb73644206b7f853781a6b4ec6280d99ea9.

- 2026-09-07T07:59:17+00:00: Recorded command exit 0; command argv SHA-256
  8362f6137c56995c6571a497edae11307cf054fc863a4a9491db8c110b5af6dd.

- 2026-09-07T07:59:22+00:00: Recorded command exit 0; command argv SHA-256
  ee436c9f78c9ed6e6111252dd479e72031aee59583d6a8166fc0c41d95882734.

- 2026-09-07T07:59:27+00:00: Recorded command exit 0; command argv SHA-256
  12950bd8eb24047b6cd030b08663ab3704e700b7879c2bef81f0670e601d592d.

- 2026-09-07T08:00:05+00:00: Recorded command exit 0; command argv SHA-256
  9b354e01a396325a99a73932b27fff689515115c8a7e2afb7003329b4adfe167.

- 2026-09-07T08:01:26+00:00: Recorded command exit 0; command argv SHA-256
  012f5095c438d1eaab71a5c4a6e53c2910b3a38de6d366d1f304ac122d6ddbfd.

- 2026-09-07T08:01:36+00:00: Recorded command exit 1; command argv SHA-256
  629426c5edfb4b81138dcc7eaaeb5ef37e036aa9e4a0cf7b1d26c0083c7dfb63.

- 2026-09-07T08:02:31+00:00: Recorded command exit 0; command argv SHA-256
  9b7766c63b8bead01b49a8703693e100f0f349295fa17e0d285ececa8b9eff4c.

- 2026-09-07T08:02:36+00:00: Recorded command exit 0; command argv SHA-256
  7c15133a47f3d4a848ff146885dee7e6ed8ad3a6cc06a136d75af9196f7833d8.

- 2026-09-07T08:02:41+00:00: Recorded command exit 0; command argv SHA-256
  34ccb1935cafa6df7f231552ffc9dda9e1cb4c7536ad8492a5b3bc833c86e31a.

- 2026-09-07T08:03:14+00:00: Recorded command exit 0; command argv SHA-256
  629426c5edfb4b81138dcc7eaaeb5ef37e036aa9e4a0cf7b1d26c0083c7dfb63.
