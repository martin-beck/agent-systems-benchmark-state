---
{
  "branch": "feature/development-host-runner-reboot-lifecycle",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-0830", "AR-0832"],
  "id": "AR-0833",
  "next_action": "Design and qualify a tokenless supervisor/orchestration path that can provision fresh ephemeral registrations after boot without storing reusable GitHub credentials.",
  "owner": "",
  "plan": "../plans/AR-0833.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "planned",
  "summary": "Qualify safe reboot and restart lifecycle for disposable development-host ASB runners.",
  "task_revision": 1,
  "title": "Qualify tokenless runner reboot lifecycle",
  "updated_at": "2026-09-07T00:00:00+00:00",
  "worktree_key": "agent-systems-benchmark-development-host-runner-reboot-lifecycle"
}
---
## AR-0833

Design and qualify reboot/start/recovery for the disposable ASB development-host runner without
claiming that a consumed ephemeral registration can restart itself. Use a tokenless supervisor or
explicitly provisioned short-lived registration broker; never persist reusable GitHub credentials.

Acceptance criteria:

- Define threat model, credential boundary, boot ordering, and failure recovery.
- Prove fresh registration, exact label/identity, one-job ephemerality, deregistration, and cleanup.
- Test restart, interrupted registration, offline GitHub, power-loss simulation, and stale-state recovery.
- Preserve existing Relay listeners and pass independent security/privacy review.
- Document unsupported reboot combinations if no safe implementation is available.

Required paths: runner lifecycle scripts/services, plans/AR-0833.md, tests/runner lifecycle fixtures,
and sanitized state evidence. No host reboot is permitted without explicit authorization.
