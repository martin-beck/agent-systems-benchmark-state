---
{
  "branch": "repair/ar-1856-pr631-protected-main-identity",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-13T16:52:03+00:00",
  "depends_on": [],
  "id": "AR-1856",
  "next_action": "Await independent exact-head review and terminal-success required checks for PR #633 at product head 6e3c57ca6550d35a5997d214479939f525e1d0e3; then merge only via tools/integration/merge_pr.py --push and verify all exact-main workflows.",
  "owner": "ar1856-protected-main-repair-luna",
  "plan": "../plans/AR-1856-pr631-protected-main-identity-recovery.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "hosted",
    "evidence_digest": "",
    "evidence_ref": "",
    "spec_ref": "specs/AR-1856.json",
    "spec_revision": 1,
    "status": "pending"
  },
  "spec_ref": "specs/AR-1856.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Recover protected-main provenance after PR #631 was GitHub-web-merged with a non-local committer.",
  "task_revision": 27,
  "title": "PR #631 protected-main identity recovery",
  "updated_at": "2026-10-13T14:53:26+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1856-pr631-protected-main-identity"
}
---

PR #631 passed exact-head review and CI, but its immutable protected-main merge
`9d2290dc89c9610bb32680f2100759aeba29a06e` was created with committer
`GitHub <noreply@github.com>`. The portable provenance gate correctly rejected
that identity in runs 38413736646 and 38413736253. Preserve the historical
merge and failure; repair only by a forward signed local integration merge.

This AR owns the provenance recovery and post-merge evidence. It does not alter
AR-1850's TUI implementation or AR-1841's Coordinator adoption/state vendor.

- 2026-10-13T14:31:38+00:00: Durable provenance failure evidence supports a narrowly scoped forward
  identity recovery; no AR-1850 or AR-1841 overlap.

- 2026-10-13T14:32:14+00:00: Claimed by ar1856-protected-main-repair-luna.

- 2026-10-13T14:32:26+00:00: Claimed after role admission. Historical merge 9d2290dc and exact
  failures are preserved; proceeding with forward-only local-identity recovery, with no AR-1850 or
  AR-1841 scope.

- 2026-10-13T14:32:57+00:00: Bound worktree
  agent-systems-benchmark-ar-1856-pr631-protected-main-identity on branch
  repair/ar-1856-pr631-protected-main-identity.

- 2026-10-13T14:34:04+00:00: Recorded command exit 0; command argv SHA-256
  6c1e90766ef1400491ebc36eb757646e8c2b13e8895625db43d602a3f0cfd75d.

- 2026-10-13T14:34:34+00:00: Recorded command exit 0; command argv SHA-256
  a42fbd7bb226431de23b1c652a13261b414febb9e2e8c3a53db9e49fbc015e6b.

- 2026-10-13T14:34:57+00:00: Recorded command exit 0; command argv SHA-256
  8f0d1de4fb7d7e7bb26bf3c1033cf0072d42a665b22ef97e23934d857cb491c7.

- 2026-10-13T14:35:40+00:00: Recorded command exit 0; command argv SHA-256
  2b28a4ab52cc20bd97cbb368b1e3ad1d3827b6ab7475a04cf3bf4ff1767a243f.

- 2026-10-13T14:36:08+00:00: Recorded command exit 0; command argv SHA-256
  c5747f4860b679d178ba3457c6b769a74405293a56a443a20a394feb07f910ce.

- 2026-10-13T14:36:25+00:00: Recorded command exit 0; command argv SHA-256
  c5747f4860b679d178ba3457c6b769a74405293a56a443a20a394feb07f910ce.

- 2026-10-13T14:36:43+00:00: Recorded command exit 0; command argv SHA-256
  2917e99eb5e034e66c4e52c61efaf9a290fcc49cefbe10b67f1772fb264111ba.

- 2026-10-13T14:36:53+00:00: Recorded command exit 0; command argv SHA-256
  6e1ff8ea8f29b102b89a844ae5ecc7b247f93cb4617131aa8ece9f5f21f5ad4f.

- 2026-10-13T14:37:04+00:00: Recorded command exit 0; command argv SHA-256
  5b1845de177ce44a103fa709d698541791fd96722973462e94d32d94aa867f2d.

- 2026-10-13T14:37:15+00:00: Recorded command exit 0; command argv SHA-256
  fd36fb11d593ee274ffd4c446ca63106f1ae0a10a08a077743d03be553fa74b3.

- 2026-10-13T14:37:22+00:00: Recorded command exit 0; command argv SHA-256
  9a8759c922c021afdb88174a7e6f1a8ca51929ac43280ea9623ce06ac8627d17.

- 2026-10-13T14:37:37+00:00: Recorded command exit 0; command argv SHA-256
  2c6b731d137a574b91e38563ef713c969545c61842ef75e6f3723229ac11de29.

- 2026-10-13T14:37:49+00:00: Recorded command exit 0; command argv SHA-256
  7ce264a4a4446c3947c9756177380abcdec21e934aaae3f5518853fda1856a05.

- 2026-10-13T14:38:39+00:00: Recorded command exit 0; command argv SHA-256
  a90c3b9a066e382a192140ef6f72dc14f138d7c2cde8f13396e2ce2554b0a0fe.

- 2026-10-13T14:38:49+00:00: Recorded command exit 0; command argv SHA-256
  d116b76cd8992c358059b0762cb669304e717788919d061a44aeaae80f371ff8.

- 2026-10-13T14:38:52+00:00: Recorded command exit 0; command argv SHA-256
  a11078b0611baade8e38b4887ceafa3db0d448675a25bdd405d9ea6a99ab098c.

- 2026-10-13T14:40:06+00:00: Corrected initial synchronization failure: PR #632 was based on
  pre-merge d0e6a28 and was closed with evidence preserved. Created PR #633 from current protected
  main 9d2290dc with exact-tree signed-DCO empty recovery commit 6e3c57ca. Local repository policy
  passed; portable provenance check is green; remaining required CI is in progress. Canonical state
  main restored and doctor --live passes.

- 2026-10-13T14:52:03+00:00: Heartbeat by ar1856-protected-main-repair-luna.

- 2026-10-13T14:52:14+00:00: Recorded command exit 1; command argv SHA-256
  c265e7c8499763bc50a2bf285aeb1a27dbed1d4433c32e6dceda7184d4a97bdc.

- 2026-10-13T14:52:37+00:00: Recorded command exit 1; command argv SHA-256
  7f458ce7c0c5a04101c512ea701c0b922955724a369f5cedab233e8d8c3a426c.

- 2026-10-13T14:52:58+00:00: Recorded command exit 0; command argv SHA-256
  d6bd0955361c3a6d91991e30d83289490481a7d94dbe19b4f4aa661c918e1aa7.

- 2026-10-13T14:53:26+00:00: Recorded command exit 0; command argv SHA-256
  7f458ce7c0c5a04101c512ea701c0b922955724a369f5cedab233e8d8c3a426c.
