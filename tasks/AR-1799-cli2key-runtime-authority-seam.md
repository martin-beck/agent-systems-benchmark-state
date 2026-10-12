---
{
  "branch": "feature/ar-1799-cli2key-runtime-authority-seam",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-12T07:11:27+00:00",
  "depends_on": [
    "AR-1729",
    "AR-1731"
  ],
  "id": "AR-1799",
  "next_action": "Implement receipt validation, sidecar bootstrap, opaque attempt issuance, and lifecycle tests.",
  "observed_branch": "feature/ar-1799-cli2key-runtime-authority-seam",
  "observed_dirty": 0,
  "observed_head": "6761a6d0bcd5d5982c92176f4adf687696de90d6",
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
  "task_revision": 14,
  "title": "Add cli2key runtime authority composition seam",
  "updated_at": "2026-10-12T04:20:31+00:00",
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
