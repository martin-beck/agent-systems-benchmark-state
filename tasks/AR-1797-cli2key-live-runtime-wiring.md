---
{
  "branch": "feature/ar-1797-cli2key-live-runtime-wiring",
  "checkpoint_commit": "85cd643e01074c51b6833212bd8f88f53fc5c839",
  "claim_expires": "2026-10-12T06:10:09+00:00",
  "depends_on": [
    "AR-1729",
    "AR-1731",
    "AR-1732",
    "AR-1733",
    "AR-1779"
  ],
  "id": "AR-1797",
  "next_action": "Wire the verified project-local cli2key bridge into the runtime-owned sidecar launch path, then qualify fake and opt-in live benchmark execution without exposing credentials.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "ar1797_cli2key_repair_luna56",
  "plan": "../plans/AR-1797-cli2key-live-runtime-wiring.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "environmental",
    "evidence_digest": "",
    "evidence_ref": "",
    "spec_ref": "specs/AR-1797.json",
    "spec_revision": 1,
    "status": "pending"
  },
  "spec_ref": "specs/AR-1797.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Repair cli2key so an installed pinned bridge receives a runtime-issued sidecar launch and can execute a development ASB benchmark.",
  "task_revision": 33,
  "title": "Wire cli2key sidecar into live benchmark execution",
  "updated_at": "2026-10-12T05:29:05+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1797-cli2key-live-runtime-wiring"
}
---

AR-1729 supplies the sidecar lifecycle and AR-1731 through AR-1733 supply the
adapter, orchestration, and qualification contracts, but direct CLI live
execution still rejects cli2key because no runtime-issued sidecar launch reaches
the execution path. Repair that integration. After AR-1779 installs the pinned
bridge through `asb tool install cli2key`, resolve only its verified receipt,
start one runtime-owned loopback sidecar per run or bounded sweep, and provide
the resulting ephemeral launch only to the Codex Responses adapter.

The user-controlled Codex login remains outside ASB: do not read, copy, log, or
persist its authentication material. Do not route through Codex app-server,
fall back to OpenRouter, API keys, replay, or another provider, or describe the
development bridge as official OpenAI support. A credential-free fake is required
in CI; one opt-in user-authorized live development benchmark proves the complete
path and records only redacted provenance and typed outcome evidence.

- 2026-10-12T02:00:43+00:00: Dependencies AR-1729, AR-1731, AR-1732, AR-1733, and AR-1779 are done
  with passing acceptance; promote for implementation.

- 2026-10-12T02:00:44+00:00: Claimed by codex-ar1797-cli2key-repair-luna56.

- 2026-10-12T02:00:53+00:00: Recorded command exit 128; command argv SHA-256
  d6eff24e71dcade67a2eabad6a7010b78f29090f9795a649e3f1d8d973580c9b.

- 2026-10-12T02:01:11+00:00: Recorded command exit 0; command argv SHA-256
  8126156a61cec28600318ff12b7cef9d1e0f21420a55e996c085a9c1d2c0ba51.

- 2026-10-12T02:01:31+00:00: Recorded command exit 0; command argv SHA-256
  d4d121064219dc7626da449789752a7f5ea2d79dbfe07ee4ffb9550dcb55c556.

- 2026-10-12T02:02:20+00:00: Recorded command exit 0; command argv SHA-256
  d4d121064219dc7626da449789752a7f5ea2d79dbfe07ee4ffb9550dcb55c556.

- 2026-10-12T02:03:24+00:00: Heartbeat by codex-ar1797-cli2key-repair-luna56.

- 2026-10-12T02:03:24+00:00: Reproduced integration gap on exact protected-main merge 24cb72d9:
  execute_loaded_plan rejects cli2key when no runtime factory; production default factory is None.
  Existing Cli2KeySidecar owns generated key only in private staging and exposes endpoint plus key
  digest, while Codex adapter accepts only digest reference. No path currently resolves AR-1779
  receipt into a runtime-owned live attempt. Next: add runtime composition seam and hostile fake
  coverage; do not weaken no-fallback or key privacy.

- 2026-10-12T02:03:24+00:00: Checkpointed source commit f972aa003bc40d13aeb0b8abe8c14decd1017080.

- 2026-10-12T02:03:28+00:00: Recorded command exit 101; command argv SHA-256
  15eaaffb686b95b4dcf29404f8209ea4bdaa24f6150886e5d4b7615ccbf8d7cd.

- 2026-10-12T02:04:03+00:00: Recorded command exit 0; command argv SHA-256
  e12dd77ba8cb32218916e7b5da2cd778f4c3cf991548ae67e8646404962334f8.

- 2026-10-12T02:04:17+00:00: Heartbeat by codex-ar1797-cli2key-repair-luna56.

- 2026-10-12T02:04:18+00:00: Focused cli2key dispatch test rerun with explicit ASB manifest path and
  offline lock: cargo test -p asb-cli cli2key_run_dispatch_reaches_runtime_factory_without_fallback
  passed (1/1). Earlier recorded exit 101 was the invalid state-repo cwd invocation with no
  Cargo.toml, not a product test failure. No product files changed; integration gap remains as
  documented.

- 2026-10-12T02:04:18+00:00: Checkpointed source commit db1a776b04c5e93c87c99180a033deca06d5eea7.

- 2026-10-12T02:06:45+00:00: Released claim after durable blocker and successor AR-1799 creation.

- 2026-10-12T05:25:07+00:00: Dependencies AR-1729/1731/1732/1733/1779 are complete; AR-1799 runtime
  authority seam is now merged on main as e0e44a7d. Resume AR-1797 wiring qualification.

- 2026-10-12T05:25:09+00:00: Claimed by ar1797_cli2key_repair_luna56.

- 2026-10-12T05:25:42+00:00: Recorded command exit 0; command argv SHA-256
  d04aa803a9fcb854b247572f9b417fd1935a57ca978bb887d2e7c188e99db043.

- 2026-10-12T05:25:47+00:00: Recorded command exit 0; command argv SHA-256
  d04aa803a9fcb854b247572f9b417fd1935a57ca978bb887d2e7c188e99db043.

- 2026-10-12T05:26:09+00:00: Recorded command exit 0; command argv SHA-256
  b832bab19dcb37de05dfb7ee61d7c27c2ee176c07f0b9f98580db5cbf41548d2.

- 2026-10-12T05:27:06+00:00: Recorded command exit 0; command argv SHA-256
  d04aa803a9fcb854b247572f9b417fd1935a57ca978bb887d2e7c188e99db043.

- 2026-10-12T05:27:40+00:00: Recorded command exit 0; command argv SHA-256
  92257921799a8b9c0e3d52164840d74a387232173b448053283533c18c513e43.

- 2026-10-12T05:28:01+00:00: Recorded command exit 0; command argv SHA-256
  a1159e9df3670d549d04524532629f5477ceb7deec9b45e47e8c009506ecb2c8.

- 2026-10-12T05:28:08+00:00: Recorded command exit 0; command argv SHA-256
  36fdf9b8c88cd5e6114b46c7d725c504492ea3517a084288e8fa12fa3e0a508c.

- 2026-10-12T05:28:16+00:00: Recorded command exit 0; command argv SHA-256
  658c6e1a720016a71297db0a2dd20100f98fe64ae48a3d6dabbc812fff49bb9a.

- 2026-10-12T05:28:24+00:00: Recorded command exit 0; command argv SHA-256
  a66de1ec896a42ae6a261044b2630f2c9310e2a813e0cc0fe8ca0208402a92cd.

- 2026-10-12T05:28:31+00:00: Recorded command exit 0; command argv SHA-256
  10dba5a27c6244900cb53d652f52d8f764b84dcf0a981e37f9a7e67de108dbf0.

- 2026-10-12T05:28:38+00:00: Recorded command exit 0; command argv SHA-256
  a8cb42e201213856414b1691316ab99517012317740a380b3387c7304a17237f.

- 2026-10-12T05:28:47+00:00: Recorded command exit 0; command argv SHA-256
  15e6b55b0526eb3b6cde496ad83044f8be88f02e45421b7875f849200649f450.

- 2026-10-12T05:28:51+00:00: Recorded command exit 1; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-10-12T05:28:58+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-12T05:29:05+00:00: Checkpointed source commit 85cd643e01074c51b6833212bd8f88f53fc5c839.
