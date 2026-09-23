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
  "next_action": "Implement the production supervisor-owned cross-crate provisioning boundary identified by AR-1343: pinned backend/live-gate discovery, benchmark ResourceLease, concrete egress allowlist, enrolled credential transport without disclosure, runtime-observed namespace rebind, launch attestation, and per-attempt relay lifecycle. Keep AR-1329 fail-closed until merged and post-merge verified.",
  "observed_branch": "feature/ar-1346-runtime-supervisor-provisioning",
  "observed_dirty": 0,
  "observed_head": "a336d6744b1a82f36a706ec606b847c92d49cfd3",
  "owner": "",
  "plan": "../plans/AR-1346-runtime-supervisor-provisioning.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "open",
  "summary": "Add the production runtime supervisor boundary needed for safe live-provider CLI acquisition.",
  "task_revision": 2,
  "title": "Runtime supervisor provisioning boundary",
  "updated_at": "2026-09-23T15:32:48+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1346-runtime-supervisor-provisioning"
}
---

Created from the AR-1343 runtime audit. Existing runtime constructors are
test-only or unrelated, and `ResolvedCredential` transport is crate-private to
`asb-agents`; do not bridge this by exposing secrets or constructing synthetic
authority in `asb-cli`.


- 2026-09-23T15:32:48+00:00: Promote coordinator-created cross-crate runtime provisioning repair;
  dependencies are complete and AR-1329 is fail-closed pending this capability.
