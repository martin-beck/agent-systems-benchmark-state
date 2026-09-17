---
{
  "branch": "feature/ar-1286-supervised-replay-lifecycle",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-17T04:28:21+00:00",
  "depends_on": [
    "AR-1282",
    "AR-1285",
    "AR-1237",
    "AR-1238",
    "AR-1239"
  ],
  "id": "AR-1286",
  "next_action": "Signed clean head 7830724 wires runtime-owned backend/context consumption into CLI replay; cargo test -p asb-runtime and -p asb-cli --locked pass (runtime 50 unit, 3 binary, 8 process, 11 sandbox, 16 scheduler, 2 doctests; CLI 71 unit, 12 capability, 3 e2e, 4 guides, 2 setup, 4 TUI, 3 workflow). Next add qualified positive child plus cancellation/timeout/crash/restart/cleanup and egress fixtures.",
  "observed_branch": "feature/ar-1286-supervised-replay-lifecycle",
  "observed_dirty": 1,
  "observed_head": "78307246832bf0f316070a91fdaa7767f7e29e09",
  "owner": "asb_ar1286_supervised_replay_lifecycle",
  "plan": "../plans/AR-1286.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Execute strict-replay cassettes through the runtime-owned supervised lifecycle.",
  "task_revision": 31,
  "title": "Supervised strict-replay cassette lifecycle",
  "updated_at": "2026-09-17T02:28:24+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1286-supervised-replay-lifecycle"
}
---

## AR-1286

Implement the next ASB-only lifecycle boundary after the merged AR-1282 transport and AR-1285
launch factory. Preserve all fail-closed authority, egress, cleanup, and no-fallback requirements;
do not touch or claim asb-tui behavior.

- Created as the dependency-safe successor for the supervised cassette lifecycle after AR-1282 and
  AR-1285 completed. Earlier blocked replay lifecycle records remain historical evidence and are
  not implementation inputs.

- 2026-09-17T02:19:11+00:00: Dependencies AR-1282, AR-1285, AR-1237, AR-1238, and AR-1239 are done;
  promote this ASB-only lifecycle successor.

- 2026-09-17T02:19:17+00:00: Claimed by asb_ar1286_supervised_replay_lifecycle.

- 2026-09-17T02:20:12+00:00: Setup checkpoint: declared isolated worktree is clean at exact
  protected main 2fd9055. Initial handoffctl bootstrap from canonical checkout was rejected because
  invocation worktree did not yet match the declared AR worktree; created the declared worktree from
  origin/main, and all subsequent product commands will run there through handoffctl.

- 2026-09-17T02:20:47+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-17T02:21:06+00:00: Recorded command exit 0; command argv SHA-256
  920d4dc14984153ac58c98ec2c07595757e3a94ef557766798bdb312328d8ce3.

- 2026-09-17T02:21:20+00:00: Recorded command exit 0; command argv SHA-256
  b56a340314485ff8f50e5f6d74979c76e51d72077e6eaa02dd388001d918fb1c.

- 2026-09-17T02:21:41+00:00: Implementation checkpoint: 08bb157 is SSH-signed+DCO and clean. Focused
  cargo test -p asb-runtime --locked passed 50 tests, 3 binary tests, 8 process-boundary, 11
  sandbox-boundary, 16 scheduler-boundary, and 2 doctests. No asb-tui paths touched.

- 2026-09-17T02:22:49+00:00: Recorded command exit 1; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-17T02:23:03+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-17T02:23:21+00:00: Recorded command exit 0; command argv SHA-256
  920d4dc14984153ac58c98ec2c07595757e3a94ef557766798bdb312328d8ce3.

- 2026-09-17T02:23:34+00:00: Recorded command exit 0; command argv SHA-256
  2b10510dfbe93741e7b318fe5404f5634a8f4e4ab2c63f35f91a00054fec6c6d.

- 2026-09-17T02:23:57+00:00: Diagnosis: first fmt-check command exited 1 only because launch_factory
  import ordering differed from rustfmt; cargo fmt --all corrected it. The subsequent locked
  asb-runtime suite passed all 50 unit, 3 binary, 8 process-boundary, 11 sandbox-boundary, 16
  scheduler-boundary, and 2 doctest checks. Signed+DCO product head eef6894 is clean.

- 2026-09-17T02:24:17+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-17T02:24:50+00:00: Recorded command exit 101; command argv SHA-256
  0945cdc35367dc565965745b158b093f3f011fc34899e6dc8b459de68f74904a.

- 2026-09-17T02:25:20+00:00: Recorded command exit 0; command argv SHA-256
  5e5ddb8a6186d3a2e0d3a01cb02a43089ede01c40d8521c7bdfb92d537530482.

- 2026-09-17T02:25:35+00:00: Recorded command exit 0; command argv SHA-256
  a6be2af828c99876502ac04b910cfcb245d6d2591532fa282a36ad820c017371.

- 2026-09-17T02:26:00+00:00: Checkpoint 7830724: ReplayLaunchFactory::issue_with_backend retains the
  runtime-owned SandboxBackend; ReplayLaunchContext::spawn transfers validated input+lease to
  SandboxBackend::spawn_launch; CLI replay now waits for a supervised child and rejects
  nonzero/failure. Focused workflow provenance test passes. Prior focused package command had one
  expected provenance-drift failure because CLI source changed; refreshed only the checked-in exact
  source digest and reran 1/1 success. Signed+DCO, clean tree, no asb-tui changes.

- 2026-09-17T02:26:26+00:00: Recorded command exit 0; command argv SHA-256
  858ad2e4956c1e7e1b8767ba4e1a064f54e12b5916bd2360c4e2ceb50d0b06a0.

- 2026-09-17T02:26:46+00:00: Recorded command exit 0; command argv SHA-256
  2ddd222d5ab3dbbc5824e8367ff0d1151a6168041a569b52fb97c11e3c8515c1.

- 2026-09-17T02:27:10+00:00: Full focused package evidence is green at 7830724; sandbox boundary
  11/11 and CLI workflow transcript 3/3 pass. The earlier CLI package failure was a deterministic
  provenance hash mismatch caused by the intentional lib.rs edit; exact source digest was updated in
  docs/examples/asb-cli-workflow-v1.provenance.json and rerun passed. Worktree clean, signed+DCO, no
  asb-tui changes.

- 2026-09-17T02:28:21+00:00: Heartbeat by asb_ar1286_supervised_replay_lifecycle.

- 2026-09-17T02:28:24+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.
