---
{
  "branch": "feature/ar-1769-human-diagnostic-completeness-ci",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-10T00:33:06+00:00",
  "depends_on": [
    "AR-1768"
  ],
  "id": "AR-1769",
  "next_action": "Add a required CI gate and executable negative journey proving every current and future public diagnostic is cataloged, specifically rendered, actionable, and privacy-safe.",
  "observed_branch": "feature/ar-1769-human-diagnostic-completeness-ci",
  "observed_dirty": 0,
  "observed_head": "5377317b7fbf04172e70a0ea000f305e5e07e23a",
  "owner": "codex-ar1769-diagnostic-ci-terra",
  "plan": "../plans/AR-1769-human-diagnostic-completeness-ci.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "hosted",
    "evidence_digest": "",
    "evidence_ref": "",
    "spec_ref": "specs/AR-1769.json",
    "spec_revision": 1,
    "status": "pending"
  },
  "spec_ref": "specs/AR-1769.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Make CI reject uncataloged, overly generic, context-free, unactionable, or privacy-unsafe human diagnostics.",
  "task_revision": 11,
  "title": "Human diagnostic completeness CI gate",
  "updated_at": "2026-10-09T22:34:40+00:00",
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


- 2026-10-09T22:31:14+00:00: AR-1768 is done and exact-main post-merge evidence is terminal green;
  dependency and declared worktree path verified.

- 2026-10-09T22:31:17+00:00: Claimed by codex-ar1769-diagnostic-ci-terra.

- 2026-10-09T22:31:44+00:00: Heartbeat by codex-ar1769-diagnostic-ci-terra.

- 2026-10-09T22:31:59+00:00: Recorded command exit 0; command argv SHA-256
  5345cd4b5f66285dc80cddfe59c0a95475263f9ff88d25d2639fce3c300aa4b9.

- 2026-10-09T22:32:28+00:00: Recorded command exit 0; command argv SHA-256
  a5453d68455ccee6a007da36aef01c94a721fd37d8c145e0baea3c3c32b88548.

- 2026-10-09T22:33:06+00:00: Heartbeat by codex-ar1769-diagnostic-ci-terra.

- 2026-10-09T22:33:50+00:00: Recorded command exit 0; command argv SHA-256
  1150d9011ed706e433cf3610bdffa0e9035490345efe325dffd1d86ef3c2bce4.

- 2026-10-09T22:34:15+00:00: Recorded command exit 1; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-10-09T22:34:40+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.
