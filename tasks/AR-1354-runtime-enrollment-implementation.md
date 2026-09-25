---
{
  "branch": "feature/ar-1354-runtime-enrollment-implementation",
  "checkpoint_commit": "d83a85926f2c4c42317617f4f6b7b3c9a3195874",
  "claim_expires": "",
  "depends_on": [
    "AR-1352"
  ],
  "id": "AR-1354",
  "next_action": "BLOCKED on an attested runtime enrollment source: asb-runtime must receive an authority-free enrollment request and obtain concrete public target(s), pinned tool attestations, lease root, and relay root from a runtime/control-owned record; do not expose these asb-cli inputs. Add a signed/attested record transport or coordinator-owned runtime enrollment AR, then implement acquire_from_enrollment and CLI dispatch with positive/negative tests.",
  "observed_branch": "feature/ar-1354-runtime-enrollment-implementation",
  "observed_dirty": 0,
  "observed_head": "d83a85926f2c4c42317617f4f6b7b3c9a3195874",
  "owner": "",
  "plan": "../plans/AR-1354-runtime-enrollment-implementation.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "blocked",
  "summary": "Implement config-backed runtime-owned enrollment for live CLI dispatch.",
  "task_revision": 10,
  "title": "Runtime enrollment implementation",
  "updated_at": "2026-09-23T21:01:36+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1354-runtime-enrollment-implementation"
}
---

Successor for AR-1353's exact missing implementation: the opaque enrollment
transport exists, but no config/control source can safely mint its handle.
AR-1353 remains evidence and is superseded only after this dependency is
durably promoted; AR-1329 remains fail-closed.

- 2026-09-23T20:55:39+00:00: Coordinator repaired stale superseded dependency edge: AR-1353
  transport evidence remains preserved, while AR-1354 now depends directly on merged AR-1352.
  Promote config-backed enrollment implementation; AR-1329 remains fail-closed.

- 2026-09-23T20:55:44+00:00: Claimed by codex-asb-ar1329-live-cli-luna56.

- 2026-09-23T20:56:52+00:00: Heartbeat by codex-asb-ar1329-live-cli-luna56.

- 2026-09-23T20:57:31+00:00: Recorded command exit 0; command argv SHA-256
  23fe83917a1f1717a8a94f9b6f08b545aeed4dbc52f65efb375cd87b979ef9f8.

- 2026-09-23T20:59:35+00:00: Recovered after heartbeat-only stall with no product diff; preserve
  AR-1354 scope and reassign to replacement gpt-5.6-luna worker.

- 2026-09-23T20:59:43+00:00: Claimed by codex-asb-runtime-acquisition-successor-luna56.

- 2026-09-23T21:00:14+00:00: Read-only architecture audit completed. Existing LiveProviderEnrollment
  can return only an opaque handle, while LiveProviderBootstrapSpec and LiveProviderProvisioner::new
  are crate-private. asb-cli has only OpenRouter config/selection digests, no attested
  target/tool/root authority. Exposing a constructor or accepting paths/targets from CLI would
  violate the AR and fail-closed boundary, so no product diff was made.

- 2026-09-23T21:01:36+00:00: Released blocked with evidence: no attested runtime/control-owned
  enrollment record can currently supply concrete target/tool/lease/relay authority without exposing
  caller-controlled launch inputs. Successor AR-1355 created for the missing transport and
  acceptance tests; AR-1329 remains fail-closed.

## Current development and CI qualification boundary

The mandatory development and CI qualification path for this AR is a deterministic
local provider/LLM mock (LiteLLM-compatible where practical), including hostile
negative tests and offline replay where applicable. External/live OpenRouter or
other provider reachability is optional supplementary evidence only; it is never a
completion, dependency-readiness, or CI gate. Production egress policy, credential
non-disclosure, runtime-owned authority, namespace/relay attestation, cancellation
and teardown, and fail-closed denial of unapproved external traffic remain required
contracts. Existing live-provider dependency edges describe production integration
ordering only and must not be used to block local qualification or to claim external
reachability.
