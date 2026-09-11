---
{
  "branch": "docs/measurement-catalog-merge-attestation",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-11T06:31:24+00:00",
  "depends_on": [
    "AR-1045"
  ],
  "id": "AR-1051",
  "next_action": "After AR-1045 restores a green protected-main descendant, publish a bounded immutable attestation for PR #140 and its missing-DCO merge boundary.",
  "observed_branch": "docs/measurement-catalog-merge-attestation",
  "observed_dirty": 0,
  "observed_head": "1a19b692d724fd5ba1996470daccbfed06171a0a",
  "owner": "codex-ar1051-measurement-catalog-attestation-20260911",
  "plan": "../plans/AR-1051.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Record the exact reviewed measurement-catalog merge and its non-compliant GitHub-authored DCO identity without rewriting history.",
  "task_revision": 9,
  "title": "Attest the measurement catalog merge boundary",
  "updated_at": "2026-09-11T03:33:14+00:00",
  "worktree_key": "agent-systems-benchmark-measurement-catalog-merge-attestation"
}
---

PR #140 passed all 12 exact-head checks and merged the reviewed catalog tree, but protected-main
quality run 34557143666 correctly rejected merge `252f746e903555c2dc626fadfa1a75bb76913144`:
the GitHub author is `martin-beck <martin.beck2@gmx.de>` while its trailer names `Martin Beck`.
Do not rewrite or retroactively call that merge compliant. Publish only bounded, reproducible
attestation evidence and a corrective future merge recipe using the exact GitHub author identity.


- 2026-09-11T03:31:21+00:00: AR-1045 is done at protected-main merge 1a19b692 with all postmerge
  workflows green; PR #140 historical attestation is dependency-ready.

- 2026-09-11T03:31:24+00:00: Claimed by codex-ar1051-measurement-catalog-attestation-20260911.

- 2026-09-11T03:31:34+00:00: Recorded command exit 0; command argv SHA-256
  0bb4def436152f367f4fa7116ee3cfb548e90e591a39a802a958d67aba426670.

- 2026-09-11T03:32:34+00:00: Recorded command exit 0; command argv SHA-256
  8b5f438fc7d30b21bfe653d3cabac1c3f2b60f41b4e1cd9a77a5dd3c627fa5be.

- 2026-09-11T03:32:48+00:00: Recorded command exit 0; command argv SHA-256
  619402b9a12255f06dd13d71aa157db6b35edcf8450890f0654051caa48d89e2.

- 2026-09-11T03:33:08+00:00: Recorded command exit 0; command argv SHA-256
  e0c1e229dc528046d86d06050a9c8c83e7d60a602856ec4b9a82aea94e8143e6.
