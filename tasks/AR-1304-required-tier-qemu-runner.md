---
{
  "branch": "feature/ar-1304-required-tier-qemu-runner",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1302"
  ],
  "id": "AR-1304",
  "next_action": "Integrate signed seed 99904f3c4 into a fresh immutable QEMU image, launch user@1000 and session bus, invoke 48da6f92b required launcher, and produce exact AR-1293 pr-publication attestation. Full-exhaustive remains gated.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1304.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "open",
  "summary": "Create a clean required-containment QEMU runner for formal publication evidence.",
  "task_revision": 49,
  "title": "Required-tier QEMU user-bus runner",
  "updated_at": "2026-09-17T15:00:19+00:00",
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

- 2026-09-17T14:54:00+00:00: Heartbeat by codex-ar1304-required-runner-20260917.

- 2026-09-17T14:54:03+00:00: Recorded command exit 0; command argv SHA-256
  22fa2122a4866c3bdd923877373b9ee30fa29e3f8633dd0004d8ac9c7ac79945.

- 2026-09-17T14:54:12+00:00: Recorded command exit 0; command argv SHA-256
  f321dd784b48b79bd8d2c316921d40566d7ea2361e52c7360f2bf43f1a516113.

- 2026-09-17T14:54:22+00:00: Recorded command exit 0; command argv SHA-256
  01b7773ff6a5df6f2c352a830ebb12c90e42979a04fa08480d075a11eb36676c.

- 2026-09-17T14:54:32+00:00: Recorded command exit 0; command argv SHA-256
  5e0edcd8b3b04405021922bdc288ed610bdda4054040da07957cdc2e68e56b34.

- 2026-09-17T14:54:43+00:00: Recorded command exit 0; command argv SHA-256
  00a5511ce90eb353147e969eefc258a75091a473261f7f712f0e107bd1d6b750.

- 2026-09-17T14:54:52+00:00: Recorded command exit 0; command argv SHA-256
  5aba1fb0770919f31197e32924bb8a998e447c45a85d30b5a5dc67161ede57a0.

- 2026-09-17T14:55:02+00:00: Recorded command exit 0; command argv SHA-256
  664562be5759b8357761bf178ca62e9608b895fafc7fb3c7e087f6544c09b630.

- 2026-09-17T14:55:57+00:00: Recorded command exit 0; command argv SHA-256
  d7fc4e94de6400889416bc7f714a8d1e3ed1b92f7b2193025433308cdc1604a6.

- 2026-09-17T14:56:36+00:00: Fresh QEMU run with native systemd seed succeeded through bus setup:
  guest started user@1000.service and asb-session-bus.service, with no network, and powered down
  cleanly. Serial evidence confirms the native unit started; however the seed still powers off
  immediately after bus socket setup and does not invoke the exact required launcher, so no
  pr-publication attestation exists. Next action: add the required launcher invocation after bus
  readiness, capture transient unit result and sanitized attestation, then rerun.

- 2026-09-17T14:56:51+00:00: Native guest bus repair is green; invoke exact required launcher and
  capture pr-publication attestation before shutdown

- 2026-09-17T14:56:54+00:00: Claimed by codex-ar1304-required-runner-20260917.

- 2026-09-17T14:57:22+00:00: Recorded command exit 0; command argv SHA-256
  22fa2122a4866c3bdd923877373b9ee30fa29e3f8633dd0004d8ac9c7ac79945.

- 2026-09-17T14:57:31+00:00: Recorded command exit 0; command argv SHA-256
  f321dd784b48b79bd8d2c316921d40566d7ea2361e52c7360f2bf43f1a516113.

- 2026-09-17T14:57:41+00:00: Recorded command exit 0; command argv SHA-256
  01b7773ff6a5df6f2c352a830ebb12c90e42979a04fa08480d075a11eb36676c.

- 2026-09-17T14:57:51+00:00: Recorded command exit 0; command argv SHA-256
  3d8121aeb86ed3036367c7de4244feecb453fd6d2f9d7b8538661d65f7357445.

- 2026-09-17T14:58:05+00:00: Recorded command exit 0; command argv SHA-256
  98f116ad3b92f1761db609ff8420227ec825cf99ee2df7c3b3923de701253f60.

- 2026-09-17T14:58:15+00:00: Recorded command exit 0; command argv SHA-256
  2c01cf2282815eb186e004c87a23d5f76c2f8d98e5068b3760537990901a46b3.

- 2026-09-17T14:58:25+00:00: Recorded command exit 0; command argv SHA-256
  73356b47ffe196c17e9552cc7029a5fab5db79967d0be4f2b068d96148974022.

- 2026-09-17T14:59:21+00:00: Recorded command exit 0; command argv SHA-256
  a4162425616b55799b69815db7beca64ca5fb1943cbe813ed8565179071abe12.

- 2026-09-17T15:00:01+00:00: Fresh native systemd seed run completed with bus service started, but
  required transient probe failed closed: cloud-init serial reports Failed to start transient
  service unit: Transport endpoint is not connected. The guest powered off cleanly; no required
  pr-publication attestation was produced. This confirms the remaining defect is user-manager/D-Bus
  transport readiness after asb-session-bus.service, not missing bus socket. Next action: start a
  system-managed user manager/session bus using the image-supported mechanism and verify systemd-run
  --user transient success before running TLC; preserve all six limits.

- 2026-09-17T15:00:19+00:00: Native user bus socket is insufficient; use the image-supported
  system-managed user bus and prove transient success before TLC
