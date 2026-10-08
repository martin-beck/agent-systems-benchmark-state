---
{
  "branch": "repair/ar-1746-protected-main-admission",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-08T18:17:11+00:00",
  "depends_on": [
    "AR-1427",
    "AR-1431"
  ],
  "id": "AR-1746",
  "next_action": "Require all exact-main post-merge workflows for 2f52ecbaf79ae8316e0c2a42ad4c4a79dae5d9eb terminal-success, then invoke the merged typed settings apply once and audit normalized live state; stop on any rejected, partial, or ambiguous result.",
  "observed_branch": "repair/ar-1746-protected-main-admission",
  "observed_dirty": 0,
  "observed_head": "fee04c29616b56cac8c54f1afd4539bedce7dee2",
  "owner": "ar1746_protected_main_admission_20261008",
  "plan": "../plans/AR-1746-protected-main-admission-enforcement.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_ref": "specs/AR-1746.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Apply and independently verify ASB's merge-only protected-main settings and active exact-head ruleset so signed local integrations are enforced by GitHub.",
  "task_revision": 40,
  "title": "Enforce protected-main admission for AR-1722 recovery",
  "updated_at": "2026-10-08T17:20:11+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1746-protected-main-admission"
}
---

ASB AR-1722 cannot be truthfully reopened while the repository's external
admission configuration contradicts the checked-in merge-integrity contract.
The current read-only audit reports merge, squash, and rebase enabled, web
signoff disabled, no rulesets, and no classic protection for `main`. Current
ASB product main is otherwise signed, reviewed-tree-equivalent, and hosted
green; this AR therefore owns the bounded external settings repair, not a
product-source rewrite.

Development review remains satisfied by an independent technical worker under
the same GitHub user after exact-head tests. No second account or authorized-
maintainer review is required. Signed commits, matching DCO, exact-tree local
integration, independent technical review, CI, and post-merge evidence remain
mandatory.

- 2026-10-08T16:15:53+00:00: AR-1427 and AR-1431 are done; current live audit confirms the external
  GitHub admission mismatch and no overlapping worker owns repository settings.

- 2026-10-08T16:17:11+00:00: Claimed by ar1746_protected_main_admission_20261008.

- 2026-10-08T16:17:43+00:00: Recorded command exit 0; command argv SHA-256
  94f02abdfe9b939aeb6a1a7498761e025303dd44291c9a4f26c429f01bcdabb9.

- 2026-10-08T16:18:55+00:00: Recorded command exit 1; command argv SHA-256
  e727b346f98e13fb2ad0d88b00531786a3633bbc23d161b0e4aee572bfb9cb4d.

- 2026-10-08T16:19:28+00:00: Recorded command exit 0; command argv SHA-256
  3dd458a2d11a2fec909a5e3d39168700e61303c564f68070ed11e7e681da45d1.

- 2026-10-08T16:20:16+00:00: Recorded command exit 0; command argv SHA-256
  cbe6a0354e44ba80ed71fe9ae7cf7b660d52c78f5a86c2b76cd9039e214845d9.

- 2026-10-08T16:21:08+00:00: Recorded command exit 1; command argv SHA-256
  71fedcebe66adb90148f9031e9484352cbc98a2265f346fbbb283de6193404a5.

- 2026-10-08T16:22:49+00:00: Recorded command exit 0; command argv SHA-256
  5c64f4b548ed68cd462c9280b85d0d78e108f16057a89f3b72d5bf50007b4235.

- 2026-10-08T16:24:53+00:00: Recorded command exit 0; command argv SHA-256
  32831504492c16501fc583fdecb04994cff2737510e6bc335987aaded540c0bc.

- 2026-10-08T16:25:52+00:00: Recorded command exit 0; command argv SHA-256
  a4a60d1754dba44f0346e48fb88f33be628214db142df79043e1672a6a3bfee6.

- 2026-10-08T16:26:33+00:00: Recorded command exit 0; command argv SHA-256
  cbe6a0354e44ba80ed71fe9ae7cf7b660d52c78f5a86c2b76cd9039e214845d9.

- 2026-10-08T16:27:07+00:00: Recorded command exit 1; command argv SHA-256
  7d2cf81f2128b77d684daeeb64c568284dd65fff80741db8fcb1d37103cc38e0.

- 2026-10-08T16:27:43+00:00: Recorded command exit 1; command argv SHA-256
  4d83e76ab2539e791b9b9ffc4f762e2b5b8713dd1ba12e4f3895ae2aa5afc53d.

- 2026-10-08T16:28:19+00:00: Recorded command exit 0; command argv SHA-256
  e59c072137c684d5a5e6176626204747cb5869d9da3ba5c6de84e5b50f810c45.

- 2026-10-08T16:29:15+00:00: Recorded command exit 0; command argv SHA-256
  cbe6a0354e44ba80ed71fe9ae7cf7b660d52c78f5a86c2b76cd9039e214845d9.

- 2026-10-08T16:29:47+00:00: Recorded command exit 0; command argv SHA-256
  2d700b4cbd9754e2b79a75c8682543a0487b36cc839a34d39adc552ed37e6844.

- 2026-10-08T16:30:23+00:00: Recorded command exit 0; command argv SHA-256
  7f62bf4391bbe415c88a0484f2fba40b5e5ebeadfea926aeefeb2469dbf92193.

- 2026-10-08T16:31:07+00:00: Recorded command exit 0; command argv SHA-256
  80172830c4b80c8b129e803a3fa0a4e49673192696722265cac7eb5fdc0df620.

- 2026-10-08T16:31:45+00:00: Recorded command exit 0; command argv SHA-256
  ce6b0c1c0e0321606c9bc1e550f1db7bf18efe150bf9b6982e6d9bca36d6d406.

- 2026-10-08T16:32:19+00:00: Recorded command exit 0; command argv SHA-256
  b60f2efeaac95790d76748581f0746bcb92cde3c8c32a80abee3e59cf935bab2.

- 2026-10-08T16:33:11+00:00: Recorded command exit 0; command argv SHA-256
  c879be0bde7885612921d009b1c99d125cf932ec5b32bc575b2bc4f085a8b4de.

- 2026-10-08T16:33:54+00:00: Recorded command exit 0; command argv SHA-256
  2b72bcf779569da24b15cf34dbb3810ff9938f5db4e22a12aa4ef5e50d7af6e7.

- 2026-10-08T16:34:29+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-10-08T16:36:26+00:00: Recorded command exit 0; command argv SHA-256
  6b4acbb524e6167877eedbed68409930ee6ed7c40a785cbbc05ae9b000a9dc5d.

- 2026-10-08T16:37:03+00:00: Recorded command exit 0; command argv SHA-256
  593f559de2c3f7a1ca8d0d339f8d0b262eb0834e3b0af27b573e5a2843dae2e8.

- 2026-10-08T16:50:39+00:00: Recorded command exit 0; command argv SHA-256
  9367942f751e5b41aba925e8ef9604831f156c95a9d65f8bb4edb3a82fa252b6.

- 2026-10-08T16:51:18+00:00: Recorded command exit 0; command argv SHA-256
  ff075de826de3ad7f165284e3dd2940bdb8cf2bb618eb81301a27055ede844a7.

- 2026-10-08T16:51:58+00:00: PR #513 exact reviewed head
  fee04c29616b56cac8c54f1afd4539bedce7dee2/tree aeb7841fc289b938e709aa87ecfecf3ae7cbd892 passed
  14/14 hosted checks and independent review. Local signed merge
  2f52ecbaf79ae8316e0c2a42ad4c4a79dae5d9eb has parents 5e8e5b7fdb04a50950e0790d9d66c605e7978606 and
  fee04c29616b56cac8c54f1afd4539bedce7dee2, preserves exact reviewed tree
  aeb7841fc289b938e709aa87ecfecf3ae7cbd892, and passes allowed SSH signature plus matching DCO
  verification.

- 2026-10-08T17:16:04+00:00: Recorded command exit 0; command argv SHA-256
  8ad5c9cdc1a5e3a50a3216e8e5f95b2090d440b66ee1d3561613dbfb4354329a.

- 2026-10-08T17:16:52+00:00: Recorded command exit 1; command argv SHA-256
  4c43b6dd74b5f2d66c24e5870e26e43b7b0f60910aed91081694319b6b8c508c.

- 2026-10-08T17:18:09+00:00: Recorded command exit 1; command argv SHA-256
  4fe5e6df52eee69f9abda47b6896be6dcde0d41f363cfac5b974b99168d876d4.

- 2026-10-08T17:18:56+00:00: Recorded command exit 0; command argv SHA-256
  d4023eeb0b733a8e10eaf93567adcef0e61e3390b6aa1b98fffc7d66f86835b4.

- 2026-10-08T17:19:38+00:00: Recorded command exit 0; command argv SHA-256
  6b9a063ca5c2e2e9821b458afe0d56d38df6c3a530762e32dbb5f296f59bfcc8.

- 2026-10-08T17:20:11+00:00: Recorded command exit 0; command argv SHA-256
  e85f35d7b680e1e5a6eb3bc5c537033b82293cbff0f6a036db7dbb3bf4b73565.
