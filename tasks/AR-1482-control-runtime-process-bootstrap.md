---
{
  "branch": "feature/ar-1482-control-runtime-process-bootstrap",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-29T11:05:15+00:00",
  "depends_on": [
    "AR-1472",
    "AR-1473",
    "AR-1480"
  ],
  "id": "AR-1482",
  "next_action": "Promote and claim, then inspect control/runtime process bootstrap APIs on protected main.",
  "observed_branch": "feature/ar-1482-control-runtime-process-bootstrap",
  "observed_dirty": 0,
  "observed_head": "fdc7f59f83f647ce099439b003848291e81dd3bb",
  "owner": "ar1482-bootstrap-luna56",
  "plan": "../plans/AR-1482-control-runtime-process-bootstrap.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Compose authenticated control enrollment into the ordinary CLI process bootstrap.",
  "task_revision": 10,
  "title": "Control-runtime process bootstrap",
  "updated_at": "2026-09-29T10:35:18+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1482-control-runtime-process-bootstrap"
}
---

Narrow successor to AR-1481. It owns only process-level composition over the
completed opaque-source contracts and must not modify asb-tui, require live
providers, accept caller-built authority, or weaken fail-closed boundaries.


- 2026-09-27T12:03:27+00:00: Narrow process-bootstrap successor to blocked AR-1481. Depends only on
  completed AR-1472, AR-1473, and AR-1480; provides authenticated receipt/chain to opaque normal CLI
  dispatch without AR-1374/1375.

- 2026-09-27T12:03:29+00:00: Claimed by ar1332-record-replay-luna56.

- 2026-09-27T12:04:15+00:00: Recorded command exit 0; command argv SHA-256
  9db94754ecef5e87fe72a8fe92c43c909ec3e90e5c6e6b2dcce52758a9dca08e.

- 2026-09-27T12:04:45+00:00: AR-1482 bounded protected-main audit at
  fdc7f59f83f647ce099439b003848291e81dd3bb: runtime exposes request_control_receipt and
  materialize_control_receipt_profile, but both require caller-supplied ControlClient/receipt-chain
  inputs; private materialize_handle and resolver methods remain pub(crate). asb-cli entry/run still
  dispatch with None,None, and only existing control commands accept explicit socket paths. No
  process-owned bootstrap owns the control session, certificate-chain store, authority resolver,
  private launch inputs, cancellation or teardown binding. Worktree clean; no safe product change
  without fabricating authority or exposing caller/config inputs. Next action: define and implement
  the authenticated control-runtime process owner/launcher that supplies these opaque inputs, then
  wire AR-1480 seam and qualify local/mock/replay.

- 2026-09-29T10:32:19+00:00: Dependencies AR-1472, AR-1473 and AR-1480 are done; start the narrow
  process-owned control bootstrap successor identified by the prior protected-main audit.

- 2026-09-29T10:32:22+00:00: Claimed by ar1482-bootstrap-luna56.

- 2026-09-29T10:35:15+00:00: Heartbeat by ar1482-bootstrap-luna56.

- 2026-09-29T10:35:18+00:00: Initial protected-main inspection: isolated worktree exact checkpoint
  fdc7f59 (AR-1480 merge); runtime has receipt/chain APIs and opaque source seam but no
  process-owned authenticated session/bootstrap. Refresh and safe owner slice pending.
