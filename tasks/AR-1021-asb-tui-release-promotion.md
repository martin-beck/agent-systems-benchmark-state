---
{
  "branch": "feature/asb-tui-release-promotion",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1017",
    "AR-1018",
    "AR-1019",
    "AR-1020",
    "AR-0877",
    "AR-0906"
  ],
  "id": "AR-1021",
  "next_action": "Review exact-head PR 8 hosted evidence, merge without weakening permanent protections, then obtain exact-main hosted and trusted local evidence.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1021.md",
  "priority": "P2",
  "schema_version": 1,
  "status": "done",
  "summary": "Audit and promote asb-tui from optional extension to verified release when eligible.",
  "task_revision": 5,
  "title": "Audit and promote the asb-tui release channel",
  "updated_at": "2026-09-10T17:17:11+00:00",
  "worktree_key": "agent-systems-benchmark-asb-tui-release-promotion"
}
---
Run independent source, license, SBOM, provenance, security, protocol, platform, UX, and exact-head
CI audits. Maintain an explicitly labelled optional/unverified channel until every policy and formal
requirement passes for asb-tui and its exact coordinator and workflow-quality releases; only then
promote the same user workflow to the verified release channel.

Acceptance criteria: public installation/upgrade workflows, capability matrix, evidence limits,
artifact cleanup policy, signed release provenance, and documented promotion/rollback criteria.

- 2026-09-10T17:06:28+00:00: All dependencies are now complete: AR-1017 through AR-1020 are
  published with exact-main hosted and trusted local evidence, and AR-0877/AR-0906 were integrated
  with AR-0907 through all-green combined and exact-main formal/platform gates. Promote for
  independent release-channel audit; retain optional/unverified classification unless signed release
  artifacts and every promotion criterion are proven.

- 2026-09-10T17:06:31+00:00: Claimed by asb_tui_coordinator_20260910.

- 2026-09-10T17:14:47+00:00: Published signed+DCO asb-tui PR 8 at exact head
  1e16eb36702e305113a096fdfed5da9bad65c3ca. The change documents and machine-enforces the
  source-only optional/unverified channel, capability and evidence limits, signed bundle promotion
  gates, rollback and artifact cleanup, MIT licensing, and Huawei Technologies Co., Ltd. 2026
  copyright headers. No tag or binary release was created because ASB routing and qualified
  interactive rendering remain unavailable. Local Rust 1.93.0 formatting, clippy, 77 tests plus
  doctests, documentation, schema/publication validation, workflow quality, coverage, and secret
  scanning passed. Hosted exact-head CI is pending; protected trusted-main verification remains
  intentionally post-merge only.

- 2026-09-10T17:17:11+00:00: Independent release-channel audit completed. Public PR 8 merged as
  GitHub-verified+DCO main 3d2b6b537da817469bf8a39841ccf9a79a4c370f with reviewed tree
  54a1eecdd3b06e2c251ef57eb4b93444f77e4fa6. Exact-main hosted Repository quality run 34507098594 and
  protected trusted local run 34507098555 both passed. The repository is public and MIT licensed;
  Huawei Technologies Co., Ltd. 2026 copyright and SPDX enforcement, signed release provenance
  criteria, capability/evidence matrix, public lifecycle unavailability, rollback, and cleanup
  policy are documented and CI-enforced. Strict required CI, signed commits, admin enforcement,
  conversation resolution, and force/delete prevention are restored. No tag or binary release
  exists: the channel correctly remains source-only optional_unverified because ASB external routing
  and the qualified interactive UI are absent. Promotion now fails closed until every
  machine-readable condition becomes true.
