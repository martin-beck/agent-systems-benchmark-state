---
{
  "branch": "feature/ar-1324-auth-helper-control-contract",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-21T05:31:23+00:00",
  "depends_on": [],
  "id": "AR-1324",
  "next_action": "Add a versioned helper-discovery/invocation control operation backed by the existing sealed CredentialBackend; return only bounded typed receipt/status data.",
  "owner": "codex-ar1324",
  "plan": "../plans/AR-1324.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Own the ASB control and runner backend for safe credential-helper invocation.",
  "task_revision": 4,
  "title": "Authenticated credential-helper control contract",
  "updated_at": "2026-09-21T03:31:23+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1324-auth-helper-control-contract"
}
---

AR-1323 owns the asb-tui user journey, but the runner must own helper
discovery, executable identity, timeout/cancellation, generation fencing and
secret resolution. This AR adds the versioned ASB control schema and backend
integration using the existing sealed helper implementation. The frontend must
never receive a raw credential or execute an arbitrary path.

- 2026-09-21T03:27:36+00:00: AR-1322 exact-main post-merge gates are green; open the runner-owned
  helper contract slice.

- 2026-09-21T03:27:39+00:00: Claimed by codex-ar1324.

- 2026-09-21T03:31:23+00:00: Heartbeat by codex-ar1324.
