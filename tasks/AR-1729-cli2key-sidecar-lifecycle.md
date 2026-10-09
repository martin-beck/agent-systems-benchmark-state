---
{
  "branch": "feature/ar-1729-cli2key-sidecar-lifecycle",
  "checkpoint_commit": "7eacb50d087ea42515d67a00488218bf0ba82880",
  "claim_expires": "2026-10-09T09:49:11+00:00",
  "depends_on": [
    "AR-1728"
  ],
  "id": "AR-1729",
  "next_action": "Promote after AR-1728; implement the runtime-owned sidecar lifecycle and hostile cleanup/privacy tests.",
  "owner": "codex-ar1729-cli2key-sidecar-20261009",
  "plan": "../plans/AR-1729-cli2key-sidecar-lifecycle.md",
  "priority": "P1",
  "schema_version": 1,
  "spec_ref": "specs/AR-1729.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Add a runtime-owned loopback sidecar lifecycle with a fresh per-invocation client key, private staging, bounded cleanup, and secret-safe evidence.",
  "task_revision": 35,
  "title": "Supervise cli2key sidecar and ephemeral key",
  "updated_at": "2026-10-09T07:49:41+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1729-cli2key-sidecar-lifecycle"
}
---

Implement a runtime-owned supervisor for the exact bridge selected by AR-1728.
Bind only to the loopback interface on a kernel-selected port and generate a fresh random
client key with at least 256 bits of entropy for each ASB run or sweep.

Keep key material out of argv, logs, reports, manifests, coordinator state, and
environment dumps. Prefer inherited descriptors; if the bridge requires files,
use an invocation-private 0700 root and 0600 no-follow file, then remove it on
all exits. Kill and reap the complete sidecar process group on success, error,
timeout, cancellation, or caller death. The sidecar alone receives upstream
egress; benchmark agents remain loopback-only.

- 2026-10-09T07:37:33+00:00: AR-1728 is done at exact main 30286af; dependencies verified

- 2026-10-09T07:37:37+00:00: Claimed by codex-ar1729-cli2key-sidecar-20261009.

- 2026-10-09T07:37:48+00:00: Recorded command exit 0; command argv SHA-256
  d3627636957d9729aaab7c75137920cd71b9e359719fc55f7cf73df1a4fb1060.

- 2026-10-09T07:38:22+00:00: Recorded command exit 0; command argv SHA-256
  e767a0c579bf67139c9d5a8832162484549e2af799dd88c0040fceead718e521.

- 2026-10-09T07:39:39+00:00: Recorded command exit 1; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-10-09T07:40:03+00:00: Recorded command exit 1; command argv SHA-256
  5679a63a49b7a64b28beabbe533d12c9abf67c8abe03ec2584e8f7d869fdcca7.

- 2026-10-09T07:40:26+00:00: Recorded command exit 0; command argv SHA-256
  f84505cfd3ac14288de90d5510d79f7ff3de6f83bcb26835cb65e0486b5997e8.

- 2026-10-09T07:40:47+00:00: Recorded command exit 101; command argv SHA-256
  297bf0426da2b3a34cc8d291742b5d89c6c71377df2a616c878604996ff250b5.

- 2026-10-09T07:41:26+00:00: Recorded command exit 101; command argv SHA-256
  2721fbf85b695554b8e2f46247222d604c4754ebb4ad0806f60b3639ca7ce9d2.

- 2026-10-09T07:41:47+00:00: Recorded command exit 0; command argv SHA-256
  f84505cfd3ac14288de90d5510d79f7ff3de6f83bcb26835cb65e0486b5997e8.

- 2026-10-09T07:42:10+00:00: Recorded command exit 0; command argv SHA-256
  2721fbf85b695554b8e2f46247222d604c4754ebb4ad0806f60b3639ca7ce9d2.

- 2026-10-09T07:42:33+00:00: Recorded command exit 0; command argv SHA-256
  f84505cfd3ac14288de90d5510d79f7ff3de6f83bcb26835cb65e0486b5997e8.

- 2026-10-09T07:42:55+00:00: Recorded command exit 0; command argv SHA-256
  2721fbf85b695554b8e2f46247222d604c4754ebb4ad0806f60b3639ca7ce9d2.

- 2026-10-09T07:43:12+00:00: Recorded command exit 0; command argv SHA-256
  f84505cfd3ac14288de90d5510d79f7ff3de6f83bcb26835cb65e0486b5997e8.

- 2026-10-09T07:43:35+00:00: Recorded command exit 0; command argv SHA-256
  2bedd4ab7e8269054fdcd1cc07aaeb03d27bc1db688a6ab561b84e0dc894fb40.

- 2026-10-09T07:43:49+00:00: Recorded command exit 0; command argv SHA-256
  5985d39c86433aedd5614c72e4caae4132b8b8c4811606d52bc014c2f70fbd36.

- 2026-10-09T07:44:11+00:00: Recorded command exit 0; command argv SHA-256
  ecf844ea83112f0d1f08251b07f82289b4e3cec7604495b0bfa35471176c8898.

- 2026-10-09T07:44:48+00:00: Recorded command exit 101; command argv SHA-256
  16f512d47ced960452d7c8c38998ebe14942ab65cb59c1ee8a4ac7b7f4e7ddaf.

- 2026-10-09T07:45:11+00:00: Recorded command exit 0; command argv SHA-256
  f84505cfd3ac14288de90d5510d79f7ff3de6f83bcb26835cb65e0486b5997e8.

- 2026-10-09T07:45:40+00:00: Recorded command exit 0; command argv SHA-256
  16f512d47ced960452d7c8c38998ebe14942ab65cb59c1ee8a4ac7b7f4e7ddaf.

- 2026-10-09T07:45:46+00:00: Recorded command exit 0; command argv SHA-256
  c0665c288cc151b4e81fd24eb882e6840537db636f6593aa66f506907c85bf67.

- 2026-10-09T07:46:08+00:00: Recorded command exit 0; command argv SHA-256
  97d4fd6bcd735d80d2f93d1619a1678f0428fa1595ec31962478f0c9648291ff.

- 2026-10-09T07:46:22+00:00: Recorded command exit 0; command argv SHA-256
  e34531e4f0f3f9ae5a30aa650aedf389f006724d7a5e68f332ce7b51f2b62105.

- 2026-10-09T07:46:47+00:00: Recorded command exit 0; command argv SHA-256
  29ef2d66d603b8437342b20db494256ff0a4cf72cb7db4ebaeee366ba92e973b.

- 2026-10-09T07:46:52+00:00: Heartbeat by codex-ar1729-cli2key-sidecar-20261009.

- 2026-10-09T07:47:14+00:00: Checkpointed source commit 7eacb50d087ea42515d67a00488218bf0ba82880.

- 2026-10-09T07:47:21+00:00: Recorded command exit 8; command argv SHA-256
  a4ed7ee757c5bba93d299db3f893952a5ca2930fa63b269bbc6261b936be5486.

- 2026-10-09T07:47:47+00:00: Recorded command exit 0; command argv SHA-256
  b097aa877aa7cbe8aea455ab4663da87bbec632bdba5f7c834cfa6a490159179.

- 2026-10-09T07:48:15+00:00: Heartbeat by codex-ar1729-cli2key-sidecar-20261009.

- 2026-10-09T07:48:19+00:00: Recorded command exit 8; command argv SHA-256
  a4ed7ee757c5bba93d299db3f893952a5ca2930fa63b269bbc6261b936be5486.

- 2026-10-09T07:48:46+00:00: Recorded command exit 8; command argv SHA-256
  a4ed7ee757c5bba93d299db3f893952a5ca2930fa63b269bbc6261b936be5486.

- 2026-10-09T07:49:11+00:00: Heartbeat by codex-ar1729-cli2key-sidecar-20261009.

- 2026-10-09T07:49:15+00:00: Recorded command exit 8; command argv SHA-256
  a4ed7ee757c5bba93d299db3f893952a5ca2930fa63b269bbc6261b936be5486.

- 2026-10-09T07:49:41+00:00: Recorded command exit 8; command argv SHA-256
  a4ed7ee757c5bba93d299db3f893952a5ca2930fa63b269bbc6261b936be5486.
