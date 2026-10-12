---
{
  "branch": "feature/ar-1773-universal-command-step-instrumentation",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-12T08:20:04+00:00",
  "depends_on": [
    "AR-1769",
    "AR-1772"
  ],
  "id": "AR-1773",
  "next_action": "Inventory all public command routes and existing human status/progress writes, then implement shared-reporter instrumentation with mode/outcome matrix.",
  "observed_branch": "feature/ar-1773-universal-command-step-instrumentation",
  "observed_dirty": 3,
  "observed_head": "9c5e557195df34675e2f5427e6ec3dff3d433254",
  "owner": "ar1772-progress-reporter-luna56",
  "plan": "../plans/AR-1773-universal-command-step-instrumentation.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "integration-test",
    "evidence_digest": "",
    "evidence_ref": "",
    "spec_ref": "specs/AR-1773.json",
    "spec_revision": 1,
    "status": "pending"
  },
  "spec_ref": "specs/AR-1773.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Dependency-safe AR-1773 claimed; clean isolated worktree created at current main 9c5e5571.",
  "task_revision": 9,
  "title": "Universal command step instrumentation",
  "updated_at": "2026-10-12T06:23:22+00:00",
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

- 2026-10-12T06:20:03+00:00: Dependencies AR-1769 and AR-1772 are complete and released; promote
  AR-1773 to open for implementation.

- 2026-10-12T06:20:04+00:00: Claimed by ar1772-progress-reporter-luna56.

- 2026-10-12T06:20:24+00:00: Recorded command exit 0; command argv SHA-256
  9cb963e1051a08fb292e41e233b68dd8e4e1d88e3773f2fa76bda9e3e21054f9.

- 2026-10-12T06:20:47+00:00: AR-1769 and AR-1772 are complete. Promoted and claimed AR-1773 under
  owner ar1772-progress-reporter-luna56. Created clean worktree
  /srv/data/projects/agent-systems-benchmark-ar-1773-universal-command-step-instrumentation on
  branch feature/ar-1773-universal-command-step-instrumentation at origin/main 9c5e5571. Next action
  is authoritative route inventory before implementation.

- 2026-10-12T06:22:31+00:00: Recorded command exit 0; command argv SHA-256
  2a8f194e6adddd75d45f4e106e0f79ed41a2c4749e10429101d9bbf524666fe0.

- 2026-10-12T06:23:13+00:00: Recorded command exit 101; command argv SHA-256
  17d0d0a0f520aeffcd369fdcda77b67a3ac6e38e4dd4288dc07237a40369e7ed.

- 2026-10-12T06:23:22+00:00: Recorded command exit 0; command argv SHA-256
  2a8f194e6adddd75d45f4e106e0f79ed41a2c4749e10429101d9bbf524666fe0.
