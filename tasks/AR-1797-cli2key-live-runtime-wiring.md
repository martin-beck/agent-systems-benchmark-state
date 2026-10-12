---
{
  "branch": "feature/ar-1797-cli2key-live-runtime-wiring",
  "checkpoint_commit": "f972aa003bc40d13aeb0b8abe8c14decd1017080",
  "claim_expires": "2026-10-12T04:03:24+00:00",
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
  "owner": "codex-ar1797-cli2key-repair-luna56",
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
  "task_revision": 10,
  "title": "Wire cli2key sidecar into live benchmark execution",
  "updated_at": "2026-10-12T02:03:24+00:00",
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
