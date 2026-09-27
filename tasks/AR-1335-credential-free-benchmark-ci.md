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
  "task_revision": 18,
  "title": "Credential-free CI stage for the benchmark path",
  "updated_at": "2026-09-27T06:15:33+00:00",
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
