---
{
  "branch": "repair/ar-1290-dependabot-dco",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-17T05:39:04+00:00",
  "depends_on": [],
  "id": "AR-1290",
  "next_action": "Audit whether 07d4b62 is an ancestor of protected main. Prefer closing/superseding the unmerged Dependabot PR and recreating its exact dependency diff in a signed+DCO topic; use a narrowly hash-bound immutable-history attestation only if ancestry proves unavoidable.",
  "observed_branch": "repair/ar-1290-dependabot-dco",
  "observed_dirty": 2,
  "observed_head": "04ce4ac5eb93a58b1a1cc79f956698b8a9e0baac",
  "owner": "asb_ar1024_lifecycle_router",
  "plan": "../plans/AR-1290.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Recover protected-main DCO assurance for the immutable Dependabot serde commit without weakening broad policy.",
  "task_revision": 15,
  "title": "Dependabot DCO boundary recovery",
  "updated_at": "2026-09-17T03:42:47+00:00",
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

- 2026-09-17T03:39:56+00:00: Recorded command exit 0; command argv SHA-256
  14cc48ae273e644cf28ae2113a89300fed545b20477c5a7d810e6182e37f1c88.

- 2026-09-17T03:40:11+00:00: Recorded command exit 0; command argv SHA-256
  00cda6a95f253cd4b24c430186afa208955ddce2df17dc95d57ad1ba916ff044.

- 2026-09-17T03:40:26+00:00: Recorded command exit 0; command argv SHA-256
  da1a2d7aa3cf871a59cc77c11ef1afcf2478e3f60676ba802beb1e81e678912d.

- 2026-09-17T03:41:31+00:00: Recorded command exit 0; command argv SHA-256
  2e0684d4f343c15ffe045572aefefe4c38188dcd87051ff6c7c2611c40a4de8e.

- 2026-09-17T03:41:58+00:00: Recorded command exit 0; command argv SHA-256
  f45bd581b0af6cc62ef100865adacd4d665242d4ed42c9a38c4b37273679967a.

- 2026-09-17T03:42:14+00:00: Recorded command exit 0; command argv SHA-256
  ebdb62ba1ede446edcfe58670bd0c3f9cc59cf8602642ea94dd7deb92c0bb8b9.

- 2026-09-17T03:42:40+00:00: Recorded command exit 0; command argv SHA-256
  63baf0273263179ed394b2fea8d2a3402af8e5f048971b842280842f15f76394.
