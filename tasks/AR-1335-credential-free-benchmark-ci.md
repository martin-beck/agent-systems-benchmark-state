---
{
  "branch": "feature/ar-1335-credential-free-benchmark-ci",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-27T08:11:24+00:00",
  "depends_on": [
    "AR-1333",
    "AR-1334"
  ],
  "id": "AR-1335",
  "next_action": "Add the required credential-free CI stage that exercises the complete benchmark path with loopback and synthetic doubles, no secrets, no egress and no network, keeping the 90% coverage floor.",
  "observed_branch": "feature/ar-1335-credential-free-benchmark-ci",
  "observed_dirty": 1,
  "observed_head": "fac11a22a93c1a075d7d528f2c6c20d426c66ba4",
  "owner": "ar1332-record-replay-luna56",
  "plan": "../plans/AR-1335.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Add the required credential-free CI stage for the complete benchmark path.",
  "task_revision": 32,
  "title": "Credential-free CI stage for the benchmark path",
  "updated_at": "2026-09-27T06:19:23+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1335-credential-free-benchmark-ci"
}
---

The benchmark path introduced by AR-1329 through AR-1334 must not degrade the
project's guarantee that CI runs without credentials, egress or network. This
AR adds a required CI stage that exercises the complete benchmark path end to
end against loopback and synthetic doubles: provider selection, live-mode
planning, execution with the deterministic double, capture, sealing, and strict
offline replay, plus the hostile negative cases. No secret, paid call, or
provider egress is permitted in any automated run; the unchanged 90% coverage
floor and all other native, formal, platform and privacy gates remain green.

## Current development and CI qualification boundary

The mandatory development and CI qualification path for this AR is a deterministic
local provider/LLM mock (LiteLLM-compatible where practical), including hostile
negative tests and offline replay where applicable. External/live OpenRouter or
other provider reachability is optional supplementary evidence only; it is never a
completion, dependency-readiness, or CI gate. Production egress policy, credential
non-disclosure, runtime-owned authority, namespace/relay attestation, cancellation
and teardown, and fail-closed denial of unapproved external traffic remain required
contracts. Existing live-provider dependency edges describe production integration
ordering only and must not be used to block local qualification or to claim external
reachability.

- 2026-09-27T06:11:11+00:00: AR-1333 supersession now explicitly points to completed AR-1456;
  AR-1334 is done. Promote credential-free benchmark CI stage.

- 2026-09-27T06:11:24+00:00: Claimed by ar1332-record-replay-luna56.

- 2026-09-27T06:11:36+00:00: Recorded command exit 0; command argv SHA-256
  ff6d1fa7a7185010f75fcfafe4bdc1bdd5b9804d8c2b3e7abdd8a1b96cd81c63.

- 2026-09-27T06:11:51+00:00: Recorded command exit 0; command argv SHA-256
  3263c5599be9960dc7234ca1bff3802a5cdd13e911bf07e76246794090949749.

- 2026-09-27T06:12:05+00:00: Recorded command exit 0; command argv SHA-256
  6840d2f0cea6f9cf6ffce81b9b1b74dcdddaff8701fc6cc1705c309033813254.

- 2026-09-27T06:12:20+00:00: Recorded command exit 0; command argv SHA-256
  5345cd4b5f66285dc80cddfe59c0a95475263f9ff88d25d2639fce3c300aa4b9.

- 2026-09-27T06:12:35+00:00: Recorded command exit 0; command argv SHA-256
  8e4e26708b15101f392b57e6f01ea86d56356873253cf4b3954629919ae8e0b1.

- 2026-09-27T06:12:54+00:00: Recorded command exit 0; command argv SHA-256
  d2c043202a90139076cc596c6fdab8558b60343eb7e299c46d415c5e60f9df06.

- 2026-09-27T06:13:08+00:00: Recorded command exit 0; command argv SHA-256
  034d567927df2bf8f970c3287e4929eeb87cc30802323b7dbabd0743063e07f7.

- 2026-09-27T06:13:23+00:00: Recorded command exit 0; command argv SHA-256
  4573850455519baa7b1a8e74b83596c19e52cfee9b8a9c6fc73cf20debba6a38.

- 2026-09-27T06:13:37+00:00: Recorded command exit 0; command argv SHA-256
  cd5f2a4087277489d9f32bc24b38289a82c3287b32d5ff036bf5f4587af72044.

- 2026-09-27T06:13:52+00:00: Recorded command exit 0; command argv SHA-256
  e9d30e627e99e3e9417a8a49be449551f07d0809ab73854294bf28c0a198c2b3.

- 2026-09-27T06:14:09+00:00: Recorded command exit 0; command argv SHA-256
  c63d7ad509aac541cd1290c74261294b56deddc6209a44e3d4a79f8cbfb6ce4c.

- 2026-09-27T06:14:24+00:00: Recorded command exit 0; command argv SHA-256
  058387a265bac86f571417f367f7dc129c4a670ef561af6a00673ce758940eff.

- 2026-09-27T06:15:21+00:00: Recorded command exit 0; command argv SHA-256
  13bc42b2516b2532990c094a4e03fd3e622c1626f1af62dc520108c3740ac530.

- 2026-09-27T06:15:36+00:00: Recorded command exit 0; command argv SHA-256
  45f841bdf293493eeb6df2ed1c1023390ccb5a7ce816fef75a79d32e4cd4c23d.

- 2026-09-27T06:15:51+00:00: Recorded command exit 0; command argv SHA-256
  dd979eb5383959f38dfaf1a6396fb8e59ab6290e95ccb5625b88c9df417c8a5d.

- 2026-09-27T06:16:06+00:00: Recorded command exit 0; command argv SHA-256
  1a78b65fb498e89d9f460db73881a7e8161f9c8a76918e72e82bbe392a7eb04a.

- 2026-09-27T06:16:29+00:00: Recorded command exit 0; command argv SHA-256
  6abb8dff03a6a04a3991e821d24feea384cf3bf374bd066f22bee07b078f9c0c.

- 2026-09-27T06:16:44+00:00: Recorded command exit 0; command argv SHA-256
  8624f885a44c637bf3f29c1a93e9bbfef8ee4fc905313f5ee1802ff4f8a55e4d.

- 2026-09-27T06:17:09+00:00: Recorded command exit 0; command argv SHA-256
  dd9d0c75acfef227e637a08863bdcca334fa0360566e2223c7b2db6a6621ae47.

- 2026-09-27T06:17:24+00:00: Recorded command exit 0; command argv SHA-256
  610fd0e51a55e551fa633b899617c1e259f6f497e981742492555ab9ebec136c.

- 2026-09-27T06:17:45+00:00: Recorded command exit 0; command argv SHA-256
  1a3993d3aec2e0332723dc6238ed68b33af9d6040bdf63a02b70926987cd524a.

- 2026-09-27T06:18:00+00:00: Recorded command exit 0; command argv SHA-256
  89cf4909d8938cff4c2eb67ad4e075eb379f9ac61cdf34885960919b6f2dc980.

- 2026-09-27T06:18:24+00:00: Recorded command exit 0; command argv SHA-256
  1d225f965f585ca15a58c2f7cc0703b4697fe85f96298169fe3b1402dda91919.

- 2026-09-27T06:18:39+00:00: Recorded command exit 0; command argv SHA-256
  6b4b51924e779b111a46d7f561b1772d8ec134bcbfd66a79ebfaee8723040df4.

- 2026-09-27T06:18:53+00:00: Recorded command exit 0; command argv SHA-256
  45f841bdf293493eeb6df2ed1c1023390ccb5a7ce816fef75a79d32e4cd4c23d.

- 2026-09-27T06:19:08+00:00: Recorded command exit 0; command argv SHA-256
  f5673972241fabd3f011e7d49744bc07b093ded6a5f69137dd2cd7efb57745cd.

- 2026-09-27T06:19:23+00:00: Recorded command exit 0; command argv SHA-256
  8421a44745674bc4f46eb5f1bfa0a2f385c985f4499303ec8b34ada104e7acb5.
