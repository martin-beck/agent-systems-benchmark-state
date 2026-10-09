---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-09T14:23:10+00:00",
  "depends_on": [
    "AR-1731"
  ],
  "id": "AR-1732",
  "next_action": "PR #529 merged as signed merge 942c7b110045823c942e362e5247b6ce15027ec5; monitor all exact-main workflows, then reconcile/doctor and accept/release AR-1732 with post-merge evidence.",
  "owner": "codex-asb-ar1732-run-sweep-20261009",
  "plan": "../plans/AR-1732-cli2key-run-sweep.md",
  "priority": "P1",
  "schema_version": 1,
  "spec_ref": "specs/AR-1732.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Make explicit cli2key selections executable through normal ASB run and sweep orchestration with bounded concurrency and typed live-development evidence.",
  "task_revision": 76,
  "title": "Integrate cli2key runs and sweeps",
  "updated_at": "2026-10-09T13:54:57+00:00",
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

- 2026-10-09T13:28:16+00:00: Recorded command exit 0; command argv SHA-256
  f9fa08abb21814f1889b7d9858c6a7058144e8b4bfe9394472b9d92b60edcfc7.

- 2026-10-09T13:28:36+00:00: Recorded command exit 0; command argv SHA-256
  dcb1d738bc1b5e07f635d521806ee90085e2e9b8ca7277e59153ab3f46f655d3.

- 2026-10-09T13:28:45+00:00: Recorded command exit 0; command argv SHA-256
  ad79496de53685a9f1764ddb222590ba14d0d280af3f650542afb698381539ab.

- 2026-10-09T13:28:58+00:00: Recorded command exit 0; command argv SHA-256
  a6a17ec3c5be1ae57bf2a84dd227c1146b069e0d5f1d88bca836cc88c7391fec.

- 2026-10-09T13:30:35+00:00: Heartbeat by codex-asb-ar1732-run-sweep-20261009.

- 2026-10-09T13:30:42+00:00: Recorded command exit 0; command argv SHA-256
  0444148d6e6443057d50176af193d199048298f8c6b1e8b3544f9abd06412489.

- 2026-10-09T13:31:02+00:00: Recorded command exit 0; command argv SHA-256
  251a640bac207088c0fe9ed5a39f99df5d5981a965b19ef8990e153b8f06fb85.

- 2026-10-09T13:31:15+00:00: Recorded command exit 1; command argv SHA-256
  218c479e0f9f2239b2fdb53c5c709fda6868c7ea959cf89145439e7ad67e2344.

- 2026-10-09T13:31:27+00:00: Recorded command exit 101; command argv SHA-256
  fc507d3ae59cda48d9510175c6aca98c4b4e6f8d694e59c809dee314cb1c47b9.

- 2026-10-09T13:31:42+00:00: Recorded command exit 0; command argv SHA-256
  ea8a0d1adc98676242bf8edbae53535664ebc1d69da387bb8ca89a60c58c1bd9.

- 2026-10-09T13:31:51+00:00: Recorded command exit 0; command argv SHA-256
  f9071f105ad1967cd0032d9f3d7a51c07396be5441b4dd8e6cf5083f7674acd3.

- 2026-10-09T13:32:06+00:00: Recorded command exit 0; command argv SHA-256
  a6a17ec3c5be1ae57bf2a84dd227c1146b069e0d5f1d88bca836cc88c7391fec.

- 2026-10-09T13:32:25+00:00: Recorded command exit 0; command argv SHA-256
  251a640bac207088c0fe9ed5a39f99df5d5981a965b19ef8990e153b8f06fb85.

- 2026-10-09T13:32:37+00:00: Recorded command exit 0; command argv SHA-256
  cc78cb678b873b620733c63f292aa358ed495f7d81f5ff34422e5953ecfa08ed.

- 2026-10-09T13:32:58+00:00: Recorded command exit 0; command argv SHA-256
  0444148d6e6443057d50176af193d199048298f8c6b1e8b3544f9abd06412489.

- 2026-10-09T13:33:08+00:00: Recorded command exit 0; command argv SHA-256
  ea8a0d1adc98676242bf8edbae53535664ebc1d69da387bb8ca89a60c58c1bd9.

- 2026-10-09T13:33:17+00:00: Recorded command exit 0; command argv SHA-256
  68e1b964f93a5b81a61fc0c723e544e8bb431aa615cf7a7d9a13df0bf968c98c.

- 2026-10-09T13:33:34+00:00: Recorded command exit 0; command argv SHA-256
  a6a17ec3c5be1ae57bf2a84dd227c1146b069e0d5f1d88bca836cc88c7391fec.

- 2026-10-09T13:33:46+00:00: Added explicit cli2key runtime-dispatch run regression and
  authority-required direct-live diagnostic; route remains fail-closed without runtime-issued
  sidecar launch. Full asb-cli suite passed.

- 2026-10-09T13:33:54+00:00: Recorded command exit 0; command argv SHA-256
  68beef4512b89d20f97d6806b8a51b6df6ea021b942ee26b427c3795b51c8391.

- 2026-10-09T13:34:08+00:00: Recorded command exit 8; command argv SHA-256
  f33195db5cf6dd94dd037bd0cda092aa3c7aa357a00bc14b1733cd777dc063de.

- 2026-10-09T13:43:43+00:00: Recorded command exit 1; command argv SHA-256
  a3ef9f768497a1a190ef668e19d3e7259064d528a71b237738f9035a20c34b8b.

- 2026-10-09T13:43:57+00:00: Recorded command exit 0; command argv SHA-256
  c7b9411de7f32ac0f06f3482e08da5f5352a570258da8faf2625cfdd519d0b99.

- 2026-10-09T13:44:14+00:00: Recorded command exit 0; command argv SHA-256
  79c912f9eb4733c94b135583ea5ddc24f953060746fc2fa72b27af549ac19d3e.

- 2026-10-09T13:44:27+00:00: Recorded command exit 0; command argv SHA-256
  20e3ad38672cdf391488622cb5bf2478371440316d88630cefcb1e6a1ab31190.

- 2026-10-09T13:44:42+00:00: merge_pr.py published the exact signed/DCO merge commit 942c7b1 to
  protected main. Exact-main workflows are running; Huawei source-header workflow already passed.

- 2026-10-09T13:45:09+00:00: Recorded command exit 0; command argv SHA-256
  fc178873c8046d55143b500df2a1a3c6dcb8939605e5697fc5e86ab6da517c1d.

- 2026-10-09T13:45:47+00:00: Recorded command exit 0; command argv SHA-256
  3e3ce62c0824377b5678b00ad5c2fec033eaf010e2a5609ca2d56cc57904bfea.

- 2026-10-09T13:46:23+00:00: Recorded command exit 0; command argv SHA-256
  3e3ce62c0824377b5678b00ad5c2fec033eaf010e2a5609ca2d56cc57904bfea.

- 2026-10-09T13:46:56+00:00: Recorded command exit 0; command argv SHA-256
  3e3ce62c0824377b5678b00ad5c2fec033eaf010e2a5609ca2d56cc57904bfea.

- 2026-10-09T13:47:28+00:00: Recorded command exit 0; command argv SHA-256
  3e3ce62c0824377b5678b00ad5c2fec033eaf010e2a5609ca2d56cc57904bfea.

- 2026-10-09T13:48:06+00:00: Recorded command exit 0; command argv SHA-256
  3e3ce62c0824377b5678b00ad5c2fec033eaf010e2a5609ca2d56cc57904bfea.

- 2026-10-09T13:48:13+00:00: Heartbeat by codex-asb-ar1732-run-sweep-20261009.

- 2026-10-09T13:49:07+00:00: Heartbeat by codex-asb-ar1732-run-sweep-20261009.

- 2026-10-09T13:50:26+00:00: Heartbeat by codex-asb-ar1732-run-sweep-20261009.

- 2026-10-09T13:51:44+00:00: Heartbeat by codex-asb-ar1732-run-sweep-20261009.

- 2026-10-09T13:53:10+00:00: Heartbeat by codex-asb-ar1732-run-sweep-20261009.

- 2026-10-09T13:54:14+00:00: Recorded command exit 0; command argv SHA-256
  b5e922c24daf5a8e091417ffc723ae374fb8f2a6f89df49308989519bbf6b902.

- 2026-10-09T13:54:28+00:00: Recorded command exit 0; command argv SHA-256
  e6757853c6620161fed474f5a06a8743bf69730a316d222da2d40587c13e3d86.

- 2026-10-09T13:54:39+00:00: Recorded command exit 0; command argv SHA-256
  efb0330cc7001f2fe97149f2a6034ed4fca0fdced9b931a4f8ef5ffbcc386bb1.

- 2026-10-09T13:54:46+00:00: Recorded command exit 0; command argv SHA-256
  2b6c17b597729f959b0af420f198523a044c95bf0ddf88620e6e0649e93876e0.

- 2026-10-09T13:54:57+00:00: Recorded command exit 0; command argv SHA-256
  eaf2472e4b0ec29bac3303a6d46474c99be3c0ab077feca87b1c3650d4745e53.
