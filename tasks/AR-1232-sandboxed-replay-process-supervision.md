---
{
  "branch": "feature/ar-1232",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-16T04:17:29+00:00",
  "depends_on": [
    "AR-0505",
    "AR-1100",
    "AR-1230"
  ],
  "id": "AR-1232",
  "next_action": "Implement the approved SandboxBackend process-supervision seam for strict replay, including real child egress denial and bounded cancellation/restart/crash recovery tests.",
  "observed_branch": "feature/ar-1232",
  "observed_dirty": 1,
  "observed_head": "a83ba8e278e40b538160e87a2a40c0fb26418dae",
  "owner": "asb_ar1232_sandbox_supervision",
  "plan": "../plans/AR-1232.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Supervise strict replay adapters inside the approved network-denied sandbox.",
  "task_revision": 12,
  "title": "Sandboxed replay process supervision",
  "updated_at": "2026-09-16T02:17:42+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1232"
}
---

- 2026-09-16T02:15:00+00:00: Created from AR-1231 review. AR-1231 provides the typed launch,
  route identity, endpoint policy, and capability contract; runtime child-process supervision and
  descendant egress proof require this separate implementation slice.

- 2026-09-16T02:14:38+00:00: Dependencies AR-0505, AR-1100 and AR-1230 are done; promote runtime
  process supervision.

- 2026-09-16T02:14:41+00:00: Claimed by asb_ar1232_sandbox_supervision.

- 2026-09-16T02:14:50+00:00: Recorded command exit 0; command argv SHA-256
  1c610d376f7e1941d69ba01298d4d9058ff38ae02a75c57f0f3963898a2c5334.

- 2026-09-16T02:16:52+00:00: Recorded command exit 0; command argv SHA-256
  0e3a40974437308cca16cde6e840d4d4136393a7a84525b667a7fcccac25615d.

- 2026-09-16T02:17:03+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T02:17:15+00:00: Recorded command exit 0; command argv SHA-256
  f74a62509d6400c77ce136d5b2349650a531f6ca635497361874995702247188.

- 2026-09-16T02:17:29+00:00: Heartbeat by asb_ar1232_sandbox_supervision.

- 2026-09-16T02:17:33+00:00: Recorded command exit 0; command argv SHA-256
  f71975b0e0b00a780fed3410ff70f306b8004ce22f8d1aecc438b8adc79fe8e9.

- 2026-09-16T02:17:42+00:00: Recorded command exit 0; command argv SHA-256
  ab2543495dcc50f7aceea8a1460a8aa5f1e9bf14a98435398770619f50c49608.
