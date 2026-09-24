---
{
  "branch": "feature/ar-1388-runtime-authority-materializer",
  "checkpoint_commit": "25548846966e37646dded8d67ed8ee5123b8bc32",
  "claim_expires": "",
  "depends_on": [
    "AR-1385",
    "AR-1384",
    "AR-1378",
    "AR-1377"
  ],
  "id": "AR-1388",
  "next_action": "Refresh the declared isolated worktree from protected main, implement the production runtime authority materializer from authenticated receipt/chain into private bootstrap inputs, and add fail-closed tests.",
  "observed_branch": "feature/ar-1388-runtime-authority-materializer",
  "observed_dirty": 0,
  "observed_head": "25548846966e37646dded8d67ed8ee5123b8bc32",
  "owner": "",
  "plan": "../plans/AR-1388-runtime-authority-materializer.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "open",
  "summary": "Materialize runtime-owned provider authority from authenticated receipt and chain state.",
  "task_revision": 2,
  "title": "Runtime authority receipt materializer",
  "updated_at": "2026-09-24T06:40:16+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1388-runtime-authority-materializer"
}
---

This repair supplies the missing production-owned conversion from the
authenticated receipt/chain to private bootstrap authority. It must never
accept caller-supplied policy, allowlists, credentials, roots, tools,
namespace identity, or launch tokens.


- 2026-09-24T06:40:16+00:00: AR-1387 audit found missing receipt-chain to private bootstrap
  constructor; dependencies verified
