---
{
  "branch": "feature/ar-1353-runtime-enrollment-cli-dispatch",
  "checkpoint_commit": "d83a85926f2c4c42317617f4f6b7b3c9a3195874",
  "claim_expires": "",
  "depends_on": [
    "AR-1352"
  ],
  "id": "AR-1353",
  "next_action": "Wire asb-cli run/sweep to acquire through LiveProviderRuntimeService::acquire_from_enrollment, using a runtime-only enrollment implementation that mints the opaque handle; remove the production requirement for caller-injected LiveProviderAttemptFactory. Add positive/negative dispatch and offline/replay tests, then run full gates.",
  "observed_branch": "feature/ar-1353-runtime-enrollment-cli-dispatch",
  "observed_dirty": 0,
  "observed_head": "d83a85926f2c4c42317617f4f6b7b3c9a3195874",
  "owner": "",
  "plan": "../plans/AR-1353-runtime-enrollment-cli-dispatch.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "superseded",
  "summary": "Add runtime-owned enrollment and opaque live CLI dispatch.",
  "task_revision": 16,
  "title": "Runtime enrollment and CLI dispatch",
  "updated_at": "2026-09-23T20:53:19+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1353-runtime-enrollment-cli-dispatch"
}
---

Successor repair for AR-1349's exact remaining gap: AR-1352 bootstrap is
private and tested, but no safe cross-crate enrollment source delivers its
opaque handle to asb-cli. AR-1349 checkpoint and evidence remain preserved;
AR-1329 stays fail-closed until this seam is merged.

- 2026-09-23T20:47:37+00:00: AR-1352 is merged and supplies the private bootstrap. Promote this
  downstream enrollment/CLI dispatch repair; AR-1349 and AR-1329 remain fail-closed consumers.

- 2026-09-23T20:47:51+00:00: Claimed by codex-asb-ar1329-live-cli-luna56.

- 2026-09-23T20:48:08+00:00: Recorded command exit 0; command argv SHA-256
  589e2ee0b49b9b295694812f8163f3a74ad9aa8aadea9279d8a99555e676994f.

- 2026-09-23T20:48:28+00:00: Recorded command exit 0; command argv SHA-256
  7ac89627b5c72731bb3d8bca3baa4957712f574223322264931f0d213dad0070.

- 2026-09-23T20:49:04+00:00: Recorded command exit 0; command argv SHA-256
  f204ba5882f7d182e4967055864a0241f63455c29baf9adecb87d8076a507971.

- 2026-09-23T20:49:23+00:00: Recorded command exit 0; command argv SHA-256
  955509a954964b88b573f399cb0ea8000cf8cdb7ab13e4197cd1005c790e7596.

- 2026-09-23T20:49:54+00:00: Signed commit d83a859 adds LiveProviderEnrollment and
  acquire_from_enrollment; only opaque LiveProviderRuntimeHandle crosses the crate boundary and
  enrollment failures are bounded. Runtime fmt/clippy passed. CLI production dispatch is still
  pending; AR-1329 remains fail-closed.

- 2026-09-23T20:52:22+00:00: Recorded command exit 0; command argv SHA-256
  68deeb379d19ea6dd1e8937391644bfe136f229825dd13a88e34e09753be9034.

- 2026-09-23T20:52:42+00:00: Recorded command exit 0; command argv SHA-256
  357f561df703edbaea3dbc0f5a1cd3d36b645510936614ab4595d52375c7f9db.

- 2026-09-23T20:52:56+00:00: Recorded command exit 0; command argv SHA-256
  00f92e563be4ae2ec0a94b2819759b596eeb35083e15fe9ae043ae6391fb8862.

- 2026-09-23T20:53:19+00:00: Superseded by AR-1354, which owns the missing config-backed enrollment
  implementation. Preserve signed opaque transport commit d83a859 and AR-1329 fail-closed status.

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
