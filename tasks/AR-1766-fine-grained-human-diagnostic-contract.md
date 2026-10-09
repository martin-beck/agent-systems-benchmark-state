---
{
  "branch": "feature/ar-1766-fine-grained-human-diagnostic-contract",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-09T19:39:26+00:00",
  "depends_on": [
    "AR-1757",
    "AR-1760",
    "AR-1761",
    "AR-1762"
  ],
  "id": "AR-1766",
  "next_action": "Run full cargo gates, then commit the reviewed diagnostic catalog/docs/tests with SSH signature and DCO; publish PR for independent review. State reconcile remains blocked by oversized generated handoffctl pyc and stale WORKTREES.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "codex-ar1766-diagnostics",
  "plan": "../plans/AR-1766-fine-grained-human-diagnostic-contract.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "contract-test",
    "evidence_digest": "",
    "evidence_ref": "",
    "spec_ref": "specs/AR-1766.json",
    "spec_revision": 1,
    "status": "pending"
  },
  "spec_ref": "specs/AR-1766.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Define a fine-grained typed diagnostic catalog carrying the safe context needed for clear human errors, failures, warnings, and remediation.",
  "task_revision": 29,
  "title": "Fine-grained human diagnostic contract",
  "updated_at": "2026-10-09T17:46:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1766-fine-grained-human-diagnostic-contract"
}
---

AR-1757 added an explicit human presentation for every public command family,
but the current public failure boundary still receives broad free-form messages.
Distinct causes can therefore collapse into text such as `unavailable`, `failed`,
`cannot be staged`, or `parent is unavailable`, without naming the affected
resource or explaining the correction.

Create one closed, typed diagnostic catalog for every public ASB command error,
operation failure, partial result, and warning. Use the finest meaningful stable
class available at the point of failure. At minimum distinguish missing parent,
missing input, target already exists, target is not a directory, target is not a
regular file, permission denied, read-only storage, unsafe/symlink topology,
invalid path, malformed or incompatible input, stale identity, unavailable
capability, missing tool, provider authentication, provider rejection, transport
failure, timeout, cancellation, partial completion, reconciliation required, and
unexpected product failure. Do not erase a known cause by mapping it to a broader
`Rejected`, `Unavailable`, validation, or I/O bucket.

Each diagnostic must carry only the safe structured context needed to render the
affected subject, user-supplied path or option, operation, state-change result,
and recovery. Internal host paths, credentials, provider payloads, prompts, and
raw operating-system error strings remain private. When a lower boundary truly
cannot determine a narrower cause, use an explicit bounded unknown-cause variant.

Preserve exit meanings and explicit JSON contracts. Cover CLI, `asb easy`,
ASB-routed TUI lifecycle results, setup/config/auth, project/tool commands,
plans, runs/sweeps, reports, record/replay, provider/network boundaries, and
warnings embedded in successful results. New public diagnostics may not bypass
the catalog.


- 2026-10-09T17:31:49+00:00: AR-1757, AR-1760, AR-1761, and AR-1762 are complete with exact-main
  evidence; begin fine-grained human diagnostic contract.

- 2026-10-09T17:32:31+00:00: Claimed by codex-ar1766-diagnostics.

- 2026-10-09T17:32:51+00:00: Recorded command exit 0; command argv SHA-256
  21b7b13cd636ee6c963751b13f21395f9e9e0479d6626bd52a97b15c4b2e0c04.

- 2026-10-09T17:34:50+00:00: Recorded command exit 1; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-10-09T17:35:14+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-09T17:35:54+00:00: Recorded command exit 101; command argv SHA-256
  343288bdbf1758fdb26903a3231ad66ab4ea21ca4fb4e05adb487da95d66d19d.

- 2026-10-09T17:36:15+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-09T17:36:39+00:00: Recorded command exit 101; command argv SHA-256
  343288bdbf1758fdb26903a3231ad66ab4ea21ca4fb4e05adb487da95d66d19d.

- 2026-10-09T17:37:07+00:00: Recorded command exit 0; command argv SHA-256
  343288bdbf1758fdb26903a3231ad66ab4ea21ca4fb4e05adb487da95d66d19d.

- 2026-10-09T17:37:44+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-09T17:38:05+00:00: Recorded command exit 0; command argv SHA-256
  4e30782b138a9ea906d2dc305eb5587cac9f1ed14209bf16e635bda3ff81642d.

- 2026-10-09T17:38:25+00:00: Recorded command exit 0; command argv SHA-256
  d32df0a8f7802e39b9a6743613fff16ac35e4dddba3905aa783a204f77a7e43f.

- 2026-10-09T17:38:59+00:00: Recorded command exit 0; command argv SHA-256
  eb8648d78be9d44db5631385c3fcbaaeaac0114989924fef6dc1415045ce0bfa.

- 2026-10-09T17:39:02+00:00: Recorded command exit 0; command argv SHA-256
  eb8648d78be9d44db5631385c3fcbaaeaac0114989924fef6dc1415045ce0bfa.

- 2026-10-09T17:39:26+00:00: Heartbeat by codex-ar1766-diagnostics.

- 2026-10-09T17:39:44+00:00: Focused cargo test -p asb-cli --test diagnostic_contract passed (3
  tests); cargo clippy --locked -p asb-cli --all-targets -- -D warnings passed. Added closed
  catalog, routed TUI resolution, privacy compatibility test, and producer inventory docs.

- 2026-10-09T17:39:54+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-10-09T17:40:40+00:00: Recorded command exit 101; command argv SHA-256
  534f8613e1c316db8f0f46dd989e44e14a8ca74304a94791b4e4a1c59b2fbb1d.

- 2026-10-09T17:41:07+00:00: Recorded command exit 0; command argv SHA-256
  1024fc1e6cefa31b078f0b5d2ed85c7ea4586897b388bf1e308f62db58574461.

- 2026-10-09T17:41:47+00:00: Recorded command exit 101; command argv SHA-256
  534f8613e1c316db8f0f46dd989e44e14a8ca74304a94791b4e4a1c59b2fbb1d.

- 2026-10-09T17:42:13+00:00: Recorded command exit 0; command argv SHA-256
  f0992fdac012a79b34ed03fc09aa8cd0bd5a9f9de3222a6d320e6e13f3d26905.

- 2026-10-09T17:42:51+00:00: Recorded command exit 101; command argv SHA-256
  534f8613e1c316db8f0f46dd989e44e14a8ca74304a94791b4e4a1c59b2fbb1d.

- 2026-10-09T17:43:16+00:00: Recorded command exit 0; command argv SHA-256
  9ff4e40d0a608a041abbfd1d435a9e4d565a2c8931e342870e1969854466c867.

- 2026-10-09T17:44:04+00:00: Recorded command exit 0; command argv SHA-256
  534f8613e1c316db8f0f46dd989e44e14a8ca74304a94791b4e4a1c59b2fbb1d.

- 2026-10-09T17:44:31+00:00: Recorded command exit 0; command argv SHA-256
  1024fc1e6cefa31b078f0b5d2ed85c7ea4586897b388bf1e308f62db58574461.

- 2026-10-09T17:45:02+00:00: Recorded command exit 0; command argv SHA-256
  b36d15881eb65027724bc584f1b04db05666cd79896b100806e528307c04b65c.

- 2026-10-09T17:45:37+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-09T17:46:00+00:00: Recorded command exit 0; command argv SHA-256
  4e30782b138a9ea906d2dc305eb5587cac9f1ed14209bf16e635bda3ff81642d.
