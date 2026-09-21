---
{
  "branch": "feature/ar-1324-auth-helper-control-contract",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [],
  "id": "AR-1324",
  "next_action": "Add a versioned helper-discovery/invocation control operation backed by the existing sealed CredentialBackend; return only bounded typed receipt/status data.",
  "owner": "",
  "plan": "../plans/AR-1324.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Own the ASB control and runner backend for safe credential-helper invocation.",
  "task_revision": 1,
  "title": "Authenticated credential-helper control contract",
  "updated_at": "2026-09-21T03:42:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1324-auth-helper-control-contract"
}
---

AR-1323 owns the asb-tui user journey, but the runner must own helper
discovery, executable identity, timeout/cancellation, generation fencing and
secret resolution. This AR adds the versioned ASB control schema and backend
integration using the existing sealed helper implementation. The frontend must
never receive a raw credential or execute an arbitrary path.
