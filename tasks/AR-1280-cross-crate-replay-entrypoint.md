---
{
  "branch": "feature/ar-1280-cross-crate-replay-entrypoint",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-17T02:13:29+00:00",
  "depends_on": [
    "AR-1237",
    "AR-1238",
    "AR-1239"
  ],
  "id": "AR-1280",
  "next_action": "Extend replay-plan dispatch to invoke runtime-owned supervised process with argument-level command and cassette service; preserve denied egress/no-fallback and add lifecycle fault tests. Current signed head f92a86b provides bridge/binding baseline.",
  "observed_branch": "feature/ar-1280-cross-crate-replay-entrypoint",
  "observed_dirty": 0,
  "observed_head": "f92a86b126e36e467bccb769ce6ead9a70cf639c",
  "owner": "asb_ar1280_runtime_cli_entrypoint",
  "plan": "../plans/AR-1280.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Implement the cross-crate runtime process entrypoint for primary strict replay.",
  "task_revision": 9,
  "title": "Cross-crate replay process entrypoint",
  "updated_at": "2026-09-17T00:16:55+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1280-cross-crate-replay-entrypoint"
}
---

## AR-1280

Implement the authenticated cross-crate replay process entrypoint from protected main. Preserve
prior blocked evidence, but do not substitute another audit-only result.

- 2026-09-17T00:13:14+00:00: Dependencies AR-1237, AR-1238, and AR-1239 are done. Prior ARs only
  establish the missing seam; this AR must implement the cross-crate entrypoint from protected main.

- 2026-09-17T00:13:29+00:00: Claimed by asb_ar1280_runtime_cli_entrypoint.

- 2026-09-17T00:13:44+00:00: Recorded command exit 0; command argv SHA-256
  3e33781563a4510d2b29ef626cb1a320e5d8447887a3ad016f11857cb6ea7563.

- 2026-09-17T00:15:26+00:00: Recorded command exit 0; command argv SHA-256
  fef085b0d28dbc6b18c7b98ffd05ceee7c8825b95c169924ce62220ed98ee824.

- 2026-09-17T00:16:10+00:00: Recorded command exit 0; command argv SHA-256
  5db74a837babd6ee91c53e4779642905895f6bbe4daa074f97c69dd4d9556914.

- 2026-09-17T00:16:55+00:00: Concrete implementation checkpoint: ported signed cross-crate artifact
  contract, runtime relay binding, StrictReplayLaunchBridge::spawn, supervisor command attestation,
  CLI replay-plan dispatch, malformed/path/digest/egress negatives, and missing-relay pre-child
  rejection. Signed product head f92a86b126e36e467bccb769ce6ead9a70cf639c is clean. Focused asb-cli
  replay_contract tests pass 5/5 under locked manifest. State push briefly failed with remote HTTP
  502 after command recording; product changes remain local and signed. Remaining acceptance is
  actual argument-level replay process invocation plus supervised cassette traffic and lifecycle
  fault matrix.
