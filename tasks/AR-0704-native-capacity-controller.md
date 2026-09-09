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
  "observed_branch": "feature/native-capacity-controller",
  "observed_dirty": 2,
  "observed_head": "b6d04a8305ce6d49cc327e4e6d2d6fa42a88050b",
  "owner": "contracts_20260906",
  "plan": "../plans/AR-0704.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Control genuine native platform capacity lifecycle.",
  "task_revision": 10,
  "title": "Control native capacity lifecycle",
  "updated_at": "2026-09-09T12:17:13+00:00",
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

- 2026-09-09T12:13:04+00:00: Recorded command exit 0; command argv SHA-256
  c107569e774896d4dc2c977d011e1a56b9a47d6f8f4f9d1193cb71e139ba20f9.

- 2026-09-09T12:16:18+00:00: Recorded command exit 0; command argv SHA-256
  52fd83c7899d290fc71d2d2d53dd973b3a98a4458397bc437c2b928999700371.

- 2026-09-09T12:16:55+00:00: Recorded command exit 1; command argv SHA-256
  5fb36337b427a59e04ba695cfeb9b4c6f76b92b6a3b6b9d795eeb474b3425af5.

- 2026-09-09T12:17:13+00:00: Recorded command exit 0; command argv SHA-256
  cf516be0d775d0d75952f479dd98da416ebafb57c63cefd7cfc80c821c636266.
