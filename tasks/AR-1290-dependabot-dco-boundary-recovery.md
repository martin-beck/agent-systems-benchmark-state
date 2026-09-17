---
{
  "branch": "repair/ar-1290-dependabot-dco",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-17T05:39:04+00:00",
  "depends_on": [],
  "id": "AR-1290",
  "next_action": "Monitor updated PR #212 exact head 418960215134b89710e5549351c5bf30ad17d3b7 until all required checks terminal-success; independent exact-head re-review is required after fuzz policy fix. Do not merge until every check passes.",
  "observed_branch": "repair/ar-1290-dependabot-dco",
  "observed_dirty": 0,
  "observed_head": "418960215134b89710e5549351c5bf30ad17d3b7",
  "owner": "asb_ar1024_lifecycle_router",
  "plan": "../plans/AR-1290.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Recover protected-main DCO assurance for the immutable Dependabot serde commit without weakening broad policy.",
  "task_revision": 31,
  "title": "Dependabot DCO boundary recovery",
  "updated_at": "2026-09-17T03:46:59+00:00",
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

- 2026-09-17T03:42:56+00:00: Recorded command exit 0; command argv SHA-256
  eba0a6a3c3958248bd22f0486f47480bb384b299a7deedee99d61164183d8a11.

- 2026-09-17T03:43:18+00:00: Audited PR #151 exact head 07d4b62: open Dependabot branch, parent
  protected main 2de393a, not an ancestor of main; trailer support@github.com does not match
  canonical author 49699333+dependabot[bot]@users.noreply.github.com, so no immutable-history
  exception is warranted. Recreated identical 12-path serde 1.0.229 diff in signed+DCO 04ce4ac, then
  fixed hosted locked-gate drift exposed by PR151: formal/Cargo.lock and fuzz/Cargo.lock required
  refreshes. Signed+DCO 1cff949 adds only those two generated lockfiles. Local cargo fmt --check and
  cargo test --locked --workspace pass (all observed suites green;
  provider/replay/sandbox/fault/formal tests pass). Independent review approved exact 04ce4ac before
  lockfile refresh; re-review required for exact 1cff949 before publication.

- 2026-09-17T03:43:46+00:00: Recorded command exit 0; command argv SHA-256
  338c173d7b437eec8dcacee53eebffbaabf2c448dc8d8fb649977426d8ab81d3.

- 2026-09-17T03:44:02+00:00: Recorded command exit 0; command argv SHA-256
  f6442e7ff280996c5efc7f32ab7709271647509badae702401a03593fe5d1b57.

- 2026-09-17T03:44:34+00:00: Published replacement PR #212
  https://github.com/martin-beck/agent-systems-benchmark/pull/212 from clean signed+DCO commits
  04ce4ac and 1cff949. Scope is 12 original serde manifest/lock paths plus generated
  formal/Cargo.lock and fuzz/Cargo.lock refreshes required by locked CI. Both commits verify Good
  SSH signatures and matching Martin DCO; exact diff check passes. Closed original unmerged PR #151
  after replacement became safely open; no history rewrite and no immutable exception. Local fmt and
  cargo test --locked --workspace passed with provider/replay/sandbox/formal/fault suites green.

- 2026-09-17T03:44:55+00:00: Recorded command exit 1; command argv SHA-256
  6cc1b2c2d7205567e61024af63495487d0243850d4eac25508415b686a38ad2a.

- 2026-09-17T03:45:11+00:00: Recorded command exit 1; command argv SHA-256
  7f498343cfe42cd8e0842d9c3ae8bc5764ac3e3462b723629629264458f64a7b.

- 2026-09-17T03:45:26+00:00: Recorded command exit 0; command argv SHA-256
  2ccb17e42bc7c11dced86dd93b0681e524ff5bea2af0fb1c854f33c51f89a30c.

- 2026-09-17T03:45:45+00:00: Recorded command exit 101; command argv SHA-256
  9a16ca9e151322355693b24a31a57fdeb37182685c8d685c17a88578772abf55.

- 2026-09-17T03:45:55+00:00: Recorded command exit 0; command argv SHA-256
  d215a98fef899cfeaa09485e24db58b391a7af6c48ff50bcbabcf274c423ffa3.

- 2026-09-17T03:46:12+00:00: Recorded command exit 0; command argv SHA-256
  6a7b8a9561df316593aef3f953d5bec19bc7e1349eab88c6aeb5ca389ed62ecb.

- 2026-09-17T03:46:39+00:00: PR #212 initial head 1cff949 failed Bounded fuzz because cargo-deny
  detected duplicate syn 3.0.6 while fuzz/deny.toml skipped syn@3.0.5; Loom/formal also failed
  locked lockfile checks on the same head. Diagnosis is deterministic lock/policy alignment, not a
  runtime defect. Added minimal signed+DCO 4189602 changing only fuzz/deny.toml syn skip to 3.0.6,
  pushed cumulative exact head 4189602. Original PR151 remains closed; no historical exception or
  force update used. Local cargo deny binary is unavailable (command not installed), so hosted
  policy must validate the pin.

- 2026-09-17T03:46:59+00:00: Recorded command exit 8; command argv SHA-256
  6cc1b2c2d7205567e61024af63495487d0243850d4eac25508415b686a38ad2a.
