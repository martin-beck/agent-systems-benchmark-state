---
{
  "branch": "feature/ar-1769-human-diagnostic-completeness-ci",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1768"],
  "id": "AR-1769",
  "next_action": "Add a required CI gate and executable negative journey proving every current and future public diagnostic is cataloged, specifically rendered, actionable, and privacy-safe.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1769-human-diagnostic-completeness-ci.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {"evidence_class": "hosted", "evidence_digest": "", "evidence_ref": "", "spec_ref": "specs/AR-1769.json", "spec_revision": 1, "status": "pending"},
  "spec_ref": "specs/AR-1769.json",
  "spec_revision": 1,
  "status": "planned",
  "summary": "Make CI reject uncataloged, overly generic, context-free, unactionable, or privacy-unsafe human diagnostics.",
  "task_revision": 1,
  "title": "Human diagnostic completeness CI gate",
  "updated_at": "2026-10-09T17:21:34+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1769-human-diagnostic-completeness-ci"
}
---

Add a required repository gate that keeps the AR-1766 and AR-1768 guarantees
true as ASB grows. A new command, error source, backend mapping, filesystem
operation, partial result, or warning must fail CI until it has a fine-grained
catalog identity, safe context mapping, explicit human presentation, meaningful
recovery, and machine/privacy compatibility tests.

The gate must not rely only on snapshots or a hand-maintained list that can drift.
Use closed Rust types and the authoritative public command inventory to generate
or mechanically validate coverage. Add controlled defects proving rejection of
an uncataloged producer, broad known-cause collapse, context-free path error,
generic `failed/unavailable/invalid` explanation, warning without consequence,
unsafe suggested command, and secret/private-path leakage.

Run an executable negative journey covering setup/configuration, project/tool and
catalog paths, plan/run/sweep/report, recording/replay, provider/network failures,
ASB-routed TUI lifecycle diagnostics, directory creation, permissions/topology,
timeouts/cancellation, partial results, and warning-only development behavior.

