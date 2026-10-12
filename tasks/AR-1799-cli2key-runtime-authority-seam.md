---
{
  "branch": "feature/ar-1799-cli2key-runtime-authority-seam",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-12T07:26:11+00:00",
  "depends_on": [
    "AR-1729",
    "AR-1731"
  ],
  "id": "AR-1799",
  "next_action": "Repair factory/sidecar lifecycle binding and add direct CLI run/sweep plus hostile cancellation/timeout/crash/concurrent teardown tests; rerun full gates.",
  "observed_branch": "feature/ar-1799-cli2key-runtime-authority-seam",
  "observed_dirty": 0,
  "observed_head": "85173e15d2e17eab0d637110c8a4e57767589752",
  "owner": "ar1799-authority-luna56",
  "plan": "../plans/AR-1799-cli2key-runtime-authority-seam.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "contract-test",
    "evidence_digest": "",
    "evidence_ref": "",
    "spec_ref": "specs/AR-1799.json",
    "spec_revision": 1,
    "status": "pending"
  },
  "spec_ref": "specs/AR-1799.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Provide the missing runtime authority composition seam for cli2key live execution without exposing invocation keys.",
  "task_revision": 44,
  "title": "Add cli2key runtime authority composition seam",
  "updated_at": "2026-10-12T04:29:28+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1799-cli2key-runtime-authority-seam"
}
---

AR-1797 established that the existing CLI cannot compose the runtime-owned
`Cli2KeySidecar` with the opaque `LiveProviderAttempt`: the sidecar keeps the
invocation key private while the runtime factory constructors are intentionally
not public. Add the narrow authority-boundary seam needed to resolve only the
verified AR-1779 receipt, supervise one sidecar per run or bounded sweep, and
issue an opaque live attempt to the Codex adapter.

- 2026-10-12T02:07:38+00:00: Claimed by codex-ar1799-authority-luna56.

- 2026-10-12T02:07:46+00:00: Claimed after removing blocked AR-1797 from dependency list; AR-1797
  remains the blocked consumer integration task and retains successor evidence.

- 2026-10-12T02:07:46+00:00: Heartbeat by codex-ar1799-authority-luna56.

- 2026-10-12T04:09:56+00:00: Heartbeat by codex-ar1799-authority-luna56.

- 2026-10-12T04:10:16+00:00: Legacy claim owner has no live worker process. Releasing for
  reassignment; prior lease heartbeat and historical evidence preserved.

- 2026-10-12T04:11:27+00:00: Claimed by ar1799-authority-luna56.

- 2026-10-12T04:11:50+00:00: Recorded command exit 0; command argv SHA-256
  2cadf8b93784f2332f913a0010756a6f89279d776e4434fc0d7fe5cf1de23126.

- 2026-10-12T04:20:07+00:00: Implementation checkpoint: claim active; inspected cli2key sidecar,
  opaque LiveProviderAttempt, and CLI dispatch APIs. Next: add receipt-bound runtime bootstrap and
  hostile lifecycle tests.

- 2026-10-12T04:20:16+00:00: Recorded command exit 0; command argv SHA-256
  1e97a7300c473ca519c378499385430704cd1cce8671616968cb8e793166f3f7.

- 2026-10-12T04:20:19+00:00: Recorded command exit 0; command argv SHA-256
  3f206acd44a6d57e9eeda3871f98e277683f2c2eb2e053d80f73c0b8d0a517a2.

- 2026-10-12T04:20:24+00:00: Recorded command exit 0; command argv SHA-256
  a454ff7d52444589115f3aa16ab485662a83dcaaa05d2d04aebe9ef8263d57a6.

- 2026-10-12T04:20:31+00:00: Recorded command exit 0; command argv SHA-256
  3792709b07a059e681fea9fff4c896a0cc6ee4b090f01de00b714862e54bcbe7.

- 2026-10-12T04:20:34+00:00: Recorded command exit 0; command argv SHA-256
  ddb9837f5430c98c46116e8ae72e5faae1fa747cab6e999c3806194af703acf7.

- 2026-10-12T04:20:44+00:00: Recorded command exit 0; command argv SHA-256
  300dde80372ebb256cef99bed9a554a45f15e99a79c423c52fc8632189ce9a20.

- 2026-10-12T04:20:48+00:00: Recorded command exit 0; command argv SHA-256
  5bf55e557f487cd883db7d6ff5d558bed77c3a97d1415921267143a06fec00ff.

- 2026-10-12T04:21:23+00:00: Recorded command exit 0; command argv SHA-256
  5a0e106c9d7f12871812bae463d54756ada3eab68a8041ca4e0736744980eff8.

- 2026-10-12T04:21:29+00:00: Recorded command exit 101; command argv SHA-256
  297bf0426da2b3a34cc8d291742b5d89c6c71377df2a616c878604996ff250b5.

- 2026-10-12T04:21:44+00:00: Recorded command exit 101; command argv SHA-256
  9dc1be90e42281958342d9209775796374f16ae9dc1e27abb99d05221dff56e1.

- 2026-10-12T04:21:51+00:00: Focused cargo test exit 101 diagnosed: asb-runtime -D missing-docs
  rejected nine public Cli2KeyRuntimeReceipt fields. Repair: added rustdoc for every public field;
  rerun formatter and focused runtime tests.

- 2026-10-12T04:21:54+00:00: Recorded command exit 0; command argv SHA-256
  5a0e106c9d7f12871812bae463d54756ada3eab68a8041ca4e0736744980eff8.

- 2026-10-12T04:22:00+00:00: Recorded command exit 0; command argv SHA-256
  9dc1be90e42281958342d9209775796374f16ae9dc1e27abb99d05221dff56e1.

- 2026-10-12T04:22:11+00:00: Recorded command exit 0; command argv SHA-256
  5a0e106c9d7f12871812bae463d54756ada3eab68a8041ca4e0736744980eff8.

- 2026-10-12T04:22:15+00:00: Recorded command exit 0; command argv SHA-256
  9dc1be90e42281958342d9209775796374f16ae9dc1e27abb99d05221dff56e1.

- 2026-10-12T04:22:29+00:00: Recorded command exit 0; command argv SHA-256
  4b4f7f229e7d494b7b35b6d42fb92e0eea49194dc08c168fef56620397c0d57b.

- 2026-10-12T04:22:43+00:00: Recorded command exit 0; command argv SHA-256
  5a0e106c9d7f12871812bae463d54756ada3eab68a8041ca4e0736744980eff8.

- 2026-10-12T04:25:33+00:00: Recorded command exit 0; command argv SHA-256
  f8fec58749f1f3f99113a25e6517cecdc8daf4f467297c76bb229d7737f17cad.

- 2026-10-12T04:25:41+00:00: Recorded command exit 0; command argv SHA-256
  4366893e55b09c21b1c3ab847b2bdcabe14cc3f720946ecc8b2e4200ffd1e160.

- 2026-10-12T04:25:44+00:00: Recorded command exit 0; command argv SHA-256
  f3e6968cd5bc77b4bfc3a648c2454b4a0dfdd81cc16e6b97a11426ca34253b36.

- 2026-10-12T04:25:56+00:00: Implementation complete at signed/DCO head 85173e15. Added secret-free
  receipt validation (schema/generation/platform/digests), executable digest accessor/binding,
  runtime-owned Cli2KeyRuntimeAuthority with sidecar lifecycle and opaque LiveProviderAttempt
  factory, and hostile receipt substitution/stale/platform tests. Focused 7 tests and full make test
  (fmt/clippy/workspace tests/docs) pass.

- 2026-10-12T04:26:11+00:00: Heartbeat by ar1799-authority-luna56.

- 2026-10-12T04:28:43+00:00: Recorded command exit 0; command argv SHA-256
  227874da58115a0301d48285de084f3eac78189247d3fb539a4bb0568f9d69c9.

- 2026-10-12T04:28:47+00:00: Recorded command exit 0; command argv SHA-256
  30a0cc3bf50707920fcd81858a20397c49bb0f27d207ee905f0e0bb1c2f049ba.

- 2026-10-12T04:28:50+00:00: Recorded command exit 0; command argv SHA-256
  2c3224a5941805731e2da99b401c9018d214a23c19ad7304c558a811b7a84f9f.

- 2026-10-12T04:28:55+00:00: Recorded command exit 0; command argv SHA-256
  7d96ff09d5239dbaa5c044d97f3c667c3f6c977002e9d6598e6f2f593e98f0a0.

- 2026-10-12T04:29:03+00:00: Recorded command exit 0; command argv SHA-256
  fe90f2d2a1328e75108ee5e75ec96c0ae811451cd4abbba387097f8f9f89478f.

- 2026-10-12T04:29:07+00:00: Recorded command exit 0; command argv SHA-256
  05a42814091a3a9f9dccee9c190bb8b89877b7c5a3964fa3206ad70af9980bdf.

- 2026-10-12T04:29:18+00:00: Independent exact-head review of 85173e15: REJECT. Signature/DCO,
  diff-check, focused 7 tests, and full make test are green, but authority bootstrap accepts an
  arbitrary externally supplied LiveProviderAttemptFactory; attempts are not
  cryptographically/lifecycle-bound to the sidecar authority, and no direct CLI run/sweep wiring or
  hostile lifecycle tests prove cancellation/timeout/crash/concurrent teardown. Repair required
  before PR.

- 2026-10-12T04:29:21+00:00: Recorded command exit 0; command argv SHA-256
  963a94b587426477d361b7530c85947663b1d1c778840939ef96083ff47b35dd.

- 2026-10-12T04:29:25+00:00: Recorded command exit 0; command argv SHA-256
  6832d68bb623015e91bf136a0fe5b4ac049d3ab7dfd83f778bc372282fa592ee.

- 2026-10-12T04:29:28+00:00: Recorded command exit 0; command argv SHA-256
  28ed211e0ed96c29bcd2cecef1ccf0cda22d7038b4f6fd7efcc48feed24aa4d7.
