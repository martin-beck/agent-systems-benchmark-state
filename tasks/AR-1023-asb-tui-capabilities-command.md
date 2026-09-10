---
{
  "branch": "feature/asb-tui-capabilities-command",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-10T22:23:58+00:00",
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
  "observed_branch": "feature/asb-tui-capabilities-command",
  "observed_dirty": 0,
  "observed_head": "66ca27afc2fb5a82b171e849e6dda4145735c8d2",
  "owner": "codex-ar1023-capabilities-20260910",
  "plan": "../plans/AR-1023.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Publish the ASB capability negotiation command required by the standalone frontend.",
  "task_revision": 5,
  "title": "Add the ASB frontend capabilities command",
  "updated_at": "2026-09-10T19:23:58+00:00",
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

- 2026-09-10T19:22:26+00:00: Recorded command exit 0; command argv SHA-256
  5fc886b4070fa3ab0ac6f393b844d9a9add78751cef9f4fa0a626ebafbee8e8b.

- 2026-09-10T19:23:58+00:00: Heartbeat by codex-ar1023-capabilities-20260910.
