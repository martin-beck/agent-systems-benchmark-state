---
{
  "branch": "feature/asb-tui-capabilities-command",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-10T22:14:02+00:00",
  "depends_on": [
    "AR-0803",
    "AR-0840",
    "AR-0841",
    "AR-0842",
    "AR-0843",
    "AR-0844",
    "AR-0904"
  ],
  "id": "AR-1023",
  "next_action": "Implement the closed side-effect-free ASB frontend capability command and cross-check its output against the published asb-tui parser contract.",
  "owner": "codex-ar1023-capabilities-20260910",
  "plan": "../plans/AR-1023.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Publish the ASB capability negotiation command required by the standalone frontend.",
  "task_revision": 2,
  "title": "Add the ASB frontend capabilities command",
  "updated_at": "2026-09-10T19:14:02+00:00",
  "worktree_key": "agent-systems-benchmark-asb-tui-capabilities-command"
}
---
Add `asb capabilities --format json` as a bounded, deterministic, side-effect-free description of
the installed ASB/frontend protocol contract. It must match the separately published asb-tui schema
and expose only capabilities the authoritative runner API actually implements.

Acceptance requires exact schema/type/fixture parity, malformed-argument and output-bound tests,
privacy-safe output, CLI help/completion/docs updates, cross-repository parser conformance, complete
local gates, independent review, exact-head CI and post-merge verification.

- 2026-09-10T19:14:02+00:00: Claimed by codex-ar1023-capabilities-20260910.
