---
{
  "branch": "feature/ar-1773-universal-command-step-instrumentation",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1769", "AR-1772"],
  "id": "AR-1773",
  "next_action": "Instrument every eligible public command operation through the shared reporter after the diagnostic gate and reporter are accepted.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1773-universal-command-step-instrumentation.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {"evidence_class": "integration-test", "evidence_digest": "", "evidence_ref": "", "spec_ref": "specs/AR-1773.json", "spec_revision": 1, "status": "pending"},
  "spec_ref": "specs/AR-1773.json",
  "spec_revision": 1,
  "status": "planned",
  "summary": "Route every eligible public ASB command step through the shared status/progress reporter with real work updates.",
  "task_revision": 1,
  "title": "Universal command step instrumentation",
  "updated_at": "2026-10-09T21:29:29+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1773-universal-command-step-instrumentation"
}
---

Replace every ad-hoc human status/progress write with the AR-1772 reporter and
instrument every eligible important command step. Cover setup/config/auth,
project initialization, tool discovery/install, catalogs and model enumeration,
plan generation, local and live run/sweep lifecycle, report/compare, recording
and replay, easy workflows, control/serve commands, and ASB-routed TUI lifecycle
commands. Include successful, failed, warning, partial, cancelled, and
reconciliation outcomes. Each call site must send actual operation-specific work
information—such as discovered/installed items, selected models, workload units,
run phases, report inputs, transfers, or concrete substeps—so the helper can
produce an honest overall indication and estimate.

Do not add fake counters to make a bar look active. Where a backend exposes no
bounded total, declare it indeterminate and continue providing relevant elapsed
and state information. Collapse only non-user-meaningful internal operations;
every meaningful external effect or wait gets a concise separate step. Route
parse, validation, and immediate failures through terminal status output without
creating a progress bar. All integrations must preserve JSON silence and quiet
silence, existing prompts, TUI ownership, diagnostic specificity, privacy, and
non-TTY compatibility.
