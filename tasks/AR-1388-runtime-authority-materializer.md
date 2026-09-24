---
{
  "branch": "feature/ar-1388-runtime-authority-materializer",
  "checkpoint_commit": "581847921990c064b5185a9e66a788a474ffcc33",
  "claim_expires": "2026-09-24T07:41:06+00:00",
  "depends_on": [
    "AR-1385",
    "AR-1384",
    "AR-1378",
    "AR-1377"
  ],
  "id": "AR-1388",
  "next_action": "Publish exact-head signed+DCO PR for 581847921990c064b5185a9e66a788a474ffcc33, monitor CI, and complete post-merge gates.",
  "observed_branch": "feature/ar-1388-runtime-authority-materializer",
  "observed_dirty": 0,
  "observed_head": "581847921990c064b5185a9e66a788a474ffcc33",
  "owner": "codex-asb-ar1329-repair-luna56",
  "plan": "../plans/AR-1388-runtime-authority-materializer.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Materialize runtime-owned provider authority from authenticated receipt and chain state.",
  "task_revision": 17,
  "title": "Runtime authority receipt materializer",
  "updated_at": "2026-09-24T06:48:44+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1388-runtime-authority-materializer"
}
---

This repair supplies the missing production-owned conversion from the
authenticated receipt/chain to private bootstrap authority. It must never
accept caller-supplied policy, allowlists, credentials, roots, tools,
namespace identity, or launch tokens.


- 2026-09-24T06:40:16+00:00: AR-1387 audit found missing receipt-chain to private bootstrap
  constructor; dependencies verified

- 2026-09-24T06:41:03+00:00: Claimed by codex-asb-ar1329-repair-luna56.

- 2026-09-24T06:41:06+00:00: Heartbeat by codex-asb-ar1329-repair-luna56.

- 2026-09-24T06:43:47+00:00: Recorded command exit 1; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-24T06:44:06+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-24T06:44:37+00:00: Recorded command exit 101; command argv SHA-256
  f02c88e5bb416ce21eb0daa1fccdd1b97d4e98bb871cd94c90ae89cf45f701db.

- 2026-09-24T06:45:38+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-24T06:45:54+00:00: Recorded command exit 0; command argv SHA-256
  f02c88e5bb416ce21eb0daa1fccdd1b97d4e98bb871cd94c90ae89cf45f701db.

- 2026-09-24T06:47:11+00:00: Recorded command exit 0; command argv SHA-256
  af984e70f12afab3393413bd30419e79ffad9c88b69d3c5c0407ee30a211c494.

- 2026-09-24T06:47:33+00:00: Recorded command exit 0; command argv SHA-256
  928f94f912f52fad0d749b7d88488bcc0ee958c31e9b017b830db7e0679e951b.

- 2026-09-24T06:47:47+00:00: Recorded command exit 0; command argv SHA-256
  951ff1fedeb660a7044895dea700f65b853127ba0560ab5d1b926787eac06433.

- 2026-09-24T06:48:33+00:00: Implemented runtime-owned receipt-to-opaque-profile materializer with
  one-shot replay/tamper tests. Tightened control/runtime receipt nonce binding to credential, tool,
  lease, and relay digests. Focused runtime/control tests and repository policy pass; commit is
  SSH-signed with matching DCO. External provider remains unnecessary; tests are local
  deterministic.

- 2026-09-24T06:48:44+00:00: Recorded command exit 0; command argv SHA-256
  bab5eadef9f3f52491de83019527292da0e05b35873d8f4a414d102081573f8a.
