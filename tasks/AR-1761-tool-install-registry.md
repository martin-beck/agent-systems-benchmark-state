---
{
  "branch": "feature/ar-1761-tool-install-registry",
  "checkpoint_commit": "c34a3d6b52b009d62a513bae6713e748b9dbd1fb",
  "claim_expires": "2026-10-09T17:41:04+00:00",
  "depends_on": [
    "AR-1759",
    "AR-1760"
  ],
  "id": "AR-1761",
  "next_action": "Retry exact full format and Clippy commands with product manifest path before the rustfmt separator.",
  "observed_branch": "feature/ar-1761-tool-install-registry",
  "observed_dirty": 0,
  "observed_head": "8b4a2bf60c4f1e8bb30363979a3c50f3a7c934b3",
  "owner": "codex-asb-ar1761-tool-install-20261009",
  "plan": "../plans/AR-1761-tool-install-registry.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "contract-test",
    "evidence_digest": "",
    "evidence_ref": "",
    "spec_ref": "specs/AR-1761.json",
    "spec_revision": 1,
    "status": "pending"
  },
  "spec_ref": "specs/AR-1761.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Install supported external ASB tools into a user/project-local root and persist validated records.",
  "task_revision": 33,
  "title": "ASB external-tool installer and registry",
  "updated_at": "2026-10-09T15:50:07+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1761-tool-install-registry"
}
---

Add a clear `asb tool install <id> --kind agent|harness|benchmark|workload|support`
command (with source/version/project and `--json` options) backed by an
extensible, bounded installer registry. It must support the external tools ASB
actually uses, install without root into a user/project-local location, record
the executable/root/source/version/platform/digest/capabilities in the project
config, and give an explicit unsupported-tool diagnostic rather than executing
arbitrary shell. Add status/list/remove or repair behavior only where needed
for idempotence; never store API keys or tokens.

- 2026-10-09T15:40:58+00:00: dependencies AR-1759 and AR-1760 verified accepted/released;
  implementation ready

- 2026-10-09T15:41:04+00:00: Claimed by codex-asb-ar1761-tool-install-20261009.

- 2026-10-09T15:41:15+00:00: Recorded command exit 0; command argv SHA-256
  8781f7f86432da71cf00304d47062d61aa5ed8ccbac43c32fffb341be9c007fd.

- 2026-10-09T15:41:35+00:00: Recorded command exit 0; command argv SHA-256
  c18ed43a4423686964d2b9e91943401cda7e5651ce092cd08b41811163bc1613.

- 2026-10-09T15:41:48+00:00: Recorded command exit 0; command argv SHA-256
  ec48e1d504dbb949df2606165a2406335cb4529dc7cbd9a666569760fe08df68.

- 2026-10-09T15:43:33+00:00: Recorded command exit 1; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-09T15:43:47+00:00: Recorded command exit 0; command argv SHA-256
  a917c5c96bb0f888caae50bea885d24f8c7158927e33da92e7b5c2eb9571981b.

- 2026-10-09T15:43:57+00:00: Recorded command exit 101; command argv SHA-256
  a37d35e290b63ddfe8627f9bdb0474ef6d3f2654ade91f05cd9a55c3a713fceb.

- 2026-10-09T15:44:27+00:00: Recorded command exit 0; command argv SHA-256
  081af90c8024d255817953c561fd64d176b2fb9188b0198239fe3000831623e8.

- 2026-10-09T15:44:46+00:00: Recorded bounded retry: initial handoffctl cargo check invocation
  failed with exit 101 because wrapper cwd is the state repository and no Cargo.toml was present.
  Repaired by invoking cargo with the product worktree manifest path; cargo check --locked
  --workspace then passed.

- 2026-10-09T15:45:17+00:00: Recorded command exit 0; command argv SHA-256
  e01e5d95dc6ad658cdb3d81caaf78261e9db1f1e205dec5cad0059c1304ba2f1.

- 2026-10-09T15:45:41+00:00: Recorded command exit 0; command argv SHA-256
  a917c5c96bb0f888caae50bea885d24f8c7158927e33da92e7b5c2eb9571981b.

- 2026-10-09T15:45:53+00:00: Recorded command exit 101; command argv SHA-256
  2607424c3654ceee26fa86e853d746acc9c602695281098ece205d223d115425.

- 2026-10-09T15:46:19+00:00: Recorded command exit 0; command argv SHA-256
  1de8f9ad957f9d922fc8cf742b621ec607aa4aa6d2a7b12e7f0ad69c06e24dd8.

- 2026-10-09T15:46:33+00:00: Focused tool tests first failed with exit 101 because the idempotence
  comparison included the generated record path/kind capability representation differently from the
  persisted record. Diagnosis is in progress; no publication was attempted.

- 2026-10-09T15:46:39+00:00: Recorded command exit 0; command argv SHA-256
  c08b6829368d7782d20a983c1344b00955db57c4e510ac63f32a16ec1bc08693.

- 2026-10-09T15:47:01+00:00: Recorded command exit 0; command argv SHA-256
  a917c5c96bb0f888caae50bea885d24f8c7158927e33da92e7b5c2eb9571981b.

- 2026-10-09T15:47:17+00:00: Recorded command exit 0; command argv SHA-256
  2607424c3654ceee26fa86e853d746acc9c602695281098ece205d223d115425.

- 2026-10-09T15:47:37+00:00: Repaired exit-101 focused test failure: ProjectConfigV1 source
  validation rejected the documented fixture:// source vocabulary. Extended the closed source
  validator to allow fixture:// only; unsupported network schemes and symlink/local-source checks
  remain fail-closed. Focused tool install/list/status/remove tests now pass (5/5).

- 2026-10-09T15:48:11+00:00: Recorded command exit 0; command argv SHA-256
  a917c5c96bb0f888caae50bea885d24f8c7158927e33da92e7b5c2eb9571981b.

- 2026-10-09T15:48:26+00:00: Recorded command exit 0; command argv SHA-256
  2607424c3654ceee26fa86e853d746acc9c602695281098ece205d223d115425.

- 2026-10-09T15:48:47+00:00: Recorded command exit 0; command argv SHA-256
  a917c5c96bb0f888caae50bea885d24f8c7158927e33da92e7b5c2eb9571981b.

- 2026-10-09T15:48:58+00:00: Recorded command exit 0; command argv SHA-256
  56d8695c759a8fa655669ce488499148d7d5f3aa5cd864b645edfddaa37bb475.

- 2026-10-09T15:49:19+00:00: Checkpointed source commit c34a3d6b52b009d62a513bae6713e748b9dbd1fb.

- 2026-10-09T15:49:29+00:00: Recorded command exit 1; command argv SHA-256
  882a2b0d15036ccccb540d14aabe9077fdf6a4b45684ccd1b5e7fecfe60460c8.

- 2026-10-09T15:49:49+00:00: Full-gate attempt failed before running Clippy: cargo fmt received
  --manifest-path after the rustfmt separator and exited 101 because the wrapper cwd is the state
  checkout. No product mutation or publication occurred; retry will pass manifest-path before --.

- 2026-10-09T15:50:07+00:00: Recorded command exit 101; command argv SHA-256
  196a03c6abea2f1ab0074c6b051e942da5ffb3890376e4b7829efa4f18e52d99.
