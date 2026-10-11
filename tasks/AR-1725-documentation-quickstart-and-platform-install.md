---
{
  "branch": "docs/ar-1725-quickstart-platform-install",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1336",
    "AR-1338",
    "AR-1641",
    "AR-1642",
    "AR-1723",
    "AR-1724"
  ],
  "id": "AR-1725",
  "next_action": "Post-merge exact main verified at 7e795589fd4dbefecf17a7d4457623e1de33d2b4: tutorial freshness passes and broken link audit reports 0. Accept and release with protected merge evidence.",
  "observed_branch": "docs/ar-1725-quickstart-platform-install",
  "observed_dirty": 0,
  "observed_head": "695f1335c4ede05b174cb6f369c4415ec1556fcf",
  "owner": "",
  "plan": "../plans/AR-1725-documentation-quickstart-and-platform-install.md",
  "priority": "P1",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "hosted",
    "evidence_digest": "sha256:70152b91b50106d78434a4d5ed78119d744753e27c26e5f60c1055fdb31e1b05",
    "evidence_ref": "quality/AR-1725-postmerge-receipt.txt",
    "spec_ref": "specs/AR-1725.json",
    "spec_revision": 1,
    "status": "pass"
  },
  "spec_ref": "specs/AR-1725.json",
  "spec_revision": 1,
  "status": "done",
  "summary": "Publish a linked, executable tutorial for two-agent OpenRouter benchmarking, ASB TUI workflows, dependencies, and per-distribution installation.",
  "task_revision": 38,
  "title": "Document two-agent OpenRouter and TUI quickstarts",
  "updated_at": "2026-10-11T07:43:38+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1725-documentation-quickstart-and-platform-install"
}
---

Create one short, linked tutorial that starts with installation and setup, selects
two compatible agents and a catalog-advertised OpenRouter free model, runs a
bounded workload against the remote provider, reports results, and explains the
explicit `--local-mock` and offline replay alternatives. Add the equivalent ASB
TUI journey (install, setup, select agents/provider/model, launch, monitor,
report, compare, and recover) with links to the asb-tui documentation boundary.

Add a dependency/install matrix for supported distributions, including pinned
Rust/toolchain requirements, required sandbox utilities, package-manager
commands, architecture notes, and actionable missing-dependency diagnostics.
Link the tutorial from README, QUICKSTART, OPERATOR_QUICKSTART, and the workflow
index. Prefer repository-owned screenshots or terminal transcript images made by
the bounded tutorial runner; never include credentials, private paths, or raw
provider content. Keep live calls opt-in where the current command contract
requires it, and label development/live, local-mock, replay, and qualification
evidence accurately.

Required evidence: tutorial-contract validation, executable command checks,
broken-link and schema checks, per-distribution dependency review, accessibility
text alternatives for every image, focused documentation gates, full applicable
gates, independent review, and exact-head hosted CI.

- 2026-10-11T06:48:55+00:00: Dependencies AR-1336, AR-1338, AR-1641, AR-1642, AR-1723, and AR-1724
  are done with checkpoints; promote documentation work.

- 2026-10-11T06:49:01+00:00: Claimed by ar1725-docs-luna56.

- 2026-10-11T06:49:31+00:00: Recorded command exit 0; command argv SHA-256
  d37193f8b9ad44178b3bff0cac7209222030e84fb25b93f00b19c585f8613a80.

- 2026-10-11T06:50:38+00:00: Recorded command exit 0; command argv SHA-256
  3bbe6c566d9770a7f1e041418b0ef9d95bc000e60deb378c762e2bf9ad167037.

- 2026-10-11T06:51:17+00:00: Recorded command exit 1; command argv SHA-256
  e0a0bb647f155e5f5e9fbfdffe12d5b8c3fc184b58478142d806a3d3ba2ca235.

- 2026-10-11T06:51:31+00:00: Recorded command exit 1; command argv SHA-256
  d99fd3918f7a0ac25cf855ebbf388c5391b566e5bfb0167fd628c89c84c3703b.

- 2026-10-11T06:51:44+00:00: Recorded command exit 1; command argv SHA-256
  bec4f6ab4d3e6d5132eaa43c8346d38f44bdffd66910652f8d66aa0482376e34.

- 2026-10-11T06:51:58+00:00: Recorded command exit 1; command argv SHA-256
  f278f9f9e4a993604fd5adc660ce4f0c5c2f181fc5e0488f47e535c30ba52ccc.

- 2026-10-11T06:52:31+00:00: Recorded command exit 0; command argv SHA-256
  a940268f1a16b759cfb4943e16441addda9e02aa82cc87db8e87ca86c73fed0e.

- 2026-10-11T06:52:43+00:00: Reconciled branch/worktree metadata through declared docs branch;
  verified baseline platform validator failure on untouched origin/main; tutorial freshness and
  guide_examples pass.

- 2026-10-11T06:53:07+00:00: Recorded command exit 101; command argv SHA-256
  50ae99437335f68b1a359bca86cdd88eb1a713a77ce847602ccf0fc639fc13b7.

- 2026-10-11T06:53:26+00:00: Full workspace gate attempted through handoffctl: 221 passed, 1
  ignored, 1 pre-existing environment failure in
  mini_swe::cancellation_leaves_no_runnable_owned_descendant; no product files changed.

- 2026-10-11T06:55:10+00:00: Recorded command exit 101; command argv SHA-256
  534f8613e1c316db8f0f46dd989e44e14a8ca74304a94791b4e4a1c59b2fbb1d.

- 2026-10-11T06:55:20+00:00: Recorded command exit 0; command argv SHA-256
  291fabd83bf08a767418181c052af16df89b1ad4479b78758e72c89c9c1f0ad8.

- 2026-10-11T06:55:32+00:00: Recorded command exit 0; command argv SHA-256
  172e6767dea5102755e50e3776e15187fde7c7a3abccc9a1a2d94cc4bb7cbc8f.

- 2026-10-11T06:55:47+00:00: Recorded command exit 0; command argv SHA-256
  8ad8454be93e66e9620734215054c97b284dbe7368e5072633ee0df0b3db51aa.

- 2026-10-11T06:56:03+00:00: Recorded command exit 8; command argv SHA-256
  4d6bb5ff2d1fb0ee1a20a2ba91c20c542ca5f3e1e9630001fef585e75ac76810.

- 2026-10-11T06:59:39+00:00: Recorded command exit 0; command argv SHA-256
  63a11cb1501eb157019bfa1b8d99416730b8f8052b5a1311148b8a3b737b3ac1.

- 2026-10-11T07:00:18+00:00: Recorded command exit 0; command argv SHA-256
  515bdac4e61da48c9b8a5251cd9c5546974c0f169cceb072236bd4918b157b59.

- 2026-10-11T07:06:25+00:00: Reconciled durable state to clean squashed PR #565 head 34848868; prior
  draft PR #564 had a gitleaks false positive and is superseded.

- 2026-10-11T07:06:31+00:00: Recorded command exit 8; command argv SHA-256
  1dd74d5c789009242632fac966edc34829f5316081d56f81f33fbdc485eaa9eb.

- 2026-10-11T07:13:39+00:00: Recorded command exit 0; command argv SHA-256
  f8035fc59c3f5f9f46744f98a63cccb92668a028a0c5f2b05c3bdb242cc5bb82.

- 2026-10-11T07:14:32+00:00: Recorded command exit 0; command argv SHA-256
  321c534968b9c456a64caf5e6d09b63780c507f97548057d2bfe31edcfd73ff4.

- 2026-10-11T07:15:08+00:00: Recorded command exit 0; command argv SHA-256
  302205046dd42e639a99d4dde574129d345812e4a2fc9764db85af707c27543f.

- 2026-10-11T07:15:29+00:00: Recorded command exit 1; command argv SHA-256
  1dd74d5c789009242632fac966edc34829f5316081d56f81f33fbdc485eaa9eb.

- 2026-10-11T07:16:02+00:00: Recorded command exit 8; command argv SHA-256
  1dd74d5c789009242632fac966edc34829f5316081d56f81f33fbdc485eaa9eb.

- 2026-10-11T07:17:01+00:00: Rebased clean squashed PR #565 branch onto current protected main
  4cb87998 and force-with-lease published signed head 8028fd66. Prior head 34848868 was behind and
  superseded.

- 2026-10-11T07:26:56+00:00: Recorded command exit 0; command argv SHA-256
  92379fa5436963edcc9340b82b9eb11f9cf47432ebfa27753a6b08c7c28aa439.

- 2026-10-11T07:27:21+00:00: Recorded command exit 0; command argv SHA-256
  e2b1aa0823c05818b629e73743c03c0caefb74b1b2878e6c3ce7f18bf947ff30.

- 2026-10-11T07:38:40+00:00: Recorded command exit 0; command argv SHA-256
  52282ab33b5122139111868a58e512f0b82fc911c1b37a993e99a0f73defda02.

- 2026-10-11T07:39:28+00:00: PR #565 merged through protected main. Exact merged tree contains six
  validated tutorial contracts and all local Markdown links resolve.

- 2026-10-11T07:42:35+00:00: Recorded command exit 1; command argv SHA-256
  0fa2804bb302ff4d47a2656381e40f87ac9793f8655c974b4c12cbdae400b8d3.

- 2026-10-11T07:43:18+00:00: Protected PR #565 merged at exact main 7e795589. Post-merge tutorial
  freshness passed for 6 contracts and Markdown link audit passed with 0 broken links.

- 2026-10-11T07:43:21+00:00: Recorded command exit 0; command argv SHA-256
  0356ba3e9812b436f79c6cbc066dde99101bb6b554d4b31a5181d281f46e4811.

- 2026-10-11T07:43:38+00:00: AR-1725 complete: protected PR #565 merged at 7e795589; exact-main
  tutorial freshness and link audit passed; hosted acceptance evidence recorded.
