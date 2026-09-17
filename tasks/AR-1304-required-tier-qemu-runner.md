---
{
  "branch": "feature/ar-1304-required-tier-qemu-runner",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-17T16:26:16+00:00",
  "depends_on": [
    "AR-1302"
  ],
  "id": "AR-1304",
  "next_action": "Independent exact-head review of signed 920356c60, 9111d2f2a, and 8a815690c; then hand required pr-publication evidence to AR-1293. Do not run full-exhaustive until coordinator accepts the attestation.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "codex-ar1304-required-runner-20260917",
  "plan": "../plans/AR-1304.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Create a clean required-containment QEMU runner for formal publication evidence.",
  "task_revision": 156,
  "title": "Required-tier QEMU user-bus runner",
  "updated_at": "2026-09-17T15:58:32+00:00",
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

- 2026-09-17T15:00:22+00:00: Claimed by codex-ar1304-required-runner-20260917.

- 2026-09-17T15:00:39+00:00: Heartbeat by codex-ar1304-required-runner-20260917.

- 2026-09-17T15:00:43+00:00: Required-tier investigation confirms standalone dbus-daemon socket is
  insufficient: native asb-session-bus.service starts and /run/user/1000/bus exists, but systemd-run
  --user returns Transport endpoint is not connected. The correct next repair must use the
  image-supported system-managed user@1000 manager/session bus ordering and environment; no wrapper,
  portable fallback, or gate weakening is acceptable. No required attestation exists.

- 2026-09-17T15:01:08+00:00: Continue active repair; do not release before implementing and testing
  system-managed user@1000 ordering

- 2026-09-17T15:01:10+00:00: Claimed by codex-ar1304-required-runner-20260917.

- 2026-09-17T15:01:44+00:00: Recorded command exit 0; command argv SHA-256
  22fa2122a4866c3bdd923877373b9ee30fa29e3f8633dd0004d8ac9c7ac79945.

- 2026-09-17T15:01:58+00:00: Recorded command exit 0; command argv SHA-256
  f321dd784b48b79bd8d2c316921d40566d7ea2361e52c7360f2bf43f1a516113.

- 2026-09-17T15:02:10+00:00: Recorded command exit 0; command argv SHA-256
  01b7773ff6a5df6f2c352a830ebb12c90e42979a04fa08480d075a11eb36676c.

- 2026-09-17T15:02:23+00:00: Recorded command exit 0; command argv SHA-256
  f038ceedf3c42b8fba892266adcdd1ef95c2a162d4920695d086155e847385af.

- 2026-09-17T15:02:36+00:00: Recorded command exit 0; command argv SHA-256
  22fa2122a4866c3bdd923877373b9ee30fa29e3f8633dd0004d8ac9c7ac79945.

- 2026-09-17T15:02:47+00:00: Recorded command exit 0; command argv SHA-256
  f321dd784b48b79bd8d2c316921d40566d7ea2361e52c7360f2bf43f1a516113.

- 2026-09-17T15:02:57+00:00: Recorded command exit 0; command argv SHA-256
  01b7773ff6a5df6f2c352a830ebb12c90e42979a04fa08480d075a11eb36676c.

- 2026-09-17T15:03:07+00:00: Recorded command exit 0; command argv SHA-256
  a4c377f134c5b39030ab457af4f83b0efb930328c81977618e2879350bd01df9.

- 2026-09-17T15:03:17+00:00: System-managed bus repair attempt committed as 2def1851e: native
  session bus now uses systemd activation semantics, and seed asks the image-native user manager to
  start dbus.service after user@1000. Focused seed test passes. A fresh QEMU retry was not completed
  in this turn; prior exact trial remains Transport endpoint is not connected with no required
  attestation. Next action: run one bounded fresh seed/QEMU retry, verify systemctl --user
  is-system-running and transient success, then run exact pr-publication.

- 2026-09-17T15:03:34+00:00: Signed systemd-activation repair 2def1851e is ready; run fresh QEMU
  required transient and pr-publication retry

- 2026-09-17T15:03:36+00:00: Claimed by codex-ar1304-required-runner-20260917.

- 2026-09-17T15:03:54+00:00: Recorded command exit 0; command argv SHA-256
  7c09be3b91084d45e719fc4a5bb495de37abc96bafc541ec4a4a589e03b48986.

- 2026-09-17T15:04:04+00:00: Recorded command exit 0; command argv SHA-256
  b46101eb02af16a142abb15ff768641eebd44775be8800a9cc6c002f7478e072.

- 2026-09-17T15:04:14+00:00: Recorded command exit 0; command argv SHA-256
  82fb4afcfe63aec91a4fe2b3f0054526e92aaa1e4174869f01d742b1b18bf28d.

- 2026-09-17T15:05:12+00:00: Recorded command exit 0; command argv SHA-256
  893cab2f5ec1c60a54bc5b18799281e8449e086bbc7e297b8ab146e79a804240.

- 2026-09-17T15:05:51+00:00: Fresh retry with signed systemd-activation/native-user-bus seed
  completed and powered down cleanly. user@1000 and asb-session-bus.service started, but exact
  required transient still failed: Failed to start transient service unit: Transport endpoint is not
  connected; /run/user/1000 unmount also failed during shutdown. No required pr-publication
  attestation exists. Next action: repair image-native user manager transport (not standalone dbus
  socket) or provision a supported dbus-user-session image; preserve six resource properties and
  fail closed.

- 2026-09-17T15:25:56+00:00: Fix seed to run required transient as user asb, matching historical
  exact-preflight success; retry fresh image

- 2026-09-17T15:25:59+00:00: Claimed by codex-ar1304-required-runner-20260917.

- 2026-09-17T15:26:31+00:00: Recorded command exit 0; command argv SHA-256
  22fa2122a4866c3bdd923877373b9ee30fa29e3f8633dd0004d8ac9c7ac79945.

- 2026-09-17T15:26:41+00:00: Recorded command exit 0; command argv SHA-256
  f321dd784b48b79bd8d2c316921d40566d7ea2361e52c7360f2bf43f1a516113.

- 2026-09-17T15:26:51+00:00: Recorded command exit 1; command argv SHA-256
  33c7a5005fe1ba735b00c97c49f5dfb16b89fbda7fb12871209a24c669437d48.

- 2026-09-17T15:27:07+00:00: Recorded command exit 0; command argv SHA-256
  01b7773ff6a5df6f2c352a830ebb12c90e42979a04fa08480d075a11eb36676c.

- 2026-09-17T15:27:18+00:00: Recorded command exit 0; command argv SHA-256
  33c7a5005fe1ba735b00c97c49f5dfb16b89fbda7fb12871209a24c669437d48.

- 2026-09-17T15:27:37+00:00: Recorded command exit 0; command argv SHA-256
  ecfda610c559d6de584c90cf12d0af24360145096142008dda305f8b2436a3f4.

- 2026-09-17T15:27:47+00:00: Recorded command exit 0; command argv SHA-256
  5b8a87e3a9445a542b30c5c82e0437ca8133843dd9832b263e515b2f1f71aeba.

- 2026-09-17T15:27:57+00:00: Recorded command exit 0; command argv SHA-256
  5062758589519f37eb83518d30cfda9686ecbf306dc5688bc4e97234bf25e91b.

- 2026-09-17T15:29:15+00:00: Heartbeat by codex-ar1304-required-runner-20260917.

- 2026-09-17T15:30:20+00:00: Recorded command exit 0; command argv SHA-256
  8c05403b33ba058c270bcd4b8b8f1e45e92fa9c5bfe83806fc55dd641460900d.

- 2026-09-17T15:31:05+00:00: Recorded command exit 1; command argv SHA-256
  c2a42bfee660a654e32623859f360b861f66fb6a9398d76e787d91d55ef28bd3.

- 2026-09-17T15:31:21+00:00: Recorded command exit 0; command argv SHA-256
  7d854384b41cb52ec42a32f59f7e5b04be9f93ca5d300a826e664cfb8fe66ba8.

- 2026-09-17T15:31:41+00:00: Recorded command exit 2; command argv SHA-256
  518395b9393f5ca538123e3ef4a500f01f505abb9d77105adebe3e361646306b.

- 2026-09-17T15:31:59+00:00: Recorded command exit 0; command argv SHA-256
  4156538b306d4d91c988fe610e2e4290e71d1f10a58ae7f52e95a44a85af1ad0.

- 2026-09-17T15:32:17+00:00: Recorded command exit 0; command argv SHA-256
  14c0270317e42228bfb63ec18e209fcb30e61a0b77e4b50f3b7a18d93cdb301b.

- 2026-09-17T15:32:32+00:00: Recorded command exit 0; command argv SHA-256
  5b8a87e3a9445a542b30c5c82e0437ca8133843dd9832b263e515b2f1f71aeba.

- 2026-09-17T15:33:33+00:00: Recorded command exit 0; command argv SHA-256
  8aa3b9540e455b53061f537ef4d357b97506190a813ec2aebef889b2b9d126d4.

- 2026-09-17T15:34:34+00:00: Recorded command exit 0; command argv SHA-256
  f69cdeed45cdc390b888fa6886e5ff2c5e54cbb8d7e53f23e3397d29c18db0b0.

- 2026-09-17T15:34:55+00:00: Recorded command exit 0; command argv SHA-256
  8999bb8d9afe589a1a51c71ab0ac6f4690228588ae68d4d73ef95880a211947e.

- 2026-09-17T15:35:10+00:00: Recorded command exit 0; command argv SHA-256
  a8fc26108c654bf1a4825b8954416f69711c622cb44bb1978da5f8577a16a231.

- 2026-09-17T15:35:26+00:00: Recorded command exit 0; command argv SHA-256
  d6e1e69d5b44032eba72f71cb741212fb5667506fcc4de247a4ffcf2fba9f1b6.

- 2026-09-17T15:35:37+00:00: Recorded command exit 0; command argv SHA-256
  b16a011080889558ec4037eb428a51591f2626fe57255a7d965153c78c6f3eb8.

- 2026-09-17T15:35:47+00:00: Recorded command exit 0; command argv SHA-256
  b16a011080889558ec4037eb428a51591f2626fe57255a7d965153c78c6f3eb8.

- 2026-09-17T15:35:59+00:00: Recorded command exit 0; command argv SHA-256
  f731392db5fb87ab97d02442e28f626bd7dcaddd0722ded313a5db9c7febbf80.

- 2026-09-17T15:36:09+00:00: Recorded command exit 0; command argv SHA-256
  412694039877f951004a12a054de2ee9f2e2916f63964fa3e8e369250de9295e.

- 2026-09-17T15:37:26+00:00: Recorded command exit 0; command argv SHA-256
  556cba6b72e60e75c90245ed5b54cbbad9361fc8bb800bc8741e82eba735dc51.

- 2026-09-17T15:37:45+00:00: Recorded command exit 0; command argv SHA-256
  4156538b306d4d91c988fe610e2e4290e71d1f10a58ae7f52e95a44a85af1ad0.

- 2026-09-17T15:37:56+00:00: Recorded command exit 0; command argv SHA-256
  14c0270317e42228bfb63ec18e209fcb30e61a0b77e4b50f3b7a18d93cdb301b.

- 2026-09-17T15:38:06+00:00: Recorded command exit 0; command argv SHA-256
  5b8a87e3a9445a542b30c5c82e0437ca8133843dd9832b263e515b2f1f71aeba.

- 2026-09-17T15:39:02+00:00: Heartbeat by codex-ar1304-required-runner-20260917.

- 2026-09-17T15:39:09+00:00: Recorded command exit 0; command argv SHA-256
  1e91f9939e7fa94e737dbc20e5b1f689a9a8cd563b72c28f2af8069e48a2d2a0.

- 2026-09-17T15:39:25+00:00: Recorded command exit 1; command argv SHA-256
  8e139055c7eb769f120e793d3f6622be045c235d7d46470671a64900b1af3e52.

- 2026-09-17T15:39:37+00:00: Recorded command exit 1; command argv SHA-256
  95abfde8615cb3e2bf6686de67c68620909aa989ec36ae272021f90dac523a56.

- 2026-09-17T15:40:02+00:00: Recorded command exit 0; command argv SHA-256
  f5a0ad10e549ed030e7f95a780d045e48f9f59e0303ecc4dd6e714137f82438e.

- 2026-09-17T15:40:22+00:00: Recorded command exit 0; command argv SHA-256
  4156538b306d4d91c988fe610e2e4290e71d1f10a58ae7f52e95a44a85af1ad0.

- 2026-09-17T15:40:32+00:00: Recorded command exit 0; command argv SHA-256
  14c0270317e42228bfb63ec18e209fcb30e61a0b77e4b50f3b7a18d93cdb301b.

- 2026-09-17T15:40:46+00:00: Recorded command exit 0; command argv SHA-256
  5b8a87e3a9445a542b30c5c82e0437ca8133843dd9832b263e515b2f1f71aeba.

- 2026-09-17T15:41:39+00:00: Recorded command exit 0; command argv SHA-256
  d4e9ccee653b1d62143b915f3d931273312f4dd436de5baf40be3e9d2f1b6fd5.

- 2026-09-17T15:41:54+00:00: Recorded command exit 0; command argv SHA-256
  3f292f40d377096d72940bff6f6a3114595b122461c6e75dc5bb0d04c3f267a0.

- 2026-09-17T15:42:18+00:00: Recorded command exit 0; command argv SHA-256
  70a8a572a56300f548062bdff39b39df0c44d00061409de30064ed594e06418e.

- 2026-09-17T15:42:39+00:00: Recorded command exit 0; command argv SHA-256
  6bf1a950bcbcbea4785d672f62ccad360505a80710290a10e772618aa88af5d7.

- 2026-09-17T15:42:49+00:00: Recorded command exit 1; command argv SHA-256
  4156538b306d4d91c988fe610e2e4290e71d1f10a58ae7f52e95a44a85af1ad0.

- 2026-09-17T15:42:59+00:00: Recorded command exit 0; command argv SHA-256
  14c0270317e42228bfb63ec18e209fcb30e61a0b77e4b50f3b7a18d93cdb301b.

- 2026-09-17T15:43:12+00:00: Recorded command exit 0; command argv SHA-256
  5b8a87e3a9445a542b30c5c82e0437ca8133843dd9832b263e515b2f1f71aeba.

- 2026-09-17T15:43:23+00:00: Recorded command exit 0; command argv SHA-256
  34e7276c4be819d1677e888a37f64196793dd7d3a14146af37ae0924cce6c6ef.

- 2026-09-17T15:43:35+00:00: Recorded command exit 5; command argv SHA-256
  4156538b306d4d91c988fe610e2e4290e71d1f10a58ae7f52e95a44a85af1ad0.

- 2026-09-17T15:44:09+00:00: Recorded command exit 0; command argv SHA-256
  f970b469adcd664841b9d22e9781a375105b4771ccd9cffc682d8896d738db1c.

- 2026-09-17T15:44:20+00:00: Recorded command exit 0; command argv SHA-256
  4156538b306d4d91c988fe610e2e4290e71d1f10a58ae7f52e95a44a85af1ad0.

- 2026-09-17T15:45:22+00:00: Recorded command exit 0; command argv SHA-256
  30164e49319514995f65582dfa80c7b88892886fad549a222e90150658e21518.

- 2026-09-17T15:45:32+00:00: Recorded command exit 0; command argv SHA-256
  1888543ac7089eb56fe0308473e7860faff3b26df930138b1d41b67316a4e823.

- 2026-09-17T15:45:46+00:00: Recorded command exit 0; command argv SHA-256
  a872e5ef0a2106a0983a3aa94c26c8a4cbf2d673b888ecf5855346c264a877f8.

- 2026-09-17T15:45:56+00:00: Recorded command exit 0; command argv SHA-256
  14c0270317e42228bfb63ec18e209fcb30e61a0b77e4b50f3b7a18d93cdb301b.

- 2026-09-17T15:46:06+00:00: Recorded command exit 0; command argv SHA-256
  5b8a87e3a9445a542b30c5c82e0437ca8133843dd9832b263e515b2f1f71aeba.

- 2026-09-17T15:47:04+00:00: Recorded command exit 0; command argv SHA-256
  2db2ad5feb85d680ca5d47a591ae17be7203ab068262aba88d5b07adc95d3a77.

- 2026-09-17T15:47:21+00:00: Recorded command exit 0; command argv SHA-256
  e99a9eaba6e7bc5a26306556cb6faa9570492d04dc64be80a0da84f53c692cf9.

- 2026-09-17T15:47:31+00:00: Recorded command exit 0; command argv SHA-256
  0aaf6619581609430f5988db70694a109f3646e66c503e6e5e948419aaec95d2.

- 2026-09-17T15:47:41+00:00: Recorded command exit 0; command argv SHA-256
  203ea09610e10cd7d772327acad09739e954c8f44238ead9bfe7217f605ac27a.

- 2026-09-17T15:48:05+00:00: Recorded command exit 0; command argv SHA-256
  8d06d641d5d965b9b28f704dfd7f213dc6928ddb22be7fbf06cb23d4685b5f6e.

- 2026-09-17T15:48:15+00:00: Recorded command exit 0; command argv SHA-256
  c3580cb8487a81f0d291210b3dd5528a879c221a256fea220f5a800488a984d8.

- 2026-09-17T15:48:33+00:00: Recorded command exit 1; command argv SHA-256
  e1adc1ecc5b6b7b4e2988bc8188bc85b84f8b986162c1a5ad0f8351206f792fa.

- 2026-09-17T15:48:43+00:00: Recorded command exit 0; command argv SHA-256
  4c2b4927fa87944957fcdf5a20a3aeb0e7bf1fadb0e69dca3beca136cfe6b3a9.

- 2026-09-17T15:48:53+00:00: Recorded command exit 0; command argv SHA-256
  4156538b306d4d91c988fe610e2e4290e71d1f10a58ae7f52e95a44a85af1ad0.

- 2026-09-17T15:49:14+00:00: Recorded command exit 0; command argv SHA-256
  1d96d56e0aedc1b5d6c098dcd4c090a253add60a744fc4d228656a36080a1458.

- 2026-09-17T15:49:23+00:00: Recorded command exit 1; command argv SHA-256
  e1adc1ecc5b6b7b4e2988bc8188bc85b84f8b986162c1a5ad0f8351206f792fa.

- 2026-09-17T15:49:33+00:00: Recorded command exit 0; command argv SHA-256
  4c2b4927fa87944957fcdf5a20a3aeb0e7bf1fadb0e69dca3beca136cfe6b3a9.

- 2026-09-17T15:49:54+00:00: Recorded command exit 0; command argv SHA-256
  d95f22f9fd496f1e35d75e3e55e6011d6e982eba20ab955a988e8f2ad9ad6e6d.

- 2026-09-17T15:50:04+00:00: Recorded command exit 0; command argv SHA-256
  e1adc1ecc5b6b7b4e2988bc8188bc85b84f8b986162c1a5ad0f8351206f792fa.

- 2026-09-17T15:50:15+00:00: Recorded command exit 0; command argv SHA-256
  4c2b4927fa87944957fcdf5a20a3aeb0e7bf1fadb0e69dca3beca136cfe6b3a9.

- 2026-09-17T15:50:30+00:00: Recorded command exit 0; command argv SHA-256
  8d06d641d5d965b9b28f704dfd7f213dc6928ddb22be7fbf06cb23d4685b5f6e.

- 2026-09-17T15:50:40+00:00: Recorded command exit 0; command argv SHA-256
  b65dd5a5292101a49b1cd3e03dae5c7d1048c2880d918d9d3259201f1ff99a4c.

- 2026-09-17T15:51:35+00:00: Recorded command exit 0; command argv SHA-256
  39a4da31a6176a10883db2646ce42dac69581bf1c0646596c076d3ac094aeee8.

- 2026-09-17T15:52:08+00:00: Recorded command exit 0; command argv SHA-256
  6ac305e2a47adeb2919edaa0648e2db964a778fd64e37aaa8651a47e967c9df6.

- 2026-09-17T15:52:21+00:00: Heartbeat by codex-ar1304-required-runner-20260917.

- 2026-09-17T15:52:56+00:00: Qualified fresh offline QEMU required publication: PR4 serial emitted
  REQUIRED_TRANSIENT_RC=0 and PR_PUBLICATION_RC=0. Attestation was extracted from the UUID-mounted
  data image at evidence/pr-publication-attestation.json: status success, profile pr-publication,
  containment_mode required, candidate 39c8933f5, six outcomes all success, memory_max 3G, swap_max
  3G, address_space_max 8G, workers 2, timeout 1800, tool JAR SHA256 936a262...050e88. Fresh VM used
  -net none, no host mounts, reviewed data filesystem UUID, 32G RAM and 8 vCPU; QEMU exited cleanly.
  Full applicable pytest passed, focused seed tests 2 passed, Ruff check/format and mypy passed. PR3
  RC1 was repaired by exporting separated GIT_DIR/GIT_WORK_TREE; no gate was weakened. Full
  attestation JSON remains in the private runner evidence path for review.

- 2026-09-17T15:56:16+00:00: Heartbeat by codex-ar1304-required-runner-20260917.

- 2026-09-17T15:56:21+00:00: Recorded command exit 0; command argv SHA-256
  d4b13486caa85bf1256288e584d7b89fdfc148916295390d2cc6e6c9d33ddee6.

- 2026-09-17T15:56:38+00:00: Recorded command exit 1; command argv SHA-256
  2c671e5fa3235e302dbcb7d267a20dd6c9ce48c448f1346e3844e0de8b94b5c0.

- 2026-09-17T15:56:54+00:00: Recorded command exit 0; command argv SHA-256
  631fe1008436f2184b0e3876f670412ac537b52fb990770f17a0322a05847db5.

- 2026-09-17T15:57:16+00:00: Recorded command exit 0; command argv SHA-256
  4156538b306d4d91c988fe610e2e4290e71d1f10a58ae7f52e95a44a85af1ad0.

- 2026-09-17T15:57:26+00:00: Recorded command exit 0; command argv SHA-256
  e1adc1ecc5b6b7b4e2988bc8188bc85b84f8b986162c1a5ad0f8351206f792fa.

- 2026-09-17T15:57:36+00:00: Recorded command exit 0; command argv SHA-256
  4c2b4927fa87944957fcdf5a20a3aeb0e7bf1fadb0e69dca3beca136cfe6b3a9.

- 2026-09-17T15:57:52+00:00: Recorded command exit 0; command argv SHA-256
  01b7773ff6a5df6f2c352a830ebb12c90e42979a04fa08480d075a11eb36676c.

- 2026-09-17T15:58:02+00:00: Recorded command exit 0; command argv SHA-256
  8f60dfc8740e3af4d847e8c52f54ad4c1fa853ff893705be397bce51319d8124.

- 2026-09-17T15:58:32+00:00: Final hygiene pass complete: corrected the literal escaped newline in
  the SPDX/ruff header of tools/required_seed.py. Focused seed tests pass 2/2; Ruff check and format
  check pass. Signed+DCO fix commit is 920356c60. Existing PR4 required publication evidence remains
  green and unchanged: REQUIRED_TRANSIENT_RC=0, PR_PUBLICATION_RC=0, six models success, exact
  candidate 39c8933f5, required systemd cgroup bounds, no network, no host mounts. Lease renewed
  before this pass; AR remains held for independent review.
