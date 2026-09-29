---
{
  "branch": "feature/ar-1506-runtime-platform-launcher-integration",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-29T03:50:37+00:00",
  "depends_on": [
    "AR-1473",
    "AR-1474",
    "AR-1480",
    "AR-1484",
    "AR-1485",
    "AR-1502",
    "AR-1505"
  ],
  "id": "AR-1506",
  "next_action": "Implement runtime-owned platform launcher adapter and wire ordinary CLI run/sweep to an opaque authenticated dispatch source; add provider-free lifecycle negatives.",
  "observed_branch": "feature/ar-1506-runtime-platform-launcher-integration",
  "observed_dirty": 1,
  "observed_head": "c9f5c1890434b8980d29ebb64823032cf0cd3e52",
  "owner": "ar1506-launcher-luna56",
  "plan": "../plans/AR-1506-runtime-platform-launcher-integration.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Connect the merged authenticated platform authority/bootstrap protocol to production ASB process startup and ordinary CLI dispatch.",
  "task_revision": 34,
  "title": "Runtime platform launcher integration",
  "updated_at": "2026-09-29T02:03:25+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1506-runtime-platform-launcher-integration"
}
---

AR-1503 and AR-1504 established the missing process-owner and platform-launcher gaps but
could not safely complete them before an authenticated platform bootstrap contract existed.
AR-1505 now provides that contract and is merged with full post-merge assurance. This AR
owns the narrow production integration slice that remains.

Acceptance requires:

- a runtime-owned, authenticated session/launcher that consumes only the AR-1505 bootstrap
  authority and never accepts caller/config/socket/chain/credential/policy/root/tool authority;
- ordinary `asb-cli` process startup and `run`/`sweep` dispatch to receive only an opaque,
  runtime-issued live dispatch source, with no `None,None` production fallback;
- lifecycle binding for cancellation, teardown, restart, expiry, revocation, and egress denial,
  with deterministic local/mock/replay tests for positive and every negative path;
- no live provider or external credential requirement for development or CI qualification;
- independent exact-head review, SSH-signed DCO commit, all hosted checks, protected merge,
  and terminal post-merge assurance on the exact resulting main SHA.

Non-goals: asb-tui changes, live OpenRouter/provider reachability, caller-built authority,
synthetic trust, weakening fail-closed behavior, or treating a mock fixture as first-customer
production evidence.

- 2026-09-29T03:46:10+02:00: Created as the narrow successor to the historical AR-1503/1504
  process-owner and launcher audits. AR-1505 merged at f92c2e941913129d7db50480f71e8361a0d43a0c,
  supplying the authenticated platform bootstrap contract required to implement this integration.

- 2026-09-29T01:47:30+00:00: Dependencies AR-1473, AR-1474, AR-1480, AR-1484, AR-1485, AR-1502, and
  AR-1505 verified done; begin production launcher integration.

- 2026-09-29T01:48:47+00:00: Claimed by ar1506-launcher-luna56.

- 2026-09-29T01:49:03+00:00: Recorded command exit 0; command argv SHA-256
  f5a589cdf7ff0b0c4aa322d6e6d65fbb05fd91306ad84af64030c0948de4ef59.

- 2026-09-29T01:49:24+00:00: Recorded command exit 0; command argv SHA-256
  74ff01ba28103f690eb7c2870d36904314cf4092a1552591485fbdd51070fdb3.

- 2026-09-29T01:49:46+00:00: Heartbeat by ar1506-launcher-luna56.

- 2026-09-29T01:50:17+00:00: Recorded command exit 0; command argv SHA-256
  dc5ebf535411dc42d472f682a12a9ba0252bc0d485f848f5f92054856a43bc83.

- 2026-09-29T01:50:37+00:00: Heartbeat by ar1506-launcher-luna56.

- 2026-09-29T01:50:44+00:00: Recorded command exit 0; command argv SHA-256
  5345cd4b5f66285dc80cddfe59c0a95475263f9ff88d25d2639fce3c300aa4b9.

- 2026-09-29T01:51:07+00:00: Recorded command exit 0; command argv SHA-256
  f9e58004e68bbe6dbe53beccbe5bb05ce78bc92eeadfbfc27796188aead36608.

- 2026-09-29T01:53:05+00:00: Audit: isolated product worktree
  agent-systems-benchmark-ar-1506-runtime-platform-launcher-integration is clean at exact AR-1505
  merge f92c2e941913129d7db50480f71e8361a0d43a0c. AR-1505 bootstrap/chain/receipt and opaque
  dispatch APIs are present, but asb-cli::run still dispatches with None,None and no runtime
  platform adapter consumes RuntimeControlBootstrap. Next action is the narrow adapter/wiring slice.

- 2026-09-29T01:54:46+00:00: Recorded command exit 0; command argv SHA-256
  b945362378f77f64a68eb9e8d400e693e008357f0cc0d69f7bfe3bb93e47ae02.

- 2026-09-29T01:56:33+00:00: Recorded command exit 101; command argv SHA-256
  ddd1f81564413ac090ce5391ffdd3806d437cd5c6a31734f8b6d6acfbba3bf48.

- 2026-09-29T01:56:52+00:00: Recorded command exit 0; command argv SHA-256
  ddd1f81564413ac090ce5391ffdd3806d437cd5c6a31734f8b6d6acfbba3bf48.

- 2026-09-29T01:57:29+00:00: Recorded command exit 0; command argv SHA-256
  ddd1f81564413ac090ce5391ffdd3806d437cd5c6a31734f8b6d6acfbba3bf48.

- 2026-09-29T01:57:47+00:00: Recorded command exit 1; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-29T01:58:09+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-29T01:58:32+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-29T01:58:49+00:00: Recorded command exit 0; command argv SHA-256
  73d005d4c4983870f0c5405c6c97dffbf521d57825b14d75dae888988fbdcd03.

- 2026-09-29T01:59:26+00:00: Recorded command exit 0; command argv SHA-256
  3d4cc54827fa0ae5c402321266e4a8e9a84a69a17f7ff27b7a0f0c858d454784.

- 2026-09-29T01:59:46+00:00: Recorded command exit 0; command argv SHA-256
  7c730eec3ea71bd24ffc5a9255bf7f542481bf601dba6c72bed6e00f6c2fab3c.

- 2026-09-29T02:00:10+00:00: Recorded command exit 0; command argv SHA-256
  683e8c15b7355ad23b78cf01e6e81e7e58087dd22d1cec275ef269ffd93b62e8.

- 2026-09-29T02:00:32+00:00: Recorded command exit 0; command argv SHA-256
  1b72418411d924a469e5112c6699964f1a1c519a30b6f3b5ea29b9bab5d58138.

- 2026-09-29T02:00:56+00:00: Recorded command exit 0; command argv SHA-256
  ff5912fa56b5f3988afeeec6bf95c92437b31658fa4570bc50e4e1d13b166a44.

- 2026-09-29T02:01:13+00:00: Recorded command exit 0; command argv SHA-256
  ff6d1fa7a7185010f75fcfafe4bdc1bdd5b9804d8c2b3e7abdd8a1b96cd81c63.

- 2026-09-29T02:01:33+00:00: Recorded command exit 0; command argv SHA-256
  303743579b82a79e6a9829b0423d0b1c8ae7e59d13feb387d976ed7f6ae316f7.

- 2026-09-29T02:02:53+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-29T02:03:25+00:00: Recorded command exit 0; command argv SHA-256
  3d4cc54827fa0ae5c402321266e4a8e9a84a69a17f7ff27b7a0f0c858d454784.
