---
{
  "branch": "feature/ar-1480-runtime-control-cli-composition",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-27T13:20:14+00:00",
  "depends_on": [
    "AR-1473",
    "AR-1472"
  ],
  "id": "AR-1480",
  "next_action": "Rerun full workspace/docs/privacy gates after provenance refresh, then independent review and signed commit.",
  "observed_branch": "feature/ar-1480-runtime-control-cli-composition",
  "observed_dirty": 3,
  "observed_head": "59323f41ed2d10a952a1276107459260ebdf409a",
  "owner": "ar1332-record-replay-luna56",
  "plan": "../plans/AR-1480-runtime-control-cli-composition.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Compose authenticated runtime enrollment into opaque normal CLI run and sweep dispatch.",
  "task_revision": 24,
  "title": "Runtime-control CLI composition",
  "updated_at": "2026-09-27T11:29:29+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1480-runtime-control-cli-composition"
}
---

Successor to the stale AR-1374/1375 adapter chain. AR-1473 and AR-1472 are
the only implementation dependencies; live provider reachability is optional
and never gates local qualification.

- The composition must preserve opaque authority and fail closed on missing,
  stale, revoked, replayed, mismatched, or caller-supplied inputs.
- Qualification uses deterministic local/mock/replay evidence only.

- 2026-09-27T11:17:28+00:00: AR-1473 and AR-1472 are durably done; promote dependency-safe CLI
  composition successor with no circular AR-1374/1375 edge.

- 2026-09-27T11:17:30+00:00: Claimed by ar1332-record-replay-luna56.

- 2026-09-27T11:17:41+00:00: Recorded command exit 0; command argv SHA-256
  31ef8dba69cadb96f0eab7a54672aa35e58192283fa68f6c82d04e7f76edc9be.

- 2026-09-27T11:18:08+00:00: Recorded command exit 0; command argv SHA-256
  e5e483509179e2d1e0604ee0f63271ced6232cbfb60eb6ccdf9fe0c6ad23a76a.

- 2026-09-27T11:20:14+00:00: Heartbeat by ar1332-record-replay-luna56.

- 2026-09-27T11:20:31+00:00: After complete AR-1480 plan/docs review and current-main audit,
  implementation adds RuntimeControlDispatchSource and run_with_runtime_control_source in asb-cli.
  The seam resolves only an opaque LiveProviderRuntimeDispatchSource from runtime/control and fails
  closed before CLI effects when unavailable; docs state ordinary process run/sweep cannot construct
  authority. Added hostile unavailable-source test; no asb-tui/live provider.

- 2026-09-27T11:21:04+00:00: Recorded command exit 0; command argv SHA-256
  b2f3fb06dee43d704705616108ddb13e7dcca021834cb50f5a41e895d2b16eff.

- 2026-09-27T11:21:37+00:00: Recorded command exit 0; command argv SHA-256
  c9a2916a927594a512151f14eab59803113f12061a17b617a103789a4ff6a824.

- 2026-09-27T11:22:04+00:00: Recorded command exit 0; command argv SHA-256
  b7a391741901b8aade6d43c13786c703d443b46d94efdaa27c0f02fa2d51a198.

- 2026-09-27T11:22:34+00:00: Recorded command exit 0; command argv SHA-256
  c44ed960f90bd281b4395dd1445881d59d09fa681f7e317ba9f0254abb8780d1.

- 2026-09-27T11:24:25+00:00: Implementation checkpoint: AR-1480 adds RuntimeControlDispatchSource
  and run_with_runtime_control_source to asb-cli. The runtime/control seam resolves only an opaque
  LiveProviderRuntimeDispatchSource and returns bounded Unavailable before CLI effects; existing
  runtime-owned source remains private. Added hostile unavailable-source test and docs/workflow
  boundary note. After refreshing clean worktree to protected main 59323f41, focused runtime source
  and CLI fail-closed tests pass. Full workspace gates are currently running under handoffctl.

- 2026-09-27T11:24:40+00:00: Recorded command exit 101; command argv SHA-256
  e1c351c46494fcbac29ac31b75b8949233e665b6ae0d88686ef9580974dee8dc.

- 2026-09-27T11:25:35+00:00: Recorded command exit 101; command argv SHA-256
  d6ece9b50bad2e5bcf4979b15480d66d38cc94e188f9c1155f51ca9f32af5728.

- 2026-09-27T11:26:08+00:00: Recorded command exit 0; command argv SHA-256
  a7f68e4c0b3fa94122973819ed7485fa9cfc8473bfd3fa2043727b74f6172a40.

- 2026-09-27T11:26:30+00:00: Recorded command exit 0; command argv SHA-256
  19d47c10c4c4e824f5a4b03933e6b89ad4378dcfbd931f0f6da06e7d709b71a8.

- 2026-09-27T11:26:58+00:00: Full workspace test initially exited 101 on existing provenance
  contract test crates/asb-cli/tests/workflow_transcript.rs: expected cli_source_sha256 4696... but
  current lib hash was f5ee7317... due this intentional CLI change. No behavioral failure. Updated
  docs/examples/asb-cli-workflow-v1.provenance.json through handoffctl product run to the exact
  current hash; focused provenance test now passes 1/1. Preserve this deterministic
  provenance-refresh evidence before full rerun.

- 2026-09-27T11:28:37+00:00: Recorded command exit 1; command argv SHA-256
  8aec24a200be13f45450c587096d341e2afdfa97823b21330001e5162e0de7c2.

- 2026-09-27T11:29:29+00:00: Recorded command exit 0; command argv SHA-256
  e6f9d6dc8581eb1ebfccd6a34944eb45eca27527ddac007d7ae2bf727be4d15f.
