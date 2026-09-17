---
{
  "branch": "feature/ar-1307-portable-tlc-runner-repair",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-18T01:51:43+00:00",
  "depends_on": [
    "AR-1302"
  ],
  "id": "AR-1307",
  "next_action": "Rebuild fresh data disk with /state checkout, /jvm, and pinned tla2tools.jar (current exact head 0ed457003); regenerate unique schema-valid seed, launch no-NIC 32 GiB overlay, and verify portable-smoke attestation.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "codex-ar1307-runner-repair-20260918",
  "plan": "../plans/AR-1307.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Repair and publish a canonical, bounded portable TLC runner for AR-1293.",
  "task_revision": 177,
  "title": "Portable TLC runner repair and qualification",
  "updated_at": "2026-09-17T23:53:04+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1307-portable-tlc-runner-repair"
}
---

## AR-1307

AR-1302's initial portable runner is not publishable: it directly invokes TLC,
does not use the canonical admission/attestation path, has incomplete
provenance and unbounded subprocess handling, and does not match the AR-1293
tier contracts. Repair it as a state-repository-only successor and produce
fresh exact-head qualification evidence. Do not touch ASB product, asb-tui,
handoffctl, external root-owned locks, or native-ARM-only requirements.

The predecessor AR-1302 is complete and is independently audited by this AR;
AR-1293 remains blocked until the repaired runner is merged and handed off.
See `../plans/AR-1307.md` for the complete scope, gates, evidence contract,
and protected publication sequence.

- 2026-09-17T23:55:00+00:00: Created as the repair successor after independent exact-head review
  found AR-1302's runner bypassed canonical admission/attestation and lacked required bounded
  execution, profile alignment, provenance, and clean publication evidence. Depends only on done
  AR-1302 so it can unblock blocked AR-1293 without a dependency cycle.

- 2026-09-17T21:53:43+00:00: Predecessor AR-1302 done; successor repair required by independent
  audit; dependencies verified.

- 2026-09-17T21:53:50+00:00: Claimed by codex-ar1307-runner-20260917.

- 2026-09-17T21:54:54+00:00: Heartbeat by codex-ar1307-runner-20260917.

- 2026-09-17T21:55:11+00:00: Heartbeat by codex-ar1307-runner-20260917.

- 2026-09-17T21:56:28+00:00: Recorded command exit 0; command argv SHA-256
  7814f4f5ae3f66be7fe59901f822afa0e2407e90e469a939a2123119a6df97c4.

- 2026-09-17T21:57:50+00:00: Recorded command exit 0; command argv SHA-256
  ceeaba81699fff9952c2220fe54bc01c6111a06d65ee6be972c52bc35a7881a9.

- 2026-09-17T22:00:13+00:00: Recorded command exit 0; command argv SHA-256
  ceeaba81699fff9952c2220fe54bc01c6111a06d65ee6be972c52bc35a7881a9.

- 2026-09-17T22:01:59+00:00: Recorded command exit 0; command argv SHA-256
  ceeaba81699fff9952c2220fe54bc01c6111a06d65ee6be972c52bc35a7881a9.

- 2026-09-17T22:02:41+00:00: Repair progress: imported the reviewed canonical runner/profile chain,
  moved default runtime paths under /srv/data/projects, added bounded argv-only process-group
  execution with output sinks and timeout classification, bound source/input/runner/artifact
  provenance, restricted attestation paths, and removed UUID privacy findings. Focused tlc runner
  suite 24/24 passes.

- 2026-09-17T22:02:54+00:00: Recorded command exit 1; command argv SHA-256
  647c7d343dc9cf1ef1dd6fc2acfc7e6c91186e61e088c40d3bcce31d2d94f1da.

- 2026-09-17T22:03:27+00:00: Recorded command exit 1; command argv SHA-256
  647c7d343dc9cf1ef1dd6fc2acfc7e6c91186e61e088c40d3bcce31d2d94f1da.

- 2026-09-17T22:03:45+00:00: Recorded command exit 0; command argv SHA-256
  647c7d343dc9cf1ef1dd6fc2acfc7e6c91186e61e088c40d3bcce31d2d94f1da.

- 2026-09-17T22:03:58+00:00: Recorded command exit 1; command argv SHA-256
  35451d934feac81f54c673dffd03f08b9f39bdca932e02bb60d02fe7b9510d85.

- 2026-09-17T22:04:10+00:00: Recorded command exit 0; command argv SHA-256
  b3a8c7a83f17becfea5e9179bb4c54e3673f4f792127f2649819ec721a2ac89d.

- 2026-09-17T22:04:25+00:00: Recorded command exit 0; command argv SHA-256
  35451d934feac81f54c673dffd03f08b9f39bdca932e02bb60d02fe7b9510d85.

- 2026-09-17T22:04:31+00:00: Recorded command exit 1; command argv SHA-256
  b306744bea32d95de88c1e3a594e1ab79c5d7426c46094ba700459370939fe04.

- 2026-09-17T22:05:11+00:00: Recorded command exit 0; command argv SHA-256
  647c7d343dc9cf1ef1dd6fc2acfc7e6c91186e61e088c40d3bcce31d2d94f1da.

- 2026-09-17T22:05:39+00:00: Recorded command exit 0; command argv SHA-256
  ceeaba81699fff9952c2220fe54bc01c6111a06d65ee6be972c52bc35a7881a9.

- 2026-09-17T22:06:13+00:00: Recorded command exit 2; command argv SHA-256
  f5f34193f66501f3096e2811565c87894753967eca8ee738bfbbad99c34b3679.

- 2026-09-17T22:06:37+00:00: Recorded command exit 1; command argv SHA-256
  b306744bea32d95de88c1e3a594e1ab79c5d7426c46094ba700459370939fe04.

- 2026-09-17T22:07:08+00:00: Recorded command exit 0; command argv SHA-256
  ceeaba81699fff9952c2220fe54bc01c6111a06d65ee6be972c52bc35a7881a9.

- 2026-09-17T22:07:17+00:00: Recorded command exit 2; command argv SHA-256
  52dc70ce238ce65929c65cc056330da4fecedb4d2aacb01d41b7ece9c79b32b0.

- 2026-09-17T22:07:48+00:00: Recorded command exit 1; command argv SHA-256
  b306744bea32d95de88c1e3a594e1ab79c5d7426c46094ba700459370939fe04.

- 2026-09-17T22:08:04+00:00: Recorded command exit 0; command argv SHA-256
  492a1eb4c948f233ed6ee3cf382c237a79a0d006f34279f5a59a15d396c285f6.

- 2026-09-17T22:09:13+00:00: Recorded command exit 0; command argv SHA-256
  e981794f7b11a2649b4994bf5c6d6766c66655b08058e1c5b9a42d7befa07770.

- 2026-09-17T22:09:20+00:00: Recorded command exit 1; command argv SHA-256
  5ebb6af0f1cb936e95b316b025375d1ee451a01daa78e70403cf5842108bcf67.

- 2026-09-17T22:11:13+00:00: Recorded command exit 0; command argv SHA-256
  5ebb6af0f1cb936e95b316b025375d1ee451a01daa78e70403cf5842108bcf67.

- 2026-09-17T22:12:32+00:00: Recorded command exit 1; command argv SHA-256
  2981d4e835200224f66ca0a1492f6ec0b04dec4fae19e8ed53255597d9916b77.

- 2026-09-17T22:14:26+00:00: Recorded command exit 0; command argv SHA-256
  2981d4e835200224f66ca0a1492f6ec0b04dec4fae19e8ed53255597d9916b77.

- 2026-09-17T22:14:58+00:00: Recorded command exit 0; command argv SHA-256
  c315ad62365a5b9b52fad355897a2d44812c99a21b83b88226c69aec5b477994.

- 2026-09-17T22:16:06+00:00: Recorded command exit 1; command argv SHA-256
  e46882a783e424548d921283edfdb2986f14cae788eabed164e66e2c8f01c2a1.

- 2026-09-17T22:16:27+00:00: Recorded command exit 0; command argv SHA-256
  e46882a783e424548d921283edfdb2986f14cae788eabed164e66e2c8f01c2a1.

- 2026-09-17T22:17:18+00:00: Recorded command exit 1; command argv SHA-256
  e981794f7b11a2649b4994bf5c6d6766c66655b08058e1c5b9a42d7befa07770.

- 2026-09-17T22:18:19+00:00: Recorded command exit 1; command argv SHA-256
  e981794f7b11a2649b4994bf5c6d6766c66655b08058e1c5b9a42d7befa07770.

- 2026-09-17T22:18:30+00:00: Recorded command exit 0; command argv SHA-256
  5e1fb184afd4dc0dc2576f69a536095d169ad68ef2b778528804e15674bc5062.

- 2026-09-17T22:19:08+00:00: Recorded command exit 1; command argv SHA-256
  e981794f7b11a2649b4994bf5c6d6766c66655b08058e1c5b9a42d7befa07770.

- 2026-09-17T22:19:49+00:00: Recorded command exit 0; command argv SHA-256
  e981794f7b11a2649b4994bf5c6d6766c66655b08058e1c5b9a42d7befa07770.

- 2026-09-17T22:20:04+00:00: Recorded command exit 1; command argv SHA-256
  21118e99fab417e16c8924f3b8ce3e80a14d6ed47ae5eb67808600994c05b27e.

- 2026-09-17T22:20:40+00:00: Recorded command exit 0; command argv SHA-256
  21118e99fab417e16c8924f3b8ce3e80a14d6ed47ae5eb67808600994c05b27e.

- 2026-09-17T22:20:56+00:00: Recorded command exit 0; command argv SHA-256
  064b762dc246489ac6b973d738892948c5a1077cd2e5168a31680c21b54457b7.

- 2026-09-17T22:21:12+00:00: Recorded command exit 0; command argv SHA-256
  4b54929262873b85aa35d9014e4dd8edd023e42855d680874c47891d11f3f0e0.

- 2026-09-17T22:22:34+00:00: Recorded command exit 1; command argv SHA-256
  e46882a783e424548d921283edfdb2986f14cae788eabed164e66e2c8f01c2a1.

- 2026-09-17T22:24:43+00:00: Recorded command exit 0; command argv SHA-256
  e46882a783e424548d921283edfdb2986f14cae788eabed164e66e2c8f01c2a1.

- 2026-09-17T22:24:53+00:00: Recorded command exit 0; command argv SHA-256
  c63074c3dcedd47044b5d3b47370590bd1797bcccad8648456111359fd11a52a.

- 2026-09-17T22:25:04+00:00: Recorded command exit 0; command argv SHA-256
  21118e99fab417e16c8924f3b8ce3e80a14d6ed47ae5eb67808600994c05b27e.

- 2026-09-17T22:25:53+00:00: Recorded command exit 0; command argv SHA-256
  5ebb6af0f1cb936e95b316b025375d1ee451a01daa78e70403cf5842108bcf67.

- 2026-09-17T22:26:05+00:00: Recorded command exit 0; command argv SHA-256
  51d288571189e7b790842bb8e9f9938e8bcd2774b82009d78d913d38bf86ded3.

- 2026-09-17T22:26:22+00:00: Recorded command exit 1; command argv SHA-256
  f89061cd09a534083a105e533e77ded075b780c94db01b2a7b8bb0c91081d74e.

- 2026-09-17T22:26:32+00:00: Recorded command exit 0; command argv SHA-256
  2a5f18a018eac4703aa065a1484ea3190893d02da0a4a6cf358510cff78afa0c.

- 2026-09-17T22:26:45+00:00: Recorded command exit 0; command argv SHA-256
  7c730eec3ea71bd24ffc5a9255bf7f542481bf601dba6c72bed6e00f6c2fab3c.

- 2026-09-17T22:27:40+00:00: Recorded command exit 0; command argv SHA-256
  cd01dc4ce3b5395605f09adb8da04db9ebe76fa4b42e0061259f36a41c77e142.

- 2026-09-17T22:27:52+00:00: Recorded command exit 0; command argv SHA-256
  a0c12852d98ed8cdeddba6cf11c4ebf6b6f4ce8b222cf71bd464d3507172c644.

- 2026-09-17T22:28:55+00:00: Recorded command exit 0; command argv SHA-256
  7e8d013647ff7a55e3142976e80beadb9b213994fc040b0a07eb27e5708731fd.

- 2026-09-17T23:13:52+00:00: Coordinator recovery: prior owner is stale/interrupted; preserving
  prior durable evidence and releasing claim for takeover.

- 2026-09-17T23:13:52+00:00: Claimed by codex-ar1307-runner-repair-20260918.

- 2026-09-17T23:14:15+00:00: Recovery checkpoint: old interrupted owner claim released and renewed.
  QEMU attempt was infrastructure-startup failure: with -nic none, serial remained at
  systemd-networkd-wait-online.service/start for ~37s and process exited; no formal result or
  success attestation. The seed mask in bootcmd was too late. Next repair is an early cloud-init
  network: config disabled seed, preserving no NIC/no host mounts and all formal gates.

- 2026-09-17T23:14:19+00:00: Recorded command exit 0; command argv SHA-256
  fac9bda16627df4fec2db22cac028da8f7d6859fffabc855a52f0008a8ec2ec4.

- 2026-09-17T23:14:34+00:00: Recorded command exit 0; command argv SHA-256
  b8426c018f2a603455ea9a581ee0956e55b20f8d0122abc5b32d29ead0875ddc.

- 2026-09-17T23:15:00+00:00: Recorded command exit 0; command argv SHA-256
  7954dbff2f08ffa9fa80dca2f4409518a6eda9cec98ea2eb681aa10a13eadd8c.

- 2026-09-17T23:15:21+00:00: Recorded command exit 0; command argv SHA-256
  c3a0b0a748eb66dd2b1b971b81945dfe62da5c28677385578addf1bde670d71e.

- 2026-09-17T23:16:19+00:00: Recorded command exit 0; command argv SHA-256
  db4f7a1f0b269f666d7a3efd932e5e0d89b7662522d697959375e73111e5fd84.

- 2026-09-17T23:16:29+00:00: Recorded command exit 0; command argv SHA-256
  3b4ea6a60bc0b724b82ba8eab905ba9d24ccfdc56d0031007626dfe12da5c67b.

- 2026-09-17T23:16:44+00:00: Recorded command exit 0; command argv SHA-256
  4fb3b2153b09d6a03be652e28e97c2075fb0c7dbb0e09d1bad1c1e1d2bfa41db.

- 2026-09-17T23:16:59+00:00: Recorded command exit 1; command argv SHA-256
  78c97931e404ab0fb1b00b84d1111d2bd8392c0e5ac63eddf9f998a32e7cb7b7.

- 2026-09-17T23:17:14+00:00: Recorded command exit 1; command argv SHA-256
  c36b5aaa72277d32122fe1ddf7b64b3c9adaca7acb90b44dabed6a5c6f35d583.

- 2026-09-17T23:17:40+00:00: Recorded command exit 0; command argv SHA-256
  01202f34d6d77ecdd202bbcc5d89db8e0a0fd3e756755d10f991b298ca9aec51.

- 2026-09-17T23:18:01+00:00: Recorded command exit 0; command argv SHA-256
  205671d3131555334b7283dd552ec3720a2b0e64b724f8de7373edec32f98419.

- 2026-09-17T23:18:15+00:00: Recorded command exit 0; command argv SHA-256
  4e36aa8a62a5ab0531ec27c0565df5b2ac7ab5b600a65e9c2e6a3395406b3cde.

- 2026-09-17T23:18:36+00:00: Recorded command exit 0; command argv SHA-256
  8a2cd257d2680049708c980ea45bafc529921934d587dccd34020f7a21f0c4c9.

- 2026-09-17T23:18:56+00:00: Recorded command exit 0; command argv SHA-256
  9625d5659fb655cbe6421163a9785687e77597cc1adf3c4f43953a23ca6400b6.

- 2026-09-17T23:19:16+00:00: Recorded command exit 0; command argv SHA-256
  32a673e43516807b35aab3a78dcc0948d27023d0ca2cde4d81b313f0cd1d768b.

- 2026-09-17T23:20:23+00:00: Recorded command exit 0; command argv SHA-256
  5ef9bcaa026b3bc7e53cc684479208b2cf0d1e54c4b17d90ac97493fe57f2f7d.

- 2026-09-17T23:20:36+00:00: Recorded command exit 0; command argv SHA-256
  de68ead3e7bbb1df13dc3d7d3f8093f45ce86c7ddd49f51bc381dd618e18c90f.

- 2026-09-17T23:20:46+00:00: Recorded command exit 0; command argv SHA-256
  20c6de78daa1446614469aac7ded9169974031a90cd89ce528357c596c204b03.

- 2026-09-17T23:20:56+00:00: Recorded command exit 0; command argv SHA-256
  6d8536b6866701469f5977c2ac9c397c140ea400fca92755ea9a47f47f997976.

- 2026-09-17T23:21:30+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-17T23:21:30+00:00: Classification: early-mask QEMU boot bypassed wait-online and reached
  cloud-init, but cloud-init failed closed with repeated OSError Errno 28 No space left on device at
  ~52s while package_update/apt and cloud-init logs wrote to the 3.5 GiB root. No formal result or
  attestation. This is runner capacity/input setup, not a model success; next action is fresh 32 GiB
  root plus offline-safe seed.

- 2026-09-17T23:22:03+00:00: Recorded command exit 0; command argv SHA-256
  8e9817d35b8e2b2da2d0e5af492eb28b1df1fdbd30bc546c8c1070f3cb12868b.

- 2026-09-17T23:22:19+00:00: Recorded command exit 0; command argv SHA-256
  282653984520fa809a266aaec9a07614839e12458bda4df2a9e4d94cb0775cd8.

- 2026-09-17T23:22:29+00:00: Recorded command exit 0; command argv SHA-256
  04fd3d5b83fcf2ecd8490c079a5686ae4480e9595aca4d9371d96ebea94173ce.

- 2026-09-17T23:22:39+00:00: Recorded command exit 0; command argv SHA-256
  516f611207e83afcd7ff449a90e96ad4aff2d063565c9356dd3dcb87a7242056.

- 2026-09-17T23:22:53+00:00: Recorded command exit 0; command argv SHA-256
  f9cd52de7a32120a9a346ca668a6473fe1816640fc8c4f025f94f7f90b66b936.

- 2026-09-17T23:23:03+00:00: Recorded command exit 0; command argv SHA-256
  0b7e73a4b4e5d854b77fc5f0bfdcba82dc2b52fd5748e644ca65a2da3a9ea04b.

- 2026-09-17T23:23:13+00:00: Recorded command exit 0; command argv SHA-256
  32a673e43516807b35aab3a78dcc0948d27023d0ca2cde4d81b313f0cd1d768b.

- 2026-09-17T23:24:46+00:00: Recorded command exit 0; command argv SHA-256
  1aae35db62bc6bb5298879b601cb7d9575e435b4f5505d9b75f5b4c031b93edd.

- 2026-09-17T23:24:56+00:00: Recorded command exit 0; command argv SHA-256
  5ecf90aa6f9102236669427adabec976943ecf2fe28288ecf082d00899cde9fe.

- 2026-09-17T23:25:25+00:00: Recorded command exit 1; command argv SHA-256
  536f4cf684165972eb5d7afac90f6761044c94b5cc4b36d4fa88e64645f2164d.

- 2026-09-17T23:25:39+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-17T23:25:46+00:00: Failure classification: generated seed was malformed because
  guest_seed.py emitted a literal newline in the offline curl printf scalar; cloud-init ignored
  user-data and produced no receipt. Earlier fresh 3.5 GiB root also failed closed with Errno 28
  ENOSPC during cloud-init. A direct host Python YAML check exited 1 because PyYAML is not
  installed; this is a tooling limitation, not YAML evidence. Source escaping and explicit
  package_update/package_upgrade false plus packages empty were patched; next gate is project
  offline YAML validation and clean boot.

- 2026-09-17T23:25:57+00:00: Recorded command exit 0; command argv SHA-256
  a665430ffafff42db935fd497dea83f66a4b4e50765a4214ec56cd80b321c7a2.

- 2026-09-17T23:26:13+00:00: Recorded command exit 0; command argv SHA-256
  357e5d3d5b248ebbc5dfd2849f632038978fdc0bb93874f4ba47558469237764.

- 2026-09-17T23:26:25+00:00: Recorded command exit 0; command argv SHA-256
  537dc7ad9ee68f1a209f933d191cfc9ff842da0132bff37cb71cacc746db542a.

- 2026-09-17T23:27:27+00:00: Recorded command exit 0; command argv SHA-256
  dbb76b70454db80d538786b17db804fb846fdab99c81e1efc7ff56fe58933434.

- 2026-09-17T23:27:56+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-17T23:28:03+00:00: Fresh 32 GiB early-mask boot reached user@1000 and D-Bus and executed
  cloud-init. Formal launch then failed closed because /mnt/asb-data/state/.asb-tlc was root-owned,
  yielding PermissionError; validator consequently found no attestation. This is an
  owner-confinement setup defect. Patched guest_seed to recursively chown the mounted state checkout
  to uid 1000 before execution. The prior host YAML validator also exited 1 due missing PyYAML; use
  available project/schema validator or cloud-init parsing.

- 2026-09-17T23:28:08+00:00: Recorded command exit 2; command argv SHA-256
  8085271911441be71965fa4475a712ec89248818f09f9f5ce0b3252d2968140e.

- 2026-09-17T23:28:35+00:00: Recorded command exit 1; command argv SHA-256
  02f27ae37112c71de44baf3af50d673ba6f909c230d988ee11ede0cf16c95f1e.

- 2026-09-17T23:28:55+00:00: Recorded command exit 0; command argv SHA-256
  5149a2d7424ac8c39d5fd7e60fc1598faab7174808ed7653845729de009f5dd1.

- 2026-09-17T23:29:06+00:00: Recorded command exit 0; command argv SHA-256
  5ef9bcaa026b3bc7e53cc684479208b2cf0d1e54c4b17d90ac97493fe57f2f7d.

- 2026-09-17T23:29:16+00:00: Recorded command exit 0; command argv SHA-256
  02f27ae37112c71de44baf3af50d673ba6f909c230d988ee11ede0cf16c95f1e.

- 2026-09-17T23:29:34+00:00: Recorded command exit 0; command argv SHA-256
  a70f5b6c4b3cd59857b6c2a6f2fda40710f43289be3036848361008be8a4e8c0.

- 2026-09-17T23:31:10+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-17T23:31:16+00:00: Classification: schema-valid seed on a fresh 32 GiB overlay reached
  user@1000 but cloud-init final emitted no runcmd and no receipt; root cause is inherited
  cloud-init semaphores in the prepared run base. Do not accept this as qualification. Next run uses
  a unique deterministic instance-id/local-hostname plus a newly created overlay.

- 2026-09-17T23:31:24+00:00: Recorded command exit 0; command argv SHA-256
  15876391cf8a9bbf0d5d9600313ba588da009a54a509288fd8faf61ba0bb89ac.

- 2026-09-17T23:31:34+00:00: Recorded command exit 0; command argv SHA-256
  2845ca1afe95936ea30f2b40ffe9300e3d5da123facfdb14d44e075f12fe1584.

- 2026-09-17T23:31:44+00:00: Recorded command exit 0; command argv SHA-256
  17f8d9af2e93b264f60e562ce2080c2149a2e8a5e12e092987ed00d01ed956b4.

- 2026-09-17T23:32:02+00:00: Recorded command exit 1; command argv SHA-256
  3da1afa129190a2823d9a274abfb609e928453e89250c9e6121ca53d8f5f866c.

- 2026-09-17T23:32:22+00:00: Recorded command exit 0; command argv SHA-256
  4a4b79d819d909645e4d03c0919a9fda845fc006e12f02eceecebc1c52177153.

- 2026-09-17T23:32:32+00:00: Recorded command exit 0; command argv SHA-256
  6efd40d669d0126099e334634d75148d67c0bcd543bbbeb80ffaf3e321d5ba59.

- 2026-09-17T23:32:42+00:00: Recorded command exit 1; command argv SHA-256
  8892be8e80a6ea973d7752540d566ab03cbd17b053a0a11bcd5696fb68999140.

- 2026-09-17T23:32:52+00:00: Recorded command exit 1; command argv SHA-256
  4593805d47d77b74fd56147fd9c289007bc7286f43bd6505c3268cdec8d9786e.

- 2026-09-17T23:33:01+00:00: Recorded command exit 1; command argv SHA-256
  38bc1f973ce4f7a0c5c06bd789a73879b57e2237f624a3d281984c28d943cac5.

- 2026-09-17T23:33:50+00:00: Recorded command exit 0; command argv SHA-256
  3da1afa129190a2823d9a274abfb609e928453e89250c9e6121ca53d8f5f866c.

- 2026-09-17T23:34:28+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-17T23:34:35+00:00: Unique NoCloud run proved runcmd execution and owner-confinement:
  state/.asb-tlc was created and transient D-Bus probe passed. Formal command failed closed at
  provenance because seed exported GIT_DIR=/mnt/asb-data/git, which does not exist for the ordinary
  state checkout (.git), so git rev-parse returned failure; no attestation was produced. This is a
  truthful seed environment defect, now patched by removing those overrides. Earlier stale-root run
  and malformed-seed/ENOSPC failures remain recorded.

- 2026-09-17T23:34:44+00:00: Recorded command exit 1; command argv SHA-256
  5149a2d7424ac8c39d5fd7e60fc1598faab7174808ed7653845729de009f5dd1.

- 2026-09-17T23:34:54+00:00: Recorded command exit 0; command argv SHA-256
  0a92b3bb3649ebd1d3af43497b70cf4c01c8bf5913d686d10400a9d219d9bfa2.

- 2026-09-17T23:35:04+00:00: Recorded command exit 0; command argv SHA-256
  fe37a9028cfd2ed3d701f2f7b6f6e10ee572313e5beaf5a570563f8c7ee8d49e.

- 2026-09-17T23:35:31+00:00: Latest portable attempt did execute runcmd (transient D-Bus RC=0 and
  state queue created) but failed closed during Git provenance because the seed supplied a
  nonexistent bare GIT_DIR; no evidence was emitted. This exact cause is now patched by removing
  GIT_DIR/GIT_WORK_TREE exports. Focused test initially caught the intentional contract update
  (obsolete GIT_DIR expectation); test was corrected. A fresh data disk and overlay are required to
  avoid stale state/evidence.

- 2026-09-17T23:35:42+00:00: Recorded command exit 0; command argv SHA-256
  195d0d2e82a167a925aeb813c219092d425f0d4cc725a4674a4838eab408af88.

- 2026-09-17T23:35:59+00:00: Recorded command exit 0; command argv SHA-256
  10fcc5f341a11e1d7c57512320bea7f4ed1084ee6ab0bb024824c341420fb8d4.

- 2026-09-17T23:36:09+00:00: Recorded command exit 0; command argv SHA-256
  09bc92f536af4e155069adaf9acc46f435c31df6773dfe0468fa466ea802a039.

- 2026-09-17T23:36:20+00:00: Recorded command exit 0; command argv SHA-256
  03f60ea01d6d4fca08d4dbbaae563b5151ceedad66136ec20b27e3b9b3410d72.

- 2026-09-17T23:36:30+00:00: Recorded command exit 0; command argv SHA-256
  7b5288040882cd6698c92dcb639abcff8c3fdb2eb009fd0104cd0bd2e8836042.

- 2026-09-17T23:36:49+00:00: Recorded command exit 0; command argv SHA-256
  29f85f22f51c708aa5a644703420af749f3d1fee3920680829b7d220d043134a.

- 2026-09-17T23:37:37+00:00: Recorded command exit 0; command argv SHA-256
  88caf16c5ba6024ffd36d79c0d74e84ee526b1bee4ae069efeafa1ba890affff.

- 2026-09-17T23:38:48+00:00: Fresh unique-instance portable run executed runcmd, passed
  user@1000/D-Bus and transient RC=0, then TLC exited 1 at startup with bounded JFR stack
  (TLAFlightRecorder via TLC.printWelcome) and no attestation. Pinned guest pair is OpenJDK 17.0.20
  + TLC 2.19 / tla2tools SHA 936a...; likely JFR cannot create temp files because Java defaults to
  root-owned /tmp while TMPDIR alone does not change java.io.tmpdir. Treat as runner environment
  failure, not formal success; next patch adds explicit -Djava.io.tmpdir owner-private.

- 2026-09-17T23:38:58+00:00: Recorded command exit 0; command argv SHA-256
  5149a2d7424ac8c39d5fd7e60fc1598faab7174808ed7653845729de009f5dd1.

- 2026-09-17T23:39:08+00:00: Recorded command exit 1; command argv SHA-256
  833530c1c3ed0326462beceb63a89c7f57d348a48decbf9ce778005fafa226f3.

- 2026-09-17T23:39:30+00:00: Recorded command exit 0; command argv SHA-256
  580198e39a723af499c3963fb9193bf8dc66534770ba1ceb3bb0c34508e56443.

- 2026-09-17T23:39:40+00:00: Recorded command exit 0; command argv SHA-256
  4c7f5454bdfd262343101f5017a1f97a7115b031cbcb94c018e800733381aacf.

- 2026-09-17T23:39:50+00:00: Recorded command exit 0; command argv SHA-256
  6c65902df44b90b32d6040ed535a40105a66a83f606b2925fcb174c607827440.

- 2026-09-17T23:40:17+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-17T23:40:34+00:00: Recorded command exit 0; command argv SHA-256
  5f455b2880c26ebf9d46345d2fe5106164bc21e22c2e594ba3bbc532752bb515.

- 2026-09-17T23:40:52+00:00: Recorded command exit 0; command argv SHA-256
  adbfd17bd5a46378d72f07219f1688bced64b1502623c7575151571fe8da7dcf.

- 2026-09-17T23:42:50+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-17T23:42:58+00:00: Recorded command exit 0; command argv SHA-256
  0b500e031bbfcb988cacf4c93adcbb80fa33615f7e30b97427dd10334ebc633b.

- 2026-09-17T23:43:10+00:00: Recorded command exit 0; command argv SHA-256
  7351a424bf79a78fb69a69e2f65a54bba03cef852e4cfbfc792d932a720abfb2.

- 2026-09-17T23:43:20+00:00: Recorded command exit 0; command argv SHA-256
  3a910fc0416d419750e327a4b86e2d7904997e8123bc35519c211c621e7f86a7.

- 2026-09-17T23:43:30+00:00: Recorded command exit 0; command argv SHA-256
  dfb9b2a643333e8a4acaf144a28f7171d1ed969db53c8ecd96a89ca99ed4b731.

- 2026-09-17T23:43:42+00:00: Recorded command exit 0; command argv SHA-256
  e6e57f3bee2d4de6d2fe049a6c3ab692ad5c26fe70973146aeec228d43d82380.

- 2026-09-17T23:43:52+00:00: Recorded command exit 0; command argv SHA-256
  1880d98e028f97d185979ea33f32da9c167599f53c4b3236f167fbfb5eb315b0.

- 2026-09-17T23:44:02+00:00: Recorded command exit 0; command argv SHA-256
  f27d014e6ac71ee49688851aee349db4f0a4053e63e34f159162c220bd503be0.

- 2026-09-17T23:44:20+00:00: Recorded command exit 0; command argv SHA-256
  388090616c4e81d7d40e44427cd04c0b801d1a6fe344200c36957ba345c6dc3b.

- 2026-09-17T23:44:29+00:00: Recorded command exit 0; command argv SHA-256
  5cc62d7aa5a0aa675321d7216cd21a748f8d665eb35a8d73835007fefeaea453.

- 2026-09-17T23:44:40+00:00: Recorded command exit 0; command argv SHA-256
  0d83b2fa8cec0340f18c35b1b8a6927bfde174f99ba8b4676242be00d4c70300.

- 2026-09-17T23:45:35+00:00: Recorded command exit 0; command argv SHA-256
  ef0b1ab8ee8987cd12e7fbfac0b291a32ab89a670e2bc6f91d732beea9931e15.

- 2026-09-17T23:46:15+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-17T23:46:22+00:00: Exact-head run reached cloud-init and user@1000, but failed before
  formal execution because the data disk staging root lacked /state: chown reported
  /mnt/asb-data/state absent and cd to /state/formal/handoffctl failed. This was caused by cloning
  the checkout directly into stage-head rather than nesting it under stage-head/state. No
  attestation accepted. Rebuilding the data image with the required layout now.

- 2026-09-17T23:46:31+00:00: Recorded command exit 0; command argv SHA-256
  31e47087583fed3b8df1d66d016592db467a274a42abfaf358a0fb1bf468842c.

- 2026-09-17T23:46:41+00:00: Recorded command exit 0; command argv SHA-256
  063a85ddd83681fce8b2fe401f9faaebbd132fb7a4f26f3e036de17481b3a0dd.

- 2026-09-17T23:46:51+00:00: Recorded command exit 0; command argv SHA-256
  86793550fdd2cd0591d928a907ab68d740bd0a57254e8d1ba36b588737e3cb36.

- 2026-09-17T23:47:01+00:00: Recorded command exit 0; command argv SHA-256
  e3dd80aee02157b76b42deb547e322c698c8659ab26a0a4f028dd25abc248de8.

- 2026-09-17T23:47:13+00:00: Recorded command exit 0; command argv SHA-256
  ec62b3b483fa4b338e71352418bafe7dbaf75e2dd12f6c778f82cc924344b7dc.

- 2026-09-17T23:47:32+00:00: Recorded command exit 0; command argv SHA-256
  b69fa0a3964bf62502dd65ac83083ad3463754cd4ac6fd234324c94709b2c7f1.

- 2026-09-17T23:47:43+00:00: Recorded command exit 0; command argv SHA-256
  d3e4bfd73309a9f6c5a2ad7a7b82b40f734933ff1233fd490df28f2ea79a51c5.

- 2026-09-17T23:47:59+00:00: Recorded command exit 0; command argv SHA-256
  94bc35cdee2f32fde888a7d930987e69ff15070ba511825bb30b0fa52ef69868.

- 2026-09-17T23:48:54+00:00: Recorded command exit 0; command argv SHA-256
  f81ebe3a9f1ab314c650370b0f384cb2d6c3cf75cec944660df313fc4a7801fe.

- 2026-09-17T23:49:46+00:00: Recorded command exit 0; command argv SHA-256
  5149a2d7424ac8c39d5fd7e60fc1598faab7174808ed7653845729de009f5dd1.

- 2026-09-17T23:49:56+00:00: Recorded command exit 0; command argv SHA-256
  7c730eec3ea71bd24ffc5a9255bf7f542481bf601dba6c72bed6e00f6c2fab3c.

- 2026-09-17T23:50:07+00:00: Recorded command exit 0; command argv SHA-256
  5a07988433ca26467f7eb4b400452bf4e4eac90db7945e8ec7a3de4caf89b4ff.

- 2026-09-17T23:50:17+00:00: Recorded command exit 0; command argv SHA-256
  202128cc7dfbcc039994721ac929ab81db2f41b3d4f21c11c1910344df45554f.

- 2026-09-17T23:50:45+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-17T23:50:46+00:00: Recorded command exit 0; command argv SHA-256
  5149a2d7424ac8c39d5fd7e60fc1598faab7174808ed7653845729de009f5dd1.

- 2026-09-17T23:50:55+00:00: Recorded command exit 0; command argv SHA-256
  5a07988433ca26467f7eb4b400452bf4e4eac90db7945e8ec7a3de4caf89b4ff.

- 2026-09-17T23:51:05+00:00: Recorded command exit 0; command argv SHA-256
  cfbf5b0aefe8b89e97d8b12aa954660caebe608187165d8c82f9c92b0a165f4d.

- 2026-09-17T23:51:23+00:00: Recorded command exit 0; command argv SHA-256
  adbfd17bd5a46378d72f07219f1688bced64b1502623c7575151571fe8da7dcf.

- 2026-09-17T23:51:43+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-17T23:51:50+00:00: Recorded command exit 0; command argv SHA-256
  6a9aa7ae59bff49171fd959f1aa379478b4e96b05ce7d809d2b887d63d6aa576.

- 2026-09-17T23:52:00+00:00: Recorded command exit 0; command argv SHA-256
  c2c00d1adc63e495f496efca7e6823a8462b80bdd033532a78620bfb6be92232.

- 2026-09-17T23:52:10+00:00: Recorded command exit 0; command argv SHA-256
  f2f08017701f3d0a1ba1729ae07db76d95e805766eb41ffc253992efc8f36821.

- 2026-09-17T23:52:23+00:00: Recorded command exit 0; command argv SHA-256
  e82f379b6f7c82f6d3d77170f1bc911ca1c3c6e552db4b74b63f7153fc55bd9d.

- 2026-09-17T23:52:33+00:00: Recorded command exit 0; command argv SHA-256
  dc1b9e1158c70444f08e4e4d0327d2e08b2843662b9689a74442a8c34a315792.

- 2026-09-17T23:52:44+00:00: Recorded command exit 0; command argv SHA-256
  0a73045730bb116861bcfc614adad08b13b76e6c957b7308ef95de47b6999e78.

- 2026-09-17T23:52:54+00:00: Recorded command exit 0; command argv SHA-256
  9db063933cc1c952d9225e9cabd59e974131842b64c916719ed0b9f6f1fc3abc.

- 2026-09-17T23:53:04+00:00: Recorded command exit 0; command argv SHA-256
  fd524869e9fc5f58ea4ad8453f2506ab17727e341830476ebcf8b00c4d31762b.
