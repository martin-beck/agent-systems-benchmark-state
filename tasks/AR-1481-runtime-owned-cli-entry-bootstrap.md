---
{
  "branch": "feature/ar-1481-runtime-owned-cli-entry-bootstrap",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1472",
    "AR-1473",
    "AR-1480"
  ],
  "id": "AR-1481",
  "next_action": "Promote and claim, then inspect the protected-main entrypoint and runtime/control bootstrap inputs.",
  "observed_branch": "feature/ar-1481-runtime-owned-cli-entry-bootstrap",
  "observed_dirty": 0,
  "observed_head": "fdc7f59f83f647ce099439b003848291e81dd3bb",
  "owner": "",
  "plan": "../plans/AR-1481-runtime-owned-cli-entry-bootstrap.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "blocked",
  "summary": "Wire runtime-owned authenticated dispatch into the ordinary CLI entry path.",
  "task_revision": 7,
  "title": "Runtime-owned CLI entry bootstrap",
  "updated_at": "2026-09-27T12:01:35+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1481-runtime-owned-cli-entry-bootstrap"
}
---

Narrow successor to the stale/circular AR-1374 and AR-1375 chain. It owns
only process-entry composition over the completed AR-1472, AR-1473, and
AR-1480 opaque-source contracts. It must not touch asb-tui, require a live
provider, accept caller-built authority, or weaken fail-closed boundaries.


- 2026-09-27T11:59:36+00:00: Dependency-safe successor for concrete AR-1480 gap: ordinary asb-cli
  entry still dispatches with no runtime/control source. Depends only on completed AR-1472, AR-1473,
  and AR-1480; avoids circular AR-1374/1375.

- 2026-09-27T11:59:44+00:00: Claimed by ar1332-record-replay-luna56.

- 2026-09-27T12:00:17+00:00: Recorded command exit 0; command argv SHA-256
  1fc84059ed837e70b9c932779a129de0d2a6a5628085d897779904dc1235c023.

- 2026-09-27T12:00:54+00:00: Recorded command exit 0; command argv SHA-256
  fcee275835bec8e5ec624f14558cdfed6753069b2e0edb8af59f27d90de94690.

- 2026-09-27T12:01:35+00:00: AR-1481 bounded protected-main audit at
  fdc7f59f83f647ce099439b003848291e81dd3bb: asb-cli entry() calls run(), and run() still dispatches
  with None, None. AR-1480 provides only run_with_runtime_control_source(control, ...), not process
  composition. asb-runtime RuntimeOwnedEnrollmentSource, materialize_handle, and
  materialize_handle_from_resolver remain pub(crate); no control-session/bootstrap owner or public
  runtime factory transfers an opaque source to the binary. Worktree is clean; no safe in-scope
  product change exists without fabricating authority or accepting CLI/config inputs. AR-1374/1375
  remain stale/circular. Next action: create a narrow control-runtime process bootstrap successor
  supplying authenticated receipt/chain and opaque source.
