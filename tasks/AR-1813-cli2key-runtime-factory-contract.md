---
{
  "branch": "feature/ar-1813-cli2key-runtime-factory-contract",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1779",
    "AR-1799"
  ],
  "id": "AR-1813",
  "next_action": "Exact-main merge 5c843a12 is verified by 9/10 terminal-success workflows; Repository quality run 38239012450 remains in progress with no failure. Wait for its terminal result, then record final post-merge receipt and release AR-1813 done.",
  "observed_branch": "feature/ar-1813-cli2key-runtime-factory-contract",
  "observed_dirty": 0,
  "observed_head": "7889b3bad4c03d1caca5eaa28ffd53b367ebf445",
  "owner": "",
  "plan": "../plans/AR-1813-cli2key-runtime-factory-contract.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "hosted",
    "evidence_digest": "sha256:0112204acd1de7f843e47097142098019e4ea1db8250c61ac7405a5b89c981d8",
    "evidence_ref": "main/5c843a12e976bc7be6c32e9fc653e566bdf20450",
    "spec_ref": "specs/AR-1813.json",
    "spec_revision": 1,
    "status": "pass"
  },
  "spec_ref": "specs/AR-1813.json",
  "spec_revision": 1,
  "status": "done",
  "summary": "Expose the runtime-owned cli2key receipt contract and opaque factory required for ordinary CLI bootstrap.",
  "task_revision": 36,
  "title": "Expose cli2key runtime factory contract",
  "updated_at": "2026-10-12T11:05:35+00:00",
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

- 2026-10-12T10:51:43+00:00: Recorded resolve interaction gate spec;
  event=sha256:d2d1381d7c6d7197a3052abde3034354c286fddabecf4078d93c4ecc97ed2e50.

- 2026-10-12T10:51:54+00:00: Recorded open interaction gate decision;
  event=sha256:898dbf009d62c5204678f7b039d7445fad8c8b9d7f7b71aa6169a5377e2b593a.

- 2026-10-12T10:51:57+00:00: Recorded resolve interaction gate decision;
  event=sha256:c4f5b993cddc4da94d8e9e15f7feb300d0104eaedafcf52432a77973f8eb6690.

- 2026-10-12T10:51:59+00:00: Recorded command exit 0; command argv SHA-256
  82af41fb18227576359b1d4e4d22e8b15255e54ce3c17a495bcff833923154f0.

- 2026-10-12T10:52:13+00:00: Recorded command exit 0; command argv SHA-256
  3f89559c7be03f821932a527202152574a956930b25f12d979f4ae8b932ce77a.

- 2026-10-12T10:54:16+00:00: Heartbeat by ar1810-cli2key-luna56.

- 2026-10-12T10:54:19+00:00: PR #607 merged exact-base signed two-parent commit 5c843a12; post-merge
  verification pending; no TLC required.

- 2026-10-12T10:56:48+00:00: Heartbeat by ar1810-cli2key-luna56.

- 2026-10-12T10:56:48+00:00: Refreshed post-merge observation; no failures and no TLC requirement.

- 2026-10-12T11:03:22+00:00: Heartbeat by ar1810-cli2key-luna56.

- 2026-10-12T11:03:22+00:00: Rust verification completed successfully; Repository quality is the
  only remaining authoritative post-merge gate.

- 2026-10-12T11:05:20+00:00: Recorded command exit 0; command argv SHA-256
  d55dc3353577df7cae9ec34b2ff6bf2c8dc5954b4b1d04259aaaf12f937d8d62.

- 2026-10-12T11:05:31+00:00: Protected exact-base merge 5c843a12 and 10/10 exact-main
  terminal-success workflows verified; signed merge/DCO/tree/parents confirmed; no TLC required for
  development.

- 2026-10-12T11:05:35+00:00: AR-1813 complete: PR #607 exact-base signed merge 5c843a12, exact-head
  checks green, 10/10 exact-main post-merge workflows terminal success, durable receipt
  quality/AR-1813-postmerge-receipt.txt.


## Preserved oracle-gate evidence

```json
{
  "completed": [
    "role",
    "spec",
    "decision"
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
    },
    {
      "action": "resolve",
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
      "disposition": "accepted",
      "public_ref": "AR-1813/spec-520987de",
      "recorded_at": "2026-10-12T10:51:43+00:00",
      "stage": "spec",
      "task_id": "AR-1813",
      "task_revision": 22
    },
    {
      "action": "open",
      "after": [
        {
          "digest": "sha256:e6aa46eac87ed9900b68e4451eb1153710211e4ae36617b0ba8f869b4a7fe176",
          "ref": "decision/merge-authorized"
        }
      ],
      "before": [
        {
          "digest": "sha256:520987deedc4089478ff58428040d951009fa41d95e13d97760a45e45fbab915",
          "ref": "specs/AR-1813.json"
        }
      ],
      "disposition": "unresolved",
      "public_ref": "PR-607/7889b3bad4c03d1caca5eaa28ffd53b367ebf445",
      "recorded_at": "2026-10-12T10:51:54+00:00",
      "stage": "decision",
      "task_id": "AR-1813",
      "task_revision": 23
    },
    {
      "action": "resolve",
      "after": [
        {
          "digest": "sha256:e6aa46eac87ed9900b68e4451eb1153710211e4ae36617b0ba8f869b4a7fe176",
          "ref": "decision/merge-authorized"
        }
      ],
      "before": [
        {
          "digest": "sha256:520987deedc4089478ff58428040d951009fa41d95e13d97760a45e45fbab915",
          "ref": "specs/AR-1813.json"
        }
      ],
      "disposition": "accepted",
      "public_ref": "PR-607/7889b3bad4c03d1caca5eaa28ffd53b367ebf445",
      "recorded_at": "2026-10-12T10:51:57+00:00",
      "stage": "decision",
      "task_id": "AR-1813",
      "task_revision": 24
    }
  ],
  "open_stage": null,
  "reconciliation_required": false,
  "required": true,
  "stage_sequence": [
    "role",
    "spec",
    "decision"
  ]
}
```
