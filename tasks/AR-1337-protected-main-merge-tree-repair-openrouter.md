---
{
  "branch": "repair/ar-1337-openrouter-merge-tree-admission",
  "checkpoint_commit": "8dc07a0f86a10aa6b20c87b2d67c34117adc69bc",
  "claim_expires": "2026-09-23T08:26:25+00:00",
  "depends_on": [
    "AR-1226"
  ],
  "id": "AR-1337",
  "next_action": "Await remaining PR #252 exact-head checks and independent review; then merge only via signed integration procedure at the current protected target and verify post-merge workflows.",
  "observed_branch": "repair/ar-1337-openrouter-merge-tree-admission",
  "observed_dirty": 0,
  "observed_head": "8dc07a0f86a10aa6b20c87b2d67c34117adc69bc",
  "owner": "codex-ar1337",
  "plan": "../plans/AR-1337.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Repair the protected-main merge-tree admission defect exposed after the OpenRouter provider merge.",
  "task_revision": 9,
  "title": "Repair protected-main merge-tree admission after OpenRouter merge",
  "updated_at": "2026-09-23T06:35:51+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1337-protected-main-merge-tree-repair"
}
---

The exact-head PR #249 checks were green, but post-merge Repository quality run
35825987339 rejected protected-main merge 56c882a06337a2b58c761bddaef2c743cba65712:
the protected-main merge tree differs from the reviewed topic tree. Reproduce
the mismatch against the immutable base and head, identify whether the merge
method or admission calculation is wrong, and repair the durable flow. Preserve
signature, DCO, exact-head and merge-tree checks; never add a one-off hash
exception or bypass the policy.

Acceptance requires a clean signed+DCO repair, independent review, exact-head
CI, a protected-main merge whose computed tree equals the reviewed topic tree,
and successful post-merge Repository quality, formal, fault, portability and
Rust workflows. Record the exact merge parents, tree IDs, run IDs and any
remaining evidence limits without private paths or credentials.

- 2026-09-23T06:23:11+00:00: Claimed by codex-ar1337.

- 2026-09-23T06:25:45+00:00: Reproduced merge 56c882a: reviewed topic 85eece9 is based on a4934fc,
  target parent was 6b06f0e, and GitHub merge tree ee822b52 differs from topic tree bdb1356c. Added
  hostile integration regression proving merge_pr rejects a protected target advanced after review;
  focused and full tools.integration.test_merge_pr pass. Signed+DCO commit 8dc07a0.

- 2026-09-23T06:26:25+00:00: Heartbeat by codex-ar1337.

- 2026-09-23T06:26:43+00:00: Recorded command exit 0; command argv SHA-256
  73ebc8b4857e2aba6ae5e051e1f1da90b69d5981a57223c16ee116b362ce5a10.

- 2026-09-23T06:27:06+00:00: Recorded command exit 0; command argv SHA-256
  7a6648f19871bcfba727d1838b42d9807516d3532946bdfcb9e2cfd09b657728.

- 2026-09-23T06:30:30+00:00: Published PR #252
  https://github.com/martin-beck/agent-systems-benchmark/pull/252 at exact head
  8dc07a0f86a10aa6b20c87b2d67c34117adc69bc, base 56c882a06337a2b58c761bddaef2c743cba65712.
  Exact-head checks: headers, platform, retained faults, bounded fuzz, Kani, Loom, mutation
  sentinels and AWQ shadow SUCCESS; emulated aarch64, policy/coverage, Rust and TLC/Alloy remain
  pending. Independent review still required; no merge performed.

- 2026-09-23T06:35:51+00:00: Recorded command exit 0; command argv SHA-256
  4557a5bdf39419249554168714ca3a7ed501fb56a58acf6a991d33e3d00b1c75.
