---
{
  "branch": "feature/ar-1770-descriptor-safe-directory-race-hardening",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-09T22:22:30+00:00",
  "depends_on": [
    "AR-1767"
  ],
  "id": "AR-1770",
  "next_action": "Implement descriptor-relative or equivalent fail-closed directory and atomic publication paths, then complete the hostile filesystem and stream matrix.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "codex-ar1770-descriptor-safe-races",
  "plan": "../plans/AR-1770-descriptor-safe-directory-race-hardening.md",
  "priority": "P1",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "property-or-fuzz",
    "evidence_digest": "",
    "evidence_ref": "",
    "spec_ref": "specs/AR-1770.json",
    "spec_revision": 1,
    "status": "pending"
  },
  "spec_ref": "specs/AR-1770.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Close remaining directory and atomic-publication replacement races and complete the AR-1767 acceptance matrix.",
  "task_revision": 3,
  "title": "Descriptor-safe directory race hardening and acceptance matrix",
  "updated_at": "2026-10-09T19:22:30+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1770-descriptor-safe-directory-race-hardening"
}
---

Harden the AR-1767 directory preparation and output publication paths against
replacement between validation and effect. Use descriptor-relative or an
equivalent fail-closed design for every command-owned directory ancestor and
for `write_atomic_private` and `publish_recording_campaign`; never follow an
attacker-replaced symlink or publish through an unvalidated ancestor. Preserve
private modes, fsync/atomicity, transaction-owned cleanup, and existing JSON
and diagnostic contracts.

Complete the missing acceptance evidence: deterministic replacement-race and
concurrent-reuse tests; dry-run no-mutation tests; permission/read-only and
rollback tests; path-specific error and human-notice tests for setup/config,
project, tool, plan, run/sweep, report, record/campaign, easy lifecycle, and
TUI routes; and machine-stream privacy checks. Record any platform-specific
implementation boundary explicitly and keep the product offline after install.

- 2026-10-09T19:22:21+00:00: AR-1767 is released done with exact merge and all post-merge gates;
  promote the descriptor-safe race and acceptance-matrix successor.

- 2026-10-09T19:22:30+00:00: Claimed by codex-ar1770-descriptor-safe-races.
