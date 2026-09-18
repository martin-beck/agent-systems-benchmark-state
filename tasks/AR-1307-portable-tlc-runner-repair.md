---
{
  "branch": "feature/ar-1307-portable-tlc-runner-repair",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-18T02:34:44+00:00",
  "depends_on": [
    "AR-1302"
  ],
  "id": "AR-1307",
  "next_action": "Build fresh stage10 data image from checkout ca43179ea (not stage9), verify debugfs root state/jvm/tla2tools and source HEAD ca43179ea, regenerate unique seed, rerun portable-smoke, extract/validate attestation commit equals ca43179ea.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "codex-ar1307-runner-repair-20260918",
  "plan": "../plans/AR-1307.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Repair and publish a canonical, bounded portable TLC runner for AR-1293.",
  "task_revision": 314,
  "title": "Portable TLC runner repair and qualification",
  "updated_at": "2026-09-18T00:35:25+00:00",
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

- 2026-09-17T23:53:29+00:00: Recorded command exit 0; command argv SHA-256
  348933151e4ecae7fc381347468e5d3cc1a028d9d475caeb90f8ccb14d08b7cd.

- 2026-09-17T23:53:39+00:00: Recorded command exit 0; command argv SHA-256
  40697fefd46fa88337f62259afc210cd176f784184f6047647b82e4f9cc99803.

- 2026-09-17T23:53:49+00:00: Recorded command exit 0; command argv SHA-256
  782e022dedcb8eb193d16a28522e009960b68ef0a3ff21045fec20d9aa1ecc44.

- 2026-09-17T23:54:43+00:00: Recorded command exit 0; command argv SHA-256
  6b21fdfc961a49a7e3e4f4d6c6bea798bfd5fcdf3f75ec5807885840d1afd6ae.

- 2026-09-17T23:55:25+00:00: Recorded command exit 0; command argv SHA-256
  5149a2d7424ac8c39d5fd7e60fc1598faab7174808ed7653845729de009f5dd1.

- 2026-09-17T23:55:35+00:00: Recorded command exit 0; command argv SHA-256
  5a07988433ca26467f7eb4b400452bf4e4eac90db7945e8ec7a3de4caf89b4ff.

- 2026-09-17T23:55:45+00:00: Recorded command exit 0; command argv SHA-256
  0a97d0dcd501ba929ac756f1c23d49b069d20453ee76a8b57e10dd5084ad0802.

- 2026-09-17T23:55:57+00:00: Recorded command exit 0; command argv SHA-256
  adbfd17bd5a46378d72f07219f1688bced64b1502623c7575151571fe8da7dcf.

- 2026-09-17T23:56:07+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-17T23:56:14+00:00: Stage2 fresh-layout run now executed runcmd and reached TLC but
  retained the JFR startup failure; no attestation. Added explicit
  JAVA_TOOL_OPTIONS=-Djava.io.tmpdir=/mnt/asb-data/tmp, /tmp 1777 setup, and bounded preflight
  stat/java property commands to the signed pushed candidate. Focused tests 25/25 pass. Remote PR
  branch is 55b6ca3c4. Remaining work is a fresh exact-head diagnostic run to prove effective JVM
  temp path and classify/repair the JFR fixture without weakening TLC/JFR.

- 2026-09-17T23:56:55+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-17T23:56:56+00:00: Recorded command exit 0; command argv SHA-256
  6a9aa7ae59bff49171fd959f1aa379478b4e96b05ce7d809d2b887d63d6aa576.

- 2026-09-17T23:57:06+00:00: Recorded command exit 0; command argv SHA-256
  6fbe707954e4144da84014b9bfaaef15052104ef8d5b61b3c54a93cb959dcafb.

- 2026-09-17T23:57:16+00:00: Recorded command exit 0; command argv SHA-256
  86a8d59443c22e1372dded52c70335bc00687a35e70b1ce1684d279b9b20355b.

- 2026-09-17T23:57:26+00:00: Recorded command exit 0; command argv SHA-256
  cce621e79c6d621eb6caf834395485521b75237fedb1ec4184ba5d645442bf24.

- 2026-09-17T23:57:36+00:00: Recorded command exit 0; command argv SHA-256
  8497946e6ae27a8e352b0570178faff648ce5558ef1a90e7c79a8be9ee800e77.

- 2026-09-17T23:57:46+00:00: Recorded command exit 0; command argv SHA-256
  dfe05fa53af1ecf911469e4eeecd3da1c0f5b4a17baa3b9e40a6c30122c5e74e.

- 2026-09-17T23:57:56+00:00: Recorded command exit 0; command argv SHA-256
  98c1213d690554539e0133ec2fdf16941f7929d255adeef2b5044af0ae5981ca.

- 2026-09-17T23:58:06+00:00: Recorded command exit 0; command argv SHA-256
  9c63685b015801ff3a311541a4b53639d33087551ef5a10fcf3d187f1932005b.

- 2026-09-17T23:58:16+00:00: Recorded command exit 0; command argv SHA-256
  191c149f04d3f641c9dc8f92b7f6260362f6c413874aaec8597d157aeae87f6b.

- 2026-09-17T23:58:42+00:00: Recorded command exit 0; command argv SHA-256
  d4366d071fc2782a45cab578fb5bc81002624702e222e41b54085a472a168b04.

- 2026-09-17T23:58:52+00:00: Recorded command exit 0; command argv SHA-256
  60c4b085010fa8041ba94aefb667e67f3a4dca5720c56866bf3cacc9b95c7053.

- 2026-09-17T23:59:11+00:00: Recorded command exit 0; command argv SHA-256
  447ebb1702beb0adee8eabd2220c17c65b2a67ba08d0d98b2a8b401ba7cb9656.

- 2026-09-17T23:59:58+00:00: Recorded command exit 0; command argv SHA-256
  7a7b1d71036cdf3a258c16cf2136f2119066e682e7cb0bf2e69e15ecaf2cd65c.

- 2026-09-18T00:00:28+00:00: Stage3 diagnostic preflight proved tmp paths are root:root mode 1777
  and JDK/JAR paths were absent: env could not execute /mnt/asb-data/jvm/bin/java, curl shim
  reported missing /mnt/asb-data/tla2tools.jar, and validator found no evidence. The staging copy
  and mke2fs overlapped, so the image captured only /state. No formal result accepted. Rebuild
  sequentially with explicit artifact presence checks.

- 2026-09-18T00:00:35+00:00: Recorded command exit 0; command argv SHA-256
  53f00c09e1bb75cabb2978f14b6c65a702a384cf74f1a9f6d5f02d7ea3804b59.

- 2026-09-18T00:00:59+00:00: Recorded command exit 0; command argv SHA-256
  4a799d8f97d522583bbb7d5dbf457a53ce9c6d5e1e2429401ab55bfdb32fbb10.

- 2026-09-18T00:01:09+00:00: Recorded command exit 0; command argv SHA-256
  080409e35548eeec0a49a6c674afc9c2fd9adbccd23884804687b0296266dc4a.

- 2026-09-18T00:01:19+00:00: Recorded command exit 0; command argv SHA-256
  1d8cf657e4f85a84ad1cfa9552ae52e7815e33b65d66ee3b53cc0c7f30ef144c.

- 2026-09-18T00:02:17+00:00: Recorded command exit 0; command argv SHA-256
  906ec34ddc100381fa2de2ffa0b0fd2f089a79aadc7064fe6eb9f3046bedd98d.

- 2026-09-18T00:02:56+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T00:02:57+00:00: Recorded command exit 0; command argv SHA-256
  5149a2d7424ac8c39d5fd7e60fc1598faab7174808ed7653845729de009f5dd1.

- 2026-09-18T00:03:07+00:00: Recorded command exit 0; command argv SHA-256
  1996a21ccec16be94279c270b51716fcbbdac3c4b5b5b6beaecb20094a66a394.

- 2026-09-18T00:03:17+00:00: Recorded command exit 0; command argv SHA-256
  4ef5ef8e256f4e1610dda51ab8cf94e6c0716bdc1a5a51b34900db8961bdde89.

- 2026-09-18T00:03:29+00:00: Recorded command exit 0; command argv SHA-256
  adbfd17bd5a46378d72f07219f1688bced64b1502623c7575151571fe8da7dcf.

- 2026-09-18T00:03:39+00:00: Stage4 verified ext4 root layout state/jvm/tla2tools.jar and booted
  isolated 32 GiB no-NIC VM. Preflight proved /mnt/asb-data/tmp and /tmp both mode 1777, Java
  17.0.20 java.io.tmpdir=/mnt/asb-data/tmp, and transient D-Bus RC=0. TLC nevertheless failed closed
  at JFR startup; prior bounded output lost the leading exception. Added signed commit 629697197 to
  preserve first+last 1000-byte diagnostic excerpts; pushed PR branch exact head 24e24690b. No
  attestation accepted and no higher tiers started.

- 2026-09-18T00:04:41+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T00:04:42+00:00: Recorded command exit 0; command argv SHA-256
  6a9aa7ae59bff49171fd959f1aa379478b4e96b05ce7d809d2b887d63d6aa576.

- 2026-09-18T00:04:52+00:00: Recorded command exit 0; command argv SHA-256
  f56c10bf4a7593d507743d973d57df5776d0bbd766e8efc9164672763e718362.

- 2026-09-18T00:05:02+00:00: Recorded command exit 0; command argv SHA-256
  59dfd56774882cf2de83efd330dd999fa2fd9086deed2a61499c4b87da18fc3c.

- 2026-09-18T00:05:12+00:00: Recorded command exit 0; command argv SHA-256
  a5245be91e491107bf975d69364d9d2baeb03c28beebfa30646a7c6e862858e9.

- 2026-09-18T00:05:22+00:00: Recorded command exit 0; command argv SHA-256
  a0b18654f7d29ef466fb78fd54e8ea18a8e3729802bebb08a312e49550986c03.

- 2026-09-18T00:05:32+00:00: Recorded command exit 0; command argv SHA-256
  0d9259f53fb25dec0428786dcf826f0f7eea7bfed25bfabf42db9494f7ce770e.

- 2026-09-18T00:05:43+00:00: Recorded command exit 0; command argv SHA-256
  9fc3df07bca15863a747d730403d40fb663b6039e94b3857f305dfdc0d4b0213.

- 2026-09-18T00:05:59+00:00: Recorded command exit 0; command argv SHA-256
  4a7f13c6923da0055d533d4a7bb6b55b27e9a7b5469795e42f1931904878fa64.

- 2026-09-18T00:06:19+00:00: Recorded command exit 0; command argv SHA-256
  2a8470c333b2e5e9e17774be3e6a7c3fa98c4a746dc97e51375634a21baf5368.

- 2026-09-18T00:06:29+00:00: Recorded command exit 0; command argv SHA-256
  f5256d57c7ea8847245d46285fc6a664d117409008418475c0683bbe6bd45b22.

- 2026-09-18T00:06:39+00:00: Recorded command exit 0; command argv SHA-256
  95ed6f78ed0850669f1a8d3fec9d04fc80d3b72e31732f47cdf3e09e867edcea.

- 2026-09-18T00:08:03+00:00: Recorded command exit 0; command argv SHA-256
  f5720cc2edba85785085cca348ea867f17135fd1a08ba74c672a3098b9fe9db9.

- 2026-09-18T00:08:33+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T00:08:42+00:00: Stage5 exact-head fresh run proved effective
  TMPDIR/java.io.tmpdir=/mnt/asb-data/tmp, writable /tmp and D-Bus, and captured leading failure:
  java.lang.InternalError: Error loading java.security file. The pinned JDK tree contains absolute
  symlinks from jvm/conf/security/java.security to /etc/java-17-openjdk/security/java.security,
  absent in the clean guest. This is a self-contained runner-artifact defect, not a TLC/JFR model
  result. Next correction resolves JDK symlinks into the data image and verifies the security file
  before boot.

- 2026-09-18T00:08:52+00:00: Recorded command exit 0; command argv SHA-256
  361f1939e4a4d26a15bbb37c7e3f85517b5a702be509e3bd785fc99b1cde7cde.

- 2026-09-18T00:09:02+00:00: Recorded command exit 0; command argv SHA-256
  3df48bf1a185025274224dc89c07f7564694365a87cfaebf46c652cb1b0af4b8.

- 2026-09-18T00:09:21+00:00: Recorded command exit 0; command argv SHA-256
  48ab975c16d26e835cc5338e16674530802a45673d7e6655e4f1d4635dbfd8b4.

- 2026-09-18T00:09:32+00:00: Recorded command exit 1; command argv SHA-256
  e48eb6f989fef752c61cc208c76667a4b46cb698aec3e323682171304eb5e6c9.

- 2026-09-18T00:09:42+00:00: Recorded command exit 0; command argv SHA-256
  8b499d31b43f4942f7f44706b3688e1bb7b97206f8c0af866f399fc8298a32c4.

- 2026-09-18T00:09:53+00:00: Recorded command exit 0; command argv SHA-256
  41bcf8b90702be8f50488277b7496cac8bea8e7f0038432b7f9c2cfb62db6f69.

- 2026-09-18T00:10:07+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T00:10:07+00:00: Recorded command exit 0; command argv SHA-256
  c7d9426244434f418d8d1b8b317a85aae7da66aee5fd53239624cf6ff874b45d.

- 2026-09-18T00:10:18+00:00: Recorded command exit 0; command argv SHA-256
  04a01ad9ae87a7f44ee75677ad4132058604663ad0c088326908ddedeb81ef86.

- 2026-09-18T00:10:37+00:00: Recorded command exit 0; command argv SHA-256
  70e54d686cfffb8b1c2d183793e4c8fb1d3ae9c4266cadfe81e6ec8118978eb4.

- 2026-09-18T00:11:26+00:00: Recorded command exit 0; command argv SHA-256
  316499fbc6dda20fb10cc8b964855b8270714e62151c55530f875d0399f01350.

- 2026-09-18T00:12:26+00:00: Recorded command exit 1; command argv SHA-256
  5149a2d7424ac8c39d5fd7e60fc1598faab7174808ed7653845729de009f5dd1.

- 2026-09-18T00:12:36+00:00: Recorded command exit 0; command argv SHA-256
  5a07988433ca26467f7eb4b400452bf4e4eac90db7945e8ec7a3de4caf89b4ff.

- 2026-09-18T00:12:46+00:00: Recorded command exit 0; command argv SHA-256
  a39932657ac5991aa638533422db72a7f125f02915a65de327588a558fc646e2.

- 2026-09-18T00:12:58+00:00: Recorded command exit 0; command argv SHA-256
  adbfd17bd5a46378d72f07219f1688bced64b1502623c7575151571fe8da7dcf.

- 2026-09-18T00:13:09+00:00: Recorded command exit 0; command argv SHA-256
  5149a2d7424ac8c39d5fd7e60fc1598faab7174808ed7653845729de009f5dd1.

- 2026-09-18T00:13:22+00:00: Recorded command exit 0; command argv SHA-256
  33b9ac5b03b52c85ea1832b090a70e43ceaa7e6b1c3f0c2a97f76d902ab9e1b5.

- 2026-09-18T00:13:32+00:00: Recorded command exit 0; command argv SHA-256
  0d77f334a6d4d1ffccf79d355e52744be6e1cd6b7cff76bc1dbddbd00bcf4227.

- 2026-09-18T00:13:44+00:00: Recorded command exit 0; command argv SHA-256
  adbfd17bd5a46378d72f07219f1688bced64b1502623c7575151571fe8da7dcf.

- 2026-09-18T00:13:54+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T00:13:54+00:00: Stage6 proved self-contained resolved-JDK closure and reached
  attest.py, which correctly rejected the prior external evidence path /mnt/asb-data/evidence. Guest
  seed and focused test contract now bind attestation/results under the checked-out state root
  /mnt/asb-data/state/evidence. Focused tests pass 25/25. PR remote exact head is 1a3e37665; no
  attestation or merge yet.

- 2026-09-18T00:14:45+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T00:14:49+00:00: Recorded command exit 0; command argv SHA-256
  6a9aa7ae59bff49171fd959f1aa379478b4e96b05ce7d809d2b887d63d6aa576.

- 2026-09-18T00:15:05+00:00: Recorded command exit 0; command argv SHA-256
  04f9d2e535d8be803914d88e3d4629b5edb167957d4ce0ce322e7e4ca82413c1.

- 2026-09-18T00:15:15+00:00: Recorded command exit 0; command argv SHA-256
  626281051a0f22746876a4bfd668b0886f58e8017a80b1beeb413570000a29cd.

- 2026-09-18T00:15:26+00:00: Recorded command exit 0; command argv SHA-256
  9e0750cbaf90b943ed71b1c838bd9c1b0222cd340b14fa018eccb552398b7cf3.

- 2026-09-18T00:15:36+00:00: Recorded command exit 1; command argv SHA-256
  2bd86ffacd2d793c4c134bac9b52172d4b732732ad6e96cd3a623dec5e79def2.

- 2026-09-18T00:15:46+00:00: Recorded command exit 0; command argv SHA-256
  f9b0557da89cdaad16201bcaf173d971da806cd37771b368bd03e5c9c88095bf.

- 2026-09-18T00:15:56+00:00: Recorded command exit 0; command argv SHA-256
  41298500a72f24611c0458e0fe3d2134d75552e65d37665ec5a820f909b68f89.

- 2026-09-18T00:16:06+00:00: Recorded command exit 0; command argv SHA-256
  a05bd32b44c44801164c3d5cbd091dc1948d649516a9cb9afc02e5f978b31eaf.

- 2026-09-18T00:16:16+00:00: Recorded command exit 0; command argv SHA-256
  18d4313bc9dba56149a6e34a1f94d3f45dea4d9c6d120908581be2531e6c1688.

- 2026-09-18T00:16:26+00:00: Recorded command exit 0; command argv SHA-256
  ef7d58fd9d4f526569df05a69b52ecfbe4401faf4438aad8bd1c8e52f51f7760.

- 2026-09-18T00:16:36+00:00: Recorded command exit 0; command argv SHA-256
  c6ca8d48720ab954614bdad16f9f09ab49fcc8b47d3e0223a0eb38d19ba3d09f.

- 2026-09-18T00:16:46+00:00: Recorded command exit 1; command argv SHA-256
  02fc0c7eb827c5c6a1cd04f4e11d421369779953c011a53dff95062d6aa9c784.

- 2026-09-18T00:17:17+00:00: Recorded command exit 0; command argv SHA-256
  d0ab6952263951d715bb052a58c0db8f895b819713cc0b782dbd3e7eb54ad4f6.

- 2026-09-18T00:18:16+00:00: Recorded command exit 0; command argv SHA-256
  e3e44ad4ff17e2a0110d9e4b44fa1d4489b45e01cf2e8d82e8ae3b9da3cdfd8d.

- 2026-09-18T00:19:45+00:00: Recorded command exit 1; command argv SHA-256
  5149a2d7424ac8c39d5fd7e60fc1598faab7174808ed7653845729de009f5dd1.

- 2026-09-18T00:19:55+00:00: Recorded command exit 0; command argv SHA-256
  5a07988433ca26467f7eb4b400452bf4e4eac90db7945e8ec7a3de4caf89b4ff.

- 2026-09-18T00:20:05+00:00: Recorded command exit 0; command argv SHA-256
  e495fa9c28a41d92e2a75807165b59e5442f9fa2faaf7f20c8f7cc2066d52e13.

- 2026-09-18T00:20:17+00:00: Recorded command exit 0; command argv SHA-256
  adbfd17bd5a46378d72f07219f1688bced64b1502623c7575151571fe8da7dcf.

- 2026-09-18T00:20:27+00:00: Recorded command exit 0; command argv SHA-256
  5149a2d7424ac8c39d5fd7e60fc1598faab7174808ed7653845729de009f5dd1.

- 2026-09-18T00:20:37+00:00: Recorded command exit 0; command argv SHA-256
  39620c078f05b36a1ff6fe915cc5aa063a03424f9c5958919c6139026558cc04.

- 2026-09-18T00:20:47+00:00: Recorded command exit 0; command argv SHA-256
  109ca6a66d63a2cb7cf3c81f901f70c760d791c676a0d3a6025ae6317945fb51.

- 2026-09-18T00:20:59+00:00: Recorded command exit 0; command argv SHA-256
  adbfd17bd5a46378d72f07219f1688bced64b1502623c7575151571fe8da7dcf.

- 2026-09-18T00:21:41+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T00:21:42+00:00: Recorded command exit 0; command argv SHA-256
  6a9aa7ae59bff49171fd959f1aa379478b4e96b05ce7d809d2b887d63d6aa576.

- 2026-09-18T00:22:01+00:00: Recorded command exit 0; command argv SHA-256
  40bc888bfc41350f56939ac63345ebbe8b8421d69ed0b038356ff7d35a9df10c.

- 2026-09-18T00:22:11+00:00: Recorded command exit 0; command argv SHA-256
  b30e303256de3fecb6fae030578ce068be26693d3069d125b4044724d23414b2.

- 2026-09-18T00:22:21+00:00: Recorded command exit 0; command argv SHA-256
  c38506aedd4abeae688d35a047c9481577a48dc9f92227a6ec5050b6ce652993.

- 2026-09-18T00:22:31+00:00: Recorded command exit 1; command argv SHA-256
  896ea9c1e88d8ae78462bffffe49cf3f5c5558906f1318017896f9c71e19473f.

- 2026-09-18T00:22:41+00:00: Recorded command exit 0; command argv SHA-256
  058a0c3caacd3006a6883b735041e6aafbdb0d3138c8723d9312d90ffffa3c07.

- 2026-09-18T00:22:52+00:00: Recorded command exit 0; command argv SHA-256
  d1f77d9becae1b255fa7630e8d185fd7ad6f711c449c5d8b342187a79657acc5.

- 2026-09-18T00:23:01+00:00: Recorded command exit 0; command argv SHA-256
  020178e5782f439f7958cd0cd02ce25dab312ab7085f634f249196a38fa4fe93.

- 2026-09-18T00:23:12+00:00: Recorded command exit 0; command argv SHA-256
  c3f84f7999d71f9f4dcf02da7ae47bbdeddd7a5d7966afbea77e969ebb743ad0.

- 2026-09-18T00:23:22+00:00: Recorded command exit 0; command argv SHA-256
  29662ca2efe10f92357a9c9fef0bf48b9505d335a350a37e9c7b019efd632688.

- 2026-09-18T00:23:32+00:00: Recorded command exit 0; command argv SHA-256
  a44fbaa64a5920adb3cddbeb43b6e80d7373c625b54ad6e8f60f693cfc6be691.

- 2026-09-18T00:24:10+00:00: Stage8 build had an overlap race: mke2fs began before the JDK/JAR copy
  completed, and debugfs proved the resulting image contained only state/jvm but lacked root
  tla2tools.jar. No QEMU evidence accepted. Stage8 staging directory is now complete; rebuilding a
  fresh stage9 image sequentially and verifying image contents before boot.

- 2026-09-18T00:24:17+00:00: Recorded command exit 0; command argv SHA-256
  c2bd314225ecfdb96a4573ceba2352bc12b92f8b3dea0d437003557a91265a5e.

- 2026-09-18T00:25:13+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T00:25:13+00:00: Recorded command exit 0; command argv SHA-256
  1b52b70aa70f2138114b72341c8b0265f38b4598a847348517d4ada24990f97d.

- 2026-09-18T00:26:03+00:00: Recorded command exit 0; command argv SHA-256
  d4d662416d2bdb0eba74ee5ea1012167000b3fa1543d4892c39cd49b2d500b9a.

- 2026-09-18T00:27:18+00:00: Recorded command exit 1; command argv SHA-256
  5149a2d7424ac8c39d5fd7e60fc1598faab7174808ed7653845729de009f5dd1.

- 2026-09-18T00:27:40+00:00: Recorded command exit 0; command argv SHA-256
  5149a2d7424ac8c39d5fd7e60fc1598faab7174808ed7653845729de009f5dd1.

- 2026-09-18T00:27:50+00:00: Recorded command exit 1; command argv SHA-256
  d4bb16b48ebe0baa596afdece40fccca4214fc3fe375652e604c8d198b74e088.

- 2026-09-18T00:28:02+00:00: Recorded command exit 0; command argv SHA-256
  adbfd17bd5a46378d72f07219f1688bced64b1502623c7575151571fe8da7dcf.

- 2026-09-18T00:28:20+00:00: Recorded command exit 0; command argv SHA-256
  39620c078f05b36a1ff6fe915cc5aa063a03424f9c5958919c6139026558cc04.

- 2026-09-18T00:28:30+00:00: Recorded command exit 0; command argv SHA-256
  d4bb16b48ebe0baa596afdece40fccca4214fc3fe375652e604c8d198b74e088.

- 2026-09-18T00:28:41+00:00: Recorded command exit 0; command argv SHA-256
  adbfd17bd5a46378d72f07219f1688bced64b1502623c7575151571fe8da7dcf.

- 2026-09-18T00:29:20+00:00: Stage9 QEMU invocation accidentally used stale stage8 seed and
  therefore reproduced the obsolete /srv/data/projects evidence path; no result accepted. Corrected
  source is now signed commit 32f44345d and pushed; PR exact remote head is ca43179ea. Focused tests
  passed 25/25 before correction. Next run must regenerate seed from ca43179ea and verify
  attestation under /mnt/asb-data/state/evidence.

- 2026-09-18T00:30:21+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T00:30:22+00:00: Recorded command exit 0; command argv SHA-256
  6a9aa7ae59bff49171fd959f1aa379478b4e96b05ce7d809d2b887d63d6aa576.

- 2026-09-18T00:30:42+00:00: Recorded command exit 0; command argv SHA-256
  5e0050652c5a0c77484cbaa0b22349eab91c34656348a7f445752be8010afc40.

- 2026-09-18T00:30:52+00:00: Recorded command exit 0; command argv SHA-256
  97696f2701f0c867ca4c05889ccff9b8a6854ec6055d2c6ff8db006d09bbe918.

- 2026-09-18T00:31:03+00:00: Recorded command exit 0; command argv SHA-256
  2704227061c8d680b2ecbbe2c098fdd2f6c7a166b692e8d41d4e26320e11ea81.

- 2026-09-18T00:31:15+00:00: Recorded command exit 0; command argv SHA-256
  3c7785f79b61a729ef30fe2fc486b24bc4a4b4de890260283a53aef0248fb3f5.

- 2026-09-18T00:32:15+00:00: Recorded command exit 0; command argv SHA-256
  7a59fe412d00d37860c2cf638452943c0f8e9aad8f702b574685656a567242f8.

- 2026-09-18T00:32:59+00:00: Recorded command exit 0; command argv SHA-256
  d4c2ec98a505b1b1297e4d31c4ddda109cca20ac0adf256c4edbea9975e37375.

- 2026-09-18T00:33:12+00:00: Recorded command exit 0; command argv SHA-256
  1169e1946c609adc354e6c7de31e5ea81f1896aa624a2ab01e3cba9ff41fb590.

- 2026-09-18T00:33:33+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T00:33:45+00:00: CA seed run itself passed: PORTABLE_SMOKE_RC=0 and clean shutdown;
  extracted JSON attestation was schema-valid/status success but reported source commit 36c93fa1f
  because stage9 data disk contained stale checkout. Therefore this is explicitly non-qualifying
  stale-input evidence. Do not advance tiers. Rebuild the data image from ca43179ea and enforce
  attestation source-commit equality before acceptance.

- 2026-09-18T00:34:44+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T00:34:44+00:00: Recorded command exit 0; command argv SHA-256
  fe6eba1a043a83c1097514efa30283629c22e614ff559f404ce48918862c9294.

- 2026-09-18T00:34:54+00:00: Recorded command exit 0; command argv SHA-256
  cc04499f4c2f810c145296c508aeba68ecebcf1c78bcd92d2ff8796c80af1474.

- 2026-09-18T00:35:05+00:00: Recorded command exit 0; command argv SHA-256
  e7821d18538efa2fae00f72b1932f2a504f19d0fc57f8507c1f1785ad7b944fb.

- 2026-09-18T00:35:15+00:00: Recorded command exit 1; command argv SHA-256
  b26d5ec7c175d1c17eb45f9da8d2aa3538d6353f67d4d314bffaac8987c21cec.

- 2026-09-18T00:35:25+00:00: Recorded command exit 0; command argv SHA-256
  bfa5dbd8fd48343c5961988aedc4439f52937346a1c116d1b4fa2cb176475166.
