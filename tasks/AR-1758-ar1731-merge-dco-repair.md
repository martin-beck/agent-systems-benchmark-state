---
{
  "branch": "repair/ar-1758-merge-dco",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-09T15:01:27+00:00",
  "depends_on": [],
  "id": "AR-1758",
  "next_action": "PR #528 exact repair head 00f0525 is green except long-running policy and emulated-aarch64 jobs; after terminal success run tools/integration/merge_pr.py with exact base b3cb9b2, head 00f0525, tree 980a60bd, --push, then verify exact-main.",
  "observed_branch": "repair/ar-1758-merge-dco",
  "observed_dirty": 0,
  "observed_head": "b3cb9b256cccc15be682dbb1019a239b50edf6cd",
  "owner": "codex-asb-ar1758-merge-dco-repair-20261009",
  "plan": "../plans/AR-1758-ar1731-merge-dco-repair.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_ref": "specs/AR-1758.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Restore a compliant protected-main publication after the AR-1731 local merge lacked a DCO trailer, without rewriting published history or weakening gates.",
  "task_revision": 12,
  "title": "Repair AR-1731 protected-main merge provenance",
  "updated_at": "2026-10-09T13:01:34+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1758-merge-dco"
}
---

AR-1731's signed local two-parent merge `b3cb9b2` preserved the reviewed tree and
parents but omitted its matching `Signed-off-by` trailer, so protected-main
portable provenance failed. This repair must preserve that historical evidence,
must not force-update or rewrite `main`, and must use a reviewed repair PR and
the repository's documented merge-integrity tooling. AR-1731 remains unaccepted
until the repaired exact-main workflows are green.

- 2026-10-09T12:55:09+00:00: Created to repair the observed AR-1731 protected-main merge/DCO
  publication mismatch without rewriting history; dependency cycle removed.

- 2026-10-09T12:55:12+00:00: Claimed by codex-asb-ar1758-merge-dco-repair-20261009.

- 2026-10-09T12:56:40+00:00: Recorded command exit 0; command argv SHA-256
  bac5d7b3843f6fd01b1cb89819cc1a7fec08c5ea266e78359b30684dd859efa7.

- 2026-10-09T12:56:49+00:00: Recorded command exit 1; command argv SHA-256
  8747ab068c792ed31e60e308318f688e1a9afa5ca63852a1a4bd512253d60047.

- 2026-10-09T12:57:04+00:00: Recorded command exit 0; command argv SHA-256
  043f15784a4f7d81f7d30fed2c163f95077fc013a261a6cd7969522924b72650.

- 2026-10-09T12:57:55+00:00: Recorded command exit 0; command argv SHA-256
  e75a34f4f25bb34858aa2834408ca3b44567522e4c707405df70509bd9081ed9.

- 2026-10-09T13:01:27+00:00: Heartbeat by codex-asb-ar1758-merge-dco-repair-20261009.

- 2026-10-09T13:01:34+00:00: Dedicated repair worktree is active; monitored hosted checks and
  preserved no-history-rewrite path.
