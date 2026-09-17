---
{
  "branch": "feature/ar-1304-required-tier-qemu-runner",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-17T15:15:02+00:00",
  "depends_on": [
    "AR-1302"
  ],
  "id": "AR-1304",
  "next_action": "Promote after review; build a fresh QEMU guest with a verified user D-Bus bus and run required pr-publication for the exact AR-1293 candidate.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "codex-ar1304-required-runner-20260917",
  "plan": "../plans/AR-1304.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Create a clean required-containment QEMU runner for formal publication evidence.",
  "task_revision": 8,
  "title": "Required-tier QEMU user-bus runner",
  "updated_at": "2026-09-17T14:46:43+00:00",
  "worktree_key": "agent-systems-benchmark-state-ar-1304-required-tier-qemu-runner"
}
---

## AR-1304

AR-1293 has a green portable-smoke result, but the required `pr-publication`
tier cannot yet attest because the guest `systemd-run --user` transient launch
returns `No medium` even when the user manager and bus socket appear healthy.
This AR owns only the clean guest launcher/runner needed to repair that path.
It must not weaken required cgroup containment, reuse stale images, expose raw
logs, or claim full-exhaustive evidence before required attestation is green.

- 2026-09-17T14:45:00+00:00: Created after AR-1293 required-tier diagnosis;
  AR-1302 portable runner remains qualified and unchanged.

- 2026-09-17T14:44:47+00:00: AR-1302 is done; required-tier runner is dependency-ready

- 2026-09-17T14:45:02+00:00: Claimed by codex-ar1304-required-runner-20260917.

- 2026-09-17T14:45:28+00:00: Recorded command exit 0; command argv SHA-256
  9ff9d5c2fd484fa439123f0a7757c378fef13283175e8ab5772ce1a769850aff.

- 2026-09-17T14:46:02+00:00: Recorded command exit 0; command argv SHA-256
  86ea2a50a415ff6acc22140f737f8bb1965c59812ef77dfc9ea2e1b9719957fb.

- 2026-09-17T14:46:12+00:00: Recorded command exit 0; command argv SHA-256
  2f30d45c4b03f1322028a5dbfe15cc7b478fe26d0195ef20e40832c111d366a8.

- 2026-09-17T14:46:21+00:00: Recorded command exit 1; command argv SHA-256
  c94dca6c50887073649e8eda3430a938346fb79f51d09d59f9696841a12d77d8.

- 2026-09-17T14:46:43+00:00: Recorded command exit 0; command argv SHA-256
  c94dca6c50887073649e8eda3430a938346fb79f51d09d59f9696841a12d77d8.
