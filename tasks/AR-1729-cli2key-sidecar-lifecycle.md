---
{
  "branch": "feature/ar-1729-cli2key-sidecar-lifecycle",
  "checkpoint_commit": "7eacb50d087ea42515d67a00488218bf0ba82880",
  "claim_expires": "2026-10-09T10:20:10+00:00",
  "depends_on": [
    "AR-1728"
  ],
  "id": "AR-1729",
  "next_action": "Construct and publish signed exact two-parent merge for PR #525; then verify post-merge workflows and close.",
  "owner": "codex-ar1729-cli2key-sidecar-20261009",
  "plan": "../plans/AR-1729-cli2key-sidecar-lifecycle.md",
  "priority": "P1",
  "schema_version": 1,
  "spec_ref": "specs/AR-1729.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Add a runtime-owned loopback sidecar lifecycle with a fresh per-invocation client key, private staging, bounded cleanup, and secret-safe evidence.",
  "task_revision": 119,
  "title": "Supervise cli2key sidecar and ephemeral key",
  "updated_at": "2026-10-09T08:21:03+00:00",
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

- 2026-10-09T07:50:09+00:00: Recorded command exit 8; command argv SHA-256
  a4ed7ee757c5bba93d299db3f893952a5ca2930fa63b269bbc6261b936be5486.

- 2026-10-09T07:50:34+00:00: Heartbeat by codex-ar1729-cli2key-sidecar-20261009.

- 2026-10-09T07:50:38+00:00: Recorded command exit 8; command argv SHA-256
  a4ed7ee757c5bba93d299db3f893952a5ca2930fa63b269bbc6261b936be5486.

- 2026-10-09T07:51:03+00:00: Recorded command exit 8; command argv SHA-256
  a4ed7ee757c5bba93d299db3f893952a5ca2930fa63b269bbc6261b936be5486.

- 2026-10-09T07:51:27+00:00: Recorded command exit 1; command argv SHA-256
  0ac74e7b444bb843f5dc9a99fe4c8b4967968e7fbc0b0ac15a3c7cc09158e7ec.

- 2026-10-09T07:51:53+00:00: Heartbeat by codex-ar1729-cli2key-sidecar-20261009.

- 2026-10-09T07:52:01+00:00: Implemented signed+DCO afca463 on
  feature/ar-1729-cli2key-sidecar-runtime. Added generated 256-bit invocation key fallback, local
  key absent/malformed/stale/valid handling, loopback readiness and executable pinning, private
  staging, env clearing, redacted digest receipt, process-group cleanup, and hostile tests. Focused
  runtime tests 177 passed/1 ignored; workspace clippy -D warnings passed.

- 2026-10-09T07:52:05+00:00: Heartbeat by codex-ar1729-cli2key-sidecar-20261009.

- 2026-10-09T07:52:12+00:00: Recorded command exit 8; command argv SHA-256
  a4ed7ee757c5bba93d299db3f893952a5ca2930fa63b269bbc6261b936be5486.

- 2026-10-09T07:52:39+00:00: Recorded command exit 8; command argv SHA-256
  a4ed7ee757c5bba93d299db3f893952a5ca2930fa63b269bbc6261b936be5486.

- 2026-10-09T07:53:09+00:00: Heartbeat by codex-ar1729-cli2key-sidecar-20261009.

- 2026-10-09T07:53:13+00:00: Recorded command exit 8; command argv SHA-256
  a4ed7ee757c5bba93d299db3f893952a5ca2930fa63b269bbc6261b936be5486.

- 2026-10-09T07:53:42+00:00: Recorded command exit 0; command argv SHA-256
  357d36406cc5123d7e431a3fc2b6e0981e7441d21ce916b0a626e082d96666e5.

- 2026-10-09T07:54:04+00:00: Recorded command exit 0; command argv SHA-256
  8b4a675907fc01aed605ab89ef4b45049497443a53829b721a23bfb9d6d43bf7.

- 2026-10-09T07:54:15+00:00: Recorded command exit 0; command argv SHA-256
  6a3d19dc67c8e76dd62ec052e1fb7e0ade9e801c078b9a74741deacbe33b17ff.

- 2026-10-09T07:54:25+00:00: Recorded command exit 0; command argv SHA-256
  6a3d19dc67c8e76dd62ec052e1fb7e0ade9e801c078b9a74741deacbe33b17ff.

- 2026-10-09T07:54:39+00:00: Recorded command exit 8; command argv SHA-256
  a4ed7ee757c5bba93d299db3f893952a5ca2930fa63b269bbc6261b936be5486.

- 2026-10-09T07:54:56+00:00: Heartbeat by codex-ar1729-cli2key-sidecar-20261009.

- 2026-10-09T07:55:05+00:00: Heartbeat by codex-ar1729-cli2key-sidecar-20261009.

- 2026-10-09T07:55:15+00:00: Recorded command exit 0; command argv SHA-256
  0606b9642c7413a52edeee341243d09012fc8ea124700504f724887113fa8360.

- 2026-10-09T07:55:38+00:00: Heartbeat by codex-ar1729-cli2key-sidecar-20261009.

- 2026-10-09T07:55:43+00:00: Recorded command exit 8; command argv SHA-256
  a4ed7ee757c5bba93d299db3f893952a5ca2930fa63b269bbc6261b936be5486.

- 2026-10-09T07:57:04+00:00: Heartbeat by codex-ar1729-cli2key-sidecar-20261009.

- 2026-10-09T07:57:07+00:00: Recorded command exit 0; command argv SHA-256
  a4ed7ee757c5bba93d299db3f893952a5ca2930fa63b269bbc6261b936be5486.

- 2026-10-09T07:57:34+00:00: Recorded command exit 0; command argv SHA-256
  06eb1c7a327ebb6114ece05019006fee20502cb0f6ebc13d52ffcdb261d71820.

- 2026-10-09T07:57:57+00:00: Recorded command exit 0; command argv SHA-256
  f84505cfd3ac14288de90d5510d79f7ff3de6f83bcb26835cb65e0486b5997e8.

- 2026-10-09T07:58:18+00:00: Recorded command exit 0; command argv SHA-256
  2721fbf85b695554b8e2f46247222d604c4754ebb4ad0806f60b3639ca7ce9d2.

- 2026-10-09T07:58:33+00:00: Recorded command exit 0; command argv SHA-256
  c0665c288cc151b4e81fd24eb882e6840537db636f6593aa66f506907c85bf67.

- 2026-10-09T07:58:39+00:00: Recorded command exit 0; command argv SHA-256
  c0665c288cc151b4e81fd24eb882e6840537db636f6593aa66f506907c85bf67.

- 2026-10-09T07:58:52+00:00: Recorded command exit 0; command argv SHA-256
  d1f187dff424896b1c1b1adcf55b406880675d7f9d687d6f7cea291af2f08796.

- 2026-10-09T07:58:58+00:00: Recorded command exit 0; command argv SHA-256
  d1f187dff424896b1c1b1adcf55b406880675d7f9d687d6f7cea291af2f08796.

- 2026-10-09T07:59:13+00:00: Recorded command exit 0; command argv SHA-256
  59664dca6d46dfc62c3bc9420839fa210bd605826662740fb8e07b157111702e.

- 2026-10-09T07:59:16+00:00: Recorded command exit 0; command argv SHA-256
  f0951ce6d4a0d15b7e64741c2e03094b7896eacae2717c794dcd3682e40c7d2b.

- 2026-10-09T07:59:27+00:00: Recorded command exit 0; command argv SHA-256
  f0951ce6d4a0d15b7e64741c2e03094b7896eacae2717c794dcd3682e40c7d2b.

- 2026-10-09T07:59:42+00:00: Recorded command exit 1; command argv SHA-256
  a4ed7ee757c5bba93d299db3f893952a5ca2930fa63b269bbc6261b936be5486.

- 2026-10-09T08:00:08+00:00: Recorded command exit 0; command argv SHA-256
  dfe7f0941bd6f0015d335de28bb9663511aba8c58dce58e37a482a6709ae14fa.

- 2026-10-09T08:00:16+00:00: Recorded command exit 0; command argv SHA-256
  456bed9b1717bd699c65a1219aa8b3ea1cd6d3b9a443c7896b850302a66f0c81.

- 2026-10-09T08:00:39+00:00: Recorded command exit 0; command argv SHA-256
  0501d9c0a3034ee765042090ce78438363237362ac523277426f21e063c0cd5b.

- 2026-10-09T08:00:48+00:00: Recorded command exit 0; command argv SHA-256
  0392f907579d5ff81d52482b139c1d957b2174fb23b1bed8f02ceea02dd69ae6.

- 2026-10-09T08:01:07+00:00: Recorded command exit 0; command argv SHA-256
  0bf4a3ba473178b1e9793edc3018fa39f3b355be964e6f6f568e6f03d96e111a.

- 2026-10-09T08:01:23+00:00: Recorded command exit 0; command argv SHA-256
  44e8d12516750d10c022b703d068352c643d9539b6c610a6c17e0955a5b46e0a.

- 2026-10-09T08:01:57+00:00: Heartbeat by codex-ar1729-cli2key-sidecar-20261009.

- 2026-10-09T08:02:03+00:00: Independent diff review found and repaired staging-root leak on
  set-permission/file-write failure; local-key read uses O_NOFOLLOW. Rebased signed+DCO
  implementation onto protected main 4f460a6, producing head 13da72b; force-with-lease publication
  succeeded. Prior CI failures were solely stale-base policy/provenance after PR #524 advanced main.

- 2026-10-09T08:02:15+00:00: Recorded command exit 8; command argv SHA-256
  a4ed7ee757c5bba93d299db3f893952a5ca2930fa63b269bbc6261b936be5486.

- 2026-10-09T08:02:49+00:00: Recorded command exit 8; command argv SHA-256
  a4ed7ee757c5bba93d299db3f893952a5ca2930fa63b269bbc6261b936be5486.

- 2026-10-09T08:03:12+00:00: Heartbeat by codex-ar1729-cli2key-sidecar-20261009.

- 2026-10-09T08:03:20+00:00: Recorded command exit 8; command argv SHA-256
  a4ed7ee757c5bba93d299db3f893952a5ca2930fa63b269bbc6261b936be5486.

- 2026-10-09T08:03:45+00:00: Recorded command exit 8; command argv SHA-256
  a4ed7ee757c5bba93d299db3f893952a5ca2930fa63b269bbc6261b936be5486.

- 2026-10-09T08:04:13+00:00: Recorded command exit 8; command argv SHA-256
  a4ed7ee757c5bba93d299db3f893952a5ca2930fa63b269bbc6261b936be5486.

- 2026-10-09T08:04:35+00:00: Heartbeat by codex-ar1729-cli2key-sidecar-20261009.

- 2026-10-09T08:04:39+00:00: Recorded command exit 8; command argv SHA-256
  a4ed7ee757c5bba93d299db3f893952a5ca2930fa63b269bbc6261b936be5486.

- 2026-10-09T08:05:03+00:00: Recorded command exit 8; command argv SHA-256
  a4ed7ee757c5bba93d299db3f893952a5ca2930fa63b269bbc6261b936be5486.

- 2026-10-09T08:05:29+00:00: Recorded command exit 8; command argv SHA-256
  a4ed7ee757c5bba93d299db3f893952a5ca2930fa63b269bbc6261b936be5486.

- 2026-10-09T08:05:32+00:00: Heartbeat by codex-ar1729-cli2key-sidecar-20261009.

- 2026-10-09T08:11:40+00:00: Heartbeat by codex-ar1729-cli2key-sidecar-20261009.

- 2026-10-09T08:11:43+00:00: Recorded command exit 0; command argv SHA-256
  805b9bef30f8e61ad0b750768cbff24c6bba29aa6738cfa031ac37c99d95af35.

- 2026-10-09T08:12:10+00:00: Recorded command exit 0; command argv SHA-256
  dfe7f0941bd6f0015d335de28bb9663511aba8c58dce58e37a482a6709ae14fa.

- 2026-10-09T08:12:14+00:00: Recorded command exit 0; command argv SHA-256
  dfe7f0941bd6f0015d335de28bb9663511aba8c58dce58e37a482a6709ae14fa.

- 2026-10-09T08:12:36+00:00: Recorded command exit 0; command argv SHA-256
  286c7d1895f9a32c25ae33c124a4e354a328c8fb5606fa31fb64acc518ef14a2.

- 2026-10-09T08:13:05+00:00: Independent full diff review completed at reviewed head 13da72b/tree
  95febde8: no remaining findings. Verified generated-key fallback and hostile key matrix, no-follow
  local key opening, loopback-only readiness, pinned executable, no secret argv/environment/receipt,
  staging failure cleanup, group teardown/reap, focused tests, signatures, DCO, and all required
  exact-head checks green.

- 2026-10-09T08:13:13+00:00: Recorded command exit 0; command argv SHA-256
  8f7a718aeffc8f07a4c0d45e46c678b93d28ddc2e43f33b178478b467113e562.

- 2026-10-09T08:13:43+00:00: Recorded command exit 1; command argv SHA-256
  4cfe68dba61ab0983ada554a77fe3a0285279ef349141b20b01e980453bf482c.

- 2026-10-09T08:14:17+00:00: Recorded command exit 0; command argv SHA-256
  64e9691a3d827d235c3bc73fee1c20fdd151734caa9d3782be26f9475abf8cbc.

- 2026-10-09T08:14:46+00:00: Recorded command exit 0; command argv SHA-256
  7a8686bb2beb7215bfcc64085aa95ebfc4be7004550d9526e26b6d9f1b24b097.

- 2026-10-09T08:15:13+00:00: Recorded command exit 0; command argv SHA-256
  5f49e9caed68b41d53934d60d3e3efd1e38e39a5e8931e0cec1b46eba1f8f18e.

- 2026-10-09T08:15:40+00:00: Recorded command exit 0; command argv SHA-256
  c4eaab702ff7147c9cbf2cb1309c8ca6141f972179fdb9beb2a6469c986169a4.

- 2026-10-09T08:15:48+00:00: Recorded command exit 0; command argv SHA-256
  306d3d96fc5e63fd4de4dec55d24c2097b0025d0ff34a74887d25ede56f06c93.

- 2026-10-09T08:16:10+00:00: Heartbeat by codex-ar1729-cli2key-sidecar-20261009.

- 2026-10-09T08:16:14+00:00: Recorded command exit 0; command argv SHA-256
  306d3d96fc5e63fd4de4dec55d24c2097b0025d0ff34a74887d25ede56f06c93.

- 2026-10-09T08:16:17+00:00: Heartbeat by codex-ar1729-cli2key-sidecar-20261009.

- 2026-10-09T08:16:38+00:00: Recorded command exit 0; command argv SHA-256
  306d3d96fc5e63fd4de4dec55d24c2097b0025d0ff34a74887d25ede56f06c93.

- 2026-10-09T08:17:04+00:00: Recorded command exit 0; command argv SHA-256
  306d3d96fc5e63fd4de4dec55d24c2097b0025d0ff34a74887d25ede56f06c93.

- 2026-10-09T08:17:28+00:00: Heartbeat by codex-ar1729-cli2key-sidecar-20261009.

- 2026-10-09T08:17:32+00:00: Recorded command exit 0; command argv SHA-256
  306d3d96fc5e63fd4de4dec55d24c2097b0025d0ff34a74887d25ede56f06c93.

- 2026-10-09T08:17:53+00:00: Recorded command exit 0; command argv SHA-256
  306d3d96fc5e63fd4de4dec55d24c2097b0025d0ff34a74887d25ede56f06c93.

- 2026-10-09T08:18:18+00:00: Recorded command exit 0; command argv SHA-256
  306d3d96fc5e63fd4de4dec55d24c2097b0025d0ff34a74887d25ede56f06c93.

- 2026-10-09T08:18:39+00:00: Heartbeat by codex-ar1729-cli2key-sidecar-20261009.

- 2026-10-09T08:18:42+00:00: Recorded command exit 0; command argv SHA-256
  306d3d96fc5e63fd4de4dec55d24c2097b0025d0ff34a74887d25ede56f06c93.

- 2026-10-09T08:19:12+00:00: Recorded command exit 0; command argv SHA-256
  306d3d96fc5e63fd4de4dec55d24c2097b0025d0ff34a74887d25ede56f06c93.

- 2026-10-09T08:19:43+00:00: Recorded command exit 0; command argv SHA-256
  306d3d96fc5e63fd4de4dec55d24c2097b0025d0ff34a74887d25ede56f06c93.

- 2026-10-09T08:20:10+00:00: Heartbeat by codex-ar1729-cli2key-sidecar-20261009.

- 2026-10-09T08:20:13+00:00: Recorded command exit 0; command argv SHA-256
  306d3d96fc5e63fd4de4dec55d24c2097b0025d0ff34a74887d25ede56f06c93.

- 2026-10-09T08:20:41+00:00: Recorded command exit 0; command argv SHA-256
  306d3d96fc5e63fd4de4dec55d24c2097b0025d0ff34a74887d25ede56f06c93.

- 2026-10-09T08:21:03+00:00: Recorded command exit 0; command argv SHA-256
  306d3d96fc5e63fd4de4dec55d24c2097b0025d0ff34a74887d25ede56f06c93.
