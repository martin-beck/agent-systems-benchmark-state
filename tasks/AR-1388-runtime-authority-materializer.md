---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1385",
    "AR-1384",
    "AR-1378",
    "AR-1377"
  ],
  "id": "AR-1388",
  "next_action": "Promote after dependency validation; implement the production runtime authority materializer from authenticated receipt/chain into private bootstrap inputs without CLI authority injection.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "0000000000000000000000000000000000000000",
  "owner": "",
  "plan": "../plans/AR-1388-runtime-authority-materializer.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Materialize runtime-owned provider authority from authenticated receipt and chain state.",
  "task_revision": 1,
  "title": "Runtime authority receipt materializer",
  "updated_at": "2026-09-24T06:40:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1388-runtime-authority-materializer"
}
---

This repair supplies the missing production-owned conversion from the
authenticated receipt/chain to private bootstrap authority. It must never
accept caller-supplied policy, allowlists, credentials, roots, tools,
namespace identity, or launch tokens.

