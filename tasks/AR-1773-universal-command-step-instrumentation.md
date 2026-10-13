---
{
  "branch": "feature/ar-1773-universal-command-step-instrumentation",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-13T21:43:48+00:00",
  "depends_on": [
    "AR-1769",
    "AR-1772"
  ],
  "execution_envelope": {
    "command_classes": {
      "read": {
        "allowed": true,
        "timeout_seconds": 120
      },
      "test": {
        "allowed": true,
        "timeout_seconds": 3600
      }
    },
    "envelope_id": "AR-1773-e1",
    "envelope_revision": 1,
    "evidence": [
      {
        "class": "contract-test",
        "id": "contract-test",
        "required": true
      },
      {
        "class": "mechanical",
        "id": "mechanical-check",
        "required": true
      }
    ],
    "non_goals": [
      "No product source changes; implementation is already an ancestor of current main."
    ],
    "outputs": [
      {
        "description": "Run bounded exact-head tests and mechanical instrumentation checks.",
        "id": "test-evidence"
      }
    ],
    "path_scope": {
      "read": [
        "crates/asb-cli",
        "docs",
        "Cargo.toml",
        "Cargo.lock"
      ],
      "write": [
        "quality"
      ]
    },
    "schema_version": 1,
    "spec_ref": "specs/AR-1773.json",
    "spec_revision": 1,
    "stop_conditions": [
      {
        "id": "unexpected-drift",
        "kind": "pause"
      }
    ],
    "task": "AR-1773",
    "task_revision": 5
  },
  "execution_envelope_digest": "sha256:36af7d046d9ef15d3ed21b798ab488b01fd26a5d9ad86cc3a2af1f75907c69cb",
  "execution_envelope_ref": "quality/AR-1773-execution-envelope.json",
  "execution_envelope_revision": 1,
  "execution_envelope_task_revision": 5,
  "execution_result": {
    "argv_digest": "741025f82ae045889c1f17411456cfd7f22843be12678fead0dcda63f198a4bd",
    "classification": "EXIT",
    "envelope_digest": "sha256:36af7d046d9ef15d3ed21b798ab488b01fd26a5d9ad86cc3a2af1f75907c69cb",
    "execution_id": "1394e95be02e43f48a0a05d87fe7348e",
    "owner": "asb_ar1773_instrument_luna",
    "recorded_at": "2026-10-13T19:43:09+00:00",
    "returncode": 1
  },
  "id": "AR-1773",
  "next_action": "Instrument every eligible public command operation through the shared reporter after the diagnostic gate and reporter are accepted.",
  "observed_branch": "feature/ar-1773-universal-command-step-instrumentation",
  "observed_dirty": 0,
  "observed_head": "f78a1006202d6fb62df4aa3d5efd0a42381b713c",
  "owner": "asb_ar1773_instrument_luna",
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
  "summary": "Route every eligible public ASB command step through the shared status/progress reporter with real work updates.",
  "task_revision": 16,
  "title": "Universal command step instrumentation",
  "updated_at": "2026-10-13T19:43:48+00:00",
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

- 2026-10-13T19:40:57+00:00: Dependencies AR-1769 and AR-1772 are done; promote dependency-ready
  implementation.

- 2026-10-13T19:41:00+00:00: Claimed by asb_ar1773_instrument_luna.

- 2026-10-13T19:41:50+00:00: Heartbeat by asb_ar1773_instrument_luna.

- 2026-10-13T19:42:32+00:00: Bound execution envelope quality/AR-1773-execution-envelope.json
  revision 1.

- 2026-10-13T19:42:37+00:00: Reserved bound execution e9219b51ac044cd68e444c9e0c5e830a.

- 2026-10-13T19:42:39+00:00: Recorded execution result e9219b51ac044cd68e444c9e0c5e830a.

- 2026-10-13T19:42:42+00:00: Recorded command exit 1; command argv SHA-256
  22fc19d872be75a975891ff0abd53f1c305974a409b50c49c5df5d842d033e81.

- 2026-10-13T19:42:51+00:00: Reserved bound execution ac0bd99bce0941eeac98a1cc81969b40.

- 2026-10-13T19:42:54+00:00: Recorded execution result ac0bd99bce0941eeac98a1cc81969b40.

- 2026-10-13T19:42:57+00:00: Recorded command exit 1; command argv SHA-256
  c69ae36c96fb966314af025bc32cf966f352c7e6191e0e9950110061d6af931e.

- 2026-10-13T19:43:07+00:00: Reserved bound execution 1394e95be02e43f48a0a05d87fe7348e.

- 2026-10-13T19:43:10+00:00: Recorded execution result 1394e95be02e43f48a0a05d87fe7348e.

- 2026-10-13T19:43:12+00:00: Recorded command exit 1; command argv SHA-256
  741025f82ae045889c1f17411456cfd7f22843be12678fead0dcda63f198a4bd.

- 2026-10-13T19:43:48+00:00: Heartbeat by asb_ar1773_instrument_luna.
