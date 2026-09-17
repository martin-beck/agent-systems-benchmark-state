---
{
  "branch": "feature/ar-1307-portable-tlc-runner-repair",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-18T01:21:30+00:00",
  "depends_on": [
    "AR-1302"
  ],
  "id": "AR-1307",
  "next_action": "Use a clean 32 GiB virtual root overlay (repair-v1 or run) after verifying pinned digest/provenance; rebuild actual guest_seed user-data with apt/package update disabled or offline-safe, retain early wait-online mask, then rerun exact b8db467ee portable-smoke and required/full tiers.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "codex-ar1307-runner-repair-20260918",
  "plan": "../plans/AR-1307.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Repair and publish a canonical, bounded portable TLC runner for AR-1293.",
  "task_revision": 79,
  "title": "Portable TLC runner repair and qualification",
  "updated_at": "2026-09-17T23:22:03+00:00",
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
