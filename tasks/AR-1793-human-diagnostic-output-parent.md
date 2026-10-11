---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1784"
  ],
  "id": "AR-1793",
  "next_action": "Repair the legacy human diagnostic output-parent wording contract and add focused positive/negative coverage; do not publish AR-1784 until green.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1793-human-diagnostic-output-parent.md",
  "priority": "P1",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "hosted",
    "evidence_digest": "sha256:06bb28a9d3818edce148598c35724c10db65f03a8f02de91bb6255710d05c578",
    "evidence_ref": "github:martin-beck/agent-systems-benchmark/commit/24f1872cdb335c13331bffb67d0f73aa3f50430d/exact-main-workflows",
    "spec_ref": "specs/AR-1793.json",
    "spec_revision": 1,
    "status": "pass"
  },
  "spec_ref": "specs/AR-1793.json",
  "spec_revision": 1,
  "status": "done",
  "summary": "Repair the legacy human diagnostic output-parent wording contract exposed by the full ASB CLI suite.",
  "task_revision": 7,
  "title": "Repair human diagnostic output-parent contract",
  "updated_at": "2026-10-11T14:31:02+00:00",
  "worktree_key": ""
}
---

AR-1793 is a narrowly scoped dependent repair for the deterministic human diagnostic contract.

- 2026-10-11: Created from AR-1784 full-suite evidence.
- Baseline origin/main test passes; the AR-1784 head exposed the contract while changing preflight diagnostic callsites.
- Exact failing test: human tests error_presentations_name_cause_state_and_recovery_without_private_text.
- Observed output: No successful state change was reported. where the contract requires a state-change phrase.

- 2026-10-11T13:53:35+00:00: Promote dependency-safe AR-1793 now that AR-1784 is durably done.

- 2026-10-11T13:55:07+00:00: Claimed by codex-ar1793-diagnostic-repair-luna56.

- 2026-10-11T14:17:37+00:00: Recorded command exit 0; command argv SHA-256
  9cf29fc0352b0e72f5005a63316a870d5238e1cd0d27389342228a8370d75300.

- 2026-10-11T14:17:52+00:00: Recorded command exit 0; command argv SHA-256
  fd122d0d9f665e58ca7762edee2e1f8c4a41bb3b5805bf31246476fb77bcdabf.

- 2026-10-11T14:30:59+00:00: Signed protected merge 24f1872c; PR #582 exact-head checks and all 14
  exact-main workflows green; focused diagnostic contract passes.

- 2026-10-11T14:31:02+00:00: AR complete: PR #582 merged as signed local merge 24f1872c; exact-main
  signature/DCO/tree and all 14 required checks green.
