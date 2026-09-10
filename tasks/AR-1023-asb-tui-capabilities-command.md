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
  "observed_dirty": 4,
  "observed_head": "66ca27afc2fb5a82b171e849e6dda4145735c8d2",
  "owner": "codex-ar1023-capabilities-20260910",
  "plan": "../plans/AR-1023.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Publish the ASB capability negotiation command required by the standalone frontend.",
  "task_revision": 10,
  "title": "Add the ASB frontend capabilities command",
  "updated_at": "2026-09-10T19:28:05+00:00",
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

- 2026-09-10T19:24:09+00:00: Reconciled standalone asb-tui capability schema at origin/main
  3d2b6b537da817469bf8a39841ccf9a79a4c370f with ASB control v1: all eight advertised frontend
  operations have authoritative typed control methods and RunnerBackend implementations;
  implementing closed side-effect-free JSON command and parity tests.

- 2026-09-10T19:26:25+00:00: Recorded command exit 2; command argv SHA-256
  48458d4adcbc2714c4ae60f17ec39d916357031118af6e75d9a5cd826c73f20e.

- 2026-09-10T19:27:22+00:00: Recorded command exit 0; command argv SHA-256
  bfb5188cf3d2030cf5658de848191cc7f96026c089e31d4d791af020d03400c7.

- 2026-09-10T19:28:05+00:00: Recorded command exit 101; command argv SHA-256
  be876d1bcca7e3e12fa64d46b3e64da1cdb663bec004b092515642b6f175e2d5.
