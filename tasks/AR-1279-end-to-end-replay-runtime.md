---
{
  "branch": "feature/ar-1279-end-to-end-replay-runtime",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1237",
    "AR-1238",
    "AR-1239"
  ],
  "id": "AR-1279",
  "next_action": "Promote after dependency verification; implement transport plus primary runtime-client handoff from protected main and prove full supervised lifecycle.",
  "observed_branch": "feature/ar-1279-end-to-end-replay-runtime",
  "observed_dirty": 0,
  "observed_head": "69e8b064d3121a4bae1f672cdae9c0c8672000bc",
  "owner": "",
  "plan": "../plans/AR-1279.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "blocked",
  "summary": "Implement end-to-end runtime-owned execution for primary strict replay.",
  "task_revision": 6,
  "title": "End-to-end primary replay runtime handoff",
  "updated_at": "2026-09-17T00:12:15+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1279-end-to-end-replay-runtime"
}
---

## AR-1279

Implement transport and primary runtime-client handoff end to end from protected main. Preserve
AR-1275 through AR-1278 blocked evidence and require real supervised cassette lifecycle proof.

- 2026-09-17T00:10:47+00:00: Dependencies AR-1237, AR-1238, and AR-1239 are done. AR-1275 through
  AR-1278 are blocked evidence only; implement transport and primary runtime-client handoff together
  from protected main.

- 2026-09-17T00:11:08+00:00: Claimed by asb_ar1024_lifecycle_router.

- 2026-09-17T00:11:38+00:00: Recorded command exit 0; command argv SHA-256
  548854c3c7b1ea753090aa5cb6bc65d48cb545a055b82ef3a11123b697c41fcb.

- 2026-09-17T00:12:15+00:00: Released blocked/ownerless after exact protected-main audit; no product
  mutation. Correct declared worktree was provisioned and audited. Current origin/main exposes
  SidecarHandoff and scheduler/process APIs, but no runtime-to-CLI transport/client contract.
  asb-cli run/dispatch/replay remains argument-only (cassette path, provider profile, agent,
  stdout). End-to-end authenticated primary replay cannot be added safely without a new reviewed
  cross-crate transport/process entrypoint; fabricating a client or authority would violate
  fail-closed requirements. Supervised cassette response, provider/descendant egress denial,
  no-fallback, cancellation/restart/timeout/crash reaping, cleanup, and malformed/stale/duplicate
  evidence remain blocked.
