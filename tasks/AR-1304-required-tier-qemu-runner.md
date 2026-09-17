---
{
  "branch": "feature/ar-1304-required-tier-qemu-runner",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-17T15:23:28+00:00",
  "depends_on": [
    "AR-1302"
  ],
  "id": "AR-1304",
  "next_action": "Integrate signed seed 99904f3c4 into a fresh immutable QEMU image, launch user@1000 and session bus, invoke 48da6f92b required launcher, and produce exact AR-1293 pr-publication attestation. Full-exhaustive remains gated.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "codex-ar1304-required-runner-20260917",
  "plan": "../plans/AR-1304.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Create a clean required-containment QEMU runner for formal publication evidence.",
  "task_revision": 27,
  "title": "Required-tier QEMU user-bus runner",
  "updated_at": "2026-09-17T14:53:28+00:00",
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

- 2026-09-17T14:46:52+00:00: Recorded command exit 0; command argv SHA-256
  6baeef2d4711a7d44dd4d5222b083db8b8c1026db014edb1ba62fecd6d09996d.

- 2026-09-17T14:47:02+00:00: Recorded command exit 0; command argv SHA-256
  4cc91cb7f2aa23e229d8127eb337c1557cf921f6f19e4f66276414f23cedc6bb.

- 2026-09-17T14:47:25+00:00: Implemented signed/DCO required user-bus launcher contract at
  48da6f92b. It fails closed on any bus other than /run/user/1000/bus and emits systemd-run --user
  with MemoryMax=3G, MemorySwapMax=3G, CPUQuota=200%, TasksMax=64, KillMode=control-group,
  RuntimeMaxSec=1800. Focused tests 2/2 and Ruff pass. Guest integration and required pr-publication
  attestation remain outstanding; full-exhaustive is still gated.

- 2026-09-17T14:47:46+00:00: Heartbeat by codex-ar1304-required-runner-20260917.

- 2026-09-17T14:47:56+00:00: Required launcher contract 48da6f92b is signed and focused-green. A
  candidate data image ar1293-39c8933f5-data.raw exists, but no reviewed fresh QEMU seed integrates
  the launcher with a deterministic user D-Bus before cloud-init; existing seed is
  portable/preflight-only. No required pr-publication attestation or negative guest-bus evidence was
  produced. Next action: create a fresh seed/service that starts user@1000 and a session bus, run
  the exact required launcher with all six resource properties, and capture sanitized bus/transient
  results before retry.

- 2026-09-17T14:48:17+00:00: Launcher contract is green; resume to integrate deterministic guest
  user bus and produce required attestation

- 2026-09-17T14:48:20+00:00: Claimed by codex-ar1304-required-runner-20260917.

- 2026-09-17T14:48:52+00:00: Recorded command exit 0; command argv SHA-256
  9d21774da9bf6357a7f1a021076f0f52abe1e34a4be35c0a531668986e6180dd.

- 2026-09-17T14:49:04+00:00: Recorded command exit 0; command argv SHA-256
  dfce5788b196edea6eabb33e4fbc94777e11b69d8fcf94beca2ced159134d6f7.

- 2026-09-17T14:49:17+00:00: Recorded command exit 0; command argv SHA-256
  8d06d641d5d965b9b28f704dfd7f213dc6928ddb22be7fbf06cb23d4685b5f6e.

- 2026-09-17T14:49:31+00:00: Recorded command exit 0; command argv SHA-256
  a24edafe9bdcb635aeb063ea9238c0d7593ceb936055f219960736c3bd73f80e.

- 2026-09-17T14:49:41+00:00: Recorded command exit 1; command argv SHA-256
  a24edafe9bdcb635aeb063ea9238c0d7593ceb936055f219960736c3bd73f80e.

- 2026-09-17T14:50:09+00:00: Added signed/DCO required guest seed 99904f3c4: masks only wait-online,
  starts user@1000, starts a non-forking D-Bus session at /run/user/1000/bus, and tests socket
  readiness without networking. Seed tests plus required launcher tests pass and Ruff is green.
  Fresh guest integration and required attestation remain outstanding.

- 2026-09-17T14:50:34+00:00: Recorded command exit 0; command argv SHA-256
  cd44ca7677ac3faaf4cadef5dbcf257bbd264d9cafcf732a79ef98b1f89bed95.

- 2026-09-17T14:50:44+00:00: Recorded command exit 0; command argv SHA-256
  d03552d25d31e0f59af4cd6dda05bc8bd8a5515af627e8783f2e84ead8f11439.

- 2026-09-17T14:50:53+00:00: Recorded command exit 0; command argv SHA-256
  5fa3be599c71d5c1571eb26658793efcbcbf0c8ac5e8396a1deb07c634de677a.

- 2026-09-17T14:53:07+00:00: Fresh QEMU integration attempted with signed seed 99904f3c4, receipt
  root/data, -net none, bounded 120s. Guest boot masked wait-online, but bootcmd loginctl failed
  with Failed to connect to bus: No such file or directory before user@1000/session bus startup; no
  bus-ready marker and no required pr-publication attestation. Next action: use a systemd-native
  guest unit ordered after user@1000.service to start the session bus, rather than invoking loginctl
  from cloud-init bootcmd; then rerun required launcher with all six resource properties.

- 2026-09-17T14:53:25+00:00: Replace cloud-init loginctl bootstrap with a systemd-native guest unit
  ordered after user@1000; retry required attestation

- 2026-09-17T14:53:28+00:00: Claimed by codex-ar1304-required-runner-20260917.
