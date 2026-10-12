---
{
  "branch": "feature/ar-1813-cli2key-runtime-factory-contract",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-12T11:20:23+00:00",
  "depends_on": [
    "AR-1779",
    "AR-1799"
  ],
  "id": "AR-1813",
  "next_action": "PR #607 rebased exact head 7889b3bad4c03d1caca5eaa28ffd53b367ebf445; hosted non-TLC checks are running. Focused/full non-TLC gates pass; obtain independent review, then protected exact-head merge and post-merge verification.",
  "observed_branch": "feature/ar-1813-cli2key-runtime-factory-contract",
  "observed_dirty": 0,
  "observed_head": "7889b3bad4c03d1caca5eaa28ffd53b367ebf445",
  "oracle_gate": {
    "completed": [
      "role"
    ],
    "discussion_rounds": 0,
    "events": [
      {
        "action": "open",
        "after": [
          {
            "digest": "sha256:2005708252e64993e95f554873286056cea4f0ed56263666e733f00403933907",
            "ref": "review/candidate"
          }
        ],
        "before": [
          {
            "digest": "sha256:2595fc33eda6071001fadbbda6d93b5a24bd5d352f55f0548d376896db0091c9",
            "ref": "review/base"
          }
        ],
        "disposition": "unresolved",
        "public_ref": "PR-607/7889b3bad4c03d1caca5eaa28ffd53b367ebf445",
        "recorded_at": "2026-10-12T10:43:45+00:00",
        "stage": "role",
        "task_id": "AR-1813",
        "task_revision": 17
      },
      {
        "action": "resolve",
        "after": [
          {
            "digest": "sha256:2005708252e64993e95f554873286056cea4f0ed56263666e733f00403933907",
            "ref": "review/accepted"
          }
        ],
        "before": [
          {
            "digest": "sha256:2005708252e64993e95f554873286056cea4f0ed56263666e733f00403933907",
            "ref": "review/candidate"
          }
        ],
        "disposition": "accepted",
        "public_ref": "PR-607/7889b3bad4c03d1caca5eaa28ffd53b367ebf445",
        "recorded_at": "2026-10-12T10:43:52+00:00",
        "stage": "role",
        "task_id": "AR-1813",
        "task_revision": 18
      },
      {
        "action": "open",
        "after": [
          {
            "digest": "sha256:520987deedc4089478ff58428040d951009fa41d95e13d97760a45e45fbab915",
            "ref": "specs/AR-1813.json"
          }
        ],
        "before": [
          {
            "digest": "sha256:2005708252e64993e95f554873286056cea4f0ed56263666e733f00403933907",
            "ref": "review/accepted"
          }
        ],
        "disposition": "unresolved",
        "public_ref": "AR-1813/spec-520987de",
        "recorded_at": "2026-10-12T10:51:40+00:00",
        "stage": "spec",
        "task_id": "AR-1813",
        "task_revision": 21
      }
    ],
    "open_stage": "spec",
    "reconciliation_required": false,
    "required": true,
    "stage_sequence": [
      "role",
      "spec",
      "decision"
    ]
  },
  "owner": "ar1810-cli2key-luna56",
  "plan": "../plans/AR-1813-cli2key-runtime-factory-contract.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "contract-test",
    "evidence_digest": "",
    "evidence_ref": "",
    "spec_ref": "specs/AR-1813.json",
    "spec_revision": 1,
    "status": "pending"
  },
  "spec_ref": "specs/AR-1813.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Expose the runtime-owned cli2key receipt contract and opaque factory required for ordinary CLI bootstrap.",
  "task_revision": 22,
  "title": "Expose cli2key runtime factory contract",
  "updated_at": "2026-10-12T10:51:40+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1813-cli2key-runtime-factory-contract"
}
---

AR-1812 cannot safely implement its ordinary `run`/`sweep` bootstrap because
the production `asb-runtime` factory constructor is private and the generic
AR-1779 receipt lacks the runtime identity/bridge fields. This AR owns only
that runtime-owned API and versioned non-secret receipt contract; it must not
fabricate authority in the CLI or introduce a provider fallback.

- 2026-10-12T10:14:31+00:00: Promoted P0 prerequisite for AR-1812: expose a runtime-owned verified
  cli2key receipt contract and opaque LiveProviderAttemptFactory without CLI authority fabrication
  or provider fallback.

- 2026-10-12T10:14:34+00:00: Claimed by ar1810-cli2key-luna56.

- 2026-10-12T10:14:56+00:00: Bound worktree
  agent-systems-benchmark-ar-1813-cli2key-runtime-factory-contract on branch
  feature/ar-1813-cli2key-runtime-factory-contract.

- 2026-10-12T10:16:18+00:00: Heartbeat by ar1810-cli2key-luna56.

- 2026-10-12T10:21:08+00:00: Recorded exact PR head and the inherited TLC workflow dependency; no
  TLC execution performed locally.

- 2026-10-12T10:34:32+00:00: Recorded command exit 0; command argv SHA-256
  b7c438686581cf292b6cd41497ceabb3af42dfed57e04dfd6cc89efed8e2d15b.

- 2026-10-12T10:35:07+00:00: Recorded command exit 0; command argv SHA-256
  297bf0426da2b3a34cc8d291742b5d89c6c71377df2a616c878604996ff250b5.

- 2026-10-12T10:37:41+00:00: Recorded command exit 0; command argv SHA-256
  7b80382008cb01e3ea6fa6e88054b624464f9801b40ed57f947b01892a686ae8.

- 2026-10-12T10:38:00+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-10-12T10:38:21+00:00: Recorded command exit 0; command argv SHA-256
  1024fc1e6cefa31b078f0b5d2ed85c7ea4586897b388bf1e308f62db58574461.

- 2026-10-12T10:38:28+00:00: Recorded command exit 0; command argv SHA-256
  1c4aafd2e66e0c5ef7f4527dab971ff1286ec76cabc073ce635539aaaa70e25a.

- 2026-10-12T10:38:40+00:00: Recorded command exit 0; command argv SHA-256
  d0b74b004b9f693da9a0ac7c2ab5dfcb88cca69545cae5aeda04ca40372cbed9.

- 2026-10-12T10:39:49+00:00: Rebased PR #607 from 458ce867 onto merged main 5a6c5477; local focused
  and full locked workspace tests, fmt, clippy, and repository policy pass. Hosted non-TLC checks
  pending.

- 2026-10-12T10:43:45+00:00: Recorded open interaction gate role;
  event=sha256:4d06e431f39441330e260bcfe7587f902f9fb6d8cd14a1bafa11bf8622641c5b.

- 2026-10-12T10:43:52+00:00: Recorded resolve interaction gate role;
  event=sha256:097a89204d037616edc44db3bc1b5d068d6fabe65a7e240bfe96d2f80511313b.

- 2026-10-12T10:47:14+00:00: Heartbeat by ar1810-cli2key-luna56.

- 2026-10-12T10:50:23+00:00: Heartbeat by ar1810-cli2key-luna56.

- 2026-10-12T10:51:40+00:00: Recorded open interaction gate spec;
  event=sha256:84b44547c3796c5b319512dc3168f86923bc90da67d65a275ced49f8936813d7.
