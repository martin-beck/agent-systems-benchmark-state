---
{
  "branch": "repair/ar-1290-dependabot-dco",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-17T05:39:04+00:00",
  "depends_on": [],
  "id": "AR-1290",
  "next_action": "Audit whether 07d4b62 is an ancestor of protected main. Prefer closing/superseding the unmerged Dependabot PR and recreating its exact dependency diff in a signed+DCO topic; use a narrowly hash-bound immutable-history attestation only if ancestry proves unavoidable.",
  "observed_branch": "repair/ar-1290-dependabot-dco",
  "observed_dirty": 0,
  "observed_head": "2de393a05cc3c65f3495238abb19408e8218e483",
  "owner": "asb_ar1024_lifecycle_router",
  "plan": "../plans/AR-1290.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Recover protected-main DCO assurance for the immutable Dependabot serde commit without weakening broad policy.",
  "task_revision": 5,
  "title": "Dependabot DCO boundary recovery",
  "updated_at": "2026-09-17T03:39:46+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1290-dependabot-dco"
}
---

## AR-1290

The protected-main quality workflow rejected Dependabot commit `07d4b62` because its
trailer does not match the commit author's canonical identity. This successor owns only
the forward-only DCO recovery and policy evidence. It must not rewrite published history,
change certificate/runtime behavior, touch asb-tui, or weaken broad policy.

- 2026-09-17T03:40:00+00:00: Created after exact hosted failure showed repository policy
  rejecting `07d4b62ad5c10444e5d0ba5f014613cd7c34c0f5` for lacking a matching Signed-off-by
  trailer. The commit has a non-matching bot trailer (`support@github.com` versus its
  canonical author identity) and is associated with open PR #151. AR-1288 is the triggering
  feature context but is intentionally not a blocking dependency: its closure must wait for
  this remediation, so adding it here would deadlock the state graph. No AR-1288 paths are
  modified here.

- 2026-09-17T03:38:58+00:00: Promote independent P0 repair: PR #151 is unmerged; recreate its exact
  dependency diff from protected main in a fresh signed+DCO topic, with no historical exception.

- 2026-09-17T03:39:04+00:00: Claimed by asb_ar1024_lifecycle_router.

- 2026-09-17T03:39:39+00:00: Recorded command exit 128; command argv SHA-256
  de8294ffb66b2a42902c535c98fbd17388f69504fc431b2d99ecfceed16f9b69.
