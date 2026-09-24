---
{
  "branch": "feature/ar-1391-runtime-control-bootstrap-constructor",
  "checkpoint_commit": "10bffbf015bd7ca78d8c0d18f04cf0190195e933",
  "claim_expires": "",
  "depends_on": [
    "AR-1388",
    "AR-1385",
    "AR-1373",
    "AR-1366",
    "AR-1341",
    "AR-1342",
    "AR-1339",
    "AR-1340"
  ],
  "id": "AR-1391",
  "next_action": "Claim the pre-bound isolated worktree, implement the runtime/control-owned authenticated bootstrap constructor, and publish a signed PR.",
  "observed_branch": "feature/ar-1391-runtime-control-bootstrap-constructor",
  "observed_dirty": 0,
  "observed_head": "10bffbf015bd7ca78d8c0d18f04cf0190195e933",
  "owner": "",
  "plan": "../plans/AR-1391-runtime-control-bootstrap-constructor.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "blocked",
  "summary": "Materialize authenticated runtime live authority into an opaque source without caller injection.",
  "task_revision": 4,
  "title": "Runtime control bootstrap constructor",
  "updated_at": "2026-09-24T07:44:12+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1391-runtime-control-bootstrap-constructor"
}
---

This narrow successor owns the missing authority source identified by the
AR-1390 audit. It must not touch asb-tui, synthesize authority, or require an
external provider connection for development or CI.

- 2026-09-24T07:42:41+00:00: Runtime authority dependencies verified; AR-1390 audit identified this
  exact missing authenticated constructor.

- 2026-09-24T07:43:46+00:00: Claimed by codex-asb-ar1329-repair-luna56.

- 2026-09-24T07:44:12+00:00: Protected-main audit confirms no production runtime/control-owned
  bootstrap constructor exists. asb-cli RuntimeAuthorityRecord and RuntimeReceipt expose only
  authenticated digest metadata; no resolver supplies private lease/relay roots, egress
  policy/allowlist, pinned tools, namespace identity, credential capability, or teardown authority.
  Existing LiveProviderRuntimeBootstrapSpec::from_enrollment and materialize_handle are
  crate-private and require caller-supplied private inputs; existing CLI source bridge accepts
  externally injected opaque source. Implementing a facade would violate acceptance and fabricate
  authority. Worktree remains clean at checkpoint 10bffbf015bd7ca78d8c0d18f04cf0190195e933; no PR
  published.
