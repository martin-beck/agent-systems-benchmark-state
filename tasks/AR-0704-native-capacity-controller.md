---
{
  "branch": "feature/native-capacity-controller",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-09T15:11:42+00:00",
  "depends_on": [
    "AR-0701",
    "AR-0103"
  ],
  "id": "AR-0704",
  "next_action": "Define authorized reservation, provisioning, teardown, privacy, cost, and evidence control for genuine native cells.",
  "owner": "contracts_20260906",
  "plan": "../plans/AR-0704.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Control genuine native platform capacity lifecycle.",
  "task_revision": 4,
  "title": "Control native capacity lifecycle",
  "updated_at": "2026-09-09T12:12:56+00:00",
  "worktree_key": "agent-systems-benchmark-native-capacity-controller"
}
---
## AR-0704

Define the credential-isolated reservation/provision/teardown controller for genuine Debian and
openEuler native x86_64 cells on the authorized development host, including local resource
ceilings, availability, privacy, boot identity, and evidence. No emulation or container
substitution satisfies the native x86_64 claim. Native ARM64 is optional future evidence and
must not block this AR or its dependents.

- 2026-09-09T12:11:35+00:00: Explicit authorization received for development-host lifecycle control:
  use existing x86_64 development capacity and keep AArch64 portability under AR-0702; no external
  provider provisioning, emulated-native substitution, or cost-bearing capacity claim. Dependencies
  AR-0701 and AR-0103 are durably done and the control-policy paths are disjoint from active AR-0702
  qualification paths.

- 2026-09-09T12:11:42+00:00: Claimed by contracts_20260906.

- 2026-09-09T12:12:56+00:00: Recorded command exit 0; command argv SHA-256
  5345cd4b5f66285dc80cddfe59c0a95475263f9ff88d25d2639fce3c300aa4b9.
