---
{
  "branch": "docs/measurement-catalog-merge-attestation",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1045"
  ],
  "id": "AR-1051",
  "next_action": "After AR-1045 restores a green protected-main descendant, publish a bounded immutable attestation for PR #140 and its missing-DCO merge boundary.",
  "observed_branch": "docs/measurement-catalog-merge-attestation",
  "observed_dirty": 0,
  "observed_head": "607a3afb3a44b87f9c60b6ae3bc764570e84d5fe",
  "owner": "",
  "plan": "../plans/AR-1051.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Record the exact reviewed measurement-catalog merge and its non-compliant GitHub-authored DCO identity without rewriting history.",
  "task_revision": 2,
  "title": "Attest the measurement catalog merge boundary",
  "updated_at": "2026-09-11T03:12:10+00:00",
  "worktree_key": "agent-systems-benchmark-measurement-catalog-merge-attestation"
}
---

PR #140 passed all 12 exact-head checks and merged the reviewed catalog tree, but protected-main
quality run 34557143666 correctly rejected merge `252f746e903555c2dc626fadfa1a75bb76913144`:
the GitHub author is `martin-beck <martin.beck2@gmx.de>` while its trailer names `Martin Beck`.
Do not rewrite or retroactively call that merge compliant. Publish only bounded, reproducible
attestation evidence and a corrective future merge recipe using the exact GitHub author identity.

