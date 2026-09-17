---
{
  "branch": "feature/shared-workflow-coordinator",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [],
  "id": "AR-0852",
  "next_action": "Preserve merged v0.1.4 effect e52ce3aa without history rewrite; complete a focused signed+DCO repair or documented signed state replacement under AR-0853, then re-audit live main before releasing AR-0852.",
  "owner": "",
  "plan": "../plans/AR-0852.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "done",
  "summary": "Adopt the path-exclusive coordinator commit fix discovered during live integration.",
  "task_revision": 15,
  "title": "Adopt coordinator path isolation fix",
  "updated_at": "2026-09-08T08:09:00+00:00",
  "worktree_key": "agent-systems-benchmark-shared-coordinator"
}
---

This follow-up preserves unrelated staged work by updating the pinned shared coordinator from
v0.1.3 to v0.1.4 after AR-0851 was completed.

- 2026-09-08T07:21:36+00:00: The exact v0.1.4 PR head passed implementation and formal CI.

- 2026-09-08T07:21:38+00:00: Claimed by codex-agent-workflow-coordinator-asb-v014-20260908.

- 2026-09-08T07:22:22+00:00: Recorded command exit 0; command argv SHA-256
  ad5cd7d7a908eac0a5fce51389fcd4f9e88ba985812ac8ec1ae7b75ba36c1dd9.

- 2026-09-08T07:25:22+00:00: Lease expired at 09:21:38Z with no active process; durable branch
  e4fecc1 preserved clean and no PR exists. Lease recovery only; re-audit and reclaim before any
  publication.

- 2026-09-08T07:26:27+00:00: Claimed by replay-20260906.

- 2026-09-08T07:30:19+00:00: Recorded command exit 1; command argv SHA-256
  ca1974136b5430835c02afc481746c096c0686555f6f8f7db1cee16755a8c27e.

- 2026-09-08T07:31:11+00:00: Recorded command exit 0; command argv SHA-256
  78a427bc7f9b2a47eb1dcdf36f2de84f01558de54583ccbdbef7d62af35315dd.

- 2026-09-08T07:31:51+00:00: Recovered publication audit: exact SSH-signed+DCO head e4fecc1e was
  already merged by PR 10 as e52ce3aaa59ffc4cc6f97657b6ea2c7dfceb2ac1. All 17 manifest artifacts
  byte-match signed upstream v0.1.4 tag and signed+DCO commit
  9733b341f25b145d6dfad8414933cb6348701769; exact-head CI was green; vendor verifier and six vendor
  tests plus six subtests pass; exact binding rejection tests and schema pass. Release blocked
  because the merge commit has no locally verifiable SSH signature and no Signed-off-by trailer.
  Preserve it; no republish or history rewrite.

- 2026-09-08T07:33:29+00:00: Recorded command exit 0; command argv SHA-256
  ccbec4b2be4e66a616e7194142ff049d96fc80d9966f6f8d05321acb221f974d.

- 2026-09-08T07:34:50+00:00: Recorded command exit 0; command argv SHA-256
  261d8b5a4c9334d9a40c2f2a208a49199ea6857aa72ae9bc41982853b5a25221.

- 2026-09-08T07:34:59+00:00: Durable PR #10 merge and v0.1.4 content are verified, but completion is
  deferred to dependency-free AR-0853 for signed/DCO additive attestation; preserve e52ce3aa and
  exact branch, no rewrite.

- 2026-09-08T08:06:06+00:00: Claimed by replay-20260906.

- 2026-09-08T08:06:23+00:00: Recorded command exit 0; command argv SHA-256
  51812688623dd5a56dd6baa6f2a5a87fca74bf5050fe9a772ccc067fd83df387.

- 2026-09-08T08:09:00+00:00: Released AR-0852 after preserving PR 10 merge
  e52ce3aaa59ffc4cc6f97657b6ea2c7dfceb2ac1 and completing dependency-free AR-0853 additive repair.
  Signed+DCO PR 11 merge 8bc57761488a1e3319307456d2a763d5418d2dd6 binds the exact v0.1.4 head,
  trees, ordered parents, signed upstream release and manifest digest while honestly retaining the
  original merge signature/DCO limitation. Exact-main coordination run 34202334252 and formal run
  34202334155 passed; postmerge vendor verification, full contracts, binding negatives, schema,
  coverage and formal gates passed. Reconcile and live doctor passed at 1ac71340.
