---
{
  "branch": "feature/ar-1346-runtime-supervisor-provisioning",
  "checkpoint_commit": "a336d6744b1a82f36a706ec606b847c92d49cfd3",
  "claim_expires": "",
  "depends_on": [
    "AR-1327",
    "AR-1328",
    "AR-1339",
    "AR-1340"
  ],
  "id": "AR-1346",
  "next_action": "Cross-crate audit found the safe boundary is not yet implemented: asb-runtime cannot depend on asb-agents because asb-agents already depends on runtime; ResolvedCredential transport bytes are crate-private, while SandboxBackend::spawn_launch constructs the child command internally. Implement a new supervisor-owned composition boundary (likely dedicated crate or runtime credential injection trait) that keeps secret bytes opaque, then add CLI wiring/tests. Do not expose bytes or bypass NetworkPolicy::Deny.",
  "observed_branch": "feature/ar-1346-runtime-supervisor-provisioning",
  "observed_dirty": 0,
  "observed_head": "a336d6744b1a82f36a706ec606b847c92d49cfd3",
  "owner": "",
  "plan": "../plans/AR-1346-runtime-supervisor-provisioning.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "superseded",
  "summary": "Add the production runtime supervisor boundary needed for safe live-provider CLI acquisition.",
  "task_revision": 9,
  "title": "Runtime supervisor provisioning boundary",
  "updated_at": "2026-09-23T15:37:14+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1346-runtime-supervisor-provisioning"
}
---

Created from the AR-1343 runtime audit. Existing runtime constructors are
test-only or unrelated, and `ResolvedCredential` transport is crate-private to
`asb-agents`; do not bridge this by exposing secrets or constructing synthetic
authority in `asb-cli`.


- 2026-09-23T15:32:48+00:00: Promote coordinator-created cross-crate runtime provisioning repair;
  dependencies are complete and AR-1329 is fail-closed pending this capability.

- 2026-09-23T15:32:51+00:00: Claimed by codex-asb-ar1329-live-cli-luna56.

- 2026-09-23T15:34:50+00:00: Heartbeat by codex-asb-ar1329-live-cli-luna56.

- 2026-09-23T15:35:39+00:00: Created isolated AR-1346 worktree at protected main a336d674 (manual
  git worktree creation was required because handoffctl validates an existing bound checkout).
  Inspected complete plan and APIs: credential resolution lives in asb-agents, runtime owns sandbox
  spawn, and the dependency direction prevents a direct runtime-to-agents implementation. No product
  mutation yet; AR-1329 remains fail-closed.

- 2026-09-23T15:36:31+00:00: Recorded command exit 0; command argv SHA-256
  75b98f3973a45dbe5611256aa534052c1e865a9242686554a86a8cea97c42e36.

- 2026-09-23T15:36:45+00:00: Recorded command exit 0; command argv SHA-256
  3928acedfc6d32e05c47078243c49c051c41ef0d31a7e2f3ad132499cc00daa8.

- 2026-09-23T15:37:00+00:00: Recorded command exit 0; command argv SHA-256
  23b2cad55d063096f1db1ccc3f3d836e4b2a7b710b948912fa96bcb9825162c3.

- 2026-09-23T15:37:14+00:00: AR-1346 audit completed without product mutation. It proved the missing
  safe primitive is a neutral opaque supervisor/credential composition contract: asb-agents already
  depends on asb-runtime and ResolvedCredential bytes are crate-private. Superseded by AR-1347;
  preserve AR-1329 fail-closed.

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
