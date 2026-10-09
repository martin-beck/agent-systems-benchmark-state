---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-09T15:16:24+00:00",
  "depends_on": [
    "AR-1731"
  ],
  "id": "AR-1732",
  "next_action": "Implementation 75826b7955b6afbcdf45aa4e8beba2d5b7af56 is signed+DCO; run independent review, push PR, exact-head CI, merge, and post-merge qualification.",
  "owner": "codex-asb-ar1732-run-sweep-20261009",
  "plan": "../plans/AR-1732-cli2key-run-sweep.md",
  "priority": "P1",
  "schema_version": 1,
  "spec_ref": "specs/AR-1732.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Make explicit cli2key selections executable through normal ASB run and sweep orchestration with bounded concurrency and typed live-development evidence.",
  "task_revision": 34,
  "title": "Integrate cli2key runs and sweeps",
  "updated_at": "2026-10-09T13:28:08+00:00",
  "worktree_key": ""
}
---

Expose explicit `cli2key` selection through the ordinary `run` and `sweep`
paths. One supervised sidecar lifetime belongs to one run or complete bounded
sweep, with per-attempt capability binding and deterministic teardown. Enforce
the configured sweep concurrency, distinguish proxy queue/transport overhead
from agent latency, and emit typed failures for auth expiry, wrong key, rate
limit, model drift, sidecar crash, timeout, and cancellation. Evidence must say
`development_remote_live` (or an equally explicit reviewed label) and cannot
serve as production or official-provider qualification.

- 2026-10-09T13:16:21+00:00: AR-1731 is durably accepted/released with hosted post-merge receipt;
  promote cli2key run/sweep integration.

- 2026-10-09T13:16:24+00:00: Claimed by codex-asb-ar1732-run-sweep-20261009.

- 2026-10-09T13:17:19+00:00: Recorded command exit 0; command argv SHA-256
  af611799c7b6337f91fe45785f8cb2fca85f1c51ecb17ab3ad04fd5fd3224570.

- 2026-10-09T13:19:46+00:00: Recorded command exit 0; command argv SHA-256
  8d52ce3c646f21c92dddf2ef27605bb6a42ded558ac85c4900dfc0401b622831.

- 2026-10-09T13:20:21+00:00: Recorded command exit 0; command argv SHA-256
  b9f27106cc4972fedb6056e7edaa162d08d8f9d8c3578cfa26292a845311a3be.

- 2026-10-09T13:20:40+00:00: Recorded command exit 1; command argv SHA-256
  e7804766a2b92155866880d4e5177edf2cdd7ddf05c5edc61a521c1f039034e7.

- 2026-10-09T13:20:50+00:00: Recorded command exit 1; command argv SHA-256
  a54ff4ad212cff333342e54921ec36b733dc79d3734f28c5952635dd805b31e2.

- 2026-10-09T13:21:01+00:00: Recorded command exit 1; command argv SHA-256
  284985b41507377dc2fd5d1c8dc3568561dc173a3faa3bced7ec36db7a4ec959.

- 2026-10-09T13:21:15+00:00: Recorded command exit 0; command argv SHA-256
  251a640bac207088c0fe9ed5a39f99df5d5981a965b19ef8990e153b8f06fb85.

- 2026-10-09T13:21:33+00:00: Recorded command exit 101; command argv SHA-256
  0444148d6e6443057d50176af193d199048298f8c6b1e8b3544f9abd06412489.

- 2026-10-09T13:22:12+00:00: Recorded command exit 0; command argv SHA-256
  251a640bac207088c0fe9ed5a39f99df5d5981a965b19ef8990e153b8f06fb85.

- 2026-10-09T13:22:24+00:00: Recorded command exit 1; command argv SHA-256
  6b14504ef5186a20a9d04d15f265819a8b670a86d6e525820ad821ba428d2b90.

- 2026-10-09T13:22:37+00:00: Recorded command exit 0; command argv SHA-256
  03f5fbe1dc8a57731279b2d2b3d4fe8d0bb86bb80bfc0655d8a90011425a12b9.

- 2026-10-09T13:22:48+00:00: Recorded command exit 0; command argv SHA-256
  b9193cd81752d5fc2cb0a8ee377f7d420c0406420283f20ac9634de3101fe040.

- 2026-10-09T13:23:05+00:00: Recorded command exit 101; command argv SHA-256
  0444148d6e6443057d50176af193d199048298f8c6b1e8b3544f9abd06412489.

- 2026-10-09T13:23:19+00:00: Recorded command exit 0; command argv SHA-256
  fc507d3ae59cda48d9510175c6aca98c4b4e6f8d694e59c809dee314cb1c47b9.

- 2026-10-09T13:23:30+00:00: Recorded command exit 0; command argv SHA-256
  ea8a0d1adc98676242bf8edbae53535664ebc1d69da387bb8ca89a60c58c1bd9.

- 2026-10-09T13:23:37+00:00: Recorded command exit 0; command argv SHA-256
  425e913ecdcfec8ca15823c7a9cb163c116f1ec07be6f9b7a80b5d4e8ce6935c.

- 2026-10-09T13:23:56+00:00: Bound fresh provider launch records to each scheduler attempt, retained
  bounded typed live-provider failure evidence, and updated CLI provenance digest. Full asb-cli
  tests pass.

- 2026-10-09T13:24:29+00:00: Recorded command exit 0; command argv SHA-256
  32996933c19eb428ea42f17fffee8266d57e3a8e6b912abe660c00a1f22526b7.

- 2026-10-09T13:24:42+00:00: Recorded command exit 0; command argv SHA-256
  026cb9c25dc6b389b46bdfe0268b235155f9c19045eae426178d7f72bc4bb0de.

- 2026-10-09T13:24:54+00:00: Recorded command exit 8; command argv SHA-256
  f33195db5cf6dd94dd037bd0cda092aa3c7aa357a00bc14b1733cd777dc063de.

- 2026-10-09T13:25:08+00:00: Recorded command exit 0; command argv SHA-256
  ab97b915f03520dc78cbea53dbee7057c0eec58d1a40c6a5302c2b3992b31adc.

- 2026-10-09T13:25:53+00:00: Recorded command exit 1; command argv SHA-256
  251a640bac207088c0fe9ed5a39f99df5d5981a965b19ef8990e153b8f06fb85.

- 2026-10-09T13:26:10+00:00: Recorded command exit 0; command argv SHA-256
  251a640bac207088c0fe9ed5a39f99df5d5981a965b19ef8990e153b8f06fb85.

- 2026-10-09T13:26:23+00:00: Recorded command exit 101; command argv SHA-256
  8d52ce3c646f21c92dddf2ef27605bb6a42ded558ac85c4900dfc0401b622831.

- 2026-10-09T13:26:37+00:00: Recorded command exit 0; command argv SHA-256
  251a640bac207088c0fe9ed5a39f99df5d5981a965b19ef8990e153b8f06fb85.

- 2026-10-09T13:26:46+00:00: Recorded command exit 0; command argv SHA-256
  8d52ce3c646f21c92dddf2ef27605bb6a42ded558ac85c4900dfc0401b622831.

- 2026-10-09T13:27:07+00:00: Recorded command exit 0; command argv SHA-256
  251a640bac207088c0fe9ed5a39f99df5d5981a965b19ef8990e153b8f06fb85.

- 2026-10-09T13:27:22+00:00: Recorded command exit 101; command argv SHA-256
  f9fa08abb21814f1889b7d9858c6a7058144e8b4bfe9394472b9d92b60edcfc7.

- 2026-10-09T13:27:40+00:00: Recorded command exit 0; command argv SHA-256
  251a640bac207088c0fe9ed5a39f99df5d5981a965b19ef8990e153b8f06fb85.

- 2026-10-09T13:27:50+00:00: Recorded command exit 101; command argv SHA-256
  f9fa08abb21814f1889b7d9858c6a7058144e8b4bfe9394472b9d92b60edcfc7.

- 2026-10-09T13:28:08+00:00: Recorded command exit 0; command argv SHA-256
  251a640bac207088c0fe9ed5a39f99df5d5981a965b19ef8990e153b8f06fb85.
